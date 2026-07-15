import re

content = open("src/recongraph/plugins/core_providers.py").read()

new_content = """from typing import Iterable, Sequence, Callable, TypeVar, Any
from dataclasses import dataclass
import datetime

from recongraph.plugins.provider import EvidenceProvider, EvidenceContribution
from recongraph.plugins.provider_v2 import EvidencePipeline, EvidenceContributionV2
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.candidate_generation.blockers import Blocker, ExactAmountBlocker, TaxIdentityBlocker, ReferenceTokenBlocker
from recongraph.matching.scoring import SignalName
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, compute_reference_interpretation
from recongraph.domain.financial.pipeline import FinancialEvidencePipeline
from recongraph.matching.signals import tax_identity_score, temporal_score

from recongraph.domain.vendor.context import VendorIdentityContext
from recongraph.domain.vendor.parser import DeterministicVendorParser
from recongraph.domain.vendor.artifact import build_vendor_observation_artifact
from recongraph.domain.vendor.interpretation import VendorPairInterpreter
from recongraph.domain.vendor.policy import VendorProjectionPolicyV1

T = TypeVar('T')

def _weakest_available(
    purchases: Sequence[PurchaseRecord],
    gsts: Sequence[GSTRecord],
    extractor: Callable[[PurchaseRecord | GSTRecord], T],
    scorer: Callable[[T, T], float | None]
) -> float | None:
    scores = []
    for p in purchases:
        p_val = extractor(p)
        for g in gsts:
            g_val = extractor(g)
            s = scorer(p_val, g_val)
            if s is not None:
                scores.append(s)
                
    if not scores:
        return None
    return min(scores)

class FinancialEvidenceProvider:
    def __init__(self, tolerance: float = 0.05):
        from decimal import Decimal
        self.pipeline = FinancialEvidencePipeline(tolerance=Decimal(str(tolerance)))
        
    def get_name(self) -> str:
        return SignalName.AMOUNT
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [ExactAmountBlocker()]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        contrib_v2 = self.pipeline.contribute(interpretation)
        return EvidenceContribution(
            provider_name=contrib_v2.provider_name,
            score=contrib_v2.score,
            violations=contrib_v2.violations,
            metadata=contrib_v2.metadata
        )

@dataclass(frozen=True)
class TemporalObservation:
    p_dates: tuple[datetime.date, ...]
    g_dates: tuple[datetime.date, ...]

class TemporalEvidencePipeline(EvidencePipeline[TemporalObservation, float | None]):
    def __init__(self, max_days: int):
        self.max_days = max_days

    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> TemporalObservation:
        return TemporalObservation(
            p_dates=tuple(p.record_date for p in purchases),
            g_dates=tuple(g.record_date for g in gsts)
        )

    def interpret(self, observation: TemporalObservation) -> float | None:
        scores = []
        for p_date in observation.p_dates:
            for g_date in observation.g_dates:
                s = temporal_score(p_date, g_date, self.max_days)
                if s is not None:
                    scores.append(s)
        if not scores:
            return None
        return min(scores)

    def contribute(self, interpretation: float | None) -> EvidenceContributionV2[float | None]:
        violations = set()
        if interpretation == 0.0:
            violations.add("TEMPORAL_MAX_DAYS_EXCEEDED")
        return EvidenceContributionV2(
            provider_name=SignalName.TEMPORAL,
            score=interpretation,
            violations=frozenset(violations),
            interpretation=interpretation
        )

class TemporalEvidenceProvider:
    def __init__(self, max_days: int = 7):
        self.pipeline = TemporalEvidencePipeline(max_days)
        
    def get_name(self) -> str:
        return SignalName.TEMPORAL
        
    def get_blockers(self) -> Iterable[Blocker]:
        return []
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        contrib_v2 = self.pipeline.contribute(interpretation)
        return EvidenceContribution(
            provider_name=contrib_v2.provider_name,
            score=contrib_v2.score,
            violations=contrib_v2.violations,
            metadata=contrib_v2.metadata
        )

@dataclass(frozen=True)
class TaxObservation:
    purchases: tuple[PurchaseRecord, ...]
    gsts: tuple[GSTRecord, ...]

class TaxEvidencePipeline(EvidencePipeline[TaxObservation, float | None]):
    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> TaxObservation:
        return TaxObservation(purchases=tuple(purchases), gsts=tuple(gsts))

    def interpret(self, observation: TaxObservation) -> float | None:
        from recongraph.domain.tax.parser import DeterministicTaxParser
        scores = []
        for p in observation.purchases:
            p_val = DeterministicTaxParser.parse(p.tax_identity, field_id="tax_identity")
            for g in observation.gsts:
                g_val = DeterministicTaxParser.parse(g.tax_identity, field_id="tax_identity")
                s = tax_identity_score(p_val, g_val)
                if s is not None:
                    scores.append(s)
        if not scores:
            return None
        return min(scores)

    def contribute(self, interpretation: float | None) -> EvidenceContributionV2[float | None]:
        violations = set()
        if interpretation == 0.0:
            violations.add("TAX_IDENTITY_CONFLICT")
        return EvidenceContributionV2(
            provider_name=SignalName.TAX_IDENTITY,
            score=interpretation,
            violations=frozenset(violations),
            interpretation=interpretation
        )

class TaxEvidenceProvider:
    def __init__(self):
        self.pipeline = TaxEvidencePipeline()

    def get_name(self) -> str:
        return SignalName.TAX_IDENTITY
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [TaxIdentityBlocker()]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        contrib_v2 = self.pipeline.contribute(interpretation)
        return EvidenceContribution(
            provider_name=contrib_v2.provider_name,
            score=contrib_v2.score,
            violations=contrib_v2.violations,
            metadata=contrib_v2.metadata
        )

@dataclass(frozen=True)
class VendorObservationPayload:
    purchases: tuple[PurchaseRecord, ...]
    gsts: tuple[GSTRecord, ...]

class VendorEvidencePipeline(EvidencePipeline[VendorObservationPayload, Any]):
    def __init__(self, context: VendorIdentityContext):
        from recongraph.domain.vendor.observation import VendorNameObservation
        from recongraph.domain.derivations import DerivedArtifactIdentity
        self.context = context
        self._artifact_cache: dict[str | None, tuple[VendorNameObservation, DerivedArtifactIdentity]] = {}

    def _get_artifact(self, raw_name: str | None):
        if raw_name not in self._artifact_cache:
            obs = DeterministicVendorParser.parse(raw_name)
            self._artifact_cache[raw_name] = (obs, build_vendor_observation_artifact(obs).identity)
        return self._artifact_cache[raw_name]

    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> VendorObservationPayload:
        return VendorObservationPayload(tuple(purchases), tuple(gsts))

    def interpret(self, observation: VendorObservationPayload) -> Any:
        scores_with_meta = []
        for p in observation.purchases:
            p_obs, p_id = self._get_artifact(p.vendor_name)
            for g in observation.gsts:
                g_obs, g_id = self._get_artifact(g.vendor_name)
                
                interp = VendorPairInterpreter.interpret(p_obs, p_id, g_obs, g_id, self.context)
                proj = VendorProjectionPolicyV1.project(interp)
                
                if proj.similarity is not None:
                    scores_with_meta.append((proj.similarity, interp, proj))
                    
        if not scores_with_meta:
            return None
            
        weakest = min(scores_with_meta, key=lambda x: x[0])
        return weakest

    def contribute(self, interpretation: Any) -> EvidenceContributionV2[Any]:
        if not interpretation:
            return EvidenceContributionV2(
                provider_name=SignalName.ENTITY,
                score=None,
                metadata={},
                interpretation=None
            )
            
        weakest_similarity, weakest_interp, weakest_proj = interpretation
        
        return EvidenceContributionV2(
            provider_name=SignalName.ENTITY,
            score=weakest_similarity,
            metadata={
                "vendor_interpretation": weakest_interp,
                "vendor_projection": weakest_proj
            },
            interpretation=interpretation
        )

class VendorEvidenceProvider:
    def __init__(self, context: VendorIdentityContext):
        self.pipeline = VendorEvidencePipeline(context)
        
    def get_name(self) -> str:
        return SignalName.ENTITY
        
    def get_blockers(self) -> Iterable[Blocker]:
        return []
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        contrib_v2 = self.pipeline.contribute(interpretation)
        return EvidenceContribution(
            provider_name=contrib_v2.provider_name,
            score=contrib_v2.score,
            violations=contrib_v2.violations,
            metadata=contrib_v2.metadata
        )

@dataclass(frozen=True)
class ReferenceObservation:
    p_refs: str
    g_refs: str

class ReferenceEvidencePipeline(EvidencePipeline[ReferenceObservation, Any]):
    def __init__(self, context: ReferenceEvidenceContext):
        self.context = context

    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> ReferenceObservation:
        p_refs = " ".join(p.reference for p in purchases if p.reference)
        g_refs = " ".join(g.reference for g in gsts if g.reference)
        return ReferenceObservation(p_refs=p_refs, g_refs=g_refs)

    def interpret(self, observation: ReferenceObservation) -> Any:
        if observation.p_refs and observation.g_refs:
            return compute_reference_interpretation(observation.p_refs, observation.g_refs, self.context)
        return None

    def contribute(self, interpretation: Any) -> EvidenceContributionV2[Any]:
        if interpretation is None:
            return EvidenceContributionV2(provider_name=SignalName.REFERENCE, score=None)
            
        return EvidenceContributionV2(
            provider_name=SignalName.REFERENCE,
            score=interpretation.score,
            metadata={"reference_interpretation": interpretation},
            interpretation=interpretation
        )

class ReferenceEvidenceProvider:
    def __init__(self, context: ReferenceEvidenceContext):
        self.context = context
        self.pipeline = ReferenceEvidencePipeline(context)
        
    def get_name(self) -> str:
        return SignalName.REFERENCE
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [ReferenceTokenBlocker(self.context.profile)]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        contrib_v2 = self.pipeline.contribute(interpretation)
        return EvidenceContribution(
            provider_name=contrib_v2.provider_name,
            score=contrib_v2.score,
            violations=contrib_v2.violations,
            metadata=contrib_v2.metadata
        )
"""

with open("src/recongraph/plugins/core_providers.py", "w") as f:
    f.write(new_content)
