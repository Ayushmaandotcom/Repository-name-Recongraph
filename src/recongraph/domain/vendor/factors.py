from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, Tuple
from recongraph.domain.vendor.observation import LegalFormCategory

class GSTRegistrationRelationState(Enum):
    BOTH_MISSING = auto()
    LEFT_MISSING = auto()
    RIGHT_MISSING = auto()
    BOTH_UNINTERPRETABLE = auto()
    LEFT_UNINTERPRETABLE = auto()
    RIGHT_UNINTERPRETABLE = auto()
    ONE_UNINTERPRETABLE = auto() # When one is missing and one is uninterpretable, or valid vs uninterpretable
    VALID_AND_EQUAL = auto()
    VALID_AND_DIFFERENT = auto()


class PANRelationState(Enum):
    BOTH_MISSING = auto()
    LEFT_MISSING = auto()
    RIGHT_MISSING = auto()
    BOTH_UNINTERPRETABLE = auto()
    LEFT_UNINTERPRETABLE = auto()
    RIGHT_UNINTERPRETABLE = auto()
    VALID_AND_EQUAL = auto()
    VALID_AND_DIFFERENT = auto()


class PANEvidenceDependence(Enum):
    INDEPENDENT = auto()
    PARTIALLY_DEPENDENT = auto()
    SAME_SOURCE_DERIVATION = auto()


class LexicalRelationState(Enum):
    EXACT_NORMALIZED_CORE_EQUALITY = auto()
    TOKEN_SET_EQUALITY = auto()
    BOUNDED_SUBSET = auto()
    BOUNDED_FUZZY_SIMILARITY = auto()
    DIFFERENT = auto()
    BOTH_MISSING = auto()


class LegalFormRelationState(Enum):
    BOTH_MISSING = auto()
    LEFT_MISSING = auto()
    RIGHT_MISSING = auto()
    OBSERVED_COMPATIBLE = auto()
    OBSERVED_INCOMPATIBLE = auto()


class CorpusDistinctivenessState(Enum):
    DISTINCTIVE_SUPPORT = auto()
    ATTENUATED_SUPPORT = auto()
    NOT_APPLICABLE = auto()


@dataclass(frozen=True)
class GSTRegistrationRelation:
    state: GSTRegistrationRelationState
    left_value: Optional[str]
    right_value: Optional[str]


@dataclass(frozen=True)
class PANRelation:
    state: PANRelationState
    dependence: Optional[PANEvidenceDependence]
    left_value: Optional[str]
    right_value: Optional[str]


@dataclass(frozen=True)
class LexicalRelation:
    state: LexicalRelationState
    similarity_score: Optional[float]
    shared_tokens: Tuple[str, ...]


@dataclass(frozen=True)
class LegalFormRelation:
    state: LegalFormRelationState
    left_category: Optional[LegalFormCategory]
    right_category: Optional[LegalFormCategory]


@dataclass(frozen=True)
class CorpusDistinctiveness:
    state: CorpusDistinctivenessState
    most_distinctive_token: Optional[str]
    document_frequency: Optional[float]
