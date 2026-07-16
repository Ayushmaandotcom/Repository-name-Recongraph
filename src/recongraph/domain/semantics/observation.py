from dataclasses import dataclass
from typing import Tuple, Optional
from recongraph.domain.semantics.artifact import DerivedEmbeddingArtifact

@dataclass(frozen=True)
class SemanticObservation:
    """
    A hybrid observation wrapping the raw text, normalized text, 
    and a reference to the DerivedEmbeddingArtifact.
    Prevents vectors from acting as the *only* evidence.
    """
    raw_text: str
    normalized_text: str
    tokens: Tuple[str, ...]
    embedding_artifact: DerivedEmbeddingArtifact
    
    @classmethod
    def create(cls, raw_text: str, embedding_artifact: DerivedEmbeddingArtifact) -> "SemanticObservation":
        import re
        normalized = re.sub(r"[^\w\s]", "", raw_text).upper().strip()
        tokens = tuple(normalized.split()) if normalized else ()
        
        return cls(
            raw_text=raw_text,
            normalized_text=normalized,
            tokens=tokens,
            embedding_artifact=embedding_artifact
        )
