from typing import Iterable, Sequence, Callable, TypeVar, Any
from dataclasses import dataclass
import datetime

from recongraph.plugins.provider import EvidenceProvider, EvidenceContribution
from recongraph.plugins.provider_v2 import EvidencePipeline, EvidenceContributionV2
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.candidate_generation.blockers import Blocker, ExactAmountBlocker, TaxIdentityBlocker, ReferenceTokenBlocker
from recongraph.matching.scoring import SignalName
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, compute_reference_interpretation
from recongraph.domain.financial.pipeline import FinancialEvidencePipeline
from recongraph.domain.temporal.interpretation import TemporalPairInterpretation
from recongraph.domain.reference.interpretation import ReferencePairInterpretation

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

class TemporalEvidencePipeline(EvidencePipeline[TemporalObservation, tuple[TemporalPairInterpretation, ...]]):
    def __init__(self, max_days: int):
        self.max_days = max_days

    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> TemporalObservation:
        return TemporalObservation(
            p_dates=tuple(p.record_date for p in purchases),
            g_dates=tuple(g.record_date for g in gsts)
        )

    def interpret(self, observation: TemporalObservation) -> tuple[TemporalPairInterpretation, ...]:
        from recongraph.domain.temporal.artifact import TemporalArtifact
        from recongraph.domain.temporal.interpretation import TemporalPairInterpreter
        
        interps = []
        for p_date in observation.p_dates:
            p_art = TemporalArtifact.create(p_date)
            for g_date in observation.g_dates:
                g_art = TemporalArtifact.create(g_date)
                interps.append(TemporalPairInterpreter.interpret(p_art, g_art, self.max_days))
                
        return tuple(interps)

    def contribute(self, interpretation: tuple[TemporalPairInterpretation, ...]) -> EvidenceContributionV2[tuple[TemporalPairInterpretation, ...]]:
        from recongraph.domain.temporal.projection import TemporalV1ProjectionContract
        
        projection = TemporalV1ProjectionContract.project(interpretation)
        
        return EvidenceContributionV2(
            provider_name=SignalName.TEMPORAL,
            score=projection.score,
            violations=projection.violations,
            interpretation=interpretation,
            metadata={"temporal_projection": projection}
        )

class TemporalEvidenceProvider:
    def __init__(self, max_days: int = 7):
        self.max_days = max_days
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

from recongraph.domain.tax.parser import DeterministicTaxParser
from recongraph.domain.tax.artifact import TaxIdentifierArtifact
from recongraph.domain.tax.interpretation import TaxPairInterpreter, TaxPairInterpretation
from recongraph.domain.tax.factors import GSTINRelationState, PANRelationState
from recongraph.domain.scopes import Proposition, PropositionSubject, ScopeKind
from recongraph.domain.assertions import EvidenceAssertionIdentity, EvidenceAssertion

class TaxEvidencePipeline(EvidencePipeline[TaxObservation, tuple[TaxPairInterpretation, ...]]):
    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> TaxObservation:
        return TaxObservation(purchases=tuple(purchases), gsts=tuple(gsts))

    def interpret(self, observation: TaxObservation) -> tuple[TaxPairInterpretation, ...]:
        interpretations = []
        for p in observation.purchases:
            p_val = DeterministicTaxParser.parse(p.tax_identity, field_id="tax_identity")
            p_artifact = TaxIdentifierArtifact.create(p_val)
            for g in observation.gsts:
                g_val = DeterministicTaxParser.parse(g.tax_identity, field_id="tax_identity")
                g_artifact = TaxIdentifierArtifact.create(g_val)
                interp = TaxPairInterpreter.interpret(p_artifact, g_artifact)
                interpretations.append(interp)
        return tuple(interpretations)

    def contribute(self, interpretation: tuple[TaxPairInterpretation, ...]) -> EvidenceContributionV2[tuple[TaxPairInterpretation, ...]]:
        from recongraph.domain.tax.projection import TaxV1ProjectionContract
        
        projection = TaxV1ProjectionContract.project(interpretation)
        
        return EvidenceContributionV2(
            provider_name=SignalName.TAX_IDENTITY,
            score=projection.score,
            violations=projection.violations,
            interpretation=interpretation,
            metadata=projection.metadata
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

class ReferenceEvidencePipeline(EvidencePipeline[ReferenceObservation, tuple[ReferencePairInterpretation, ...]]):
    def __init__(self, context: ReferenceEvidenceContext):
        self.context = context

    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> ReferenceObservation:
        p_refs = " ".join(p.reference for p in purchases if p.reference)
        g_refs = " ".join(g.reference for g in gsts if g.reference)
        return ReferenceObservation(p_refs=p_refs, g_refs=g_refs)

    def interpret(self, observation: ReferenceObservation) -> tuple[ReferencePairInterpretation, ...]:
        from recongraph.domain.reference.parser import DeterministicReferenceParser
        from recongraph.domain.reference.artifact import ReferenceIdentifierArtifact
        from recongraph.domain.reference.interpretation import ReferencePairInterpreter

        p_art = ReferenceIdentifierArtifact.create(DeterministicReferenceParser.parse(observation.p_refs))
        g_art = ReferenceIdentifierArtifact.create(DeterministicReferenceParser.parse(observation.g_refs))
        
        interp = ReferencePairInterpreter.interpret(p_art, g_art)
        return (interp,)

    def contribute(self, interpretation: tuple[ReferencePairInterpretation, ...]) -> EvidenceContributionV2[tuple[ReferencePairInterpretation, ...]]:
        from recongraph.domain.reference.projection import ReferenceV1ProjectionContract
        
        projection = ReferenceV1ProjectionContract.project(interpretation)
            
        return EvidenceContributionV2(
            provider_name=SignalName.REFERENCE,
            score=projection.score,
            violations=projection.violations,
            metadata={"reference_projection": projection},
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
