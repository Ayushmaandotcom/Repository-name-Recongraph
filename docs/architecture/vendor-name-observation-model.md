# Vendor Name Observation Model V1

## Challenging the Naive Design

A naive vendor name observation might look like this:
```python
@dataclass(frozen=True, slots=True)
class VendorNameObservation:
    raw_name: str
    canonical_text: str
    organization_tokens: tuple[str, ...]
    legal_form: LegalFormId | None
```
While simple, this destroys context. If a downstream consumer or an auditor asks *why* a particular token was removed or how the core was derived, this model provides no answers. It does not separate trade names from noise, nor does it preserve the spans of the original text.

## The Justified Observation Schema

To support explainability, debugging, and exact semantic mapping, the `VendorNameObservation` must preserve spans, categorization, and the sequence of transformations.

```python
@dataclass(frozen=True, slots=True)
class VendorNameObservation:
    raw_name: str
    canonical_text: str
    organization_tokens: tuple[str, ...]
    legal_form: LegalFormId | None
    recognized_designators: tuple[str, ...]
    unresolved_tokens: tuple[str, ...]
    token_spans: tuple[TokenSpan, ...]
    normalization_events: tuple[VendorNormalizationEvent, ...]
    geographic_tokens: tuple[str, ...]
    trade_name_tokens: tuple[str, ...]
    noise_tokens: tuple[str, ...]
```

### Why Token Spans Matter

Consider the example: `MAHINDRA & MAHINDRA LIMITED`

- tokens: `[MAHINDRA, &, MAHINDRA, LIMITED]`
- organization span: `[0:3]` (covering MAHINDRA & MAHINDRA)
- legal form span: `[3:4]` (covering LIMITED)
- canonical org core: `MAHINDRA AND MAHINDRA`
- legal form: `LIMITED`

By preserving spans, the system can eventually provide an explanation string:
*"LIMITED was recognized as a legal-form designator at position 3 and excluded from organization-core comparison."*

### Field Justifications

- `recognized_designators`: The exact tokens (e.g. `PVT`, `LTD`) that matched a canonical legal form.
- `unresolved_tokens`: Tokens that could not be confidently classified as core, designator, geographic, or noise.
- `token_spans`: `(start_index, end_index, label)` tuples mapping canonical tokens back to the `raw_name` string.
- `normalization_events`: Transformations applied (e.g., casing, Unicode normalization).
- `geographic_tokens`: Tokens detected as locations (e.g., `DELHI`, `MUMBAI`). Important to prevent false negatives when one system includes the city and the other does not.
- `trade_name_tokens`: Tokens explicitly recognized as a DBA or brand (if structural parsing permits).
- `noise_tokens`: Tokens with no semantic identity value (e.g., standard stopwords like `THE`).
