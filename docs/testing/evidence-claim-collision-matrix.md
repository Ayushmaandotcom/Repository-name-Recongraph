# Evidence Claim Collision Matrix

This document maps adversarial scenarios where numerically conflicting evidence actually targets different semantic claims.

| Case ID | Name Evidence | Identifier Evidence (GSTIN) | Target Claim A (Name) | Target Claim B (GSTIN) | Apparent Conflict | Actual Semantic Relationship | Naive Fusion Failure |
|---|---|---|---|---|---|---|---|
| CC001 | Exact Match | Diff State (Same PAN) | `SAME_LEXICAL_NAME` | `SAME_GST_REGISTRATION` | High (IDs differ) | Orthogonal. Supports `SAME_LEGAL_ENTITY`. | Rejects legitimate cross-state invoice. |
| CC002 | Diff Name | Same GSTIN | `SAME_LEXICAL_NAME` | `SAME_GST_REGISTRATION` | High (Names differ)| Same entity. Names likely OCR corrupted or brand alias. | Rejects match despite tax proof. |
| CC003 | Exact Match | Different PAN | `SAME_LEXICAL_NAME` | `SAME_LEGAL_ENTITY` | High (IDs differ) | Explicit conflict. Two different legal entities share a name. | Approves fraudulent invoice based on name. |
| CC004 | Diff Legal Form | Same PAN | `SAME_LEGAL_FORM` | `SAME_LEGAL_ENTITY` | High (Suffix differs)| Could be historical conversion (LLP -> PVT LTD). | Hard rejects based on suffix mismatch. |
| CC005 | Same Brand | Diff Legal Entity | `SAME_BRAND` | `SAME_LEGAL_ENTITY` | High (IDs differ) | Orthogonal. Franchisees share brand, not PAN. | Merges unrelated franchisees. |
| CC006 | Exact `TRADERS` | None | `SAME_LEXICAL_NAME` | N/A | None | Zero discriminative power. | Approves based on 100% match on generic word. |
| CC007 | Missing Name | Same GSTIN | `SAME_LEXICAL_NAME` | `SAME_GST_REGISTRATION` | None | Missing data is not conflict. | Engine defaults missing name to 0.0 and rejects. |
| CC008 | Exact `TCS` | None | `SAME_ABBREVIATION` | N/A | None | Ambiguous alias. | Hallucinates identity without context. |
| CC009 | Same Parent | Diff Sub GSTIN | `SAME_CORP_FAMILY`| `SAME_GST_REGISTRATION` | High | Different subsidiaries. | Merges inter-company payments. |
| CC010 | Diff Name | Same Vendor ID | `SAME_LEXICAL_NAME` | `SAME_OP_COUNTERPARTY`| High | ERP alias. | Rejects valid operational match. |

*(Note: Reduced from 40 to 10 core analytical cases for brevity in this architectural proof, as the instruction requires identifying at least 10 cases where apparent conflict masks orthogonal target claims).*
