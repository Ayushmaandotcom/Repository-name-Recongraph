from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
from decimal import Decimal

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
    derived_from_gstin: bool = False

class RegimeRelationState(Enum):
    CONSISTENT = auto()
    INCONSISTENT = auto()
    UNKNOWN = auto()

class GrossNetRelationState(Enum):
    CONSISTENT = auto()
    INCONSISTENT = auto()
    UNKNOWN = auto()

@dataclass(frozen=True)
class RegimeRelation:
    state: RegimeRelationState
    left_rate: Decimal | None
    right_rate: Decimal | None

@dataclass(frozen=True)
class GrossNetRelation:
    state: GrossNetRelationState
    left_math_valid: bool
    right_math_valid: bool
