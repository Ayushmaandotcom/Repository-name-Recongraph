# Vendor Identity Factor Model V1

Vendor identity is not a monolith. Lexical similarity is not legal identity. This document explicitly decomposes vendor identity into distinct latent variables. 

## Latent Variables

### 1. LEGAL_ENTITY_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | A distinct legal person (corporation, LLP, partnership, individual) capable of entering contracts and bearing liability. |
| **Identity/Attribute** | Entity Identity |
| **Shared by multiple entities?** | No. |
| **Multiple values per entity?** | No. |
| **Equality = Support?** | Yes (Tautological: this is the target identity). |
| **Inequality = Conflict?** | Yes. |
| **Missing? Ambiguous? Derived?** | Never missing in reality. Highly ambiguous in records. Strictly derived via Stage 8J fusion. |
| **Observable via** | Legal registries (MCA), tax filings, authoritative vendor masters. Not directly observable from generic text. |
| **Correlations** | Strongly correlated with TAX_IDENTITY, GST_REGISTRATION_IDENTITY, ORGANIZATION_CORE_IDENTITY. |
| **Stronger claims supported** | Corporate group membership. |
| **MUST NEVER IMPLY** | That two distinct entities share operations (they might be entirely separate). |

### 2. GST_REGISTRATION_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | A specific registration under the Goods and Services Tax regime in a specific Indian state. |
| **Identity/Attribute** | Entity Identity (State-level) |
| **Shared by multiple entities?** | No. (A GSTIN maps to exactly one PAN). |
| **Multiple values per entity?** | Yes. (An entity can have one per state, and sometimes multiple per state). |
| **Equality = Support?** | Yes. |
| **Inequality = Conflict?** | Yes (for state-registration identity). |
| **Missing? Ambiguous? Derived?** | Missing frequently. Derived deterministically if parsing succeeds. |
| **Observable via** | GSTIN strings on invoices, GST portal, tax records. |
| **Correlations** | Perfectly correlates with state geography and TAX_IDENTITY (PAN is embedded). |
| **Stronger claims supported** | `identity.same_tax_identity` (implicitly). |
| **MUST NEVER IMPLY** | Inequality MUST NOT imply `different_legal_entity` (an entity holds many GSTINs). |

### 3. ORGANIZATION_CORE_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | The central lexical component of a firm's name, stripped of legal designators and noise. |
| **Identity/Attribute** | Attribute Identity |
| **Shared by multiple entities?** | Yes. (e.g. ABC PVT LTD and ABC LLP share "ABC"). |
| **Multiple values per entity?** | Yes. (Trade names, aliases, rebranded divisions). |
| **Equality = Support?** | Yes (positive lexical evidence). |
| **Inequality = Conflict?** | No. (A firm can use different aliases/cores). |
| **Missing? Ambiguous? Derived?** | Derived algorithmically. Can be missing/ambiguous. |
| **Observable via** | Purchase orders, invoices, bank statements. |
| **Correlations** | Strongly correlates with TRADE_NAME_IDENTITY, LEGAL_ENTITY_IDENTITY. |
| **Stronger claims supported** | Provides support to `identity.same_legal_entity`. |
| **MUST NEVER IMPLY** | Equality MUST NOT imply `identity.same_legal_entity` (ABC TRADERS != ABC TECHNOLOGIES). |

### 4. LEGAL_FORM_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | The canonical structural categorization of the firm under corporate law (e.g., PRIVATE LIMITED, LLP). |
| **Identity/Attribute** | Attribute Identity |
| **Shared by multiple entities?** | Yes (millions of Private Limiteds). |
| **Multiple values per entity?** | No (at a given snapshot in time, an entity has exactly one legal form). |
| **Equality = Support?** | Yes. |
| **Inequality = Conflict?** | Yes. |
| **Missing? Ambiguous? Derived?** | Often missing in trade usage. Derived via parsing. |
| **Observable via** | Vendor names, registry filings. |
| **Correlations** | None directly, mostly independent. |
| **Stronger claims supported** | Supports `identity.same_legal_entity`. |
| **MUST NEVER IMPLY** | Equality MUST NOT imply `identity.same_legal_entity`. Absence MUST NOT imply conflict. |

### 5. BRANCH_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | A specific physical or operational location of a legal entity. |
| **Identity/Attribute** | Entity Identity (Sub-entity) |
| **Shared by multiple entities?** | No. |
| **Multiple values per entity?** | Yes. |
| **Equality = Support?** | Yes. |
| **Inequality = Conflict?** | Yes (for branch). |
| **Missing? Ambiguous? Derived?** | Often missing. |
| **Observable via** | Addresses, internal vendor codes, GSTIN (state-level branch proxy). |
| **Correlations** | GEOGRAPHIC_REGISTRATION_IDENTITY. |
| **Stronger claims supported** | `identity.same_legal_entity`. |
| **MUST NEVER IMPLY** | Inequality MUST NOT imply `different_legal_entity`. |

### 6. TRADE_NAME_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | The "doing business as" (DBA) brand or trade name used by an entity. |
| **Identity/Attribute** | Attribute Identity |
| **Shared by multiple entities?** | Yes (trademarks can be shared/licensed, or coincidentally identical). |
| **Multiple values per entity?** | Yes (an entity can operate multiple brands). |
| **Equality = Support?** | Yes. |
| **Inequality = Conflict?** | No. |
| **Missing? Ambiguous? Derived?** | Highly ambiguous. Derived. |
| **Observable via** | Invoices, websites, GST portal. |
| **Correlations** | ORGANIZATION_CORE_IDENTITY. |
| **Stronger claims supported** | `identity.same_legal_entity`. |
| **MUST NEVER IMPLY** | Equality MUST NOT imply `identity.same_legal_entity`. Inequality MUST NOT imply `different_legal_entity`. |

