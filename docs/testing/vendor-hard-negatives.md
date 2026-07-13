# Vendor Hard Negatives

This document defines the permanent adversarial specification that future Vendor Identity implementations must survive.

| Case ID | Observed Name A | Observed Name B | Identifier State | Known Ground Truth | What Lexical Evidence Says | What Authoritative Evidence Says | Knowledge Required | Dangerous Naive Conclusion |
|---|---|---|---|---|---|---|---|---|
| VH001 | SHREE TRADERS | SHREE ENTERPRISES | Exact Identifier | Same Entity | Low/Medium | Match | Generic suffix collision | Different vendors due to name |
| VH002 | ABC LLP | ABC PRIVATE LIMITED | Exact Identifier | Same Entity (renamed) | High | Match | Suffix conflict | Different vendors |
| VH003 | TATA MOTORS | TATA TECHNOLOGIES | Different Identifier | Different Entity | Medium/High | Conflict | Corporate family | Same vendor due to 'TATA' |
| VH004 | ABC | ABC | Different Identifier | Different Entity | Exact | Conflict | Abbreviation collision | Same vendor |
| VH005 | MICROSOFT | MICR0SOFT | Exact Identifier | Same Entity | High | Match | OCR corruption (0 vs O) | Different vendors |
| VH006 | 123 STORE | ONE TWO THREE STORE | Exact Identifier | Same Entity | Low | Match | Numeric substitution | Different vendors |
| VH007 | A&B | AB | Exact Identifier | Same Entity | High | Match | Punctuation collapse | Same vendor |
| VH008 | COMPANY A | COMPANY    A | Exact Identifier | Same Entity | High | Match | Whitespace collapse | Different vendors |
| VH009 | XEROX | XEROX CORPORATION | Exact Identifier | Same Entity | Medium | Match | Brand vs Legal Entity | Different vendors |
| VH010 | FACEBOOK INC | META PLATFORMS INC | Exact Identifier | Same Entity | Low | Match | Historical rename | Different vendors |
| VH011 | TRADERS | TRADERS | No Identifier | Unknown | Exact | Missing | Exact generic names | Same vendor |
| VH012 | BHARAT LTD | INDIA LTD | Exact Identifier | Same Entity | Medium | Match | Multilingual/transliteration | Different vendors |
| VH013 | ALPHABET INC | GOOGLE LLC | Different Identifier | Different Entity | Low | Conflict | Parent/subsidiary | Unrelated |
| VH014 | ALPHA IND | OMEGA LOGISTICS | Exact Identifier | Same Entity (anomaly) | Low | Match | Same ID / Different Name | Different vendors |
| VH015 | ABC LTD | ABC LTD | Different Identifier | Different Entity | Exact | Conflict | Different ID / Same Name | Same vendor |
| VH016 | RELIANCE RETAIL | RELIANCE JIO | Different Identifier | Different Entity | Medium | Conflict | Corporate family | Same vendor |
| VH017 | AMAZON SELLER SERVICES | AMAZON TRANSPORTATION | Different Identifier | Different Entity | Medium | Conflict | Corporate family | Same vendor |
| VH018 | FLIPKART | INSTAKART | Exact Identifier | Same Entity | Low | Match | Brand/Entity mismatch | Different vendors |
| VH019 | IBM | INTERNATIONAL BUSINESS MACHINES | Exact Identifier | Same Entity | Low | Match | Acronym expansion | Different vendors |
| VH020 | H&M | HENNES & MAURITZ | Exact Identifier | Same Entity | Low | Match | Brand expansion | Different vendors |
| VH021 | APPLE INC | APPLE | Exact Identifier | Same Entity | High | Match | Missing suffix | Different vendors |
| VH022 | P W C | PWC | Exact Identifier | Same Entity | High | Match | Whitespace injection | Different vendors |
| VH023 | DELOITTE | DELOITE | Exact Identifier | Same Entity | High | Match | Typo | Different vendors |
| VH024 | ERNST & YOUNG | EY | Exact Identifier | Same Entity | Low | Match | Acronym | Different vendors |
| VH025 | L&T | LARSEN AND TOUBRO | Exact Identifier | Same Entity | Low | Match | Acronym/Ampersand | Different vendors |
| VH026 | TCS | TATA CONSULTANCY SERVICES | Exact Identifier | Same Entity | Low | Match | Acronym | Different vendors |
| VH027 | INFOSYS | INFOSYS TECHNOLOGIES | Exact Identifier | Same Entity | High | Match | Historical suffix drop | Different vendors |
| VH028 | MAHINDRA | MAHINDRA & MAHINDRA | Exact Identifier | Same Entity | High | Match | Brand vs Legal | Different vendors |
| VH029 | SBI | STATE BANK OF INDIA | Exact Identifier | Same Entity | Low | Match | Acronym | Different vendors |
| VH030 | HDFC | HOUSING DEVELOPMENT FINANCE CORP | Exact Identifier | Same Entity | Low | Match | Acronym | Different vendors |
