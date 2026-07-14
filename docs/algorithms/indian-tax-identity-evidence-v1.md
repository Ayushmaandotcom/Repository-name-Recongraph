# Indian Tax Identity Evidence V1

This document defines the semantic boundary and extraction rules for Goods and Services Tax Identification Number (GSTIN) and Permanent Account Number (PAN) evidence in ReconGraph.

## Section A — GSTIN Structural Decomposition

A GSTIN is structurally composed of meaningful fields. It is a 15-character alphanumeric string.
Example: `07ABCDE1234F1Z5`

1. **State Code** (Positions 1-2): Integer `01` to `38`. Represents the state jurisdiction of the registration.
2. **PAN** (Positions 3-12): The 10-character Permanent Account Number of the legal entity. Structure: `AAAAA9999A` (5 alpha, 4 digit, 1 alpha).
3. **Entity Number** (Position 13): Alphanumeric (`1-9`, `A-Z`). Indicates the number of registrations the entity holds in that state.
4. **Z Character** (Position 14): Hardcoded to `Z` by default.
5. **Checksum** (Position 15): Alphanumeric checksum character.

## Section B — Identity Separation Table

We separate state-level GST registration from national-level PAN tax identity.

| Scenario | full GSTIN | state code | PAN | entity num | assertions emitted |
|---|---|---|---|---|---|
| Same GSTIN | same | same | same | same | SUPPORT `same_gst_registration` 1.0, SUPPORT `same_tax_identity` 1.0 |
| Same PAN, same state, diff entity | diff | same | same | diff | CONFLICT `same_gst_registration`, SUPPORT `same_tax_identity` |
| Same PAN, diff state | diff | diff | same | - | CONFLICT `same_gst_registration`, SUPPORT `same_tax_identity` |
| Diff PAN | diff | - | diff | - | CONFLICT `same_gst_registration`, CONFLICT `same_tax_identity` |
| One missing | one absent | - | - | - | MISSING_INPUT for all |
| One malformed | structurally invalid | - | - | - | UNINTERPRETABLE_INPUT |

## Section C — Validation Rules

Before ANY extraction occurs, the GSTIN must pass structural validation.

1. **Length check**: Must be exactly 15 characters.
2. **State code validity**: Must be an integer between `01` and `38`.
3. **PAN structural pattern**: Positions 3-12 must match the regex `[A-Z]{5}[0-9]{4}[A-Z]`.
4. **Entity number**: Position 13 must be `1-9` or `A-Z`.
5. **Character at position 14**: Must be `Z`.
6. **Character at position 15**: Must be a valid alphanumeric checksum char.

IF validation fails → `UNINTERPRETABLE_INPUT`. Do NOT attempt PAN extraction.
IF validation passes → Extract components and produce typed observations.

## Section D — OCR Corruption Patterns

GSTINs from invoices are often corrupted by Optical Character Recognition (OCR).
Common confusions:
- `O` / `0` (letter O vs digit zero)
- `I` / `1`
- `B` / `8`
- `G` / `6`

Example: `O7ABCDE1234F1Z5` (O instead of 0 for state code).

**Validate, don't guess.** A malformed GSTIN must not produce any tax assertion. We do not silently repair tax identifiers in deterministic vendor identity V1. It produces `UNINTERPRETABLE_INPUT`.

## Section E — Non-Entailment Rules

- `identity.same_tax_identity` MUST NOT imply `identity.same_gst_registration`.
- `identity.same_gst_registration` MUST NOT directly imply `identity.same_legal_entity` (though it provides extremely strong evidence).
- `different_state_code` MUST NOT imply `identity.different_legal_entity`.
- `identity.same_tax_identity` (same PAN) MUST NOT imply `identity.same_legal_entity` without additional evidence (mergers/acquisitions can complicate PAN ownership, though 99% of the time PAN = Legal Entity).
