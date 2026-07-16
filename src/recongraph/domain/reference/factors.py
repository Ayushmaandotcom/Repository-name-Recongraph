from enum import Enum, auto
from dataclasses import dataclass

class ReferenceRelationState(Enum):
    EXACT_MATCH = auto()
    DISTINCT = auto()
    ONE_MISSING = auto()
    BOTH_MISSING = auto()

@dataclass(frozen=True)
class ReferenceRelation:
    state: ReferenceRelationState
    shared_numeric_tokens: frozenset[str]
