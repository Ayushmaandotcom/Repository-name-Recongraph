# Evidence Assertion Ancestry Decision

## Summary
An `EvidenceAssertion` represents a single semantic claim. It must reference exactly one valid semantic ancestry root (`EvidenceAncestryRef`).

## AAQ Questions

**AAQ001 What exactly does an assertion reference?**
Exactly one `EvidenceAncestryRef`.

**AAQ002 Does it reference an object or stable identity?**
Stable identity.

**AAQ003 Does ObservationOccurrence have stable identity?**
Yes, introduced as `ObservationOccurrenceIdentity`.

**AAQ004 Does DerivationExecution have stable identity?**
Yes, renamed and introduced as `DerivationOccurrenceIdentity`.

**AAQ015 Can one assertion have multiple ancestry roots?**
No. Multi-parent derivation converges into a single `DerivationOccurrence`.

**AAQ020 Final model.**
`EvidenceAssertion` contains `ancestry: EvidenceAncestryRef` wrapping a `KernelIdentityRef`. Only `observation_occurrence` and `derivation_occurrence` domains are permitted in v1 core.
