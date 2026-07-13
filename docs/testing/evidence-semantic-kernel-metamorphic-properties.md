# Metamorphic Properties for the Semantic Kernel

## Core Properties

**EM-001 — Claim Preservation**
* **Transformation:** Change `support_magnitude` from 0.5 to 0.9.
* **Invariant:** `claim_id` must remain unchanged.
* **Failure:** Magnitude updates alter semantic target.

**EM-002 — Missingness Non-Support**
* **Transformation:** Compare two missing fields.
* **Invariant:** `support_magnitude` == 0.0.
* **Failure:** Missing data hallucinated as positive match.

**EM-003 — Missingness Non-Conflict**
* **Transformation:** Compare two missing fields.
* **Invariant:** `conflict_magnitude` == 0.0.
* **Failure:** Ignorance penalized as contradiction.

**EM-004 — Provenance Distinction**
* **Transformation:** Generate exactly identical semantic output from two different source documents.
* **Invariant:** The `lineage` field distinguishes them.
* **Failure:** Double-counting vulnerability.

**EM-005 — Claim Distinction**
* **Transformation:** Exact Name Match vs Exact GSTIN Match.
* **Invariant:** Generate different `claim_id`s.
* **Failure:** Conflating string types.

**EM-006 — Authority Distinction**
* **Transformation:** Name match from ERP vs OCR.
* **Invariant:** Generate different `authority` descriptors.
* **Failure:** Loss of epistemic trust context.

**EM-007 — Support/Conflict Independence**
* **Transformation:** Increase `support_magnitude`.
* **Invariant:** `conflict_magnitude` does not automatically decrease (unless explicit math requires it).
* **Failure:** Forced probability exclusivity.

**EM-008 — Conflict Preservation**
* **Transformation:** Add a weak name match (low authority) to a record with a mismatched tax ID (high authority).
* **Invariant:** The tax ID conflict assertion remains intact in the payload.
* **Failure:** Lower authority support erases higher authority conflict.

**EM-009 — Observation State Preservation**
* **Transformation:** Evaluate a ubiquitous token (`TRADERS`) vs Missing data.
* **Invariant:** `TRADERS` state is `OBSERVED` (mag=0.0). Missing state is `MISSING`.
* **Failure:** Both collapse to `None` or `0.0` without state.

**EM-010 — Uninterpretable Preservation**
* **Transformation:** Evaluate unparseable text vs Missing data.
* **Invariant:** States `UNINTERPRETABLE` vs `MISSING` remain distinct.
* **Failure:** Information loss regarding model capability.

**EM-011 — Serialization Round Trip**
* **Transformation:** `Assertion -> JSON -> Assertion`.
* **Invariant:** All fields (claim, state, magnitudes, authority, lineage) are identical.
* **Failure:** Trace replay fails.

**EM-012 — Payload Version Preservation**
* **Transformation:** Serialize payload.
* **Invariant:** `schema_version` is present in JSON.
* **Failure:** Future breaking changes crash readers.

**EM-013 — Unknown Payload Safety**
* **Transformation:** Deserialize a trace with an unknown `payload_type`.
* **Invariant:** Yields a generic dictionary or stub without crashing.
* **Failure:** Forward incompatibility.

**EM-014 — Provider Extensibility**
* **Transformation:** Introduce `CUSTOM_CLAIM_123`.
* **Invariant:** No `Enum` in core engine throws `ValueError`.
* **Failure:** Hardcoded claim registry.

**EM-015 — No Probability Claim**
* **Transformation:** Print representation of assertion.
* **Invariant:** Output does not say "90% Probability". It says "Support Magnitude 0.9".
* **Failure:** Misleading calibration statements.

**EM-016 — Claim-Local Conflict**
* **Transformation:** Conflict on `SAME_GST_REGISTRATION`.
* **Invariant:** Does not automatically populate conflict on `SAME_LEGAL_ENTITY` inside the core kernel. (That requires fusion rules).
* **Failure:** Premature logical entailment.

**EM-017 — Symmetry Where Applicable**
* **Transformation:** Evaluate A vs B, then B vs A.
* **Invariant:** Output semantic assertion is identical.
* **Failure:** Directional bias in pair scoring.

**EM-018 — Directionality Preservation**
* **Transformation:** Evaluate Historical Predecessor A vs Successor B.
* **Invariant:** If explicitly directional, reversing order produces a different assertion.
* **Failure:** Forced symmetry destroys temporal facts.

**EM-019 — Authority Non-Numericity**
* **Transformation:** Upgrade `Authority` from `OCR` to `SYSTEM_OF_RECORD`.
* **Invariant:** `support_magnitude` does not mathematically change inside the semantic assertion (though downstream fusion may weigh it differently).
* **Failure:** Authority conflated with observation magnitude.

**EM-020 — Fusion Absence**
* **Transformation:** Add two assertions together.
* **Invariant:** The semantic kernel class does not implement `__add__` to produce a fused decision.
* **Failure:** Local greedy fusion bypassing the global engine.
