import re
from recongraph.normalization.text import normalize_reference
from recongraph.domain.reference.artifact import ParsedReferenceIdentifier

class DeterministicReferenceParser:
    @classmethod
    def parse(cls, reference: str | None) -> ParsedReferenceIdentifier:
        if reference is None or not reference.strip():
            return ParsedReferenceIdentifier("", frozenset(), False)
            
        normalized = normalize_reference(reference)
        if not normalized:
            return ParsedReferenceIdentifier("", frozenset(), False)
            
        tokens = frozenset(re.findall(r"\d+", reference))
        return ParsedReferenceIdentifier(
            normalized_value=normalized,
            numeric_tokens=tokens,
            is_valid=True
        )
