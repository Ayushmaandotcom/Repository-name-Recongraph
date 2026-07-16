from dataclasses import dataclass
from recongraph.domain.reference.interpretation import ReferencePairInterpretation
from recongraph.domain.reference.factors import ReferenceRelationState

@dataclass(frozen=True)
class ReferenceV1ScalarProjection:
    score: float | None
    violations: frozenset[str]
    metadata: dict[str, str]

class ReferenceV1ProjectionContract:
    @classmethod
    def project(cls, interpretations: tuple[ReferencePairInterpretation, ...]) -> ReferenceV1ScalarProjection:
        violations: set[str] = set()
        
        has_match = False
        for interp in interpretations:
            if interp.relation.state == ReferenceRelationState.EXACT_MATCH:
                has_match = True
            elif interp.relation.shared_numeric_tokens:
                has_match = True
                
        score = 1.0 if has_match else None
        
        return ReferenceV1ScalarProjection(
            score=score,
            violations=frozenset(violations),
            metadata={
                "projection_version": "1.0",
                "projection_boundary": "ReferenceV1ScalarProjection"
            }
        )
