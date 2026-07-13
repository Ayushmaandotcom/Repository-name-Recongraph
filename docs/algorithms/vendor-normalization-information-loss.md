# Vendor Normalization Destructiveness Audit

This document audits `normalize_vendor_name()` in `src/recongraph/normalization/text.py`.

## Current Normalization Operations
1. **Lowercasing:** Converts all characters to lowercase.
2. **Punctuation to Whitespace:** Non-alphanumeric characters become spaces.
3. **Whitespace Collapse:** implicit via `.split()` and `" ".join()`.
4. **Legal Suffix Removal:** Removes exact tokens `{"pvt", "private", "ltd", "limited"}`.
5. **Token Aliasing:** Applies `VENDOR_TOKEN_ALIASES` replacement.

## Destructiveness Classification

| Operation | Classification | Justification |
|---|---|---|
| **Lowercasing** | INFORMATION_LOSS_ACCEPTED | Case rarely holds legal distinction for organizations. |
| **Punctuation to Whitespace** | LEGAL_IDENTITY_RISK | `A&B` becomes `A B`. Ampersands can be legally significant parts of names. |
| **Whitespace Collapse** | REVERSIBLE (semantically) | Repeated spaces are typographic noise. |
| **Legal Suffix Removal** | LEGAL_IDENTITY_RISK | Deletes legal form entirely. `TATA PVT LTD` becomes `TATA`. This destroys the ability to distinguish between corporate entities within a family. |
| **Accent Removal (Absent)** | LANGUAGE_RISK | Currently absent. `müller` and `muller` remain distinct, causing mismatches on valid OCR. |
| **Numeric Substitution (Absent)** | UNKNOWN | `MICR0SOFT` vs `MICROSOFT` remains distinct. Without OCR confidence scores, normalizing this is risky. |

## Empirical Adversarial Results

From `experiments/audit_vendor_normalization_information_loss.py`:

* `ABC LLP` vs `ABC LTD` -> `abc llp` vs `abc`. `LTD` is deleted, `LLP` is preserved. Asymmetry.
* `A&B` vs `AB` -> `a b` vs `ab`. Mismatch.
* `TATA PVT LTD` vs `TATA PRIVATE LIMITED` -> `tata` vs `tata`. Match achieved by total deletion of legal identity.

## Conclusion
The current normalization destroys legal identity to achieve lexical matching. By stripping `PVT LTD` but leaving `LLP`, it operates asymmetrically. Legal suffixes are not "noise" to be stripped; they are a separate dimension of identity evidence.
