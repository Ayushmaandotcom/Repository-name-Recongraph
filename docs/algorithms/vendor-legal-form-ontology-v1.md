# Vendor Legal Form Ontology V1

This document defines the canonical legal form vocabulary for Indian organizations, particularly in the context of B2B invoices and GST data. It specifies how lexical variants are mapped to canonical forms, and the extraction model to separate organization core identity from legal structure.

## Section A — Canonical Legal Form Vocabulary

The following canonical identifiers represent distinct legal structures under Indian corporate and tax law.

| Canonical ID | Real-world Meaning | Can Register GST? | Can have multiple GSTINs? | PAN Holder Type |
|---|---|---|---|---|
| `PRIVATE_LIMITED` | A privately held company registered under the Companies Act. | Yes | Yes (one per state/business vertical) | Company (`C`) |
| `PUBLIC_LIMITED` | A publicly held company registered under the Companies Act. | Yes | Yes | Company (`C`) |
| `LIMITED` | Often used interchangeably with Public Limited, sometimes ambiguous. | Yes | Yes | Company (`C`) |
| `LIMITED_LIABILITY_PARTNERSHIP` | A corporate business vehicle that enables professional expertise and entrepreneurial initiative to combine and operate in flexible, innovative and efficient manner. | Yes | Yes | Firm (`F`) |
| `PARTNERSHIP` | A traditional partnership firm. | Yes | Yes | Firm (`F`) |
| `PROPRIETORSHIP` | A business owned by a single individual, legally indistinct from the owner. | Yes | Yes | Individual (`P`) |
| `ONE_PERSON_COMPANY` | A company with only one member. | Yes | Yes | Company (`C`) |
| `SECTION_8_COMPANY` | A non-profit organization registered as a company. | Yes | Yes | Company (`C`) |
| `COOPERATIVE` | A cooperative society. | Yes | Yes | Association (`A`) / Trust (`T`) |
| `TRUST` | A legal arrangement where property is held by one party for the benefit of another. | Yes | Yes | Trust (`T`) |
| `SOCIETY` | A registered society. | Yes | Yes | Association (`A`) |
| `HINDU_UNDIVIDED_FAMILY` | A joint family recognized as a separate taxable entity. | Yes | Yes | HUF (`H`) |
| `GOVERNMENT_ENTITY` | A state or central government department/enterprise. | Yes | Yes | Govt (`G`) |
| `FOREIGN_COMPANY` | A company incorporated outside India. | Yes | Yes | Company (`C`) |
| `UNKNOWN` | A legal form designator was detected, but its specific type could not be resolved. | - | - | - |

## Section B — Lexical Variant Catalog

Real-world vendor names contain massive lexical variation for legal forms.

- `PRIVATE_LIMITED`: PVT LTD, PVT. LTD., PRIVATE LTD, PRIVATE LIMITED, (P) LTD, P. LTD, (PVT) LTD, P LIMITED
- `PUBLIC_LIMITED`: PLC, PUBLIC LIMITED
- `LIMITED`: LTD, LTD., LIMITED, LMTD
- `LIMITED_LIABILITY_PARTNERSHIP`: LLP, L.L.P., LIMITED LIABILITY PARTNERSHIP, L. L. P.
- `PARTNERSHIP`: PARTNERS, & CO, AND CO, & COMPANY (Note: highly ambiguous, often part of trade name)
- `PROPRIETORSHIP`: PROP, PROPRIETOR
- `ONE_PERSON_COMPANY`: OPC, ONE PERSON COMPANY
- `SECTION_8_COMPANY`: FOUNDATION (ambiguous)
- `COOPERATIVE`: COOP, CO-OP, COOPERATIVE, SAHAKARI
- `TRUST`: TRUST
- `SOCIETY`: SOC, SOCIETY
- `HINDU_UNDIVIDED_FAMILY`: HUF, H.U.F.
- `GOVERNMENT_ENTITY`: GOVT, GOVERNMENT
- `FOREIGN_COMPANY`: INC, INCORPORATED, LLC, GMBH, CORP, CORPORATION, CO., LTD.

## Section C — Extraction Model

Information extraction must precede information removal.

We do NOT implement a lossy normalizer that simply strips legal suffixes (e.g., `normalize("ABC PVT LTD") -> "abc"`). Doing so destroys the fact that the source explicitly stated "PVT LTD".

The extraction model is rule-based and follows this sequence:

1. **Raw Token Sequence Input**: The original vendor name is tokenized and canonicalized for unicode/whitespace.
2. **Suffix and Infix Recognition**: We apply a priority-ordered list of multi-token and single-token patterns. Legal forms typically appear as suffixes, so matching starts from the end of the token sequence.
3. **Canonical Form Assignment**: Matched tokens are mapped to their corresponding Canonical ID (e.g., `PVT LTD` → `PRIVATE_LIMITED`).
4. **Organization Core Extraction**: The tokens remaining after the legal form tokens are removed become the `organization_core`.
5. **Preservation of Span Information**: The exact character spans of the recognized legal form and the organization core are preserved in the `VendorNameObservation` for explainability.

Example:
Input: `ABC PVT LTD`
Output: `organization_core = "ABC"`, `legal_form = PRIVATE_LIMITED`

## Section D — Edge Cases and Traps

- **Ambiguous tokens**: `CO`, `COMPANY`, `CORPORATION`, `INC` can be legal designators, but in the Indian B2B context they are often just words in a name (e.g., "FORD MOTOR COMPANY"). If they appear without a strong designator like "LIMITED", they should often be left as part of the organization core.
- **Legal form as part of trade name**: "FORD MOTOR COMPANY" (COMPANY is part of the brand, not the legal form designator).
- **Missing legal form**: Trade names and invoices frequently omit legal designators entirely.
- **Multiple designators**: "TATA SONS PVT LTD" (SONS is a structural indicator but not a canonical legal form; PVT LTD is the legal form).
- **Non-English designators**: Occasionally seen in regional GST data.

## Section E — Semantic Rules for Legal Form Comparison

The comparison of canonical legal forms produces `identity.same_legal_form` assertions.

- `PRIVATE LIMITED` ↔ `PRIVATE LIMITED` → **SUPPORT** `identity.same_legal_form`, magnitude `1.0`
- `PRIVATE LIMITED` ↔ `PVT LTD` → **SUPPORT** `identity.same_legal_form`, magnitude `1.0` (Canonical equivalence)
- `PRIVATE LIMITED` ↔ `LLP` → **CONFLICT** `identity.same_legal_form`, magnitude `1.0` (Explicit contradiction)
- `PRIVATE LIMITED` ↔ `(missing)` → **MISSING_INPUT** (No assertion emitted, we cannot assume conflict if one side omits it)
- `(missing)` ↔ `(missing)` → **MISSING_INPUT**
