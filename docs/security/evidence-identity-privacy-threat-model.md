# Evidence Identity Privacy Threat Model
## Part P — Leakage Risks

### The Dictionary Attack
Since ObservationFingerprint is deterministic SHA-256 over `(slot, state, value)`, an attacker can precompute hashes for known vendor names (`TATA MOTORS`, etc.) and identify them in a tenant's DAG.

### Mitigation Stance
Identity semantics will use `TENANT_SCOPED` salts if payload protection is required, or rely on application-layer encryption of the DAG storage. The Semantic Kernel defines structure, but the persistence layer must handle cryptographic salts.
