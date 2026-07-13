# Evidence Assertion Kernel Architecture Decision Report V2

## Scope
**Q1. Does EvidenceAssertion require explicit subject scope?** Yes. An assertion without a subject is semantically meaningless.
**Q2. Which scope model is selected?** Scope D (Canonical Proposition Subject).
**Q3. Why?** It preserves bipartite structure (Left/Right) allowing 1:1, 1:N, and N:M assertions.
**Q4. Are scopes directional?** Scope directionality is determined by the *Claim*, not the scope object.
**Q5. How are symmetric scopes canonicalized?** If the Claim is symmetric, the Left and Right subject sets are sorted (e.g. hashed and ordered) so `A↔B` is structurally identical to `B↔A`.
**Q6. Who defines claim symmetry?** The `ClaimDescriptor`.
**Q7. Can pair and group assertions be combined directly?** No.
**Q8. What is a projection rule?** A domain rule that defines how a pairwise magnitude (e.g. P1↔G1) translates into a group-level magnitude (P1↔{G1,G2}).
**Q9. Are projection rules part of the kernel?** No. They belong to Stage 8J Fusion.

## Claims
**Q10. Does Claim Model B survive?** No. It is upgraded to Claim Model B3.
**Q11. Is a ClaimDescriptor required?** Yes.
**Q12. What metadata belongs in the descriptor?** `claim_id`, `semantic_version`, `is_symmetric`, `allowed_scope_kinds`, `magnitude_contract`.
**Q13. Can plugins define claims?** Yes, by defining a new `ClaimDescriptor`.
**Q14. Can unknown claims be serialized?** Yes.
**Q15. Can unknown claims be fused?** No.
**Q16. How are claim semantic changes versioned?** Via the `semantic_version` in the descriptor.

## Observations
**Q17. Does ReconGraph require observation identity?** Yes.
**Q18. Which observation identity model is selected?** OI-D (Structural Observation ID).
**Q19. Does identity refer to a field slot or value occurrence?** A field slot.
**Q20. How are revisions represented?** The slot ID remains the same, but the payload value changes (and the derivation metadata logs the new engine state/time).
**Q21. Are IDs random?** No.
**Q22. Are raw values included in IDs?** No.
**Q23. Can multiple assertions derive from one observation?** Yes.
**Q24. Can one assertion derive from multiple observations?** Yes (e.g. `amount_conservation`).

## Derivation
**Q25. What derivation metadata is required?** `provider_id`, `provider_semantic_version`, `policy_hash`.
**Q26. What does provider semantic version mean?** The version of the epistemic interpretation logic.
**Q27. What does policy hash mean?** The configuration threshold state during execution.
**Q28. What does engine version mean?** The core ReconGraph framework version.
**Q29. Which one explains algorithm behavior?** `provider_semantic_version` + `policy_hash`.
**Q30. What is the v0.1 reproducibility guarantee?** Replay A (Historical Explanation) and Replay C (Counterfactual Re-evaluation).

## Duplicate Evidence
**Q31. What is an exact duplicate assertion?** Same assertion fields derived from the exact same process.
**Q32. What is derived dependence?** Two different assertions derived from the same raw field (e.g., Lexical Match and Legal Form match from one string).
**Q33. What metadata exposes shared derivation context?** `ObservationIdentity` and `StructuredSourceLineage`.
**Q34. Does the kernel deduplicate?** No. It only prevents instantiation of exact duplicates (value equality).
**Q35. Does Stage 8J deduplicate?** It must apply rules to avoid double-counting dependent assertions.
**Q36. What must happen before fusion?** Projection to common scopes and detection of shared derivation contexts.

## Assertion Identity
**Q37. Does an assertion have assertion_id?** No.
**Q38. Does it have semantic_key?** No.
**Q39. What fields define semantic identity?** The entire value-object structure (dataclass `__eq__`).
**Q40. Do magnitudes participate?** Yes.
**Q41. Does explanatory text participate?** No. It is explicitly forbidden from the assertion core.
**Q42. How are sensitive raw values excluded?** By referencing them only via structural `ObservationIdentity` and `Lineage`, not by storing the raw strings in the core identifier.

## State
**Q43. Is one EvidenceState sufficient?** No.
**Q44. Are ObservationState and InterpretationState separate?** Yes.
**Q45. What are their exact allowed values?** Obs: `PRESENT`, `MISSING`, `INVALID`. Int: `INTERPRETED`, `UNINTERPRETABLE`.
**Q46. Can PRESENT + UNINTERPRETABLE coexist?** Yes (e.g. unknown language).
**Q47. Can INVALID + INTERPRETED coexist?** Yes.
**Q48. Under what claim, if any?** E.g. `document.contains_invalid_tax_identifier`.
**Q49. Can PARTIALLY_INTERPRETED exist?** No.
**Q50. Is partial interpretation better represented by multiple assertions?** Yes.

## Authority / Quality
**Q51. Does AuthorityDescriptor survive?** No.
**Q52. What is it renamed to, if anything?** `EvidenceQualityContext`.
**Q53. Which quality properties belong to observations?** Source Trust, Extraction Trust.
**Q54. Which belong to assertions?** Verification Trust, Temporal Validity.
**Q55. Does quality alter magnitude?** No.
**Q56. Can interpreter confidence exist?** Yes, in the typed payload.
**Q57. How is it different from support magnitude?** Confidence is certainty of observation. Support is certainty of the mathematical proposition assuming the observation is true.

