# Stage 8C-V1-0 Gate QA (Q1–Q60 Audit)

## Section 1: Latent Variables & Semantic Identity (Q1-Q10)

**1. What exact latent variable does "vendor identity" refer to?**
"Vendor identity" is an overloaded term that naively conflates `LEGAL_ENTITY_IDENTITY`, `TRADE_NAME_IDENTITY`, and `VENDOR_MASTER_IDENTITY`. In Stage 8C, we decompose it; the ultimate reconciliation target is usually `LEGAL_ENTITY_IDENTITY`, but we can only observe attributes (like `ORGANIZATION_CORE_IDENTITY`) and state registrations (like `GST_REGISTRATION_IDENTITY`).

**2. Why is lexical equality not legal identity?**
Lexical equality (e.g., "ABC TRADERS" == "ABC TRADERS") proves `identity.same_organization_core`. It does not prove they are the same juridical person. "ABC TRADERS" in Delhi might be a distinct proprietorship from "ABC TRADERS" in Mumbai. Conversely, "ABC TRADERS" might be the trade name for "XYZ PRIVATE LIMITED". 

**3. Can one legal entity have multiple GST registrations?**
Yes. An entity can (and often must) have at least one GSTIN per state where it operates, and can have multiple GSTINs within the same state for different business verticals.

**4. Can two records share organization core but represent different legal entities?**
Yes. Two different entities can adopt the same organization core (e.g., millions of local shops use common names like "BALAJI ENTERPRISES"). Parent and subsidiary companies also frequently share the core (e.g., "RELIANCE INDUSTRIES" and "RELIANCE RETAIL" sharing "RELIANCE").

**5. Can legal-form mismatch prove different legal entities?**
Yes. If one record explicitly declares `PRIVATE_LIMITED` and the other declares `LIMITED_LIABILITY_PARTNERSHIP`, these are structurally distinct entities under corporate law. This yields `CONFLICT identity.same_legal_form`.

**6. When is legal-form absence missingness rather than agreement?**
When a trade name or casual invoice omits the legal form (e.g., "ABC" vs "ABC PRIVATE LIMITED"), the absence of the form in the first string is an absence of data (`MISSING_INPUT`), not an assertion that the entity has no legal form. 

**7. Should ABC LTD and ABC produce legal-form conflict?**
No. "ABC" lacks a legal form, so it yields `MISSING_INPUT` for the legal form factor. We cannot assume "ABC" is not a limited company.

**8. Should ABC PVT LTD and ABC LLP produce legal-entity conflict directly?**
No. They produce `CONFLICT identity.same_legal_form`. Stage 8J (fusion) will evaluate that conflict alongside other factors (like matching GSTINs, if present, which might override the name conflict if one system has an outdated name).

**9. What does same PAN support?**
Same PAN asserts `SUPPORT identity.same_tax_identity`, which provides extremely strong (though technically not absolute, due to mergers) evidence supporting `identity.same_legal_entity`.

**10. What does different PAN conflict with?**
Different PAN asserts `CONFLICT identity.same_tax_identity` and `CONFLICT identity.same_gst_registration` (since PAN is embedded in GSTIN). It strongly implies `different_legal_entity`.

## Section 2: Tax Identity Semantics (Q11-Q20)

**11. Can malformed GSTIN produce any tax assertion?**
No. A malformed GSTIN yields `UNINTERPRETABLE_INPUT` for both tax and GST registration factors.

**12. Should deterministic GSTIN repair exist in V1?**
No. "Validate, don't guess." Auto-repairing OCR errors (like O to 0) introduces non-deterministic risk. It should be handled as a separate low-authority pipeline (e.g. Stage 8D), not the deterministic V1 pipeline.

**13. What is an organization core?**
The central lexical component of a firm's name, derived by stripping recognized legal designators, normalizing whitespace/punctuation, and canonicalizing unicode.

**14. Is organization core extraction reversible?**
No. Once "PVT LTD" is stripped to leave "ABC", you cannot determine if the original string was "ABC PVT LTD", "ABC PRIVATE LIMITED", or just "ABC". This is why `VendorNameObservation` must store spans and events.

