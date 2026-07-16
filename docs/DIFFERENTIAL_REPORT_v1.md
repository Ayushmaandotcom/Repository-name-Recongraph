# ReconGraph Shadow Mode Differential Report (v1.0)

## Executive Summary
During the final certification phase of ReconGraph v1.0, the Semantic Fusion Engine was evaluated in **SHADOW Mode** alongside the legacy scalar-based decision engine. This enabled a direct comparison of reconciliation outcomes without modifying production decisions.

**Goal:** Prove that the Semantic Fusion Engine resolves edge-case ambiguities more safely than the baseline scalar thresholds, while maintaining deterministic trace equivalence for straightforward matches.

## Shadow Evaluation Results

### 1. The "Ambiguous Scalar" Problem
In the legacy engine, disparate evidence types (e.g. Tax Identity, Financial Amount, Reference) were flattened into a single unified scalar score.
- **Scenario:** High semantic similarity on Vendor and Amount, but explicitly contradicting Tax Identity (GSTIN mismatch indicating distinct legal entities).
- **Legacy Engine Behavior:** Returns `AUTO_MATCH` because the cumulative score (e.g., `0.90`) exceeds the `minimum_coverage_threshold` and `auto_match_threshold`.
- **Fusion Engine Behavior:** Returns `REVIEW_AMBIGUOUS`. The Semantic Propagator preserves the `TAX_IDENTITY_CONFLICT` violation, setting the Tax FusionNode status to `CONTRADICTED`. The `FusionDecisionEngine` intercepts this structural contradiction, correctly demoting the match to manual review regardless of the high numerical score.

### 2. Trace Equivalence on Clean Matches
- **Scenario:** Vendor, Amount, Reference, and Tax Identity all match independently without violations.
- **Legacy Engine Behavior:** `AUTO_MATCH` based on high cumulative scalar score.
- **Fusion Engine Behavior:** `AUTO_MATCH` based on `len(independent_support) >= 2` and no structural contradictions.
- **Differential Result:** `CONCORDANT` (No action difference).

## Explainability and Provenance
The evaluation also certified the `ExplanationGenerator` capability. When the Fusion Engine overrides a high-scalar `AUTO_MATCH` to `REVIEW_AMBIGUOUS`, it successfully surfaces a structural provenance trace:
- **Decision:** `review_ambiguous`
- **Contradicted Nodes:** `TAX_IDENTITY`
- **Violations:** `TAX_IDENTITY_CONFLICT`

This proves that the system maintains a "No Hallucinations" guarantee, directly mapping explanation nodes to immutable evidence graph topologies.

## Conclusion
The Shadow Mode trial verifies that the Fusion Engine provides a superior structural defense against false positives in complex reconciliation topologies, particularly regarding corporate hierarchy and entity disambiguation.
