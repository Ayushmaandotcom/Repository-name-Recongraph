# Evidence State Algebra V2

This document challenges the Stage 8C-0C state model by splitting Observation and Interpretation.

## State Separation Analysis

**Is EvidenceState one variable trying to encode two orthogonal dimensions?**
Yes. Whether data is physically present (Observation) is a factual structural reality. Whether an algorithm can extract mathematical meaning from it (Interpretation) is an algorithmic capability.

### Scenario Breakdown
* **PS001 (Valid name, fails legal form extraction):** Observation is `PRESENT`. Lexical interpretation is `INTERPRETED`. Legal-form interpretation is `UNINTERPRETABLE`.
* **PS002 (GSTIN fails checksum):** Observation is `INVALID`. (It is structurally malformed data, not missing data).
* **PS003 (GSTIN valid, unknown jurisdiction):** Observation is `PRESENT`. Interpretation is `UNINTERPRETABLE` for the jurisdiction claim.
* **PS008 (Explicit "UNKNOWN"):** Observation is `INVALID` (or a known null-value proxy).
* **PS009 (Blank):** Observation is `MISSING`.
* **PS010 (Field not in schema):** Observation is `MISSING`.

## Evaluation of State Models
* **ES-A (3 states):** Conflates missing data with invalid data.
* **ES-B (4 states):** Conflates structural validity with algorithmic capability.
* **ES-C (5 states):** Adds `PARTIALLY_INTERPRETABLE`, creating ambiguity (which part failed?).
* **ES-D (Separated Enum):** Creates a clean orthogonal space. 

**Can PARTIALLY_INTERPRETED exist?**
No. If an observation supports multiple claims and one fails, the provider must emit two separate assertions: one `INTERPRETED` and one `UNINTERPRETABLE`. A single assertion must represent exactly one claim, so it must be fully interpreted or uninterpretable for that specific claim.

## Recommendation
**Model ES-D (Separated Enums).**
Stage 8C-0C's state recommendation was fundamentally flawed by category conflation. The kernel requires two distinct properties on the assertion:
1. `ObservationState` (Enum: `PRESENT`, `MISSING`, `INVALID`)
2. `InterpretationState` (Enum: `INTERPRETED`, `UNINTERPRETABLE`)
