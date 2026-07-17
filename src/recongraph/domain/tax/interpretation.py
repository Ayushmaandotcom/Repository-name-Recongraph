from dataclasses import dataclass

from recongraph.domain.tax.artifact import TaxIntelligenceArtifact
from recongraph.domain.tax.factors import (
    GSTINRelation, GSTINRelationState,
    PANRelation, PANRelationState,
    RegimeRelation, RegimeRelationState,
    GrossNetRelation, GrossNetRelationState
)
from decimal import Decimal

@dataclass(frozen=True)
class TaxIntelligenceInterpretation:
    left_artifact: TaxIntelligenceArtifact
    right_artifact: TaxIntelligenceArtifact
    
    gstin_relation: GSTINRelation
    pan_relation: PANRelation
    regime_relation: RegimeRelation
    gross_net_relation: GrossNetRelation


class TaxIntelligenceInterpreter:
    """
    Produces factorized comparative evidence for tax identifiers and financial regimes.
    """
    
    VERSION = "2.0.0"
    TOLERANCE = Decimal("0.01")

    @classmethod
    def interpret(
        cls,
        left: TaxIntelligenceArtifact,
        right: TaxIntelligenceArtifact
    ) -> TaxIntelligenceInterpretation:
        
        gstin_rel = cls._compare_gstin(left, right)
        pan_rel = cls._compare_pan(left, right)
        regime_rel = cls._compare_regime(left, right)
        gn_rel = cls._compare_gross_net(left, right)
        
        return TaxIntelligenceInterpretation(
            left_artifact=left,
            right_artifact=right,
            gstin_relation=gstin_rel,
            pan_relation=pan_rel,
            regime_relation=regime_rel,
            gross_net_relation=gn_rel
        )

    @classmethod
    def _compare_gstin(cls, left: TaxIntelligenceArtifact, right: TaxIntelligenceArtifact) -> GSTINRelation:
        l_gstin = left.tax_identity.parsed_result.gstin_candidate if left.tax_identity.parsed_result.gstin_valid else None
        r_gstin = right.tax_identity.parsed_result.gstin_candidate if right.tax_identity.parsed_result.gstin_valid else None

        if not l_gstin and not r_gstin:
            return GSTINRelation(GSTINRelationState.BOTH_MISSING, None, None)
        if not l_gstin or not r_gstin:
            return GSTINRelation(GSTINRelationState.ONE_MISSING, l_gstin, r_gstin)

        if l_gstin == r_gstin:
            return GSTINRelation(GSTINRelationState.EXACT_MATCH, l_gstin, r_gstin)
            
        # Check if PANs match even though GSTINs differ (using the deterministic parser's output)
        l_pan = left.tax_identity.parsed_result.pan_candidate
        r_pan = right.tax_identity.parsed_result.pan_candidate

        if l_pan and r_pan and l_pan == r_pan:
            return GSTINRelation(GSTINRelationState.DIFFERENT_STATE_SAME_PAN, l_gstin, r_gstin)
            
        return GSTINRelation(GSTINRelationState.DISTINCT, l_gstin, r_gstin)

    @classmethod
    def _compare_pan(cls, left: TaxIntelligenceArtifact, right: TaxIntelligenceArtifact) -> PANRelation:
        l_pan = left.tax_identity.parsed_result.pan_candidate if left.tax_identity.parsed_result.pan_valid else None
        r_pan = right.tax_identity.parsed_result.pan_candidate if right.tax_identity.parsed_result.pan_valid else None

        l_derived = left.tax_identity.parsed_result.pan_derived_from_gstin
        r_derived = right.tax_identity.parsed_result.pan_derived_from_gstin
        derived = l_derived or r_derived

        if not l_pan and not r_pan:
            return PANRelation(PANRelationState.BOTH_MISSING, None, None, derived)
        if not l_pan or not r_pan:
            return PANRelation(PANRelationState.ONE_MISSING, l_pan, r_pan, derived)

        if l_pan == r_pan:
            return PANRelation(PANRelationState.EXACT_MATCH, l_pan, r_pan, derived)
            
        return PANRelation(PANRelationState.DISTINCT, l_pan, r_pan, derived_from_gstin=False)

    @classmethod
    def _compare_regime(cls, left: TaxIntelligenceArtifact, right: TaxIntelligenceArtifact) -> RegimeRelation:
        if left.tax_rate is None or right.tax_rate is None:
            return RegimeRelation(RegimeRelationState.UNKNOWN, left.tax_rate, right.tax_rate)
            
        diff = abs(left.tax_rate - right.tax_rate)
        if diff <= cls.TOLERANCE:
            state = RegimeRelationState.CONSISTENT
        else:
            state = RegimeRelationState.INCONSISTENT
            
        return RegimeRelation(state, left.tax_rate, right.tax_rate)

    @classmethod
    def _compare_gross_net(cls, left: TaxIntelligenceArtifact, right: TaxIntelligenceArtifact) -> GrossNetRelation:
        def is_math_valid(artifact: TaxIntelligenceArtifact) -> bool:
            if artifact.net_amount is None or artifact.tax_amount is None:
                return False
            # Check if net + tax == amount (within tolerance)
            expected = artifact.net_amount + artifact.tax_amount
            return abs(expected - artifact.amount) <= cls.TOLERANCE
            
        l_valid = is_math_valid(left)
        r_valid = is_math_valid(right)
        
        # We define consistency if both sides have valid internal gross/net math.
        # Note: If one side doesn't have net_amount/tax_amount, we mark UNKNOWN.
        if (left.net_amount is None or left.tax_amount is None) or (right.net_amount is None or right.tax_amount is None):
            return GrossNetRelation(GrossNetRelationState.UNKNOWN, l_valid, r_valid)
            
        if l_valid and r_valid:
            return GrossNetRelation(GrossNetRelationState.CONSISTENT, l_valid, r_valid)
            
        return GrossNetRelation(GrossNetRelationState.INCONSISTENT, l_valid, r_valid)
