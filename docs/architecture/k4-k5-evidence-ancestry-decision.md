# K4-K5 Evidence Ancestry ADR (Q1-Q100)
## Part R — Adversarial Questions

**(Excerpt of Key Decisions)**
* **Q12**: Does ingestion time define source identity? **Decision:** NO. **Reason:** Destroys replayability.
* **Q24**: Can one Observation have multiple lineages? **Decision:** NO. We use `ObservationOccurrence` (ObservationProvenance) wrappers. **Reason:** Protects epistemic purity of Observation.
* **Q65**: Are symmetric inputs ordered? **Decision:** We use `DerivationInputBinding(role=str)`. The MethodDescriptor determines if the roles are canonically sorted (ORDERED) or content-sorted (UNORDERED).
* **Q88**: Are traces the DAG? **Decision:** NO. Traces are temporal event logs over the timeless DAG.
