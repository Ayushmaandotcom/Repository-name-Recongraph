# Derivation Identity vs Execution Decision

## Questions and Answers

### Does semantic cache identity require content identities?
**Yes.** To know if we have already performed a computation (e.g. `normalize("ABC LTD")`), we must key the cache by the content identity of the inputs, the provider version, and the method identity.

### Does evidence ancestry require occurrences?
**Yes.** We must trace the final semantic claim back to exactly which source line (e.g. SAP row 123 vs GST row 456) provided the input. Content alone cannot prove causation from a specific source.

### Can one object safely represent both?
**No.** If we use occurrence for cache identity, identical contents from different occurrences execute redundantly. If we use content for ancestry, we lose the operational source lineage.

### Should we separate them?
**Yes.** 
- `DerivationIdentity` = Content-addressed semantic computation key.
- `DerivationExecution` = Provenance record binding the computation to actual input occurrences.

### Does a cache hit create a new derivation execution?
**Yes.** The execution occurred logically. We skipped the CPU cost, but the new source occurrence still participated in deriving the fact. We must record the new `DerivationExecution` connecting the new occurrence to the cached result.

### If yes, does it reference the reused DerivedArtifact?
**Yes.** Multiple `DerivationExecutions` (provenance edges) point to the same `DerivedArtifact` (semantic state).

### Can two executions share one DerivationIdentity?
**Yes.** If both executions operate on inputs with identical content state.

### Can two executions share one DerivedArtifact?
**Yes.** By definition, if they share a `DerivationIdentity`, the deterministic function yields the identical `DerivedArtifact`.

### Does the Evidence DAG contain DerivationIdentity or DerivationExecution nodes?
The DAG is bipartite / multi-layered. The *Semantic State Graph* contains `ObservationIdentity`, `DerivationIdentity`, and `DerivedArtifact`. The *Provenance Graph* contains `ObservationOccurrence` and `DerivationExecution`. We will persist the provenance graph edges.

### What does an assertion lineage reference?
It must reference the full provenance paths (the occurrences and executions) that prove *why* the engine believes the assertion.

## Final Design Boundary
```python
DerivationIdentity  # Owns SHA-256 over method + semantic version + input identities
DerivationExecution # Owns the DerivationIdentity + actual ObservationOccurrences
```
