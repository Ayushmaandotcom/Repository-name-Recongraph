# Evidence Fusion Design Report (Stage 8I)

This document synthesizes the overarching fusion strategy, covering Double-Counting, Mathematical Models, Adversarial Falsification, and Final Recommendations.

## Phase 4: Double Counting Falsification

Adversarial scenarios designed to prevent synthetic certainty.

1. **Same PAN observed twice**
   - **Scenario:** The Vendor Name provider fuzzy-matches two names, and the Tax Identity provider exactly matches the PAN extracted from two GSTINs.
   - **Handling:** Since Vendor is highly correlated with PAN, the Fusion layer must **Sub-additively** accumulate this. Support increases marginally, but not linearly.
2. **Same GSTIN observed three ways**
   - **Scenario:** E-Invoice, GST Returns, and Purchase Register all log identical GSTINs.
   - **Handling:** Duplicate edge. Support remains **Constant**. Three instances of the identical artifact from non-orthogonal sources do not mathematically compound.
3. **Invoice number repeated in two datasets**
   - **Scenario:** Reference pipeline perfectly aligns.
   - **Handling:** Highly orthogonal to identity. Support increases independently.

## Phase 10: Mathematical Fusion Model

Comparative analysis of candidate models for the Evidence Graph.

| Model | Advantages | Failure Modes | Determinism | Explainability | Complexity |
|-------|------------|---------------|-------------|----------------|------------|
| **Weighted Additive Support** | Easy to implement. | Massive double-counting risk. Cannot represent vetos effectively. | High | High | Low |
| **Rule-Based (Current)** | Simple to audit. Rigid guarantees. | Scales poorly. Combinatorial explosion of rules as providers increase. | High | High | Medium |
| **Dempster-Shafer (Belief Accumulation)** | Mathematically formalizes missingness vs. contradiction vs. support. | Extremely difficult to explain to end-users (Probability masses). | High | Low | High |
| **Graph Propagation (Constraint Satisfaction)** | **Recommended:** Naturally handles topological dependencies, derived edges, and structural vetos. | Requires complex cyclic checks. | High | Very High (Path Tracing) | Medium |

**Selection:** A Topological Constraint Satisfaction Graph. Support propagates through independent edges and is throttled by derived edges. Contradictions act as constraints that block propagation.

## Phase 11: Adversarial Falsification Plan

Before implementing production fusion, we will execute this adversarial test suite:

**100 Conformance Scenarios:**
- Prove baseline deterministic evaluation of exact matching, 1-character typos, and standardized dates.

**50 Adversarial Scenarios:**
- Test 1: Contradictory GSTINs but exact Vendor match. (Must Veto)
- Test 2: Identical Dates and Amounts, but distinct Vendor. (Must Veto)
- Test 3: Missing Tax, Missing Vendor, Identical Amount. (Must Review)

**50 Metamorphic Properties:**
- Permutation Invariance: Changing the order of node addition to the `EvidenceGraph` must yield identical `FusionResult`.
- Duplication Idempotency: Adding a `DuplicateEdge` must not alter `Compatibility`.

## Phase 14: Final Architectural Review

**Open Architectural Questions:**
1. How should we serialize the `EvidenceGraph` into the `DecisionTrace` without bloating the storage footprint?
2. Does Constraint Satisfaction negatively impact latency for large candidate pools (e.g. 1-to-N matching)?

**Known Risks:**
- **Double Counting:** Remains the largest epistemic risk if the Dependency Graph (`DerivedEdge`) is inaccurately modeled.

**Recommended Implementation Order (Stage 8J):**
1. Implement the `EvidenceGraph` topology classes (DAG construction).
2. Implement `FusionNode` and `FusionEdge` mapping from `EvidenceContributionV2`.
3. Implement the Topological Constraint Satisfaction Engine.
4. Replace the legacy `PairScorer` aggregation with the `FusionEngine`.
