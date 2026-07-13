# Stage 8J Semantic Kernel Pre-Mortem

**Scenario:** It is six months from now. Stage 8J Evidence Fusion has failed because the generic Evidence Semantic Kernel was poorly designed.

| Failure | Root Cause | Earliest Detectable Signal | Metamorphic Property Violated | Architectural Seam Required | Cost |
|---|---|---|---|---|---|
| **Claims were too broad** | Modeled `SAME_VENDOR` instead of `SAME_LEGAL_ENTITY` and `SAME_OPERATIONAL_COUNTERPARTY`. | Hard-coding claim logic inside individual providers. | EM-005 Claim Distinction | Extensible Claim Identifier | CATASTROPHIC |
| **Claims were too granular** | Modeled 500 different micro-claims that the fusion engine couldn't aggregate. | Massive switch statements in fusion logic. | EM-014 Provider Extensibility | Claim Hierarchy Registry | HIGH |
| **Claim enum prevented plugin extensibility** | Used Python `Enum` for claims. | 3rd-party plugin crashes core on import. | EM-014 Provider Extensibility | String-backed Value Object | CATASTROPHIC |
| **Support was mistaken for probability** | Multiplied independent support values leading to 0.0001 scores. | Explanation texts saying "90% match". | EM-015 No Probability Claim | `support_magnitude` field name | HIGH |
| **Conflict was treated as 1 - support** | Missing data caused `support=0`, which became `conflict=1`. | High rejection rate on sparse data. | EM-007 Support/Conflict Independence | Explicit Bipolar Modeling | CATASTROPHIC |
| **Missing evidence was serialized as zero evidence** | No explicit `EvidenceState` enum. | `support=0.0` inside JSON trace without context. | EM-009 State Preservation | `EvidenceState` Enum | CATASTROPHIC |
| **Uninterpretable evidence was treated as missing** | OCR garbage fell back to `None`. | Model blindness to its own limitations. | EM-010 Uninterpretable Preservation | `UNINTERPRETABLE` State | MEDIUM |
| **Authority became a hidden weight** | Multiplied `support * 0.8` for OCR. | Loss of epistemic source in trace. | EM-019 Authority Non-Numericity | Authority Descriptor | HIGH |
| **Lineage fields existed but providers populated them incorrectly** | Passed `correlation_group="vendor"` for all inputs. | Everything clustered together in fusion. | EM-004 Provenance Distinction | Structured Source Lineage | MEDIUM |
| **Shared provenance was mistaken for measured statistical dependence** | Used covariance matrices without calibration data. | Bizarre fusion behavior, over-penalizing corroborated evidence. | N/A (Math Error) | Dependence Terminology Ban | CATASTROPHIC |
| **Typed payload versions became impossible to replay** | Altered `VendorPayload` schema without versioning. | Benchmark runner crashes on old traces. | EM-012 Payload Version Preservation | `schema_version` | HIGH |
| **Unknown plugin payloads crashed trace readers** | Used strict Pydantic parsing for all payloads in core. | Core crashes when plugin disabled. | EM-013 Unknown Payload Safety | Tagged Serializable Union | CATASTROPHIC |
| **Vendor and GSTIN targeted different identity claims** | GSTIN asserted `SAME_GST_REGISTRATION`, Name asserted `SAME_LEGAL_ENTITY`. Fusion didn't know how to link them. | Ignored GSTINs entirely. | EM-016 Claim-Local Conflict | Claim Logic Registry | HIGH |
| **Fusion combined evidence across incompatible claims** | Added Amount Support to Name Support. | Apples-to-oranges score summation. | EM-005 Claim Distinction | Type-Safe Fusion | CATASTROPHIC |
| **Explanation Builder translated claim-specific evidence into generic "strong match" language** | Ignored the `claim_id` when rendering text. | User sees "Strong Match" when tax IDs conflict. | EM-001 Claim Preservation | Claim-Aware Templates | HIGH |
