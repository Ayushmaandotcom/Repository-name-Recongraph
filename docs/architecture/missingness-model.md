# Missingness Algebra (Stage 8I)

This document differentiates the various states of missing evidence and defines how they propagate through the Fusion Layer.

## Phase 6: Missingness Algebra

An absent observation is not simply a `None` value in ReconGraph. We strictly differentiate between ontological states of absence.

### Categories of Missingness

1. **Missing (Silent Absence)**
   - **Definition:** The field was completely empty in the source record (e.g., `tax_identity=""`).
   - **Semantics:** Confers NO evidence. `Support = 0`, `Contradiction = False`.
   
2. **Unknown (Unparseable)**
   - **Definition:** The field existed, but the `DeterministicParser` failed to recognize the format.
   - **Semantics:** Triggers a Warning flag in the `DecisionTrace`. Confers NO evidence, but flags human review if `Compatibility` is marginal.
   
3. **Invalid (Checksum Failure)**
   - **Definition:** The string parsed correctly into a structural format (e.g., a GSTIN), but failed the cryptographic checksum (e.g., Modulo 36).
   - **Semantics:** Invalid data cannot be trusted. Treated as `Missing`, but permanently tags the Record as `DATA_QUALITY_ISSUE`.
   
4. **Not Applicable (Domain Exclusion)**
   - **Definition:** A field is logically impossible given the context (e.g., seeking an Import Code on a domestic invoice).
   - **Semantics:** Filtered completely from the `EvidenceGraph`.
   
5. **Contradictory Missingness**
   - **Definition:** Field A explicitly claims an entity is Unregistered, but Field B provides a valid Tax ID.
   - **Semantics:** Elevates immediately to `Contradiction`.

### Propagation Rules

- `Missing ∪ Missing = Missing` (Two blanks do not match each other).
- `Missing ∪ Valid = Missing` (A blank and a value do not contradict).
- `Invalid ∪ Valid = Missing` (An invalid GSTIN does not contradict a valid GSTIN; it implies a typo).

**Fusion Impact:** Missing dimensions reduce the maximum possible `Compatibility` score, preventing an `AUTO_MATCH` decision if critical dimensions (like Financial and Vendor) are absent.
