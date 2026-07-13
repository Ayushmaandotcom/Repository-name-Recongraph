# Metamorphic Properties for the Semantic Kernel V2

## Scope & Identity Properties

**EM2-001 — Scope Preservation**
* **Precondition:** Valid Assertion.
* **Transformation:** Change magnitude from 0.5 to 0.9.
* **Invariant:** `AssertionScope` remains identical.
* **Failure:** Scope is functionally linked to confidence.

**EM2-002 — Scope Distinction**
* **Precondition:** Two scopes: P1↔G1 and P1↔{G1,G2}.
* **Transformation:** Generate assertions for both with identical claim and magnitude.
* **Invariant:** Assertions are not `__eq__`.
* **Failure:** Graph context destroyed.

**EM2-003 — Symmetric Canonicalization**
* **Precondition:** Claim is marked `is_symmetric=True`.
* **Transformation:** Create Scope(Left=A, Right=B) and Scope(Left=B, Right=A).
* **Invariant:** `AssertionScope` objects are structurally identical (e.g., frozensets).
* **Failure:** Duplicate symmetric logic creates two independent assertions.

**EM2-004 — Directional Preservation**
* **Precondition:** Claim is marked `is_symmetric=False`.
* **Transformation:** Create Scope(Left=A, Right=B) and Scope(Left=B, Right=A).
* **Invariant:** `AssertionScope` objects are NOT equal.
* **Failure:** Graph directionality destroyed.

**EM2-005 — Observation Distinction**
* **Precondition:** Two distinct fields on the same document yield identical payload strings.
* **Transformation:** Create assertions for both.
* **Invariant:** `ObservationIdentity` differs.
* **Failure:** Independent observations collapsed into one.

**EM2-006 — Derivation Distinction**
* **Precondition:** Same input processed by Provider V1 and V2.
* **Transformation:** V1 and V2 output identical assertions.
* **Invariant:** `ProviderSemanticVersion` distinguishes them.
* **Failure:** Ambiguous trace history.

**EM2-007 — Exact Duplicate Detectability**
* **Precondition:** Two identical assertions generated.
* **Transformation:** Compare via `==`.
* **Invariant:** Returns `True`.
* **Failure:** Uncontrolled instance generation (e.g. random UUIDs inside dataclass).

**EM2-008 — Derived Sibling Preservation**
* **Precondition:** Two assertions from the same raw field.
* **Transformation:** Check `ObservationIdentity`.
* **Invariant:** IDs are strictly equal.
* **Failure:** Cannot detect double-counting vulnerability.

**EM2-009 — Pair/Group Non-Equivalence**
* **Precondition:** Pair scope and Group scope.
* **Transformation:** `==` check.
* **Invariant:** Returns `False`.
* **Failure:** Apples-to-oranges fusion.

**EM2-010 — Overlapping Scope Non-Identity**
* **Precondition:** {P1, P2} ↔ G1 and {P2, P3} ↔ G1.
* **Transformation:** `==` check.
* **Invariant:** Returns `False`.

## State & Semantics Properties

**EM2-011 — Observation State Independence**
* **Precondition:** Change `ObservationState` from `PRESENT` to `INVALID`.
* **Transformation:** Re-evaluate assertion.
* **Invariant:** `InterpretationState` may change to `UNINTERPRETABLE`, but the states remain distinct fields.

**EM2-012 — Interpretation State Independence**
* **Precondition:** Interpretation throws error.
* **Transformation:** Check `ObservationState`.
* **Invariant:** Remains `PRESENT`.
* **Failure:** Algorithmic failure rewrites factual data presence.

**EM2-013 — Invalid Observation Non-Support**
* **Precondition:** `ObservationState` = `INVALID`.
* **Transformation:** Check magnitude.
* **Invariant:** `support_magnitude` == 0.0 (unless claim explicitly targets invalidity).
* **Failure:** Garbage-in produces positive support.

**EM2-014 — Claim Semantic Version Preservation**
* **Precondition:** Serialize and deserialize.
* **Transformation:** Check `semantic_version`.
* **Invariant:** Matches original.

**EM2-015 — Payload Version Independence**
* **Precondition:** Bump payload `schema_version`.
* **Transformation:** Check `ClaimDescriptor.semantic_version`.
* **Invariant:** Unchanged.

**EM2-016 — Provider Version Preservation**
* **Precondition:** Serialize and deserialize.
* **Transformation:** Check `provider_semantic_version`.
* **Invariant:** Matches original.

**EM2-017 — Magnitude Contract Preservation**
* **Precondition:** Assert magnitude 0.8.
* **Transformation:** Check context.
* **Invariant:** Contract ID (e.g., `rarity_v1`) is accessible.

**EM2-018 — Unknown Claim Non-Fusion**
* **Precondition:** `claim_id = custom.future_claim`.
* **Transformation:** Stage 8J attempts to sum.
* **Invariant:** Engine raises error or explicitly skips.
* **Failure:** Blind math.

**EM2-019 — Unknown Payload Core Preservation**
* **Precondition:** Deserialize trace without Python dataclass definition.
* **Transformation:** Read `claim_id` and `support_magnitude`.
* **Invariant:** Core fields are fully available and correct.
* **Failure:** Trace reader crash.

**EM2-020 — V1 Adapter Non-Reentry**
* **Precondition:** V2 Assertion -> V1 Scalar -> V2 Assertion.
* **Transformation:** Re-insert into graph.
* **Invariant:** Fails validation or explicitly marked as projection.
* **Failure:** Infinite feedback loop.
