from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Tuple

class VendorObservationState(Enum):
    PRESENT = auto()
    MISSING = auto()          # No string was provided
    EMPTY = auto()            # An empty or purely whitespace string was provided
    UNINTERPRETABLE = auto()  # String was provided but could not be parsed meaningfully

class TransformationType(Enum):
    UNICODE_NORMALIZATION = auto()
    CASE_NORMALIZATION = auto()
    WHITESPACE_COLLAPSE = auto()
    PUNCTUATION_STRIP = auto()
    LEGAL_FORM_EXTRACTION = auto()

class LegalFormCategory(Enum):
    PRIVATE_LIMITED = auto()
    PUBLIC_LIMITED = auto()
    LIMITED_LIABILITY_PARTNERSHIP = auto()
    PARTNERSHIP = auto()
    ONE_PERSON_COMPANY = auto()
    PROPRIETORSHIP = auto()
    TRUST = auto()
    GOVERNMENT = auto()
    HUF = auto()              # Hindu Undivided Family

@dataclass(frozen=True)
class TokenSpan:
    start_index: int
    end_index: int
    label: str

@dataclass(frozen=True)
class VendorNormalizationEvent:
    transformation_type: TransformationType
    affected_span: Optional[TokenSpan]
    before_value: str
    after_value: str
    rule_name: str

@dataclass(frozen=True)
class VendorNameObservation:
    """
    Immutable, context-independent observation of a vendor identity string.
    Must not contain cross-record assumptions or pairwise identity claims.
    """
    raw_name: str
    observation_state: VendorObservationState
    
    canonical_core_text: str
    organization_tokens: Tuple[str, ...]
    
    legal_form_category: Optional[LegalFormCategory]
    recognized_designators: Tuple[str, ...]
    
    token_spans: Tuple[TokenSpan, ...]
    normalization_events: Tuple[VendorNormalizationEvent, ...]
    
    gstin_candidate: Optional[str]
    gstin_structurally_valid: Optional[bool]
    
    pan_candidate: Optional[str]
    pan_structurally_valid: Optional[bool]
    pan_derived_from_gstin: bool
