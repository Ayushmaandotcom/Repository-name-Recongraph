# Identifier Authority Boundary

This document challenges the assumption that "an exact tax ID conflict overrides an exact name match" by exploring the Indian tax registration hierarchy (PAN vs GSTIN).

## The Nuance of Identifier Types

**IB-001 What is a "tax ID" in current ReconGraph?**
Currently, it is a flat string mapped to `SignalName.TAX_IDENTITY`.

**IB-002 Is identifier type explicitly represented?**
No.

**IB-003 Can two identifiers be compared without knowing their type?**
No. Comparing a 10-character PAN to a 15-character GSTIN via string equality is conceptually invalid.

## GSTIN vs Legal Entity Identity

**IB-004 Can the same legal entity legitimately have multiple GST registrations?**
Yes. In India, a single legal entity (identified by one PAN) MUST have different GSTINs for operations in different states. It may also voluntarily have multiple GSTINs within the same state (e.g. for different business verticals).

**IB-005 Does a different GSTIN necessarily prove a different legal entity?**
NO. A company with `GSTIN_MAHARASHTRA` and `GSTIN_KARNATAKA` is the exact same legal entity (same PAN). Therefore, a GSTIN mismatch **does not contradict** `SAME_LEGAL_ENTITY`. It only contradicts `SAME_GST_REGISTRATION`.

**IB-006 Could different registrations belong to the same PAN-level legal entity?**
Yes. The 13th to 15th characters of the GSTIN (e.g. `1Z5`) differentiate registrations under the same 10-character PAN (characters 3-12).

**IB-007 Is ReconGraph currently reconciling at GST registration identity or legal entity identity?**
Currently, the GST provider enforces exact string equality on `tax_id`, so it is strictly checking `SAME_GST_REGISTRATION`. However, because it's called `tax_identity`, humans interpret it as legal entity identity.

**IB-008 Has the research decision accidentally chosen a claim broader than the identifier can directly observe?**
Yes. If we use GSTIN to enforce `SAME_LEGAL_ENTITY` via strict equality, we will artificially penalize legitimate interstate transactions where the operational branch (GSTIN) differs but the corporate counterparty (PAN/Legal Entity) is identical.

## Observation vs Claim Matrix

| Claim | Vendor Name | GSTIN | PAN | Registry Entity ID | Can Directly Observe? |
|---|---|---|---|---|---|
| `SAME_LEXICAL_NAME` | Yes | No | No | No | Vendor Name |
| `SAME_GST_REGISTRATION`| No | Yes | No | No | GSTIN |
| `SAME_LEGAL_ENTITY` | No | No (Proxy via parsing) | Yes | Yes | PAN / Registry ID |
| `SAME_CORPORATE_FAMILY`| No | No | No | Yes (Parent ID) | Registry Parent ID |
| `SAME_OP_COUNTERPARTY` | Yes (Proxy) | Yes (Proxy) | No | No | Billing System ID |

## Revised Conclusion for Stage 8C
The claim `SAME_LEGAL_ENTITY` is technically incorrect if backed purely by unparsed GSTIN string equality. 

Stage 8C must model two distinct claims:
1. `SAME_LEGAL_ENTITY` (supported by exact PAN match / parsed GSTIN PAN substring).
2. `SAME_GST_REGISTRATION` (supported by full 15-character GSTIN match).

A conflict on `SAME_GST_REGISTRATION` does *not* automatically generate a conflict on `SAME_LEGAL_ENTITY`.
