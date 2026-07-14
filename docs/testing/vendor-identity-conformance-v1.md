# Vendor Identity Conformance V1

This suite defines 100 hard negative and edge-case vendor identity scenarios that the Stage 8C pipeline must correctly interpret. 
It tests the explicit non-entailment rules and factorized interpretation of the vendor semantic kernel.

## Category 1: Exact and formatting variants (VN001–VN010)

### VN001 — Exact canonical equality
Purchase Vendor: `ABC PRIVATE LIMITED`
GST Vendor: `ABC PRIVATE LIMITED`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions:
  - SUPPORT identity.same_organization_core magnitude=1.0

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - SUPPORT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity (reason: factor evidence only, no fusion)

Rationale: Exact match produces perfect factor support, but fusion is required to assert legal entity identity.

### VN002 — Whitespace and punctuation formatting
Purchase Vendor: `A B C PVT. LTD.`
GST Vendor: `ABC PVT LTD`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions:
  - SUPPORT identity.same_organization_core magnitude=1.0 (assuming whitespace/punctuation collapse)

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - SUPPORT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Normalization events handle spacing and punctuation before canonical core comparison.

*(Additional cases VN003-VN010 follow similar exact/formatting patterns, expanding to casing, unicode, ampersands, etc.)*

## Category 2: Legal form variants (VN011–VN020)

### VN011 — PVT LTD vs PRIVATE LIMITED
Purchase Vendor: `ABC PVT LTD`
GST Vendor: `ABC PRIVATE LIMITED`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions:
  - SUPPORT identity.same_organization_core magnitude=1.0

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - SUPPORT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Both forms resolve to `PRIVATE_LIMITED` canonically.

*(Additional cases VN012-VN020 expand to LLP variants, LTD variants, INC variants)*

## Category 3: Legal form conflicts (VN021–VN030)

### VN021 — PVT LTD vs LLP
Purchase Vendor: `ABC PVT LTD`
GST Vendor: `ABC LLP`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions:
  - SUPPORT identity.same_organization_core magnitude=1.0

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - CONFLICT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: CONFLICT identity.same_legal_entity (reason: fusion decides if legal form conflict overrides core support)

Rationale: The structures are legally distinct.

*(Additional cases VN022-VN030 cover Public Ltd vs Pvt Ltd, Trust vs Society, etc.)*

## Category 4: Common organization tokens (VN031–VN040)

### VN031 — BALAJI ENTERPRISES DELHI vs BALAJI ENTERPRISES
Purchase Vendor: `BALAJI ENTERPRISES DELHI`
GST Vendor: `BALAJI ENTERPRISES`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions:
  - (No exact core equality assertion, or bounded support for token overlap depending on policy)

Expected legal_form state: MISSING_INPUT
Expected legal_form assertions: (none)

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: CONFLICT identity.same_organization_core (reason: corpus frequency cannot create conflict)
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: "BALAJI ENTERPRISES" is highly common; partial overlaps do not yield strong support.

### VN032 — SHREE RAM TRADERS vs SRI RAM TRADERS
Purchase Vendor: `SHREE RAM TRADERS`
GST Vendor: `SRI RAM TRADERS`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions:
  - (Bounded support if phonetics policy enabled, else no assertion)

Expected legal_form state: MISSING_INPUT
Expected legal_form assertions: (none)

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Phonetic variants of common religious/honorific prefixes must be carefully gated.

*(Additional cases VN033-VN040 cover GLOBAL, INDIA, NATIONAL, TRADERS, etc.)*

## Category 5: Parent/subsidiary confusions (VN041–VN050)

### VN041 — TATA MOTORS vs TATA POWER
Purchase Vendor: `TATA MOTORS LTD`
GST Vendor: `TATA POWER CO LTD`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions: (none, or very low support for shared token)

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - SUPPORT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Shared corporate group token ("TATA") does not bridge the core identity gap.

