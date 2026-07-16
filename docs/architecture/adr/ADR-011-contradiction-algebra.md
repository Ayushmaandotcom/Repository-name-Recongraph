# ADR-011: Contradiction Algebra

## Status
Active

## Context
When multi-evidence domains interact, they frequently disagree. Intuition-based or heuristic resolution of these disagreements leads to non-deterministic, hard-to-audit bugs (e.g. allowing an exact Tax PAN match to override an out-of-tolerance Financial amount mismatch). 

## Decision
We formally adopt a Contradiction Algebra.

1. **Veto Supremacy**: A definitive contradiction on an `IndependentEdge` (e.g., Financial Amount, Tax Identity) acts as an absolute veto. The entire Candidate Hypothesis is marked `INELIGIBLE`, overriding any aligned support.
2. **Orthogonal Conflict Override**: A strict Tax contradiction permanently overrides a fuzzy Vendor support, because Vendor is probabilistically derived from Tax identity.
3. **Missingness Immunity**: `Missing` data NEVER triggers a contradiction. 

## Consequences
- The Fusion layer evaluates Constraints (Contradictions) before evaluating Support (Compatibility).
- A single strict contradiction blocks the `FusionNode` from passing Compatibility to the final `FusionResult`.
