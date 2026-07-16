# ADR-013: Fusion Decision Semantics

## Status
Active

## Context
ReconGraph's ultimate output is a decision on a candidate pair (e.g., `AUTO_MATCH`, `REVIEW_AMBIGUOUS`). We need to precisely define the mathematical quantity that drives this decision.

## Decision
We formally adopt `Compatibility` as the core semantic metric of the Fusion layer.

We explicitly reject the terms "Confidence" or "Probability", as they imply statistical frequencies over ensembles that ReconGraph does not possess. 

`Compatibility` is defined as:
The degree of structural alignment between two records as observed through independent deterministic pipelines, normalized against the Topological Dependency Graph to prevent double-counting.

It is strictly bounded to `[0.0, 1.0]`.

## Consequences
- The Fusion Engine will calculate a single `Compatibility` score for every `EvidenceGraph`.
- The `DecisionEngine` policies will evaluate `Compatibility` alongside `Contradictions` and `Missingness` to emit the final `DecisionAction`.
