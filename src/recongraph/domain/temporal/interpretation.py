from dataclasses import dataclass

from recongraph.domain.temporal.artifact import TemporalArtifact
from recongraph.domain.temporal.factors import TemporalRelation, TemporalRelationState

@dataclass(frozen=True)
class TemporalPairInterpretation:
    left_artifact: TemporalArtifact
    right_artifact: TemporalArtifact
    relation: TemporalRelation

class TemporalPairInterpreter:
    @staticmethod
    def _parse_period(period: str | None) -> tuple[int, int] | None:
        if not period:
            return None
        parts = period.split("-")
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return int(parts[0]), int(parts[1])
        return None

    @staticmethod
    def _period_diff_months(p1: str | None, p2: str | None) -> int | None:
        parsed1 = TemporalPairInterpreter._parse_period(p1)
        parsed2 = TemporalPairInterpreter._parse_period(p2)
        if not parsed1 or not parsed2:
            return None
        y1, m1 = parsed1
        y2, m2 = parsed2
        return (y1 - y2) * 12 + (m1 - m2)

    @classmethod
    def interpret(
        cls,
        left: TemporalArtifact,
        right: TemporalArtifact,
        max_days: int
    ) -> TemporalPairInterpretation:
        
        day_difference = abs((left.record_date - right.record_date).days)
        period_diff = cls._period_diff_months(left.filing_period, right.filing_period)
        
        if day_difference == 0 and period_diff == 0:
            state = TemporalRelationState.EXACT_MATCH
        elif day_difference <= max_days:
            # Check for late filing. Suppose left is Purchase and right is GST.
            # Usually GST is filed in a later month if the invoice was late in the month.
            # But the interpreter doesn't know which is which. 
            # If period_diff is not 0, but day diff is within max_days, it's a cross-period match.
            if period_diff is not None and period_diff != 0:
                state = TemporalRelationState.LATE_FILING
            else:
                state = TemporalRelationState.WITHIN_TOLERANCE
        else:
            state = TemporalRelationState.EXCEEDS_WINDOW
            
        rel = TemporalRelation(
            state=state,
            day_difference=day_difference,
            max_days=max_days,
            period_difference=period_diff
        )
                
        return TemporalPairInterpretation(
            left_artifact=left,
            right_artifact=right,
            relation=rel
        )
