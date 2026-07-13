from typing import Protocol, Any, runtime_checkable
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, _extract_numeric_tokens
from recongraph.normalization.text import normalize_reference
import math

@runtime_checkable
class Blocker(Protocol):
    """
    Protocol for extracting indexing keys from a financial record.
    Keys are returned as a set of strings.
    """
    def extract_keys(self, record: Any) -> frozenset[str]:
        ...

class ExactAmountBlocker:
    """Blocks records based on exactly matching amounts."""
    def extract_keys(self, record: Any) -> frozenset[str]:
        amount = getattr(record, "amount", None)
        if amount is None:
            return frozenset()
        return frozenset([f"AMT:{amount:.2f}"])

class TaxIdentityBlocker:
    """Blocks records based on exact normalized tax identity."""
    def extract_keys(self, record: Any) -> frozenset[str]:
        tax_identity = getattr(record, "tax_identity", None)
        if not tax_identity:
            return frozenset()
        # Normalizing to uppercase and stripped string
        identity = str(tax_identity).strip().upper()
        if not identity:
            return frozenset()
        return frozenset([f"TAX:{identity}"])

class ReferenceTokenBlocker:
    """
    Extracts blocking keys from the reference field.
    Only yields keys for statistically rare tokens to prevent
    highly generic tokens from generating thousands of candidate edges.
    """
    def __init__(self, profile: ReferenceCorpusProfile, rarity_threshold: float = 0.8):
        self.profile = profile
        self.rarity_threshold = rarity_threshold

    def _is_rare(self, freq: int, total: int) -> bool:
        if total == 0:
            return False
        # Calculate magnitude: 1 - sqrt(freq / total)
        magnitude = 1.0 - math.sqrt(freq / total)
        return magnitude >= self.rarity_threshold

    def extract_keys(self, record: Any) -> frozenset[str]:
        reference = getattr(record, "reference", None)
        if not reference:
            return frozenset()
            
        keys = set()
        
        # Exact normalized match key
        normalized = normalize_reference(reference)
        if normalized:
            freq = self.profile.normalized_reference_frequency.get(normalized, 0)
            if self._is_rare(freq, self.profile.reference_count):
                keys.add(f"REF_NORM:{normalized}")
                
        # Token match keys
        tokens = _extract_numeric_tokens(reference)
        for token in tokens:
            freq = self.profile.numeric_token_document_frequency.get(token, 0)
            if self._is_rare(freq, self.profile.reference_count):
                keys.add(f"REF_TOK:{token}")
                
        return frozenset(keys)
