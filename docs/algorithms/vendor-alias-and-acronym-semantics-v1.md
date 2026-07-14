# Vendor Alias and Acronym Semantics V1

Acronyms in Indian B2B data represent a giant false-positive minefield. Generic acronym algorithms can create catastrophic matches. (e.g. `TCS` = `Tata Consultancy Services` or `TCS Logistics`).

We structure acronym and alias evidence across three authority levels.

## 1. Derived Acronym (Low Authority)
- **Algorithm**: Deterministic derivation (e.g. `TATA CONSULTANCY SERVICES` → `TCS` by taking the first letters of major tokens).
- **Authority**: `deterministic_rule.acronym_derivation`
- **Constraint**: Derivation must be strictly deterministic so that the same input yields the same derived artifact identity.
- **Risk**: High collision rate. `TCS LOGISTICS` would also match the derived acronym `TCS`. Therefore, this evidence alone is low authority and usually requires corroboration (like a matching GSTIN).

## 2. Known Alias (Higher Authority)
- **Algorithm**: An explicit mapping in the vendor master or a verified registry (`TCS` ↔ `TATA CONSULTANCY SERVICES`).
- **Authority**: `vendor_master.alias_registry`
- **Constraint**: Must carry a `SemanticDependencyRef` to the alias snapshot used for the lookup. If the snapshot changes, the derived interpretation changes.

## 3. Observed Acronym (Context-Dependent Authority)
- **Algorithm**: The acronym is explicitly observed in the same source document (e.g., an invoice reading `"Tata Consultancy Services (TCS)"`).
- **Authority**: Depends on the source occurrence.
- **Constraint**: Must carry ancestry back to the source occurrence.

### The Stage 8J Preservation Requirement
If both the purchase vendor name and the GST vendor name derive their acronyms from the **SAME** uploaded invoice, this creates correlated evidence. If Stage 8J double-counts this, it will falsely inflate confidence.
**Rule:** Do not solve alias fusion now. But preserve ancestry via `EvidenceAncestryRef` so Stage 8J can detect correlated evidence.

## Specific Traps
- `TCS (Tata Consultancy Services)` vs `TCS (TCS Logistics)` (TCS is their actual brand/core).
- `SBI (State Bank of India)` vs `SBI Life Insurance` (SBI is the parent company acronym, but they are different legal entities).
- `HUL (Hindustan Unilever)` — A highly reliable known alias at the registry level.
- `IOC (Indian Oil Corporation)` vs `IOC` (any number of other International/Indian entities).
