# Observation Occurrence Naming Decision

## Comparison of Candidates

### `ObservationProvenance`
**Pros:** Familiar term for origin metadata.
**Cons:** The object binds `ObservationIdentity` (what fact exists) with `StructuredSourceLineage` (where it came from). Calling it "Provenance" implies it only contains source metadata, obscuring the fact that it conceptually represents the *occurrence* of the observation.

### `SourcedObservation`
**Pros:** grammatically pleasing.
**Cons:** Implies the observation is mutated or wrapped into a new type of observation, which breaks the epistemic boundaries.

### `ObservedOccurrence`
**Pros:** Accurate to the physical reality.
**Cons:** Loses the explicit link to the `Observation` kernel class.

### `ObservationOccurrence`
**Pros:** Perfectly maps to the established pattern:
- `ObservationIdentity`: Answers "What content state exists?"
- `ObservationOccurrence`: Answers "Where was this content state observed?"
It explicitly binds fact identity + source occurrence without semantic conflation. 

## Final Decision
**Final class name: `ObservationOccurrence`**

## Required Invariants
1. Same `ObservationIdentity` + Same `StructuredSourceLineage` = Equal.
2. Same `ObservationIdentity` + Different lineage = Distinct.
3. Different `ObservationIdentity` + Same lineage = Distinct. (e.g. two different OCR engines reading the same PDF bbox producing different text).

> **Important OCR Note**: 
> A raw PDF region is source material. The extracted OCR text should technically be modeled as a `DerivedArtifact` derived from a raw `ObservationOccurrence` of the region. `ObservationOccurrence` gives us the structural precision to model this correctly, rather than falsely claiming the PDF directly observed the text "ABC LTD".
