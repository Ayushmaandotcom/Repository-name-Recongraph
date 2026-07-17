from enum import Enum, auto
from dataclasses import dataclass

class TemporalRelationState(Enum):
    EXACT_MATCH = auto()
    WITHIN_TOLERANCE = auto()
    LATE_FILING = auto()
    EXCEEDS_WINDOW = auto()

@dataclass(frozen=True)
class TemporalRelation:
    state: TemporalRelationState
    day_difference: int
    max_days: int
    period_difference: int | None = None
