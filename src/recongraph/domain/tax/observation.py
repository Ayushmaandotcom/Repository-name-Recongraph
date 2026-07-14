from dataclasses import dataclass
from enum import Enum, auto

class TaxObservationState(Enum):
    PRESENT = auto()
    MISSING = auto()          # No string was provided
    EMPTY = auto()            # An empty or purely whitespace string was provided
    UNINTERPRETABLE = auto()  # String was provided but could not be parsed meaningfully
    CORRUPTED = auto()        # String has characteristics of OCR corruption

class TaxIdentifierCandidateType(Enum):
    GSTIN = auto()
    PAN = auto()
    UNKNOWN = auto()          # Does not look like either

@dataclass(frozen=True)
class TaxIdentifierObservation:
    """
    Immutable, context-independent observation of a tax identifier string.
    Records exactly what was observed from the source field.
    """
    raw_value: str
    source_field_identity: str
    candidate_type: TaxIdentifierCandidateType
    observation_state: TaxObservationState
