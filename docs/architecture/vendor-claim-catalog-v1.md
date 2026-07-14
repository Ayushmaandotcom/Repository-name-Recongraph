# Vendor Claim Catalog V1

This catalog formally defines the vendor identity claims used in ReconGraph.

## 1. identity.same_legal_entity
- **ClaimId**: `identity.same_legal_entity`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR, GROUP_PAIR
- **semantic_definition**: Both representations refer to the exact same juridical person under the law, capable of entering contracts and bearing liability.
- **positive_evidence_conditions**: Exact TAX_IDENTITY (PAN) match combined with supporting factor evidence (like ORGANIZATION_CORE), explicit legal registry mapping, or strong VENDOR_MASTER_IDENTITY match.
- **conflict_evidence_conditions**: Conflicting TAX_IDENTITY, conflicting LEGAL_FORM, explicitly different legal entities under the same corporate group.
- **missingness_conditions**: MISSING_INPUT when both source strings are missing/blank.
- **known_confounders**: Corporate restructurings, mergers, and parent/subsidiary relationships sharing similar names.
- **authority_sensitive_interpretations**: High authority needed for SUPPORT (e.g. government registry).
- **MUST NOT IMPLY**: Does not imply they share a trade name or a GSTIN.

## 2. identity.same_gst_registration
- **ClaimId**: `identity.same_gst_registration`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations refer to the exact same 15-character Goods and Services Tax Identification Number (GSTIN) issued by an Indian state.
- **positive_evidence_conditions**: Exact structural and character equality of the 15-character GSTIN strings.
- **conflict_evidence_conditions**: Different GSTIN strings (e.g. diff state, diff PAN, or diff entity number).
- **missingness_conditions**: MISSING_INPUT when one or both GSTINs are absent.
- **known_confounders**: OCR errors converting '0' to 'O'.
- **authority_sensitive_interpretations**: Deterministic parsing rule.
- **MUST NOT IMPLY**: MUST NOT directly imply `identity.same_legal_entity` (an entity holds many GSTINs). MUST NOT imply `identity.different_legal_entity` if GSTINs differ.

## 3. identity.same_tax_identity
- **ClaimId**: `identity.same_tax_identity`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations refer to the same 10-character Permanent Account Number (PAN) issued by the Indian Income Tax Department.
- **positive_evidence_conditions**: Exact equality of the 10-character PAN extracted from a validated GSTIN or direct PAN observation.
- **conflict_evidence_conditions**: Different 10-character PANs.
- **missingness_conditions**: MISSING_INPUT when PAN cannot be derived.
- **known_confounders**: Fraudulent PAN use.
- **authority_sensitive_interpretations**: Highly authoritative if validated.
- **MUST NOT IMPLY**: MUST NOT imply `identity.same_gst_registration` (same PAN can hold different state GSTINs).

## 4. identity.same_organization_core
- **ClaimId**: `identity.same_organization_core`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations share the identical canonical lexical core name, after stripping legal forms, punctuation, and normalized whitespace.
- **positive_evidence_conditions**: Exact string equality of the canonicalized organization core.
- **conflict_evidence_conditions**: None (lexical mismatch does not prove they are not the same core via aliases).
- **missingness_conditions**: MISSING_INPUT if the parsed core is empty.
- **known_confounders**: Highly common tokens (e.g., "BALAJI ENTERPRISES").
- **authority_sensitive_interpretations**: Magnitude may be bounded by corpus distinctiveness.
- **MUST NOT IMPLY**: MUST NOT imply `identity.same_legal_entity` (ABC TRADERS != ABC TECHNOLOGIES, or parent/subsidiary sharing "TATA").

