# Evidence Assertion Kernel Pre-Mortem V2

**Scenario:** We built the Stage 8C-0C kernel. Stage 8J (Fusion) still failed catastrophically six months later.

| Failure | Root Cause | Earliest Detection | Required Metadata | Metamorphic Property | Stage 8J Consequence | Reversal Cost |
|---|---|---|---|---|---|---|
| **Assertions lacked subject scope.** | Kernel only modeled claim, magnitude, state. | Fusing pairwise evidence with group evidence blindly. | `AssertionScope` | EM2-001 | Fuses evidence for unrelated hypotheses. | CATASTROPHIC |
| **Subject ordering changed equality.** | Scope was a tuple `(P1, G1)`. | Claim `A↔B` didn't match `B↔A`. | `is_symmetric` | EM2-003 | Misses duplicate evidence. | HIGH |
| **Symmetric claims were treated directionally.** | Claim lacked symmetry metadata. | `A↔B` fused independently from `B↔A`. | `ClaimDescriptor` | EM2-003 | Overconfidence / double counting. | HIGH |
| **Directional claims were canonicalized.** | Scope automatically sorted left/right. | `A supersedes B` became `B supersedes A`. | `ClaimDescriptor` | EM2-004 | Reverses causal logic. | CATASTROPHIC |
| **Unknown plugin claims were fused.** | String ID passed through blindly. | Unknown claims summed into random buckets. | `ClaimDescriptor` | EM2-018 | Corrupts fusion math. | CATASTROPHIC |
| **Same observation generated duplicated evidence.** | No `ObservationIdentity`. | Name & normalized name both added 0.8 support. | `ObservationID` | EM2-005 | Extreme overconfidence. | CATASTROPHIC |
| **Normalized and raw name evidence were double counted.** | Same as above. | | | | | |
| **Provider V1 and V2 outputs were fused together.** | Trace replay loaded both versions into one hypothesis. | `ProviderSemanticVersion` | EM2-006 | Double counting. | HIGH |
| **Pairwise and group-level evidence were combined directly.** | Scope size ignored during fusion. | `AssertionScope` | EM2-009 | Apples-to-oranges addition. | CATASTROPHIC |
| **Observation state and interpretation state were conflated.** | Used one `EvidenceState` enum. | `INVALID` GSTIN treated same as `MISSING` GSTIN. | Split Enums | EM2-011 | Ignored explicit malformed data. | HIGH |
| **Invalid identifiers were treated as uninterpretable.** | See above. | | | | | |
| **Missing fields were treated as invalid.** | See above. | | | | | |
| **Authority metadata duplicated observation quality inconsistently.** | `AuthorityDescriptor` was poorly defined. | `EvidenceQualityContext` | N/A | Ignored OCR errors. | MEDIUM |
| **Support magnitudes from incompatible scales were compared.** | Universal magnitude assumption. | `MagnitudeContract` | EM2-017 | Bizarre math behavior. | CATASTROPHIC |
| **0.9 was interpreted as probability.** | No calibration. | UI showed "90% match". | Documentation | EM-015 | Breaks user trust. | HIGH |
| **Payload schema version was mistaken for claim semantic version.** | Schema V2 caused Claim to act like V2. | `ClaimDescriptor` | EM2-015 | Breaks old traces. | HIGH |
| **Provider version was mistaken for engine version.** | Trace metadata was insufficient. | `DerivationMetadata` | EM2-016 | Trace lies about what ran. | MEDIUM |
| **Historical trace could not explain old assertions.** | Payload failed to deserialize, dropped assertion. | Tagged Union | EM2-019 | Irrecoverable traces. | CATASTROPHIC |
| **Content hashes leaked business-sensitive values.** | Hashed Vendor Name in `ObservationID`. | Security Audit. | Structural ID | N/A | Security Incident. | HIGH |
| **V1 scalar adapter re-entered the V2 evidence graph.** | Adapter logic was circular. | Projection rules | EM2-020 | Infinite loop / double score. | HIGH |
