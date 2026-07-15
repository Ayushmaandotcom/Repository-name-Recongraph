from dataclasses import dataclass
from recongraph.domain.tax.interpretation import TaxPairInterpretation
from recongraph.domain.tax.factors import GSTINRelationState, PANRelationState

@dataclass(frozen=True)
class TaxV1ScalarProjection:
    """
    Lossy compression of a rich tax semantic interpretation into a scalar score.
    """
    score: float | None
    violations: frozenset[str]
    metadata: dict[str, str]

class TaxV1ProjectionContract:
    """
    Projects Tax Pair Interpretations into V1 legacy scalar scores.
    """
    @classmethod
    def project(cls, interpretations: tuple[TaxPairInterpretation, ...]) -> TaxV1ScalarProjection:
        violations = set()
        
        same_legal_entity_proven = False
        distinct_legal_entity = False
        
        for interp in interpretations:
            if interp.gstin_relation.state in (GSTINRelationState.EXACT_MATCH, GSTINRelationState.DIFFERENT_STATE_SAME_PAN):
                same_legal_entity_proven = True
            elif interp.pan_relation.state == PANRelationState.EXACT_MATCH:
                same_legal_entity_proven = True
            elif interp.pan_relation.state == PANRelationState.DISTINCT:
                distinct_legal_entity = True
                violations.add("TAX_IDENTITY_CONFLICT")
                
        # Compression into a scalar
        # 1.0 -> We have proof they are the same legal entity
        # 0.0 -> We have proof they are distinct entities
        # None -> We have no proof either way
        if distinct_legal_entity:
            score = 0.0
        elif same_legal_entity_proven:
            score = 1.0
        else:
            score = None
            
        metadata = {
            "projection_version": "1.0",
            "projection_boundary": "TaxV1ScalarProjection"
        }
            
        return TaxV1ScalarProjection(
            score=score,
            violations=frozenset(violations),
            metadata=metadata
        )
