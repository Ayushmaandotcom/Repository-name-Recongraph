# Trace Serialization Schema V1

## Purpose
The `DecisionTrace` represents the immutable historical record of an entire reconciliation execution. Its identity contract (TRACE-003) demands that the trace identity uniquely represents the **semantic decision**, not merely the evaluation scope.

## Schema Version
`recongraph.decision_trace_identity.v1`

## Identity Computation
Trace identity is computed using domain-separated hashing (K6 primitives).

```python
payload = {
    "schema": "recongraph.decision_trace_identity.v1",
    "engine_version": "...",
    "config_hash": "...",
    "component_nodes": ["urn:recongraph:purchase:1", "urn:recongraph:gst:1"],
    "decision": "auto_match",
    "selected_hypothesis": {
        "hypothesis_identity": [["urn:recongraph:purchase:1", "urn:recongraph:gst:1"]],
        "eligibility": "eligible",
        "semantic_findings": ["exact_match"],
        "base_score": 10000,
        "coverage": 10000,
        "relationship_score": 10000,
        "provider_projection_identities": ["AMOUNT", "ENTITY", "REFERENCE", "TAX_IDENTITY", "TEMPORAL"]
    }
}
```

## Score Canonicalization
Scores are canonicalized to avoid floating-point drift and hardware nondeterminism.
Scores are represented as integers (basis points).
`canonicalize_score(score: float) -> int`: `round(score * 10000)`.

## Invariants
- Same semantic inputs -> same identity.
- Different semantic outputs -> different identity.
- Runtime-only changes (timestamps, wording) -> same identity.
