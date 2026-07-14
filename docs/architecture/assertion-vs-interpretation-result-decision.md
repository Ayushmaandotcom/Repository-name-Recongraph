# Assertion vs Interpretation Result Decision

## Summary
Missingness and interpretability are properties of the attempt to evaluate evidence, not the semantic claim itself.

## Model Chosen
Model C (Interpretation envelope).

`EvidenceInterpretationResult` encapsulates:
- `EvidenceInterpretationState`
- A unique, canonically ordered tuple of `EvidenceAssertion`s.

If state is NOT `INTERPRETED`, the assertions tuple MUST be empty. If it is `INTERPRETED`, the tuple may be empty (evaluated, but no assertion produced).
