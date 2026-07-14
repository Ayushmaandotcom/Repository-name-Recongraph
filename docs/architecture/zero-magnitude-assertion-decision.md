# Zero Magnitude Assertion Decision

## Summary
Zero-magnitude assertions (`0.0`) are redundant and semantically empty. They are forbidden.

## Decision
Adopt Model ZM-B. Magnitude range is `(0.0, 1.0]`. An evaluated path yielding no evidence is represented by `EvidenceInterpretationResult` with `state=INTERPRETED` and an empty `assertions` tuple.
