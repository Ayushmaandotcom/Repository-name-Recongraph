from collections.abc import Mapping
from dataclasses import dataclass

from recongraph.domain.records import GSTRecord, PurchaseRecord
from recongraph.matching.scoring import (
    RelationshipPolicy,
    RelationshipScore,
    SignalName,
    calculate_relationship_score,
)
from recongraph.matching.reference_evidence import ReferenceEvidenceContext
from recongraph.domain.vendor.context import VendorIdentityContext
from recongraph.plugins.core_providers import (
    VendorEvidenceProvider,
    TaxEvidenceProvider,
    FinancialEvidenceProvider,
    TemporalEvidenceProvider,
    ReferenceEvidenceProvider,
)
from recongraph.plugins.semantic_providers import SemanticEvidenceProvider
from recongraph.plugins.provider_v2 import EvidenceContributionV2

PURCHASE_TO_GST_MAX_DAYS = 7

PURCHASE_TO_GST_POLICY = RelationshipPolicy(
    weights={
        SignalName.ENTITY: 0.20,
        SignalName.REFERENCE: 0.20,
        SignalName.AMOUNT: 0.25,
        SignalName.TEMPORAL: 0.10,
        SignalName.TAX_IDENTITY: 0.25,
    },
    contradiction_penalties={},
)

PURCHASE_TO_GST_POLICY_WITH_SEMANTICS = RelationshipPolicy(
    weights={
        SignalName.ENTITY: 0.20,
        SignalName.REFERENCE: 0.15,
        SignalName.AMOUNT: 0.25,
        SignalName.TEMPORAL: 0.10,
        SignalName.TAX_IDENTITY: 0.20,
        SignalName.SEMANTICS: 0.10,
    },
    contradiction_penalties={},
)

@dataclass(frozen=True)
class PairScoringResult:
    """Represent raw evidence contributions from Providers."""
    contributions: Mapping[str, EvidenceContributionV2]
    
    @property
    def signals(self) -> dict[str, float | None]:
        return {k: v.score for k, v in self.contributions.items()}



