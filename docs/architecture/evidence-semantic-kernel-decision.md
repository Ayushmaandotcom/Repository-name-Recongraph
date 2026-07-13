# Evidence Semantic Kernel Architecture Decision Report

This report finalizes Stage 8C-0C.

## Environment
**Q1. Why did RapidFuzz fail to import?** The repository was executed in an environment (likely global or a different venv) where the dependency existed, but the active interpreter lacked it. The declaration in `pyproject.toml` was correct.
**Q2. Is repository reproducibility currently healthy?** Yes. A clean `pip install -e .[dev]` restored the environment.
**Q3. What action, if any, is required?** None further.

## Claims
**Q4. Does ReconGraph require first-class target claims?** Yes. Evidence without a target proposition is meaningless.
**Q5. Which claim model is recommended?** Claim Model B (Typed Claim Identifier).
**Q6. Why?** It provides type safety and extensibility without the overhead of a formal logical reasoning registry (which is overkill for v0.1).
**Q7. Are negative claims explicitly represented in v0.1?** No. Conflict against a positive claim is sufficient.
**Q8. Can claims express logical relationships in v0.1?** No. Entailment rules are deferred to Stage 8J fusion.

## Evidence State
**Q9. What states are required?** `OBSERVED`, `MISSING`, `UNINTERPRETABLE`.
**Q10. Are absence and ignorance distinct?** Yes. Missing data vs data the model cannot parse.
**Q11. Can observed evidence carry zero support and zero conflict?** Yes. (Neutral evidence).
**Q12. Can uninterpretable evidence carry magnitude?** No.

## Magnitude
**Q13. What exactly does support magnitude mean?** The degree to which the observation corroborates the target claim, independent of its epistemic authority.
**Q14. What exactly does conflict magnitude mean?** The degree to which the observation contradicts the target claim.
**Q15. Are they probabilities?** No.
**Q16. Must support + conflict <= 1.0?** No. They are independent measurements of semantic vectors.
**Q17. Can support and conflict both be non-zero?** Yes. Bipolar evidence exists.

## Authority
**Q18. What minimum authority seam is required?** Authority Model C (Structured Descriptor). A minimal enum like `AuthorityClass(SYSTEM_OF_RECORD, EXTRACTED)`.
**Q19. Is authority numeric?** No.
**Q20. Is authority totally ordered?** No.
**Q21. Does authority alter magnitude?** No. It contextualizes magnitude.

## Lineage
**Q22. Which lineage model is recommended?** Lineage Model L2 (Structured).
**Q23. Which fields are mandatory?** `source_system` and `source_record_id`.
**Q24. Which may be unknown?** None (they must be explicitly tracked at ingestion).
**Q25. Does lineage itself assert dependence?** No. It asserts factual shared provenance.

## Payload
**Q26. Which typed payload contract is recommended?** TP-C (Tagged Serializable Union).
**Q27. How are payload types identified?** Via a string `payload_type` tag.
**Q28. How are schema versions represented?** Via a `schema_version` integer/string field.
**Q29. What happens to unknown payload versions?** Deserialized into a generic `dict` preserving the tag.
**Q30. Can plugins introduce payloads without editing the core?** Yes, by defining a new tag and adhering to the union schema.

## Kernel
**Q31. Which semantic kernel object model is recommended?** Kernel D (Claim-Centric `EvidenceAssertion`).
**Q32. Does it replace `EvidenceContributionV2`?** No.
**Q33. Does it wrap it?** `EvidenceContributionV2` wraps one or more `EvidenceAssertion`s.
**Q34. What exact responsibilities belong to the kernel?** Enforcing state algebra invariants, bounding magnitudes, structuring lineage and authority.
**Q35. What responsibilities are explicitly forbidden?** Fusion, decision thresholds, and probability calibration.

## Vendor Identity
**Q36. Is `SAME_LEGAL_ENTITY` still the correct Stage 8C claim after the identifier authority audit?** No. GSTIN equality only observes `SAME_GST_REGISTRATION`. Using it to claim `SAME_LEGAL_ENTITY` will falsely penalize legitimate cross-state branches.
**Q37. Or should Stage 8C model a narrower identity claim?** Yes. It must model both `SAME_LEGAL_ENTITY` (via PAN) and `SAME_GST_REGISTRATION` (via GSTIN) separately.
**Q38. Which Vendor v0.1 primitive evidence units are authorized?** VE-001 (Exact Lexical Name), VE-003/004 (Legal Form Extraction), VE-005/006 (Authoritative ID Agreement/Conflict).
**Q39. Which units are explicitly deferred?** Corpus Statistics, Aliases, OCR correction, Generics.
**Q40. Does Vendor v0.1 require corpus statistics?** No, explicitly deferred.
**Q41. Does Vendor v0.1 require external alias knowledge?** No, explicitly deferred.
**Q42. Does Vendor v0.1 perform OCR correction?** No.

## Compatibility
**Q43. Can the existing scalar provider interface remain temporarily?** Yes.
**Q44. Where does the V2-to-V1 projection occur?** In an explicit Adapter prior to the Explanation Builder.
**Q45. Is that projection allowed inside the semantic kernel?** Absolutely not.
**Q46. What is the explicit deletion condition for the V1 projection?** When downstream review UI and benchmarks natively accept typed V2 Evidence Assertions.

## Stage 8J
**Q47. What information will Stage 8J receive that it does not receive today?** Explicit claims, bipolar support/conflict magnitudes, epistemic authority, and source lineage.
**Q48. What information will Stage 8J still NOT know?** True statistical dependence (covariance).
**Q49. What empirical work remains before dependence-aware fusion?** Gathering ground-truth error distribution data across systems.
**Q50. What architectural mistake would be most expensive to reverse after this stage?** Conflating magnitude with probability, or using an untyped dictionary for payloads without versioning.
