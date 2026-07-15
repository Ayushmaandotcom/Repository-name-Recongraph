from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class GSTINRelationState(Enum):
    EXACT_MATCH = auto()
    DIFFERENT_STATE_SAME_PAN = auto()
    DISTINCT = auto()
    ONE_MISSING = auto()
    BOTH_MISSING = auto()

class PANRelationState(Enum):
    EXACT_MATCH = auto()
    DISTINCT = auto()
    ONE_MISSING = auto()
    BOTH_MISSING = auto()

@dataclass(frozen=True)
class GSTINRelation:
    state: GSTINRelationState
    left_gstin: Optional[str]
    right_gstin: Optional[str]

@dataclass(frozen=True)
class PANRelation:
    state: PANRelationState
    left_pan: Optional[str]
    right_pan: Optional[str]
    derived_from_gstin: bool
