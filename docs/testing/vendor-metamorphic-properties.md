# Metamorphic Identity Properties

## VM-001 — Case Invariance
* **Preconditions:** Two identical vendor names differing only by case.
* **Transformation:** Change case of Name A.
* **Expected Invariant:** Lexical identity support must remain identical.
* **Failure Meaning:** The normalization or embedding model is case-sensitive, which is fragile for financial OCR.
* **Future Test Layer:** Normalization Unit Tests.

## VM-002 — Harmless Whitespace Invariance
* **Preconditions:** Vendor name with standard spaces.
* **Transformation:** Inject extra spaces, tabs, or newlines.
* **Expected Invariant:** Lexical identity support remains identical.
* **Failure Meaning:** Brittle string matching.
* **Future Test Layer:** Normalization Unit Tests.

## VM-003 — Symmetry
* **Preconditions:** A vs B yields Evidence E.
* **Transformation:** Swap to B vs A.
* **Expected Invariant:** Yields exactly Evidence E.
* **Failure Meaning:** Directional bias in matching logic, preventing true commutative scoring.
* **Future Test Layer:** Pair Scorer Property Tests.

## VM-004 — Authoritative Conflict Preservation
* **Preconditions:** A vs B yields Strong Lexical Support.
* **Transformation:** Add conflicting Tax IDs to A and B.
* **Expected Invariant:** Strong Lexical Support is preserved AND Strong Authoritative Conflict is added. The final hypothesis MUST reflect the conflict.
* **Failure Meaning:** The engine collapses the conflict into a "medium" score, hiding a potential fraud or data error from the user.
* **Future Test Layer:** Hypothesis Evaluator Integration Tests.

## VM-005 — Missingness Non-Contradiction
* **Preconditions:** Record A has no Vendor Name. Record B has no Vendor Name.
* **Transformation:** Compare A vs B.
* **Expected Invariant:** The evidence contribution is ZERO conflict and ZERO support. It is purely absent.
* **Failure Meaning:** If this produces `0.0` (conflict) as it does today, the system actively contradicts the match based on ignorance.
* **Future Test Layer:** Evidence Provider Tests.

## VM-006 — Generic Token Replication
* **Preconditions:** Token `TRADERS` appears 5 times in corpus. Score for A vs B on `TRADERS` is S.
* **Transformation:** Add 100 more unique entities containing `TRADERS` to corpus.
* **Expected Invariant:** Score S must decrease or remain constant; it must NOT increase.
* **Failure Meaning:** The model rewards generic terms instead of penalizing them.
* **Future Test Layer:** Corpus Profiler Tests.

## VM-007 — Corpus Replication Invariance
* **Preconditions:** Entity X appears 1 time.
* **Transformation:** Duplicate all records in the corpus exactly 10 times.
* **Expected Invariant:** The rarity/discriminative weight of Entity X's tokens must remain unchanged.
* **Failure Meaning:** The profiler is counting raw documents instead of distinct identities.
* **Future Test Layer:** Corpus Profiler Tests.

## VM-008 — Provenance Preservation
* **Preconditions:** Same evidence magnitude derived from OCR vs ERP.
* **Transformation:** Alter the evidence source system string.
* **Expected Invariant:** The correlation_group or lineage metadata must reflect the change.
* **Failure Meaning:** Evidence fusion cannot detect that two signals are actually the same signal.
* **Future Test Layer:** Evidence Lineage Tests.

## VM-009 — Exact Lexical Equality Does Not Prove Legal Identity
* **Preconditions:** Exact name match `ABC LTD` vs `ABC LTD`.
* **Transformation:** Provide conflicting GSTINs.
* **Expected Invariant:** Legal Identity is CONTRADICTED despite Lexical Identity being SUPPORTED.
* **Failure Meaning:** Vendor similarity overrides authoritative tax identity.
* **Future Test Layer:** Decision Engine Tests.

## VM-010 — Alias Knowledge Monotonicity
* **Preconditions:** `TCS` vs `TATA CONSULTANCY SERVICES` with Tax ID conflict.
* **Transformation:** Add alias mapping `TCS -> TATA CONSULTANCY SERVICES` to domain knowledge.
* **Expected Invariant:** Lexical Support increases, but Tax ID Conflict remains EXACTLY as strong.
* **Failure Meaning:** Knowing they are aliases erased the fact that their tax IDs contradict.
* **Future Test Layer:** Evidence Fusion Tests.
