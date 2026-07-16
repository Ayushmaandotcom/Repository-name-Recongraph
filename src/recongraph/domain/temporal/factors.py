from enum import Enum, auto
from dataclasses import dataclass

class TemporalRelationState(Enum):
    WITHIN_WINDOW = auto()
    EXCEEDS_WINDOW = auto()

@dataclass(frozen=True)
class TemporalRelation:
    state: TemporalRelationState
    day_difference: int
    max_days: int