## Magnitudes
**Q58. Is there a universal magnitude scale?** No.
**Q59. Which magnitude model is selected?** MM-C (Claim-Local Magnitude Contract).
**Q60. Can Stage 8J compare magnitudes across claims?** No, not without a formal calibration rule.
**Q61. Can Stage 8J compare magnitudes across providers?** Only if they target the same Claim and adhere to its magnitude contract.
**Q62. What is a magnitude contract?** A definition of what 0.0 and 1.0 mean for a specific claim.
**Q63. Does Reference Evidence require one?** Yes (`rarity_v1`).
**Q64. Does Financial Evidence require one?** Yes (`conservation_v1`).
**Q65. Are binary magnitudes valid?** Yes.
**Q66. What is Stage 8J forbidden from doing before calibration?** Naively summing uncalibrated magnitudes as if they were probabilities.

## Payload / Provenance
**Q67. What belongs in typed payload?** Normalized data, tokens, interpreter confidence.
**Q68. What belongs in lineage?** `source_system`, `source_record_id`.
**Q69. What belongs in derivation metadata?** `provider_version`, `policy_hash`.
**Q70. What belongs in epistemic/quality context?** Source trust, extraction reliability.
**Q71. Does explanation text belong in assertions?** Absolutely not.
**Q72. Where does statistics_available belong?** Typed Payload.
**Q73. Where does corpus frequency belong?** Typed Payload.
**Q74. Where does OCR confidence belong?** Typed Payload.

## Trace
**Q75. Which replay modes does v0.1 support?** A (Explanation) and C (Counterfactual).
**Q76. Are assertions serialized in traces?** Yes.
**Q77. Are observations serialized?** Yes.
**Q78. What happens to unknown payload versions?** Preserved as JSON dicts.
**Q79. What happens to unknown claims?** Preserved structurally.
**Q80. Can a trace remain explainable without re-executing historical provider code?** Yes.

## Kernel
**Q81. Is Kernel D still selected?** Yes, upgraded with scopes and descriptors.
**Q82. Provide the exact conceptual object graph.** (See Part Q below).
**Q83. What object owns claim?** `EvidenceAssertion`.
**Q84. What object owns scope?** `EvidenceAssertion`.
**Q85. What object owns observation identity?** `EvidenceAssertion`.
**Q86. What object owns derivation metadata?** `EvidenceAssertion`.
**Q87. What object owns quality context?** `EvidenceAssertion`.
**Q88. What object owns typed payload?** `EvidenceAssertion`.
**Q89. What is EvidenceAssertion responsible for?** Representing an immutable, typed epistemic proposition.
**Q90. What is EvidenceAssertion explicitly forbidden from doing?** Fusion, decision making, holding human text.

## Vendor Stage 8C
**Q91. What exact claims will Vendor Identity v0.1 emit?** `SAME_LEGAL_ENTITY`, `SAME_GST_REGISTRATION`.
**Q92. Is lexical name identity a separate claim?** It may be (e.g. `SAME_LEXICAL_CORE`), pending final domain rules.
**Q93. Is same legal entity emitted without PAN-level evidence?** No. Name-only matches yield `SAME_LEXICAL_NAME`, not `SAME_LEGAL_ENTITY`.
**Q94. Is same GST registration emitted without full valid GSTIN evidence?** No.
**Q95. Can vendor name evidence directly conflict with same GST registration?** No, orthogonal axes.
**Q96. Can legal-form conflict directly contradict same legal entity?** Yes, if temporal knowledge proves no conversion occurred.
**Q97. Which claims are structural heuristics?** Name, Legal Form.
**Q98. Which claims require authoritative identifiers?** Legal Entity (PAN), GST Registration (GSTIN).
**Q99. Which Vendor evidence units remain deferred?** Rarity/corpus profiling, alias resolution, ML models.
**Q100. Is ReconGraph finally ready to implement the minimal semantic kernel?** YES.

---

## Part Q — Conceptual Object Graph

```text
Source Record
    │
    ▼ [derives from]
Observation
├── ObservationIdentity (owns: system, record_id, slot_id)
├── ObservationState (owns: PRESENT, MISSING, INVALID)
├── Lineage (owns: factual source provenance)
└── Raw / Extracted Value (owns: strings, numbers)
    │
    ▼ [interpreted by]
Evidence Provider / Interpreter
├── ProviderIdentity
├── ProviderSemanticVersion
└── PolicyHash
    │
    ▼ [constructs]
EvidenceAssertion
├── ClaimDescriptor (references: claim_id, symmetry rules, magnitude contract)
├── EvidenceScope (owns: left subjects, right subjects, canonicalization logic)
├── SupportMagnitude (owns: float)
├── ConflictMagnitude (owns: float)
├── InterpretationState (owns: INTERPRETED, UNINTERPRETABLE)
├── EvidenceQualityContext (owns: trust layers)
├── ObservationIdentity (references)
├── DerivationMetadata (owns: provider info, policy hash)
└── TypedPayload (owns: specific data structures, tags)
    │
    ▼ [serializes]
Trace
├── preserves assertion core
├── preserves semantic versions
└── tolerates unknown payloads
    │
    ▼ [consumed by]
Stage 8J Fusion
[NOT IMPLEMENTED]
```
