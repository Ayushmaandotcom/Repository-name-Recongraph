# Traceability in ReconGraph

ReconGraph's `DecisionTrace` serves as the immutable ledger for every decision made by the system. Traceability ensures that developers and auditors can point to a single ID and recover the exact execution history of that reconciliation attempt.

## The DecisionTrace

At the end of every evaluation in the `ReconGraphEngine`, a `DecisionTrace` is built. It captures:
1. `trace_id`: A deterministic hash acting as the primary key.
2. `engine_version`: The software version that ran the execution.
3. `config_hash`: The configuration state at runtime.
4. `events`: An ordered list of `TraceEvent` objects detailing the pipeline execution.

### Trace Events
Events are appended to the trace at critical points in the pipeline:
- `CANDIDATE_GENERATION`: How many candidates were considered.
- `GRAPH_BUILDING`: The size and shape of the candidate graph.
- `HYPOTHESIS_EVALUATION`: The number of hypotheses tested.
- `DECISION_EVALUATION`: The final chosen action and hypothesis score.

## Deterministic Identity (`trace_id`)
The `trace_id` is NOT a random UUID. It is computed via a domain-separated hash function:

```python
trace_id = DecisionTrace.compute_identity(
    engine_version="1.4.0",
    config_hash="a1b2c3d4",
    component_nodes=frozenset(["P1", "G1"]),
    decision=decision
)
```

This guarantees that two identical reconciliation jobs (same inputs, same configuration, same version) will yield the exact same `trace_id`. This allows downstream systems to deduplicate traces and natively understand when engine updates change behavior (as the engine version or decision action will alter the hash).
