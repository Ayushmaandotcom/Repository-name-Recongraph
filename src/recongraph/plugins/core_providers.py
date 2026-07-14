from typing import Iterable, Sequence, Callable, TypeVar
from recongraph.plugins.provider import EvidenceProvider, EvidenceContribution
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
        self.pipeline = FinancialEvidencePipeline(tolerance=tolerance)
        
    def get_name(self) -> str:
        return SignalName.AMOUNT
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [ExactAmountBlocker()]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        from recongraph.domain.financial.amount_projection import project_amount_similarity
        
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        projection = project_amount_similarity(interpretation)
        
        violations = set(projection.warnings)
        if interpretation.currency_relation.value == "DIFFERENT":
            violations.add("CURRENCY_MISMATCH")
        elif projection.similarity < 0.5 and interpretation.equality.value != "EQUAL":
            violations.add("SEVERE_AMOUNT_CONFLICT")
            
        return EvidenceContribution(
            provider_name=self.get_name(),
            score=projection.similarity,
            violations=frozenset(violations),
            metadata={
                "interpretation": interpretation,
                "projection": projection
            }
        )

class TemporalEvidenceProvider:
    def __init__(self, max_days: int = 7):
        self.max_days = max_days
        
    def get_name(self) -> str:
        return SignalName.TEMPORAL
        
    def get_blockers(self) -> Iterable[Blocker]:
        return []
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        score = _weakest_available(
            purchases,
            gsts,
            lambda r: r.record_date,
            lambda d1, d2: temporal_score(d1, d2, self.max_days)
        )
        
        if score == 0.0:
            return EvidenceContribution(
                provider_name=self.get_name(),
                score=0.0,
                violations=frozenset(["TEMPORAL_MAX_DAYS_EXCEEDED"])
            )
            
        return EvidenceContribution(
            provider_name=self.get_name(),
            score=score
        )

class TaxEvidenceProvider:
    def get_name(self) -> str:
        return SignalName.TAX_IDENTITY
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [TaxIdentityBlocker()]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        from recongraph.domain.tax.parser import DeterministicTaxParser
        
        score = _weakest_available(
            purchases,
            gsts,
            lambda r: DeterministicTaxParser.parse(r.tax_identity, field_id="tax_identity"),
            tax_identity_score
        )
        
        if score == 0.0:
            return EvidenceContribution(
                provider_name=self.get_name(),
                score=0.0,
                violations=frozenset(["TAX_IDENTITY_CONFLICT"])
            )
            
        return EvidenceContribution(
            provider_name=self.get_name(),
            score=score
        )

class VendorEvidenceProvider:
    def __init__(self, context: VendorIdentityContext):
        self.context = context
        self._artifact_cache = {}
        
    def get_name(self) -> str:
        return SignalName.ENTITY
        
    def get_blockers(self) -> Iterable[Blocker]:
        return []
        
    def _get_artifact(self, raw_name: str | None):
        if raw_name not in self._artifact_cache:
            obs = DeterministicVendorParser.parse(raw_name)
            self._artifact_cache[raw_name] = (obs, build_vendor_observation_artifact(obs).identity)
        return self._artifact_cache[raw_name]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        best_similarity = None
        best_metadata = None
        
        # Vendor semantics (V1-1D): Compute pairwise interpretation and take the weakest scalar available
        # among the pairs. If there are multiple edges, we project each pair.
        scores_with_meta = []
        for p in purchases:
            p_obs, p_id = self._get_artifact(p.vendor_name)
            for g in gsts:
                g_obs, g_id = self._get_artifact(g.vendor_name)
                
                interp = VendorPairInterpreter.interpret(p_obs, p_id, g_obs, g_id, self.context)
                proj = VendorProjectionPolicyV1.project(interp)
                
                if proj.similarity is not None:
                    scores_with_meta.append((proj.similarity, interp, proj))
                    
        if not scores_with_meta:
            # Handle entirely uninterpretable or missing
            return EvidenceContribution(
                provider_name=self.get_name(),
                score=None,
                metadata={}
            )
            
        # Extract the weakest available (matching the legacy semantics)
        weakest = min(scores_with_meta, key=lambda x: x[0])
        weakest_similarity, weakest_interp, weakest_proj = weakest
        
        return EvidenceContribution(
            provider_name=self.get_name(),
            score=weakest_similarity,
            metadata={
                "vendor_interpretation": weakest_interp,
                "vendor_projection": weakest_proj
            }
        )

class ReferenceEvidenceProvider:
    def __init__(self, context: ReferenceEvidenceContext):
        self.context = context
        
    def get_name(self) -> str:
        return SignalName.REFERENCE
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [ReferenceTokenBlocker(self.context.profile)]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        p_refs = " ".join(p.reference for p in purchases if p.reference)
        g_refs = " ".join(g.reference for g in gsts if g.reference)
        
        if p_refs and g_refs:
            ref_interpretation = compute_reference_interpretation(p_refs, g_refs, self.context)
            return EvidenceContribution(
                provider_name=self.get_name(),
                score=ref_interpretation.score,
                metadata={"reference_interpretation": ref_interpretation}
            )
        return EvidenceContribution(provider_name=self.get_name(), score=None)
