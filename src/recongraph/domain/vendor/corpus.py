from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class VendorCorpusProfile:
    """
    A minimal stub representing the corpus frequency of vendor tokens.
    """
    corpus_size: int
    token_document_frequencies: Dict[str, int]
    digest: str
    
    def document_frequency(self, token: str) -> float:
        """Returns the normalized document frequency of a token."""
        if self.corpus_size == 0:
            return 0.0
        return self.token_document_frequencies.get(token, 0) / self.corpus_size
        
    def is_distinctive(self, token: str, threshold: float = 0.01) -> bool:
        """
        Determines if a token is distinctive enough to provide support.
        Threshold is the maximum document frequency to be considered distinctive.
        """
        return self.document_frequency(token) <= threshold