**15. Which normalization steps destroy information?**
All of them. Case folding destroys capitalization; legal form stripping destroys structural indicators; punctuation removal destroys abbreviations.

**16. Must all destructive transformations first emit structured observations?**
Yes. Information extraction must precede information removal. This is stored in `VendorNormalizationEvent`s inside the `DerivedArtifact`.

**17. Are token positions semantically meaningful?**
Yes. "PRIVATE LIMITED" at the end of a string is a legal designator. "COMPANY" at the start of a string (e.g., "COMPANY FORMATION SERVICES") is part of the organization core.

**18. Is token multiplicity meaningful?**
Yes. "MAHINDRA MAHINDRA" is semantically distinct from "MAHINDRA".

**19. Does MAHINDRA MAHINDRA equal MAHINDRA?**
No. Token multiset equality or exact core match fails here.

**20. Are connectors such as AND and & semantic?**
They are semantically equivalent to each other (connectors) and should be canonicalized (e.g., `&` → `AND`), but they are not purely noise; they structure the core.

## Section 3: Similarity, Metrics, and Rarity (Q21-Q35)

**21. How do we treat SHREE versus SRI?**
These are phonetic/transliteration variants. They should be recognized by specialized equivalence rules or phonetic matching, but must carry a lower confidence magnitude than exact matches.

**22. Is phonetic similarity evidence or preprocessing?**
It is an observation (evidence). Preprocessing (canonicalization) must be strictly deterministic and un-opinionated.

**23. Can fuzzy metric values directly become assertion magnitudes?**
No. 

**24. Why not?**
A Jaro-Winkler score of 0.92 means there is high edit similarity. It does *not* mean there is a 92% probability they are the same core, nor does it translate directly to a semantic magnitude of 0.92. Metric output is an observation; assertion magnitude is a policy-driven interpretation of that observation.

**25. Which metric best separates hard positives from hard negatives?**
Token-set equality combined with canonical exact match handles reordering and variants well. Jaro-Winkler is prone to false positives on short acronyms.

**26. What happens when all metrics disagree?**
The interpretation policy defines precedence (e.g., exact match wins). If metrics yield weak or conflicting signals below threshold, no assertion is emitted (`INSUFFICIENT_INPUT`).

**27. Should the provider emit multiple metric assertions?**
No. It should emit one assertion per semantic proposition (e.g., one `SUPPORT identity.same_organization_core`).

**28. Would that create correlated evidence?**
Yes, emitting `SUPPORT same_core` via ExactMatch and `SUPPORT same_core` via TokenSet from the same two strings is double-counting.

**29. Should metrics instead become one derived artifact consumed by one interpreter?**
Yes. The metrics are observations computed on the `DerivedArtifact`. The interpreter evaluates them and emits a single assertion per factor.

**30. How does Stage 8J know multiple assertions came from the same lexical observation?**
Through the `EvidenceAncestryRef` on the `EvidenceAssertion`, which points back to the exact `ObservationOccurrence` (the raw vendor string) or `DerivationOccurrence`.

**31. What vendor tokens are common?**
Tokens like `ENTERPRISES`, `TRADERS`, `INDUSTRIES`, `SERVICES`, `GLOBAL`, `INDIA`.

**32. Should token rarity affect exact organization-core equality?**
Yes. If two records are exactly "BALAJI ENTERPRISES", it is a match, but the magnitude of the `same_organization_core` assertion should be bounded/reduced because the core is highly common.

**33. Should token rarity affect partial overlap?**
Yes, heavily. Sharing the token `MAHINDRA` is strong evidence; sharing the token `TRADERS` is nearly meaningless.

**34. Can corpus statistics create conflict evidence?**
No.

**35. Or can they only reduce/withhold support?**
They can only reduce or withhold support. High frequency is an absence of distinctiveness, not a contradiction.

## Section 4: Aliases and Lineage (Q36-Q42)

**36. Is acronym derivation deterministic?**
Yes, algorithmic acronym derivation (e.g., taking the first letter of non-stop words) is deterministic.

**37. Is acronym equality strong evidence?**
No, it is very low authority evidence due to massive collision rates (e.g., TCS = Tata Consultancy Services OR TCS Logistics).

