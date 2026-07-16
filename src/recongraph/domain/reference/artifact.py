from dataclasses import dataclass
import re

from recongraph.normalization.text import normalize_reference

@dataclass(frozen=True)
class ParsedReferenceIdentifier:
    normalized_value: str
    numeric_tokens: frozenset[str]
    is_valid: bool

@dataclass(frozen=True)
class ReferenceIdentifierArtifact:
    parsed_result: ParsedReferenceIdentifier
    
    @classmethod
    def create(cls, parsed_result: ParsedReferenceIdentifier) -> "ReferenceIdentifierArtifact":
        return cls(parsed_result=parsed_result)
