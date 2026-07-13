# Observation Identity Model

This document defines Observation Identity—the stable identifier of the raw data slot that generated an assertion.

## Identity Questions

**OI-001 Are those three assertions derived from one observation?**
Yes. `normalized_name`, `legal_form`, and `tokens` are all derivations of the single source field `vendor_name`.

**OI-002 Does shared lineage alone prove this?**
No. Lineage (`source_record_id`) tells us they came from the same *document*. It does not tell us they came from the exact same *field* on that document.

**OI-003 Could two different fields in the same source record share lineage?**
Yes. `vendor_name` and `billing_name` share the same lineage but are distinct observations.

**OI-004 Does `source_record_id` uniquely identify an observation?**
No.

**OI-005 Is `source_field` required?**
Yes, structurally. It defines the exact slot on the document.

**OI-006 Can one observation combine multiple source fields?**
Yes. E.g. `gross_amount = net_amount + tax_amount`. The observation identity would need to reference multiple fields or a synthetic "composite" slot.

**OI-007 Can one observation derive from multiple parent observations?**
Yes. 

**OI-008 Do we need a derivation DAG now?**
No. We are not tracing the infinite history of knowledge, just preventing Stage 8J from double-counting two pieces of evidence derived from the same source field on the same document.

**OI-009 What minimum identity prevents accidental duplicate counting?**
`{source_system}:{source_record_id}:{source_field}`.

**OI-010 Should observation IDs be random UUIDs?**
No. They destroy determinism and make duplicate detection impossible if the same document is re-parsed.

**OI-011 Should observation IDs be content hashes?**
No. If the human corrects a typo in the field, the content hash changes, breaking the identity of the *slot* and making it look like a brand new observation rather than a corrected one. It also leaks PII in the hash (rainbow table attacks).

**OI-012 Should observation IDs be deterministic structural identifiers?**
Yes. `obs:{source_system}:{source_record_id}:{source_field}`.

**OI-013 What happens when the same source field is ingested twice?**
The structural ID is identical, cleanly identifying it as the same observation.

**OI-014 What happens when the field value changes?**
The *value* changes, but the *slot identity* remains identical. This allows the system to recognize it as an update/correction.

**OI-015 Does observation identity identify a slot or a value occurrence?**
A slot. The value is the payload.

## Evaluation
* **OI-A (No ID):** Double counting inevitable.
* **OI-B (Random UUID):** Kills determinism.
* **OI-C (Content-Derived ID):** Fragile to corrections, leaks PII.
* **OI-D (Structural Observation ID):** Identifies the slot stably. `obs:erp:inv123:vendor_name`.
* **OI-E (Structural Slot ID + Observation Revision/Fingerprint):** Overkill for v0.1.

## Recommendation
**OI-D (Structural Observation ID)**. An observation ID must be a deterministic string combining the system, record, and field path, identifying the *slot* from which the value was extracted, regardless of the value itself.
