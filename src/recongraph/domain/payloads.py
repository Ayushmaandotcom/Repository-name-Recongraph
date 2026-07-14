from dataclasses import dataclass
from typing import Any
from .identity import canonical_encode


@dataclass(frozen=True, slots=True)
class CanonicalPayloadEnvelope:
    """
    Guarantees deterministic JSON serialization for semantic identity hashing.
    Enforces int64, NFC strings, strict dictionary sorting, and NO floats.
    """
    content: Any

    def canonicalize(self) -> bytes:
        return canonical_encode(self.content)

    def to_dict(self) -> Any:
        return self.content


@dataclass(frozen=True, slots=True, order=True)
class TypedPayloadEnvelope:
    """
    A typed payload with a semantic version and canonicalized content.
    """
    type_id: str
    semantic_version: str
    payload: CanonicalPayloadEnvelope

    def canonicalize(self) -> bytes:
        return canonical_encode({
            "type_id": self.type_id,
            "semantic_version": self.semantic_version,
            # We don't hash the raw content string, but canonicalize it first, or just include it.
            # `canonical_encode` recursively validates payload content.
            "payload": self.payload.to_dict()
        })
