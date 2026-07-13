# Typed Evidence Semantic Kernel Design

This document designs the smallest generic evidence semantic kernel.

## Kernel Design Questions

**SK-001 Should support and conflict be bounded [0.0, 1.0]?**
Yes. For mathematical stability, bounded magnitudes prevent unbounded divergence.

**SK-002 Can support and conflict both be non-zero?**
Yes. (e.g., Lexical support but Tax ID conflict).

**SK-003 Can both equal 1.0?**
Yes. A model might be 100% certain names match, and 100% certain tax IDs contradict.

**SK-004 Should the kernel forbid support + conflict > 1.0?**
No. They are independent magnitudes on independent evidence axes (often stemming from different attributes of the observation), not complementary probabilities.

**SK-005 Does support/conflict require normalization?**
No. Normalization enforces a probability distribution, which implies exclusivity. Support for A does not reduce Conflict against A.

**SK-006 Should magnitude fields be named `support_magnitude` and `conflict_magnitude` to prevent probability interpretation?**
Yes, this is an excellent naming defense.

**SK-007 Can MISSING evidence carry non-zero support?**
No. That is a strict semantic violation.

**SK-008 Can UNINTERPRETABLE evidence carry conflict?**
No. If it cannot be interpreted, it cannot contradict.

**SK-009 Can OBSERVED evidence have zero support and zero conflict?**
Yes. (e.g. Neutral evidence, `TRADERS`).

**SK-010 Does the kernel need `statistics_available`?**
No. That is a property of the specific observation (e.g. token rarity), which belongs in the typed payload.

**SK-011 Does the kernel replace `EvidenceContributionV2`?**
No. The contribution is the transport envelope; the semantic assertion is the payload.

**SK-012 Or should `EvidenceContributionV2` contain semantic output?**
Yes. 

**SK-013 Does `provider_id` belong in lineage or contribution metadata?**
Contribution metadata. The provider is the agent that made the assertion, not the source of the data itself.

**SK-014 How is schema version represented?**
Via a string/int on the Payload, or implicitly by the Python type name if using a registry.

**SK-015 Can the kernel be JSON serialized without custom object identity assumptions?**
Yes, if it relies purely on standard primitives and strings.

## Candidate Object Models

### Kernel A — Expand EvidenceContributionV2
Add `claim`, `support`, `conflict`, `state` directly to the `EvidenceContribution` class.
* **Flaw:** Conflates the graph's container requirements with the semantic truth of the assertion.

### Kernel B — EvidenceContributionV2 Contains EvidenceSemantics
`EvidenceContribution(..., semantics=EvidenceSemantics(...))`
* **Flaw:** What if a provider wants to assert *two* claims from one observation?

### Kernel C — Generic Typed EvidenceContribution[T_Payload]
Focuses on typing the payload, but leaves the semantic assertion structure loosely defined.
* **Flaw:** Does not formalize the claim ontology at the core level.

### Kernel D — Claim-Centric EvidenceAssertion
```python
@dataclass(frozen=True)
class EvidenceAssertion:
    claim: str # typed claim id
    support_magnitude: float
    conflict_magnitude: float
    state: EvidenceState
    authority: EvidenceAuthority
    lineage: EvidenceLineage
    payload: Any # Typed via payload protocol
```
A provider returns `list[EvidenceAssertion]`. The `EvidenceContribution` wraps these assertions for graph insertion.

## Recommendation
**Kernel D (Claim-Centric EvidenceAssertion).** It completely decouples the epistemic truth (the assertion) from the graph's transport mechanism (the contribution). A single plugin can observe one document and emit multiple independent assertions (e.g. one for `legal_entity`, one for `financial_conservation`).
