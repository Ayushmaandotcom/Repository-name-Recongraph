# Vendor Observation State Truth Table V1

ReconGraph's semantic kernel supports strict epistemic states: `MISSING_INPUT`, `INSUFFICIENT_INPUT`, `UNINTERPRETABLE_INPUT`, `NOT_APPLICABLE`, and `INTERPRETED`.

## Why a Single Global State is Wrong

A monolithic vendor pipeline might attempt to emit a single global state. 
For example, if the vendor name is entirely missing from the purchase record, a naive pipeline returns `MISSING_INPUT`.

**However, if both records contain perfectly valid, matching GSTINs, that global `MISSING_INPUT` state silently destroys the tax identity evidence.**

Therefore, the `VendorIdentityInterpretation` object must hold a tuple of factor-level `EvidenceInterpretationResult`s. The states below apply **per-factor**.

## Vendor Name Truth Table (Organization Core & Legal Form)

| Purchase Name | GST Name | Expected State (Core/Form) | Reasoning |
|---|---|---|---|
| `None` | `ABC LTD` | `MISSING_INPUT` | One side is completely absent. |
| `""` | `ABC LTD` | `MISSING_INPUT` | Empty string provides no evidence. |
| `" "` | `ABC LTD` | `MISSING_INPUT` | Whitespace-only string provides no evidence. |
| `"---"` | `"ABC LTD"` | `UNINTERPRETABLE_INPUT` | Contains characters but no semantic lexical tokens. |
| `"A"` | `"B"` | `INSUFFICIENT_INPUT` | Single characters are too short to form a meaningful organization core for comparison. Threshold required. |
| `"ABC"` | `"ABC"` | `INTERPRETED` | Valid comparison. |
| `"ABC LTD"` | `"ABC LLP"` | `INTERPRETED` | Valid comparison. Produces `CONFLICT` assertion for legal form. |
| `"ABC LTD"` | `valid GSTIN` | `MISSING_INPUT` | (Assuming GST name is missing, only GSTIN provided). |
| `malformed GSTIN` | `valid GSTIN` | `MISSING_INPUT` | (Assuming name fields are missing). |

*Note on Single-Character Names:* We recommend a minimum character length threshold (e.g., 2 or 3 alphanumeric chars) to transition from `INSUFFICIENT_INPUT` to `INTERPRETED`, as comparing "A" and "B" introduces massive false positive/negative risks without providing meaningful semantic grounding.

## GSTIN Truth Table (GST Registration & Tax Identity)

| Purchase GSTIN | GST GSTIN | Validation Result | Expected State | Expected Assertions | Reasoning |
|---|---|---|---|---|---|
| `07ABCDE1234F1Z5` | `07ABCDE1234F1Z5` | Both Valid | `INTERPRETED` | SUPPORT `same_gst_registration`, SUPPORT `same_tax_identity` | Exact match. |
| `07ABCDE1234F1Z5` | `29ABCDE1234F1Z5` | Both Valid | `INTERPRETED` | CONFLICT `same_gst_registration`, SUPPORT `same_tax_identity` | Different states, same PAN. |
| `07ABCDE1234F1Z5` | `07XYZDE9876Q1Z5` | Both Valid | `INTERPRETED` | CONFLICT `same_gst_registration`, CONFLICT `same_tax_identity` | Completely different identities. |
| `None` | `07ABCDE1234F1Z5` | N/A | `MISSING_INPUT` | None | Cannot compare. |
| `07ABCDE1234F1Z5` | `INVALID_STR` | One Invalid | `UNINTERPRETABLE_INPUT` | None | Malformed GSTIN halts the tax pipeline. |
| `O7ABCDE1234F1Z5` | `07ABCDE1234F1Z5` | One Invalid (OCR) | `UNINTERPRETABLE_INPUT` | None | Do not guess or repair in the deterministic pipeline. |
