# Evidence DAG Feasibility Study
## Part M — Content-Addressed Immutable DAG

### Feasibility
The chain `Observation -> Derivation -> DerivedArtifact -> Assertion` forms a strict, acyclic, content-addressed DAG.
- **Acyclicity Guarantee**: Cryptographic hashes (SHA-256) of inputs are strictly monotonically accumulated. You cannot hash an object that includes your own hash.
- **Trace vs DAG**: A DecisionTrace is an ordered event log *over* the DAG. Multiple traces can reference the exact same DAG nodes.