## 5. identity.same_legal_form
- **ClaimId**: `identity.same_legal_form`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations explicitly declare the same canonical structural categorization under corporate law.
- **positive_evidence_conditions**: Extraction yields identical canonical legal forms (e.g., PVT LTD and PRIVATE LIMITED both map to PRIVATE_LIMITED).
- **conflict_evidence_conditions**: Extraction yields different canonical legal forms (e.g., PRIVATE_LIMITED vs LLP).
- **missingness_conditions**: MISSING_INPUT if one or both representations lack a recognizable legal form.
- **known_confounders**: Trade names frequently omit the legal form.
- **authority_sensitive_interpretations**: Deterministic parsing rule.
- **MUST NOT IMPLY**: Equality MUST NOT imply `identity.same_legal_entity` (millions of firms share a legal form). Absence MUST NOT imply conflict.

## 6. identity.same_trade_name
- **ClaimId**: `identity.same_trade_name`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations use the same "doing business as" brand or trade name.
- **positive_evidence_conditions**: Exact string match of extracted trade name tokens.
- **conflict_evidence_conditions**: None.
- **missingness_conditions**: MISSING_INPUT if not present.
- **known_confounders**: Franchises sharing trade names.
- **authority_sensitive_interpretations**: Usually extracted heuristically.
- **MUST NOT IMPLY**: Equality MUST NOT imply `identity.same_legal_entity`. Inequality MUST NOT imply `identity.different_legal_entity`.

## 7. identity.same_branch
- **ClaimId**: `identity.same_branch`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations refer to the specific physical or operational location of a legal entity.
- **positive_evidence_conditions**: Exact match of branch codes or highly specific address parsing.
- **conflict_evidence_conditions**: Explicitly different branch codes for the same entity.
- **missingness_conditions**: MISSING_INPUT if branch details are absent.
- **known_confounders**: Multiple addresses for the same branch.
- **authority_sensitive_interpretations**: Requires ERP or registry authority.
- **MUST NOT IMPLY**: Inequality MUST NOT imply `identity.different_legal_entity`.

## 8. identity.same_vendor_master_record
- **ClaimId**: `identity.same_vendor_master_record`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations map to the exact same internal record ID in the buyer's ERP/vendor master system.
- **positive_evidence_conditions**: Exact match of ERP vendor codes.
- **conflict_evidence_conditions**: None (due to ERP duplication).
- **missingness_conditions**: MISSING_INPUT if vendor codes are unmapped.
- **known_confounders**: Duplicate vendor records created by users.
- **authority_sensitive_interpretations**: ERP database is the authority.
- **MUST NOT IMPLY**: Inequality MUST NOT imply `identity.different_legal_entity` (an entity may have multiple ERP records).

## 9. identity.same_geographic_registration
- **ClaimId**: `identity.same_geographic_registration`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR
- **semantic_definition**: Both representations hold a registration in the same state/jurisdiction.
- **positive_evidence_conditions**: Matching GSTIN state codes (first 2 digits).
- **conflict_evidence_conditions**: None.
- **missingness_conditions**: MISSING_INPUT if state code cannot be extracted.
- **known_confounders**: Entities have registrations in multiple states.
- **authority_sensitive_interpretations**: Deterministic parsing.
- **MUST NOT IMPLY**: Inequality MUST NOT imply `identity.different_legal_entity`.

## 10. identity.same_corporate_group
- **ClaimId**: `identity.same_corporate_group`
- **semantic_version**: 1
- **symmetry**: SYMMETRIC
- **allowed_scope_kinds**: RECORD_PAIR, GROUP_PAIR
- **semantic_definition**: Both representations belong to the same economic conglomerate or parent-subsidiary cluster.
- **positive_evidence_conditions**: Strong organization core overlap paired with known registry linkage.
- **conflict_evidence_conditions**: Explicit proof of different ownership groups.
- **missingness_conditions**: INSUFFICIENT_INPUT if no group linkage data is available.
- **known_confounders**: Coincidental name similarities.
- **authority_sensitive_interpretations**: Highly dependent on MCA/registry data.
- **MUST NOT IMPLY**: Equality MUST NOT imply `identity.same_legal_entity` (Tata Motors != Tata Power).
