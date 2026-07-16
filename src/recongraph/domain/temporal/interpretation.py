from dataclasses import dataclass

from recongraph.domain.temporal.artifact import TemporalArtifact
from recongraph.domain.temporal.factors import TemporalRelation, TemporalRelationState

@dataclass(frozen=True)
class TemporalPairInterpretation:
    left_artifact: TemporalArtifact
    right_artifact: TemporalArtifact
    relation: TemporalRelation

class TemporalPairInterpreter:
    @classmethod
    def interpret(
        cls,
        left: TemporalArtifact,
        right: TemporalArtifact,
        max_days: int
    ) -> TemporalPairInterpretation:
        
        day_difference = abs((left.record_date - right.record_date).days)
        
        if day_difference <= max_days:
            state = TemporalRelationState.WITHIN_WINDOW
        else:
            state = TemporalRelationState.EXCEEDS_WINDOW
            
        rel = TemporalRelation(
            state=state,
            day_difference=day_difference,
            max_days=max_days
        )
                
        return TemporalPairInterpretation(
            left_artifact=left,
            right_artifact=right,
            relation=rel
        )