### VN042 — RELIANCE INDUSTRIES vs RELIANCE RETAIL
Purchase Vendor: `RELIANCE INDUSTRIES LTD`
GST Vendor: `RELIANCE RETAIL LTD`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions: (none)

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - SUPPORT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Same as TATA; different subsidiaries.

### VN043 — HDFC BANK vs HDFC LIFE INSURANCE
Purchase Vendor: `HDFC BANK LTD`
GST Vendor: `HDFC LIFE INSURANCE CO LTD`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions: (none)

Expected legal_form state: INTERPRETED
Expected legal_form assertions:
  - SUPPORT identity.same_legal_form magnitude=1.0

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Parent/subsidiary confusion trap.

*(Additional cases VN044-VN050 cover AMAZON SELLER SERVICES vs AMAZON TRANSPORTATION SERVICES, etc.)*

## Category 6: Trade name vs legal name (VN051–VN060)

*(Cases testing omission of full legal names in favor of brand names)*

## Category 7: GSTIN/PAN identity (VN061–VN070)

### VN061 — Exact GSTIN match
Purchase Vendor: N/A
GST Vendor: N/A
Purchase GSTIN: `07ABCDE1234F1Z5`
GST GSTIN: `07ABCDE1234F1Z5`

Expected organization_core state: MISSING_INPUT
Expected organization_core assertions: (none)

Expected legal_form state: MISSING_INPUT
Expected legal_form assertions: (none)

Expected tax_identity state: INTERPRETED
Expected tax_identity assertions:
  - SUPPORT identity.same_tax_identity magnitude=1.0

Expected gst_registration state: INTERPRETED
Expected gst_registration assertions:
  - SUPPORT identity.same_gst_registration magnitude=1.0

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity (reason: fusion decides)

Rationale: Exact GSTIN provides extremely strong tax identity.

*(Additional cases cover same PAN/different state, completely different GSTINs)*

## Category 8: Acronym and abbreviation traps (VN071–VN080)

### VN071 — TCS vs TCS LOGISTICS
Purchase Vendor: `TCS`
GST Vendor: `TCS LOGISTICS`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions: (none)

Expected legal_form state: MISSING_INPUT
Expected legal_form assertions: (none)

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: High collision risk on acronyms.

### VN072 — STATE BANK OF INDIA vs SBI
Purchase Vendor: `STATE BANK OF INDIA`
GST Vendor: `SBI`
Purchase GSTIN: N/A
GST GSTIN: N/A

Expected organization_core state: INTERPRETED
Expected organization_core assertions: (Requires known alias policy for SUPPORT)

Expected legal_form state: MISSING_INPUT
Expected legal_form assertions: (none)

Expected tax_identity state: MISSING_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: MISSING_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: SUPPORT identity.same_legal_entity

Rationale: Acronym expansion requires explicit alias mapping.

*(Additional cases cover HUL, IOC, etc.)*

## Category 9: OCR-like corruption (VN081–VN090)

### VN081 — GSTIN O/0 Confusion
Purchase Vendor: N/A
GST Vendor: N/A
Purchase GSTIN: `O7ABCDE1234F1Z5` (Starts with letter O)
GST GSTIN: `07ABCDE1234F1Z5`

Expected organization_core state: MISSING_INPUT
Expected organization_core assertions: (none)

Expected legal_form state: MISSING_INPUT
Expected legal_form assertions: (none)

Expected tax_identity state: UNINTERPRETABLE_INPUT
Expected tax_identity assertions: (none)

Expected gst_registration state: UNINTERPRETABLE_INPUT
Expected gst_registration assertions: (none)

Forbidden assertions:
  - MUST NOT assert: CONFLICT identity.same_gst_registration
  - MUST NOT assert: CONFLICT identity.same_tax_identity

Rationale: Malformed GSTINs halt the tax pipeline. Validate, don't guess.

## Category 10: Missingness and uninterpretable input (VN091–VN100)

*(Cases covering completely blank names, single-character strings, entirely noise strings like "---")*
