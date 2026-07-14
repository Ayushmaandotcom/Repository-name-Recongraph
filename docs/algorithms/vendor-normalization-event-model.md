# Vendor Normalization Event Model V1

Normalization must be modeled as an event stream, not a silent mutation.

## VendorNormalizationEventKind

We define the following standard normalization events:

- `UNICODE_CANONICALIZED`: Transformations like NFD to NFC or NFKC.
- `CASE_FOLDED`: Standardizing to an uppercase canonical form.
- `PUNCTUATION_STANDARDIZED`: e.g., removing full stops in abbreviations (`PVT.` → `PVT`).
- `WHITESPACE_COLLAPSED`: Replacing multiple consecutive spaces or tabs with a single space.
- `LEGAL_FORM_RECOGNIZED`: Classification of tokens as a legal designator.
- `ABBREVIATION_EXPANDED`: Expanding common abbreviations (`PVT` → `PRIVATE`, `LTD` → `LIMITED`).
- `CONNECTOR_CANONICALIZED`: Standardizing ampersands or connectives (`&` → `AND`).
- `TOKEN_CLASSIFIED`: General classification of a token (e.g. as geographic or noise).

## Event Data Structure

```python
@dataclass(frozen=True, slots=True)
class VendorNormalizationEvent:
    kind: VendorNormalizationEventKind
    input_span: tuple[int, int]
    original_value: str
    canonical_value: str
```

## Why this is a DerivedArtifact

A structured vendor parse is a highly valuable, computationally expensive asset. 
We model it as a `DerivedArtifact` (per K5) rather than a production-runtime side effect because it represents a **semantically reusable, independently addressable intermediate**.

If we parse "ABC PVT LTD" for Candidate A, and then we need to compare Candidate A to Candidate C later, we should not parse "ABC PVT LTD" again. By storing the structured observation (including its normalization events) as a `DerivedArtifact`, we can retrieve it by its content hash.

## The Derivation DAG Node

- `ObservationOccurrence`: Raw vendor name string from a source system (e.g., SAP row).
- `DerivationOccurrence`: The execution of `vendor.parse_name.v1`.
- `DerivedArtifact`: The resulting `VendorNameObservation` + list of `VendorNormalizationEvent`s (`vendor.structured_name.v1`).
