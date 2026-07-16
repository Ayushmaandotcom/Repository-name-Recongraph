# ADR-012: Missingness Semantics

## Status
Active

## Context
When evidence is absent (e.g., a blank GSTIN field on an invoice), it is often treated as a `None` scalar, leading to null-pointer exceptions or silent bypasses in legacy systems. We must strictly define the epistemic meaning of absence.

## Decision
We categorize Missingness into 5 ontological states:
1. `Missing`: Silent absence. `Support = 0`, `Contradict = False`.
2. `Unknown`: Parsing failure. Triggers review warning.
3. `Invalid`: Cryptographic/Checksum failure. Tags record for Data Quality issues, then treats as `Missing`.
4. `Not Applicable`: Logically impossible domain. Filtered from the Graph.
5. `Contradictory Missingness`: Explicit assertion of absence vs explicit assertion of presence. Elevates to `Contradiction`.

## Consequences
- The Fusion layer must natively propagate Missingness states. Missing domains reduce the maximum obtainable `Compatibility` score.
- An `AUTO_MATCH` decision cannot be reached if structurally mandatory orthogonal edges (like Tax and Financial) are completely missing.
