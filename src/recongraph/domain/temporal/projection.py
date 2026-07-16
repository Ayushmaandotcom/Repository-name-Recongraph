from dataclasses import dataclass
from recongraph.domain.temporal.interpretation import TemporalPairInterpretation
from recongraph.domain.temporal.factors import TemporalRelationState

@dataclass(frozen=True)
class TemporalV1ScalarProjection:
    score: float | None
    violations: frozenset[str]
    metadata: dict[str, str]

class TemporalV1ProjectionContract:
    @classmethod
    def project(cls, interpretations: tuple[TemporalPairInterpretation, ...]) -> TemporalV1ScalarProjection:
        violations = set()
        scores = []
        
        for interp in interpretations:
            if interp.relation.state == TemporalRelationState.EXCEEDS_WINDOW:
                violations.add("TEMPORAL_MAX_DAYS_EXCEEDED")
                scores.append(0.0)
            else:
                diff = interp.relation.day_difference
                max_d = interp.relation.max_days
                s = max(0.0, 1.0 - (diff / max_d)) if max_d > 0 else 0.0
                scores.append(s)
                
        if not scores:
            score = None
        else:
            score = min(scores)
            if score == 0.0:
                violations.add("TEMPORAL_MAX_DAYS_EXCEEDED")
                
        return TemporalV1ScalarProjection(
            score=score,
            violations=frozenset(violations),
            metadata={
                "projection_version": "1.0",
                "projection_boundary": "TemporalV1ScalarProjection"
            }
        )