### 7. GEOGRAPHIC_REGISTRATION_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | The state or jurisdiction where a particular registration is held. |
| **Identity/Attribute** | Attribute Identity |
| **Shared by multiple entities?** | Yes (millions share a state). |
| **Multiple values per entity?** | Yes. |
| **Equality = Support?** | Yes (weak). |
| **Inequality = Conflict?** | No. |
| **Missing? Ambiguous? Derived?** | Derived from GSTIN state codes. |
| **Observable via** | GSTIN. |
| **Correlations** | GST_REGISTRATION_IDENTITY, BRANCH_IDENTITY. |
| **Stronger claims supported** | `identity.same_gst_registration` (necessary component). |
| **MUST NEVER IMPLY** | Inequality MUST NOT imply `different_legal_entity`. |

### 8. TAX_IDENTITY (PAN)
| Property | Value |
|---|---|
| **Real-world thing** | The 10-character Permanent Account Number issued by the Income Tax Department. |
| **Identity/Attribute** | Entity Identity (National-level) |
| **Shared by multiple entities?** | No. |
| **Multiple values per entity?** | No (strictly 1:1 with legal entity in India). |
| **Equality = Support?** | Yes (very strong). |
| **Inequality = Conflict?** | Yes (very strong). |
| **Missing? Ambiguous? Derived?** | Derived from GSTIN. |
| **Observable via** | GSTIN extraction, PAN card, registry. |
| **Correlations** | LEGAL_ENTITY_IDENTITY, GST_REGISTRATION_IDENTITY. |
| **Stronger claims supported** | `identity.same_legal_entity`. |
| **MUST NEVER IMPLY** | Equality MUST NOT imply `identity.same_gst_registration` (same PAN can hold different state GSTINs). |

### 9. VENDOR_MASTER_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | A record ID in the buyer's internal ERP or vendor master system. |
| **Identity/Attribute** | Entity Identity (System-level) |
| **Shared by multiple entities?** | No. |
| **Multiple values per entity?** | Yes (duplicate vendor records are common in ERPs). |
| **Equality = Support?** | Yes. |
| **Inequality = Conflict?** | No (due to ERP duplication). |
| **Missing? Ambiguous? Derived?** | Often missing in external docs. |
| **Observable via** | Purchase records, vendor mappings. |
| **Correlations** | LEGAL_ENTITY_IDENTITY. |
| **Stronger claims supported** | `identity.same_legal_entity`. |
| **MUST NEVER IMPLY** | Inequality MUST NOT imply `different_legal_entity`. |

### 10. CORPORATE_GROUP_IDENTITY
| Property | Value |
|---|---|
| **Real-world thing** | An economic conglomerate or parent-subsidiary cluster (e.g., The Tata Group). |
| **Identity/Attribute** | Group Identity |
| **Shared by multiple entities?** | Yes (by definition). |
| **Multiple values per entity?** | No. |
| **Equality = Support?** | Yes. |
| **Inequality = Conflict?** | Yes. |
| **Missing? Ambiguous? Derived?** | Highly derived. |
| **Observable via** | Organization core similarities (sometimes), registries (MCA), external datasets. |
| **Correlations** | ORGANIZATION_CORE_IDENTITY (parent/subsidiary often share cores). |
| **Stronger claims supported** | N/A (this is a macro group). |
| **MUST NEVER IMPLY** | Equality MUST NOT imply `identity.same_legal_entity` (Tata Motors != Tata Power, despite sharing group identity). |

## Correlation Matrix

| Variable | Correlates With | Direction / Nature |
|---|---|---|
| GST_REGISTRATION_IDENTITY | TAX_IDENTITY | Contains PAN; same GSTIN → same PAN. |
| TAX_IDENTITY | LEGAL_ENTITY_IDENTITY | Strictly 1:1. PAN defines the legal taxpayer. |
| ORGANIZATION_CORE_IDENTITY | CORPORATE_GROUP_IDENTITY | Subsidiaries often share core tokens (e.g., Reliance). |
| TRADE_NAME_IDENTITY | ORGANIZATION_CORE_IDENTITY | Trade names often map directly to organization cores. |
| GST_REGISTRATION_IDENTITY | GEOGRAPHIC_REGISTRATION_IDENTITY | GSTIN state code maps 1:1 with state jurisdiction. |

## Non-Entailment Rules (Invariants)

1. `ORGANIZATION_CORE_IDENTITY` equality MUST NOT imply `identity.same_legal_entity`.
2. `GST_REGISTRATION_IDENTITY` inequality MUST NOT imply `identity.different_legal_entity` (entities hold multiple state registrations).
3. `LEGAL_FORM_IDENTITY` equality MUST NOT imply `identity.same_legal_entity` (millions of firms share a legal form).
4. `TAX_IDENTITY` (PAN) equality strongly supports but MUST NOT strictly imply `identity.same_legal_entity` in all contexts without verification (exceptions exist around mergers, though rare).
5. `TAX_IDENTITY` equality MUST NOT imply `identity.same_gst_registration` (different state registrations have the same PAN).
6. `VENDOR_MASTER_IDENTITY` inequality MUST NOT imply `identity.different_legal_entity` (due to ERP duplication).
7. `CORPORATE_GROUP_IDENTITY` equality MUST NOT imply `identity.same_legal_entity` (parent/subsidiary confusion).
