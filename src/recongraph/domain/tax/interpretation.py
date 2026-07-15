from dataclasses import dataclass

from recongraph.domain.tax.artifact import TaxIdentifierArtifact
from recongraph.domain.tax.factors import (
    GSTINRelation, GSTINRelationState,
    PANRelation, PANRelationState
)

@dataclass(frozen=True)
class TaxPairInterpretation:
    left_artifact: TaxIdentifierArtifact
    right_artifact: TaxIdentifierArtifact
    
    gstin_relation: GSTINRelation
    pan_relation: PANRelation


class TaxPairInterpreter:
    """
    Produces factorized comparative evidence for tax identifiers.
    """
    
    VERSION = "1.0.0"

    @classmethod
    def interpret(
        cls,
        left: TaxIdentifierArtifact,
        right: TaxIdentifierArtifact
    ) -> TaxPairInterpretation:
        
        gstin_rel = cls._compare_gstin(left, right)
        pan_rel = cls._compare_pan(left, right)
        
        return TaxPairInterpretation(
            left_artifact=left,
            right_artifact=right,
            gstin_relation=gstin_rel,
            pan_relation=pan_rel
        )

    @classmethod
    def _compare_gstin(cls, left: TaxIdentifierArtifact, right: TaxIdentifierArtifact) -> GSTINRelation:
        l_gstin = left.parsed_result.gstin_candidate if left.parsed_result.gstin_valid else None
        r_gstin = right.parsed_result.gstin_candidate if right.parsed_result.gstin_valid else None

        if not l_gstin and not r_gstin:
            return GSTINRelation(GSTINRelationState.BOTH_MISSING, None, None)
        if not l_gstin or not r_gstin:
            return GSTINRelation(GSTINRelationState.ONE_MISSING, l_gstin, r_gstin)

        if l_gstin == r_gstin:
            return GSTINRelation(GSTINRelationState.EXACT_MATCH, l_gstin, r_gstin)
            
        # Check if PANs match even though GSTINs differ (using the deterministic parser's output)
        l_pan = left.parsed_result.pan_candidate
        r_pan = right.parsed_result.pan_candidate
        if l_pan and r_pan and l_pan == r_pan:
            return GSTINRelation(GSTINRelationState.DIFFERENT_STATE_SAME_PAN, l_gstin, r_gstin)
            
        return GSTINRelation(GSTINRelationState.DISTINCT, l_gstin, r_gstin)

    @classmethod
    def _compare_pan(cls, left: TaxIdentifierArtifact, right: TaxIdentifierArtifact) -> PANRelation:
        l_pan = left.parsed_result.pan_candidate if left.parsed_result.pan_valid else None
        r_pan = right.parsed_result.pan_candidate if right.parsed_result.pan_valid else None

        l_derived = left.parsed_result.pan_derived_from_gstin
        r_derived = right.parsed_result.pan_derived_from_gstin
        derived = l_derived or r_derived

        if not l_pan and not r_pan:
            return PANRelation(PANRelationState.BOTH_MISSING, None, None, derived)
        if not l_pan or not r_pan:
            return PANRelation(PANRelationState.ONE_MISSING, l_pan, r_pan, derived)

        if l_pan == r_pan:
            return PANRelation(PANRelationState.EXACT_MATCH, l_pan, r_pan, derived)
            
        return PANRelation(PANRelationState.DISTINCT, l_pan, r_pan, derived)
