# Vendor Identity Latent Variables

## The Latent Variables

The current architecture confusingly bundles multiple identity questions into a single scalar "vendor score". This document formally separates them.

### LI-001 — Lexical Name Identity
* **Question:** Do the observed vendor name strings appear to represent the same written organization name?
* **Example:** `TATA CONSULTANCY SERVICES LIMITED` vs `Tata Consultancy Services Ltd`

### LI-002 — Legal Entity Identity
* **Question:** Do the records refer to the exact same legally registered entity?
* **Example:** `ABC PRIVATE LIMITED` vs `ABC LLP`

### LI-003 — Corporate Family Identity
* **Question:** Do the records refer to organizations belonging to the same corporate group?
* **Example:** `TATA MOTORS LIMITED` vs `TATA TECHNOLOGIES LIMITED`

### LI-004 — Operational Counterparty Identity
* **Question:** Do the records refer to the same operational counterparty for reconciliation purposes?

### LI-005 — Historical Identity Continuity
* **Question:** Do two names refer to the same organization across a rename or legal transformation?

### LI-006 — Brand / Trade Name Association
* **Question:** Is one observed name a trade name or brand associated with a legal organization?

### LI-007 — Authoritative Identifier Identity
* **Question:** Do authoritative identifiers assert the same registered entity?

## Evidence Matrix

| Evidence Source | LI-001 (Lexical) | LI-002 (Legal) | LI-003 (Family) | LI-004 (Operational) | LI-005 (Historical) | LI-006 (Brand) | LI-007 (Identifier) |
|---|---|---|---|---|---|---|---|
| **Raw Vendor Name** | DIRECT | WEAK_PROXY | WEAK_PROXY | WEAK_PROXY | UNOBSERVABLE | WEAK_PROXY | UNOBSERVABLE |
| **Normalized Vendor Name** | DIRECT | PROXY | WEAK_PROXY | WEAK_PROXY | UNOBSERVABLE | WEAK_PROXY | UNOBSERVABLE |
| **Tax Identity (GSTIN)** | UNOBSERVABLE | DIRECT | PROXY | PROXY | DIRECT | PROXY | DIRECT |
| **Domain Corpus/Alias Graph** | UNOBSERVABLE | PROXY | DIRECT | PROXY | DIRECT | DIRECT | UNOBSERVABLE |

## Variable Modeling Decisions

1. **Are they currently represented?** No. They are all conflated into a single `score: float` or binary `1.0`/`0.5`.
2. **Can Legal Identity be determined from names alone?** No. `ABC LLP` and `ABC LTD` share Lexical Name Identity but have different Legal Entity Identity.
3. **Can it be contradicted by authoritative identifiers?** Yes. If GSTINs don't match, Legal Entity Identity is contradicted, regardless of Lexical Identity.
4. **Should ReconGraph v0.1 model all of these?**
   - ReconGraph **MUST** distinguish between Lexical Identity (what the strings say) and Legal Entity Identity (what the identifiers and legal suffixes prove).
   - ReconGraph v0.1 should defer Historical Identity (LI-005) and Brand Association (LI-006) as we lack temporal valid-from knowledge bases.
5. **Explicitly Accepted Failure Mode:** By deferring LI-005, we explicitly accept that a vendor renaming itself mid-year without a shared GSTIN will be treated as two distinct entities, causing a reconciliation failure. This is safer than hallucinating an identity connection.
