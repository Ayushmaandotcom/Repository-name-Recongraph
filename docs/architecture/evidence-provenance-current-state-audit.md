# Evidence Provenance Current State Audit
## Part A — Audit Every Existing Provenance Concept

### Audit Summary
The ReconGraph repository lacks formalized provenance. Existing evidence objects implicitly rely on string-shaped identifiers (e.g., `record_id`) and temporal execution state rather than cryptographic or structural lineage.

| Concept | File | Current Identity | Provenance Preserved? | Lost Information | K4/K5 Risk |
|---|---|---|---|---|---|
| `record_id` | `records.py` | String identifier | No | Namespace, Source System | High - Can collide across tenants/systems |
| `config_hash` | `config.py` | SHA256 of params | Partial | Historical context | Medium - Describes engine, not fact |
| `trace` | `trace.py` | Event log | No | Derivation logic | High - Log is not a DAG |
| `payload` | `scoring.py` | Dict | No | Implied semantics | High - Payload fields lack claim identity |

### Object Attack Matrix
* **PurchaseRecord / GSTRecord**: Assumes `record_id` is globally unique. `record_id="123"` is not lineage; it is an identifier-shaped string. Serializing this 6 months later provides zero epistemic value without the original database context.
* **EvidenceContribution**: Assumes `provider_id` is sufficient provenance. Destroys the exact source observation content state.
* **DecisionTrace**: Captures temporal engine state. Cannot be used to prove causal independence of facts.
