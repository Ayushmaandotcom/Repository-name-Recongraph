# Primitive Evidence Units for Legal Entity Identity

This document defines the primitive evidence units capable of bearing evidence on the claim `SAME_LEGAL_ENTITY`.

## Primitive Units

### VE-001 — Exact Normalized Full Name Agreement
* **Required Observations:** Raw string A, Raw string B.
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Potential Support:** Weak (without statistics).
* **Potential Conflict:** None. (Mismatch does not prove different entity, as aliases exist).
* **Authority Source:** Structural Heuristic.
* **Statistics Required:** No.
* **External Knowledge:** No.

### VE-002 — Discriminative Name Token Agreement
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Potential Support:** High (if rare token).
* **Potential Conflict:** None.
* **Statistics Required:** Yes. (Must know token document frequency).

### VE-003 — Legal Form Agreement
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Potential Support:** Weak. (Many companies are `PVT LTD`).
* **Potential Conflict:** Strong. (A mismatch from `LLP` to `PVT LTD` on the same core name is highly conflicting).
* **Statistics Required:** No.
* **External Knowledge:** Legal suffix dictionary.

### VE-004 — Legal Form Conflict
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Can this directly contradict same legal entity?** Yes. Unless a historical legal conversion took place (which requires temporal data), an LLP and a PVT LTD are distinctly registered legal entities.

### VE-005 — Authoritative Identifier Agreement
* **Target Claim:** `SAME_REGISTERED_TAX_IDENTITY` (A proxy for Legal Entity).
* **Potential Support:** Strongest.
* **Potential Conflict:** Strongest.
* **Authority:** Verifiable Registry.

### VE-006 — Authoritative Identifier Conflict
* **Can PAN and GSTIN be compared?** No. A PAN identifies a taxpayer. A GSTIN identifies a state-level registration under a PAN. Comparing PAN `ABCDE1234F` to GSTIN `27ABCDE1234F1Z5` string-to-string is invalid. They must be parsed.

### VE-010 — Generic Full Name Equality
* **Example:** `TRADERS` vs `TRADERS`.
* **Potential Support:** Zero. (Discriminative power is nil).

### VE-012 — OCR-Confusable Name Similarity
* **Example:** `MICR0SOFT` vs `MICROSOFT`.
* **Potential Conflict:** Without OCR provenance (e.g. knowing it was extracted from an image), treating this as conflict is dangerous. With OCR provenance, it can be normalized as an observation error.

## Authorized Units for v0.1
To keep v0.1 narrow and intellectually honest, the following are AUTHORIZED:
* VE-001 (Exact Normalized Full Name Agreement)
* VE-003 (Legal Form Extraction/Agreement)
* VE-004 (Legal Form Conflict)
* VE-005/VE-006 (Authoritative Identifier Agreement/Conflict)

The following are EXPLICITLY DEFERRED:
* VE-002 (Corpus Statistics) - Requires a profiler infrastructure.
* VE-007 (Aliases) - Requires a knowledge base.
* VE-012 (OCR correction) - Requires confidence scores we lack.
