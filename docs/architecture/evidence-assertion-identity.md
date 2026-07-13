# Evidence Assertion Identity

This document evaluates whether an `EvidenceAssertion` needs its own identifier.

## Identity Questions

**AI-001 Is equality sufficient to detect exact duplicate assertions?**
Yes, structurally. If two frozen dataclasses have identical fields, they are `==`.

**AI-002 What happens when payload contains explainability metadata?**
If `payload={"explanation": "Matched 3 tokens"}` and another assertion has `payload={"explanation": "Matched three tokens"}`, they are unequal in Python, but semantically identical propositions.

**AI-003 Should two assertions with identical semantics but different explanatory text be equal?**
Yes. Explanation text does not change epistemic truth.

**AI-004 Should magnitudes participate in assertion identity?**
Yes. An assertion that `support=0.9` is fundamentally a different proposition than one that `support=0.2`. (Alternatively, they are the *same* proposition with different confidence. But if a provider upgrades a score, the new assertion replaces the old).

**AI-005 If provider V2 changes support from 0.7 to 0.8, is it the same assertion revised or a new assertion?**
A new assertion. Immutability demands that we don't "update" assertions. We issue new ones from new derivations.

**AI-006 Can deterministic IDs leak sensitive source values?**
Yes, if they hash the payload or observation values directly.

**AI-007 Should raw values ever participate directly in IDs?**
No.

**AI-008 Can semantic identity be separated from assertion instance identity?**
Yes. 

## Evaluation
* **AI-A (No ID):** Relies on `__eq__`. Fails if payload contains non-epistemic fluff (like timestamps or strings).
* **AI-B (Random Assertion UUID):** Safe, but makes testing and deduplication harder.
* **AI-C (Deterministic Content Hash):** Dangerous.
* **AI-D (Deterministic Semantic Key):** `hash(claim, scope, observation_id, provider_id)`. 

## Recommendation
**Neither `assertion_id` nor `semantic_key` as a mandatory primary field.**
Assertions should be pure value objects. However, they must strictly forbid explanation text from residing in the assertion core or the typed payload boundary. If the payload strictly contains *epistemic truth properties*, then standard dataclass `__eq__` (and `__hash__`) is sufficient and mathematically sound. If an ID is needed for a specific graph persistence layer later, it can generate a random UUID on the edge envelope (`EvidenceContribution`), leaving the `EvidenceAssertion` mathematically pure.
