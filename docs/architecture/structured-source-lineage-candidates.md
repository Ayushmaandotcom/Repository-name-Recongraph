# Structured Source Lineage Candidates
## Part F — Defining Lineage

### Candidate Evaluation
1. **L1: Flat Descriptor** (Score: 25/40) - Simple but lacks structural extensibility.
2. **L2: Hierarchical Path** (Score: 28/40) - Hard to serialize universally without delimiter collisions.
3. **L3: Typed Source Nodes** (Score: 38/40) - Separate `SourceSystemNode`, `SourceArtifactNode`, `SourceVersionNode`. Perfect extensibility.
4. **L4: Provenance DAG** (Score: 32/40) - Overkill for initial extraction; better suited for derivation layer.
5. **L5: Occurrence + Content Identity** (Score: 39/40) - Formally separates the epistemic fact from its temporal source coordinates.

### Decision
We select a variation of **L3/L5**. Lineage represents the occurrence coordinates, while Observation (K3) represents the content state. A wrapper (`ObservationProvenance`) binds them.
