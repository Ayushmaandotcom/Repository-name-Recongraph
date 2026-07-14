import hashlib
import json
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(frozen=True)
class VendorEvidenceProjection:
    """
    A lossy legacy compatibility representation of vendor identity evidence.
    This is NOT authoritative semantic truth, and MUST NOT be treated as
    legal-entity identity probability. It is a structural requirement of the
    Stage 8A/8B scoring engine.
    """
    similarity: Optional[float]
    policy_identity: str
    source_interpretation_identity: str
    
    considered_factors: Tuple[str, ...]
    missing_factors: Tuple[str, ...]
    uninterpretable_factors: Tuple[str, ...]
    
    dependence_groups: Tuple[str, ...]
    contradiction_markers: Tuple[str, ...]
    warnings: Tuple[str, ...]

    @property
    def identity_digest(self) -> str:
        """Deterministic identity for this projection."""
        payload = {
            "schema": "recongraph.vendor_evidence_projection.v1",
            "similarity": self.similarity,
            "policy_identity": self.policy_identity,
            "source_interpretation_identity": self.source_interpretation_identity,
            "considered_factors": list(self.considered_factors),
            "missing_factors": list(self.missing_factors),
            "uninterpretable_factors": list(self.uninterpretable_factors),
            "dependence_groups": list(self.dependence_groups),
            "contradiction_markers": list(self.contradiction_markers),
            "warnings": list(self.warnings),
        }
        
        canonical_bytes = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False
        ).encode("utf-8")
        
        domain_separated = b"recongraph:vendor_evidence_projection:v1\x00" + canonical_bytes
        digest_hex = hashlib.sha256(domain_separated).hexdigest()
        return f"sha256:{digest_hex}"
