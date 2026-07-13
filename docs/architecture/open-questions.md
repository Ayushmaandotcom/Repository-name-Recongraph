# Open Architecture Questions

This document tracks intentional architectural deferrals, unresolved boundaries, and known limitations that were deliberately out-of-scope for the v0.1 release of ReconGraph.

Good architecture isn't just documenting decisions—it's documenting the decisions we intentionally *didn't* make.

## Reference Evidence Interpretation

* **Continuous Coverage**: `statistical_coverage` is binary (0.0 or 1.0) in v0.1 due to the strongest-unit selection model. If a future strategy aggregates multiple tokens (e.g., probabilistic union), coverage mapping may need to become continuous.
* **Joint DF Statistics**: Token independence is not assumed. The current model does not mathematically combine probabilities for multiple tokens because marginal document frequencies (`df(A)`) do not provide enough statistical justification for `df(A ∩ B)`. 
* **Probabilistic Accumulation**: We currently use magnitude-based selection rather than probability calculation. Does the system eventually need a true Bayesian or probabilistic model for accumulating confidence?
* **Exact-Reference Fallback Calibration**: The default heuristic magnitude for an out-of-profile exact identity match is currently locked at `0.60`. This may require empirical calibration against real dataset baselines.
* **Serialization Strategy**: The `ReferenceEvidenceInterpretation` object drops the explicit `selected_contribution` reference to avoid standard dataclass serialization/deserialization issues (JSON recreating objects and breaking Python's `is` checks). The strict serialization boundaries for evidence lineage remain unresolved.
* **Group-Level Evidence Accumulation**: v0.1 focuses on pair-level compatibility. Expanding this to evaluate reconciliation groupings across the graph remains deferred.