**38. How do we prevent TCS collisions?**
By refusing to emit high-magnitude assertions based solely on derived acronyms, relying instead on known alias registries or requiring corroborating GSTIN evidence.

**39. What is the authority of a known vendor-master alias?**
High authority (`vendor_master.alias_registry`), provided the alias snapshot is accurate.

**40. What is the authority of an algorithmically derived acronym?**
Low authority (`deterministic_rule.acronym_derivation`).

**41. Does source lineage affect assertion magnitude?**
No, source lineage tracks *where* the evidence came from.

**42. Or only fusion interpretation?**
Only fusion interpretation (Stage 8J). Fusion looks at the lineage to discount correlated evidence (e.g., two acronym observations derived from the exact same PDF invoice).

## Section 5: Architecture and Factors (Q43-Q52)

**43. Should a factor-level result be missing while the vendor interpretation remains valid?**
Yes. `VendorIdentityInterpretation` is factorized. The legal form can be `MISSING_INPUT` while the organization core is `INTERPRETED`.

**44. Why is one global vendor state dangerous?**
If a missing vendor name forces a global `MISSING_INPUT` state, it silently discards perfectly valid GSTIN or PAN evidence present on the same records.

**45. Should vendor interpretation use fixed fields or open factor IDs?**
Open factor IDs (`VendorIdentityFactorId`). As seen with `ClaimId`, fixed dataclass fields explode when plugins add new factors (e.g., LEI, DUNS).

**46. How are duplicate factor results prevented?**
The interpretation tuple rejects duplicate `VendorIdentityFactorId`s at construction.

**47. How is factor ordering canonicalized?**
The tuple of factors is canonically sorted by the string value of the factor ID.

**48. Which policy values alter derivation semantics?**
Any policy value that changes assertion output (e.g., `similarity_threshold` dropping from 0.90 to 0.85). 

**49. Must corpus profile identity participate in derivation identity?**
Yes. If the corpus profile updates and changes token distinctiveness, the resulting assertion magnitudes might change. It must be tracked via a `SemanticDependencyRef`.

**50. Must alias snapshot identity participate?**
Yes, for the same reason.

**51. Can mutable alias data be globally cached?**
Yes, but the cache key must include the cryptographic digest of the alias snapshot (`MutableReference` dependency) so cache hits are semantically safe.

**52. How should an absent alias snapshot differ from an empty alias snapshot?**
Absent = `MISSING_INPUT` (the system lacks the capability to check). Empty = `INSUFFICIENT_INPUT` (the system checked, but found no aliases for this input).

## Section 6: Materialization and Integration (Q53-Q60)

**53. Is parsing a reusable derived artifact?**
Yes. Structured vendor parses are stored as `DerivedArtifact`s because they are computationally expensive and semantically reusable.

**54. Should parsing occur before candidate generation?**
Yes, ideally. This is Option C (Pre-Materialization). 

**55. How many times is a vendor currently evaluated per reconciliation run?**
Currently, vendor evidence is evaluated per *candidate pair*. If a record has 100 candidates, it is evaluated 100 times.

**56. What is the projected parse amplification factor?**
Massive. 1,000 purchases × 1,000 GSTs × 100 candidates = 200,000 parse operations for only 2,000 unique strings.

**57. Can content-addressed artifacts eliminate duplicate parsing?**
Yes. By caching parses keyed on `ObservationIdentity` (or pre-materializing them), we drop 200,000 parses down to 2,000.

**58. What information must the V1 scalar adapter discard?**
It discards assertion polarity (conflict vs support), ancestry, authority basis, factor-level granularity, and magnitude distinctions.

**59. How will we prove the adapter is lossy and never authoritative?**
By explicitly naming it `project_vendor_evidence_to_legacy_scalar`, documenting it as a temporary Stage 8C-to-8A bridge, and preventing it from being used as the ground truth.

**60. What exact boundary marks Stage 8C-V1 ready for implementation?**
The completion and approval of this research gate: the factor model, claim catalog, legal ontology, state tables, similarity/corpus research, DAG architecture, conformance/metamorphic suites, and context/adapter designs—with absolutely zero production vendor pipeline code written.
