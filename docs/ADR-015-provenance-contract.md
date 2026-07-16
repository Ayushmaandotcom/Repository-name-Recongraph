# ADR-015: Provenance Contract

## Status
Accepted

## Context
As a financial reconciliation system, ReconGraph operates in a heavily audited environment. When a reconciliation decision is questioned by a regulator or auditor, the system must be able to prove exactly what data it saw, what rules were active, and how it reached its conclusion.

Previously, `DecisionTrace` existed but was primarily used as a logging mechanism. It lacked strong cryptographic binding to the semantic evidence that drove the decision.

## Decision
We establish a strict **Provenance Contract** for all ReconGraph decisions. 

The contract dictates that every `DecisionTrace` must serve as an irrefutable, immutable historical record of the reconciliation execution. The identity of a trace (the `trace_id`) must be a domain-separated hash of the inputs, configuration, and structural decision, rather than a random UUID.

### The Provenance Chain
Provenance is maintained backwards through the entire data lifecycle:
`Decision` → `FusionResult` → `Propagation` → `EvidenceContribution` → `Projection` → `Interpretation` → `Observation` → `Parser` → `Raw Record`

### Deterministic Identity
The `trace_id` is computed deterministically using:
1. `engine_version`
2. `config_hash`
3. `component_nodes` (sorted)
4. `decision` action

This ensures that if the exact same inputs are processed by the exact same engine version and config, yielding the same decision, the `trace_id` will be identical. 

### Falsifiability
If an explanation claims that a `TAX_NODE` contradicted a match, the provenance contract requires that the `DecisionTrace` contains the exact semantic properties of that node. 

## Consequences
- **Positive:** Full auditability. Any decision can be re-simulated or proven mathematically.
- **Positive:** Trace collisions act as a feature, deduplicating identical semantic encounters over time.
- **Negative:** Adding new fields to domain objects requires careful consideration of hashing and canonicalization.
