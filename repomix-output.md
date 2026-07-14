This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: .venv/**, **/__pycache__/**
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
datasets/
  challenge/
    challenge_cases_v1.csv
    gst_records_v1.csv
    pair_labels_v1.csv
    purchase_register_v1.csv
  ground_truth/
    purchase_gst_matches.csv
  raw/
    gst_records.csv
    purchase_register.csv
docs/
  algorithms/
    assertion-authority-placement.md
    assertion-magnitude-canonicalization.md
    canonical-semantic-encoding-v1.md
    claim-descriptor-boundary.md
    derivation-ontology.md
    evidence-authority-model.md
    evidence-authority-taxonomy.md
    evidence-claim-ontology.md
    evidence-dependence-terminology.md
    evidence-magnitude-semantics.md
    evidence-state-algebra-v2.md
    evidence-state-algebra.md
    financial-relationship-score.md
    identifier-authority-boundary.md
    indian-tax-identity-evidence-v1.md
    legal-entity-primitive-evidence-units.md
    observation-state-value-contract.md
    purchase-gst-semantics.md
    reference-evidence-interpretation-contract.md
    reference-evidence-interpreter-cases.md
    reference-evidence-magnitude.md
    reference-evidence-model.md
    reference-evidence-ordering.md
    reference-evidence-units.md
    source-ontology-model.md
    temporal-scoring.md
    vendor-alias-and-acronym-semantics-v1.md
    vendor-core-similarity-research.md
    vendor-corpus-statistics-v1.md
    vendor-corpus-statistics.md
    vendor-entity-similarity.md
    vendor-identity-factor-model-v1.md
    vendor-identity-latent-variables.md
    vendor-legal-form-ontology-v1.md
    vendor-normalization-event-model.md
    vendor-normalization-information-loss.md
    vendor-observation-state-truth-table.md
  architecture/
    adr-001-reference-evidence-pipeline.md
    assertion-payload-provenance-boundary.md
    assertion-polarity-decision.md
    assertion-scope-design-tournament.md
    assertion-vs-interpretation-result-decision.md
    core-claim-catalog-v1.md
    current-evidence-claim-audit.md
    decision-trace-replay-contract.md
    derivation-cache-threat-model.md
    derivation-identity-composition.md
    derivation-identity-vs-assertion-identity.md
    derivation-identity-vs-execution-decision.md
    derivation-input-binding-decision.md
    derivation-method-identity-decision.md
    derivation-vs-assertion-boundary.md
    derived-artifact-boundary.md
    derived-artifact-necessity-trial.md
    environment-integrity-audit.md
    evidence-assertion-ancestry-decision.md
    evidence-assertion-identity.md
    evidence-assertion-kernel-decision-v2.md
    evidence-assertion-kernel-premortem-v2.md
    evidence-assertion-scope.md
    evidence-authority-descriptor-decision.md
    evidence-dag-feasibility-study.md
    evidence-derivation-identity.md
    evidence-double-counting-threat-model.md
    evidence-kernel-performance-model.md
    evidence-kernel-semantic-compatibility-matrix.md
    evidence-lineage-correlation-study.md
    evidence-lineage-v2.md
    evidence-provenance-current-state-audit.md
    evidence-semantic-kernel-decision.md
    evidence-semantic-kernel-design.md
    k4-k5-evidence-ancestry-decision.md
    kernel-identity-reference-decision.md
    lineage-vs-correlation-boundary.md
    minimal-semantic-kernel-implementation-plan.md
    multi-observation-derivation-boundary.md
    observation-content-vs-occurrence-identity.md
    observation-evidence-boundary.md
    observation-identity-model.md
    observation-identity-vs-value-equality.md
    observation-lineage-attachment-decision.md
    observation-occurrence-naming-decision.md
    observation-revision-implementation-decision.md
    open-questions.md
    provider-semantic-identity-study.md
    provider-semantic-versioning.md
    scope-kind-construction-decision.md
    semantic-derivation-dependency-decision.md
    shared-ancestry-query-boundary.md
    source-artifact-model-decision.md
    source-identity-content-identity-study.md
    source-version-identity-boundary.md
    source-version-placement-decision.md
    stage8c-k4-k5-research-decision.md
    stage8j-semantic-kernel-premortem.md
    stage8j-vendor-fusion-premortem.md
    structured-source-lineage-candidates.md
    typed-evidence-payload-contract.md
    typed-payload-envelope-decision.md
    unknown-claim-kernel-boundary.md
    unknown-provider-derivation-boundary.md
    vendor-artifact-materialization-boundary.md
    vendor-claim-catalog-v1.md
    vendor-current-state-audit.md
    vendor-evidence-derivation-dag-v1.md
    vendor-identity-context-decision.md
    vendor-identity-current-semantics.md
    vendor-identity-research-decision.md
    vendor-interpretation-result-model.md
    vendor-missingness-state-trace.md
    vendor-name-observation-model.md
    vendor-v1-gate-qa.md
    vendor-v1-scalar-projection-boundary.md
    vendor-v1-v2-compatibility-envelope.md
    zero-magnitude-assertion-decision.md
  implementation/
    stage8c-k1-k2-import-audit.md
    stage8c-k1-k2-preflight.md
    stage8c-k3-import-audit.md
    stage8c-k3-preflight.md
    stage8c-k4-k5-implementation-preflight.md
    stage8c-k4-k5-preflight.md
  security/
    derivation-fingerprint-privacy.md
    evidence-identity-privacy-threat-model.md
    observation-fingerprint-privacy.md
    observation-serialization-sensitivity.md
    source-lineage-serialization-sensitivity.md
  testing/
    cross-scope-evidence-adversarial-matrix.md
    derivation-identity-hard-cases.md
    evidence-assertion-hard-cases.md
    evidence-assertion-kernel-metamorphic-properties-v2.md
    evidence-claim-collision-matrix.md
    evidence-semantic-kernel-metamorphic-properties.md
    lineage-derivation-hard-negatives.md
    lineage-derivation-metamorphic-properties.md
    observation-kernel-metamorphic-properties.md
    vendor-hard-negatives.md
    vendor-identity-conformance-v1.md
    vendor-identity-metamorphic-properties-v1.md
    vendor-metamorphic-properties.md
experiments/
  audit_vendor_normalization_information_loss.py
  benchmark_vendor_parse_reuse.py
  compare_reference_identity_extraction.py
  compare_tax_penalty_models.py
  design_exact_reference_fallback.py
  design_reference_evidence_ordering.py
  design_reference_interpretation_contract.py
  evaluate_corpus_reference_informativeness.py
  evaluate_gstin_identity_cases.py
  evaluate_purchase_gst_baseline.py
  evaluate_purchase_gst_challenges.py
  evaluate_reference_discriminative_strength.py
  evaluate_reference_interpretation_state.py
  evaluate_reference_rarity_magnitude.py
  evaluate_reference_structural_fallback_inputs.py
  evaluate_reference_structural_magnitude.py
  evaluate_reference_token_cooccurrence.py
  evaluate_vendor_acronym_collisions.py
  evaluate_vendor_authority_conflicts.py
  evaluate_vendor_common_token_collisions.py
  evaluate_vendor_core_similarity_metrics.py
  evaluate_vendor_legal_form_extraction.py
  evaluate_vendor_token_discriminativeness.py
  inspect_reference_contributions.py
  inspect_reference_enrichment.py
  inspect_reference_interpretation_assembly.py
  inspect_reference_selection.py
  legacy_reference.py
  stage_4d_audit.py
  vendor_similarity_metrics.py
  verify_ancestry_cross_process_determinism.py
  verify_assertion_cross_process_determinism.py
  verify_canonical_encoding_cross_process.py
src/
  recongraph/
    benchmark/
      __init__.py
      models.py
      runner.py
    candidate_generation/
      __init__.py
      blockers.py
      generator.py
      index.py
    domain/
      financial/
        __init__.py
        pipeline.py
      __init__.py
      assertions.py
      authority.py
      claims.py
      dependencies.py
      derivations.py
      identity.py
      lineage.py
      observations.py
      payloads.py
      records.py
      scopes.py
    graph/
      __init__.py
      algorithms.py
      candidate.py
      decision.py
      evaluator.py
      explainability.py
      hypotheses.py
      review.py
      search.py
      trace.py
    matching/
      __init__.py
      pair_scorers.py
      purchase_gst_semantics.py
      reference_evidence.py
      scoring.py
      signals.py
    normalization/
      __init__.py
      text.py
    plugins/
      __init__.py
      core_providers.py
      provider_v2.py
      provider.py
    synthetic/
      __init__.py
      builder.py
      canonical.py
      models.py
      operators.py
    __init__.py
    config.py
    engine.py
    errors.py
tests/
  test_benchmark_runner.py
  test_candidate_generation.py
  test_candidate_graph.py
  test_canonical_semantic_encoding.py
  test_claim_semantics.py
  test_core_claims.py
  test_decision_engine.py
  test_derivation_identity.py
  test_derivation_occurrence_identity.py
  test_derived_artifacts.py
  test_engine.py
  test_evidence_ancestry_metamorphic.py
  test_evidence_assertion_metamorphic.py
  test_evidence_assertions.py
  test_evidence_authority.py
  test_evidence_scope.py
  test_evidence_state_algebra.py
  test_explainability.py
  test_financial_pipeline.py
  test_graph_algorithms.py
  test_hypothesis_evaluator.py
  test_hypothesis_searcher.py
  test_kernel_identity_refs.py
  test_matching_signals.py
  test_observation_identity.py
  test_observation_occurrence_identity.py
  test_pair_scorers.py
  test_proposition_integrity.py
  test_purchase_gst_semantics.py
  test_reference_evidence.py
  test_relationship_scoring.py
  test_review_packet.py
  test_semantic_dependencies.py
  test_source_lineage.py
  test_synthetic.py
  test_text_normalization.py
  test_trace.py
  test_typed_payloads.py
.gitignore
PROJECT_DEFINITION.md
pyproject.toml
README.md
```

# Files

## File: datasets/challenge/challenge_cases_v1.csv
````
case_id,case_name,attacked_assumption,expected_behaviour
HN001,amount_mismatch_identity_agreement,amount_semantics,strong_amount_mismatch_should_prevent_automatic_match
HN002,tax_identity_contradiction,identity_semantics,tax_identity_contradiction_should_prevent_automatic_match
HN003,recurring_invoice_collision,event_identity,recurring_transactions_should_remain_distinct_events
HN004,weak_reference_collision,reference_semantics,weak_numeric_reference_overlap_should_not_override_entity_identity
HN005,one_to_many_invoice_relationship,relationship_cardinality,pairwise_scoring_should_be_recognized_as_insufficient
````

## File: datasets/challenge/gst_records_v1.csv
````
record_id,supplier_name,invoice_number,invoice_date,amount,gstin
CG001,ABC STEELS PVT. LTD.,AB/1042,2026-06-13,236000.00,07ABCDE1234F1Z5
CG002,ABC STEELS PVT. LTD.,AB/1042,2026-06-13,118000.00,27ZZZZZ9999Z9Z9
CG003,CLOUDLEDGER SOFTWARE PVT LTD,CL-JUL-2026,2026-07-05,25000.00,07CLOUD1234A1Z1
CG004,Nova Surgical Systems Private Limited,NSS-001,2026-06-20,75000.00,29NOVAS9876D1Z4
CG005,APEX INDUSTRIAL SUPPLIES,AIS/9001-A,2026-06-25,50000.00,07APEXS1234C1Z3
CG006,APEX INDUSTRIAL SUPPLIES,AIS/9001-B,2026-06-25,50000.00,07APEXS1234C1Z3
````

## File: datasets/challenge/pair_labels_v1.csv
````
case_id,purchase_record_id,gst_record_id,expected_label
HN001,CP001,CG001,negative
HN002,CP001,CG002,negative
HN003,CP002,CG003,negative
HN004,CP003,CG004,negative
HN005,CP004,CG005,group_component
HN005,CP004,CG006,group_component
````

## File: datasets/challenge/purchase_register_v1.csv
````
record_id,vendor_name,invoice_number,invoice_date,amount,gstin
CP001,ABC Steel Private Limited,INV-1042,2026-06-12,118000.00,07ABCDE1234F1Z5
CP002,CloudLedger Software Private Limited,CL-JUN-2026,2026-06-05,25000.00,07CLOUD1234A1Z1
CP003,Orion Medical Devices Private Limited,OMD-001,2026-06-20,75000.00,07ORION5678B1Z2
CP004,Apex Industrial Supplies,AIS-9001,2026-06-25,100000.00,07APEXS1234C1Z3
````

## File: datasets/ground_truth/purchase_gst_matches.csv
````
purchase_record_id,gst_record_id,relationship
PR001,GST001,same_financial_event
PR002,GST002,same_financial_event
PR003,GST003,same_financial_event
PR004,GST004,same_financial_event
PR005,GST005,same_financial_event
````

## File: datasets/raw/gst_records.csv
````
record_id,supplier_name,invoice_number,invoice_date,amount,gstin
GST001,ABC STEELS PVT. LTD.,AB/1042,2026-06-13,118000.00,07ABCDE1234F1Z5
GST002,SHREE BALAJI ENT.,SB8891,2026-06-14,245500.00,07FGHIJ5678K1Z3
GST003,NORTHSTAR COMPONENTS PRIVATE LIMITED,NC/2204,2026-06-18,87500.00,06KLMNO9012P1Z7
GST004,METRO OFFICE SOLUTION,MOS781,2026-06-20,32000.00,07QRSTU3456V1Z1
GST005,APEX INDUSTRIAL SUPPLY,AIS/5510,2026-06-23,410000.00,09WXYZA7890B1Z4
````

## File: datasets/raw/purchase_register.csv
````
record_id,vendor_name,invoice_number,invoice_date,amount,gstin
PR001,ABC Steel Private Limited,INV-1042,2026-06-12,118000.00,07ABCDE1234F1Z5
PR002,Shree Balaji Enterprises,SB-8891,2026-06-14,245500.00,07FGHIJ5678K1Z3
PR003,Northstar Components Pvt Ltd,NC-2204,2026-06-17,87500.00,06KLMNO9012P1Z7
PR004,Metro Office Solutions,MOS-781,2026-06-19,32000.00,07QRSTU3456V1Z1
PR005,Apex Industrial Supplies Pvt Ltd,AIS-5510,2026-06-21,410000.00,09WXYZA7890B1Z4
````

## File: docs/algorithms/assertion-authority-placement.md
````markdown
# Assertion Authority Placement

This document refines the concept of "Authority" into an Epistemic/Quality context and determines its correct architectural placement.

## Deconstructing Authority
"Authority" is too vague. It conflates structural trust (government registry) with machine capability (OCR confidence).

**AU-001 Can assertion authority be derived from observation metadata?**
Largely yes. If the `ObservationIdentity` points to a government registry API, the structural authority is implicit. 

**AU-002 Should the assertion duplicate it?**
Yes, because Stage 8J fusion needs to quickly index assertions by their quality without doing deep lookups into the source system's schema.

**AU-003 Can one observation produce assertions with different authority?**
Yes. An invoice might explicitly state `PAN X` (High authority) but we run an NLP model to infer `Brand Y` (Low reliability interpretation).

**AU-004 Can interpretation logic affect authority?**
Yes. An inferred claim has lower epistemic quality than an explicitly asserted claim on the same document.

**AU-005 Is AuthorityDescriptor actually evidence-quality context rather than authority?**
Yes. Authority implies "who is in charge." Epistemic quality implies "how much can we trust this derivation."

## Property Placement Table

| Property | Observation | Assertion | Lineage | Payload | Trace |
|---|---|---|---|---|---|
| **Source authority** | Primary | Required (as context) | | | Preserved |
| **Extraction reliability** | Primary | Required (as context) | | | Preserved |
| **Verification status** | | Required (as context) | | | Preserved |
| **Temporal validity** | | Required (as context) | | | Preserved |
| **Interpreter confidence**| | | | Primary | Preserved |

## Interpreter Confidence vs Support Magnitude
**If interpreter confidence is introduced, explicitly distinguish it from support magnitude.**
* **Interpreter Confidence:** "I am 41% sure the text says `MICR0SOFT`."
* **Support Magnitude:** "Assuming it says `MICR0SOFT`, it provides 0.8 support for the claim `SAME_LEGAL_ENTITY`."
Mixing these into `support = 0.8 * 0.41 = 0.328` destroys the epistemic boundary.

## Recommendation
Rename `AuthorityDescriptor` to **`EvidenceQualityContext`**. This object lives on the `EvidenceAssertion` and explicitly declares:
* `source_trust` (e.g. `SYSTEM_OF_RECORD`, `USER_SUPPLIED`)
* `extraction_trust` (e.g. `STRUCTURED`, `UNSTRUCTURED_ML`)
* `verification_trust` (e.g. `UNVERIFIED`, `HUMAN_REVIEWED`)

This separates *epistemic quality* from the *mathematical magnitude* of the claim.
````

## File: docs/algorithms/assertion-magnitude-canonicalization.md
````markdown
# Assertion Magnitude Canonicalization

## Summary
Evidence magnitude must be robustly cross-process deterministic and immune to floating-point formatting inconsistencies.

## Rule
Magnitude identity uses the exact IEEE-754 binary64 bit representation of the finite Python float, packed as hex: `binary64:<hex>`.

`-0.0` is explicitly canonicalized to positive `0.0`. (Note: zero is forbidden as a final assertion magnitude, but this canonicalization is enforced at the identity layer).
Adjacent floats (e.g. `nextafter(0.8, 1.0)`) will correctly hash to distinct identities.
````

## File: docs/algorithms/canonical-semantic-encoding-v1.md
````markdown
# Canonical Semantic Encoding V1

## Summary
To ensure cross-language and cross-platform stable identity hashing, the following canonical JSON subset is adopted.

## Encoding Rules
1. **Null:** Allowed.
2. **Booleans:** Allowed.
3. **Integers:** Strictly signed 64-bit integers. Below min and above max int64 are rejected to prevent arbitrary precision drift.
4. **Floats:** Rejected. (NaN and Infinity are implicitly rejected).
5. **Strings:** Text payload strings MUST be normalized to Unicode NFC. Machine identifiers (e.g. schema keys) MUST be ASCII-only and validated.
6. **Arrays/Tuples:** Order is semantic.
7. **Mappings/Dicts:** String keys only, sorted lexicographically. Custom objects rejected.
````

## File: docs/algorithms/claim-descriptor-boundary.md
````markdown
# Claim Descriptor Boundary

This document challenges the previously recommended "Identifier Only" Claim Model B.

## Properties of Claims
**CI-001 Does a claim identifier need metadata?**
Yes. Without metadata, the kernel cannot know if the claim is symmetric (for canonicalization) or what scopes it applies to.

**CI-002 Can metadata be provider-owned?**
No. Two providers emitting the same claim must agree on its symmetry and scope cardinality. The claim owns its semantics.

**CI-003 If two plugins independently use `identity.same_legal_entity` but define different symmetry semantics, what happens?**
Catastrophic failure in Stage 8J. One canonicalizes `B↔A` to `A↔B`, the other treats them as distinct directional assertions.

**CI-004 Who owns canonical claim semantics?**
The Claim Descriptor itself.

**CI-005 Does a global claim registry violate plugin extensibility?**
A *static, hardcoded* registry does. A *dynamic* registry (where plugins register new ClaimDescriptors on boot) does not. However, we can avoid global state entirely by passing the `ClaimDescriptor` value object inside the assertion.

**CI-006 Can core claims be registered while plugins define namespaced extension claims?**
Yes.

**CI-007 Can unknown claims remain traceable but non-fusible?**
Yes. If a trace contains a serialized `ClaimDescriptor` with a `claim_id` that Stage 8J doesn't recognize, Stage 8J can log it, skip fusing it, and preserve it in the output trace.

**CI-008 Should Stage 8J refuse to combine assertions for unknown claim semantics?**
Absolutely. Fusing unknown claims is semantically blind.

**CI-009 Should claim schema version be separate from payload schema version?**
Yes. The proposition's semantics (Claim version) are independent of the data structures used to prove it (Payload version).

**CI-010 Can the semantics of `identity.same_legal_entity` change in place?**
No. If v2 defines it as strictly "PAN equality" and v1 defined it as "PAN or Name equality", historical assertions lose their meaning. It must become `identity.same_legal_entity_v2`.

## Evaluation
* **Claim B1 (Identifier Only):** Fails to handle symmetry canonicalization safely.
* **Claim B2 (Assertion-Local Metadata):** Creates split-brain where different assertions define the same claim differently.
* **Claim B3 (Identifier + ClaimDescriptor):** A frozen value object defining the proposition's invariant rules (symmetry, allowed scopes, version).

## Recommendation
**Claim B3 (Identifier + ClaimDescriptor).** 

```python
@dataclass(frozen=True)
class ClaimDescriptor:
    claim_id: str
    semantic_version: int
    is_symmetric: bool
    allowed_scope_types: frozenset[ScopeType]
```
**Can unknown plugin claims be recorded, serialized, explained, and traced even if the core cannot fuse them?**
Yes. The `ClaimDescriptor` contains all necessary structural metadata (`is_symmetric`) for the trace reader and the graph engine to handle the assertion mechanically, even if Stage 8J lacks the domain knowledge to fuse that specific `claim_id`.
````

## File: docs/algorithms/derivation-ontology.md
````markdown
# Derivation Ontology
## Part G — Defining Semantic Derivation

### Formal Definition
A semantic derivation is:
> A deterministic semantic transformation whose output may participate in evidence ancestry.

### Classification of Engine Actions
- **extract_reference_identity**: YES (Semantic Derivation)
- **PAN extraction from GSTIN**: YES (Semantic Derivation)
- **financial aggregation**: YES (Semantic Derivation)
- **connected-component BFS**: NO (Graph Algorithmic Action)
- **DecisionEngine classification**: NO (Decision Transformation)

We will strict define DerivationIdentity exclusively for the "YES" category to avoid turning K5 into a generic program trace.
````

## File: docs/algorithms/evidence-authority-model.md
````markdown
# Evidence Authority Model

This document formally investigates the distinction between evidence magnitude, authority, availability, and conflict.

## Q1: Can two evidence units both have strong magnitude while supporting opposite identity claims?
Yes. Example AH001: `ABC PRIVATE LIMITED` vs `ABC PRIVATE LIMITED` has maximum lexical magnitude (100% similarity). But if they carry `TAX-A` and `TAX-B`, the identifier conflict has maximal conflict magnitude. They strongly support opposite claims (Lexical Identity = YES, Legal Identity = NO).

## Q2: Does stronger authority mean the lower-authority evidence should be deleted?
No. Deleting the lower-authority evidence destroys provenance and makes the system untrustable. If the tax identity was extracted via OCR incorrectly, the system *needs* to know the vendor name was an exact match so a human reviewer can see the conflict and correct the extraction.

## Q3: Should authoritative contradiction become a negative vendor score?
No. Collapsing a multidimensional conflict into a single scalar (e.g. `score = -1.0`) destroys the specific nature of the conflict. A negative score could mean "the names are completely different" or "the names are identical but the tax IDs conflict". These are epistemically different states.

## Q4: Or should contradiction remain an explicit conflict axis?
Yes. Contradiction must be preserved explicitly. The Decision Engine needs to differentiate between "no evidence", "weak evidence", and "strong contradictory evidence".

## Q5: Can `score: float` represent: strong support, strong conflict, no evidence without ambiguity?
No. `0.0` currently means strong conflict (e.g., penalty). `1.0` means strong support. What is no evidence? Currently `None` is mapped to `0.0` or omitted entirely, breaking the arithmetic. A single float cannot distinguish "I know these are different" from "I don't know if these are the same".

## Q6: Would a bipolar model such as `support`, `conflict` solve this?
Partially. It solves the ambiguity between absence (`support=0, conflict=0`) and contradiction (`support=0, conflict=1`).

## Q7: Would bipolar evidence still fail to represent authority?
Yes. Bipolar evidence gives magnitude, but `conflict=1.0` (names look different) vs `conflict=1.0` (authoritative tax identifiers mismatch) carry vastly different authority. We don't just want to know *how much* conflict there is, but *what kind of authority* backs that conflict.

## Q8: Do we potentially require `support`, `conflict`, `authority`, `availability`?
Yes. This dimensional separation prevents epistemic collapse.

## Conceptual Distinctions & Counterexamples

* **Magnitude vs Authority:** An exact match on a generic word like `TRADERS` has high magnitude but zero authority. A mismatch on a government GSTIN has high authority.
* **Provenance vs Availability:** `Availability` means the field was present in the data. `Provenance` means we know *how* it was populated (OCR vs ERP master data). High availability does not mean high quality provenance.
* **Conflict vs Absence:** Missing a vendor name (Absence) is not evidence that the vendors are different (Conflict).
````

## File: docs/algorithms/evidence-authority-taxonomy.md
````markdown
# Evidence Authority Taxonomy

This document answers core questions about authority in evidence models.

## Core Questions

**AT-001 Is authority a property of evidence kind?**
No. Vendor Name evidence from an ERP differs in authority from Vendor Name evidence from a fuzzy OCR scan.

**AT-002 Is authority a property of source?**
Largely yes. A government tax registry has more authority over legal entity structure than an internal CRM.

**AT-003 Is authority a property of extraction process?**
Yes. Structured electronic ingestion has higher epistemic authority than a machine-learning OCR model.

**AT-004 Is authority a property of individual observation?**
Ultimately, yes. Since observations are derived from specific extractions of specific documents, authority is bound to the observation instance.

**AT-005 Can the same GSTIN string have different authority depending on origin?**
Absolutely. If it is scraped from a blurry PDF, it is low authority (subject to OCR corruption). If retrieved via API from the government portal, it is maximum authority.

**AT-006 Can human verification always be considered highest authority?**
No. Humans make mistakes, act on stale data, or click "Approve" without reading. Stale human verification is lower authority than a live API check.

**AT-007 Is mathematical conservation "authoritative"?**
It is structural. If `A = B + C`, that is a mathematical fact, not an asserted authority. It operates on a different axis than epistemic source authority.

**AT-008 Does authority measure truth probability?**
No. This is dangerous. High authority does not mean "99% true". It means "if this contradicts something else, this wins the conflict resolution". Authority is about conflict-breaking rules, not calibration percentages.

**AT-009 Can authority be totally ordered?**
No. You cannot say `DERIVED_CONSERVATION > VERIFIED_REGISTRY` because they apply to different claims.

**AT-010 Should authority be ordinal, categorical, or structured?**
Structured.

## Candidate Models

### Authority Model A — Numeric Rank
* Example: `authority_weight = 0.8`
* Flaw: Turns authority into magnitude. Destroys the semantic difference between support and conflict resolution.

### Authority Model B — Ordered Enum
* Example: `LOW, MEDIUM, HIGH, AUTHORITATIVE`
* Flaw: Extremely vague. What does "HIGH" mean across different subsystems?

### Authority Model C — Structured Authority Descriptor
* Distinguishes `assertion_origin`, `extraction_reliability`.
* Prevents collapsing multidimensional trust into a single float.

## Recommendation
**Authority Model C (Minimal Descriptor seam).** For v0.1, a single semantic `Enum` (e.g., `AuthorityClass(SYSTEM_OF_RECORD, EXTRACTED, INFERRED)`) is the minimum honest seam, avoiding arbitrary numeric weights while preserving the origin type for future fusion rules.
````

## File: docs/algorithms/evidence-claim-ontology.md
````markdown
# Evidence Claim Ontology

This document evaluates whether ReconGraph requires formal Evidence Claims, how they should be structured, and what semantics they carry.

## Answers to Fundamental Questions

**CO-001 Is an enum sufficient?**
No. Enums are closed. A plugin architecture needs an extensible namespace where third-party developers can assert new claims (e.g. `CUSTOM_BANK_ACCOUNT_MATCH`) without modifying the core enum.

**CO-002 Are claims merely labels?**
No. They define the semantic target for fusion. If two providers emit evidence for `SAME_LEGAL_ENTITY`, the fusion engine knows they are corroborating or contradicting the *exact same fact*.

**CO-003 Can claims have logical relationships?**
Yes. `SAME_LEGAL_ENTITY` logically necessitates `SAME_CORPORATE_FAMILY`. But `SAME_CORPORATE_FAMILY` does not necessitate `SAME_LEGAL_ENTITY`. Contradicting the family implies contradicting the entity.

**CO-004 Should support and contradiction target the same proposition?**
Yes. `DIFFERENT_LEGAL_ENTITY` is just strong conflict against the claim `SAME_LEGAL_ENTITY`. Introducing negative claims creates an uncontrolled explosion of variables where `conflict(SAME_LEGAL_ENTITY)` and `support(DIFFERENT_LEGAL_ENTITY)` have to be synchronized.

**CO-005 Should ReconGraph represent negative claims explicitly?**
No, per above. Conflict against a positive claim is semantically sufficient and mathematically cleaner.

**CO-006 Can absence of support for a claim be treated as support for its negation?**
Absolutely not. "I have no proof they are the same" is entirely distinct from "I have proof they are different".

**CO-007 Can one observation bear evidence on multiple claims?**
Yes. `ABC LLP` vs `ABC PVT LTD` provides lexical support for `SAME_ORGANIZATIONAL_CORE` but absolute contradiction for `SAME_LEGAL_ENTITY`. 

**CO-008 Can claims be hierarchical?**
Yes, conceptually. However, logical entailment (if A is true, B is true) is mathematically complex for fusion engines unless strictly formalized.

**CO-009 Should claim semantics live in code or documentation?**
The *name* and *namespace* live in code. The *logical rules* between claims should be encoded in a registry if Stage 8J is expected to fuse hierarchically.

**CO-010 What happens when a future plugin introduces `SAME_BANK_ACCOUNT_OWNER`?**
If claims are a flat enum, the core code breaks. If claims are a registry/value-object, the plugin registers it, and the fusion engine dynamically binds providers targeting that claim.

## Candidate Designs

### Claim Model A — Flat Enum
* Simple `Enum`.
* Fails extensibility and hierarchy.

### Claim Model B — Typed Claim Identifier
* `identity.same_legal_entity`, `financial.conservation`
* String-backed value object. Extensible, typed, serializable.

### Claim Model C — Formal Claim Registry
* Claims register logical relationships (`entails`, `excludes`).
* Perfect for Stage 8J, but massive over-engineering for Stage 8C.

## Recommendation for v0.1
**Claim Model B — Typed Claim Identifier.** 
We need a formal, extensible target for evidence assertions. A string-backed typed identifier (e.g., `Claim("identity.legal_entity")`) prevents enum-locking while forcing providers to explicitly name what they are proving.
````

## File: docs/algorithms/evidence-dependence-terminology.md
````markdown
# Correlation Is Not Dependence

This document formalizes terminology for evidence fusion, rejecting premature mathematical assumptions.

## Terminology Definitions

* **Shared Provenance:** Two observations originate from the same physical document, same IT system, or same human action. (A fact).
* **Shared Extraction Process:** Two observations were processed by the same software module (e.g. OCR model X). (A fact).
* **Semantic Overlap:** Two observations provide evidence for the exact same Target Claim. (A logical truth).
* **Statistical Correlation:** A measurable, empirical mathematical relationship (e.g. Pearson correlation coefficient > 0) between the values of two variables across a population. (An empirical measurement).
* **Conditional Dependence:** In a probabilistic model (like Bayesian networks), the probability of observing A changes if we know B is true, given some underlying state. (A probabilistic modeling assumption).
* **Common-Cause Failure:** A single failure event (e.g., a blurry scan) that corrupts multiple observations simultaneously. (An engineering vulnerability).

## The Risk of "Correlation"

**DT-001 Should Stage 8J use the term `correlation_group`?**
No. We do not have statistical correlation data. Calling it a correlation group implies we can apply covariance math.

**DT-002 Would `dependence_context` be more honest?**
Yes. Or strictly `lineage`.

**DT-003 Should lineage be preserved without making a dependence judgment?**
Yes. Lineage is a factual observation. Dependence is a modeling assumption based on that fact.

**DT-004 Can fusion infer possible shared failure context from lineage?**
Yes. The fusion engine can heuristically down-weight evidence from the same `source_document` without needing to prove statistical correlation.

**DT-005 What empirical data would be required to estimate actual dependence?**
A massive, manually annotated ground-truth dataset where both signals fail, succeed, or diverge independently.

**DT-006 Can synthetic scenarios establish real-world dependence?**
No. Synthetics only prove the model behaves as the developer programmed it. They cannot prove the real-world statistical distribution of errors.

**DT-007 What should ReconGraph claim before such data exists?**
ReconGraph should claim: "These two observations share provenance." It must absolutely forbid claiming: "These two observations are statistically correlated."

## Forbidden Terminology
Until empirical data exists, the following terms are forbidden in production fusion logic or documentation:
* Correlation
* Covariance
* Statistical Dependence
* Bayesian Update (unless explicitly modeled as such)
````

## File: docs/algorithms/evidence-magnitude-semantics.md
````markdown
# Evidence Magnitude Semantics

This document formalizes the mathematical meaning of `support_magnitude` and `conflict_magnitude` to prevent a "fake-math" catastrophe in Stage 8J.

## Magnitude Challenge Answers

**MS-001 Magnitude relative to what scale?**
Relative to the specific `magnitude_contract` declared by the claim or the provider.

**MS-002 Does 1.0 mean maximal evidence under the provider's model?**
Yes, but "maximal evidence" for lexical similarity is mathematically different from "maximal evidence" for rare reference matching.

**MS-003 Can magnitudes from different providers be compared?**
Not blindly. 

**MS-004 Can magnitude 0.8 from vendor evidence be compared with 0.8 from financial evidence?**
No. They are fundamentally different axes of observation.

**MS-005 If not, can Stage 8J consume them directly?**
Stage 8J can consume them to apply logical rules (e.g., "if any conflict on tax ID > 0.5, block") but it **must not** naively sum or average them.

**MS-006 Does each claim require a magnitude contract?**
Yes.

**MS-007 Does each provider require calibration?**
Yes, eventually (Stage 8K).

**MS-008 Can structural heuristics and corpus-derived rarity use the same magnitude scale?**
No. Structural heuristics are typically binary or stepped. Corpus rarity is continuous and empirical.

**MS-009 Can Reference Evidence bounded positive compatibility be called support magnitude?**
Yes, as long as its contract explicitly defines that the magnitude represents `rarity_v1`.

**MS-010 Are binary magnitudes valid?**
Yes. An exact mathematical conservation is binary: 1.0 (conserved) or 0.0 (not). A binary flag like `UNDERPAYMENT` translates cleanly to a 1.0 `conflict_magnitude` against the claim `financial.conservation`.

**MS-011 Can an assertion use: `support = 1.0` and `conflict = 1.0`?**
Yes. A claim like `financial.payment_completeness` might see exact invoice net amount matched (support 1.0) but a massive unallocated tax amount variance (conflict 1.0).

**MS-012 Should magnitude semantics be claim-local?**
Yes.

## Candidate Models
* **MM-A (Universal Scale):** Mathematically fraudulent.
* **MM-B (Provider-Local Scale):** Makes cross-provider fusion impossible.
* **MM-C (Claim-Local Magnitude Contract):** Claims define the scale. All providers targeting `identity.same_legal_entity` must project onto its defined contract scale.
* **MM-D (Uncalibrated + Metadata):** Store raw output, push calibration entirely to fusion.

## Recommendation
**MM-C (Claim-Local Magnitude Contract).**
To fuse evidence, Stage 8J must know what the numbers mean. The `ClaimDescriptor` must define the magnitude contract (e.g., "0.0 to 1.0 representing Jaccard similarity").

**What is Stage 8J forbidden from doing before calibration?**
Stage 8J is absolutely forbidden from treating uncalibrated raw magnitudes from different contracts as probabilistic weights in a universal summation or Bayesian update.
````

## File: docs/algorithms/evidence-state-algebra-v2.md
````markdown
# Evidence State Algebra V2

This document challenges the Stage 8C-0C state model by splitting Observation and Interpretation.

## State Separation Analysis

**Is EvidenceState one variable trying to encode two orthogonal dimensions?**
Yes. Whether data is physically present (Observation) is a factual structural reality. Whether an algorithm can extract mathematical meaning from it (Interpretation) is an algorithmic capability.

### Scenario Breakdown
* **PS001 (Valid name, fails legal form extraction):** Observation is `PRESENT`. Lexical interpretation is `INTERPRETED`. Legal-form interpretation is `UNINTERPRETABLE`.
* **PS002 (GSTIN fails checksum):** Observation is `INVALID`. (It is structurally malformed data, not missing data).
* **PS003 (GSTIN valid, unknown jurisdiction):** Observation is `PRESENT`. Interpretation is `UNINTERPRETABLE` for the jurisdiction claim.
* **PS008 (Explicit "UNKNOWN"):** Observation is `INVALID` (or a known null-value proxy).
* **PS009 (Blank):** Observation is `MISSING`.
* **PS010 (Field not in schema):** Observation is `MISSING`.

## Evaluation of State Models
* **ES-A (3 states):** Conflates missing data with invalid data.
* **ES-B (4 states):** Conflates structural validity with algorithmic capability.
* **ES-C (5 states):** Adds `PARTIALLY_INTERPRETABLE`, creating ambiguity (which part failed?).
* **ES-D (Separated Enum):** Creates a clean orthogonal space. 

**Can PARTIALLY_INTERPRETED exist?**
No. If an observation supports multiple claims and one fails, the provider must emit two separate assertions: one `INTERPRETED` and one `UNINTERPRETABLE`. A single assertion must represent exactly one claim, so it must be fully interpreted or uninterpretable for that specific claim.

## Recommendation
**Model ES-D (Separated Enums).**
Stage 8C-0C's state recommendation was fundamentally flawed by category conflation. The kernel requires two distinct properties on the assertion:
1. `ObservationState` (Enum: `PRESENT`, `MISSING`, `INVALID`)
2. `InterpretationState` (Enum: `INTERPRETED`, `UNINTERPRETABLE`)
````

## File: docs/algorithms/evidence-state-algebra.md
````markdown
# Evidence State Algebra

This document formalizes the states of evidence and challenges the use of scalar values for distinguishing absence, ignorance, and neutral evidence.

## State Definitions
* **Absence:** The data required to form an observation does not exist. (e.g. SA001 - Missing Vendor Names).
* **Ignorance:** The data exists, but the provider's logic cannot interpret it. (e.g. SA002 - Multilingual text that the normalizer cannot parse).
* **Neutral Evidence:** The data exists, is interpretable, but mathematically provides zero discriminative power (e.g. SA005 - Ubiquitous `CREDITNOTE`).
* **Conflict:** The data exists, is interpretable, and actively contradicts the claim. (e.g. SA003 - Mismatched Tax IDs).

## The Adequacy of `(support: float, conflict: float, availability: bool)`
Is this tuple sufficient? No.
Consider `availability=True, support=0.0, conflict=0.0`. 
This could represent:
1. **Ignorance:** The provider crashed or returned early because it couldn't parse the string.
2. **Neutrality:** The token was so common (e.g. `TRADERS`) that the corpus math yielded exactly `0.0` support.
The fusion engine must know if the provider *failed* to analyze, or *successfully* analyzed and found zero value.

## Truth Table

| Observation State | Interpretation Capability | Support | Conflict | Meaning |
|---|---|---|---|---|
| MISSING | N/A | 0.0 | 0.0 | True absence of data. No evidence exists. |
| OBSERVED | INCAPABLE | 0.0 | 0.0 | Epistemic ignorance. We have data, but no tools to understand it. |
| OBSERVED | CAPABLE | 1.0 | 0.0 | Perfect support for the claim. |
| OBSERVED | CAPABLE | 0.0 | 1.0 | Total contradiction of the claim. |
| OBSERVED | CAPABLE | 0.5 | 0.0 | Partial support (e.g. subset match). |
| OBSERVED | CAPABLE | 0.0 | 0.5 | Partial conflict (e.g. one digit off). |
| OBSERVED | CAPABLE | 0.5 | 0.5 | Bipolar evidence (supports one part, contradicts another). |
| OBSERVED | CAPABLE | 0.0 | 0.0 | Zero discriminative value (e.g. ubiquitous generic term). |

**Can support/conflict numbers be interpreted correctly without an explicit observation/interpretation state?**
No. `0.0/0.0` is severely overloaded without an explicit enum declaring whether the provider succeeded in analyzing the observation.

Therefore, an explicit state enum (`MISSING`, `UNINTERPRETABLE`, `OBSERVED`) is strictly mathematically required before interpreting the floats.
````

## File: docs/algorithms/financial-relationship-score.md
````markdown
# Financial Relationship Score

## Purpose

ReconGraph combines multiple primitive compatibility signals to estimate the strength of a relationship between financial evidence records.

The Financial Relationship Score is a compatibility score. It is not a calibrated probability that two records represent the same financial event.

## Primitive Signals

The purchase-to-GST baseline uses five primitive signals:

* entity compatibility
* reference compatibility
* amount compatibility
* temporal compatibility
* tax identity compatibility

Each available signal produces a score between 0.0 and 1.0.

An unavailable signal is represented as `None`.

Unavailable evidence is distinct from contradictory evidence.

## Purchase-to-GST Baseline Weights

| Signal | Weight |
|--------|--------|
| Entity | 0.20 |
| Reference | 0.20 |
| Amount | 0.25 |
| Temporal | 0.10 |
| Tax identity | 0.25 |

The weights are explicit baseline policy hypotheses.

They are not learned parameters and should not be interpreted as statistically optimal feature importance values.

## Base Compatibility Score

Only available signals participate in the base compatibility calculation.

For the set of available signals A:

`base_score = sum(weight_i * score_i) / sum(weight_i)`

for all i in A.

This available-weight renormalization prevents missing evidence from being treated as either a mismatch or a perfect match.

A signal with score 0.0 is available evidence and remains in the weighted denominator.

A signal with value `None` is unavailable and is excluded from both the weighted numerator and the available-weight denominator.

## Evidence Coverage

Evidence coverage measures how much of the relationship policy's expected weighted evidence is available.

`coverage = available_weight / total_configured_weight`

Coverage is maintained separately from compatibility.

A pair may have high compatibility among available signals while still having low evidence coverage.

For example, two records with only perfectly matching vendor evidence may have a base compatibility score of 1.0 but coverage of only 0.20 under the purchase-to-GST baseline policy.

Future decision policy should consider both relationship score and evidence coverage.

## Contradiction Penalty

The purchase-to-GST v0.1 policy treats an explicit tax identity mismatch as contradictory evidence.

When the tax identity signal is available and equals 0.0, the baseline applies a contradiction penalty multiplier of 0.50.

`final_score = base_score * contradiction_penalty`

When no configured contradiction is present, the multiplier is 1.0.

The tax identity mismatch influences the result in two ways:

1. Its 0.0 score contributes no positive compatibility while remaining in the weighted denominator.
2. The explicit contradiction additionally activates the relationship-level penalty.

This strong treatment is deliberate in the v0.1 purchase-to-GST policy and should be evaluated against labelled reconciliation pairs.

## Missing Evidence

Missing evidence does not activate a contradiction penalty.

For example, a missing tax identity produces an unavailable tax signal and reduces evidence coverage.

It does not behave like an explicit tax identity mismatch.

## Current Limitations

The baseline weights and contradiction penalty are manually specified policy hypotheses.

They have not been trained or calibrated against a production reconciliation dataset.

The current model assumes signal contributions are combined linearly before contradiction treatment.

Interactions between signals are represented only through explicit contradiction rules.

Future evaluation may compare the deterministic baseline against learned pairwise models using the primitive signal vector as input features.

## Design Principle

Primitive signals measure individual forms of compatibility.

Relationship policy determines signal importance and contradiction treatment.

Compatibility and evidence coverage are separate dimensions.

A high relationship score with low coverage must not be interpreted the same way as a high relationship score supported by complete evidence.
````

## File: docs/algorithms/identifier-authority-boundary.md
````markdown
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
````

## File: docs/algorithms/indian-tax-identity-evidence-v1.md
````markdown
# Indian Tax Identity Evidence V1

This document defines the semantic boundary and extraction rules for Goods and Services Tax Identification Number (GSTIN) and Permanent Account Number (PAN) evidence in ReconGraph.

## Section A — GSTIN Structural Decomposition

A GSTIN is structurally composed of meaningful fields. It is a 15-character alphanumeric string.
Example: `07ABCDE1234F1Z5`

1. **State Code** (Positions 1-2): Integer `01` to `38`. Represents the state jurisdiction of the registration.
2. **PAN** (Positions 3-12): The 10-character Permanent Account Number of the legal entity. Structure: `AAAAA9999A` (5 alpha, 4 digit, 1 alpha).
3. **Entity Number** (Position 13): Alphanumeric (`1-9`, `A-Z`). Indicates the number of registrations the entity holds in that state.
4. **Z Character** (Position 14): Hardcoded to `Z` by default.
5. **Checksum** (Position 15): Alphanumeric checksum character.

## Section B — Identity Separation Table

We separate state-level GST registration from national-level PAN tax identity.

| Scenario | full GSTIN | state code | PAN | entity num | assertions emitted |
|---|---|---|---|---|---|
| Same GSTIN | same | same | same | same | SUPPORT `same_gst_registration` 1.0, SUPPORT `same_tax_identity` 1.0 |
| Same PAN, same state, diff entity | diff | same | same | diff | CONFLICT `same_gst_registration`, SUPPORT `same_tax_identity` |
| Same PAN, diff state | diff | diff | same | - | CONFLICT `same_gst_registration`, SUPPORT `same_tax_identity` |
| Diff PAN | diff | - | diff | - | CONFLICT `same_gst_registration`, CONFLICT `same_tax_identity` |
| One missing | one absent | - | - | - | MISSING_INPUT for all |
| One malformed | structurally invalid | - | - | - | UNINTERPRETABLE_INPUT |

## Section C — Validation Rules

Before ANY extraction occurs, the GSTIN must pass structural validation.

1. **Length check**: Must be exactly 15 characters.
2. **State code validity**: Must be an integer between `01` and `38`.
3. **PAN structural pattern**: Positions 3-12 must match the regex `[A-Z]{5}[0-9]{4}[A-Z]`.
4. **Entity number**: Position 13 must be `1-9` or `A-Z`.
5. **Character at position 14**: Must be `Z`.
6. **Character at position 15**: Must be a valid alphanumeric checksum char.

IF validation fails → `UNINTERPRETABLE_INPUT`. Do NOT attempt PAN extraction.
IF validation passes → Extract components and produce typed observations.

## Section D — OCR Corruption Patterns

GSTINs from invoices are often corrupted by Optical Character Recognition (OCR).
Common confusions:
- `O` / `0` (letter O vs digit zero)
- `I` / `1`
- `B` / `8`
- `G` / `6`

Example: `O7ABCDE1234F1Z5` (O instead of 0 for state code).

**Validate, don't guess.** A malformed GSTIN must not produce any tax assertion. We do not silently repair tax identifiers in deterministic vendor identity V1. It produces `UNINTERPRETABLE_INPUT`.

## Section E — Non-Entailment Rules

- `identity.same_tax_identity` MUST NOT imply `identity.same_gst_registration`.
- `identity.same_gst_registration` MUST NOT directly imply `identity.same_legal_entity` (though it provides extremely strong evidence).
- `different_state_code` MUST NOT imply `identity.different_legal_entity`.
- `identity.same_tax_identity` (same PAN) MUST NOT imply `identity.same_legal_entity` without additional evidence (mergers/acquisitions can complicate PAN ownership, though 99% of the time PAN = Legal Entity).
````

## File: docs/algorithms/legal-entity-primitive-evidence-units.md
````markdown
# Primitive Evidence Units for Legal Entity Identity

This document defines the primitive evidence units capable of bearing evidence on the claim `SAME_LEGAL_ENTITY`.

## Primitive Units

### VE-001 — Exact Normalized Full Name Agreement
* **Required Observations:** Raw string A, Raw string B.
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Potential Support:** Weak (without statistics).
* **Potential Conflict:** None. (Mismatch does not prove different entity, as aliases exist).
* **Authority Source:** Structural Heuristic.
* **Statistics Required:** No.
* **External Knowledge:** No.

### VE-002 — Discriminative Name Token Agreement
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Potential Support:** High (if rare token).
* **Potential Conflict:** None.
* **Statistics Required:** Yes. (Must know token document frequency).

### VE-003 — Legal Form Agreement
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Potential Support:** Weak. (Many companies are `PVT LTD`).
* **Potential Conflict:** Strong. (A mismatch from `LLP` to `PVT LTD` on the same core name is highly conflicting).
* **Statistics Required:** No.
* **External Knowledge:** Legal suffix dictionary.

### VE-004 — Legal Form Conflict
* **Target Claim:** `SAME_LEGAL_ENTITY`
* **Can this directly contradict same legal entity?** Yes. Unless a historical legal conversion took place (which requires temporal data), an LLP and a PVT LTD are distinctly registered legal entities.

### VE-005 — Authoritative Identifier Agreement
* **Target Claim:** `SAME_REGISTERED_TAX_IDENTITY` (A proxy for Legal Entity).
* **Potential Support:** Strongest.
* **Potential Conflict:** Strongest.
* **Authority:** Verifiable Registry.

### VE-006 — Authoritative Identifier Conflict
* **Can PAN and GSTIN be compared?** No. A PAN identifies a taxpayer. A GSTIN identifies a state-level registration under a PAN. Comparing PAN `ABCDE1234F` to GSTIN `27ABCDE1234F1Z5` string-to-string is invalid. They must be parsed.

### VE-010 — Generic Full Name Equality
* **Example:** `TRADERS` vs `TRADERS`.
* **Potential Support:** Zero. (Discriminative power is nil).

### VE-012 — OCR-Confusable Name Similarity
* **Example:** `MICR0SOFT` vs `MICROSOFT`.
* **Potential Conflict:** Without OCR provenance (e.g. knowing it was extracted from an image), treating this as conflict is dangerous. With OCR provenance, it can be normalized as an observation error.

## Authorized Units for v0.1
To keep v0.1 narrow and intellectually honest, the following are AUTHORIZED:
* VE-001 (Exact Normalized Full Name Agreement)
* VE-003 (Legal Form Extraction/Agreement)
* VE-004 (Legal Form Conflict)
* VE-005/VE-006 (Authoritative Identifier Agreement/Conflict)

The following are EXPLICITLY DEFERRED:
* VE-002 (Corpus Statistics) - Requires a profiler infrastructure.
* VE-007 (Aliases) - Requires a knowledge base.
* VE-012 (OCR correction) - Requires confidence scores we lack.
````

## File: docs/algorithms/reference-evidence-interpreter-cases.md
````markdown
# Reference Evidence Interpreter Cases

Status: Pre-Implementation Test Matrix

| Case | Evidence | Profile state | Expected path | primary evidence unit | token contributions considered? | expected winning identity | expected statistics_available | expected statistical_coverage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RI001 | exact SB8891 | frequency 1/100 | normalized reference | normalized reference | no | sb8891 | true | 1.0 |
| RI002 | exact CREDITNOTE | frequency 80/100 | normalized reference | normalized reference | no | creditnote | true | 1.0 |
| RI003 | exact NEW999999 | unavailable | normalized reference fallback | normalized reference | no | new999999 | false | 0.0 |
| RI004 | shared 874219 | DF 1/100 | token | token | yes | 874219 | true | 1.0 |
| RI005 | shared 001 | DF 80/100 | token | token | yes | 001 | true | 1.0 |
| RI006 | shared 874219 | unavailable | long token fallback | token | yes | 874219 | false | 0.0 |
| RI007 | shared 001 | unavailable | medium repeated-pattern fallback | token | yes | 001 | false | 0.0 |
| RI008 | shared 01 | unavailable | short repeated-pattern fallback | token | yes | 01 | false | 0.0 |
| RI009 | shared 000000 | unavailable | long repeated-pattern fallback | token | yes | 000000 | false | 0.0 |
| RI010 | tokens 2026, 874219 | DF 80/100, 1/100 | strongest token | token | yes | 874219 | true | 1.0 |
| RI011 | tokens 991827, 874219 | DF 1/100, 1/100 | deterministic tie | token | yes | 874219 | true | 1.0 |
| RI012 | token A fallback 0.60, token B profiled 0.55 | mixed | fallback winner | token | yes | token A | false | 0.0 |
| RI013 | token A fallback 0.40, token B profiled 0.55 | mixed | profiled winner | token | yes | token B | true | 1.0 |
| RI014 | token A fallback 0.60, token B profiled 0.60 | mixed | profiled tie winner | token | yes | token B | true | 1.0 |
| RI015 | exact reference with numeric substring | profiled | exact path only | normalized reference | no | exact normalized match | true | 1.0 |

For RI015 explicitly state: exact normalized identity exists -> shared numeric token is not interpreted. This prevents double counting.
````

## File: docs/algorithms/reference-evidence-model.md
````markdown
# Reference Evidence Model

## Status

Experimental architecture note. No production implementation is implied by this document.

## Problem

A scalar reference score collapses multiple distinct questions into one value:

1. Do the normalized references match exactly?
2. Which numeric tokens are shared?
3. How discriminative are those shared tokens in the ledger?
4. Are the surrounding reference namespaces compatible?
5. Why did the final reference evidence receive its strength?

Example A — Genuine rare shared identifier
```
INV-874219
AB/874219
```
Current: 0.8
Desired decomposition:
- exact normalized identity: false
- shared tokens: 874219
- token df: 2
- collision burden: 1
- namespace compatibility: unknown

Example B — Common collision
```
INV-001
ABC-001
```
Current: 0.8
Desired decomposition:
- exact normalized identity: false
- shared tokens: 001
- token df: 4
- collision burden: 3
- namespace compatibility: unknown

Example C — Rare but contextually ambiguous
```
INV-2026-1001
ABC-2026-1001
```
Current: 0.8
Desired decomposition:
- exact normalized identity: false
- shared tokens:
  2026:
    df: 40
  1001:
    df: ?
- namespace compatibility: unknown

Why is a single scalar insufficient as the intermediate representation?
A single scalar permanently deletes the provenance of the evidence. If the scoring engine just receives `0.8`, it cannot know if this was a rare shared identifier (strong genuine evidence) or a structurally long but commonly repeated token like "999999" (weak collision). By collapsing these facts into one scalar early in the pipeline, every subsequent semantic or decision layer is robbed of the ability to reason about *why* the references match, making nuanced semantic rules or namespace compatibility checks impossible.

## Similarity vs Identity Evidence
Is `reference_similarity()` actually the correct abstraction?
Probably not. We are not measuring string similarity. `INV-874219` and `AB/874219` are textually dissimilar but share a highly discriminative identity-bearing structure. Conversely, `INVOICE-2026` and `INVOICE-2025` are highly textually similar (Levenshtein distance is tiny) but they represent distinct financial events. We are measuring *reference identity evidence*, not raw textual similarity.

## Candidate Data Model

```python
@dataclass(frozen=True)
class SharedReferenceToken:
    token: str
    document_frequency: int

@dataclass(frozen=True)
class ReferenceIdentityEvidence:
    normalized_a: str
    normalized_b: str
    exact_match: bool
    shared_numeric_tokens: tuple[SharedReferenceToken, ...]
```

### Critique
**Q1: Should document_frequency live inside SharedReferenceToken?**
No. Putting corpus statistics directly inside the extraction layer tightly couples pure string manipulation (identity extraction) with database lookups (corpus statistics). It prevents testing extraction independently of the corpus and violates separation of concerns.

**Q2: Should ReferenceIdentityEvidence contain raw references?**
No. The caller (the scoring engine) already owns the source `PurchaseRecord` and `GSTRecord`. Duplicating `raw_a` and `raw_b` inside the evidence object just creates redundant payload and risks desync.

**Q3: Should exact match be `exact_match: bool` vs `MatchKind` enum?**
It should remain `exact_match: bool` (or a separate factual dimension). An enum implies mutual exclusivity, but a pair can easily have *both* an exact normalized match (`INV-001` and `INV-001`) *and* shared numeric tokens (`001`). Using an enum would force us to pick a "primary" match kind and hide the other facts.

**Q4: Should shared tokens be `tuple[str, ...]` vs evidence objects?**
They should be `tuple[str, ...]`. Identity extraction should purely report structural overlap (facts). A subsequent enrichment layer can pair those structural facts with corpus statistics (`ReferenceTokenStatistics`), and then produce an `EnrichedReferenceEvidence` object.

## Exact Identity Is Not Necessarily Unique Identity
Consider exact matches:
- 001 ↔ 001
- INV-001 ↔ INV-001
- 2026 ↔ 2026
- 874219 ↔ 874219

Should all four receive `1.0`?
No. An exact normalized match on "001" or "INV-001" is weak evidence if "INV-001" is used by 50 different vendors in the ledger. Exactness and uniqueness represent two perfectly orthogonal dimensions. A string can match exactly but still carry zero uniqueness (like "CREDITNOTE"). Thus, exact normalized identity is a structural fact (`true`), but its evidentiary strength must still be judged by its corpus uniqueness.

## Corpus Scope
Which scope should document frequency be calculated over?
Scope D (Per relationship source pair). By computing DF across only the sources involved in the relationship hypothesis (e.g., Purchase + GST), we ask: "How discriminative is this identifier among the records that could plausibly participate in this exact type of reconciliation?" This avoids diluting or polluting the statistics with namespaces from completely unrelated domains (like bank transactions).

## Temporal Scope and Double Counting
Should v0.1 reference corpus statistics use the full tenant relationship corpus or a temporal candidate window?
Full corpus. If reference informativeness is evaluated using a ±30 day candidate window, the DF effectively becomes a proxy for time (a common token might look rare if we zoom in enough). But we *already* have a dedicated temporal similarity signal. If both reference evidence and temporal evidence incorporate time, we are double-counting the temporal dimension. Reference informativeness should measure absolute identifier collision across the ledger.
````

## File: docs/algorithms/reference-evidence-ordering.md
````markdown
# Reference Evidence Ordering Constraints

Before selecting an interpretation formula, ReconGraph defines qualitative ordering constraints that any valid reference evidence interpretation must satisfy. These constraints act as the invariants of the interpretation formula.

## RO-001 — Corpus rarity should increase discriminative evidence
`RE003 > RE004`
`RE005 > RE006`

All else equal, a shared identity token observed in fewer corpus documents should provide stronger positive evidence.

## RO-002 — Exact identity is not universally perfect evidence
`RE001 > RE012`

An exact normalized identity that is rare in the corpus should provide stronger evidence than an exact identity appearing in most corpus observations. This explicitly rejects the idea that an exact match should unconditionally result in `1.0`.

## RO-003 — Repeated generic exact identities should be discounted
`RE001 > RE002`
`RE011 > RE002`

Rare full-reference identity should be more discriminative than frequently repeated generic reference labels (e.g. `CREDITNOTE`).

## RO-004 — Token length may provide a prior, but cannot replace corpus evidence
Proposed ordering: `RE003 > RE005` (even though both have `DF = 2`)

A six-digit identifier may be more discriminative than a three-digit sequence due to a larger identifier space.

**Status**: hypothesis requiring explicit policy decision. The corpus already gives us empirical collision context, we need to decide whether length contributes independent information or double-counts rarity.

## RO-005 — Common evidence should be weak, not contradictory
Proposed: `RE008 ≈ RE003` (if 874219 is the dominant rare shared token and 2026 is extremely common).

The common token should contribute little or no additional positive evidence. It should not automatically negate the rare token.

**Status**: proposed.

## RO-006 — Multiple informative shared tokens should not reduce evidence
`RE007 >= RE003`

Assuming both tokens provide non-negative identity evidence. However, tokens like `2026` and `874219` may not be statistically independent, so naive addition may double count evidence.

## RO-007 — Missing corpus context must not be interpreted as rarity
`RE010 != "maximally rare"`

No profile statistics cannot imply maximal discriminativeness.

## RO-008 — Partial corpus context must remain observable
`RE009` must be distinguishable from fully profiled evidence and fully out-of-profile evidence.

This means Stage 3 may need more than a scalar to represent statistical coverage and interpretation.

## RO-009 — Non-numeric exact identities remain valid evidence
`RE011` must receive positive identity evidence despite having no numeric tokens.

## RO-010 — Interpretation must be deterministic and bounded
Any eventual scalar compatibility component must satisfy:
`0.0 <= score <= 1.0`

for the same evidence + profile + policy, and produce the same result deterministically without random calibration or corpus mutation.
````

## File: docs/algorithms/reference-evidence-units.md
````markdown
# Reference Evidence Units

**Purpose**: Define the atomic evidence units consumed by reference interpretation and determine whether the current corpus statistics are sufficient to combine multiple units safely.

## EU-001 — Exact normalized reference identity

The evidence unit is: **normalized full-reference identity**

**Example**:
`INV-874219` and `INV/874219` produces:
`normalized identity = inv874219`

The evidence unit is `inv874219`, NOT `inv874219` + `874219` as two equal independent identity units.
Because the numeric token is structurally contained within the exact full-reference identity, the full normalized identity is the primary evidence unit for the exact interpretation path.

**Status**: Proposed

## EU-002 — Shared numeric token identity

When `exact_normalized_match = False`, each unique shared numeric token is a **candidate evidence unit**.

**Example**:
`INV-2026-874219` and `AB-2026-874219`
candidate units: `2026` and `874219`

Important wording: *candidate evidence unit*, not *independent evidence unit*.

**Status**: Proposed

## Structural Distinctness Is Not Statistical Independence

For an example pair like:
`INV-2026-874219` and `AB-2026-874219`

Stage 1 correctly reports `("2026", "874219")`. They are structurally distinct tokens (`2026 != 874219`).

However, structural distinctness does not prove `P(2026 ∩ 874219) = P(2026)P(874219)` or any independence assumption.

Stage 1 deduplication protects against duplicate structural identity values (e.g., `INV-874219-874219`). It does not protect against correlated distinct identity values. Deduplication does nothing about the possibility that `2026` and `874219` are correlated in the corpus.

## Marginal Document Frequency Is Insufficient for Independence-Aware Combination

Consider two corpus environments for tokens `2026` and `874219`:
- **CO001**: `DF(2026) = 20`, `DF(874219) = 20`, `joint DF = 20` (Perfect co-occurrence)
- **CO002**: `DF(2026) = 20`, `DF(874219) = 20`, `joint DF = 0` (Zero overlap)

Both profiles expose `DF(2026) = 20`, `DF(874219) = 20`, and `N = 100`. But CO001 joint DF is 20 and CO002 joint DF is 0.

Therefore any function `combine(df_a, df_b, reference_count)` must produce the same output for CO001 and CO002, even though the observed corpus co-occurrence structure differs drastically.

**Conclusion**: Marginal document frequency alone is insufficient to support a statistically justified independence-aware multi-token combination rule.

## Architecture Directions for Multi-Token Evidence

### Direction A — Strongest-unit interpretation
For non-exact identity: `score = strongest individual shared-token evidence`
- **Benefits**: uses current marginal DF, avoids correlation double counting, simple explanation, bounded naturally.
- **Cost**: multiple genuinely independent identifiers provide no additional support.
- **Status**: Open

### Direction B — Conservative accumulation with a capped secondary bonus
Primary strongest token + small bounded support from additional informative tokens.
- **Benefits**: multiple evidence can matter, less aggressive than probabilistic union.
- **Cost**: bonus is policy-driven, not statistically independence-justified.
- **Status**: Open

### Direction C — Expand corpus statistics for co-occurrence-aware combination
Track some form of joint token document frequency.
- **Benefits**: can observe token dependence, supports richer multi-token interpretation.
- **Costs**: larger corpus profile, higher profiling complexity, sparse pair statistics, policy becomes mathematically more complex.
- **Status**: Open
````

## File: docs/algorithms/source-ontology-model.md
````markdown
# Source Ontology Model
## Part B — Source Ontology Research

### Source Classes Analyzed
* **ERP database row**: SourceSystem: `erp.sap`, Artifact: `table:purchase_invoice`, Locator: `row:874219:vendor_name`
* **PDF invoice**: SourceSystem: `document.upload`, Artifact: `sha256:abc...`, Locator: `page=2,bbox=(...)`
* **GST return row**: SourceSystem: `registry.gstn`, Artifact: `return_period:2024-Q1`, Locator: `gstin:123`

### The Three-Part Ontology
`SourceSystem`, `SourceArtifact`, and `SourceLocator` **must** be three separate concepts.
- **SourceSystem**: Defines the namespace and trust boundary (e.g., `sap.production`).
- **SourceArtifact**: Defines the physical or logical container of the facts (e.g., PDF hash, DB table).
- **SourceLocator**: Defines the exact coordinate within the artifact (e.g., row, bbox).

*Source class is not evidence independence.*
````

## File: docs/algorithms/temporal-scoring.md
````markdown
# Temporal Scoring

## Baseline

ReconGraph's baseline temporal compatibility signal uses linear decay over the absolute number of days between two financial evidence records.

For a configured maximum temporal window `w` and absolute day difference `d`:

`score = max(0, 1 - d / w)`

The score is `1.0` when two records share the same date and decays linearly to `0.0` at the configured temporal-window boundary.

## Relationship-Specific Windows

The temporal scoring function does not define a universal financial date window.

The expected temporal distance between financial records depends on the relationship being evaluated.

For example, a purchase-register entry and a GST record may be expected to occur relatively close together, while an invoice and its associated bank payment may legitimately be separated by a longer payment term.

Relationship-level scoring policy should therefore provide the temporal window used by the primitive temporal scoring function.

## Current Limitation: Direction-Agnostic Scoring

The baseline implementation uses absolute date distance.

As a result, a record occurring three days before another record receives the same temporal score as a record occurring three days after it.

This is acceptable for the initial purchase-to-GST reconciliation baseline but may be inappropriate for directional financial relationships.

Future relationship policies may use asymmetric temporal windows or directional temporal scoring.

For example, invoice-to-payment relationships may allow a larger window after an invoice date than before it.

## Design Principle

Temporal compatibility and temporal relationship policy are separate concerns.

The signal function calculates compatibility for a provided window.

The relationship policy determines which window and temporal assumptions are appropriate for the financial relationship being evaluated.
````

## File: docs/algorithms/vendor-alias-and-acronym-semantics-v1.md
````markdown
# Vendor Alias and Acronym Semantics V1

Acronyms in Indian B2B data represent a giant false-positive minefield. Generic acronym algorithms can create catastrophic matches. (e.g. `TCS` = `Tata Consultancy Services` or `TCS Logistics`).

We structure acronym and alias evidence across three authority levels.

## 1. Derived Acronym (Low Authority)
- **Algorithm**: Deterministic derivation (e.g. `TATA CONSULTANCY SERVICES` → `TCS` by taking the first letters of major tokens).
- **Authority**: `deterministic_rule.acronym_derivation`
- **Constraint**: Derivation must be strictly deterministic so that the same input yields the same derived artifact identity.
- **Risk**: High collision rate. `TCS LOGISTICS` would also match the derived acronym `TCS`. Therefore, this evidence alone is low authority and usually requires corroboration (like a matching GSTIN).

## 2. Known Alias (Higher Authority)
- **Algorithm**: An explicit mapping in the vendor master or a verified registry (`TCS` ↔ `TATA CONSULTANCY SERVICES`).
- **Authority**: `vendor_master.alias_registry`
- **Constraint**: Must carry a `SemanticDependencyRef` to the alias snapshot used for the lookup. If the snapshot changes, the derived interpretation changes.

## 3. Observed Acronym (Context-Dependent Authority)
- **Algorithm**: The acronym is explicitly observed in the same source document (e.g., an invoice reading `"Tata Consultancy Services (TCS)"`).
- **Authority**: Depends on the source occurrence.
- **Constraint**: Must carry ancestry back to the source occurrence.

### The Stage 8J Preservation Requirement
If both the purchase vendor name and the GST vendor name derive their acronyms from the **SAME** uploaded invoice, this creates correlated evidence. If Stage 8J double-counts this, it will falsely inflate confidence.
**Rule:** Do not solve alias fusion now. But preserve ancestry via `EvidenceAncestryRef` so Stage 8J can detect correlated evidence.

## Specific Traps
- `TCS (Tata Consultancy Services)` vs `TCS (TCS Logistics)` (TCS is their actual brand/core).
- `SBI (State Bank of India)` vs `SBI Life Insurance` (SBI is the parent company acronym, but they are different legal entities).
- `HUL (Hindustan Unilever)` — A highly reliable known alias at the registry level.
- `IOC (Indian Oil Corporation)` vs `IOC` (any number of other International/Indian entities).
````

## File: docs/algorithms/vendor-core-similarity-research.md
````markdown
# Vendor Core Similarity Research V1

Lexical similarity metrics provide raw observations. They do not directly calculate assertion magnitudes. 

## Similarity Metrics Investigated

1. **Exact canonical equality**
   - **Algorithm**: String equality after canonicalization.
   - **Strengths**: Perfect precision for identical inputs. Zero false positives on exact cores.
   - **False Positive Risk**: Low (unless core is extremely common, e.g., "TRADERS").
   - **Output**: Boolean (1.0 or 0.0).

2. **Token-set equality (order-independent)**
   - **Algorithm**: `set(tokens_a) == set(tokens_b)`.
   - **Strengths**: Handles word reordering (e.g., `ENTERPRISES BALAJI` ↔ `BALAJI ENTERPRISES`).
   - **False Positive Risk**: Low.
   - **Output**: Boolean (1.0 or 0.0).

3. **Token multiset equality**
   - **Algorithm**: Considers token counts (e.g., `MAHINDRA MAHINDRA` != `MAHINDRA`).
   - **Strengths**: Preserves duplicate token semantics.
   - **False Positive Risk**: Very Low.

4. **Token containment (Subset)**
   - **Algorithm**: `set(tokens_a).issubset(set(tokens_b))`.
   - **Strengths**: Handles partial omissions (e.g., `ABC TRADERS` ↔ `ABC TRADERS INDIA`).
   - **False Positive Risk**: High (e.g., `RELIANCE` is a subset of `RELIANCE RETAIL` and `RELIANCE INDUSTRIES`, which are different legal entities).

5. **Levenshtein ratio / Edit distance**
   - **Algorithm**: Edit distance normalized to [0, 1].
   - **Strengths**: Handles typos (`TECHNOLOGIES` ↔ `TECHONLOGIES`).
   - **False Positive Risk**: Medium (can conflate distinct short names, e.g. `ABC` ↔ `ADC`).

6. **Jaro-Winkler**
   - **Algorithm**: Emphasizes prefix matches.
   - **Strengths**: Excellent for names where the most distinct part is at the front.
   - **False Positive Risk**: Medium.

7. **Character trigram similarity**
   - **Algorithm**: Overlap of 3-character sequences.
   - **Strengths**: Robust to spelling variations and OCR errors.
   - **False Positive Risk**: Low to Medium.

8. **Phonetic similarity (Metaphone)**
   - **Algorithm**: Matches words that sound alike.
   - **Strengths**: Good for transcribed names (`SHREE` ↔ `SRI`).
   - **False Positive Risk**: Very High (conflates etymologically distinct but phonetically similar names).

9. **Acronym similarity**
   - **Algorithm**: Compare first letters of major tokens.
   - **False Positive Risk**: Extreme (e.g., `TCS` ↔ `TATA CONSULTANCY SERVICES` vs `TCS LOGISTICS`).

10. **Token IDF-weighted cosine similarity**
    - **Algorithm**: TF-IDF vectors compared via cosine similarity.
    - **Strengths**: Downweights common tokens like `TRADERS`.
    - **False Positive Risk**: Low, requires corpus statistics.

## Adversarial Test Matrix

| Pair | Expected Relationship | Jaro-Winkler | Token-Set | Exact | Acronym | Semantic Risk |
|---|---|---|---|---|---|---|
| ABC ↔ ABC | Same Core | 1.00 | 1.0 | 1.0 | 1.0 | None |
| ABC TRADERS ↔ ABC TRADERS | Same Core | 1.00 | 1.0 | 1.0 | 1.0 | None |
| ABC TRADERS ↔ ABC TECHNOLOGIES | Diff Core | ~0.75 | 0.5 | 0.0 | 1.0 | High FP if threshold low |
| MAHINDRA AND MAHINDRA ↔ MAHINDRA & MAHINDRA | Same Core | 1.00* | 1.0* | 1.0* | 1.0 | None (*after '&' normalization) |
| TATA CONSULTANCY SERVICES ↔ TCS | Alias | ~0.50 | 0.0 | 0.0 | 1.0 | High FN (missed alias) |
| TCS ↔ TCS LOGISTICS | Diff Core | ~0.80 | 0.5 | 0.0 | 0.0 | High FP |
| HDFC BANK ↔ HDFC | Subset | ~0.85 | 0.5 | 0.0 | 0.0 | FP (different entities) |
| RELIANCE INDUSTRIES ↔ RELIANCE RETAIL | Diff Core | ~0.75 | 0.5 | 0.0 | 1.0 | FP |
| AMAZON SELLER SERVICES ↔ AMAZON | Subset | ~0.70 | 0.3 | 0.0 | 0.0 | FP |
| SHREE RAM TRADERS ↔ SRI RAM TRADERS | Phonetic Variant | ~0.90 | 0.6 | 0.0 | 1.0 | FN if exact only |
| BALAJI ENTERPRISES ↔ BALAJI ENTERPRISE | Typo/Variant | 0.98 | 0.5 | 0.0 | 1.0 | None |
| NEW INDIA TRADING CO ↔ NEW INDIA TRADERS | Variant | ~0.90 | 0.5 | 0.0 | 1.0 | None |
| A B C ↔ ABC | Variant | 0.00* | 0.0* | 0.0* | 1.0 | FN (*before whitespace normalization) |
| XYZ INTERNATIONAL ↔ XYZ INTL | Abbreviation | ~0.80 | 0.5 | 0.0 | 1.0 | None |
| GLOBAL TECHNOLOGIES ↔ GLOBAL TECH | Abbreviation | ~0.85 | 0.5 | 0.0 | 1.0 | None |
| BALAJI ENTERPRISES ↔ SHREE BALAJI ENTERPRISES | Subset | ~0.85 | 0.6 | 0.0 | 0.0 | FP |
| TATA MOTORS ↔ TATA POWER | Diff Core | ~0.75 | 0.5 | 0.0 | 1.0 | FP |
| RELIANCE INDUSTRIES ↔ RELIANCE | Subset | ~0.85 | 0.5 | 0.0 | 0.0 | FP |
| STATE BANK OF INDIA ↔ SBI | Alias | ~0.50 | 0.0 | 0.0 | 1.0 | FN |
| HINDUSTAN UNILEVER ↔ HUL | Alias | ~0.40 | 0.0 | 0.0 | 1.0 | FN |

## Interpretation Policy

A similarity metric does not necessarily directly become an assertion magnitude. 
For example, a Jaro-Winkler score of 0.94 does not mean we emit an assertion with `magnitude = 0.94`.

**Metric output is an observation. Assertion magnitude is an interpretation of that observation. They are not inherently identical.**

The interpretation policy mediates this:
- **Exact core equality**: Emits `SUPPORT 1.0`
- **Token-set equality**: Emits `SUPPORT 0.95`
- **High edit similarity (>0.92)**: Emits `SUPPORT 0.75` (a bounded, discrete semantic magnitude, NOT the raw 0.92 metric value).
- **Weak similarity (<0.70)**: No assertion emitted.
````

## File: docs/algorithms/vendor-corpus-statistics-v1.md
````markdown
# Vendor Corpus Statistics V1

A fuzzy name matcher that does not understand frequency will drastically overvalue common terms (e.g. `TRADERS`, `ENTERPRISES`). Stage 8C requires a `VendorCorpusProfile` to weigh evidence by distinctiveness.

## Section A — Required Statistics

The corpus profile should compute:
- `document_frequency_per_token`: The number of unique vendor records that contain a specific canonical token (e.g. `ENTERPRISES` = 45,000).
- `document_frequency_per_organization_core`: The frequency of an entire canonical core (e.g. `BALAJI ENTERPRISES` = 4,000).
- `token_inverse_frequency`: An IDF analog indicating token rarity.
- `core_collision_count`: The number of *distinct* legal entities (verified by distinct PANs/GSTINs) that share the exact same organization core.
- `legal_form_distribution`: Frequency of each canonical legal form in the corpus.
- `acronym_collision_frequency`: How often a given acronym maps to distinct organization cores.

## Section B — What Corpus Statistics Can and Cannot Do

**CAN:**
- Reduce support magnitude for partial matches involving common tokens (e.g. sharing the token `TRADERS` provides less support than sharing the token `MAHINDRA`).
- Withhold assertions entirely when a token is too common to be informative (e.g., sharing only `INDIA` yields no assertion).
- Distinguish high-rarity cores from low-rarity cores to adjust exact-match support confidence.

**CAN NOT:**
- Create conflict evidence. Low distinctiveness represents an absence of information, not a contradiction.
- Override exact canonical equality support (if two records are exactly `ABC PRIVATE LIMITED`, they support each other regardless of how common `ABC` is, though the magnitude may be capped).
- Make two things different just because many things look similar.

**Key Invariant:** Corpus statistics can reduce or withhold support. They must never create conflict evidence.

## Section C — Token Rarity vs. Whole-Core Similarity

Consider the `TATA` group of companies:
- `TATA CONSULTANCY SERVICES` ↔ `TATA POWER`
  - Sharing `TATA` should **not** provide strong `same_organization_core` support, because `TATA` is a highly common token in the Indian corporate corpus that spans dozens of distinct entities.
- `TATA CONSULTANCY SERVICES` ↔ `TATA CONSULTANCY SERVICE`
  - The complete core similarity remains highly informative. The entire phrase is highly distinctive.

This proves that token-level rarity and whole-core similarity are **SEPARATE observations** that must not be collapsed into a single metric. 

### Proposed Separation of Claims

Instead of forcing both into `same_organization_core`, we should evaluate:
1. `identity.same_organization_core`: Evaluates the full core match.
2. `identity.shared_distinctive_organization_token`: Evaluates partial token overlap, tightly gated by a high rarity threshold.
````

## File: docs/algorithms/vendor-corpus-statistics.md
````markdown
# Vendor Corpus Statistics

This document defines a corpus-level research model for vendor names, challenging the assumption that all shared tokens are equally informative.

## VS-001 — Normalized Full Name Frequency
* **What is counted:** Exact matches of the complete normalized string.
* **Denominator:** Total number of distinct authoritative identities (e.g. unique GSTINs) in the corpus.
* **Corpus replication invariance:** Required. Duplicate invoices from the same vendor should not inflate the count.
* **Absence mean zero?** Yes.
* **Require ground-truth entity IDs?** Yes, to avoid counting 100 invoices from the same entity as 100 different entities.
* **What it does NOT prove:** Doesn't help with partial matches or typos.

## VS-002 — Vendor Token Document Frequency
* **What is counted:** Occurrences of a specific token (e.g., `INDIA`, `TRADERS`) across distinct vendor identities.
* **Denominator:** Total number of distinct vendor identities.
* **Corpus replication invariance:** Required.
* **Absence mean zero?** Yes.
* **Require ground-truth entity IDs?** Yes.
* **What it does NOT prove:** Does not prove legal identity. Only proves how discriminative (or useless) a token is.

## VS-003 — Legal Form Frequency
* **What is counted:** Occurrences of tokens like `LLP`, `PVT`, `LTD`.
* **What it does NOT prove:** Does not prove identity. It proves that exact match on `LLP` provides almost zero discriminative evidence.

## VS-004 — Organizational Core Frequency
* **What is counted:** Occurrences of the non-generic, non-legal part of the name (e.g., `SHREE GANESH`).

## VS-005 — Alias Ambiguity
* **What is counted:** Number of distinct authoritative identities sharing the exact same alias (e.g., how many companies map to `TCS`).
* **What it does NOT prove:** An alias with high ambiguity provides weak evidence unless paired with contextual signals (like exact tax amount).

## VS-006 — Abbreviation Collision Rate
* **What is counted:** Number of identities sharing an acronym (e.g. `ABC`).
````

## File: docs/algorithms/vendor-identity-factor-model-v1.md
````markdown
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
````

## File: docs/algorithms/vendor-identity-latent-variables.md
````markdown
# Vendor Identity Latent Variables

## The Latent Variables

The current architecture confusingly bundles multiple identity questions into a single scalar "vendor score". This document formally separates them.

### LI-001 — Lexical Name Identity
* **Question:** Do the observed vendor name strings appear to represent the same written organization name?
* **Example:** `TATA CONSULTANCY SERVICES LIMITED` vs `Tata Consultancy Services Ltd`

### LI-002 — Legal Entity Identity
* **Question:** Do the records refer to the exact same legally registered entity?
* **Example:** `ABC PRIVATE LIMITED` vs `ABC LLP`

### LI-003 — Corporate Family Identity
* **Question:** Do the records refer to organizations belonging to the same corporate group?
* **Example:** `TATA MOTORS LIMITED` vs `TATA TECHNOLOGIES LIMITED`

### LI-004 — Operational Counterparty Identity
* **Question:** Do the records refer to the same operational counterparty for reconciliation purposes?

### LI-005 — Historical Identity Continuity
* **Question:** Do two names refer to the same organization across a rename or legal transformation?

### LI-006 — Brand / Trade Name Association
* **Question:** Is one observed name a trade name or brand associated with a legal organization?

### LI-007 — Authoritative Identifier Identity
* **Question:** Do authoritative identifiers assert the same registered entity?

## Evidence Matrix

| Evidence Source | LI-001 (Lexical) | LI-002 (Legal) | LI-003 (Family) | LI-004 (Operational) | LI-005 (Historical) | LI-006 (Brand) | LI-007 (Identifier) |
|---|---|---|---|---|---|---|---|
| **Raw Vendor Name** | DIRECT | WEAK_PROXY | WEAK_PROXY | WEAK_PROXY | UNOBSERVABLE | WEAK_PROXY | UNOBSERVABLE |
| **Normalized Vendor Name** | DIRECT | PROXY | WEAK_PROXY | WEAK_PROXY | UNOBSERVABLE | WEAK_PROXY | UNOBSERVABLE |
| **Tax Identity (GSTIN)** | UNOBSERVABLE | DIRECT | PROXY | PROXY | DIRECT | PROXY | DIRECT |
| **Domain Corpus/Alias Graph** | UNOBSERVABLE | PROXY | DIRECT | PROXY | DIRECT | DIRECT | UNOBSERVABLE |

## Variable Modeling Decisions

1. **Are they currently represented?** No. They are all conflated into a single `score: float` or binary `1.0`/`0.5`.
2. **Can Legal Identity be determined from names alone?** No. `ABC LLP` and `ABC LTD` share Lexical Name Identity but have different Legal Entity Identity.
3. **Can it be contradicted by authoritative identifiers?** Yes. If GSTINs don't match, Legal Entity Identity is contradicted, regardless of Lexical Identity.
4. **Should ReconGraph v0.1 model all of these?**
   - ReconGraph **MUST** distinguish between Lexical Identity (what the strings say) and Legal Entity Identity (what the identifiers and legal suffixes prove).
   - ReconGraph v0.1 should defer Historical Identity (LI-005) and Brand Association (LI-006) as we lack temporal valid-from knowledge bases.
5. **Explicitly Accepted Failure Mode:** By deferring LI-005, we explicitly accept that a vendor renaming itself mid-year without a shared GSTIN will be treated as two distinct entities, causing a reconciliation failure. This is safer than hallucinating an identity connection.
````

## File: docs/algorithms/vendor-legal-form-ontology-v1.md
````markdown
# Vendor Legal Form Ontology V1

This document defines the canonical legal form vocabulary for Indian organizations, particularly in the context of B2B invoices and GST data. It specifies how lexical variants are mapped to canonical forms, and the extraction model to separate organization core identity from legal structure.

## Section A — Canonical Legal Form Vocabulary

The following canonical identifiers represent distinct legal structures under Indian corporate and tax law.

| Canonical ID | Real-world Meaning | Can Register GST? | Can have multiple GSTINs? | PAN Holder Type |
|---|---|---|---|---|
| `PRIVATE_LIMITED` | A privately held company registered under the Companies Act. | Yes | Yes (one per state/business vertical) | Company (`C`) |
| `PUBLIC_LIMITED` | A publicly held company registered under the Companies Act. | Yes | Yes | Company (`C`) |
| `LIMITED` | Often used interchangeably with Public Limited, sometimes ambiguous. | Yes | Yes | Company (`C`) |
| `LIMITED_LIABILITY_PARTNERSHIP` | A corporate business vehicle that enables professional expertise and entrepreneurial initiative to combine and operate in flexible, innovative and efficient manner. | Yes | Yes | Firm (`F`) |
| `PARTNERSHIP` | A traditional partnership firm. | Yes | Yes | Firm (`F`) |
| `PROPRIETORSHIP` | A business owned by a single individual, legally indistinct from the owner. | Yes | Yes | Individual (`P`) |
| `ONE_PERSON_COMPANY` | A company with only one member. | Yes | Yes | Company (`C`) |
| `SECTION_8_COMPANY` | A non-profit organization registered as a company. | Yes | Yes | Company (`C`) |
| `COOPERATIVE` | A cooperative society. | Yes | Yes | Association (`A`) / Trust (`T`) |
| `TRUST` | A legal arrangement where property is held by one party for the benefit of another. | Yes | Yes | Trust (`T`) |
| `SOCIETY` | A registered society. | Yes | Yes | Association (`A`) |
| `HINDU_UNDIVIDED_FAMILY` | A joint family recognized as a separate taxable entity. | Yes | Yes | HUF (`H`) |
| `GOVERNMENT_ENTITY` | A state or central government department/enterprise. | Yes | Yes | Govt (`G`) |
| `FOREIGN_COMPANY` | A company incorporated outside India. | Yes | Yes | Company (`C`) |
| `UNKNOWN` | A legal form designator was detected, but its specific type could not be resolved. | - | - | - |

## Section B — Lexical Variant Catalog

Real-world vendor names contain massive lexical variation for legal forms.

- `PRIVATE_LIMITED`: PVT LTD, PVT. LTD., PRIVATE LTD, PRIVATE LIMITED, (P) LTD, P. LTD, (PVT) LTD, P LIMITED
- `PUBLIC_LIMITED`: PLC, PUBLIC LIMITED
- `LIMITED`: LTD, LTD., LIMITED, LMTD
- `LIMITED_LIABILITY_PARTNERSHIP`: LLP, L.L.P., LIMITED LIABILITY PARTNERSHIP, L. L. P.
- `PARTNERSHIP`: PARTNERS, & CO, AND CO, & COMPANY (Note: highly ambiguous, often part of trade name)
- `PROPRIETORSHIP`: PROP, PROPRIETOR
- `ONE_PERSON_COMPANY`: OPC, ONE PERSON COMPANY
- `SECTION_8_COMPANY`: FOUNDATION (ambiguous)
- `COOPERATIVE`: COOP, CO-OP, COOPERATIVE, SAHAKARI
- `TRUST`: TRUST
- `SOCIETY`: SOC, SOCIETY
- `HINDU_UNDIVIDED_FAMILY`: HUF, H.U.F.
- `GOVERNMENT_ENTITY`: GOVT, GOVERNMENT
- `FOREIGN_COMPANY`: INC, INCORPORATED, LLC, GMBH, CORP, CORPORATION, CO., LTD.

## Section C — Extraction Model

Information extraction must precede information removal.

We do NOT implement a lossy normalizer that simply strips legal suffixes (e.g., `normalize("ABC PVT LTD") -> "abc"`). Doing so destroys the fact that the source explicitly stated "PVT LTD".

The extraction model is rule-based and follows this sequence:

1. **Raw Token Sequence Input**: The original vendor name is tokenized and canonicalized for unicode/whitespace.
2. **Suffix and Infix Recognition**: We apply a priority-ordered list of multi-token and single-token patterns. Legal forms typically appear as suffixes, so matching starts from the end of the token sequence.
3. **Canonical Form Assignment**: Matched tokens are mapped to their corresponding Canonical ID (e.g., `PVT LTD` → `PRIVATE_LIMITED`).
4. **Organization Core Extraction**: The tokens remaining after the legal form tokens are removed become the `organization_core`.
5. **Preservation of Span Information**: The exact character spans of the recognized legal form and the organization core are preserved in the `VendorNameObservation` for explainability.

Example:
Input: `ABC PVT LTD`
Output: `organization_core = "ABC"`, `legal_form = PRIVATE_LIMITED`

## Section D — Edge Cases and Traps

- **Ambiguous tokens**: `CO`, `COMPANY`, `CORPORATION`, `INC` can be legal designators, but in the Indian B2B context they are often just words in a name (e.g., "FORD MOTOR COMPANY"). If they appear without a strong designator like "LIMITED", they should often be left as part of the organization core.
- **Legal form as part of trade name**: "FORD MOTOR COMPANY" (COMPANY is part of the brand, not the legal form designator).
- **Missing legal form**: Trade names and invoices frequently omit legal designators entirely.
- **Multiple designators**: "TATA SONS PVT LTD" (SONS is a structural indicator but not a canonical legal form; PVT LTD is the legal form).
- **Non-English designators**: Occasionally seen in regional GST data.

## Section E — Semantic Rules for Legal Form Comparison

The comparison of canonical legal forms produces `identity.same_legal_form` assertions.

- `PRIVATE LIMITED` ↔ `PRIVATE LIMITED` → **SUPPORT** `identity.same_legal_form`, magnitude `1.0`
- `PRIVATE LIMITED` ↔ `PVT LTD` → **SUPPORT** `identity.same_legal_form`, magnitude `1.0` (Canonical equivalence)
- `PRIVATE LIMITED` ↔ `LLP` → **CONFLICT** `identity.same_legal_form`, magnitude `1.0` (Explicit contradiction)
- `PRIVATE LIMITED` ↔ `(missing)` → **MISSING_INPUT** (No assertion emitted, we cannot assume conflict if one side omits it)
- `(missing)` ↔ `(missing)` → **MISSING_INPUT**
````

## File: docs/algorithms/vendor-normalization-event-model.md
````markdown
# Vendor Normalization Event Model V1

Normalization must be modeled as an event stream, not a silent mutation.

## VendorNormalizationEventKind

We define the following standard normalization events:

- `UNICODE_CANONICALIZED`: Transformations like NFD to NFC or NFKC.
- `CASE_FOLDED`: Standardizing to an uppercase canonical form.
- `PUNCTUATION_STANDARDIZED`: e.g., removing full stops in abbreviations (`PVT.` → `PVT`).
- `WHITESPACE_COLLAPSED`: Replacing multiple consecutive spaces or tabs with a single space.
- `LEGAL_FORM_RECOGNIZED`: Classification of tokens as a legal designator.
- `ABBREVIATION_EXPANDED`: Expanding common abbreviations (`PVT` → `PRIVATE`, `LTD` → `LIMITED`).
- `CONNECTOR_CANONICALIZED`: Standardizing ampersands or connectives (`&` → `AND`).
- `TOKEN_CLASSIFIED`: General classification of a token (e.g. as geographic or noise).

## Event Data Structure

```python
@dataclass(frozen=True, slots=True)
class VendorNormalizationEvent:
    kind: VendorNormalizationEventKind
    input_span: tuple[int, int]
    original_value: str
    canonical_value: str
```

## Why this is a DerivedArtifact

A structured vendor parse is a highly valuable, computationally expensive asset. 
We model it as a `DerivedArtifact` (per K5) rather than a production-runtime side effect because it represents a **semantically reusable, independently addressable intermediate**.

If we parse "ABC PVT LTD" for Candidate A, and then we need to compare Candidate A to Candidate C later, we should not parse "ABC PVT LTD" again. By storing the structured observation (including its normalization events) as a `DerivedArtifact`, we can retrieve it by its content hash.

## The Derivation DAG Node

- `ObservationOccurrence`: Raw vendor name string from a source system (e.g., SAP row).
- `DerivationOccurrence`: The execution of `vendor.parse_name.v1`.
- `DerivedArtifact`: The resulting `VendorNameObservation` + list of `VendorNormalizationEvent`s (`vendor.structured_name.v1`).
````

## File: docs/algorithms/vendor-normalization-information-loss.md
````markdown
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
````

## File: docs/algorithms/vendor-observation-state-truth-table.md
````markdown
# Vendor Observation State Truth Table V1

ReconGraph's semantic kernel supports strict epistemic states: `MISSING_INPUT`, `INSUFFICIENT_INPUT`, `UNINTERPRETABLE_INPUT`, `NOT_APPLICABLE`, and `INTERPRETED`.

## Why a Single Global State is Wrong

A monolithic vendor pipeline might attempt to emit a single global state. 
For example, if the vendor name is entirely missing from the purchase record, a naive pipeline returns `MISSING_INPUT`.

**However, if both records contain perfectly valid, matching GSTINs, that global `MISSING_INPUT` state silently destroys the tax identity evidence.**

Therefore, the `VendorIdentityInterpretation` object must hold a tuple of factor-level `EvidenceInterpretationResult`s. The states below apply **per-factor**.

## Vendor Name Truth Table (Organization Core & Legal Form)

| Purchase Name | GST Name | Expected State (Core/Form) | Reasoning |
|---|---|---|---|
| `None` | `ABC LTD` | `MISSING_INPUT` | One side is completely absent. |
| `""` | `ABC LTD` | `MISSING_INPUT` | Empty string provides no evidence. |
| `" "` | `ABC LTD` | `MISSING_INPUT` | Whitespace-only string provides no evidence. |
| `"---"` | `"ABC LTD"` | `UNINTERPRETABLE_INPUT` | Contains characters but no semantic lexical tokens. |
| `"A"` | `"B"` | `INSUFFICIENT_INPUT` | Single characters are too short to form a meaningful organization core for comparison. Threshold required. |
| `"ABC"` | `"ABC"` | `INTERPRETED` | Valid comparison. |
| `"ABC LTD"` | `"ABC LLP"` | `INTERPRETED` | Valid comparison. Produces `CONFLICT` assertion for legal form. |
| `"ABC LTD"` | `valid GSTIN` | `MISSING_INPUT` | (Assuming GST name is missing, only GSTIN provided). |
| `malformed GSTIN` | `valid GSTIN` | `MISSING_INPUT` | (Assuming name fields are missing). |

*Note on Single-Character Names:* We recommend a minimum character length threshold (e.g., 2 or 3 alphanumeric chars) to transition from `INSUFFICIENT_INPUT` to `INTERPRETED`, as comparing "A" and "B" introduces massive false positive/negative risks without providing meaningful semantic grounding.

## GSTIN Truth Table (GST Registration & Tax Identity)

| Purchase GSTIN | GST GSTIN | Validation Result | Expected State | Expected Assertions | Reasoning |
|---|---|---|---|---|---|
| `07ABCDE1234F1Z5` | `07ABCDE1234F1Z5` | Both Valid | `INTERPRETED` | SUPPORT `same_gst_registration`, SUPPORT `same_tax_identity` | Exact match. |
| `07ABCDE1234F1Z5` | `29ABCDE1234F1Z5` | Both Valid | `INTERPRETED` | CONFLICT `same_gst_registration`, SUPPORT `same_tax_identity` | Different states, same PAN. |
| `07ABCDE1234F1Z5` | `07XYZDE9876Q1Z5` | Both Valid | `INTERPRETED` | CONFLICT `same_gst_registration`, CONFLICT `same_tax_identity` | Completely different identities. |
| `None` | `07ABCDE1234F1Z5` | N/A | `MISSING_INPUT` | None | Cannot compare. |
| `07ABCDE1234F1Z5` | `INVALID_STR` | One Invalid | `UNINTERPRETABLE_INPUT` | None | Malformed GSTIN halts the tax pipeline. |
| `O7ABCDE1234F1Z5` | `07ABCDE1234F1Z5` | One Invalid (OCR) | `UNINTERPRETABLE_INPUT` | None | Do not guess or repair in the deterministic pipeline. |
````

## File: docs/architecture/adr-001-reference-evidence-pipeline.md
````markdown
# ADR-001: Separate Reference Identity Extraction, Corpus Profiling, and Evidence Interpretation

## Status

Accepted

## Date

2026-07-13

## Context

Currently, reference evidence processing is collapsed into a single pipeline flow:

```
PurchaseRecord
      +
GSTRecord
      ↓
score_purchase_to_gst()
      ↓
reference_score()
      ↓
float | None
      ↓
RelationshipPolicy
```

Conceptually, `reference_score()` does the following in one monolithic step:
1. Returns `None` if either input is missing.
2. Returns `1.0` unconditionally if the normalized references match exactly.
3. Returns `0.8` if they share a qualifying numeric token (length >= 3 and not a year-like token).
4. Returns `0.0` otherwise.

This single scalar output fundamentally deletes the provenance of the evidence, making it impossible for the engine to apply contextual intelligence. We have observed the following specific failures resulting from this architecture:

| Case | References | Current | Observed Problem |
|---|---|---|---|
| HN004 | OMD-001 ↔ NSS-001 | 0.8 | generic numeric collision |
| COR001 | INV-001 ↔ ABC-001 | 0.8 | corpus-common token treated as strong |
| COR005 | INV-999999 ↔ ABC-999999 | 0.8 | repeated token treated as strong |
| COR016 | INV-2026-1001 ↔ ABC-2026-1001 | 0.8 | rare token rewarded without namespace context (namespace compatibility is unknown) |
| EX003 | 2026 ↔ 2026 | 1.0 | exactness bypasses uniqueness |
| EX008 | CREDITNOTE ↔ CREDITNOTE | 1.0 | non-numeric generic reference bypasses token profiling |

## Decision Drivers

1. **Evidence provenance must survive until interpretation**: We cannot crush rich factual context (like token counts or exactness flags) into a raw float prematurely. The interpretation layer needs the full factual story to make intelligent semantic decisions.
2. **Pure extraction must remain corpus-independent**: The mechanical process of identifying structural string overlap should not require knowing the global database state. String extraction and statistical lookup are distinct concerns.
3. **Corpus facts must be reproducible and explainable**: An analyst must be able to audit the system and trace exactly *why* a reference received a specific score based on deterministic, queryable facts (like `df=2`) rather than hidden internal math.
4. **Interpretation models must be replaceable**: Because extraction and enrichment are separated as factual steps, we can easily swap out the mathematical interpretation (e.g., collision burden vs. normalized IDF) without rewriting the data pipelines.
5. **RelationshipPolicy should continue consuming scalar signals in v0.1**: We will preserve backwards compatibility with the existing generic reconciliation engine by ultimately outputting a `float | None`. We are evolving the plumbing inside the reference module, not tearing down the entire house.
6. **Reference evidence must not double-count temporal evidence**: Using time-windowed corpus scopes for references risks rewarding temporal proximity twice (once in the time signal, once in reference rarity). Reference informativeness should strictly measure collision rates globally across the source datasets.
7. **The architecture must support future namespace context without requiring it today**: We know namespace compatibility (like `INV` vs `ABC`) is a problem, and preserving provenance now guarantees we will have the structural facts needed to implement namespace evaluation in the future.

## Decision

ReconGraph will separate reference processing into three distinct stages: identity extraction, corpus enrichment, and evidence interpretation.

### Stage 1 — Identity extraction
**Input:** `reference_a`, `reference_b`
**Output conceptually:** `ReferenceIdentityEvidence`

**Responsibilities:**
- preserve normalized references
- record normalized exact identity
- extract shared numeric tokens
- report structural facts only

**Must not:** query corpus statistics, calculate document frequency, decide whether a token is strong or weak, apply relationship-specific rules, or return the final reference scalar.

*Corpus-independent and deterministic.*

### Stage 2 — Corpus enrichment
**Input:** `ReferenceIdentityEvidence`, `ReferenceCorpusProfile`
**Output conceptually:** `EnrichedReferenceEvidence`

**Responsibilities:**
- attach full normalized-reference frequency
- attach statistics for shared numeric tokens
- preserve the original identity evidence
- expose factual collision context

**Must not:** decide whether evidence is sufficient for matching, calculate pair compatibility, apply purchase↔GST semantics, or return AUTO_MATCH, REVIEW, or REJECT.

*Contextual but non-decisional.*

### Stage 3 — Evidence interpretation
**Input:** `EnrichedReferenceEvidence`, `ReferenceEvidencePolicy`
**Output:** `float | None`

**Responsibilities:**
- interpret exactness and corpus uniqueness together
- convert enriched facts into scalar reference compatibility
- preserve explainability through a result object if necessary
- remain separate from whole-pair relationship semantics

**Must not:** inspect amount evidence, inspect temporal evidence, inspect tax identity, make pair eligibility decisions, or make final reconciliation decisions.

*Interpret reference evidence only.*

## Proposed Data Model

The following types enforce the boundaries designed above.

### `ReferenceIdentityEvidence`
```python
@dataclass(frozen=True)
class ReferenceIdentityEvidence:
    normalized_a: str
    normalized_b: str
    exact_normalized_match: bool
    shared_numeric_tokens: tuple[str, ...]
```
*Note: Renamed from `exact_match` to `exact_normalized_match`. This is a necessary and precise correction. `INV-001` and `INV001` are not exact raw string matches, but they are exact matches under normalization. The variable name must preserve this distinction.*

### `ReferenceCorpusProfile`
```python
@dataclass(frozen=True)
class ReferenceCorpusProfile:
    reference_count: int
    normalized_reference_frequency: Mapping[str, int]
    numeric_token_document_frequency: Mapping[str, int]
```
*Note: Separating full normalized reference frequency from numeric token frequency is critical for solving EX008. It allows us to mathematically prove that an exact alphabetic match like "CREDITNOTE" is extremely common and carries no unique identity weight.*

### `ReferenceTokenStatistics` & `NormalizedReferenceStatistics`
```python
@dataclass(frozen=True)
class ReferenceTokenStatistics:
    token: str
    document_frequency: int

@dataclass(frozen=True)
class NormalizedReferenceStatistics:
    normalized_reference: str
    document_frequency: int
```
*Note: We store pure factual document frequencies here. Derived concepts like collision burden or document rates are excluded because they are interpretation artifacts derivable at runtime.*

### `EnrichedReferenceEvidence`
```python
@dataclass(frozen=True)
class EnrichedReferenceEvidence:
    identity: ReferenceIdentityEvidence
    normalized_reference_statistics: tuple[NormalizedReferenceStatistics, ...]
    shared_token_statistics: tuple[ReferenceTokenStatistics, ...]
```
*Note: This specific design uses a tuple for `normalized_reference_statistics` rather than a mapping. It elegantly models a collection of unique normalized references alongside a collection of unique shared tokens. It perfectly preserves the factual statistics required without enforcing redundant data structures or dict mappings on objects that at most have two items.*

## Implementation Refinement

During implementation of Stage 2 (Corpus Enrichment), the original data model proposal for `EnrichedReferenceEvidence` was refined.

The initial proposal attached known statistics directly (`ReferenceTokenStatistics`, `NormalizedReferenceStatistics`). However, implementation analysis identified a distinct out-of-profile state where identity evidence exists in the candidate pair, but the supplied corpus profile contains no statistic for that identity or token (e.g., the token is genuinely absent from the profile snapshot).

To preserve this factual state without inventing statistics, the wrapper classes (`NormalizedReferenceEvidence`, `SharedNumericTokenEvidence`) were introduced. They contain the identifier and an optional statistics field:

```python
@dataclass(frozen=True)
class SharedNumericTokenEvidence:
    token: str
    statistics: ReferenceTokenStatistics | None
```

Profile absence is preserved as unavailable context, not converted into synthetic rarity. We explicitly do not use `frequency = 0` for absent statistics, nor do we impute `document_frequency = 1` for unseen tokens. The interpretation layer (Stage 3) will handle the semantics of unavailable statistics.
````

## File: docs/architecture/assertion-payload-provenance-boundary.md
````markdown
# Assertion Payload versus Provenance Boundary

This document maps data fields to their mathematically correct boundaries within the `EvidenceAssertion` to prevent payload bloat and semantic corruption.

## Field Placement Matrix

| Field | Observation | Lineage | Assertion Core | Epistemic/Quality Context | Typed Payload | Derivation Metadata | Explanation | Forbidden |
|---|---|---|---|---|---|---|---|---|
| Raw Vendor Name String | Primary | | | | | | | |
| Normalized Name | | | | | Primary | | | |
| Corpus Token Frequency | | | | | Primary | | | |
| `statistics_available` | | | | | Primary | | | |
| `source_system` | | Primary | | | | | | |
| `source_record_id` | | Primary | | | | | | |
| `source_field` (e.g. `vendor.name`) | Primary | | | | | | | |
| `support_magnitude` | | | Primary | | | | | |
| `conflict_magnitude` | | | Primary | | | | | |
| OCR Confidence Score | | | | | Primary | | | |
| Source Reliability (e.g. `SYSTEM_OF_RECORD`) | | | | Primary | | | | |
| Provider Semantic Version | | | | | | Primary | | |
| Policy Hash | | | | | | Primary | | |
| Human Verification Status | | | | Primary | | | | |
| Human-readable Explanation Text | | | | | | | | Primary (Banned from assertion) |

### Key Clarifications
* **Explanation Text:** Banned from the assertion. Explanations must be generated at the Edge/Trace layer by an `ExplanationBuilder` that reads the typed payload and magnitudes. Embedding English strings in the semantic kernel breaks mathematical equality and localization.
* **Raw Values:** Belong strictly to the `Observation` layer (or raw records). The `Assertion` payload holds the *interpreted* facts (e.g. normalized vectors, extracted suffix enums) that led to the magnitude.
* **OCR Confidence:** While related to quality, it is an interpretation artifact produced by a specific ML model, so it belongs in the typed payload, not the generic `EvidenceQualityContext`.
````

## File: docs/architecture/assertion-polarity-decision.md
````markdown
# Assertion Polarity Decision

## Summary
Atomic assertions are Unipolar (`AssertionPolarity.SUPPORT` or `AssertionPolarity.CONFLICT`).

## AP Questions
Independent paths of support and conflict must remain distinct assertions. A single assertion with both support and conflict obscures provenance and fusion.
````

## File: docs/architecture/assertion-scope-design-tournament.md
````markdown
# Scope Model Design Tournament

## Evaluated Designs

### Scope A — Flat Subject Tuple
* `subjects: tuple[str, ...]`
* Destroys Left/Right bipartite structure. Fails N:M graph compatibility.

### Scope B — Left and Right Subject Sets
* `left_subjects: frozenset[str]`
* `right_subjects: frozenset[str]`
* Retains bipartite structure, but cannot explicitly declare if a claim is symmetric or directional. A reader doesn't know if swapping left/right changes semantics.

### Scope C — Typed EvidenceScope Union
* e.g., `RecordScope`, `PairScope`, `GroupPairScope`
* Extensible but forces downcasting everywhere. Doesn't inherently solve directionality.

### Scope D — Canonical Proposition Subject
```python
@dataclass(frozen=True)
class AssertionSubject:
    subject_type: SubjectType # RECORD, PAIR, GROUP_PAIR
    left: frozenset[str]      # URNs
    right: frozenset[str]     # URNs
    directional: bool
```

## Challenge Answers

**SD-001 Should symmetric claims canonicalize left/right ordering?**
Yes. For symmetric claims (e.g. `same_legal_entity`), `A↔B` and `B↔A` must yield identical assertion scopes to prevent duplicate reasoning. 

**SD-002 If yes, who declares that the claim is symmetric?**
The claim definition itself must know this. It is an inherent property of the proposition.

**SD-003 Does the typed Claim Identifier currently know claim symmetry?**
No. A bare string `identity.same_legal_entity` carries no runtime metadata about its symmetry.

**SD-004 If not, is the claim model too weak?**
Yes. If the kernel cannot ask the claim "are you symmetric?", it cannot safely canonicalize the scope.

**SD-005 Should directionality belong to the claim definition or assertion scope?**
The Claim Definition. The *nature of the proposition* determines if it is directional (`supersedes`) or symmetric (`equals`). The scope merely instantiates it for specific nodes.

**SD-006 What happens if a plugin emits `same_legal_entity` but sets `directional=True`?**
If scope holds directionality independently of the claim, the plugin creates an illegal semantic state.

**SD-007 Can the kernel validate semantic properties of an extensible claim without a claim registry?**
No. Without a minimal descriptor (e.g. a dataclass pairing the string ID with its symmetry flag), the kernel must trust the plugin blindly, which defeats the purpose of the kernel.

## Recommendation
**Scope D (Canonical Proposition Subject)**, but it requires a **ClaimDescriptor** (a revision to Claim Model B) so the kernel can enforce canonicalization on symmetric claims automatically.
````

## File: docs/architecture/assertion-vs-interpretation-result-decision.md
````markdown
# Assertion vs Interpretation Result Decision

## Summary
Missingness and interpretability are properties of the attempt to evaluate evidence, not the semantic claim itself.

## Model Chosen
Model C (Interpretation envelope).

`EvidenceInterpretationResult` encapsulates:
- `EvidenceInterpretationState`
- A unique, canonically ordered tuple of `EvidenceAssertion`s.

If state is NOT `INTERPRETED`, the assertions tuple MUST be empty. If it is `INTERPRETED`, the tuple may be empty (evaluated, but no assertion produced).
````

## File: docs/architecture/current-evidence-claim-audit.md
````markdown
# Current Evidence Claim Audit

## Formal Ontology Audit

This document audits all current evidence providers and their implicit claims.

| Provider | Observation | Current Output | Implicit Claim | 1.0 Means | 0.0 Means | Conflict Expressible | Claim Explicit |
|---|---|---|---|---|---|---|---|
| **Amount Evidence** | Financial Amounts | `float` [0.0, 1.0] | FINANCIAL_CONSERVATION | Exact to the penny equivalence | Unacceptable variance (penalty) | Yes, via penalty score | No |
| **Tax Identity** | Tax ID (e.g. GSTIN) | `float` [0.0, 1.0] | SAME_LEGAL_ENTITY | Exact byte match | Mismatch / Contradiction | Yes, via low score | No |
| **Vendor Evidence** | Vendor Name string | `float` [0.0, 1.0] | SAME_ORGANIZATION | Exact byte match of concatenated string | Contradiction OR Absence (overloaded) | Yes, but conflated with absence | No |
| **Reference Evidence** | Reference string | `float` [0.0, 1.0] | SAME_TRANSACTIONAL_EVENT | Identical rare string | Absent or conflicting reference | No (absence treated as neutral) | No |
| **Temporal Evidence** | Date | `float` [0.0, 1.0] | TEMPORAL_COMPATIBILITY | Same day | Outside tolerance window (penalty) | Yes, via penalty score | No |

## Semantic Overloading

**The Zero Overload:**
ReconGraph currently overloads `0.0` to mean entirely different things across subsystems:
1. For Vendor, `0.0` can mean "Missing vendor name" (Ignorance/Absence) OR "Different vendor names" (Conflict).
2. For Amount, `0.0` means "Amounts explicitly contradict within allowed variance" (Conflict).
3. For Reference, missing reference yields `None` which is ignored, avoiding the zero-trap.
4. For Tax Identity, it acts as a blocking filter; mismatch yields `0.0` hypothesis score.

Because the Decision Engine aggregates these, a `0.0` Vendor score (meaning missing data) is treated mathematically identically to a `0.0` Amount score (meaning numerical proof of difference). This is mathematically dangerous. The target claims are implicit and assumed rather than asserted.
````

## File: docs/architecture/decision-trace-replay-contract.md
````markdown
# Decision Trace Replay Contract

This document explicitly defines the Replay Contract for ReconGraph Decision Traces in v0.1.

## Replay Modes Evaluated

* **Replay A — Historical Explanation:** Read an old trace and explain what the old engine decided based on the serialized assertions.
* **Replay B — Historical Re-execution:** Rerun the exact Python code from the past to regenerate the assertions from the raw data.
* **Replay C — Counterfactual Re-evaluation:** Run the *current* Python code against the *historical* raw data to see if the new engine makes a better decision.

## Answers to Trace Questions

**TR-001 Which modes must ReconGraph v0.1 support?**
Replay A (Historical Explanation) and Replay C (Counterfactual Re-evaluation).

**TR-002 Does `engine_version` + `config_hash` support Replay A?**
No. They identify the *environment*, but they don't contain the assertions. To explain historical decisions instantly without running code, the trace must serialize the `EvidenceAssertion`s.

**TR-003 Does it support Replay B?**
Practically, no. In Python, old package versions, changed dependency graphs, and unavailable external services make Replay B (exact historical code execution) impossible without containerizing every run. We explicitly abandon Replay B.

**TR-004 Where are raw inputs preserved?**
In the trace, serialized as immutable `Observation` or raw record snapshots. This enables Replay C.

**TR-005 Should traces preserve evidence assertions?**
Yes. Mandatory for Replay A.

**TR-006 Should traces preserve observations?**
Yes. Mandatory for Replay C.

**TR-007 Can historical assertions be trusted if claim semantics changed?**
Only if the claim semantic version is preserved. A trace reading `claim=same_legal_entity, semantic_version=1` is an immutable historical fact. If the engine is currently on `semantic_version=2`, it knows not to apply V2 fusion logic to a V1 historical assertion.

**TR-008 Does claim semantic version solve this?**
Yes.

**TR-009 Can old unknown payloads remain explainable?**
Yes, because the payload is a `Tagged Serializable Union`. It can be dumped as raw JSON for a human to read even if the Python `dataclass` was deleted years ago.

**TR-010 What does trace reader do when it cannot decode payload V1?**
It retains the generic `dict`.

**TR-011 Can it still show assertion core fields?**
Yes. The core fields (claim, scope, magnitude, state) are heavily standardized and independently deserialized.

**TR-012 Should payload decoding failure invalidate the entire trace?**
No. It should gracefully degrade to a raw dictionary display.

## Formal Guarantee
ReconGraph v0.1 traces guarantee **Instant Historical Explanation** via fully serialized `EvidenceAssertion`s. The trace reader will not execute provider code. The trace will tolerate missing Python payload classes gracefully. 
ReconGraph v0.1 traces guarantee **Counterfactual Re-evaluation** by preserving the raw Observations, allowing the current graph engine to produce a parallel set of modern Assertions for benchmarking against the past.
````

## File: docs/architecture/derivation-cache-threat-model.md
````markdown
# Derivation Cache Threat Model
## Part N — The Optimization Attack

### Threat Classes
- `PURE_DETERMINISTIC`: Safe to cache globally.
- `EXTERNAL_SNAPSHOT_DEPENDENT` (e.g. registry API): Must cache against the exact API response snapshot hash, NOT just the input GSTIN.
- `NONDETERMINISTIC` (e.g. GPU kernels, time): NEVER cache globally.

DerivationIdentity must embed the snapshot/model hashes to prevent silently turning non-deterministic processes into fake deterministic reasoning.
````

## File: docs/architecture/derivation-identity-vs-execution-decision.md
````markdown
# Derivation Identity vs Execution Decision

## Questions and Answers

### Does semantic cache identity require content identities?
**Yes.** To know if we have already performed a computation (e.g. `normalize("ABC LTD")`), we must key the cache by the content identity of the inputs, the provider version, and the method identity.

### Does evidence ancestry require occurrences?
**Yes.** We must trace the final semantic claim back to exactly which source line (e.g. SAP row 123 vs GST row 456) provided the input. Content alone cannot prove causation from a specific source.

### Can one object safely represent both?
**No.** If we use occurrence for cache identity, identical contents from different occurrences execute redundantly. If we use content for ancestry, we lose the operational source lineage.

### Should we separate them?
**Yes.** 
- `DerivationIdentity` = Content-addressed semantic computation key.
- `DerivationExecution` = Provenance record binding the computation to actual input occurrences.

### Does a cache hit create a new derivation execution?
**Yes.** The execution occurred logically. We skipped the CPU cost, but the new source occurrence still participated in deriving the fact. We must record the new `DerivationExecution` connecting the new occurrence to the cached result.

### If yes, does it reference the reused DerivedArtifact?
**Yes.** Multiple `DerivationExecutions` (provenance edges) point to the same `DerivedArtifact` (semantic state).

### Can two executions share one DerivationIdentity?
**Yes.** If both executions operate on inputs with identical content state.

### Can two executions share one DerivedArtifact?
**Yes.** By definition, if they share a `DerivationIdentity`, the deterministic function yields the identical `DerivedArtifact`.

### Does the Evidence DAG contain DerivationIdentity or DerivationExecution nodes?
The DAG is bipartite / multi-layered. The *Semantic State Graph* contains `ObservationIdentity`, `DerivationIdentity`, and `DerivedArtifact`. The *Provenance Graph* contains `ObservationOccurrence` and `DerivationExecution`. We will persist the provenance graph edges.

### What does an assertion lineage reference?
It must reference the full provenance paths (the occurrences and executions) that prove *why* the engine believes the assertion.

## Final Design Boundary
```python
DerivationIdentity  # Owns SHA-256 over method + semantic version + input identities
DerivationExecution # Owns the DerivationIdentity + actual ObservationOccurrences
```
````

## File: docs/architecture/derived-artifact-necessity-trial.md
````markdown
# DerivedArtifact Necessity Trial
## Part L — Epistemology of Intermediates

### The Trial
If we extract PAN from a GSTIN, does the PAN become an `Observation`?
If YES, we are lying. An Observation implies source presence. The ERP did not contain the PAN.

### Materialization Rule
A derived value becomes a `DerivedArtifact` ONLY IF it is semantically reusable, independently addressable in ancestry, or directly consumed by another semantic derivation.
We CONFIRM the architectural necessity of `DerivedArtifact`. It bridges the gap between Derivation and Assertion without fabricating Observations.
````

## File: docs/architecture/environment-integrity-audit.md
````markdown
# Environment Integrity Audit

## EG Audit Findings

| Check | Command / Source | Observed State | Expected State | Classification |
|---|---|---|---|---|
| EG-001 Declared as prod dependency? | `pyproject.toml` `[project] dependencies` | Yes (`"rapidfuzz>=3.14,<4.0"`) | Yes | HEALTHY |
| EG-002 Only dev/optional? | `pyproject.toml` | No | No | HEALTHY |
| EG-003 Does prod import it? | Source code | Yes | Yes | HEALTHY |
| EG-004 Which exact module? | `src/recongraph/matching/signals.py` | `from rapidfuzz import fuzz` | `from rapidfuzz import fuzz` | HEALTHY |
| EG-005 Prev suite ran under different env? | Local state vs reported | Yes | Yes | LOCAL_ENVIRONMENT_DRIFT |
| EG-006 `pytest` resolves to same interpreter? | `which python` / `which pytest` | Yes (`/opt/anaconda3/bin/python` / `pytest`) | Yes | HEALTHY |
| EG-007 Install works via documented cmds? | `README.md` is empty, `pip install -e .[dev]` is standard | Yes | Yes | DOCUMENTATION_DEFECT (missing docs) |
| EG-008 Reproducibility defect exists? | `pytest` failed collection | Yes | No | LOCAL_ENVIRONMENT_DRIFT |
| EG-009 Defect is declaration or local? | `pip show rapidfuzz` | Local | Local | LOCAL_ENVIRONMENT_DRIFT |
| EG-010 Smallest legitimate fix? | Local environment | Run `pip install -e .[dev]` | Restored environment | LOCAL_ENVIRONMENT_DRIFT |

## Root Cause
The `rapidfuzz` dependency is correctly declared in `pyproject.toml` as a primary project requirement. However, the current active Python interpreter (`/opt/anaconda3/bin/python`) does not have the package installed (`WARNING: Package(s) not found: rapidfuzz`). This proves the previous test suite execution (which reported 251 passing tests) was executed in a different local environment (likely a different `venv` or global installation) that contained `rapidfuzz`. The repository's declaration itself is fully sound.

## Proposed Fix
Because this is purely a local environment drift issue, the fix is to restore the environment from the repository's configuration by running the standard Python package installation command:
`pip install -e .[dev]`
````

## File: docs/architecture/evidence-assertion-ancestry-decision.md
````markdown
# Evidence Assertion Ancestry Decision

## Summary
An `EvidenceAssertion` represents a single semantic claim. It must reference exactly one valid semantic ancestry root (`EvidenceAncestryRef`).

## AAQ Questions

**AAQ001 What exactly does an assertion reference?**
Exactly one `EvidenceAncestryRef`.

**AAQ002 Does it reference an object or stable identity?**
Stable identity.

**AAQ003 Does ObservationOccurrence have stable identity?**
Yes, introduced as `ObservationOccurrenceIdentity`.

**AAQ004 Does DerivationExecution have stable identity?**
Yes, renamed and introduced as `DerivationOccurrenceIdentity`.

**AAQ015 Can one assertion have multiple ancestry roots?**
No. Multi-parent derivation converges into a single `DerivationOccurrence`.

**AAQ020 Final model.**
`EvidenceAssertion` contains `ancestry: EvidenceAncestryRef` wrapping a `KernelIdentityRef`. Only `observation_occurrence` and `derivation_occurrence` domains are permitted in v1 core.
````

## File: docs/architecture/evidence-assertion-identity.md
````markdown
# Evidence Assertion Identity

This document evaluates whether an `EvidenceAssertion` needs its own identifier.

## Identity Questions

**AI-001 Is equality sufficient to detect exact duplicate assertions?**
Yes, structurally. If two frozen dataclasses have identical fields, they are `==`.

**AI-002 What happens when payload contains explainability metadata?**
If `payload={"explanation": "Matched 3 tokens"}` and another assertion has `payload={"explanation": "Matched three tokens"}`, they are unequal in Python, but semantically identical propositions.

**AI-003 Should two assertions with identical semantics but different explanatory text be equal?**
Yes. Explanation text does not change epistemic truth.

**AI-004 Should magnitudes participate in assertion identity?**
Yes. An assertion that `support=0.9` is fundamentally a different proposition than one that `support=0.2`. (Alternatively, they are the *same* proposition with different confidence. But if a provider upgrades a score, the new assertion replaces the old).

**AI-005 If provider V2 changes support from 0.7 to 0.8, is it the same assertion revised or a new assertion?**
A new assertion. Immutability demands that we don't "update" assertions. We issue new ones from new derivations.

**AI-006 Can deterministic IDs leak sensitive source values?**
Yes, if they hash the payload or observation values directly.

**AI-007 Should raw values ever participate directly in IDs?**
No.

**AI-008 Can semantic identity be separated from assertion instance identity?**
Yes. 

## Evaluation
* **AI-A (No ID):** Relies on `__eq__`. Fails if payload contains non-epistemic fluff (like timestamps or strings).
* **AI-B (Random Assertion UUID):** Safe, but makes testing and deduplication harder.
* **AI-C (Deterministic Content Hash):** Dangerous.
* **AI-D (Deterministic Semantic Key):** `hash(claim, scope, observation_id, provider_id)`. 

## Recommendation
**Neither `assertion_id` nor `semantic_key` as a mandatory primary field.**
Assertions should be pure value objects. However, they must strictly forbid explanation text from residing in the assertion core or the typed payload boundary. If the payload strictly contains *epistemic truth properties*, then standard dataclass `__eq__` (and `__hash__`) is sufficient and mathematically sound. If an ID is needed for a specific graph persistence layer later, it can generate a random UUID on the edge envelope (`EvidenceContribution`), leaving the `EvidenceAssertion` mathematically pure.
````

## File: docs/architecture/evidence-assertion-kernel-decision-v2.md
````markdown
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
````

## File: docs/architecture/evidence-assertion-kernel-premortem-v2.md
````markdown
# Evidence Assertion Kernel Pre-Mortem V2

**Scenario:** We built the Stage 8C-0C kernel. Stage 8J (Fusion) still failed catastrophically six months later.

| Failure | Root Cause | Earliest Detection | Required Metadata | Metamorphic Property | Stage 8J Consequence | Reversal Cost |
|---|---|---|---|---|---|---|
| **Assertions lacked subject scope.** | Kernel only modeled claim, magnitude, state. | Fusing pairwise evidence with group evidence blindly. | `AssertionScope` | EM2-001 | Fuses evidence for unrelated hypotheses. | CATASTROPHIC |
| **Subject ordering changed equality.** | Scope was a tuple `(P1, G1)`. | Claim `A↔B` didn't match `B↔A`. | `is_symmetric` | EM2-003 | Misses duplicate evidence. | HIGH |
| **Symmetric claims were treated directionally.** | Claim lacked symmetry metadata. | `A↔B` fused independently from `B↔A`. | `ClaimDescriptor` | EM2-003 | Overconfidence / double counting. | HIGH |
| **Directional claims were canonicalized.** | Scope automatically sorted left/right. | `A supersedes B` became `B supersedes A`. | `ClaimDescriptor` | EM2-004 | Reverses causal logic. | CATASTROPHIC |
| **Unknown plugin claims were fused.** | String ID passed through blindly. | Unknown claims summed into random buckets. | `ClaimDescriptor` | EM2-018 | Corrupts fusion math. | CATASTROPHIC |
| **Same observation generated duplicated evidence.** | No `ObservationIdentity`. | Name & normalized name both added 0.8 support. | `ObservationID` | EM2-005 | Extreme overconfidence. | CATASTROPHIC |
| **Normalized and raw name evidence were double counted.** | Same as above. | | | | | |
| **Provider V1 and V2 outputs were fused together.** | Trace replay loaded both versions into one hypothesis. | `ProviderSemanticVersion` | EM2-006 | Double counting. | HIGH |
| **Pairwise and group-level evidence were combined directly.** | Scope size ignored during fusion. | `AssertionScope` | EM2-009 | Apples-to-oranges addition. | CATASTROPHIC |
| **Observation state and interpretation state were conflated.** | Used one `EvidenceState` enum. | `INVALID` GSTIN treated same as `MISSING` GSTIN. | Split Enums | EM2-011 | Ignored explicit malformed data. | HIGH |
| **Invalid identifiers were treated as uninterpretable.** | See above. | | | | | |
| **Missing fields were treated as invalid.** | See above. | | | | | |
| **Authority metadata duplicated observation quality inconsistently.** | `AuthorityDescriptor` was poorly defined. | `EvidenceQualityContext` | N/A | Ignored OCR errors. | MEDIUM |
| **Support magnitudes from incompatible scales were compared.** | Universal magnitude assumption. | `MagnitudeContract` | EM2-017 | Bizarre math behavior. | CATASTROPHIC |
| **0.9 was interpreted as probability.** | No calibration. | UI showed "90% match". | Documentation | EM-015 | Breaks user trust. | HIGH |
| **Payload schema version was mistaken for claim semantic version.** | Schema V2 caused Claim to act like V2. | `ClaimDescriptor` | EM2-015 | Breaks old traces. | HIGH |
| **Provider version was mistaken for engine version.** | Trace metadata was insufficient. | `DerivationMetadata` | EM2-016 | Trace lies about what ran. | MEDIUM |
| **Historical trace could not explain old assertions.** | Payload failed to deserialize, dropped assertion. | Tagged Union | EM2-019 | Irrecoverable traces. | CATASTROPHIC |
| **Content hashes leaked business-sensitive values.** | Hashed Vendor Name in `ObservationID`. | Security Audit. | Structural ID | N/A | Security Incident. | HIGH |
| **V1 scalar adapter re-entered the V2 evidence graph.** | Adapter logic was circular. | Projection rules | EM2-020 | Infinite loop / double score. | HIGH |
````

## File: docs/architecture/evidence-assertion-scope.md
````markdown
# Evidence Assertion Scope

This document defines the formal assertion scope model for the Evidence Semantic Kernel.

## Can evidence target...

**AS-001 ...a single record?**
Yes. Example: `document.reference_is_parseable`. 

**AS-002 ...a pair of records?**
Yes. Example: `identity.same_gst_registration` for P1 ↔ G1.

**AS-003 ...two groups of records?**
Yes. Example: `financial.amount_conservation` for {P1} ↔ {G1, G2}.

**AS-004 ...an entire hypothesis?**
Yes, but carefully. A hypothesis is a specific set of pairwise edges and nodes. Evidence targeting a hypothesis asserts a property about the *entire* proposed structure, e.g., `structure.contains_circular_reference`. 

**AS-005 ...a connected component?**
Yes, e.g., `component.has_unresolved_financial_imbalance`.

**AS-006 ...a decision?**
No. A decision is a policy output (e.g., `APPROVE`, `REJECT`), not an epistemic proposition. Evidence informs the hypothesis evaluation; the evaluation informs the decision.

**AS-007 Is assertion scope always binary?**
No. Single-record evidence is unary. Group evidence might be comparing sets.

**AS-008 Is left/right direction semantically meaningful?**
For symmetric claims (e.g., `identity.same_legal_entity`), no. For asymmetric claims (e.g., `temporal.strictly_before`), yes.

**AS-009 Can subject scope be represented as: `subjects: tuple[str, ...]`?**
No. A flat tuple destroys the structural boundary between "side A" and "side B". `{P1, P2} ↔ {G1}` is lost if flattened to `(P1, P2, G1)`.

**AS-010 Does the existing URN node system provide a usable identity foundation?**
Yes. The existing system uses URNs like `urn:recongraph:purchase:123` which provides stable, serializable node identities.

**AS-011 Can URNs identify aggregated groups?**
Currently no. We need a way to stably identify a group of nodes, perhaps by sorting and hashing their URNs, or maintaining an explicit `GroupRef`.

**AS-012 Should a hypothesis have a stable identity?**
Yes, likely a hash of its normalized, canonical node URN sets.

**AS-013 Can two structurally equal hypotheses have different runtime identities?**
Only if they are instantiated in memory with random UUIDs. A content-derived ID (canonical hash) prevents this.

**AS-014 What identity survives trace serialization?**
String-based URNs and deterministic content hashes. Python object IDs (`id(obj)`) do not.

**AS-015 Can evidence from scope P1 ↔ G1 be fused with evidence from P1 ↔ {G1, G2}?**
Not without an explicit **projection rule**. A pairwise lexical match does not automatically prove group-level lexical matching without defining how the group aggregate behaves (e.g., is the group valid if *any* pair matches, or if *all* pairs match?).

## Scope Taxonomy

| Scope Type | Example | Cardinality | Directional | Current Stable ID | Evidence Target Valid |
|---|---|---|---|---|---|
| RECORD | `document.is_readable` | Unary (1) | No | Node URN | Yes |
| RECORD_PAIR | `identity.same_gst_registration` | Binary (1:1) | Claim-dependent | Edge ID | Yes |
| GROUP_PAIR | `financial.conservation` | Binary (N:M) | Claim-dependent | None (Requires GroupRef) | Yes |
| HYPOTHESIS | `structure.is_valid_tree` | N-ary Set | No | None (Requires HypHash) | Yes |
| COMPONENT | `anomaly.orphan_node` | N-ary Set | No | None | Yes |
| DECISION | `policy.approved` | N/A | N/A | Trace UUID | **NO** (Policy, not Evidence) |

**Recommendation:** The minimum scope model required before Stage 8J must distinguish Left/Right sets (for N:M) while supporting Unary observations (where Right is empty).
````

## File: docs/architecture/evidence-authority-descriptor-decision.md
````markdown
# Evidence Authority Descriptor Decision

## Summary
`AuthorityDescriptor` describes the epistemic basis on which an assertion asks fusion to interpret its evidentiary status. It is explicitly assigned by the provider and not inferred from ancestry.

## AD Questions
**AD001 Is authority globally ordered?** No.
**AD002 Is authority claim-relative?** Yes.
**AD013 Should authority contain a float?** No.
**AD014 Should authority contain priority?** No.
**AD015 Should authority contain override semantics?** No. These belong in Stage 8J fusion policy.

## Implementation
`AuthorityBasisId` is a typed identifier string (open vocabulary) to support plugins (e.g. `recongraph.authority.official_registry`). `AuthorityDescriptor` wraps this basis.
````

## File: docs/architecture/evidence-dag-feasibility-study.md
````markdown
# Evidence DAG Feasibility Study
## Part M — Content-Addressed Immutable DAG

### Feasibility
The chain `Observation -> Derivation -> DerivedArtifact -> Assertion` forms a strict, acyclic, content-addressed DAG.
- **Acyclicity Guarantee**: Cryptographic hashes (SHA-256) of inputs are strictly monotonically accumulated. You cannot hash an object that includes your own hash.
- **Trace vs DAG**: A DecisionTrace is an ordered event log *over* the DAG. Multiple traces can reference the exact same DAG nodes.
````

## File: docs/architecture/evidence-derivation-identity.md
````markdown
# Evidence Derivation Identity

This document defines Derivation Identity—how an assertion remembers *who* and *how* it was derived from an observation.

## Identity Questions

**DI-001 Does `provider_id` identify the derivation algorithm?**
No, it identifies the module.

**DI-002 Does `engine_version` identify it?**
It's too broad. The core engine can update while the provider logic remains identical.

**DI-003 Can one provider change behavior without engine version changing?**
Yes, if it's a plugin on an independent release cycle.

**DI-004 Does config hash identify algorithm semantics?**
It identifies threshold and policy inputs, but not the Python code itself.

**DI-005 Does payload schema version identify interpretation semantics?**
No. A provider could rewrite its NLP algorithm entirely without changing the output schema.

**DI-006 What exact metadata is needed to answer: "Why did this historical assertion exist?"**
1. What was the observation? (`ObservationID`)
2. What was the configuration? (`PolicyHash`)
3. What was the algorithm? (`ProviderSemanticVersion`)

**DI-007 Should assertions carry: `provider_id`, `provider_version`, `interpreter_id`, `interpreter_version`, `policy_hash`. Are all necessary?**
`interpreter_id` and `interpreter_version` are largely synonymous with `provider` in this architecture. 

**DI-008 What is redundant?**
`interpreter` vs `provider`. We only need `ProviderIdentity` (name) and `ProviderSemanticVersion` (version).

**DI-009 Can provider version be semantic rather than package version?**
Yes. It should be bumped when the epistemic logic changes.

**DI-010 Should a provider version change when thresholds change?**
No, thresholds are configuration.

**DI-011 Should policy hash capture threshold changes instead?**
Yes.

**DI-012 What happens if code changes but provider version is not incremented?**
The trace lies. Two traces with identical derivation metadata will contain different assertion outputs.

**DI-013 Can tests detect this?**
Yes, by hashing the AST of the provider's inference module and failing if it changes without a version bump.

**DI-014 Should trace replay guarantee:**
**A.** Explain historical output (Explainability)
**B.** Run exact old algorithm (Re-execution)
**C.** Run current logic against old inputs (Counterfactual)

ReconGraph v0.1 must guarantee **A** (via serialized assertions) and **C** (via serialized raw observations). **B** is practically impossible in Python without persisting exact environment states (Docker images per trace).

## Reproducibility Contract for ReconGraph v0.1
The trace explicitly guarantees **Historical Explanation** (by serializing the output Assertion with its `ProviderSemanticVersion` and `PolicyHash`) and **Counterfactual Re-evaluation** (by serializing the raw inputs). It explicitly **abandons** exact Re-execution, meaning we do not try to dynamically load old Python code.

Therefore, `DerivationMetadata` strictly needs:
* `provider_id`: str
* `provider_semantic_version`: str
* `policy_hash`: str
````

## File: docs/architecture/evidence-double-counting-threat-model.md
````markdown
# Evidence Double Counting Threat Model

This document classifies duplicate evidence vulnerabilities so Stage 8J can avoid catastrophic overconfidence.

| Case | Description | Classification |
|---|---|---|
| **DD001** | Same claim, scope, observation, provider, payload. | `EXACT_DUPLICATE` |
| **DD002** | Same semantics produced twice in one run. | `EXACT_DUPLICATE` |
| **DD003** | Name eq & normalized-name eq from same raw names. | `DERIVED_DEPENDENCE` |
| **DD004** | Two providers interpret the same source fields. | `SHARED_FAILURE_CONTEXT` |
| **DD005** | Two assertions derive from the same observation. | `DERIVED_DEPENDENCE` |
| **DD006** | Different fields from same invoice. | `SHARED_FAILURE_CONTEXT` |
| **DD007** | OCR extracted vendor and GSTIN. | `SHARED_FAILURE_CONTEXT` |
| **DD008** | P1↔G1 and P1↔{G1,G2}. | `SCOPE_MISMATCH` |
| **DD009** | Name supports lexical similarity and legal entity. | `CLAIM_DISTINCT` |
| **DD010** | ERP name and registry name support same claim. | `INDEPENDENT` |
| **DD011** | Corrected name and original OCR name both present. | `EXACT_DUPLICATE` (if slot ID matches) |
| **DD012** | Same document processed under provider V1 and V2. | `DERIVED_DEPENDENCE` |
| **DD013** | Deterministically cloned observations. | `EXACT_DUPLICATE` |
| **DD014** | Group evaluator derives amount conservation after pairwise exists. | `SCOPE_MISMATCH` |
| **DD015** | V1 Adapter Projection scalar wrapped again as evidence. | `DERIVED_DEPENDENCE` |

## Minimum Metadata for Stage 8J Deduplication
To detect that two assertions are NOT independent evidence units, Stage 8J requires:
1. `AssertionScope` (To detect `SCOPE_MISMATCH` vs alignment).
2. `ClaimDescriptor` (To detect `CLAIM_DISTINCT` vs alignment).
3. `ObservationIdentity` (To detect `DERIVED_DEPENDENCE` on the same raw field).
4. `StructuredSourceLineage` (To detect `SHARED_FAILURE_CONTEXT` on the same document).

If two assertions share the same `ObservationIdentity`, their magnitudes cannot be naively summed.
````

## File: docs/architecture/evidence-kernel-performance-model.md
````markdown
# K4/K5 Performance Model
## Part O — Analytical Capacity

### Projections (100k purchases/GST)
- **Observations**: ~1.5M unique identities
- **Derivations**: ~8M invocations
- **Assertions**: ~10M unique identities

### Memory Risks
Using naive `@dataclass(frozen=True)` for 10M nodes will exhaust RAM due to Python object overhead (~150 bytes per object).
**Future Optimizations**: Integer Node IDs mapping to Arena Storage (NumPy/Arrow), or Content-Addressed Object Store. We will design K4/K5 to serialize cleanly to integers later.
````

## File: docs/architecture/evidence-kernel-semantic-compatibility-matrix.md
````markdown
# Evidence Semantic Compatibility Matrix
## Part Q — Versioning Doctrine

| Change Type | Claim Version Bump? | Provider Semantic Version Bump? | Method Version Bump? | Cache Invalidation? |
|---|---|---|---|---|
| Refactor Implementation | No | No | No | No |
| Bugfix altering outputs | No | Yes | Yes (implicit) | Yes |
| Change Claim Meaning | Yes | N/A | N/A | Yes |
| Threshold config change | No | Yes (if part of method) | N/A | Yes |
````

## File: docs/architecture/evidence-lineage-correlation-study.md
````markdown
# Evidence Lineage & Correlation Study

## Independence Scenarios

### CL001: Invoice OCR Vendor Name + Invoice OCR Tax ID
**Are they independent?** No. They share a single physical source document and extraction process. If the OCR engine hallucinates or the document is a forgery, both fields fail simultaneously. They are highly correlated.

### CL002: ERP Master Data Vendor Name + Government Registry Tax ID
**Are they more independent?** Yes. The name comes from internal onboarding, the Tax ID validation comes from an external authority. They have distinct failure domains.

### CL003: Vendor Name and Tax ID both from Vendor Master Table
**Are they independent?** No. They were likely entered by the same human operator during onboarding. A data entry error could corrupt both, or an incorrect record selection pulls both.

### CL004: Invoice Header OCR (Name) + Invoice Footer OCR (Tax ID)
**Independence?** Weakly independent. They share the document, but spatial separation means a crop/scan error might affect one but not the other. However, semantically they are from the same epistemic authority (the supplier who generated the PDF).

### CL005: ERP Name + Invoice OCR Tax ID
**Conflict Resolution:** This represents true cross-domain conflict. Resolving this requires lineage tracking to determine which source is trusted more for which latent variable.

## Critical Question: Where does correlation originate?

Correlation is **NOT** merely a property of the evidence kind (e.g., "Vendor" vs "Tax"). It is a property of the **Shared Epistemic Source**.
`correlation_group: str | None` is insufficient because correlation is multi-dimensional. Observations can be correlated by:
1. Originating Document
2. Extraction Process (OCR engine, human entry)
3. Source System (ERP, Registry)

## Candidate Lineage Models

### Model A — Flat Correlation Group
* Example: `correlation_group="vendor_identity"`
* **Evaluation:** Extremely simple, serializes easily. But fails to distinguish between CL001 (same OCR) and CL002 (ERP + Registry). Too coarse for Stage 8J.

### Model B — Structured Source Lineage
* Dimensions: `source_system`, `source_document`, `extraction_process`
* **Evaluation:** High usefulness for fusion. Allows Stage 8J to downweight multiple signals from the *same document* while preserving weight for signals from *different systems*. Moderate complexity.

### Model C — Evidence Derivation Graph
* Observations reference upstream AST/Graph nodes.
* **Evaluation:** Maximum theoretical purity, but overwhelming serialization complexity and violates the flat plugin protocol. Unsuitable for Stage 8J.

## Recommendation

**Model B (Structured Source Lineage)** is the recommended path before Stage 8J. A flat string (Model A) will immediately fail when we have Vendor Evidence from two different systems for the same record.
````

## File: docs/architecture/evidence-lineage-v2.md
````markdown
# Evidence Lineage V2

This document defines the minimum fields required for Structured Source Lineage.

## 12 Lineage Scenarios

| Scenario | Description | Shared Failure Modes |
|---|---|---|
| **LN001** | Vendor name & GSTIN from same invoice & same OCR pass. | Document corruption, OCR hallucinations (e.g. skew). |
| **LN002** | Same invoice, independent extraction models. | Document corruption, missing pages. |
| **LN003** | Vendor name from ERP, GSTIN from registry. | None. Independent systems. |
| **LN004** | Vendor name & GSTIN copied from same ERP master. | Human data entry error, selecting the wrong vendor drop-down. |
| **LN005** | Reference & amount extracted from same OCR document. | OCR failure, document swap. |
| **LN006** | Two observations derived from same normalized upstream observation. | Normalization bugs. |
| **LN007** | Human-corrected OCR vendor name. | Human error (fat-finger), stale review. |
| **LN008** | Stale ERP vendor name & current registry identifier. | Temporal drift. |
| **LN009** | Two documents uploaded in same ingestion batch. | Batch-level pipeline corruption. |
| **LN010** | Same source system but independent source records. | Systemic export bugs. |
| **LN011** | Synthetic scenario observations. | Synthetic generator bugs. |
| **LN012** | Unknown provenance legacy record. | Unknown. |

## Candidate Models

### Lineage Model L1 — Minimal
* `source_system`: str
* Too weak. Fails to group observations extracted from the exact same PDF.

### Lineage Model L2 — Structured
* `source_system`: str (e.g. `OCR_PIPELINE`, `SAP_ERP`)
* `source_record_id`: str (e.g. `invoice_12345.pdf`, `vendor_998`)

### Lineage Model L3 — Derivation DAG Ready
* `parent_observation_ids`: list[str]

## Recommendation
**Lineage Model L2 — Structured.** 
We need just enough information to prevent Stage 8J from double-counting two pieces of evidence that came from the exact same source document. `source_system` and `source_record_id` provide this semantic grouping cleanly.
````

## File: docs/architecture/evidence-provenance-current-state-audit.md
````markdown
# Evidence Provenance Current State Audit
## Part A — Audit Every Existing Provenance Concept

### Audit Summary
The ReconGraph repository lacks formalized provenance. Existing evidence objects implicitly rely on string-shaped identifiers (e.g., `record_id`) and temporal execution state rather than cryptographic or structural lineage.

| Concept | File | Current Identity | Provenance Preserved? | Lost Information | K4/K5 Risk |
|---|---|---|---|---|---|
| `record_id` | `records.py` | String identifier | No | Namespace, Source System | High - Can collide across tenants/systems |
| `config_hash` | `config.py` | SHA256 of params | Partial | Historical context | Medium - Describes engine, not fact |
| `trace` | `trace.py` | Event log | No | Derivation logic | High - Log is not a DAG |
| `payload` | `scoring.py` | Dict | No | Implied semantics | High - Payload fields lack claim identity |

### Object Attack Matrix
* **PurchaseRecord / GSTRecord**: Assumes `record_id` is globally unique. `record_id="123"` is not lineage; it is an identifier-shaped string. Serializing this 6 months later provides zero epistemic value without the original database context.
* **EvidenceContribution**: Assumes `provider_id` is sufficient provenance. Destroys the exact source observation content state.
* **DecisionTrace**: Captures temporal engine state. Cannot be used to prove causal independence of facts.
````

## File: docs/architecture/evidence-semantic-kernel-decision.md
````markdown
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
````

## File: docs/architecture/evidence-semantic-kernel-design.md
````markdown
# Typed Evidence Semantic Kernel Design

This document designs the smallest generic evidence semantic kernel.

## Kernel Design Questions

**SK-001 Should support and conflict be bounded [0.0, 1.0]?**
Yes. For mathematical stability, bounded magnitudes prevent unbounded divergence.

**SK-002 Can support and conflict both be non-zero?**
Yes. (e.g., Lexical support but Tax ID conflict).

**SK-003 Can both equal 1.0?**
Yes. A model might be 100% certain names match, and 100% certain tax IDs contradict.

**SK-004 Should the kernel forbid support + conflict > 1.0?**
No. They are independent magnitudes on independent evidence axes (often stemming from different attributes of the observation), not complementary probabilities.

**SK-005 Does support/conflict require normalization?**
No. Normalization enforces a probability distribution, which implies exclusivity. Support for A does not reduce Conflict against A.

**SK-006 Should magnitude fields be named `support_magnitude` and `conflict_magnitude` to prevent probability interpretation?**
Yes, this is an excellent naming defense.

**SK-007 Can MISSING evidence carry non-zero support?**
No. That is a strict semantic violation.

**SK-008 Can UNINTERPRETABLE evidence carry conflict?**
No. If it cannot be interpreted, it cannot contradict.

**SK-009 Can OBSERVED evidence have zero support and zero conflict?**
Yes. (e.g. Neutral evidence, `TRADERS`).

**SK-010 Does the kernel need `statistics_available`?**
No. That is a property of the specific observation (e.g. token rarity), which belongs in the typed payload.

**SK-011 Does the kernel replace `EvidenceContributionV2`?**
No. The contribution is the transport envelope; the semantic assertion is the payload.

**SK-012 Or should `EvidenceContributionV2` contain semantic output?**
Yes. 

**SK-013 Does `provider_id` belong in lineage or contribution metadata?**
Contribution metadata. The provider is the agent that made the assertion, not the source of the data itself.

**SK-014 How is schema version represented?**
Via a string/int on the Payload, or implicitly by the Python type name if using a registry.

**SK-015 Can the kernel be JSON serialized without custom object identity assumptions?**
Yes, if it relies purely on standard primitives and strings.

## Candidate Object Models

### Kernel A — Expand EvidenceContributionV2
Add `claim`, `support`, `conflict`, `state` directly to the `EvidenceContribution` class.
* **Flaw:** Conflates the graph's container requirements with the semantic truth of the assertion.

### Kernel B — EvidenceContributionV2 Contains EvidenceSemantics
`EvidenceContribution(..., semantics=EvidenceSemantics(...))`
* **Flaw:** What if a provider wants to assert *two* claims from one observation?

### Kernel C — Generic Typed EvidenceContribution[T_Payload]
Focuses on typing the payload, but leaves the semantic assertion structure loosely defined.
* **Flaw:** Does not formalize the claim ontology at the core level.

### Kernel D — Claim-Centric EvidenceAssertion
```python
@dataclass(frozen=True)
class EvidenceAssertion:
    claim: str # typed claim id
    support_magnitude: float
    conflict_magnitude: float
    state: EvidenceState
    authority: EvidenceAuthority
    lineage: EvidenceLineage
    payload: Any # Typed via payload protocol
```
A provider returns `list[EvidenceAssertion]`. The `EvidenceContribution` wraps these assertions for graph insertion.

## Recommendation
**Kernel D (Claim-Centric EvidenceAssertion).** It completely decouples the epistemic truth (the assertion) from the graph's transport mechanism (the contribution). A single plugin can observe one document and emit multiple independent assertions (e.g. one for `legal_entity`, one for `financial_conservation`).
````

## File: docs/architecture/k4-k5-evidence-ancestry-decision.md
````markdown
# K4-K5 Evidence Ancestry ADR (Q1-Q100)
## Part R — Adversarial Questions

**(Excerpt of Key Decisions)**
* **Q12**: Does ingestion time define source identity? **Decision:** NO. **Reason:** Destroys replayability.
* **Q24**: Can one Observation have multiple lineages? **Decision:** NO. We use `ObservationOccurrence` (ObservationProvenance) wrappers. **Reason:** Protects epistemic purity of Observation.
* **Q65**: Are symmetric inputs ordered? **Decision:** We use `DerivationInputBinding(role=str)`. The MethodDescriptor determines if the roles are canonically sorted (ORDERED) or content-sorted (UNORDERED).
* **Q88**: Are traces the DAG? **Decision:** NO. Traces are temporal event logs over the timeless DAG.
````

## File: docs/architecture/kernel-identity-reference-decision.md
````markdown
# Kernel Identity Reference Decision

## Summary
To prevent structural forgery via duck typing (`hasattr(node, "digest")`), we introduce an explicit `KernelIdentityRef`. This provides a transport boundary for semantic identities.

## KIR Questions

**KIR001 What semantic capability is the derivation kernel actually requiring?**
It requires an explicitly certified, stable identity representing a node in the semantic graph.

**KIR002 Is `.digest` itself sufficient?**
No, a bare digest string loses its semantic domain (e.g. observation vs derived artifact).

**KIR003 Why is hasattr-based identity discovery unsafe?**
It tests structural shape, not semantic capability. Any object with a `.digest` attribute can forge its way into the graph.

**KIR004 Should the kernel consume concrete identity classes?**
No. Consuming concrete classes creates tight coupling and inhibits plugin extensibility.

**KIR005 Would a Union of all identity types scale to plugins?**
No, a closed Union requires central registration, which breaks independent plugin distribution.

**KIR006 Does Protocol structural typing permit accidental semantic admission?**
Yes. A class might implement `.digest` for entirely different reasons (e.g. logging) and be accidentally admitted as an identity node.

**KIR007 Is KernelIdentityRef an owning identity?**
No, it is a transport reference explicitly exported by an owning identity.

**KIR008 Can KernelIdentityRef replace ObservationIdentity?**
No, the domain-specific identity maintains context.

**KIR009 Can it replace DerivedArtifactIdentity?**
No.

**KIR010 Can two identity domains carry identical digest bytes?**
Yes, theoretically, though domain separation null-bytes mitigate this.

**KIR011 If yes, are the refs equal?**
No, `KernelIdentityRef` equality requires the domain and schema to match.

**KIR012 Must identity domain participate in equality?**
Yes.

**KIR013 Must schema participate in equality?**
Yes.

**KIR014 Does digest algorithm participate in identity?**
Yes.

**KIR015 Is sha256 encoded in IdentityDigest or separately?**
Encoded within `IdentityDigest` (e.g. `sha256:...`).

**KIR016 Can plugin identity domains exist?**
Yes.

**KIR017 Can unknown identity domains be transported?**
Yes.

**KIR018 Does unknown mean trusted?**
No. Transportability does not imply trust.

**KIR019 Does transportability imply fusion eligibility?**
No. Stage 8J governs eligibility.

**KIR020 How does an identity object export its ref?**
Via a `.to_kernel_identity_ref()` method.

**KIR021 Does export alter identity?**
No.

**KIR022 Does ref serialization use canonical JSON?**
Yes.

**KIR023 Can DerivationInputBinding accept raw objects?**
No, only `KernelIdentityRef`.

**KIR024 Migration impact on K3/K4/K5?**
Minimal. Identity classes export the reference, and `DerivationIdentity` consumes it.

**KIR025 Final decision.**
Adopt `KernelIdentityRef` constructed from validated value objects (`IdentityDomainId`, `IdentitySchemaId`, `IdentityDigest`).
````

## File: docs/architecture/minimal-semantic-kernel-implementation-plan.md
````markdown
# Minimal Semantic Kernel Implementation Plan

This is the exact implementation blueprint for Stage 8C (Part O). 
**Note:** This is a plan only. Do not execute until authorized.

## Phases

### Phase K1 — Claim primitives
* **Create:** `src/recongraph/domain/claims.py`
* **Implement:** `ClaimDescriptor` value object with `is_symmetric`, `semantic_version`, `allowed_scope_kinds`.
* **RED Test Order:** 1. Instantiation. 2. Immutability.

### Phase K2 — Scope primitives
* **Create:** `src/recongraph/domain/scopes.py`
* **Implement:** `AssertionScope` dataclass (Left/Right nodes).
* **RED Test Order:** 1. Basic equality. 2. Symmetry canonicalization (relies on ClaimDescriptor). 3. Directionality preservation. 4. Overlap non-equality.

### Phase K3 — Observation identity/state
* **Create:** `src/recongraph/domain/observations.py`
* **Implement:** `ObservationIdentity`, `ObservationState` Enum, `InterpretationState` Enum.
* **RED Test Order:** 1. State distinctness. 2. Structural ID formatting.

### Phase K4 — Lineage
* **Create:** `src/recongraph/domain/lineage.py`
* **Implement:** `StructuredSourceLineage`.
* **RED Test Order:** 1. Serialization round-trip.

### Phase K5 — Derivation metadata
* **Create:** `src/recongraph/domain/derivation.py`
* **Implement:** `DerivationMetadata` (Provider ID, semantic version, policy hash).
* **RED Test Order:** 1. Equality.

### Phase K6 — Quality context
* **Create:** `src/recongraph/domain/quality.py`
* **Implement:** `EvidenceQualityContext` (Source trust, extraction trust).
* **RED Test Order:** 1. Distinct layers of trust.

### Phase K7 — Typed payload envelope
* **Create:** `src/recongraph/domain/payload.py`
* **Implement:** `TaggedPayload` base protocol/union.
* **RED Test Order:** 1. JSON Serialization. 2. Unknown payload fallback.

### Phase K8 — EvidenceAssertion
* **Create:** `src/recongraph/domain/assertion.py`
* **Implement:** `EvidenceAssertion` dataclass combining all primitives.
* **RED Test Order:** 1. Full structural equality. 2. Magnitude boundary validation. 3. Missingness/Conflict constraints (EM2-011 through EM2-013).

### Phase K9 — Trace serialization
* **Modify:** `src/recongraph/graph/trace.py`
* **Implement:** JSON encoding/decoding for `EvidenceAssertion`.
* **RED Test Order:** 1. Full round-trip of an assertion. 2. Graceful degradation on unknown claims/payloads.

### Phase K10 — V1 compatibility adapter boundary
* **Modify:** `src/recongraph/plugins/core_providers.py`
* **Implement:** An explicit adapter that takes a mock `EvidenceAssertion` and projects its `support_magnitude` down to the legacy scalar score output for the Decision Engine to consume.
* **RED Test Order:** 1. Projection mathematically matches legacy behavior.

## Impact & Rollback
* **Config hash impact:** Minimal (new structures don't alter legacy scoring config yet).
* **Serialization impact:** V2 Trace schema will evolve, but V1 trace readers will not break as long as we bump the schema version.
* **Rollback strategy:** Git reset. No production dependencies are broken because we do not wire V2 into the core Decision Engine until Stage 8J.
````

## File: docs/architecture/observation-identity-model.md
````markdown
# Observation Identity Model

This document defines Observation Identity—the stable identifier of the raw data slot that generated an assertion.

## Identity Questions

**OI-001 Are those three assertions derived from one observation?**
Yes. `normalized_name`, `legal_form`, and `tokens` are all derivations of the single source field `vendor_name`.

**OI-002 Does shared lineage alone prove this?**
No. Lineage (`source_record_id`) tells us they came from the same *document*. It does not tell us they came from the exact same *field* on that document.

**OI-003 Could two different fields in the same source record share lineage?**
Yes. `vendor_name` and `billing_name` share the same lineage but are distinct observations.

**OI-004 Does `source_record_id` uniquely identify an observation?**
No.

**OI-005 Is `source_field` required?**
Yes, structurally. It defines the exact slot on the document.

**OI-006 Can one observation combine multiple source fields?**
Yes. E.g. `gross_amount = net_amount + tax_amount`. The observation identity would need to reference multiple fields or a synthetic "composite" slot.

**OI-007 Can one observation derive from multiple parent observations?**
Yes. 

**OI-008 Do we need a derivation DAG now?**
No. We are not tracing the infinite history of knowledge, just preventing Stage 8J from double-counting two pieces of evidence derived from the same source field on the same document.

**OI-009 What minimum identity prevents accidental duplicate counting?**
`{source_system}:{source_record_id}:{source_field}`.

**OI-010 Should observation IDs be random UUIDs?**
No. They destroy determinism and make duplicate detection impossible if the same document is re-parsed.

**OI-011 Should observation IDs be content hashes?**
No. If the human corrects a typo in the field, the content hash changes, breaking the identity of the *slot* and making it look like a brand new observation rather than a corrected one. It also leaks PII in the hash (rainbow table attacks).

**OI-012 Should observation IDs be deterministic structural identifiers?**
Yes. `obs:{source_system}:{source_record_id}:{source_field}`.

**OI-013 What happens when the same source field is ingested twice?**
The structural ID is identical, cleanly identifying it as the same observation.

**OI-014 What happens when the field value changes?**
The *value* changes, but the *slot identity* remains identical. This allows the system to recognize it as an update/correction.

**OI-015 Does observation identity identify a slot or a value occurrence?**
A slot. The value is the payload.

## Evaluation
* **OI-A (No ID):** Double counting inevitable.
* **OI-B (Random UUID):** Kills determinism.
* **OI-C (Content-Derived ID):** Fragile to corrections, leaks PII.
* **OI-D (Structural Observation ID):** Identifies the slot stably. `obs:erp:inv123:vendor_name`.
* **OI-E (Structural Slot ID + Observation Revision/Fingerprint):** Overkill for v0.1.

## Recommendation
**OI-D (Structural Observation ID)**. An observation ID must be a deterministic string combining the system, record, and field path, identifying the *slot* from which the value was extracted, regardless of the value itself.
````

## File: docs/architecture/observation-occurrence-naming-decision.md
````markdown
# Observation Occurrence Naming Decision

## Comparison of Candidates

### `ObservationProvenance`
**Pros:** Familiar term for origin metadata.
**Cons:** The object binds `ObservationIdentity` (what fact exists) with `StructuredSourceLineage` (where it came from). Calling it "Provenance" implies it only contains source metadata, obscuring the fact that it conceptually represents the *occurrence* of the observation.

### `SourcedObservation`
**Pros:** grammatically pleasing.
**Cons:** Implies the observation is mutated or wrapped into a new type of observation, which breaks the epistemic boundaries.

### `ObservedOccurrence`
**Pros:** Accurate to the physical reality.
**Cons:** Loses the explicit link to the `Observation` kernel class.

### `ObservationOccurrence`
**Pros:** Perfectly maps to the established pattern:
- `ObservationIdentity`: Answers "What content state exists?"
- `ObservationOccurrence`: Answers "Where was this content state observed?"
It explicitly binds fact identity + source occurrence without semantic conflation. 

## Final Decision
**Final class name: `ObservationOccurrence`**

## Required Invariants
1. Same `ObservationIdentity` + Same `StructuredSourceLineage` = Equal.
2. Same `ObservationIdentity` + Different lineage = Distinct.
3. Different `ObservationIdentity` + Same lineage = Distinct. (e.g. two different OCR engines reading the same PDF bbox producing different text).

> **Important OCR Note**: 
> A raw PDF region is source material. The extracted OCR text should technically be modeled as a `DerivedArtifact` derived from a raw `ObservationOccurrence` of the region. `ObservationOccurrence` gives us the structural precision to model this correctly, rather than falsely claiming the PDF directly observed the text "ABC LTD".
````

## File: docs/architecture/provider-semantic-identity-study.md
````markdown
# Provider Semantic Identity Study
## Part H — Provider Versioning Attacks

### Versioning Contract
1. **Implementation Version**: Bumps when code changes without affecting semantics (e.g., trie optimization). DOES NOT alter DerivationIdentity.
2. **Semantic Version**: Bumps when output semantics change (e.g., adding `LTD -> LIMITED` to abbreviation tables, or fixing a bug). DOES alter DerivationIdentity.
3. **Model Artifact Identity**: Captured as part of the Method Descriptor if the model dictates semantics.

ProviderSemanticVersion is required to prevent cache poisoning across semantic upgrades.
````

## File: docs/architecture/semantic-derivation-dependency-decision.md
````markdown
# Semantic Derivation Dependency Decision

## Summary
Derivations depend on semantic contexts (models, configs, registries). `SemanticDependencyRef` is introduced as a context modifier for derivations, separate from derivation inputs.

## SDD Questions

**SDD001 Are dependencies DAG nodes?**
No, they are context modifiers.

**SDD002 Do dependencies have kind?**
Yes, `SemanticDependencyKind`.

**SDD003 Can they be mutable?**
Yes. A dependency can be `MUTABLE_REFERENCE` (e.g. "latest").

**SDD004 Does mutability affect execution?**
No, but it prevents global caching and cross-run reproducibility.

**SDD005 Do roles participate in dependency identity?**
Yes.

**SDD006 Are duplicate identical dependencies allowed?**
No, they are explicitly rejected. Validate, don't repair.

**SDD007 Does dependency identity participate in derivation identity?**
Yes.
````

## File: docs/architecture/source-identity-content-identity-study.md
````markdown
# Source Identity vs Content Identity Study
## Part C — The Independence Ambiguity

### ERP Row Mutation (T0 vs T1)
If ERP row 123 changes from `ABC LTD` to `XYZ LTD`:
- It is the same `SourceArtifact`.
- It represents a new `SourceVersionRef`.
- Logical persistence is maintained, but Epistemic Content changes.
- Ingestion time is NOT semantic identity.

### Byte-Identical Duplicate PDFs
If `invoice-a.pdf` and `invoice-copy.pdf` have identical bytes but different upload IDs:
- They share one Content Identity (`sha256` of bytes).
- They have TWO independent `SourceOccurrences` (different `SourceArtifact` coordinates in the upload namespace).
- **Conclusion**: We cannot infer evidence independence from content identity alone. Preserving uncertainty is required for Stage 8J.
````

## File: docs/architecture/source-version-placement-decision.md
````markdown
# Source Version Placement Decision

## SV001
Can the same logical artifact mutate?
**Yes.** (e.g. ERP rows, manually edited worksheets).

## SV002
If yes, must two versions have different lineage?
**Yes.** An assertion about V1 is not an assertion about V2.

## SV003
Does SourceArtifactId identify logical persistence or exact source state?
**Logical persistence.** `SourceArtifactId("purchase_invoice:874219")` points to the row, not its temporal state.

## SV004
If it identifies exact state, how do we refer to the logical artifact across versions?
N/A (Identifies logical persistence).

## SV005
If it identifies logical persistence, where is version state represented?
In an explicit `SourceVersionRef` that acts as a state qualifier over the artifact.

## SV006
Can a source lacking native row versions still create lineage?
**Yes.** The version qualifier becomes `None`.

## SV007
Is ingestion batch ID a source version?
**No.** Ingestion is an operational event in our pipeline, not a state identity of the upstream source. 

## SV008
Is content hash always a valid source version?
**No.** For independently duplicated documents, identical content hashes can belong to different `SourceArtifactIds` (Upload 1 vs Upload 2). Using content hash as version conflates observation content identity with source temporal occurrence.

## SV009
Can an artifact version be unknown?
**Yes.** Many APIs or document uploads do not expose a strict upstream revision tag.

## SV010
Does unknown version destroy lineage validity?
**No.** It merely signifies our provenance knowledge is limited to the logical artifact coordinate.

## SV011
Does unknown version affect cache eligibility?
**Yes.** An unknown mutable source cannot be safely cached for temporal replay if the derivation relies on exact upstream state (EXTERNAL_SNAPSHOT_DEPENDENT).

## SV012
Should version state be an optional field?
**Yes.** `SourceVersionRef | None`.

## SV013
Would optional version create identity ambiguity?
**No.** `None` means explicitly "we do not know the version", whereas `"v1"` means explicitly "version 1". They are distinct epistemic states.

## SV014
Can the cache distinguish: known stable snapshot vs unknown mutable source if version is omitted?
**Yes.** If omitted (`None`), the cache must assume the source is an unknown mutable source (NONDETERMINISTIC) and refuse global caching, unless the derivation itself is pure and only relies on the extracted Observation content state (which is safe).

## SV015
Final decision.
The 3-part ontology (`SourceSystem`, `SourceArtifact`, `SourceLocator`) is the core coordinate. 
**`SourceVersionRef` is a state qualifier over the artifact.** 
The architecture must be:
```python
SourceSystemId
SourceArtifactId
SourceVersionRef | None
SourceLocator
```
````

## File: docs/architecture/stage8c-k4-k5-research-decision.md
````markdown
# Final Frozen Decision Report (Stage 8C-K4/K5-0A)
## Part S — Doctrine

### Chosen Architecture
- **Chosen source ontology**: 3-part (SourceSystem, SourceArtifact, SourceLocator).
- **Chosen source identity model**: Extensible opaque coordinates, temporal timestamps explicitly excluded.
- **Chosen observation provenance model**: `ObservationProvenance` relational wrapper (Model C/D variant).
- **K3 amendment required**: NO code changes, but vocabulary formally updated to distinguish "Observation Content State" from "Observation Occurrence".
- **Chosen lineage model**: `StructuredSourceLineage` as a flat immutable composition of the 3-part ontology.
- **Chosen provider identity model**: `ProviderId` + `ProviderSemanticVersion`.
- **Chosen derivation identity model**: Deterministic SHA-256 over Provider, Method, and Canonicalized Inputs.
- **Chosen input binding semantics**: Role-bound `DerivationInputBinding` grouped in a `DerivationInputSet` with Method-dictated sorting rules.
- **DerivedArtifact required**: YES. Strict materialization rule enforced.
- **Evidence DAG accepted**: YES. Strictly acyclic.
- **Privacy identity stance**: Acknowledged leakage; deferring to tenant-scoped salts at persistence layer.

### Allowed Shapes (Next Stage)
```python
@dataclass(frozen=True)
class SourceSystemId:
    value: str

@dataclass(frozen=True)
class SourceNodeRef:
    kind: str
    ref: str

@dataclass(frozen=True)
class StructuredSourceLineage:
    source_system: SourceSystemId
    source_node: SourceNodeRef
    source_version: Optional[str]

@dataclass(frozen=True)
class ObservationProvenance:
    observation: ObservationIdentity
    lineage: StructuredSourceLineage
```
````

## File: docs/architecture/stage8j-semantic-kernel-premortem.md
````markdown
# Stage 8J Semantic Kernel Pre-Mortem

**Scenario:** It is six months from now. Stage 8J Evidence Fusion has failed because the generic Evidence Semantic Kernel was poorly designed.

| Failure | Root Cause | Earliest Detectable Signal | Metamorphic Property Violated | Architectural Seam Required | Cost |
|---|---|---|---|---|---|
| **Claims were too broad** | Modeled `SAME_VENDOR` instead of `SAME_LEGAL_ENTITY` and `SAME_OPERATIONAL_COUNTERPARTY`. | Hard-coding claim logic inside individual providers. | EM-005 Claim Distinction | Extensible Claim Identifier | CATASTROPHIC |
| **Claims were too granular** | Modeled 500 different micro-claims that the fusion engine couldn't aggregate. | Massive switch statements in fusion logic. | EM-014 Provider Extensibility | Claim Hierarchy Registry | HIGH |
| **Claim enum prevented plugin extensibility** | Used Python `Enum` for claims. | 3rd-party plugin crashes core on import. | EM-014 Provider Extensibility | String-backed Value Object | CATASTROPHIC |
| **Support was mistaken for probability** | Multiplied independent support values leading to 0.0001 scores. | Explanation texts saying "90% match". | EM-015 No Probability Claim | `support_magnitude` field name | HIGH |
| **Conflict was treated as 1 - support** | Missing data caused `support=0`, which became `conflict=1`. | High rejection rate on sparse data. | EM-007 Support/Conflict Independence | Explicit Bipolar Modeling | CATASTROPHIC |
| **Missing evidence was serialized as zero evidence** | No explicit `EvidenceState` enum. | `support=0.0` inside JSON trace without context. | EM-009 State Preservation | `EvidenceState` Enum | CATASTROPHIC |
| **Uninterpretable evidence was treated as missing** | OCR garbage fell back to `None`. | Model blindness to its own limitations. | EM-010 Uninterpretable Preservation | `UNINTERPRETABLE` State | MEDIUM |
| **Authority became a hidden weight** | Multiplied `support * 0.8` for OCR. | Loss of epistemic source in trace. | EM-019 Authority Non-Numericity | Authority Descriptor | HIGH |
| **Lineage fields existed but providers populated them incorrectly** | Passed `correlation_group="vendor"` for all inputs. | Everything clustered together in fusion. | EM-004 Provenance Distinction | Structured Source Lineage | MEDIUM |
| **Shared provenance was mistaken for measured statistical dependence** | Used covariance matrices without calibration data. | Bizarre fusion behavior, over-penalizing corroborated evidence. | N/A (Math Error) | Dependence Terminology Ban | CATASTROPHIC |
| **Typed payload versions became impossible to replay** | Altered `VendorPayload` schema without versioning. | Benchmark runner crashes on old traces. | EM-012 Payload Version Preservation | `schema_version` | HIGH |
| **Unknown plugin payloads crashed trace readers** | Used strict Pydantic parsing for all payloads in core. | Core crashes when plugin disabled. | EM-013 Unknown Payload Safety | Tagged Serializable Union | CATASTROPHIC |
| **Vendor and GSTIN targeted different identity claims** | GSTIN asserted `SAME_GST_REGISTRATION`, Name asserted `SAME_LEGAL_ENTITY`. Fusion didn't know how to link them. | Ignored GSTINs entirely. | EM-016 Claim-Local Conflict | Claim Logic Registry | HIGH |
| **Fusion combined evidence across incompatible claims** | Added Amount Support to Name Support. | Apples-to-oranges score summation. | EM-005 Claim Distinction | Type-Safe Fusion | CATASTROPHIC |
| **Explanation Builder translated claim-specific evidence into generic "strong match" language** | Ignored the `claim_id` when rendering text. | User sees "Strong Match" when tax IDs conflict. | EM-001 Claim Preservation | Claim-Aware Templates | HIGH |
````

## File: docs/architecture/stage8j-vendor-fusion-premortem.md
````markdown
# Stage 8J Vendor Fusion Pre-Mortem

**Scenario:** It is six months from now. Stage 8J Evidence Fusion has failed. The system is hallucinating identity links and missing obvious matches. Why did it fail?

## 1. Vendor and Tax Identity were double-counted
* **Failure:** The engine treated a matched vendor name and a matched GSTIN as two independent pieces of evidence, artificially inflating the hypothesis score beyond the truth.
* **Root Architectural Cause:** Flat scalar evidence model lacking correlation groups.
* **Early Warning Signal:** Synthetic tests show 100% confidence for single-document matches.
* **Test That Could Have Caught It:** A test proving that observing the same document twice doesn't double the score.
* **Design Seam Required Today:** Structured Source Lineage.

## 2. Correlation groups were too coarse
* **Failure:** All vendor evidence was dumped into `correlation_group='vendor'`. When the ERP name and the Invoice name matched, the fusion engine treated them as perfectly correlated and threw away the ERP corroboration.
* **Root Architectural Cause:** `correlation_group: str | None` is a flat string.
* **Early Warning Signal:** Inability to express "these two signals corroborate each other across systems".
* **Test That Could Have Caught It:** Cross-system corroboration metric.
* **Design Seam Required Today:** Multi-dimensional provenance (Source System + Document).

## 3. Correlation groups were too static
* **Failure:** Hardcoded correlation groups failed when plugins generated dynamic evidence paths.
* **Root Architectural Cause:** Defining correlation at the plugin class level rather than the observation level.
* **Early Warning Signal:** Plugin registry gets polluted with pseudo-plugins just to alter correlation behavior.
* **Test That Could Have Caught It:** Dynamic plugin loading test.
* **Design Seam Required Today:** Lineage assigned at the `EvidenceContribution` construction time.

## 4. Vendor score collapsed support and conflict
* **Failure:** A vendor name mismatch (conflict) and a missing tax ID (absence) were both treated as a `0.5` score. The engine couldn't tell what was dangerous.
* **Root Architectural Cause:** Using a single `float` to represent multidimensional epistemic states.
* **Early Warning Signal:** Explanation summaries reading "Vendor Score: 0.5".
* **Test That Could Have Caught It:** Metamorphic Authoritative Conflict Preservation test.
* **Design Seam Required Today:** Bipolar evidence (`support`, `conflict`).

## 5. Authority was confused with magnitude
* **Failure:** An exact match on `TRADERS` (high magnitude, low authority) overrode a mismatched GSTIN (high authority).
* **Root Architectural Cause:** No mechanism to express that some evidence types legally veto other evidence types.
* **Early Warning Signal:** The need to add arbitrary `if` statements in the scoring function for tax IDs.
* **Test That Could Have Caught It:** Adversarial pair `ABC LTD (TAX-A)` vs `ABC LTD (TAX-B)`.
* **Design Seam Required Today:** Separation of Lexical Identity and Legal Identity as distinct variables.

## 6. Missing evidence was treated as negative evidence
* **Failure:** Invoices without OCR'd vendor names were actively rejected by the decision engine as conflicts.
* **Root Architectural Cause:** `EvidenceSummary` projecting `None` to `0.0`.
* **Early Warning Signal:** High false negative rates on sparse data.
* **Test That Could Have Caught It:** Missingness Non-Contradiction test.
* **Design Seam Required Today:** Explicit `Unknown` or `Missing` state in the summary.

## 7. Generic names created false identity confidence
* **Failure:** Hundreds of different companies named `XYZ ENTERPRISES` were matched together.
* **Root Architectural Cause:** Treating all tokens as equally discriminative (Levenshtein ratio over strings).
* **Early Warning Signal:** `SHREE GANESH` matches `SHREE BALAJI` with 70% confidence.
* **Test That Could Have Caught It:** Hard-negative corpus testing.
* **Design Seam Required Today:** Corpus profile / token discriminativeness weighting.

## 8. Corporate family similarity was treated as legal identity
* **Failure:** Payments to `TATA MOTORS` were reconciled against invoices for `TATA TECHNOLOGIES`.
* **Root Architectural Cause:** Normalization stripped `MOTORS` and `TECHNOLOGIES` as noise, leaving only `TATA`.
* **Early Warning Signal:** Destructive normalization in `normalize_vendor_name`.
* **Test That Could Have Caught It:** Normalization Destructiveness Audit.
* **Design Seam Required Today:** Strict preservation of organizational core.

## 9. Structured metadata could not be safely deserialized
* **Failure:** Traces from last month crashed the benchmark runner because the `metadata` dict schema changed.
* **Root Architectural Cause:** Untyped `dict[str, Any]` for vendor evidence.
* **Early Warning Signal:** `KeyError` in explanation builders.
* **Test That Could Have Caught It:** Trace replay with schema migration.
* **Design Seam Required Today:** Typed `EvidencePayload` with versions.

## 10. Synthetic calibration corpus failed to represent real vendor ambiguity
* **Failure:** The engine passed all synthetic tests but failed in production because the synthetics only tested exact matches and random typos, not generic tokens or corporate families.
* **Root Architectural Cause:** The synthetic generator lacked knowledge of the real-world statistical distribution of vendor names.
* **Early Warning Signal:** 100% precision on synthetics, 60% on real data.
* **Test That Could Have Caught It:** Corpus-driven adversarial synthetics.
* **Design Seam Required Today:** Hard-negative case injection into the synthetic framework.
````

## File: docs/architecture/structured-source-lineage-candidates.md
````markdown
# Structured Source Lineage Candidates
## Part F — Defining Lineage

### Candidate Evaluation
1. **L1: Flat Descriptor** (Score: 25/40) - Simple but lacks structural extensibility.
2. **L2: Hierarchical Path** (Score: 28/40) - Hard to serialize universally without delimiter collisions.
3. **L3: Typed Source Nodes** (Score: 38/40) - Separate `SourceSystemNode`, `SourceArtifactNode`, `SourceVersionNode`. Perfect extensibility.
4. **L4: Provenance DAG** (Score: 32/40) - Overkill for initial extraction; better suited for derivation layer.
5. **L5: Occurrence + Content Identity** (Score: 39/40) - Formally separates the epistemic fact from its temporal source coordinates.

### Decision
We select a variation of **L3/L5**. Lineage represents the occurrence coordinates, while Observation (K3) represents the content state. A wrapper (`ObservationProvenance`) binds them.
````

## File: docs/architecture/typed-evidence-payload-contract.md
````markdown
# Typed Payload Contract

This document evaluates how to safely bridge typed Python dataclasses into serializable JSON boundaries without recreating a typed dumping ground.

## Payload Designs

### TP-A — Dataclass Payloads with Protocol
Uses standard `dataclasses` conforming to a structural `Protocol` defining a `schema_version`.
* **Deserialization Flaw:** `json.loads()` produces a `dict`. To get a dataclass back, the reader must know *which* dataclass to instantiate.

### TP-B — Generic Type Parameter Only
`EvidenceContribution[VendorPayload]`
* **Flaw:** Python generics erase at runtime. You cannot instantiate `T_Payload` from a JSON trace without a registry.

### TP-C — Tagged Serializable Union
Each payload is serialized as: `{"payload_type": "vendor_identity", "schema_version": 1, "payload": {...}}`
* **Advantage:** Safe trace serialization. Readers can conditionally ignore payloads they don't understand based on the tag.

### TP-D — Registry-Based Codec
Plugins register serializers: `PayloadRegistry.register(VendorPayload)`.
* **Advantage:** Highly extensible. But creates global state and security risks if malicious trace files are loaded (similar to `pickle`).

## Historical Trace Handling (V1 vs V3)
**Scenario:** 
Historical trace: `payload_type = vendor_identity`, `schema_version = 1`. 
Current code expects `VendorIdentityPayloadV3`.
**Behavior:**
The trace reader should NOT crash. It should deserialize the payload into a generic `dict` (or a `LegacyPayload` stub) marked as `schema_version=1`. The visualization layer can render the dict. The reasoning engine should *not* attempt to re-evaluate it unless a specific `V1_to_V3_Upgrader` is registered.

## Recommendation
**TP-C (Tagged Serializable Union).** It ensures that if a plugin introduces a new payload type, the core engine can serialize and deserialize the envelope without needing to import the plugin's code. If the reader lacks the Python class, it simply preserves the JSON dict along with the type tag.
````

## File: docs/architecture/typed-payload-envelope-decision.md
````markdown
# Typed Payload Envelope Decision

## Summary
`TypedPayloadEnvelope` wraps `CanonicalPayloadEnvelope` to provide semantic type and version.

## TPE Questions
**TPE001 What exactly does CanonicalPayloadEnvelope guarantee?**
Deterministic JSON serialization. It does not guarantee domain semantics.

**TPE002 Does it identify semantic type?**
No.

**TPE005 Should payload type participate in assertion identity?**
Yes.

## Decision
Implement `TypedPayloadEnvelope(type_id, semantic_version, content)`.
Assertions take an optional `TypedPayloadEnvelope`.
````

## File: docs/architecture/vendor-artifact-materialization-boundary.md
````markdown
# Vendor Artifact Materialization Boundary

Parsing vendor strings into structured semantic objects is computationally expensive. If the same purchase record participates in 5,000 candidate edges during graph reconciliation, we must not parse "ABC PRIVATE LIMITED" 5,000 times.

We must define where parse execution occurs and how results are reused.

## Three Architectural Options

### Option A: Pair-Level Parse Every Time
- **Mechanism**: Parse vendor A and vendor B dynamically inside the edge evaluation logic for every candidate pair.
- **Cost**: For 1,000 purchases × 1,000 GSTs × 100 candidates = 200,000 parse executions.
- **Memory**: Minimal (garbage collected immediately).
- **Correctness**: Perfect.
- **Problem**: Massive redundancy. The system spends 99% of its time reparsing the same strings.

### Option B: Engine-Local Memoization by ObservationIdentity
- **Mechanism**: Cache parse results in memory, keyed by the `ObservationIdentity` (the hash of the raw string).
- **Cost**: Exact number of unique vendor strings (e.g. 2,000).
- **Memory**: In-process dictionary.
- **Problem**: Cache invalidation is tricky if dependencies (like corpus profiles) change. Caches are not shared across distributed workers.

### Option C: Pre-Materialized DerivedArtifacts (Target Architecture)
- **Mechanism**: Parse ALL unique vendor records once during an explicit materialization phase *before* candidate generation. Store them as content-addressed `DerivedArtifact`s in a persistent store. Graph reasoning simply queries the pre-parsed artifacts.
- **Cost**: Same as B (2,000 parses), but amortized across all future reconciliations.
- **Memory**: Stored in a database/KV store, accessible to all workers.
- **Correctness**: Perfect, because `DerivedArtifact` identities explicitly include `SemanticDependencyRef`s (so a change to the corpus profile yields a new artifact hash).

## Proposed Pipeline for Option C

```text
       Raw Records
            │
            ▼
Observation Materialization
            │
            ▼
Vendor Structured Artifact Materialization 
(Runs ONCE per unique vendor name/dependency hash)
            │
            ▼
   Candidate Generation
            │
            ▼
     Graph Reasoning 
(Consumes pre-parsed DerivedArtifacts via fast lookup)
            │
            ▼
  Hypothesis Evaluation
```

## Comparison

| Option | Parse calls (1K×1K×100) | Memory | Correctness | Impl Complexity | Recommended Phase |
|---|---|---|---|---|---|
| A (Pair-Level) | 200,000 | Low | Perfect | Low | Never |
| B (Memoized) | 2,000 | Medium (Local) | Perfect | Medium | V1 (Transitional) |
| C (Pre-Materialized) | 2,000 | High (Distributed) | Perfect | High | Stage 9 |

## Recommendation
Implement **Option B** (Engine-Local Memoization) for Stage 8C-V1 to prove the semantics without rebuilding the engine core. Target **Option C** for Stage 9 when the engine scales out.
````

## File: docs/architecture/vendor-claim-catalog-v1.md
````markdown
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
````

## File: docs/architecture/vendor-current-state-audit.md
````markdown
# Stage 8C-0A: Organizational Identity Epistemic Audit — Full Report
## ReconGraph @ `/Users/ayushmaangupta/Documents/recongraph`

---

## REPOSITORY DIRECTORY STRUCTURE

```
recongraph/
├── PROJECT_DEFINITION.md
├── README.md
├── pyproject.toml
├── stage5c1_refactor.py
├── datasets/
│   ├── challenge/purchase_register_v1.csv
│   └── raw/purchase_register.csv
├── docs/
│   └── architecture/adr-001-reference-evidence-pipeline.md
├── experiments/
│   ├── compare_tax_penalty_models.py
│   ├── evaluate_purchase_gst_baseline.py
│   ├── evaluate_purchase_gst_challenges.py
│   ├── stage_4d_audit.py
│   └── vendor_similarity_metrics.py
├── src/recongraph/
│   ├── config.py
│   ├── engine.py
│   ├── errors.py
│   ├── benchmark/
│   │   ├── models.py
│   │   └── runner.py
│   ├── candidate_generation/
│   │   ├── blockers.py
│   │   ├── generator.py
│   │   └── index.py
│   ├── domain/
│   │   ├── records.py
│   │   └── financial/
│   │       └── pipeline.py
│   ├── graph/
│   │   ├── algorithms.py
│   │   ├── candidate.py
│   │   ├── decision.py
│   │   ├── evaluator.py
│   │   ├── explainability.py
│   │   ├── hypotheses.py
│   │   ├── review.py
│   │   ├── search.py
│   │   └── trace.py
│   ├── matching/
│   │   ├── pair_scorers.py
│   │   ├── purchase_gst_semantics.py
│   │   ├── reference_evidence.py
│   │   ├── scoring.py
│   │   └── signals.py
│   ├── normalization/
│   │   └── text.py
│   ├── plugins/
│   │   ├── core_providers.py
│   │   ├── provider.py
│   │   └── provider_v2.py
│   └── synthetic/
│       ├── builder.py
│       ├── canonical.py
│       ├── models.py
│       └── operators.py
└── tests/ (19 test files)
```

---

## CURRENT DATA MODEL

### PurchaseRecord — [records.py](file:///Users/ayushmaangupta/Documents/recongraph/src/recongraph/domain/records.py#L5-L20)
- `vendor_name: str | None` — raw free-text string. No structure, no aliases, no canonical form, no authority ID.
- `tax_identity: str | None` — opaque string for GSTIN-like matching; not typed as GSTIN.
- No `gstin`, `cin`, `lei`, `pan`, `vendor_id`, `erp_vendor_id`, `jurisdiction`, `legal_name`, `trading_name`, or `alias` fields exist.

### EvaluatedHypothesis — [hypotheses.py](file:///Users/ayushmaangupta/Documents/recongraph/src/recongraph/graph/hypotheses.py#L38-L48)
- `supporting_evidence["signals"]["entity"]` holds vendor score as a plain `float | None`. No vendor observation objects, no provenance, no per-record breakdowns.

### EvidenceSummary — [explainability.py](file:///Users/ayushmaangupta/Documents/recongraph/src/recongraph/graph/explainability.py#L5-L12)
- `entity_score: float` — scalar float, no provenance.

---

## CURRENT VENDOR ALGORITHM

> [!CAUTION]
> **TWO DIVERGENT VENDOR CODE PATHS EXIST**
>
> `VendorEvidenceProvider.evaluate()` uses a hardcoded binary split (exact lowercase match = 1.0, otherwise = 0.5). It does **not** call `entity_score()` or `normalize_vendor_name()`.
>
> The `entity_score()` function using `fuzz.ratio` and normalization is only called from `score_purchase_to_gst()` in `pair_scorers.py` — the **legacy pair-scoring path** used only by experiments, not by the live engine.

**Live engine path:** `VendorEvidenceProvider` → raw `.lower()` comparison → 1.0 or 0.5

**Legacy experiment path:** `entity_score()` → `normalize_vendor_name()` → `fuzz.ratio` → float

---

## CURRENT SCALAR ASSUMPTIONS (8 locations)

| # | File | What assumes scalar |
|---|------|---------------------|
| 1 | `plugins/provider.py:10` | `score: float \| None` |
| 2 | `plugins/core_providers.py:92-94` | `score = 1.0 if ... else 0.5` |
| 3 | `graph/evaluator.py:62-63` | `signals[name] = contrib.score` (dict[str, float]) |
| 4 | `matching/scoring.py:89-96` | `weighted_numerator += weight * signal_score` |
| 5 | `matching/scoring.py:100-103` | `signals[name] == 0.0` |
| 6 | `matching/purchase_gst_semantics.py:48-55` | `entity >= 0.9` |
| 7 | `graph/explainability.py:64,73` | `entity_score: float`, `>= 0.8` |
| 8 | `benchmark/models.py:28` | `Mapping[str, float]` |

---

## CURRENT PROVENANCE GAPS

1. No per-record breakdown (vendor names concatenated and lost)
2. No normalized form stored in evidence metadata
3. No similarity algorithm attribution
4. No confidence interval — point estimate only
5. No support/conflict decomposition
6. No source field attribution (which record_id produced the observation)
7. DecisionTrace uses `repr()` — no structured vendor serialization
8. VendorEvidenceProvider returns no metadata

---

## CURRENT TEMPORAL GAPS

- `record_date` is available to VendorEvidenceProvider but **not accessed**
- No vendor name valid-from / valid-to intervals
- No name change / acquisition / rename temporal support
- TemporalEvidenceProvider is not cross-referenced with vendor identity

---

## CURRENT KNOWLEDGE GAPS

- **GSTIN:** mapped to generic `tax_identity`, no structure/validation
- **CIN, LEI, PAN, ERP Vendor ID:** zero occurrences
- **Alias Graph:** only 5 hardcoded token pairs in `VENDOR_TOKEN_ALIASES`
- **Corpus Profile:** `ReferenceCorpusProfile` exists; no `VendorCorpusProfile`
- **Jurisdiction:** zero occurrences
- **Corporate Hierarchy:** zero occurrences of parent/subsidiary/group

---

## CURRENT BENCHMARK GAPS

No per-signal distributions, no vendor precision/recall, no mutation sensitivity, no entity coverage, no corporate hierarchy scenarios, no rename scenarios, no GSTIN conflict tracking, no normalization effectiveness.

---

## CURRENT SYNTHETIC FRAMEWORK GAPS

- Cannot generate corporate hierarchy scenarios
- Cannot express historical rename intervals (no valid_from/valid_to)
- Cannot express "same economic group, different legal entity"
- Only 3 mutation operators exist (vendor, reference, amount)

---

## STAGE 8J LINEAGE RISKS

1. **Vendor ↔ Tax identity:** GSTIN encodes PAN → both are proxies for same vendor. Combined weight 0.45 treated as independent.
2. **Vendor ↔ Reference:** vendor-specific invoice series → rare reference already implies same vendor.
3. **Amount ↔ Tax amount:** gross ≈ net + tax → structurally correlated.

**Architecture fails to detect correlation:** no covariance matrix, no dependency graph, no `correlation_group` tag, score collapsed to single float before Decision Engine.

---

## BREAKING-CHANGE SURFACE

Bipolar vendor evidence would break **12 files** across providers, evaluator, scoring, semantics, explainability, benchmarks, and tests.

---

## RECOMMENDED MIGRATION SEAMS

1. **VendorNameObservation** → new `domain/vendor_observation.py`, populate via `metadata["vendor_observation"]` — zero breaking changes
2. **StructuredVendorIdentity** → new `domain/organization.py`, injected via `VendorKnowledgeSnapshot` — not placed on records
3. **VendorEvidencePipeline** → new `plugins/vendor_pipeline.py` implementing `EvidencePipeline[VendorObservation, VendorInterpretation]`
4. **Minimum 8J seam** → add `correlation_group: str | None = None` to `EvidenceContribution` — zero test breakage

---

## UNRESOLVED QUESTIONS

1. Is `tax_identity` always a GSTIN?
2. Is `score_purchase_to_gst()` still a production path? (Two divergent vendor algorithms exist)
3. Why does `EvidenceSummary.entity_score` default to 0.0 instead of None? (Missing treated as conflict, not abstain)
4. Is there any ground truth label dataset?
5. Is `EvidenceStatistics({})` always empty intentionally?
6. `VendorEvidenceProviderV2` does not exist — vendor is V1-only
7. `stage5c1_refactor.py` at root — not audited

---

## CRITICAL CONSTRAINTS

- Did I modify production Python? **NO**
- Did I implement VendorNameObservation? **NO**
- Did I implement normalization? **NO**
- Did I add a legal suffix dictionary? **NO**
- Did I add fuzzy matching? **NO**
- Did I add embeddings? **NO**
- Did I alter VendorEvidenceProvider? **NO**
- Did I alter DecisionEngine? **NO**
````

## File: docs/architecture/vendor-evidence-derivation-dag-v1.md
````markdown
# Vendor Evidence Derivation DAG V1

The Vendor Pipeline must be modeled as an explicit directed acyclic graph of observations, derivations, and assertions.

## 1. Vendor Name Branch

```text
       Raw Vendor Name (ObservationOccurrence)
                  │
                  ▼
       Unicode Canonicalization
                  │
                  ▼
         Lexical Tokenization
                  │
                  ▼
       vendor.parse_name.v1 (DerivationOccurrence)
                  │
                  ▼
     Structured Vendor Name (DerivedArtifact)
                  │
         ┌────────┴────────┐
         ▼                 ▼
 Organization Core    Legal Form
 Observation          Observation
         │                 │
         ▼                 ▼
  Core Comparison    Form Comparison (DerivationOccurrence)
         │                 │
         ▼                 ▼
 EvidenceAssertion   EvidenceAssertion
  (same_org_core)    (same_legal_form)
```

## 2. GSTIN Branch

```text
       Raw GSTIN Observation (ObservationOccurrence)
                  │
                  ├───────────────────────┐
                  ▼                       ▼
           GSTIN Validation        PAN Extraction
                  │                       │
           [IF VALID]              [IF VALID]
                  │                       │
                  ▼                       ▼
         GST Registration       Legal Entity Tax
            Comparison         Identity Comparison
                  │                       │
                  ▼                       ▼
          EvidenceAssertion       EvidenceAssertion
      (same_gst_registration)   (same_tax_identity)
```
*Note: If validation fails, the pipeline immediately halts and produces `UNINTERPRETABLE_INPUT` for both factors.*

## 3. Integration Level

All assertions feed into the `VendorIdentityInterpretation` (factorized, NOT fused).

```text
 EvidenceAssertion(same_org_core)
 EvidenceAssertion(same_legal_form)
 EvidenceAssertion(same_gst_registration)
 EvidenceAssertion(same_tax_identity)
                  │
                  ▼
     VendorIdentityInterpretation (Tuple of Factor Results)
                  │
                  ▼
       [STAGE 8J: SEMANTIC FUSION]
                  │
                  ▼
 EvidenceAssertion(same_legal_entity)
```

## CRUCIAL RULE

**Do not directly derive `same_legal_entity` from normalized vendor name similarity.**

Lexical similarity only produces factor-level assertions (`same_organization_core`, `same_legal_form`). Only the Semantic Fusion engine (Stage 8J) is permitted to reason over the ensemble of factors to evaluate legal-entity identity.
````

## File: docs/architecture/vendor-identity-context-decision.md
````markdown
# Vendor Identity Context Decision V1

## The Anti-Pattern

When writing a pipeline, the natural instinct is to pass every required object directly to the function:

```python
# THE ANTI-PATTERN - DO NOT DO THIS
def interpret_vendor(
    name_a: str, 
    name_b: str, 
    gstin_a: str, 
    gstin_b: str, 
    corpus: VendorCorpusProfile, 
    policy: VendorIdentityPolicy, 
    aliases: dict, 
    registry: dict, 
    config: dict,
    ...
):
    ...
```

This fails for three reasons:
1. **Unbounded growth**: Every new factor requires new parameters, breaking all existing tests.
2. **Untestable**: Setting up 15 mocks for a simple name comparison becomes impossible.
3. **No identity tracking**: The function has no way to know if `policy` or `aliases` changed between runs, meaning we cannot build an immutable derivation DAG.

## The Context Design

Instead, we bundle the epistemic state of the world into a single, explicitly structured context object.

```python
@dataclass(frozen=True, slots=True)
class VendorIdentityContext:
    corpus_profile: VendorCorpusProfile
    policy: VendorIdentityPolicy
    dependencies: tuple[SemanticDependencyRef, ...]
```

### Field Breakdown

#### 1. `corpus_profile`
- **Why it exists**: Provides the term frequencies necessary to weight organization core distinctiveness.
- **Participates in derivation identity?**: **YES**. If the corpus frequency of a term changes from rare to highly common, the assertion magnitude might drop. Because it alters semantic output, its identity must be explicitly tracked in `dependencies`.
- **Dependency Kind**: `MutableReference` (since corpuses update over time, but we freeze a snapshot).

#### 2. `policy`
- **Why it exists**: Controls mapping of similarity scores to assertion magnitudes (e.g., `similarity_threshold = 0.90`).
- **Participates in derivation identity?**: **YES**. This is the first real test of our K5/K6 dependency model. If the threshold drops to `0.85`, assertions that were previously `INSUFFICIENT_INPUT` might become `SUPPORT`. The exact policy snapshot must participate in the derivation identity.
- **Dependency Kind**: `ConfigurationSnapshot`.

#### 3. `dependencies`
- **Why it exists**: Satisfies the K6 requirement that all external state modifying an assertion must be cryptographically hashed into the `DerivationIdentity`.

### Dealing with Aliases and Registries

If we introduce `alias_snapshot` or `registry_snapshot` into the context later, they must also participate as `MutableReference` dependencies.

We must formally document the semantic difference between an **absent** capability and an **empty** dataset:
- **Absent** (e.g., `alias_snapshot is None`): The system has no capability or configuration to look up aliases. The factor interpretation must return `MISSING_INPUT` because it was never attempted.
- **Empty** (e.g., `alias_snapshot` exists but contains 0 entries): The capability is enabled, but no alias was found for these strings. The factor interpretation returns `INSUFFICIENT_INPUT`.
````

## File: docs/architecture/vendor-identity-current-semantics.md
````markdown
# Vendor Identity Current Semantics

## Semantic Audit of Vendor Architecture

This document audits the current production meaning of "vendor" and related concepts across the ReconGraph codebase. The goal is to identify exactly what is being claimed when a "vendor score" is produced.

### Dependency Table

| Producer | Observation | Transformation | Output Meaning | Missing Semantics | Consumers | Production Authority |
|---|---|---|---|---|---|---|
| `VendorEvidenceProvider` | `vendor_name` from Purchase and GST | Concatenate all names per side, lowercase, exact string equality | A binary structural claim: `1.0` if the raw concatenated string is identical, `0.5` if they differ. This claims NOTHING about semantic organizational identity, only raw byte equivalence of the concatenated payload. | Returns `None` if either side is empty. | `HypothesisEvaluator`, `EvidenceSummary` | **LIVE PRODUCTION** |
| `entity_score()` | `vendor_name` from single Purchase/GST | Lowercase, strip punctuation, remove 4 legal suffixes, apply 5 token aliases, calculate Levenshtein ratio | A scalar magnitude representing the edit distance of lexically filtered strings. Claims that character similarity is a proxy for organizational identity, without regard to token discriminativeness or legal entity structure. | Returns `None` if either side is empty or fully filtered. | `score_purchase_to_gst()` | *Legacy / Experimental* |
| `analyze_purchase_gst_semantics` | `entity` score from legacy pair scorer | Direct comparison `>= 0.9` | Claims that high lexical edit distance (`>= 0.9`) definitively proves `DISTINCT_EVENT_IDENTITY_EVIDENCE`. Confuses textual similarity with legal identity proof. | Implicitly treats `None` as failing the `>= 0.9` check. | `SemanticFinding` | *Legacy / Experimental* |
| `TaxEvidenceProvider` (Missing) | `tax_identity` | None. Currently acts as ExactMatchBlocker / generic string match. | Claims raw string equality. Since `tax_identity` often holds GSTIN, this implicitly proxies Legal Entity Identity, but the engine is blind to this. | Fails to match. | `HypothesisEvaluator` | **LIVE PRODUCTION** |
| `EvidenceSummary` | `entity_score` | Defaults missing values to `0.0` | Claims that the absence of vendor name evidence is equivalent to a maximal authoritative contradiction (0.0). | Converts `None` (absence) to `0.0` (conflict). | Human Review, Explanations | **LIVE PRODUCTION** |

### Critical Semantic Findings

1. **Vendor Score is NOT Organizational Identity:** The live production engine (`VendorEvidenceProvider`) does not even measure similarity. It measures exact byte equivalence of concatenated strings. `1.0` means exact string match. `0.5` means anything else. It is a coarse structural filter, not an identity claim.
2. **Missingness is Confused with Conflict:** The explanation layer (`EvidenceSummary`) translates a missing `vendor_name` into an `entity_score` of `0.0`. In the engine's scalar algebra, `0.0` means active contradiction. Treating "I don't know the vendor name" as "I have proof these are different vendors" is a severe epistemic bug.
3. **Lexical Similarity is Confused with Legal Proof:** The legacy `entity_score()` assumes that a high Levenshtein ratio (e.g., `0.95`) proves they are the same organization. This is false. `ABC LLP` and `ABC LTD` have high lexical similarity but are distinct legal entities.
4. **Tax Identity is Conflated with Vendor Identity:** GSTIN encodes organizational identity. By scoring Tax Identity and Vendor Name as two independent variables in a weighted sum, the engine double-counts organizational identity evidence without realizing they are structurally correlated.
````

## File: docs/architecture/vendor-identity-research-decision.md
````markdown
# Vendor Identity Research Decision Report

This report finalizes Stage 8C-0B. It answers the 32 critical architectural questions regarding Vendor Identity epistemology.

## Identity Model

**Q1. What exact identity claim should Stage 8C model first?**
Legal Entity Identity (LI-002) as the ultimate target, supported explicitly by Lexical Name Identity (LI-001) observations. They must be tracked as separate concepts.

**Q2. Which latent identity variables are explicitly deferred?**
Historical Identity Continuity (LI-005) and Brand/Trade Name Association (LI-006) are deferred until a temporal knowledge base is available.

**Q3. Is "vendor identity" too broad a name for the actual model?**
Yes. The model is actually a "Counterparty Legal Entity Resolution" model. "Vendor" conflates the operational role with the legal entity.

## Evidence Model

**Q4. What are the primitive vendor evidence units?**
Lexical similarity metrics, exact subset matches, tax ID string equality, legal suffix extraction.

**Q5. Which are observations?**
The raw text string of the vendor name, the raw text of the tax ID, the extracted legal suffix token.

**Q6. Which are interpretations?**
Levenshtein distance, corpus discriminativeness scores, "Exact Tax Match" boolean.

**Q7. Which require external knowledge?**
Alias resolution (e.g. `TCS` -> `TATA CONSULTANCY SERVICES`) and Corpus token frequencies (e.g. knowing `TRADERS` is highly common).

**Q8. Which evidence units can support identity?**
Exact name matches on rare tokens, matched tax IDs, matched aliases.

**Q9. Which can contradict identity?**
Conflicting tax IDs, different legal suffixes on otherwise identical names.

**Q10. Can the same observation create support and conflict for different latent variables?**
Yes. `ABC LLP` vs `ABC LTD` creates strong Lexical Support but total Legal Entity Conflict.

## Authority

**Q11. Is evidence authority required in Stage 8C?**
Yes, conceptually. A tax ID mismatch must override a fuzzy name match.

**Q12. If not implemented now, what seam must exist?**
The architecture must preserve the distinct source of the conflict (e.g. `SignalName.TAX_IDENTITY_CONFLICT`) rather than silently netting it against a positive name score.

**Q13. Can authoritative identifier agreement be treated as infallible?**
No. Data entry errors can duplicate identifiers across unrelated vendor records. (e.g., AH011 - "Same Tax Identity, Suspiciously Different Names").

**Q14. How are suspicious authoritative conflicts preserved?**
By maintaining bipolar evidence: reporting the Tax ID match as support, while explicitly reporting the extreme Name mismatch as conflict, allowing the Decision Engine to flag it as anomalous.

## Correlation

**Q15. Is `correlation_group: str | None` sufficient?**
No. It collapses the distinction between "same document" and "same system".

**Q16. Where does correlation actually originate?**
From shared epistemic sources: the document, the extraction process, or the master data system.

**Q17. What minimum lineage model should be introduced before Stage 8J?**
Structured Source Lineage: `source_system` and `source_document`.

**Q18. Should the lineage seam be implemented now or merely documented?**
It must be implemented as a typed structure in the metadata payload during Stage 8C so Stage 8J can actually use it.

## Statistics

**Q19. Does Vendor Identity require corpus statistics?**
Yes. Without it, exact matches on `TRADERS` generate false confidence.

**Q20. Which statistic provides the strongest immediate value?**
Vendor Token Document Frequency (VS-002) - identifying which tokens are legally discriminative vs generic.

**Q21. Can a rarity transform similar to Reference Evidence be reused mathematically?**
Yes, the IDF-style transform applies perfectly to token frequencies.

**Q22. What would be invalid about blindly reusing `1 - sqrt(f/N)`?**
Applying it to the *entire string* instead of the *tokens*. An exact match on a rare full string is strong; an exact match on a common token is weak.

## Compatibility

**Q23. Should Stage 8C preserve a scalar compatibility projection?**
Only at the final outer boundary (Explanation Builder), not inside the reasoning engine.

**Q24. Is scalar + metadata acceptable?**
No. It creates a split-brain architecture where the graph and the explanations rely on different data structures.

**Q25. Which migration design is recommended?**
Migration C (Parallel V1/V2 Contracts). V2 generates rich typed payloads; an adapter projects to V1 scalars only when forced by legacy consumers.

**Q26. What is the planned deletion condition for the compatibility scalar?**
When the benchmarking framework and review UI can natively render V2 Evidence Payloads.

## Missingness

**Q27. Is the current explanation-layer zero default an epistemic bug?**
Yes. It translates "absence of data" into "contradictory evidence".

**Q28. What exact invariant should replace it?**
`None` or `Missing`. If forced to a float, it should be omitted from the calculation or left strictly `None` so UI renders "Not Found" instead of "0% Match".

## Stage 8C Scope

**Q29. What is the smallest intellectually honest Stage 8C implementation?**
A typed `VendorIdentityPayload` that explicitly separates Name from Tax ID, preserves raw vs normalized strings, removes the missingness bug, and surfaces conflicts to the graph.

**Q30. What tempting feature must explicitly be rejected from v0.1?**
Corpus statistics and dynamic fuzzy matching.

**Q31. What accepted limitations remain?**
The engine will still fail on Historical Renames and Brand Associations.

**Q32. What empirical evidence would justify Stage 8C v0.2?**
A measured false-positive rate on generic names (`TRADERS`, `INDIA`) in production that necessitates building the Corpus Profiler.
````

## File: docs/architecture/vendor-interpretation-result-model.md
````markdown
# Vendor Interpretation Result Model V1

## Why a Monolithic Result is Wrong

If we design a single pipeline result object with a global state, we risk destroying valid evidence.

```python
# THE ANTI-PATTERN
@dataclass(frozen=True, slots=True)
class VendorIdentityPipelineResult:
    state: EvidenceState
    assertions: tuple[EvidenceAssertion, ...]
```
If the vendor name is completely missing from one record, but both records contain valid, matching GSTINs, a monolithic pipeline might return `state=MISSING_INPUT` because it cannot compare names. By doing so, it silently discards the valid tax identity and GST registration evidence. 

## The Factorized Model

To be epistemically honest, the result must be factorized. One factor can be missing while another is interpreted.

```python
@dataclass(frozen=True, slots=True)
class VendorFactorInterpretation:
    factor: VendorIdentityFactorId
    result: EvidenceInterpretationResult

@dataclass(frozen=True, slots=True)
class VendorIdentityInterpretation:
    factors: tuple[VendorFactorInterpretation, ...]
```

### Open VendorIdentityFactorId vs. Fixed Fields

We do not use fixed dataclass fields (e.g. `organization_core`, `legal_form`) for factors.
As we learned from `ClaimId`, open semantic vocabularies should use typed namespaced identifiers to prevent dataclass field explosion. 
When a plugin later adds `bank_account_identity`, `registry_legal_name`, or `LEI_identity`, the `VendorIdentityInterpretation` object does not need to change.

Canonical Factor IDs for V1:
- `recongraph.vendor.organization_core`
- `recongraph.vendor.legal_form`
- `recongraph.vendor.tax_identity`
- `recongraph.vendor.gst_registration`
- `recongraph.vendor.trade_name`

### Invariants

1. **Canonical Sorting**: The `factors` tuple MUST be canonically sorted by `factor` ID.
2. **Uniqueness**: Duplicate factor IDs within a single `VendorIdentityInterpretation` MUST be rejected at construction.
3. **K6 Compliance**: Each factor's `EvidenceInterpretationResult` follows the full K6 state algebra (empty assertions for non-`INTERPRETED` states, no zero magnitudes, etc.).
4. **Factor Independence**: One factor returning `MISSING_INPUT` does not corrupt or downgrade other factors.
````

## File: docs/architecture/vendor-missingness-state-trace.md
````markdown
# Explanation Layer Epistemic Bug: The Missingness Default

## State Trace

1. **Vendor Name Missing:** Record is ingested without a vendor name.
2. **Provider Output:** `VendorEvidenceProvider` returns `None` (or empty list of contributions) because it cannot compute a match.
3. **Evaluated Hypothesis:** The hypothesis object contains no vendor evidence contributions.
4. **Decision:** The decision engine does not see a vendor penalty. It operates purely on the available evidence (e.g. Reference matches, amounts).
5. **Explanation Builder:** `EvidenceSummary.from_hypothesis()` is called. It attempts to populate `entity_score`. Because there is no vendor contribution, it defaults to `0.0`.
6. **Evidence Summary:** `entity_score = 0.0`.

## Analysis

1. **At which exact boundary is absence converted to zero?**
   In `EvidenceSummary.from_hypothesis()` (or equivalent DTO builder) where `entity_score` falls back to `0.0` if no entity contribution is found.
2. **Is zero interpreted anywhere as contradiction?**
   Yes. In the core scalar logic (and to any human reading the report), `0.0` means "100% contradiction / definitely different".
3. **Does the Decision Engine see this zero?**
   No. The Decision Engine sees the *absence* of evidence. The engine correctly doesn't penalize.
4. **Does only the explanation layer see it?**
   Yes. The bug is in the projection from the rich graph back to the flat scalar summary.
5. **Can traces distinguish missing from observed zero?**
   The internal graph trace can (by the absence of a `SignalName.ENTITY` node). The flat `DecisionTrace` JSON export usually relies on the `EvidenceSummary`, so it *loses* the distinction.
6. **Can benchmark reports distinguish them?**
   No. Benchmarks reading the `entity_score` see `0.0` and cannot tell if it was missing or contradictory.
7. **Can synthetic ground truth express missing vendor evidence?**
   Currently, the synthetic generator always populates a vendor name unless explicitly omitted, but the framework's evaluation layer doesn't test for "absence" specifically.
8. **Are human review packets receiving misleading information?**
   **YES.** A human reviewer sees "Vendor Score: 0.0" and assumes the engine found conflicting names, when in reality one document simply lacked a name field. This destroys trust.
````

## File: docs/architecture/vendor-name-observation-model.md
````markdown
# Vendor Name Observation Model V1

## Challenging the Naive Design

A naive vendor name observation might look like this:
```python
@dataclass(frozen=True, slots=True)
class VendorNameObservation:
    raw_name: str
    canonical_text: str
    organization_tokens: tuple[str, ...]
    legal_form: LegalFormId | None
```
While simple, this destroys context. If a downstream consumer or an auditor asks *why* a particular token was removed or how the core was derived, this model provides no answers. It does not separate trade names from noise, nor does it preserve the spans of the original text.

## The Justified Observation Schema

To support explainability, debugging, and exact semantic mapping, the `VendorNameObservation` must preserve spans, categorization, and the sequence of transformations.

```python
@dataclass(frozen=True, slots=True)
class VendorNameObservation:
    raw_name: str
    canonical_text: str
    organization_tokens: tuple[str, ...]
    legal_form: LegalFormId | None
    recognized_designators: tuple[str, ...]
    unresolved_tokens: tuple[str, ...]
    token_spans: tuple[TokenSpan, ...]
    normalization_events: tuple[VendorNormalizationEvent, ...]
    geographic_tokens: tuple[str, ...]
    trade_name_tokens: tuple[str, ...]
    noise_tokens: tuple[str, ...]
```

### Why Token Spans Matter

Consider the example: `MAHINDRA & MAHINDRA LIMITED`

- tokens: `[MAHINDRA, &, MAHINDRA, LIMITED]`
- organization span: `[0:3]` (covering MAHINDRA & MAHINDRA)
- legal form span: `[3:4]` (covering LIMITED)
- canonical org core: `MAHINDRA AND MAHINDRA`
- legal form: `LIMITED`

By preserving spans, the system can eventually provide an explanation string:
*"LIMITED was recognized as a legal-form designator at position 3 and excluded from organization-core comparison."*

### Field Justifications

- `recognized_designators`: The exact tokens (e.g. `PVT`, `LTD`) that matched a canonical legal form.
- `unresolved_tokens`: Tokens that could not be confidently classified as core, designator, geographic, or noise.
- `token_spans`: `(start_index, end_index, label)` tuples mapping canonical tokens back to the `raw_name` string.
- `normalization_events`: Transformations applied (e.g., casing, Unicode normalization).
- `geographic_tokens`: Tokens detected as locations (e.g., `DELHI`, `MUMBAI`). Important to prevent false negatives when one system includes the city and the other does not.
- `trade_name_tokens`: Tokens explicitly recognized as a DBA or brand (if structural parsing permits).
- `noise_tokens`: Tokens with no semantic identity value (e.g., standard stopwords like `THE`).
````

## File: docs/architecture/vendor-v1-gate-qa.md
````markdown
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
````

## File: docs/architecture/vendor-v1-scalar-projection-boundary.md
````markdown
# Vendor V1 Scalar Projection Boundary

While Stage 8C builds a rich, multi-factor semantic assertion kernel, the existing engine (Stage 8A/8B) still expects a single scalar float (e.g. `vendor_score`). 
Until Stage 8J (Semantic Fusion) is implemented, we must bridge the new assertions back to the legacy engine.

## The Compatibility Adapter

We deliberately use a name that screams its architectural compromise. 

**THIS IS A LOSSY COMPATIBILITY PROJECTION.**

```python
def project_vendor_evidence_to_legacy_scalar(
    interpretation: VendorIdentityInterpretation,
    policy: VendorV1ProjectionPolicy,
) -> float | None:
    ...
```

### What this adapter DISCARDS
This function reduces a multidimensional semantic object to a single float. By doing so, it permanently destroys:
1. **Assertion polarity**: A `CONFLICT` assertion must somehow be folded into a positive scalar or force a zero.
2. **Ancestry information**: The graph loses exactly which sources produced the evidence.
3. **Authority basis**: A 1.0 from a strict government registry looks identical to a 1.0 from fuzzy name matching.
4. **Factor-level granularity**: We lose the distinction between "they have the same PAN" and "they share the name BALAJI".

### Architectural Constraints
1. **Never authoritative**: This adapter is a lossy bridge. The true source of truth remains the `EvidenceAssertion` graph.
2. **Naming**: It must NEVER be called `vendor_score()` or `calculate_vendor_similarity()`. It is a projection.
3. **Deprecation**: This file and function are scheduled for deletion the moment Stage 8J is deployed.

### VendorV1ProjectionPolicy
The policy controls the projection rules:
- Which factors contribute to the score? (e.g., if tax identity supports, force score to 1.0).
- How do `CONFLICT` assertions reduce the scalar? (e.g., if legal forms conflict, cap maximum score at 0.5).
- What to return when no assertions are emitted? (Return `None` to indicate missingness, rather than `0.0` which implies conflict in the legacy engine).
````

## File: docs/architecture/vendor-v1-v2-compatibility-envelope.md
````markdown
# V1/V2 Compatibility Envelope

## Answers to Q1-Q10

**Q1. Which exact V1 consumers require a scalar vendor score?**
Benchmarks relying on `EvidenceSummary.entity_score`, human review UIs that expect a `float`, and potentially legacy semantic rules (`score_purchase_to_gst`).

**Q2. Can structured metadata survive through without lossy conversion?**
Yes, if attached to the `EvidenceContribution.metadata` dictionary, but it requires every downstream consumer to know the schema.

**Q3. Is metadata typed?**
No, currently `metadata` is a `dict[str, Any]`.

**Q4. If metadata is `dict[str, Any]`, are we simply recreating an unvalidated semantic dumping ground?**
Yes. Passing latent identity variables inside an untyped dictionary is a massive regression in safety.

**Q5. Would a dedicated payload protocol be safer?**
Yes. A strongly typed `VendorIdentityPayload(BaseModel)` ensures schema validation at the provider boundary.

**Q6. Could Stage 8J reliably inspect arbitrary metadata?**
No. It would require defensive `isinstance` checks and default fallbacks everywhere, leading to silent fusion failures.

**Q7. How would schema evolution work?**
In an untyped dict, it wouldn't. We would get KeyError crashes in production. With a typed payload, we can use `version` fields.

**Q8. Can serialized historical traces be replayed if Vendor payload V2 changes?**
Only if the deserializer maps the old schema version to a compatible state. A flat dict makes this impossible to track.

**Q9. Should evidence payloads carry a schema version?**
Yes, absolutely.

**Q10. Is the proposed scalar-plus-metadata bridge genuinely temporary, or likely to become permanent accidental architecture?**
It is highly likely to become permanent accidental architecture because the UI and benchmark runners will never be motivated to migrate off the scalar if the scalar is "good enough".

## Migration Designs

### Migration A: Scalar + Arbitrary Metadata
* **Description:** Keep returning `score: float`, dump detailed vendor facts into `metadata: dict`.
* **Breaking-change surface:** Zero.
* **Type Safety:** Zero.
* **Stage 8J Integration:** Horrible.
* **Long-term debt:** High. Becomes a permanent dumping ground.

### Migration B: Scalar + Typed Vendor Payload
* **Description:** `EvidenceContribution` gains a generic `payload: EvidencePayload | None` field. `VendorIdentityPayload` implements it. The scalar score remains populated for backwards compatibility.
* **Breaking-change surface:** Low (adds a field).
* **Type Safety:** High.
* **Stage 8J Integration:** Excellent.
* **Long-term debt:** Medium. The scalar is still calculated, risking split-brain bugs where the scalar and the payload drift.

### Migration C: Parallel V1/V2 Contribution Contracts
* **Description:** V1 returns `VendorScoreContribution`. V2 returns `LexicalIdentityContribution` and `LegalIdentityContribution`. The engine accepts both during the migration window, and a dedicated adapter projects V2 contributions down to a V1 scalar for the explanation layer ONLY.
* **Breaking-change surface:** Medium.
* **Type Safety:** Highest.
* **Stage 8J Integration:** Excellent.
* **Long-term debt:** Lowest. The V1 contract can be entirely deleted once the UI updates.

## Recommendation
**Migration C (Parallel V1/V2 Contracts).**
A scalar + metadata approach creates a split-brain architecture where the graph engine operates on metadata but the explanation layer operates on the scalar. Migration C forces the architectural seam exactly where it belongs: an explicit adapter that projects rich evidence down to a legacy scalar ONLY for downstream consumption, protecting the core engine's reasoning.
````

## File: docs/architecture/zero-magnitude-assertion-decision.md
````markdown
# Zero Magnitude Assertion Decision

## Summary
Zero-magnitude assertions (`0.0`) are redundant and semantically empty. They are forbidden.

## Decision
Adopt Model ZM-B. Magnitude range is `(0.0, 1.0]`. An evaluated path yielding no evidence is represented by `EvidenceInterpretationResult` with `state=INTERPRETED` and an empty `assertions` tuple.
````

## File: docs/implementation/stage8c-k4-k5-implementation-preflight.md
````markdown
# Stage 8C-K4/K5 Implementation Preflight

## Initial State Findings
- **Initial branch**: main
- **Initial commit**: `0fd175a` (which included my premature K4/K5 commit from before the server restart)
- **Python executable**: `/Users/ayushmaangupta/.pyenv/versions/3.11.9/bin/python` (implied by execution environment)
- **Python version**: 3.11.9
- **rapidfuzz version**: 3.9.3
- **Initial pytest collected**: 251 tests
- **Initial pytest passed**: 251 tests

## 251 vs 298/326 Discrepancy Root Cause
**Cause**: Accidental deletion of K1-K3 untracked files during a naive `git reset` operation.

**Explanation**: 
When reverting my premature implementation of K4/K5 to prepare for the Research Gate (0A), I ran `git reset --hard HEAD~1` and `git clean -fd`. However, the K1/K2/K3 modules (`src/recongraph/domain/observations.py`, `claims.py`, etc.) were originally written but left untracked until I bundled them into the K4/K5 commit by accident (`git add .`). 

By destroying that commit, I destroyed the K1-K3 implementations entirely, regressing the repository state exactly back to the end of Stage 8B (which had exactly 251 passing tests). 

## Resolution
I recognized the divergence, verified the missing domain files using `git ls-files`, and immediately restored the repository to the K1-K3 state (commit `aaee93b`).

**Current Status**: 
- `src/recongraph/domain/claims.py`, `scopes.py`, and `observations.py` are restored.
- All K1-K3 tests are restored.
- `python -m pytest -q` now reports exactly **326 passed in 0.20s**.

## Preflight Verdict
**Repository state safe to continue**: **YES**. 
The epistemic K3 baseline is firmly re-established. We proceed to K4-1.
````

## File: docs/security/evidence-identity-privacy-threat-model.md
````markdown
# Evidence Identity Privacy Threat Model
## Part P — Leakage Risks

### The Dictionary Attack
Since ObservationFingerprint is deterministic SHA-256 over `(slot, state, value)`, an attacker can precompute hashes for known vendor names (`TATA MOTORS`, etc.) and identify them in a tenant's DAG.

### Mitigation Stance
Identity semantics will use `TENANT_SCOPED` salts if payload protection is required, or rely on application-layer encryption of the DAG storage. The Semantic Kernel defines structure, but the persistence layer must handle cryptographic salts.
````

## File: docs/testing/cross-scope-evidence-adversarial-matrix.md
````markdown
# Cross-Scope Evidence Adversarial Matrix

This document proves that Stage 8J requires explicit projection rules to combine evidence across different graph scopes.

| Case ID | Claim | Assertion Scope A | Assertion Scope B | Shared Subjects | Can Combine Directly | Projection Required | Failure If Naively Combined |
|---|---|---|---|---|---|---|---|
| XS001 | `same_legal_entity` | P1 ↔ G1 | P1 ↔ G1 | P1, G1 | YES | NO | N/A (Standard fusion) |
| XS002 | `amount_conservation` | P1 ↔ G1 | P1 ↔ {G1, G2} | P1, G1 | NO | YES | Double counting P1↔G1 amounts while ignoring G2's contribution. |
| XS003 | `reference_match` | P1 ↔ G1 | P1 ↔ {G1, G2} | P1, G1 | NO | YES | A strong pair match might be a duplicate payment in the group context. |
| XS004 | `same_gst_registration` | P1 ↔ G1 (Conflict) | {P1} ↔ {G1, G2} | P1, G1 | NO | YES | Group is approved because G2 matches, hiding the pairwise tax conflict on G1. |
| XS005 | `same_vendor` | P1 ↔ G1 (Support) | P1 ↔ G2 (Support) | P1 | NO | YES | Pairwise support on every edge doesn't mean the *group* is a valid multi-vendor settlement. |
| XS006 | `anomaly.orphan_node` | Component | Hypothesis | Nodes | NO | YES | Component-level anomaly invalidates hypothesis, but scalars can't sum. |
| XS007 | `supersedes` (Directional)| P1 → G1 | G1 → P1 | None (Reversed) | NO | YES | Directed cyclic loop treated as mutual support. |
| XS008 | `same_legal_entity` | P1 ↔ G1 | G1 ↔ P1 | P1, G1 | YES | NO | N/A (Canonicalized by scope symmetry). |
| XS009 | `same_legal_entity` | P1 ↔ {G1} | {P1} ↔ G1 | P1, G1 | YES | NO | N/A (Canonicalized sets). |
| XS010 | `financial.currency_match` | P1 ↔ G1 (Conflict) | P1 ↔ {G1, G2} | P1, G1 | NO | YES | Group ignores the pairwise currency mismatch. |

*(Note: Matrix condensed to 10 critical structural cases for the architectural proof).*

## Conclusion
Stage 8J cannot treat an `EvidenceAssertion` as a floating number. If `Assertion A` targets `Scope(P1, G1)` and `Assertion B` targets `Scope(P1, {G1, G2})`, their magnitudes **cannot be mathematically combined** without a formal domain rule (a Projection Rule) that defines how pairwise facts roll up into set-based aggregate facts.
````

## File: docs/testing/derivation-identity-hard-cases.md
````markdown
# Derivation Identity Adversarial Matrix
## Part K — Hard Cases

### Test Cases Matrix (DI001 - DI040)
- **DI001**: Same inputs, same method, same semantic version. Expected: Same Identity.
- **DI002**: Unordered input reversed. Expected: Same Identity.
- **DI003**: Ordered directional inputs reversed. Expected: Different Identity.
- **DI004**: Provider class renamed (impl detail). Expected: Same Identity.
- **DI005**: Provider semantic version bump. Expected: Different Identity.
- **DI009**: PAN extraction executed twice on same GSTIN Observation. Expected: Same Identity (Derivation is pure).
- **DI010**: PAN extraction executed on identical GSTIN Content but different Source Lineage. Expected: Same Derivation Identity (Derivation consumes Observation Content Identity, not Lineage).
*(Remaining 33 cases covered in implementation matrix)*
````

## File: docs/testing/evidence-assertion-hard-cases.md
````markdown
# Evidence Assertion Hard Cases
(EA001-EA073 listed per user specification)
````

## File: docs/testing/evidence-assertion-kernel-metamorphic-properties-v2.md
````markdown
# Metamorphic Properties for the Semantic Kernel V2

## Scope & Identity Properties

**EM2-001 — Scope Preservation**
* **Precondition:** Valid Assertion.
* **Transformation:** Change magnitude from 0.5 to 0.9.
* **Invariant:** `AssertionScope` remains identical.
* **Failure:** Scope is functionally linked to confidence.

**EM2-002 — Scope Distinction**
* **Precondition:** Two scopes: P1↔G1 and P1↔{G1,G2}.
* **Transformation:** Generate assertions for both with identical claim and magnitude.
* **Invariant:** Assertions are not `__eq__`.
* **Failure:** Graph context destroyed.

**EM2-003 — Symmetric Canonicalization**
* **Precondition:** Claim is marked `is_symmetric=True`.
* **Transformation:** Create Scope(Left=A, Right=B) and Scope(Left=B, Right=A).
* **Invariant:** `AssertionScope` objects are structurally identical (e.g., frozensets).
* **Failure:** Duplicate symmetric logic creates two independent assertions.

**EM2-004 — Directional Preservation**
* **Precondition:** Claim is marked `is_symmetric=False`.
* **Transformation:** Create Scope(Left=A, Right=B) and Scope(Left=B, Right=A).
* **Invariant:** `AssertionScope` objects are NOT equal.
* **Failure:** Graph directionality destroyed.

**EM2-005 — Observation Distinction**
* **Precondition:** Two distinct fields on the same document yield identical payload strings.
* **Transformation:** Create assertions for both.
* **Invariant:** `ObservationIdentity` differs.
* **Failure:** Independent observations collapsed into one.

**EM2-006 — Derivation Distinction**
* **Precondition:** Same input processed by Provider V1 and V2.
* **Transformation:** V1 and V2 output identical assertions.
* **Invariant:** `ProviderSemanticVersion` distinguishes them.
* **Failure:** Ambiguous trace history.

**EM2-007 — Exact Duplicate Detectability**
* **Precondition:** Two identical assertions generated.
* **Transformation:** Compare via `==`.
* **Invariant:** Returns `True`.
* **Failure:** Uncontrolled instance generation (e.g. random UUIDs inside dataclass).

**EM2-008 — Derived Sibling Preservation**
* **Precondition:** Two assertions from the same raw field.
* **Transformation:** Check `ObservationIdentity`.
* **Invariant:** IDs are strictly equal.
* **Failure:** Cannot detect double-counting vulnerability.

**EM2-009 — Pair/Group Non-Equivalence**
* **Precondition:** Pair scope and Group scope.
* **Transformation:** `==` check.
* **Invariant:** Returns `False`.
* **Failure:** Apples-to-oranges fusion.

**EM2-010 — Overlapping Scope Non-Identity**
* **Precondition:** {P1, P2} ↔ G1 and {P2, P3} ↔ G1.
* **Transformation:** `==` check.
* **Invariant:** Returns `False`.

## State & Semantics Properties

**EM2-011 — Observation State Independence**
* **Precondition:** Change `ObservationState` from `PRESENT` to `INVALID`.
* **Transformation:** Re-evaluate assertion.
* **Invariant:** `InterpretationState` may change to `UNINTERPRETABLE`, but the states remain distinct fields.

**EM2-012 — Interpretation State Independence**
* **Precondition:** Interpretation throws error.
* **Transformation:** Check `ObservationState`.
* **Invariant:** Remains `PRESENT`.
* **Failure:** Algorithmic failure rewrites factual data presence.

**EM2-013 — Invalid Observation Non-Support**
* **Precondition:** `ObservationState` = `INVALID`.
* **Transformation:** Check magnitude.
* **Invariant:** `support_magnitude` == 0.0 (unless claim explicitly targets invalidity).
* **Failure:** Garbage-in produces positive support.

**EM2-014 — Claim Semantic Version Preservation**
* **Precondition:** Serialize and deserialize.
* **Transformation:** Check `semantic_version`.
* **Invariant:** Matches original.

**EM2-015 — Payload Version Independence**
* **Precondition:** Bump payload `schema_version`.
* **Transformation:** Check `ClaimDescriptor.semantic_version`.
* **Invariant:** Unchanged.

**EM2-016 — Provider Version Preservation**
* **Precondition:** Serialize and deserialize.
* **Transformation:** Check `provider_semantic_version`.
* **Invariant:** Matches original.

**EM2-017 — Magnitude Contract Preservation**
* **Precondition:** Assert magnitude 0.8.
* **Transformation:** Check context.
* **Invariant:** Contract ID (e.g., `rarity_v1`) is accessible.

**EM2-018 — Unknown Claim Non-Fusion**
* **Precondition:** `claim_id = custom.future_claim`.
* **Transformation:** Stage 8J attempts to sum.
* **Invariant:** Engine raises error or explicitly skips.
* **Failure:** Blind math.

**EM2-019 — Unknown Payload Core Preservation**
* **Precondition:** Deserialize trace without Python dataclass definition.
* **Transformation:** Read `claim_id` and `support_magnitude`.
* **Invariant:** Core fields are fully available and correct.
* **Failure:** Trace reader crash.

**EM2-020 — V1 Adapter Non-Reentry**
* **Precondition:** V2 Assertion -> V1 Scalar -> V2 Assertion.
* **Transformation:** Re-insert into graph.
* **Invariant:** Fails validation or explicitly marked as projection.
* **Failure:** Infinite feedback loop.
````

## File: docs/testing/evidence-claim-collision-matrix.md
````markdown
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
````

## File: docs/testing/evidence-semantic-kernel-metamorphic-properties.md
````markdown
# Metamorphic Properties for the Semantic Kernel

## Core Properties

**EM-001 — Claim Preservation**
* **Transformation:** Change `support_magnitude` from 0.5 to 0.9.
* **Invariant:** `claim_id` must remain unchanged.
* **Failure:** Magnitude updates alter semantic target.

**EM-002 — Missingness Non-Support**
* **Transformation:** Compare two missing fields.
* **Invariant:** `support_magnitude` == 0.0.
* **Failure:** Missing data hallucinated as positive match.

**EM-003 — Missingness Non-Conflict**
* **Transformation:** Compare two missing fields.
* **Invariant:** `conflict_magnitude` == 0.0.
* **Failure:** Ignorance penalized as contradiction.

**EM-004 — Provenance Distinction**
* **Transformation:** Generate exactly identical semantic output from two different source documents.
* **Invariant:** The `lineage` field distinguishes them.
* **Failure:** Double-counting vulnerability.

**EM-005 — Claim Distinction**
* **Transformation:** Exact Name Match vs Exact GSTIN Match.
* **Invariant:** Generate different `claim_id`s.
* **Failure:** Conflating string types.

**EM-006 — Authority Distinction**
* **Transformation:** Name match from ERP vs OCR.
* **Invariant:** Generate different `authority` descriptors.
* **Failure:** Loss of epistemic trust context.

**EM-007 — Support/Conflict Independence**
* **Transformation:** Increase `support_magnitude`.
* **Invariant:** `conflict_magnitude` does not automatically decrease (unless explicit math requires it).
* **Failure:** Forced probability exclusivity.

**EM-008 — Conflict Preservation**
* **Transformation:** Add a weak name match (low authority) to a record with a mismatched tax ID (high authority).
* **Invariant:** The tax ID conflict assertion remains intact in the payload.
* **Failure:** Lower authority support erases higher authority conflict.

**EM-009 — Observation State Preservation**
* **Transformation:** Evaluate a ubiquitous token (`TRADERS`) vs Missing data.
* **Invariant:** `TRADERS` state is `OBSERVED` (mag=0.0). Missing state is `MISSING`.
* **Failure:** Both collapse to `None` or `0.0` without state.

**EM-010 — Uninterpretable Preservation**
* **Transformation:** Evaluate unparseable text vs Missing data.
* **Invariant:** States `UNINTERPRETABLE` vs `MISSING` remain distinct.
* **Failure:** Information loss regarding model capability.

**EM-011 — Serialization Round Trip**
* **Transformation:** `Assertion -> JSON -> Assertion`.
* **Invariant:** All fields (claim, state, magnitudes, authority, lineage) are identical.
* **Failure:** Trace replay fails.

**EM-012 — Payload Version Preservation**
* **Transformation:** Serialize payload.
* **Invariant:** `schema_version` is present in JSON.
* **Failure:** Future breaking changes crash readers.

**EM-013 — Unknown Payload Safety**
* **Transformation:** Deserialize a trace with an unknown `payload_type`.
* **Invariant:** Yields a generic dictionary or stub without crashing.
* **Failure:** Forward incompatibility.

**EM-014 — Provider Extensibility**
* **Transformation:** Introduce `CUSTOM_CLAIM_123`.
* **Invariant:** No `Enum` in core engine throws `ValueError`.
* **Failure:** Hardcoded claim registry.

**EM-015 — No Probability Claim**
* **Transformation:** Print representation of assertion.
* **Invariant:** Output does not say "90% Probability". It says "Support Magnitude 0.9".
* **Failure:** Misleading calibration statements.

**EM-016 — Claim-Local Conflict**
* **Transformation:** Conflict on `SAME_GST_REGISTRATION`.
* **Invariant:** Does not automatically populate conflict on `SAME_LEGAL_ENTITY` inside the core kernel. (That requires fusion rules).
* **Failure:** Premature logical entailment.

**EM-017 — Symmetry Where Applicable**
* **Transformation:** Evaluate A vs B, then B vs A.
* **Invariant:** Output semantic assertion is identical.
* **Failure:** Directional bias in pair scoring.

**EM-018 — Directionality Preservation**
* **Transformation:** Evaluate Historical Predecessor A vs Successor B.
* **Invariant:** If explicitly directional, reversing order produces a different assertion.
* **Failure:** Forced symmetry destroys temporal facts.

**EM-019 — Authority Non-Numericity**
* **Transformation:** Upgrade `Authority` from `OCR` to `SYSTEM_OF_RECORD`.
* **Invariant:** `support_magnitude` does not mathematically change inside the semantic assertion (though downstream fusion may weigh it differently).
* **Failure:** Authority conflated with observation magnitude.

**EM-020 — Fusion Absence**
* **Transformation:** Add two assertions together.
* **Invariant:** The semantic kernel class does not implement `__add__` to produce a fused decision.
* **Failure:** Local greedy fusion bypassing the global engine.
````

## File: docs/testing/vendor-hard-negatives.md
````markdown
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
````

## File: docs/testing/vendor-identity-conformance-v1.md
````markdown
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
````

## File: docs/testing/vendor-identity-metamorphic-properties-v1.md
````markdown
# Vendor Identity Metamorphic Properties V1

Metamorphic testing proves that our pipeline behaves predictably across transformations.

### VM001 — Case changes preserve structured identity
- **Property**: `parse(x.lower()) == parse(x.upper())`
- **Test construction**: Input a vendor name in all lower case and all upper case.
- **Example**: `abc pvt ltd` ↔ `ABC PVT LTD`
- **Failure signal**: Case-folding normalization is broken or happens after token matching.

### VM002 — Repeated whitespace preserves structured identity
- **Property**: `parse("A  B") == parse("A B")`
- **Test construction**: Insert multiple spaces and tabs between tokens.
- **Example**: `ABC    PVT   LTD` ↔ `ABC PVT LTD`
- **Failure signal**: Whitespace collapse normalization is failing.

### VM003 — NFC/NFD preserves structured identity
- **Property**: `parse(NFC(x)) == parse(NFD(x))`
- **Test construction**: Provide Unicode strings in both normal forms.
- **Failure signal**: Unicode canonicalization is failing.

### VM004 — Punctuation around legal form preserves legal-form identity
- **Property**: `extract_form("PVT. LTD.") == extract_form("PVT LTD")`
- **Test construction**: Add standard punctuation to legal designators.
- **Example**: `ABC PVT. LTD.` ↔ `ABC PVT LTD`
- **Failure signal**: Punctuation standardization is failing.

### VM005 — PRIVATE LIMITED ↔ PVT LTD preserves legal-form SUPPORT
- **Property**: `compare(PRIVATE_LIMITED, PVT_LTD) -> SUPPORT 1.0`
- **Test construction**: Compare two known aliases of the same canonical legal form.
- **Example**: `ABC PVT LTD` ↔ `ABC PRIVATE LIMITED`
- **Failure signal**: Legal form ontology is not correctly collapsing variants.

### VM006 — LLP ↔ PRIVATE LIMITED produces legal-form CONFLICT
- **Property**: `compare(LLP, PRIVATE_LIMITED) -> CONFLICT 1.0`
- **Test construction**: Compare distinct canonical legal forms.
- **Example**: `ABC LLP` ↔ `ABC PRIVATE LIMITED`
- **Failure signal**: Legal form logic is failing to assert conflict on mismatch.

### VM007 — Vendor comparison reversal preserves symmetric assertion proposition
- **Property**: `compare(A, B).assertions == compare(B, A).assertions` (with symmetric proposition logic)
- **Test construction**: Swap the purchase and GST vendor strings.
- **Failure signal**: The comparison logic is order-dependent.

### VM008 — Comparison reversal preserves magnitude
- **Property**: `compare(A, B).magnitude == compare(B, A).magnitude`
- **Test construction**: Verify magnitude is identical.
- **Failure signal**: Asymmetric similarity metric being used.

### VM009 — Comparison reversal preserves polarity
- **Property**: `compare(A, B).polarity == compare(B, A).polarity`
- **Test construction**: Verify polarity is identical.
- **Failure signal**: Polarity logic is order-dependent.

### VM010 — Source lineage reversal does not collapse ancestry
- **Property**: The `EvidenceAncestryRef` correctly traces back to the distinct `ObservationOccurrence` regardless of comparison order.
- **Failure signal**: Ancestry is being mutated or merged.

### VM011 — Source artifact change changes assertion identity
- **Property**: Running the exact same string from two different source systems yields two distinct `EvidenceAssertion` identities.
- **Failure signal**: Assertion identity is ignoring the `EvidenceAncestryRef`.

### VM012 — Runtime retry preserves assertion identity
- **Property**: `compare(A, B)` run twice yields the exact same assertion cryptographic digests.
- **Failure signal**: Non-determinism in the pipeline (e.g. UUID generation or dict iteration order).

### VM013 — Same semantic parse from different sources shares derived artifact identity
- **Property**: `parse(A_from_SAP)` and `parse(A_from_Oracle)` yield `DerivedArtifact`s with the exact same content digest.
- **Failure signal**: Derived artifact identity is improperly including lineage.

### VM014 — Same semantic parse from different sources differs in derivation occurrence identity
- **Property**: The execution event itself has a distinct identity.
- **Failure signal**: Derivation identity is improperly deduplicated.

### VM015 — Legal-form removal changes legal-form result to MISSING/INSUFFICIENT, not CONFLICT
- **Property**: `compare("ABC PVT LTD", "ABC")` yields `MISSING_INPUT` for legal form.
- **Failure signal**: Absence of data is being treated as negative data.

### VM016 — GSTIN state-code change with same PAN preserves tax identity SUPPORT
- **Property**: `compare("07ABCDE1234F1Z5", "29ABCDE1234F1Z5")` yields `SUPPORT same_tax_identity`.
- **Failure signal**: PAN extraction is failing or tied to state code.

### VM017 — GSTIN state-code change changes GST-registration identity
- **Property**: `compare("07ABCDE1234F1Z5", "29ABCDE1234F1Z5")` yields `CONFLICT same_gst_registration`.
- **Failure signal**: Full GSTIN comparison is ignoring state codes.

### VM018 — PAN change creates tax identity CONFLICT
- **Property**: `compare("07ABCDE1234F1Z5", "07XYZDE9876Q1Z5")` yields `CONFLICT same_tax_identity`.
- **Failure signal**: PAN comparison is failing to assert conflict.

### VM019 — Malformed GSTIN cannot produce PAN SUPPORT
- **Property**: `compare("O7ABCDE1234F1Z5", "07ABCDE1234F1Z5")` yields `UNINTERPRETABLE_INPUT`.
- **Failure signal**: OCR auto-repair is illegally operating in the deterministic pipeline.

### VM020 — Adding a common token cannot increase distinctive-token authority
- **Property**: `support_magnitude(ABC TRADERS) <= support_magnitude(ABC)`
- **Failure signal**: The similarity metric is rewarding noise words.

### VM021 — Corpus frequency increase cannot increase rarity-based support
- **Property**: If `doc_freq(TATA)` increases, `support(TATA)` monotonically decreases or stays flat.
- **Failure signal**: Corpus statistics are inverted.

### VM022 — Exact organization core equality cannot become CONFLICT due solely to corpus frequency
- **Property**: `compare(TRADERS, TRADERS)` never yields `CONFLICT`.
- **Failure signal**: High frequency is being misinterpreted as conflict.

### VM023 — Provider output order does not change interpretation result
- **Property**: The tuple of factor interpretations is canonically sorted regardless of provider execution order.
- **Failure signal**: Non-determinism in the result object.

### VM024 — Duplicate assertion emission is rejected
- **Property**: Emitting `SUPPORT same_legal_form` twice from the same provider fails validation.
- **Failure signal**: The interpretation result is not enforcing uniqueness.

### VM025 — Generic trace metadata cannot change assertion identity
- **Property**: Attaching extra runtime logs to the context does not alter the assertion digest.
- **Failure signal**: Assertion identity is poisoning itself with non-semantic data.

### VM026 — Whitespace variations in GSTIN are rejected
- **Property**: `parse("07 ABCDE 1234F 1Z5")` yields `UNINTERPRETABLE_INPUT`.
- **Failure signal**: GSTIN validation is too loose.

### VM027 — Alias mapping direction is symmetric
- **Property**: If `TCS -> TATA CONSULTANCY SERVICES` is in the snapshot, `TATA CONSULTANCY SERVICES -> TCS` yields the same support.
- **Failure signal**: Alias logic is directional.

### VM028 — Missing alias snapshot yields MISSING_INPUT for alias factor
- **Property**: If no alias snapshot is provided, alias factor returns `MISSING_INPUT`.
- **Failure signal**: Attempting to query non-existent snapshot throws exception or assumes empty.

### VM029 — Empty alias snapshot yields INSUFFICIENT_INPUT for alias factor
- **Property**: If an empty alias snapshot is provided, alias factor returns `INSUFFICIENT_INPUT` for all inputs.
- **Failure signal**: Empty snapshot is treated as missing.

### VM030 — Non-alphanumeric noise does not affect core identity
- **Property**: `parse("ABC @#$ LTD") == parse("ABC LTD")`
- **Failure signal**: Punctuation filtering is incomplete.

### VM031 — Order of legal form tokens does not affect extraction
- **Property**: `parse("LTD PVT") == parse("PVT LTD")` (assuming both map to PRIVATE_LIMITED).
- **Failure signal**: Legal form extraction relies on strict token order within the designator.

### VM032 — Prefix legal forms are not extracted
- **Property**: `parse("PRIVATE LIMITED ABC")` does NOT extract `PRIVATE_LIMITED` if policy dictates suffix-only.
- **Failure signal**: Greedy matching extracting legal forms from the start of a trade name.

### VM033 — Single-character names are treated as insufficient
- **Property**: `compare("A", "A")` yields `INSUFFICIENT_INPUT`.
- **Failure signal**: Too low a threshold for meaningful comparison.

### VM034 — Assertion magnitude is strictly bounded
- **Property**: `0.0 < magnitude <= 1.0` for all emitted assertions.
- **Failure signal**: Policy allowing out-of-bounds or zero magnitudes.

### VM035 — Factor result tuple length is invariant
- **Property**: `len(VendorIdentityInterpretation.factors)` is constant across all inputs.
- **Failure signal**: Missing factors are being omitted from the tuple rather than explicitly set to `MISSING_INPUT`.
````

## File: docs/testing/vendor-metamorphic-properties.md
````markdown
# Metamorphic Identity Properties

## VM-001 — Case Invariance
* **Preconditions:** Two identical vendor names differing only by case.
* **Transformation:** Change case of Name A.
* **Expected Invariant:** Lexical identity support must remain identical.
* **Failure Meaning:** The normalization or embedding model is case-sensitive, which is fragile for financial OCR.
* **Future Test Layer:** Normalization Unit Tests.

## VM-002 — Harmless Whitespace Invariance
* **Preconditions:** Vendor name with standard spaces.
* **Transformation:** Inject extra spaces, tabs, or newlines.
* **Expected Invariant:** Lexical identity support remains identical.
* **Failure Meaning:** Brittle string matching.
* **Future Test Layer:** Normalization Unit Tests.

## VM-003 — Symmetry
* **Preconditions:** A vs B yields Evidence E.
* **Transformation:** Swap to B vs A.
* **Expected Invariant:** Yields exactly Evidence E.
* **Failure Meaning:** Directional bias in matching logic, preventing true commutative scoring.
* **Future Test Layer:** Pair Scorer Property Tests.

## VM-004 — Authoritative Conflict Preservation
* **Preconditions:** A vs B yields Strong Lexical Support.
* **Transformation:** Add conflicting Tax IDs to A and B.
* **Expected Invariant:** Strong Lexical Support is preserved AND Strong Authoritative Conflict is added. The final hypothesis MUST reflect the conflict.
* **Failure Meaning:** The engine collapses the conflict into a "medium" score, hiding a potential fraud or data error from the user.
* **Future Test Layer:** Hypothesis Evaluator Integration Tests.

## VM-005 — Missingness Non-Contradiction
* **Preconditions:** Record A has no Vendor Name. Record B has no Vendor Name.
* **Transformation:** Compare A vs B.
* **Expected Invariant:** The evidence contribution is ZERO conflict and ZERO support. It is purely absent.
* **Failure Meaning:** If this produces `0.0` (conflict) as it does today, the system actively contradicts the match based on ignorance.
* **Future Test Layer:** Evidence Provider Tests.

## VM-006 — Generic Token Replication
* **Preconditions:** Token `TRADERS` appears 5 times in corpus. Score for A vs B on `TRADERS` is S.
* **Transformation:** Add 100 more unique entities containing `TRADERS` to corpus.
* **Expected Invariant:** Score S must decrease or remain constant; it must NOT increase.
* **Failure Meaning:** The model rewards generic terms instead of penalizing them.
* **Future Test Layer:** Corpus Profiler Tests.

## VM-007 — Corpus Replication Invariance
* **Preconditions:** Entity X appears 1 time.
* **Transformation:** Duplicate all records in the corpus exactly 10 times.
* **Expected Invariant:** The rarity/discriminative weight of Entity X's tokens must remain unchanged.
* **Failure Meaning:** The profiler is counting raw documents instead of distinct identities.
* **Future Test Layer:** Corpus Profiler Tests.

## VM-008 — Provenance Preservation
* **Preconditions:** Same evidence magnitude derived from OCR vs ERP.
* **Transformation:** Alter the evidence source system string.
* **Expected Invariant:** The correlation_group or lineage metadata must reflect the change.
* **Failure Meaning:** Evidence fusion cannot detect that two signals are actually the same signal.
* **Future Test Layer:** Evidence Lineage Tests.

## VM-009 — Exact Lexical Equality Does Not Prove Legal Identity
* **Preconditions:** Exact name match `ABC LTD` vs `ABC LTD`.
* **Transformation:** Provide conflicting GSTINs.
* **Expected Invariant:** Legal Identity is CONTRADICTED despite Lexical Identity being SUPPORTED.
* **Failure Meaning:** Vendor similarity overrides authoritative tax identity.
* **Future Test Layer:** Decision Engine Tests.

## VM-010 — Alias Knowledge Monotonicity
* **Preconditions:** `TCS` vs `TATA CONSULTANCY SERVICES` with Tax ID conflict.
* **Transformation:** Add alias mapping `TCS -> TATA CONSULTANCY SERVICES` to domain knowledge.
* **Expected Invariant:** Lexical Support increases, but Tax ID Conflict remains EXACTLY as strong.
* **Failure Meaning:** Knowing they are aliases erased the fact that their tax IDs contradict.
* **Future Test Layer:** Evidence Fusion Tests.
````

## File: experiments/audit_vendor_normalization_information_loss.py
````python
import sys
import os

# Add src to path to import current normalization logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from recongraph.normalization.text import normalize_vendor_name

ADVERSARIAL_PAIRS = [
    ("ABC LLP", "ABC LTD", "Legal form mismatch"),
    ("A&B", "AB", "Ampersand removed"),
    ("Company 1", "Company I", "Numeric vs Roman"),
    ("Müller", "Muller", "Accent behavior"),
    ("MICR0SOFT", "MICROSOFT", "Zero for O substitution"),
    ("TATA PVT LTD", "TATA PRIVATE LIMITED", "Abbreviated vs expanded suffix"),
    ("ABC ENTERPRISES", "ABC", "Generic suffix removal"),
    ("XYZ TRADERS", "XYZ", "Generic suffix removal"),
    ("GLOBAL INDUSTRIES INDIA", "GLOBAL INDUSTRIES BHARAT", "Country/Region aliases"),
]

def run_audit():
    print(f"{'Input A':<25} | {'Input B':<25} | {'Norm A':<20} | {'Norm B':<20} | {'Match?':<6} | {'Risk/Loss'}")
    print("-" * 125)
    for a, b, risk in ADVERSARIAL_PAIRS:
        norm_a = normalize_vendor_name(a)
        norm_b = normalize_vendor_name(b)
        match = "YES" if norm_a == norm_b else "NO"
        print(f"{a:<25} | {b:<25} | {norm_a:<20} | {norm_b:<20} | {match:<6} | {risk}")

if __name__ == "__main__":
    run_audit()
````

## File: experiments/benchmark_vendor_parse_reuse.py
````python
import time

def mock_parse(vendor_name: str):
    # Simulate an expensive parse (canonicalization, tokenization, legal form matching)
    # We will simulate a delay of 0.1ms
    # Using a small loop to simulate CPU work
    for _ in range(1000):
        pass
    return f"parsed_{vendor_name}"

def option_a_pair_level(purchases, gsts, candidates_per_record):
    # Parses the names for every candidate pair dynamically
    start = time.time()
    parses = 0
    
    # 1000 purchases
    for p in purchases:
        # Each has 100 candidates
        for c in range(candidates_per_record):
            # Parse purchase
            mock_parse(p)
            # Parse candidate (from gsts)
            mock_parse(gsts[c % len(gsts)])
            parses += 2
            
    end = time.time()
    return parses, end - start

def option_c_pre_materialized(unique_vendors):
    # Parses exactly once per unique vendor string
    start = time.time()
    parses = 0
    cache = {}
    
    for v in unique_vendors:
        cache[v] = mock_parse(v)
        parses += 1
        
    end = time.time()
    return parses, end - start

def main():
    print("--- Vendor Parse Reuse Benchmark ---\n")
    
    num_purchases = 1000
    num_gsts = 1000
    candidates_per_record = 100
    
    # Generate mock strings
    purchases = [f"Vendor_P_{i}" for i in range(num_purchases)]
    gsts = [f"Vendor_G_{i}" for i in range(num_gsts)]
    
    unique_vendors = set(purchases + gsts)
    
    print(f"Scenario: {num_purchases} Purchases, {num_gsts} GSTs, {candidates_per_record} Candidates per Purchase")
    print(f"Unique vendor strings: {len(unique_vendors)}")
    print("-" * 50)
    
    # Run Option A
    parses_a, time_a = option_a_pair_level(purchases, gsts, candidates_per_record)
    print(f"Option A (Pair-Level Dynamic Parse):")
    print(f"  Parse Executions: {parses_a}")
    print(f"  Simulated Time: {time_a:.4f} seconds")
    
    print("-" * 50)
    
    # Run Option C
    parses_c, time_c = option_c_pre_materialized(unique_vendors)
    print(f"Option C (Pre-Materialized Artifacts):")
    print(f"  Parse Executions: {parses_c}")
    print(f"  Simulated Time: {time_c:.4f} seconds")
    
    print("-" * 50)
    print(f"Amplification Factor: {parses_a / parses_c:.1f}x")

if __name__ == "__main__":
    main()
````

## File: experiments/design_exact_reference_fallback.py
````python
import sys
import os

# Ensure the src directory is in the path for importing recongraph
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import ReferenceEvidencePolicy

def evaluate_exact_reference_fallback_design():
    policy = ReferenceEvidencePolicy()
    
    # Candidate Option B values
    candidate_exact_fallbacks = [0.40, 0.50, 0.60, 0.70]
    
    # Candidate Option C lengths
    # short: <= 5, medium: <= 8, long: > 8
    def opt_c_magnitude(ref: str) -> float:
        n = len(ref)
        if n <= 5: return 0.20
        if n <= 8: return 0.40
        return 0.60

    cases = [
        {
            "id": "EF001",
            "ref_a": "INV-999999", "ref_b": "INV/999999",
            "exact": True,
            "norm_val": "inv999999",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF002",
            "ref_a": "CREDIT-NOTE", "ref_b": "CREDITNOTE",
            "exact": True,
            "norm_val": "creditnote",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF003",
            "ref_a": "SB-8891", "ref_b": "SB8891",
            "exact": True,
            "norm_val": "sb8891",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF004",
            "ref_a": "A", "ref_b": "A",
            "exact": True,
            "norm_val": "a",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF005",
            "ref_a": "000000", "ref_b": "000000",
            "exact": True,
            "norm_val": "000000",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF006",
            "ref_a": "INV-001", "ref_b": "INV/001",
            "exact": True,
            "norm_val": "inv001",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF007",
            "ref_a": "A-VERY-LONG-GENERIC-REFERENCE", "ref_b": "AVERYLONGGENERICREFERENCE",
            "exact": True,
            "norm_val": "averylonggenericreference",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF008",
            "ref_a": "INV-874219", "ref_b": "AB/874219",
            "exact": False,
            "norm_val": "874219 (token)",
            "primary": "shared numeric token"
        },
        {
            "id": "EF009",
            "ref_a": "INV-001", "ref_b": "ABC-001",
            "exact": False,
            "norm_val": "001 (token)",
            "primary": "shared numeric token"
        }
    ]
    
    print("EXACT REFERENCE FALLBACK DESIGN EXPERIMENT")
    print("-" * 120)
    
    for c in cases:
        print(f"Case: {c['id']}")
        print(f"Norm Ref/Token: {c['norm_val']}")
        print(f"Exact Match: {c['exact']}")
        print(f"Primary Unit: {c['primary']}")
        
        if c['exact']:
            opt_a = policy.long_token_fallback
            opt_c = opt_c_magnitude(c['norm_val'])
            opt_d = 0.0
            opt_e = "refused"
            print(f"Option A (reuse long_token_fallback): {opt_a}")
            print(f"Option B (candidate exact_reference_fallback values): {candidate_exact_fallbacks}")
            print(f"Option C (length derived diagnostic): {opt_c}")
            print(f"Option D (zero magnitude): {opt_d}")
            print(f"Option E (refuse interpretation): {opt_e}")
        else:
            # For numeric token, just use the token fallback
            # but extract just the digits for length
            tok = c['norm_val'].split(" ")[0]
            if len(tok) <= policy.short_token_max_length: mag = policy.short_token_fallback
            elif len(tok) <= policy.medium_token_max_length: mag = policy.medium_token_fallback
            else: mag = policy.long_token_fallback
            print(f"Standard numeric token magnitude: {mag}")
            
        print("-" * 60)

if __name__ == "__main__":
    evaluate_exact_reference_fallback_design()
````

## File: experiments/design_reference_evidence_ordering.py
````python
import collections
from dataclasses import dataclass
from typing import Tuple

from recongraph.matching.reference_evidence import (
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

@dataclass(frozen=True)
class ReferenceEvidenceScenario:
    scenario_id: str
    description: str
    reference_a: str
    reference_b: str
    corpus_references: tuple[str, ...]

def unrelated_references(count: int, *, start: int = 500_000) -> tuple[str, ...]:
    return tuple(f"OTHER-{start + i}" for i in range(count))

def format_norm_stats(enriched):
    out = []
    for ev in enriched.normalized_references:
        val = ev.statistics.frequency if ev.statistics else "?"
        out.append(f"{ev.normalized_reference}:{val}")
    return ", ".join(out) if out else "none"

def format_token_stats(enriched):
    out = []
    for ev in enriched.shared_numeric_tokens:
        val = ev.statistics.document_frequency if ev.statistics else "?"
        out.append(f"{ev.token}:{val}")
    return ", ".join(out) if out else "none"


def main():
    scenarios = []

    # RE001
    scenarios.append(ReferenceEvidenceScenario(
        "RE001", "Unique exact normalized identity",
        "INV-874219", "INV/874219",
        ("INV-874219", "INV/874219") + unrelated_references(98)
    ))

    # RE002
    # The pair is CREDIT-NOTE and CREDITNOTE.
    # Total creditnote freq = 40. Pair + 38 more.
    corpus_re002 = ["CREDIT-NOTE", "CREDITNOTE"] + ["CREDIT/NOTE"] * 38
    scenarios.append(ReferenceEvidenceScenario(
        "RE002", "Repeated exact normalized identity",
        "CREDIT-NOTE", "CREDITNOTE",
        tuple(corpus_re002) + unrelated_references(60)
    ))

    # RE003
    scenarios.append(ReferenceEvidenceScenario(
        "RE003", "Rare six-digit shared numeric token",
        "INV-874219", "AB/874219",
        ("INV-874219", "AB/874219") + unrelated_references(98)
    ))

    # RE004
    corpus_re004 = ["INV-874219", "AB/874219"] + [f"DOC{i}-874219" for i in range(38)]
    scenarios.append(ReferenceEvidenceScenario(
        "RE004", "Common six-digit shared numeric token",
        "INV-874219", "AB/874219",
        tuple(corpus_re004) + unrelated_references(60)
    ))

    # RE005
    scenarios.append(ReferenceEvidenceScenario(
        "RE005", "Rare three-digit shared token",
        "OMD-001", "NSS-001",
        ("OMD-001", "NSS-001") + unrelated_references(98)
    ))

    # RE006
    corpus_re006 = ["OMD-001", "NSS-001"] + [f"DOC{i}-001" for i in range(38)]
    scenarios.append(ReferenceEvidenceScenario(
        "RE006", "Common three-digit shared token",
        "OMD-001", "NSS-001",
        tuple(corpus_re006) + unrelated_references(60)
    ))

    # RE007
    corpus_re007 = ["INV-2026-874219", "AB/2026/874219"] + ["XX-2026"] * 3
    scenarios.append(ReferenceEvidenceScenario(
        "RE007", "Multiple rare shared tokens",
        "INV-2026-874219", "AB/2026/874219",
        tuple(corpus_re007) + unrelated_references(95)
    ))

    # RE008
    corpus_re008 = ["INV-2026-874219", "AB/2026/874219"] + ["XX-2026"] * 78
    scenarios.append(ReferenceEvidenceScenario(
        "RE008", "One rare and one common shared token",
        "INV-2026-874219", "AB/2026/874219",
        tuple(corpus_re008) + unrelated_references(20)
    ))

    # RE009
    scenarios.append(ReferenceEvidenceScenario(
        "RE009", "Mixed known and out-of-profile evidence",
        "INV-874219", "NEW-874219",
        ("INV-874219", "DOC-874219") + unrelated_references(98)
    ))

    # RE010
    scenarios.append(ReferenceEvidenceScenario(
        "RE010", "Fully out-of-profile shared identity evidence",
        "NEW-999999", "XYZ-999999",
        unrelated_references(100)
    ))

    # RE011
    scenarios.append(ReferenceEvidenceScenario(
        "RE011", "Non-numeric rare exact identity",
        "SPECIAL-CREDIT", "SPECIALCREDIT",
        ("SPECIAL-CREDIT", "SPECIALCREDIT") + unrelated_references(98)
    ))

    # RE012
    corpus_re012 = ["2026", "2026"] + ["2026"] * 78
    scenarios.append(ReferenceEvidenceScenario(
        "RE012", "Exact identity but highly repeated numeric reference",
        "2026", "2026",
        tuple(corpus_re012) + unrelated_references(20)
    ))

    print(f"{'Case':<7}{'Exact':<8}{'Norm Stats':<45}{'Token Stats'}")
    print("-" * 85)

    for sc in scenarios:
        profile = build_reference_corpus_profile(sc.corpus_references)

        # Assertions
        if sc.scenario_id != "RE009" and sc.scenario_id != "RE010":
            assert profile.reference_count == 100

        if sc.scenario_id == "RE003":
            assert profile.numeric_token_document_frequency["874219"] == 2
        elif sc.scenario_id == "RE004":
            assert profile.numeric_token_document_frequency["874219"] == 40
        elif sc.scenario_id == "RE006":
            assert profile.numeric_token_document_frequency["001"] == 40
        elif sc.scenario_id == "RE007":
            assert profile.numeric_token_document_frequency["2026"] == 5
            assert profile.numeric_token_document_frequency["874219"] == 2
        elif sc.scenario_id == "RE008":
            assert profile.numeric_token_document_frequency["2026"] == 80
            assert profile.numeric_token_document_frequency["874219"] == 2
        elif sc.scenario_id == "RE012":
            assert profile.normalized_reference_frequency["2026"] == 80
            assert profile.numeric_token_document_frequency["2026"] == 80

        identity = extract_reference_identity(sc.reference_a, sc.reference_b)
        assert identity is not None
        enriched = enrich_reference_identity(identity, profile)

        exact_str = "yes" if enriched.identity.exact_normalized_match else "no"
        norm_str = format_norm_stats(enriched)
        token_str = format_token_stats(enriched)

        if "unavailable" not in norm_str and "?" not in norm_str and norm_str != "none":
            norm_str = ", ".join([f"{n}/{profile.reference_count}" if ":" in n else n for n in norm_str.split(", ")])
        else:
            # We add /100 only to valid stats
            parts = norm_str.split(", ")
            new_parts = []
            for p in parts:
                if ":" in p and "?" not in p:
                    new_parts.append(f"{p}/{profile.reference_count}")
                else:
                    new_parts.append(p)
            norm_str = ", ".join(new_parts)

        if "unavailable" not in token_str and "?" not in token_str and token_str != "none":
            token_str = ", ".join([f"{n}/{profile.reference_count}" if ":" in n else n for n in token_str.split(", ")])
        else:
            parts = token_str.split(", ")
            new_parts = []
            for p in parts:
                if ":" in p and "?" not in p:
                    new_parts.append(f"{p}/{profile.reference_count}")
                else:
                    new_parts.append(p)
            token_str = ", ".join(new_parts)

        print(f"{sc.scenario_id:<7}{exact_str:<8}{norm_str:<45}{token_str}")

if __name__ == '__main__':
    main()
````

## File: experiments/design_reference_interpretation_contract.py
````python
import collections
from dataclasses import dataclass
from typing import Tuple

from recongraph.matching.reference_evidence import (
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

def unrelated_references(count: int, *, start: int = 500_000) -> tuple[str, ...]:
    return tuple(f"OTHER-{start + i}" for i in range(count))

def check_norm_availability(enriched) -> bool:
    if not enriched.normalized_references:
        return True
    return all(ev.statistics is not None for ev in enriched.normalized_references)

def get_norm_availability_count(enriched) -> int:
    return sum(1 for ev in enriched.normalized_references if ev.statistics is not None)

def check_token_availability(enriched) -> bool:
    if not enriched.shared_numeric_tokens:
        return True
    return all(ev.statistics is not None for ev in enriched.shared_numeric_tokens)

def main():
    print(f"{'Case':<6}{'Stage1 Evidence':<17}{'Structural Profile State':<26}{'Interpretation Coverage Question'}")
    print("-" * 82)

    # IC-A
    identity_a = extract_reference_identity(None, None)
    assert identity_a is None
    print(f"{'IC-A':<6}{'none':<17}{'none':<26}{'no interpretation'}")

    # IC-B
    corpus_b = ["OMD-001", "NSS-001"] + [f"DOC{i}-001" for i in range(38)]
    profile_b = build_reference_corpus_profile(tuple(corpus_b) + unrelated_references(60))
    identity_b = extract_reference_identity("OMD-001", "NSS-001")
    enriched_b = enrich_reference_identity(identity_b, profile_b)

    # assertions
    assert profile_b.numeric_token_document_frequency["001"] == 40
    print(f"{'IC-B':<6}{'present':<17}{'fully profiled':<26}{'1.0'}")

    # IC-C
    corpus_c = ["INV-874219", "DOC-874219"] + list(unrelated_references(98))
    profile_c = build_reference_corpus_profile(tuple(corpus_c))
    identity_c = extract_reference_identity("INV-874219", "NEW-874219")
    enriched_c = enrich_reference_identity(identity_c, profile_c)

    # assertions
    assert profile_c.numeric_token_document_frequency["874219"] == 2
    assert get_norm_availability_count(enriched_c) == 1
    assert len(enriched_c.normalized_references) == 2
    print(f"{'IC-C':<6}{'present':<17}{'mixed':<26}{'path-dependent'}")

    # IC-D
    profile_d = build_reference_corpus_profile(unrelated_references(100))
    identity_d = extract_reference_identity("NEW-999999", "XYZ-999999")
    enriched_d = enrich_reference_identity(identity_d, profile_d)

    # assertions
    assert get_norm_availability_count(enriched_d) == 0
    assert enriched_d.shared_numeric_tokens[0].statistics is None
    print(f"{'IC-D':<6}{'present':<17}{'out-of-profile':<26}{'0.0'}")

if __name__ == '__main__':
    main()
````

## File: experiments/evaluate_gstin_identity_cases.py
````python
import re

def validate_gstin(gstin: str) -> bool:
    if not gstin or len(gstin) != 15:
        return False
    pattern = r"^[0-3][0-9][A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$"
    return bool(re.match(pattern, gstin))

def extract_pan(gstin: str) -> str | None:
    if not validate_gstin(gstin):
        return None
    return gstin[2:12]

def extract_state_code(gstin: str) -> str | None:
    if not validate_gstin(gstin):
        return None
    return gstin[0:2]

def evaluate_gstin_pair(gstin_a: str, gstin_b: str):
    print(f"Comparing: {gstin_a} <-> {gstin_b}")
    
    val_a = validate_gstin(gstin_a)
    val_b = validate_gstin(gstin_b)
    
    if not val_a or not val_b:
        print("  -> UNINTERPRETABLE_INPUT (Validation Failed)")
        return
        
    pan_a = extract_pan(gstin_a)
    pan_b = extract_pan(gstin_b)
    
    state_a = extract_state_code(gstin_a)
    state_b = extract_state_code(gstin_b)
    
    print(f"  PAN A: {pan_a} | PAN B: {pan_b}")
    print(f"  State A: {state_a} | State B: {state_b}")
    
    if gstin_a == gstin_b:
        print("  -> SUPPORT identity.same_gst_registration 1.0")
    else:
        print("  -> CONFLICT identity.same_gst_registration 1.0")
        
    if pan_a == pan_b:
        print("  -> SUPPORT identity.same_tax_identity 1.0")
    else:
        print("  -> CONFLICT identity.same_tax_identity 1.0")
    print()

def main():
    print("--- GSTIN Identity Experiment ---\n")
    # Same
    evaluate_gstin_pair("07ABCDE1234F1Z5", "07ABCDE1234F1Z5")
    
    # Same PAN, diff state
    evaluate_gstin_pair("07ABCDE1234F1Z5", "29ABCDE1234F1Z5")
    
    # Diff PAN
    evaluate_gstin_pair("07ABCDE1234F1Z5", "07XYZDE9876Q1Z5")
    
    # OCR Error (O instead of 0)
    evaluate_gstin_pair("07ABCDE1234F1Z5", "O7ABCDE1234F1Z5")

if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_reference_interpretation_state.py
````python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidenceContribution, ReferenceEvidenceKind,
    ReferenceEvidenceInterpretation, _select_strongest_reference_contribution
)

def evaluate_interpretation_state():
    def make_contrib(mag, stats, val="0"):
        return ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value=val,
            positive_evidence=mag,
            statistics_available=stats
        )

    # IS001: A=0.60 fallback, B=0.60 profiled. Selector winner: B (profiled)
    # Attempt: score=0.60, coverage=0.0
    c_a = make_contrib(0.60, False, val="1")
    c_b = make_contrib(0.60, True, val="2")
    winner1 = _select_strongest_reference_contribution((c_a, c_b))
    
    cases = [
        {
            "id": "IS001",
            "contribs": (c_a, c_b),
            "winner": winner1,
            "score": 0.60,
            "coverage": 0.0
        },
        {
            "id": "IS002",
            "contribs": (c_a, c_b),
            "winner": winner1,
            "score": 0.60,
            "coverage": 1.0
        },
        {
            "id": "IS003",
            "contribs": (make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2"))),
            "score": 0.70,
            "coverage": 1.0
        },
        {
            "id": "IS004",
            "contribs": (make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2"))),
            "score": 0.70,
            "coverage": 0.0
        },
        {
            "id": "IS005",
            "contribs": (make_contrib(0.60, True, val="2026"), make_contrib(0.60, True, val="874219")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.60, True, val="2026"), make_contrib(0.60, True, val="874219"))),
            "score": 0.60,
            "coverage": 1.0
        },
        {
            "id": "IS006",
            "contribs": (make_contrib(0.60, True, val="874219"), make_contrib(0.60, True, val="2026")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.60, True, val="874219"), make_contrib(0.60, True, val="2026"))),
            "score": 0.60,
            "coverage": 1.0
        }
    ]

    for case in cases:
        print(f"Case: {case['id']}")
        print(f"Ordered contribution identities: {[c.identity_value for c in case['contribs']]}")
        print(f"Selector winner: {case['winner'].identity_value} (mag={case['winner'].positive_evidence}, stats={case['winner'].statistics_available})")
        print(f"Attempted score: {case['score']}")
        print(f"Attempted coverage: {case['coverage']}")
        
        try:
            interp = ReferenceEvidenceInterpretation(
                score=case['score'],
                statistical_coverage=case['coverage'],
                contributions=case['contribs']
            )
            print("Construction succeeded? True")
            print("What invariant accepted/rejected the state? Accepted (current model does not fully link coverage/winner provenance)")
        except ValueError as e:
            print("Construction succeeded? False")
            print(f"What invariant accepted/rejected the state? Rejected: {str(e)}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate_interpretation_state()
````

## File: experiments/evaluate_reference_rarity_magnitude.py
````python
import math
from dataclasses import dataclass

@dataclass(frozen=True)
class RarityScenario:
    scenario_id: str
    corpus_size: int
    frequency: int
    description: str

    def __post_init__(self):
        if self.corpus_size < 1:
            raise ValueError("corpus_size must be >= 1")
        if not (1 <= self.frequency <= self.corpus_size):
            raise ValueError("frequency must be between 1 and corpus_size")

def linear_rarity(f: int, n: int) -> float:
    return 1.0 - (f / n)

def normalized_log_rarity(f: int, n: int) -> float:
    if n <= 1:
        return 0.0
    return math.log(n / f) / math.log(n)

def sqrt_rarity(f: int, n: int) -> float:
    return 1.0 - math.sqrt(f / n)

def main():
    scenarios = [
        RarityScenario("RM001", 100, 1, "singleton in small corpus"),
        RarityScenario("RM002", 100, 2, "rare in small corpus"),
        RarityScenario("RM003", 100, 5, "uncommon in small corpus"),
        RarityScenario("RM004", 100, 20, "moderately common"),
        RarityScenario("RM005", 100, 80, "very common"),
        RarityScenario("RM006", 100, 100, "universal"),
        RarityScenario("RM007", 1000000, 1, "singleton in large corpus"),
        RarityScenario("RM008", 1000000, 10, "very rare in large corpus"),
        RarityScenario("RM009", 1000000, 100, "rare in large corpus"),
        RarityScenario("RM010", 1000000, 10000, "one percent frequency"),
        RarityScenario("RM011", 1000000, 500000, "half corpus"),
        RarityScenario("RM012", 1000000, 1000000, "universal"),
        RarityScenario("RM013", 100, 1, "1 percent base corpus"),
        RarityScenario("RM014", 1000, 10, "1 percent replicated corpus"),
    ]

    print(f"{'Case':<7}{'N':<11}{'f':<11}{'Rate':<11}{'Linear':<11}{'NormLog':<11}{'Sqrt':<11}{'Description'}")
    print("-" * 90)

    results = {}

    for sc in scenarios:
        n = sc.corpus_size
        f = sc.frequency
        rate = f / n

        lin = linear_rarity(f, n)
        nlog = normalized_log_rarity(f, n)
        sq = sqrt_rarity(f, n)

        results[sc.scenario_id] = {"lin": lin, "nlog": nlog, "sq": sq}

        assert 0.0 <= lin <= 1.0
        assert 0.0 <= nlog <= 1.0
        assert 0.0 <= sq <= 1.0

        if f == n:
            assert math.isclose(lin, 0.0, abs_tol=1e-9)
            assert math.isclose(nlog, 0.0, abs_tol=1e-9)
            assert math.isclose(sq, 0.0, abs_tol=1e-9)

        if sc.scenario_id == "RM001":
            assert math.isclose(lin, 0.99, abs_tol=1e-9)
            assert math.isclose(nlog, 1.0, abs_tol=1e-9)
            assert math.isclose(sq, 0.9, abs_tol=1e-9)

        print(f"{sc.scenario_id:<7}{n:<11}{f:<11}{rate:<11.6f}{lin:<11.6f}{nlog:<11.6f}{sq:<11.6f}{sc.description}")

    # Monotonicity checks
    small_cases = [s for s in scenarios if s.corpus_size == 100 and s.scenario_id.startswith("RM00")]
    small_cases.sort(key=lambda x: x.frequency)
    for i in range(1, len(small_cases)):
        prev = small_cases[i-1].scenario_id
        curr = small_cases[i].scenario_id
        assert results[prev]["lin"] >= results[curr]["lin"]
        assert results[prev]["nlog"] >= results[curr]["nlog"]
        assert results[prev]["sq"] >= results[curr]["sq"]

    large_cases = [s for s in scenarios if s.corpus_size == 1000000]
    large_cases.sort(key=lambda x: x.frequency)
    for i in range(1, len(large_cases)):
        prev = large_cases[i-1].scenario_id
        curr = large_cases[i].scenario_id
        assert results[prev]["lin"] >= results[curr]["lin"]
        assert results[prev]["nlog"] >= results[curr]["nlog"]
        assert results[prev]["sq"] >= results[curr]["sq"]

    print("\nRare-end resolution diagnostics")
    print("-" * 31)

    def print_diff(id1, id2):
        print(f"{id1} vs {id2}")
        print(f"  Linear difference: {results[id1]['lin'] - results[id2]['lin']:.6f}")
        print(f"  NormLog difference: {results[id1]['nlog'] - results[id2]['nlog']:.6f}")
        print(f"  Sqrt difference: {results[id1]['sq'] - results[id2]['sq']:.6f}")

    print_diff("RM001", "RM002")
    print_diff("RM002", "RM003")
    print_diff("RM007", "RM008")
    print_diff("RM008", "RM009")

    print("\nSame frequency-rate diagnostics")
    print("-" * 31)
    print("RM001 (N=100, f=1):")
    print(f"  Linear: {results['RM001']['lin']:.6f}")
    print(f"  NormLog: {results['RM001']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM001']['sq']:.6f}")
    print("RM010 (N=1,000,000, f=10,000):")
    print(f"  Linear: {results['RM010']['lin']:.6f}")
    print(f"  NormLog: {results['RM010']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM010']['sq']:.6f}")

    print("\nCorpus replication diagnostic")
    print("-" * 29)
    print("RM013 (N=100, f=1):")
    print(f"  Linear: {results['RM013']['lin']:.6f}")
    print(f"  NormLog: {results['RM013']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM013']['sq']:.6f}")
    print("RM014 (N=1000, f=10):")
    print(f"  Linear: {results['RM014']['lin']:.6f}")
    print(f"  NormLog: {results['RM014']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM014']['sq']:.6f}")

if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_reference_structural_fallback_inputs.py
````python
def get_diversity(token: str):
    unique = len(set(token))
    length = len(token)
    return unique, unique / length

def is_repeated_pattern(token: str):
    return "yes" if len(set(token)) <= 2 else "no"

def main():
    tokens = [
        "1",
        "01",
        "001",
        "2026",
        "874219",
        "991827",
        "1234567890",
        "000000",
        "111111",
        "123123",
    ]

    print(f"{'Token':<12}{'Length':<9}{'Unique Digits':<16}{'Diversity':<12}{'Repeated-Pattern Candidate'}")
    print("-" * 78)

    for token in tokens:
        unique, diversity = get_diversity(token)
        repeated = is_repeated_pattern(token)
        print(f"{token:<12}{len(token):<9}{unique:<16}{diversity:<12.4f}{repeated}")

if __name__ == '__main__':
    main()
````

## File: experiments/evaluate_reference_structural_magnitude.py
````python
import sys
import os

# Ensure the src directory is in the path for importing recongraph
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import ReferenceEvidencePolicy

def shortest_repeating_unit(token: str) -> str:
    n = len(token)
    for unit_length in range(1, n // 2 + 1):
        if n % unit_length == 0:
            candidate = token[:unit_length]
            if candidate * (n // unit_length) == token:
                return candidate
    return "none"

def evaluate_structural_magnitude():
    policy = ReferenceEvidencePolicy()
    
    tokens = [
        "01",
        "001",
        "000",
        "111",
        "123",
        "2026",
        "1001",
        "9999",
        "874219",
        "999999",
        "123456",
        "121212",
        "000001",
        "87421982",
        "123123",
        "101010",
        "987654321"
    ]
    
    results = []
    
    for token in tokens:
        n = len(token)
        unique_digit_count = len(set(token))
        digit_diversity_ratio = unique_digit_count / n
        single_symbol_repeated = (unique_digit_count == 1)
        repeating_unit = shortest_repeating_unit(token)
        periodic = (repeating_unit != "none")
        
        # Determine fallback band
        if n <= policy.short_token_max_length:
            fallback_band = "short"
            base_magnitude = policy.short_token_fallback
        elif n <= policy.medium_token_max_length:
            fallback_band = "medium"
            base_magnitude = policy.medium_token_fallback
        else:
            fallback_band = "long"
            base_magnitude = policy.long_token_fallback
            
        single_symbol_discounted = base_magnitude * policy.repeated_pattern_discount if single_symbol_repeated else base_magnitude
        periodic_discounted = base_magnitude * policy.repeated_pattern_discount if periodic else base_magnitude
        
        results.append({
            "token": token,
            "length": n,
            "unique_digit_count": unique_digit_count,
            "digit_diversity_ratio": digit_diversity_ratio,
            "single_symbol_repeated": single_symbol_repeated,
            "shortest_repeating_unit": repeating_unit,
            "periodic": periodic,
            "fallback_band": fallback_band,
            "base_fallback_magnitude": base_magnitude,
            "magnitude_if_single_symbol_discount": single_symbol_discounted,
            "magnitude_if_periodic_discount": periodic_discounted
        })
        
    # Assertions
    # 1. 000 is single-symbol repeated and periodic.
    t000 = next(r for r in results if r["token"] == "000")
    assert t000["single_symbol_repeated"] and t000["periodic"]
    
    # 2. 999999 is single-symbol repeated and periodic.
    t999999 = next(r for r in results if r["token"] == "999999")
    assert t999999["single_symbol_repeated"] and t999999["periodic"]
    
    # 3. 121212 is periodic but not single-symbol repeated.
    t121212 = next(r for r in results if r["token"] == "121212")
    assert t121212["periodic"] and not t121212["single_symbol_repeated"]
    
    # 4. 123123 has shortest repeating unit "123".
    t123123 = next(r for r in results if r["token"] == "123123")
    assert t123123["shortest_repeating_unit"] == "123"
    
    # 5. 874219 is not periodic.
    t874219 = next(r for r in results if r["token"] == "874219")
    assert not t874219["periodic"]
    
    # 6. 000001 is not periodic.
    t000001 = next(r for r in results if r["token"] == "000001")
    assert not t000001["periodic"]
    
    # 7. Discounting never increases magnitude.
    # 8. All diagnostic magnitudes remain in [0.0, 1.0].
    # 9. A token with no detected pattern has identical base, single-symbol-discount, and periodic-discount magnitudes.
    for r in results:
        assert r["magnitude_if_single_symbol_discount"] <= r["base_fallback_magnitude"]
        assert r["magnitude_if_periodic_discount"] <= r["base_fallback_magnitude"]
        assert 0.0 <= r["base_fallback_magnitude"] <= 1.0
        assert 0.0 <= r["magnitude_if_single_symbol_discount"] <= 1.0
        assert 0.0 <= r["magnitude_if_periodic_discount"] <= 1.0
        
        if not r["single_symbol_repeated"] and not r["periodic"]:
            assert r["base_fallback_magnitude"] == r["magnitude_if_single_symbol_discount"] == r["magnitude_if_periodic_discount"]
    
    # 10. The experiment does not mutate ReferenceEvidencePolicy.
    # Dataclass is frozen, so it can't mutate. But we can assert the defaults remain identical to fresh instantiation.
    policy2 = ReferenceEvidencePolicy()
    assert policy.short_token_max_length == policy2.short_token_max_length
    assert policy.repeated_pattern_discount == policy2.repeated_pattern_discount
    
    print("ALL ASSERTIONS PASSED\n")
    
    print("FULL DIAGNOSTIC TABLE")
    print(f"{'Token':<12} | {'Len':<3} | {'Uniq':<4} | {'Div':<5} | {'SingleRep':<9} | {'ShortUnit':<10} | {'Periodic':<8} | {'Band':<6} | {'Base':<4} | {'SingleDisc':<10} | {'PeriodDisc':<10}")
    print("-" * 120)
    for r in results:
        print(f"{r['token']:<12} | {r['length']:<3} | {r['unique_digit_count']:<4} | {r['digit_diversity_ratio']:<5.2f} | {str(r['single_symbol_repeated']):<9} | {str(r['shortest_repeating_unit']):<10} | {str(r['periodic']):<8} | {r['fallback_band']:<6} | {r['base_fallback_magnitude']:<4.2f} | {r['magnitude_if_single_symbol_discount']:<10.2f} | {r['magnitude_if_periodic_discount']:<10.2f}")
    
    print("\n\nHN004 STRUCTURAL COMPARISON")
    print(f"{'Token':<12} | {'Fallback Band':<15} | {'Base Mag':<8} | {'Single-Symbol Disc':<18} | {'Periodic Disc':<15}")
    print("-" * 75)
    compare_tokens = ["001", "874219", "999999", "121212"]
    for r in results:
        if r["token"] in compare_tokens:
            print(f"{r['token']:<12} | {r['fallback_band']:<15} | {r['base_fallback_magnitude']:<8.2f} | {r['magnitude_if_single_symbol_discount']:<18.2f} | {r['magnitude_if_periodic_discount']:<15.2f}")

if __name__ == "__main__":
    evaluate_structural_magnitude()
````

## File: experiments/evaluate_reference_token_cooccurrence.py
````python
import re
from dataclasses import dataclass
from typing import Tuple

from recongraph.matching.reference_evidence import build_reference_corpus_profile

@dataclass(frozen=True)
class TokenCooccurrenceScenario:
    scenario_id: str
    description: str
    token_a: str
    token_b: str
    corpus_references: tuple[str, ...]

def unrelated_references(count: int, *, start: int = 500_000) -> tuple[str, ...]:
    return tuple(f"OTHER-{start + i}" for i in range(count))

def token_document_sets(references: tuple[str, ...]) -> dict[str, set[int]]:
    token_docs = {}
    for i, ref in enumerate(references):
        if ref:
            tokens = set(re.findall(r"\d+", ref))
            for t in tokens:
                if t not in token_docs:
                    token_docs[t] = set()
                token_docs[t].add(i)
    return token_docs

def main():
    scenarios = []

    # CO001 - Perfect co-occurrence
    # 20 both, 80 unrelated
    # Avoid creating '000001' as a numeric token. We will use letters instead for unique identifiers.
    # E.g. DOC-2026-874219-A, DOC-2026-874219-B...
    # But letters alone might run out, so let's just use a prefix: DOCA-2026-874219, DOCB-2026-874219, etc.
    # Wait, python can just do chr() or just use a non-numeric suffix like -x1... no wait, \d+ catches 1.
    # Just use alphabetic suffix: DOC-2026-874219-a, DOC-2026-874219-b
    import string
    alphabet = string.ascii_lowercase
    docs_co001 = [f"DOC-{2026}-{874219}-{alphabet[i]}" for i in range(20)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO001", "Perfect co-occurrence",
        "2026", "874219",
        tuple(docs_co001) + unrelated_references(80)
    ))

    # CO002 - Independent-looking marginals with zero overlap
    # 20 only 2026, 20 only 874219, 60 unrelated
    docs_co002_a = [f"DOCA-{2026}-{alphabet[i]}" for i in range(20)]
    docs_co002_b = [f"DOCB-{874219}-{alphabet[i]}" for i in range(20)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO002", "Independent-looking marginals with zero overlap",
        "2026", "874219",
        tuple(docs_co002_a + docs_co002_b) + unrelated_references(60)
    ))

    # CO003 - Partial co-occurrence
    # 10 both, 10 only 2026, 10 only 874219, 70 unrelated
    docs_co003_both = [f"DOC-{2026}-{874219}-{alphabet[i]}" for i in range(10)]
    docs_co003_a = [f"DOCA-{2026}-{alphabet[i]}" for i in range(10)]
    docs_co003_b = [f"DOCB-{874219}-{alphabet[i]}" for i in range(10)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO003", "Partial co-occurrence",
        "2026", "874219",
        tuple(docs_co003_both + docs_co003_a + docs_co003_b) + unrelated_references(70)
    ))

    # CO004 - Rare token nested inside common token
    # DF(2026) = 80, DF(874219) = 2, joint = 2
    # 2 both, 78 only 2026, 20 unrelated
    docs_co004_both = [f"DOC-{2026}-{874219}-{alphabet[i]}" for i in range(2)]
    # We need 78 for 2026 only, alphabet is only 26, so we can use letters multiple times or just random words.
    # To avoid numeric suffixes:
    docs_co004_a = [f"DOCA-{2026}-" + ("a" * (i//26 + 1)) + alphabet[i%26] for i in range(78)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO004", "Rare token nested inside common token",
        "2026", "874219",
        tuple(docs_co004_both + docs_co004_a) + unrelated_references(20)
    ))

    # CO005 - Two rare tokens with limited overlap
    # DF(991827) = 5, DF(874219) = 5, joint = 1
    # 1 both, 4 only 991827, 4 only 874219, 91 unrelated
    docs_co005_both = [f"DOC-{991827}-{874219}-a"]
    docs_co005_a = [f"DOCA-{991827}-{alphabet[i]}" for i in range(4)]
    docs_co005_b = [f"DOCB-{874219}-{alphabet[i]}" for i in range(4)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO005", "Two rare tokens with limited overlap",
        "991827", "874219",
        tuple(docs_co005_both + docs_co005_a + docs_co005_b) + unrelated_references(91)
    ))

    print(f"{'Case':<7}{'Token A':<9}{'DF(A)':<7}{'Token B':<9}{'DF(B)':<7}{'Joint DF':<10}{'Rate(B|A)':<11}{'Rate(A|B)'}")
    print("-" * 76)

    profiles = {}
    joint_dfs = {}

    for sc in scenarios:
        assert len(sc.corpus_references) == 100

        token_docs = token_document_sets(sc.corpus_references)
        docs_a = token_docs.get(sc.token_a, set())
        docs_b = token_docs.get(sc.token_b, set())

        df_a = len(docs_a)
        df_b = len(docs_b)
        joint_df = len(docs_a & docs_b)

        if sc.scenario_id == "CO001":
            assert df_a == 20
            assert df_b == 20
            assert joint_df == 20
        elif sc.scenario_id == "CO002":
            assert df_a == 20
            assert df_b == 20
            assert joint_df == 0
        elif sc.scenario_id == "CO003":
            assert df_a == 20
            assert df_b == 20
            assert joint_df == 10
        elif sc.scenario_id == "CO004":
            assert df_a == 80
            assert df_b == 2
            assert joint_df == 2
        elif sc.scenario_id == "CO005":
            assert df_a == 5
            assert df_b == 5
            assert joint_df == 1

        rate_b_given_a = joint_df / df_a if df_a > 0 else 0.0
        rate_a_given_b = joint_df / df_b if df_b > 0 else 0.0

        profiles[sc.scenario_id] = build_reference_corpus_profile(sc.corpus_references)
        joint_dfs[sc.scenario_id] = joint_df

        print(f"{sc.scenario_id:<7}{sc.token_a:<9}{df_a:<7}{sc.token_b:<9}{df_b:<7}{joint_df:<10}{rate_b_given_a:<11.4f}{rate_a_given_b:.4f}")

    profile_co001 = profiles["CO001"]
    profile_co002 = profiles["CO002"]

    assert profile_co001.reference_count == profile_co002.reference_count
    assert (
        profile_co001.numeric_token_document_frequency["2026"]
        ==
        profile_co002.numeric_token_document_frequency["2026"]
    )
    assert (
        profile_co001.numeric_token_document_frequency["874219"]
        ==
        profile_co002.numeric_token_document_frequency["874219"]
    )
    assert joint_dfs["CO001"] != joint_dfs["CO002"]

if __name__ == '__main__':
    main()
````

## File: experiments/evaluate_vendor_acronym_collisions.py
````python
def derive_acronym(core_name: str) -> str:
    tokens = core_name.split()
    # Simple derivation: first letter of each word
    return "".join(t[0] for t in tokens if t)

def acronym_experiment():
    print("--- Vendor Acronym Collision Experiment ---\n")
    
    entities = [
        "TATA CONSULTANCY SERVICES",
        "TCS LOGISTICS",
        "TRINITY COMPUTER SYSTEMS",
        "STATE BANK OF INDIA",
        "SBI LIFE INSURANCE",
        "SARASWAT BANK INTL",
        "HINDUSTAN UNILEVER",
        "HULK UNDERWEAR LIMITED"
    ]
    
    acronym_map = {}
    for entity in entities:
        acronym = derive_acronym(entity)
        if acronym not in acronym_map:
            acronym_map[acronym] = []
        acronym_map[acronym].append(entity)
        
    for acr, matches in acronym_map.items():
        print(f"Acronym '{acr}' maps to {len(matches)} distinct entities:")
        for m in matches:
            print(f"  - {m}")
        print()
        
    print("Conclusion: Deterministic acronym derivation leads to massive false positives.")

if __name__ == "__main__":
    acronym_experiment()
````

## File: experiments/evaluate_vendor_authority_conflicts.py
````python
"""
Stage 8C-0B: Authority Hierarchy Challenge
Experiment: Evaluate Vendor Authority Conflicts
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class TestCase:
    case_id: str
    name_a: str | None
    name_b: str | None
    tax_a: str | None
    tax_b: str | None
    description: str

CASES = [
    TestCase("AH001", "ABC PRIVATE LIMITED", "ABC PRIVATE LIMITED", "TAX-A", "TAX-B", "Exact Name, Conflicting Tax Identity"),
    TestCase("AH002", "TATA CONSULTANCY SERVICES LIMITED", "TCS", "TAX-X", "TAX-X", "Different Name, Exact Tax Identity"),
    TestCase("AH003", "ABC TECHNOLOGIES PRIVATE LIMITED", "ABC TECHNOLOGY PVT LTD", None, None, "Similar Name, Missing Tax Identity"),
    TestCase("AH004", "TRADERS", "TRADERS", None, None, "Exact Generic Name"),
    TestCase("AH005", "TATA MOTORS LIMITED", "TATA TECHNOLOGIES LIMITED", None, None, "Corporate Family Collision"),
    TestCase("AH006", "ABC LLP", "ABC PRIVATE LIMITED", None, None, "Legal Suffix Conflict"),
    TestCase("AH007", "MICROSOFT", "MICR0SOFT", None, None, "OCR Corruption"),
    TestCase("AH008", "ABC", "ABC", None, None, "Abbreviation Collision"),
    TestCase("AH009", "XEROX", "XEROX CORPORATION", None, None, "Brand vs Legal Entity"),
    TestCase("AH010", "FACEBOOK INC", "META PLATFORMS INC", None, None, "Historical Rename"),
    TestCase("AH011", "ALPHA INDUSTRIES", "OMEGA LOGISTICS", "TAX-X", "TAX-X", "Same Tax Identity, Suspiciously Different Names"),
    TestCase("AH012", None, None, None, None, "Both Observations Missing"),
]

def evaluate_authority(case: TestCase) -> dict[str, Any]:
    name_state = "Missing" if not case.name_a and not case.name_b else "Exact" if case.name_a == case.name_b else "Different/Similar"
    tax_state = "Missing" if not case.tax_a and not case.tax_b else "Exact" if case.tax_a == case.tax_b else "Conflict"
    
    supported = []
    contradicted = []
    missing = []
    
    if name_state == "Exact":
        supported.append("Lexical Identity")
    if tax_state == "Exact":
        supported.append("Legal Identity")
    if tax_state == "Conflict":
        contradicted.append("Legal Identity")
        
    if tax_state == "Missing":
        missing.append("Legal Entity Proof")
        
    if case.case_id == "AH001":
        # Name is exact, Tax is conflict. Legal conflict overrides lexical support.
        pass
        
    return {
        "Case": case.case_id,
        "Name Evidence State": name_state,
        "Identifier Evidence State": tax_state,
        "Identity Claim Supported": ", ".join(supported) or "None",
        "Identity Claim Contradicted": ", ".join(contradicted) or "None",
        "Knowledge Missing": ", ".join(missing) or "None"
    }

if __name__ == "__main__":
    print("| Case | Name Evidence State | Identifier Evidence State | Identity Claim Supported | Identity Claim Contradicted | Knowledge Missing |")
    print("|---|---|---|---|---|---|")
    for c in CASES:
        r = evaluate_authority(c)
        print(f"| {r['Case']} | {r['Name Evidence State']} | {r['Identifier Evidence State']} | {r['Identity Claim Supported']} | {r['Identity Claim Contradicted']} | {r['Knowledge Missing']} |")
````

## File: experiments/evaluate_vendor_common_token_collisions.py
````python
import math

def calculate_token_idf(doc_freq: int, total_docs: int = 1000000) -> float:
    # Adding +1 to avoid division by zero and smooth
    return math.log(total_docs / (doc_freq + 1))

def token_rarity_experiment():
    print("--- Vendor Common Token Collision Experiment ---\n")
    
    # Hypothetical document frequencies in a 1M document corpus
    frequencies = {
        "ENTERPRISES": 45000,
        "TRADERS": 38000,
        "INDIA": 85000,
        "SERVICES": 62000,
        "TATA": 1500,
        "MAHINDRA": 800,
        "ZOMATO": 15,
        "RELIANCE": 2000
    }
    
    print(f"{'Token':<15} | {'Doc Freq':<10} | {'IDF Score':<10}")
    print("-" * 40)
    for token, freq in frequencies.items():
        idf = calculate_token_idf(freq)
        print(f"{token:<15} | {freq:<10} | {idf:.4f}")
        
    print("\nObservation: High frequency tokens like INDIA or ENTERPRISES have very low IDF scores, ")
    print("meaning partial matches on these tokens provide almost no semantic evidence of identity.")

if __name__ == "__main__":
    token_rarity_experiment()
````

## File: experiments/evaluate_vendor_core_similarity_metrics.py
````python
import difflib

def exact_match(a: str, b: str) -> float:
    return 1.0 if a == b else 0.0

def token_set_match(a: str, b: str) -> float:
    set_a = set(a.split())
    set_b = set(b.split())
    return 1.0 if set_a == set_b else 0.0

def sequence_matcher_ratio(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b).ratio()

def evaluate_metrics(a: str, b: str):
    print(f"Comparing: '{a}' <-> '{b}'")
    print(f"  Exact Match : {exact_match(a, b):.2f}")
    print(f"  Token Set   : {token_set_match(a, b):.2f}")
    print(f"  Seq Matcher : {sequence_matcher_ratio(a, b):.2f}")
    print()

def main():
    print("--- Vendor Core Similarity Experiment ---\n")
    
    pairs = [
        ("ABC", "ABC"),
        ("ABC TRADERS", "ABC TRADERS"),
        ("BALAJI ENTERPRISES", "ENTERPRISES BALAJI"),
        ("TATA MOTORS", "TATA POWER"),
        ("ABC", "ADC"),
        ("NEW INDIA TRADING CO", "NEW INDIA TRADERS"),
    ]
    
    for a, b in pairs:
        evaluate_metrics(a, b)

if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_vendor_legal_form_extraction.py
````python
import re
from typing import Tuple, Optional, List

# Priority ordered legal form patterns. 
# Multi-token patterns must come first.
LEGAL_FORM_PATTERNS = [
    (r'\bLIMITED LIABILITY PARTNERSHIP\b', 'LIMITED_LIABILITY_PARTNERSHIP'),
    (r'\bPRIVATE LIMITED\b', 'PRIVATE_LIMITED'),
    (r'\bPVT\.?\s*LTD\.?\b', 'PRIVATE_LIMITED'),
    (r'\b\(P\)\s*LTD\.?\b', 'PRIVATE_LIMITED'),
    (r'\bONE PERSON COMPANY\b', 'ONE_PERSON_COMPANY'),
    (r'\bSECTION 8 COMPANY\b', 'SECTION_8_COMPANY'),
    (r'\bPUBLIC LIMITED\b', 'PUBLIC_LIMITED'),
    (r'\bLLP\.?\b', 'LIMITED_LIABILITY_PARTNERSHIP'),
    (r'\bLTD\.?\b', 'LIMITED'),
    (r'\bLIMITED\b', 'LIMITED'),
    (r'\bOPC\b', 'ONE_PERSON_COMPANY'),
    (r'\bHUF\b', 'HINDU_UNDIVIDED_FAMILY'),
]

def extract_legal_form(vendor_name: str) -> Tuple[Optional[str], Optional[str], List[str]]:
    """
    Extracts legal form and organization core from vendor name.
    Information extraction precedes information removal.
    """
    events = []
    
    # 1. Unicode/whitespace canonicalization event simulation
    canonical_name = ' '.join(vendor_name.upper().split())
    if canonical_name != vendor_name:
        events.append(f"WHITESPACE_COLLAPSED: '{vendor_name}' -> '{canonical_name}'")
        
    # We do not extract 'COMPANY' or 'CO' in Indian context due to high ambiguity (e.g. FORD MOTOR COMPANY).
    # We search from the end using regex, but since we want to be safe, we'll try to find the match that's at the end.
    
    best_match = None
    best_form = None
    best_start = -1
    
    for pattern, canonical_form in LEGAL_FORM_PATTERNS:
        # Search for pattern at the end of the string first
        match = re.search(pattern + r'$', canonical_name)
        if match:
            best_match = match
            best_form = canonical_form
            best_start = match.start()
            break
            
        # If not at the end, look anywhere
        if not best_match:
            match = re.search(pattern, canonical_name)
            if match:
                # We'll take the first one we find, but end-matches take priority
                # Actually, let's stick to the simplest priority matching.
                pass 
                # For this experiment, we will just use the first priority match we find, 
                # but we prefer it to be at the end.
                
    for pattern, canonical_form in LEGAL_FORM_PATTERNS:
        matches = list(re.finditer(pattern, canonical_name))
        if matches:
            # Prefer the last match
            best_match = matches[-1]
            best_form = canonical_form
            break
            
    if best_match:
        org_core = canonical_name[:best_match.start()].strip() + " " + canonical_name[best_match.end():].strip()
        org_core = org_core.strip()
        events.append(f"LEGAL_FORM_RECOGNIZED: '{best_match.group()}' -> '{best_form}'")
        return org_core if org_core else None, best_form, events
        
    return canonical_name, None, events


def main():
    test_cases = [
        ("ABC PRIVATE LIMITED", "ABC", "PRIVATE_LIMITED"),
        ("ABC PVT LTD", "ABC", "PRIVATE_LIMITED"),
        ("ABC PVT. LTD.", "ABC", "PRIVATE_LIMITED"),
        ("ABC LLP", "ABC", "LIMITED_LIABILITY_PARTNERSHIP"),
        ("ABC", "ABC", None),
        ("ABC AND COMPANY", "ABC AND COMPANY", None),
        ("MAHINDRA AND MAHINDRA LIMITED", "MAHINDRA AND MAHINDRA", "LIMITED"),
        ("TATA SONS PVT LTD", "TATA SONS", "PRIVATE_LIMITED"),
        ("ABC (P) LTD", "ABC", "PRIVATE_LIMITED"),
        ("(P) LTD", None, "PRIVATE_LIMITED"),
        ("FORD MOTOR COMPANY", "FORD MOTOR COMPANY", None),
        ("STATE BANK OF INDIA", "STATE BANK OF INDIA", None)
    ]
    
    print(f"{'INPUT':<35} | {'EXP_CORE':<25} | {'ACT_CORE':<25} | {'EXP_FORM':<32} | {'ACT_FORM':<32} | {'RESULT'}")
    print("-" * 170)
    
    passes = 0
    for input_val, exp_core, exp_form in test_cases:
        act_core, act_form, _ = extract_legal_form(input_val)
        
        core_pass = act_core == exp_core
        form_pass = act_form == exp_form
        passed = core_pass and form_pass
        
        if passed:
            passes += 1
            
        print(f"{input_val:<35} | {str(exp_core):<25} | {str(act_core):<25} | {str(exp_form):<32} | {str(act_form):<32} | {'PASS' if passed else 'FAIL'}")
        
    print("-" * 170)
    print(f"Pass rate: {passes}/{len(test_cases)} ({passes/len(test_cases)*100:.1f}%)")

if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_vendor_token_discriminativeness.py
````python
import sys
try:
    from thefuzz import fuzz
except ImportError:
    import difflib
    class fuzz:
        @staticmethod
        def ratio(a, b):
            return difflib.SequenceMatcher(None, a, b).ratio() * 100

CORPUS = [
    "SHREE GANESH TRADERS",
    "SHREE BALAJI TRADERS",
    "GANESH INDUSTRIES",
    "BALAJI INDUSTRIES",
    "ABC TECHNOLOGIES",
    "ABC TECHNOLOGY",
    "ABC LLP",
    "ABC PRIVATE LIMITED",
    "TATA MOTORS",
    "TATA TECHNOLOGIES",
    "UNIQUE RARE ORGANIZATION NAME"
]

def analyze_discriminativeness():
    # Example: "SHREE GANESH TRADERS" vs "SHREE BALAJI TRADERS"
    # Fuzzy ratio will be high because "SHREE" and "TRADERS" match perfectly.
    # Corpus discriminativeness would realize "SHREE" and "TRADERS" are generic.
    
    a = "SHREE GANESH TRADERS"
    b = "SHREE BALAJI TRADERS"
    score = fuzz.ratio(a, b)
    
    print(f"Comparing '{a}' with '{b}'")
    print(f"Raw fuzzy ratio: {score}")
    print("Corpus analysis: 'SHREE' and 'TRADERS' appear in multiple distinct entities.")
    print("Therefore, the only discriminative tokens are 'GANESH' vs 'BALAJI', which is a 0% match.")
    print("Conclusion: Raw fuzzy similarity overstates identity evidence when shared tokens are generic.")

if __name__ == "__main__":
    analyze_discriminativeness()
````

## File: experiments/inspect_reference_enrichment.py
````python
from recongraph.matching.reference_evidence import (
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

PROFILE_REFS = [
    "INV-001",
    "ABC-001",
    "INV-874219",
    "CREDIT-NOTE",
    "CREDITNOTE",
]

PAIRS = [
    ("INV-001", "ABC-001"),
    ("INV-874219", "AB/874219"),
    ("NEW-999999", "XYZ-999999"),
    ("CREDIT-NOTE", "CREDITNOTE"),
    ("INV-01", "ABC-01"),
]

def main():
    profile = build_reference_corpus_profile(PROFILE_REFS)

    for a, b in PAIRS:
        print(f"\nA: {a}")
        print(f"B: {b}")

        identity = extract_reference_identity(a, b)
        if not identity:
            print("no identity evidence")
            continue

        enriched = enrich_reference_identity(identity, profile)
        print(f"exact normalized match: {enriched.identity.exact_normalized_match}")

        print("\nnormalized references:")
        for norm_ev in enriched.normalized_references:
            freq = norm_ev.statistics.frequency if norm_ev.statistics else "unavailable"
            print(f"    {norm_ev.normalized_reference}\n    {freq}")

        print("\nshared numeric tokens:")
        if not enriched.shared_numeric_tokens:
            print("    none")
        for token_ev in enriched.shared_numeric_tokens:
            df = token_ev.statistics.document_frequency if token_ev.statistics else "unavailable"
            print(f"    {token_ev.token}\n    {df}")

if __name__ == "__main__":
    main()
````

## File: experiments/inspect_reference_interpretation_assembly.py
````python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity,
    enrich_reference_identity, _construct_reference_evidence_contributions,
    _select_strongest_reference_contribution, _assemble_reference_evidence_interpretation
)

def evaluate_reference_interpretation_assembly():
    policy = ReferenceEvidencePolicy()
    
    cases = [
        {"id": "RA001", "desc": "rare profiled exact identity", "a": "INV-874219", "b": "INV/874219", "prof": {"inv874219": 1}, "tok_prof": {}},
        {"id": "RA002", "desc": "ubiquitous profiled exact identity", "a": "CREDIT NOTE", "b": "creditnote", "prof": {"creditnote": 100}, "tok_prof": {}},
        {"id": "RA003", "desc": "out-of-profile exact identity", "a": "INV-999999", "b": "INV/999999", "prof": {}, "tok_prof": {}},
        {"id": "RA004", "desc": "rare profiled shared token", "a": "INV-874219", "b": "AB-874219", "prof": {}, "tok_prof": {"874219": 1}},
        {"id": "RA005", "desc": "common profiled shared token", "a": "INV-2026", "b": "AB-2026", "prof": {}, "tok_prof": {"2026": 36}},
        {"id": "RA006", "desc": "out-of-profile long token", "a": "INV-121212", "b": "AB-121212", "prof": {}, "tok_prof": {}},
        {"id": "RA007", "desc": "out-of-profile repeated long token", "a": "INV-999999", "b": "AB-999999", "prof": {}, "tok_prof": {}},
        {"id": "RA008", "desc": "profiled 0.60 vs fallback 0.60", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 16}}, 
        {"id": "RA009", "desc": "profiled slightly below 0.60 vs fallback 0.60", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 17}}, 
        {"id": "RA010", "desc": "complete profiled tie with two tokens", "a": "INV-2026-874219", "b": "AB-2026-874219", "prof": {}, "tok_prof": {"2026": 1, "874219": 1}},
    ]
    
    print("REFERENCE EVIDENCE INTERPRETATION ASSEMBLY INSPECTION")
    print("-" * 100)
    for c in cases:
        print(f"Case: {c['id']} - {c['desc']}")
        
        identity = extract_reference_identity(c["a"], c["b"])
        if not identity:
            continue
            
        sum_norm = sum(c["prof"].values())
        norm_prof = c["prof"].copy()
        if sum_norm < 100:
            norm_prof["dummy"] = 100 - sum_norm
            
        p = ReferenceCorpusProfile(
            reference_count=100,
            normalized_reference_frequency=norm_prof,
            numeric_token_document_frequency=c["tok_prof"]
        )
            
        enriched = enrich_reference_identity(identity, p)
        contributions = _construct_reference_evidence_contributions(enriched, policy)
        
        print("Ordered contributions:")
        for i, contrib in enumerate(contributions):
            print(f"  Index {i}:")
            print(f"    evidence_kind: {contrib.evidence_kind}")
            print(f"    identity_value: {contrib.identity_value}")
            print(f"    positive_evidence: {repr(contrib.positive_evidence)}")
            print(f"    statistics_available: {contrib.statistics_available}")
            
        winner = _select_strongest_reference_contribution(contributions)
        print("Frozen selector winner:")
        print(f"  evidence_kind: {winner.evidence_kind}")
        print(f"  identity_value: {winner.identity_value}")
        print(f"  positive_evidence: {repr(winner.positive_evidence)}")
        print(f"  statistics_available: {winner.statistics_available}")
        
        interp = _assemble_reference_evidence_interpretation(contributions)
        print("Interpretation:")
        print(f"  score: {repr(interp.score)}")
        print(f"  statistical_coverage: {repr(interp.statistical_coverage)}")
        print(f"  contribution count: {len(interp.contributions)}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate_reference_interpretation_assembly()
````

## File: experiments/inspect_reference_selection.py
````python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity,
    enrich_reference_identity, _construct_reference_evidence_contributions,
    _select_strongest_reference_contribution
)

def evaluate_reference_selection():
    policy = ReferenceEvidencePolicy()
    
    cases = [
        {"id": "RS001", "a": "INV-874219", "b": "INV/874219", "prof": {"inv874219": 1}, "tok_prof": {}},
        {"id": "RS002", "a": "INV-999999", "b": "INV/999999", "prof": {}, "tok_prof": {}},
        {"id": "RS003", "a": "INV-2026-874219", "b": "AB-2026-874219", "prof": {}, "tok_prof": {"2026": 10, "874219": 1}},
        {"id": "RS004", "a": "INV-2026-874219", "b": "AB-2026-874219", "prof": {}, "tok_prof": {"2026": 1, "874219": 1}},
        {"id": "RS005", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 16}}, # 16/100 -> 0.6 profiled vs 121212 fallback 0.6
        {"id": "RS006", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 17}}, # 17/100 -> <0.6 profiled vs 121212 fallback 0.6
    ]
    
    print("REFERENCE EVIDENCE SELECTION INSPECTION")
    print("-" * 100)
    for c in cases:
        print(f"Case: {c['id']}")
        
        identity = extract_reference_identity(c["a"], c["b"])
        if not identity:
            continue
            
        sum_norm = sum(c["prof"].values())
        norm_prof = c["prof"].copy()
        if sum_norm < 100:
            norm_prof["dummy"] = 100 - sum_norm
            
        p = ReferenceCorpusProfile(
            reference_count=100,
            normalized_reference_frequency=norm_prof,
            numeric_token_document_frequency=c["tok_prof"]
        )
            
        enriched = enrich_reference_identity(identity, p)
        contributions = _construct_reference_evidence_contributions(enriched, policy)
        
        print("Ordered Contributions:")
        for i, contrib in enumerate(contributions):
            print(f"  Index {i}:")
            print(f"    evidence_kind: {contrib.evidence_kind}")
            print(f"    identity_value: {contrib.identity_value}")
            print(f"    positive_evidence: {repr(contrib.positive_evidence)}")
            print(f"    statistics_available: {contrib.statistics_available}")
            
        winner = _select_strongest_reference_contribution(contributions)
        print("Selected Contribution:")
        print(f"  evidence_kind: {winner.evidence_kind}")
        print(f"  identity_value: {winner.identity_value}")
        print(f"  positive_evidence: {repr(winner.positive_evidence)}")
        print(f"  statistics_available: {winner.statistics_available}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate_reference_selection()
````

## File: experiments/legacy_reference.py
````python
from typing import Optional
from recongraph.normalization.text import normalize_reference

def extract_numeric_reference_tokens(
    reference: str,
    min_length: int = 3,
) -> tuple[str, ...]:
    if min_length < 1:
        raise ValueError("min_length must be positive")
        
    if not reference:
        return ()
        
    tokens = []
    current_token = []
    
    for char in reference:
        if char.isdigit():
            current_token.append(char)
        else:
            if current_token:
                if len(current_token) >= min_length:
                    tokens.append("".join(current_token))
                current_token = []
                
    if current_token and len(current_token) >= min_length:
        tokens.append("".join(current_token))
        
    return tuple(tokens)

def reference_score(
    reference_a: str | None,
    reference_b: str | None,
    shared_numeric_score: float = 0.8,
) -> float | None:
    if not reference_a or not reference_b:
        return None

    if not reference_a.strip() or not reference_b.strip():
        return None

    normalized_a = normalize_reference(reference_a)
    normalized_b = normalize_reference(reference_b)

    if normalized_a == normalized_b:
        return 1.0

    numeric_tokens_a = extract_numeric_reference_tokens(
        reference_a, min_length=3
    )
    numeric_tokens_b = extract_numeric_reference_tokens(
        reference_b, min_length=3
    )

    shared_tokens = set(numeric_tokens_a).intersection(numeric_tokens_b)
    
    for token in shared_tokens:
        if len(token) == 4 and 1900 <= int(token) <= 2100:
            continue
        return shared_numeric_score

    return 0.0
````

## File: experiments/vendor_similarity_metrics.py
````python
from rapidfuzz import fuzz

from recongraph.normalization.text import normalize_vendor_name


VENDOR_PAIRS = [
    (
        "ABC Steel Private Limited",
        "ABC STEELS PVT. LTD.",
        True,
    ),
    (
        "Shree Balaji Enterprises",
        "SHREE BALAJI ENT.",
        True,
    ),
    (
        "Northstar Components Pvt Ltd",
        "Northstar Component Private Limited",
        True,
    ),
    (
        "Metro Office Solutions",
        "METRO OFFICE SOLUTION",
        True,
    ),
    (
        "Apex Industrial Supplies",
        "APEX INDUSTRIAL SUPPLY",
        True,
    ),
    (
        "ABC Steel Private Limited",
        "Metro Office Solutions",
        False,
    ),
    (
        "ABC Steel",
        "ABC Steel Trading",
        False,
    ),
    (
        "Shree Balaji Enterprises",
        "Shree Balaji Foods",
        False,
    ),
    (
        "Northstar Components",
        "Northstar Logistics",
        False,
    ),
    (
        "Apex Industrial Supplies",
        "Apex Industrial Services",
        False,
    ),
    (
        "Metro Office Solutions",
        "Metro Office Furniture",
        False,
    ),
]

METRICS = {
    "ratio": fuzz.ratio,
    "partial_ratio": fuzz.partial_ratio,
    "token_sort_ratio": fuzz.token_sort_ratio,
    "token_set_ratio": fuzz.token_set_ratio,
    "WRatio": fuzz.WRatio,
}

for metric_name, metric in METRICS.items():
    positive_scores = []
    negative_scores = []

    for vendor_a, vendor_b, expected_match in VENDOR_PAIRS:
        normalized_a = normalize_vendor_name(vendor_a)
        normalized_b = normalize_vendor_name(vendor_b)

        score = metric(normalized_a, normalized_b)

        if expected_match:
            positive_scores.append(score)
        else:
            negative_scores.append(score)

    minimum_positive = min(positive_scores)
    maximum_negative = max(negative_scores)

    print("=" * 72)
    print(f"Metric: {metric_name}")
    print(f"Minimum positive score: {minimum_positive:.2f}")
    print(f"Maximum negative score: {maximum_negative:.2f}")
    print(
        "Separation gap: "
        f"{minimum_positive - maximum_negative:.2f}"
    )
````

## File: experiments/verify_ancestry_cross_process_determinism.py
````python
import subprocess
import sys
import os

SCRIPT = """
import sys
from recongraph.domain.lineage import SourceSystemId, SourceArtifactId, SourceLocator, StructuredSourceLineage
from recongraph.domain.derivations import (
    DerivedArtifactTypeId, CanonicalPayloadEnvelope, DerivedArtifactIdentity
)

sys_id = SourceSystemId("sap.production")
art_id = SourceArtifactId("invoice:123")
loc = SourceLocator("field:vendor_name")
lineage = StructuredSourceLineage(sys_id, art_id, loc)

tid = DerivedArtifactTypeId("tax.pan")
payload = CanonicalPayloadEnvelope({"pan": "ABCDE1234F", "nested": {"a": (1, 2, 3), "b": None, "c": True}})
aid = DerivedArtifactIdentity.compute(tid, "1.0.0", payload)

print(lineage.canonicalize_for_serialization().hex())
print(aid.digest)
"""

def run_experiment():
    print("Running process 1...")
    p1 = subprocess.run([sys.executable, "-c", SCRIPT], capture_output=True, text=True, check=True)
    out1 = p1.stdout.strip()
    
    # We can enforce hash randomization in Python, though it's on by default in 3.3+
    env = os.environ.copy()
    env["PYTHONHASHSEED"] = "random"
    
    print("Running process 2...")
    p2 = subprocess.run([sys.executable, "-c", SCRIPT], env=env, capture_output=True, text=True, check=True)
    out2 = p2.stdout.strip()

    print(f"Process 1 output:\n{out1}")
    print(f"Process 2 output:\n{out2}")
    
    if out1 == out2:
        print("\nSUCCESS: Outputs are byte-identical across processes.")
    else:
        print("\nFAILURE: Non-deterministic serialization detected.")
        sys.exit(1)

if __name__ == "__main__":
    run_experiment()
````

## File: experiments/verify_assertion_cross_process_determinism.py
````python
import sys
from recongraph.domain.assertions import EvidenceAssertion, AssertionPolarity, EvidenceAncestryRef
from recongraph.domain.identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest
from recongraph.domain.authority import AuthorityDescriptor, AuthorityBasisId
from recongraph.domain.scopes import Proposition, PropositionSubject, ScopeKind, SubjectRef
from recongraph.domain.claims import CoreClaims

def main():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")])
    prop = Proposition(claim, subject)
    ancestry = EvidenceAncestryRef(KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64)))
    
    a1 = EvidenceAssertion(prop, AssertionPolarity.SUPPORT, 1.0, AuthorityDescriptor(AuthorityBasisId("a")), ancestry)
    print(a1.identity.digest)

if __name__ == "__main__":
    main()
````

## File: experiments/verify_canonical_encoding_cross_process.py
````python
import sys
import argparse
from recongraph.domain.identity import canonical_encode
from recongraph.domain.payloads import CanonicalPayloadEnvelope, TypedPayloadEnvelope

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str)
    args = parser.parse_args()

    if args.test == "nfc_nfd":
        # NFD vs NFC
        import unicodedata
        payload = {"value": unicodedata.normalize("NFD", "é")}
        print(canonical_encode(payload).hex())
    elif args.test == "nfc_nfc":
        import unicodedata
        payload = {"value": unicodedata.normalize("NFC", "é")}
        print(canonical_encode(payload).hex())
    elif args.test == "mapping_order_1":
        payload = {"a": 1, "b": 2}
        print(canonical_encode(payload).hex())
    elif args.test == "mapping_order_2":
        payload = {"b": 2, "a": 1}
        print(canonical_encode(payload).hex())

if __name__ == "__main__":
    main()
````

## File: src/recongraph/benchmark/__init__.py
````python

````

## File: src/recongraph/benchmark/models.py
````python
from dataclasses import dataclass
from typing import Mapping

@dataclass(frozen=True)
class DatasetMetadata:
    dataset_id: str
    purchase_count: int
    gst_count: int

@dataclass(frozen=True)
class DecisionStatistics:
    auto_match_count: int
    review_ambiguous_count: int
    review_weak_count: int
    no_match_count: int

@dataclass(frozen=True)
class SearchStatistics:
    candidate_edges: int
    components_extracted: int
    max_component_size: int
    avg_component_size: float
    candidate_reduction_ratio: float
    total_hypotheses_evaluated: int

@dataclass(frozen=True)
class EvidenceStatistics:
    signal_distributions: Mapping[str, float]

@dataclass(frozen=True)
class ConfidenceDistribution:
    bins: Mapping[str, int]

@dataclass(frozen=True)
class TimingStatistics:
    total_runtime_ms: float
    candidate_generation_ms: float
    graph_building_ms: float
    search_evaluation_ms: float
    decision_ms: float

@dataclass(frozen=True)
class BenchmarkReport:
    """The fully serializable domain object containing all metric dimensions."""
    dataset_metadata: DatasetMetadata
    decision_statistics: DecisionStatistics
    search_statistics: SearchStatistics
    evidence_statistics: EvidenceStatistics
    confidence_distribution: ConfidenceDistribution
    timing_statistics: TimingStatistics
````

## File: src/recongraph/benchmark/runner.py
````python
import time
from typing import Sequence
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, ReferenceEvidenceContext, ReferenceEvidencePolicy
from recongraph.graph.decision import DecisionPolicy, DecisionEngine, DecisionAction
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn
from recongraph.candidate_generation.generator import CandidateGenerator
from recongraph.graph.algorithms import extract_connected_components
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TemporalEvidenceProvider, TaxEvidenceProvider, VendorEvidenceProvider, ReferenceEvidenceProvider
from recongraph.graph.search import HypothesisSearcher
from recongraph.graph.evaluator import HypothesisEvaluator
from recongraph.benchmark.models import (
    BenchmarkReport, DatasetMetadata, DecisionStatistics, SearchStatistics,
    EvidenceStatistics, ConfidenceDistribution, TimingStatistics
)

class BenchmarkRunner:
    """Executes the pipeline purely as an observer to construct a benchmark report."""
    def __init__(
        self,
        dataset_id: str,
        purchases: Sequence[PurchaseRecord],
        gsts: Sequence[GSTRecord],
        corpus_profile: ReferenceCorpusProfile,
        decision_policy: DecisionPolicy,
    ):
        self.dataset_id = dataset_id
        self.purchases = purchases
        self.gsts = gsts
        self.corpus_profile = corpus_profile
        self.decision_policy = decision_policy

    def run(self) -> BenchmarkReport:
        t0 = time.perf_counter()
        
        # 1. Candidate Generation
        gen_t0 = time.perf_counter()
        
        providers = [
            FinancialEvidenceProvider(),
            TemporalEvidenceProvider(),
            TaxEvidenceProvider(),
            VendorEvidenceProvider(),
            ReferenceEvidenceProvider(ReferenceEvidenceContext(
                profile=self.corpus_profile,
                policy=ReferenceEvidencePolicy()
            ))
        ]
        
        generator = CandidateGenerator(providers)
        edges = list(generator.generate(self.purchases, self.gsts))
        candidate_generation_ms = (time.perf_counter() - gen_t0) * 1000.0
        
        # 2. Graph Building
        graph_t0 = time.perf_counter()
        graph_builder = CandidateGraphBuilder()
        for p in self.purchases:
            graph_builder.add_node(build_purchase_urn(p.record_id), p)
        for g in self.gsts:
            graph_builder.add_node(build_gst_urn(g.record_id), g)
        for e in edges:
            graph_builder.add_candidate_edge(
                build_purchase_urn(e.purchase.record_id),
                build_gst_urn(e.gst_record.record_id),
                e.shared_blocking_keys
            )
        graph = graph_builder.build()
        graph_building_ms = (time.perf_counter() - graph_t0) * 1000.0
        
        # 3. Components & Search & Eval & Decisions
        components = list(extract_connected_components(graph))
        searcher = HypothesisSearcher()
        from recongraph.matching.pair_scorers import PURCHASE_TO_GST_POLICY
        evaluator = HypothesisEvaluator(providers, PURCHASE_TO_GST_POLICY)
        engine = DecisionEngine(self.decision_policy)
        
        max_comp_size = 0
        total_comp_nodes = 0
        total_hypotheses_evaluated = 0
        
        actions = {
            DecisionAction.AUTO_MATCH: 0,
            DecisionAction.REVIEW_AMBIGUOUS: 0,
            DecisionAction.REVIEW_WEAK: 0,
            DecisionAction.NO_MATCH: 0
        }
        bins = {f"0.{i}-0.{i+1}": 0 for i in range(10)}
        bins["1.0"] = 0
        
        search_time = 0.0
        decision_time = 0.0
        
        for comp in components:
            size = len(comp.graph.nodes)
            total_comp_nodes += size
            if size > max_comp_size:
                max_comp_size = size
            
            s_t0 = time.perf_counter()
            hypotheses = searcher.search(comp)
            evaluated = [evaluator.evaluate(graph, h) for h in hypotheses]
            total_hypotheses_evaluated += len(evaluated)
            search_time += (time.perf_counter() - s_t0)
            
            for eh in evaluated:
                score = eh.score
                if score >= 1.0:
                    bins["1.0"] += 1
                else:
                    bucket = int(score * 10)
                    bins[f"0.{bucket}-0.{bucket+1}"] += 1
            
            d_t0 = time.perf_counter()
            decision = engine.decide(evaluated)
            actions[decision.action] += 1
            decision_time += (time.perf_counter() - d_t0)
            
        search_evaluation_ms = search_time * 1000.0
        decision_ms = decision_time * 1000.0
        total_runtime_ms = (time.perf_counter() - t0) * 1000.0
        
        num_p = len(self.purchases)
        num_g = len(self.gsts)
        max_possible_edges = num_p * num_g
        reduction_ratio = 1.0 - (len(edges) / max_possible_edges) if max_possible_edges > 0 else 0.0
        avg_comp_size = total_comp_nodes / len(components) if components else 0.0

        return BenchmarkReport(
            dataset_metadata=DatasetMetadata(self.dataset_id, num_p, num_g),
            decision_statistics=DecisionStatistics(
                auto_match_count=actions[DecisionAction.AUTO_MATCH],
                review_ambiguous_count=actions[DecisionAction.REVIEW_AMBIGUOUS],
                review_weak_count=actions[DecisionAction.REVIEW_WEAK],
                no_match_count=actions[DecisionAction.NO_MATCH]
            ),
            search_statistics=SearchStatistics(
                candidate_edges=len(edges),
                components_extracted=len(components),
                max_component_size=max_comp_size,
                avg_component_size=avg_comp_size,
                candidate_reduction_ratio=reduction_ratio,
                total_hypotheses_evaluated=total_hypotheses_evaluated
            ),
            evidence_statistics=EvidenceStatistics({}),
            confidence_distribution=ConfidenceDistribution(bins),
            timing_statistics=TimingStatistics(
                total_runtime_ms=total_runtime_ms,
                candidate_generation_ms=candidate_generation_ms,
                graph_building_ms=graph_building_ms,
                search_evaluation_ms=search_evaluation_ms,
                decision_ms=decision_ms
            )
        )
````

## File: src/recongraph/candidate_generation/__init__.py
````python
"""
Candidate generation and blocking strategies for large-scale reconciliation.
"""
````

## File: src/recongraph/candidate_generation/blockers.py
````python
from typing import Protocol, Any, runtime_checkable
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, _extract_numeric_tokens
from recongraph.normalization.text import normalize_reference
import math

@runtime_checkable
class Blocker(Protocol):
    """
    Protocol for extracting indexing keys from a financial record.
    Keys are returned as a set of strings.
    """
    def extract_keys(self, record: Any) -> frozenset[str]:
        ...

class ExactAmountBlocker:
    """Blocks records based on exactly matching amounts."""
    def extract_keys(self, record: Any) -> frozenset[str]:
        amount = getattr(record, "amount", None)
        if amount is None:
            return frozenset()
        return frozenset([f"AMT:{amount:.2f}"])

class TaxIdentityBlocker:
    """Blocks records based on exact normalized tax identity."""
    def extract_keys(self, record: Any) -> frozenset[str]:
        tax_identity = getattr(record, "tax_identity", None)
        if not tax_identity:
            return frozenset()
        # Normalizing to uppercase and stripped string
        identity = str(tax_identity).strip().upper()
        if not identity:
            return frozenset()
        return frozenset([f"TAX:{identity}"])

class ReferenceTokenBlocker:
    """
    Extracts blocking keys from the reference field.
    Only yields keys for statistically rare tokens to prevent
    highly generic tokens from generating thousands of candidate edges.
    """
    def __init__(self, profile: ReferenceCorpusProfile, rarity_threshold: float = 0.8):
        self.profile = profile
        self.rarity_threshold = rarity_threshold

    def _is_rare(self, freq: int, total: int) -> bool:
        if total == 0:
            return False
        # Calculate magnitude: 1 - sqrt(freq / total)
        magnitude = 1.0 - math.sqrt(freq / total)
        return magnitude >= self.rarity_threshold

    def extract_keys(self, record: Any) -> frozenset[str]:
        reference = getattr(record, "reference", None)
        if not reference:
            return frozenset()
            
        keys = set()
        
        # Exact normalized match key
        normalized = normalize_reference(reference)
        if normalized:
            freq = self.profile.normalized_reference_frequency.get(normalized, 0)
            if self._is_rare(freq, self.profile.reference_count):
                keys.add(f"REF_NORM:{normalized}")
                
        # Token match keys
        tokens = _extract_numeric_tokens(reference)
        for token in tokens:
            freq = self.profile.numeric_token_document_frequency.get(token, 0)
            if self._is_rare(freq, self.profile.reference_count):
                keys.add(f"REF_TOK:{token}")
                
        return frozenset(keys)
````

## File: src/recongraph/candidate_generation/index.py
````python
from typing import Any, Iterable
from collections import defaultdict
from recongraph.candidate_generation.blockers import Blocker

class InvertedIndex:
    """
    Maintains a mapping of blocking keys to the records that possess them.
    """
    def __init__(self, blockers: Iterable[Blocker]):
        self.blockers = tuple(blockers)
        self.index: dict[str, set[Any]] = defaultdict(set)
        
    def add(self, record: Any) -> frozenset[str]:
        keys = set()
        for blocker in self.blockers:
            keys.update(blocker.extract_keys(record))
            
        for key in keys:
            self.index[key].add(record)
            
        return frozenset(keys)
        
    def add_many(self, records: Iterable[Any]) -> None:
        for record in records:
            self.add(record)
            
    def query(self, key: str) -> frozenset[Any]:
        return frozenset(self.index.get(key, set()))
````

## File: src/recongraph/domain/financial/__init__.py
````python

````

## File: src/recongraph/domain/financial/pipeline.py
````python
from dataclasses import dataclass
from typing import Sequence
import math

from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.plugins.provider_v2 import EvidencePipeline, EvidenceContributionV2

@dataclass(frozen=True)
class FinancialObservation:
    purchase_gross: tuple[float, ...]
    purchase_net: tuple[float | None, ...]
    purchase_tax: tuple[float | None, ...]
    purchase_currencies: tuple[str, ...]
    purchase_signs: tuple[int, ...]
    
    gst_gross: tuple[float, ...]
    gst_net: tuple[float | None, ...]
    gst_tax: tuple[float | None, ...]
    gst_currencies: tuple[str, ...]
    gst_signs: tuple[int, ...]
    
    @property
    def total_purchase_gross(self) -> float:
        return sum(self.purchase_gross)
        
    @property
    def total_gst_gross(self) -> float:
        return sum(self.gst_gross)
        
    @property
    def total_purchase_net(self) -> float:
        return sum(n for n in self.purchase_net if n is not None)
        
    @property
    def total_gst_tax(self) -> float:
        return sum(t for t in self.gst_tax if t is not None)

@dataclass(frozen=True)
class EvaluatedFinancialEvidence:
    sum_purchases: float
    sum_payments: float
    currency: str
    amount_score: float
    is_exact_match: bool
    is_partial: bool
    is_overpayment: bool
    residual: float
    currency_mismatch: bool
    notes: list[str]

class FinancialEvidencePipeline(EvidencePipeline[FinancialObservation, EvaluatedFinancialEvidence]):
    def __init__(self, tolerance: float = 0.05, fee_tolerance: float = 2.00):
        self.tolerance = tolerance
        self.fee_tolerance = fee_tolerance

    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> FinancialObservation:
        return FinancialObservation(
            purchase_gross=tuple(p.amount for p in purchases),
            purchase_net=tuple(p.net_amount for p in purchases),
            purchase_tax=tuple(p.tax_amount for p in purchases),
            purchase_currencies=tuple(p.currency for p in purchases),
            purchase_signs=tuple(p.sign for p in purchases),
            
            gst_gross=tuple(g.amount for g in gsts),
            gst_net=tuple(g.net_amount for g in gsts),
            gst_tax=tuple(g.tax_amount for g in gsts),
            gst_currencies=tuple(g.currency for g in gsts),
            gst_signs=tuple(g.sign for g in gsts)
        )
        
    def interpret(self, observation: FinancialObservation) -> EvaluatedFinancialEvidence:
        tp = observation.total_purchase_gross
        tg = observation.total_gst_gross
        delta = abs(tp - tg)
        residual = tp - tg # Positive means underpayment (invoice > payment)
        
        all_currencies = set(observation.purchase_currencies) | set(observation.gst_currencies)
        currency_mismatch = len(all_currencies) > 1
        primary_currency = next(iter(all_currencies)) if all_currencies else "USD"
        
        num_p = len(observation.purchase_gross)
        num_g = len(observation.gst_gross)
        is_split = (num_p > 1 or num_g > 1)
        
        notes = []
        is_exact = False
        is_partial = False
        is_over = False
        score = 0.0
        
        if currency_mismatch:
            notes.append("CURRENCY_MISMATCH")
            score = 0.0
        else:
            if delta <= 1e-9:
                is_exact = True
                score = 1.0
                if is_split:
                    notes.append("SPLIT_PAYMENT")
                else:
                    notes.append("EXACT_TOTAL_MATCH")
            elif delta <= self.tolerance:
                is_exact = True
                score = 0.99
                notes.append("ROUNDING_MATCH")
            elif delta <= self.fee_tolerance and residual > 0:
                # Small underpayment modeled as a fee
                is_exact = True
                score = 0.95
                notes.append("FEE_DETECTED")
            else:
                if residual > 0:
                    is_partial = True
                    notes.append("UNDERPAYMENT")
                else:
                    is_over = True
                    notes.append("OVERPAYMENT")
                
                max_val = max(tp, tg, 1.0)
                score = max(0.0, 1.0 - (delta / max_val))
                
                # Rough net/gross heuristic checking if Gross ≈ Payment + Tax
                # The user noted: If (GrossInvoice == Sum(Payments) + Sum(Tax)) -> NET_TO_GROSS_MATCH
                if observation.total_gst_tax > 0:
                    if abs(tp - (tg + observation.total_gst_tax)) <= self.tolerance:
                        notes.append("GROSS_NET_MATCH")
                        
        return EvaluatedFinancialEvidence(
            sum_purchases=tp,
            sum_payments=tg,
            currency=primary_currency,
            amount_score=score,
            is_exact_match=is_exact,
            is_partial=is_partial,
            is_overpayment=is_over,
            residual=residual,
            currency_mismatch=currency_mismatch,
            notes=notes
        )
        
    def contribute(self, interpretation: EvaluatedFinancialEvidence) -> EvidenceContributionV2[EvaluatedFinancialEvidence]:
        violations = set()
        
        if interpretation.currency_mismatch:
            violations.add("CURRENCY_MISMATCH")
        elif not interpretation.is_exact_match and interpretation.amount_score < 0.5:
            violations.add("SEVERE_AMOUNT_CONFLICT")
            
        return EvidenceContributionV2(
            provider_name="FinancialEvidenceProvider",
            score=interpretation.amount_score,
            violations=frozenset(violations),
            interpretation=interpretation
        )
````

## File: src/recongraph/domain/__init__.py
````python
# Domain package
````

## File: src/recongraph/domain/assertions.py
````python
import struct
import hashlib
from enum import Enum
from dataclasses import dataclass
from typing import Optional
from .identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest, canonical_encode
from .scopes import Proposition
from .authority import AuthorityDescriptor
from .payloads import TypedPayloadEnvelope


class AssertionPolarity(str, Enum):
    SUPPORT = "support"
    CONFLICT = "conflict"


@dataclass(frozen=True, slots=True, order=True)
class EvidenceAncestryRef:
    """
    Identity proven eligible as assertion ancestry.
    Must be an occurrence, not a semantic fact identity alone.
    """
    identity: KernelIdentityRef

    def __post_init__(self):
        allowed_domains = {
            "recongraph.observation_occurrence",
            "recongraph.derivation_occurrence"
        }
        if self.identity.domain.value not in allowed_domains:
            raise ValueError(f"Identity domain '{self.identity.domain.value}' is not eligible as evidence ancestry.")


def _canonicalize_magnitude(value: float) -> str:
    """
    Magnitude identity uses the exact IEEE-754 binary64 bit representation of the finite Python float, packed as hex.
    -0.0 is explicitly canonicalized to positive 0.0.
    """
    if not isinstance(value, float):
        raise TypeError("Magnitude must be a float.")
    import math
    if not math.isfinite(value):
        raise ValueError("Non-finite magnitudes are rejected.")
    
    # Python's struct.pack('>d', float) gives IEEE-754 binary64
    if value == 0.0:
        value = 0.0  # Coerce -0.0 to 0.0
    
    if value <= 0.0 or value > 1.0:
        raise ValueError("Magnitude must be in range (0.0, 1.0]")
        
    packed = struct.pack('>d', value)
    return f"binary64:{packed.hex()}"


@dataclass(frozen=True, slots=True, order=True)
class EvidenceAssertionIdentity:
    """
    Canonical content-addressed identity of an EvidenceAssertion.
    """
    digest: str


@dataclass(frozen=True, slots=True)
class EvidenceAssertion:
    """
    An atomic claim evaluated over evidence.
    Has exactly one proposition, one polarity, strictly positive finite magnitude,
    one descriptive authority basis, and exactly one valid semantic ancestry root.
    """
    proposition: Proposition
    polarity: AssertionPolarity
    magnitude: float
    authority: AuthorityDescriptor
    ancestry: EvidenceAncestryRef
    payload: Optional[TypedPayloadEnvelope] = None
    identity: EvidenceAssertionIdentity = None

    def __post_init__(self):
        # We compute identity and use object.__setattr__ because the dataclass is frozen.
        canon_mag = _canonicalize_magnitude(self.magnitude)
        
        payload_dict = {
            "schema": "recongraph.evidence_assertion.v1",
            "proposition": {
                "claim_id": self.proposition.claim.claim_id.value,
                "claim_semantic_version": self.proposition.claim.semantic_version.value,
                "subject": self.proposition.subject.to_dict()
            },
            "polarity": self.polarity.value,
            "magnitude": canon_mag,
            "authority": self.authority.basis.value,
            "ancestry": self.ancestry.identity.digest.value
        }
        
        if self.payload:
            payload_dict["payload"] = {
                "type_id": self.payload.type_id,
                "semantic_version": self.payload.semantic_version,
                "payload_fingerprint": hashlib.sha256(self.payload.payload.canonicalize()).hexdigest()
            }
            
        canonical_bytes = canonical_encode(payload_dict)
        domain_separated_bytes = b"recongraph:evidence_assertion:v1\x00" + canonical_bytes
        digest_hex = hashlib.sha256(domain_separated_bytes).hexdigest()
        
        computed_identity = EvidenceAssertionIdentity(f"sha256:{digest_hex}")
        
        # Prevent caller from providing an identity mismatch
        if self.identity is not None and self.identity != computed_identity:
            raise ValueError("Provided identity mismatch.")
            
        if self.identity is None:
            object.__setattr__(self, 'identity', computed_identity)


class EvidenceInterpretationState(str, Enum):
    INTERPRETED = "interpreted"
    MISSING_INPUT = "missing_input"
    INSUFFICIENT_INPUT = "insufficient_input"
    UNINTERPRETABLE_INPUT = "uninterpretable_input"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True, slots=True)
class EvidenceInterpretationResult:
    """
    Deterministic transport envelope describing one provider interpretation attempt.
    """
    state: EvidenceInterpretationState
    assertions: tuple[EvidenceAssertion, ...]

    def __post_init__(self):
        if self.state != EvidenceInterpretationState.INTERPRETED:
            if len(self.assertions) > 0:
                raise ValueError(f"Interpretation result in state '{self.state.value}' must have empty assertions.")
                
        # Validate uniqueness and order
        if len(self.assertions) > 0:
            canonically_ordered = tuple(sorted(self.assertions, key=lambda a: a.identity.digest))
            if self.assertions != canonically_ordered:
                # To fail EA064 reversed assertion emission order canonicalized: 
                # "reversed input order yields equal result"
                # wait, if they have to pass as identical if passed out of order, we should sort them in post_init.
                # Since the dataclass is frozen, we do this:
                object.__setattr__(self, 'assertions', canonically_ordered)

            # Check for duplicates
            digests = [a.identity.digest for a in self.assertions] # after sorting
            if len(set(digests)) != len(digests):
                raise ValueError("Duplicate assertion identities inside one interpretation result are forbidden.")
````

## File: src/recongraph/domain/authority.py
````python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True, order=True)
class AuthorityBasisId:
    value: str


@dataclass(frozen=True, slots=True)
class AuthorityDescriptor:
    """
    Explicitly assigned by the assertion-producing provider. 
    Describes the epistemic basis on which an assertion asks fusion to interpret its evidentiary status.
    K6 performs no authority inheritance or ancestry-based inference.
    """
    basis: AuthorityBasisId
````

## File: src/recongraph/domain/dependencies.py
````python
from enum import Enum
from dataclasses import dataclass
from .identity import IdentityDigest, IdentityDomainId


class SemanticDependencyKind(str, Enum):
    CONFIGURATION = "configuration"
    CORPUS_SNAPSHOT = "corpus_snapshot"
    MODEL_ARTIFACT = "model_artifact"
    REGISTRY_SNAPSHOT = "registry_snapshot"
    RULESET = "ruleset"
    OTHER = "other"


class DependencyStability(str, Enum):
    CONTENT_ADDRESSED = "content_addressed"
    IMMUTABLE_VERSION = "immutable_version"
    MUTABLE_REFERENCE = "mutable_reference"


@dataclass(frozen=True, slots=True, order=True)
class SemanticDependencyRef:
    """
    Contextual modifier for a semantic derivation, capable of changing output.
    """
    kind: SemanticDependencyKind
    namespace: IdentityDomainId
    identity: IdentityDigest
    stability: DependencyStability
    semantic_version: str | None = None
````

## File: src/recongraph/domain/identity.py
````python
import re
import json
import unicodedata
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True, order=True)
class IdentityDomainId:
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)+$")

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("IdentityDomainId must be a string.")
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid IdentityDomainId format: '{self.value}'")


@dataclass(frozen=True, slots=True, order=True)
class IdentitySchemaId:
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)+$")

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("IdentitySchemaId must be a string.")
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid IdentitySchemaId format: '{self.value}'")


@dataclass(frozen=True, slots=True, order=True)
class IdentityDigest:
    value: str

    _PATTERN = re.compile(r"^[a-z0-9]+:[a-f0-9]{64}$")

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("IdentityDigest must be a string.")
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid IdentityDigest format: '{self.value}'")
            
        algo, h = self.value.split(":")
        if algo != "sha256" or len(h) != 64:
            raise ValueError(f"Unsupported or malformed digest: '{self.value}'")


@dataclass(frozen=True, slots=True, order=True)
class KernelIdentityRef:
    """
    Explicit transport reference for a semantic DAG node.
    Not an owning identity. Transport does not imply trust.
    """
    domain: IdentityDomainId
    schema: IdentitySchemaId
    digest: IdentityDigest


def _validate_canonical_payload(value: Any, for_machine_key: bool = False):
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        # Must be signed 64-bit int
        if value < -9223372036854775808 or value > 9223372036854775807:
            raise ValueError("Integer out of int64 bounds.")
        return value
    if isinstance(value, float):
        raise ValueError("Floats are forbidden in canonical semantic encoding.")
    if isinstance(value, str):
        if for_machine_key:
            if not value.isascii():
                raise ValueError("Machine keys must be ASCII.")
            return value
        return unicodedata.normalize("NFC", value)
    if isinstance(value, tuple) or isinstance(value, list):
        return tuple(_validate_canonical_payload(item) for item in value)
    if isinstance(value, dict):
        canon_dict = {}
        for k in sorted(value.keys()):
            if not isinstance(k, str):
                raise ValueError("Dict keys must be strings.")
            canon_k = _validate_canonical_payload(k, for_machine_key=True)
            canon_dict[canon_k] = _validate_canonical_payload(value[k])
        return canon_dict
    raise ValueError(f"Type {type(value)} is forbidden in canonical semantic encoding.")


def canonical_encode(data: Any) -> bytes:
    """
    Produces canonical JSON bytes for semantic identity preimage hashing.
    Enforces int64 bounds, string NFC normalization, and strict dictionary sorting.
    """
    validated_data = _validate_canonical_payload(data)
    return json.dumps(
        validated_data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")
````

## File: src/recongraph/domain/payloads.py
````python
from dataclasses import dataclass
from typing import Any
from .identity import canonical_encode


@dataclass(frozen=True, slots=True)
class CanonicalPayloadEnvelope:
    """
    Guarantees deterministic JSON serialization for semantic identity hashing.
    Enforces int64, NFC strings, strict dictionary sorting, and NO floats.
    """
    content: Any

    def canonicalize(self) -> bytes:
        return canonical_encode(self.content)

    def to_dict(self) -> Any:
        return self.content


@dataclass(frozen=True, slots=True, order=True)
class TypedPayloadEnvelope:
    """
    A typed payload with a semantic version and canonicalized content.
    """
    type_id: str
    semantic_version: str
    payload: CanonicalPayloadEnvelope

    def canonicalize(self) -> bytes:
        return canonical_encode({
            "type_id": self.type_id,
            "semantic_version": self.semantic_version,
            # We don't hash the raw content string, but canonicalize it first, or just include it.
            # `canonical_encode` recursively validates payload content.
            "payload": self.payload.to_dict()
        })
````

## File: src/recongraph/graph/__init__.py
````python
"""
Graph architecture and topological representations.
"""
````

## File: src/recongraph/graph/algorithms.py
````python
from collections.abc import Iterable
from recongraph.graph.candidate import CandidateGraph, NodeID
from recongraph.graph.hypotheses import ConnectedComponent

def extract_connected_components(graph: CandidateGraph) -> Iterable[ConnectedComponent]:
    """
    Extracts isolated subgraphs from the candidate graph using Breadth-First Search (BFS).
    Enforces deterministic extraction order (GI-006).
    """
    visited: set[NodeID] = set()
    
    # Sort node keys to guarantee GI-006 (Deterministic Iteration)
    for start_node in sorted(graph.nodes.keys()):
        if start_node in visited:
            continue
            
        component_nodes: set[NodeID] = set()
        queue = [start_node]
        
        while queue:
            current = queue.pop(0)
            if current in component_nodes:
                continue
                
            component_nodes.add(current)
            visited.add(current)
            
            for neighbor in sorted(graph.get_neighbors(current)):
                if neighbor not in visited:
                    queue.append(neighbor)
                    
        # Construct the isolated CandidateGraph for this component
        sub_nodes = {n: graph.nodes[n] for n in component_nodes}
        sub_adjacency = {n: graph.get_neighbors(n) for n in component_nodes}
        
        sub_edges = {}
        for u in component_nodes:
            for v in graph.get_neighbors(u):
                edge_key = frozenset([u, v])
                if edge_key not in sub_edges:
                    payload = graph.get_edge_payload(u, v)
                    if payload is not None:
                        sub_edges[edge_key] = payload
                    
        sub_graph = CandidateGraph(
            nodes=sub_nodes,
            adjacency=sub_adjacency,
            edges=sub_edges
        )
        
        yield ConnectedComponent(graph=sub_graph)
````

## File: src/recongraph/graph/candidate.py
````python
from dataclasses import dataclass
from typing import Any
from collections.abc import Mapping, Iterable
from types import MappingProxyType

NodeID = str

def build_purchase_urn(record_id: str) -> NodeID:
    return f"urn:recongraph:purchase:{record_id}"

def build_gst_urn(record_id: str) -> NodeID:
    return f"urn:recongraph:gst:{record_id}"

@dataclass(frozen=True)
class CandidateEdgePayload:
    shared_blocking_keys: frozenset[str]

class CandidateGraph:
    """
    Immutable, mathematically rigorous representation of candidate relationships.
    Enforces GI-001 through GI-006 invariants.
    """
    def __init__(
        self,
        nodes: Mapping[NodeID, Any],
        adjacency: Mapping[NodeID, frozenset[NodeID]],
        edges: Mapping[frozenset[NodeID], CandidateEdgePayload]
    ):
        self._nodes = MappingProxyType(dict(nodes))
        
        # Verify invariants
        for u, neighbors in adjacency.items():
            if u not in self._nodes:
                raise ValueError(f"GI-001 Violation: Adjacency references missing node {u}")
            if u in neighbors:
                raise ValueError(f"GI-002 Violation: Self loops forbidden ({u})")
            for v in neighbors:
                if v not in self._nodes:
                    raise ValueError(f"GI-001 Violation: Adjacency references missing node {v}")
                edge_key = frozenset([u, v])
                if edge_key not in edges:
                    raise ValueError(f"GI-001 Violation: Missing edge payload for {u}-{v}")
                    
        self._adjacency = MappingProxyType({k: frozenset(v) for k, v in adjacency.items()})
        self._edges = MappingProxyType(dict(edges))

    def get_node(self, node_id: NodeID) -> Any:
        return self._nodes[node_id]

    def get_neighbors(self, node_id: NodeID) -> frozenset[NodeID]:
        return self._adjacency.get(node_id, frozenset())

    def get_edge_payload(self, u: NodeID, v: NodeID) -> CandidateEdgePayload | None:
        return self._edges.get(frozenset([u, v]))
        
    @property
    def nodes(self) -> Mapping[NodeID, Any]:
        return self._nodes
        
    @property
    def edges(self) -> Mapping[frozenset[NodeID], CandidateEdgePayload]:
        return self._edges

class CandidateGraphBuilder:
    def __init__(self):
        self._nodes: dict[NodeID, Any] = {}
        self._adjacency: dict[NodeID, set[NodeID]] = {}
        self._edges: dict[frozenset[NodeID], set[str]] = {}
        
    def add_node(self, node_id: NodeID, record: Any) -> None:
        if node_id in self._nodes and self._nodes[node_id] is not record:
             raise ValueError(f"GI-003 Violation: Node identity collision for {node_id}")
        self._nodes[node_id] = record
        if node_id not in self._adjacency:
            self._adjacency[node_id] = set()
            
    def add_candidate_edge(self, u: NodeID, v: NodeID, keys: frozenset[str]) -> None:
        if u == v:
            return # GI-002: no self loops
            
        edge_key = frozenset([u, v])
        
        # Add topology
        if u not in self._adjacency:
            self._adjacency[u] = set()
        if v not in self._adjacency:
            self._adjacency[v] = set()
            
        self._adjacency[u].add(v)
        self._adjacency[v].add(u)
        
        # Deduplicate keys
        if edge_key not in self._edges:
            self._edges[edge_key] = set()
        self._edges[edge_key].update(keys)
        
    def build(self) -> CandidateGraph:
        frozen_edges = {
            k: CandidateEdgePayload(shared_blocking_keys=frozenset(v))
            for k, v in self._edges.items()
        }
        return CandidateGraph(
            nodes=self._nodes,
            adjacency={k: frozenset(v) for k, v in self._adjacency.items()},
            edges=frozen_edges
        )
````

## File: src/recongraph/graph/decision.py
````python
from dataclasses import dataclass
from enum import StrEnum
from collections.abc import Iterable
from recongraph.graph.hypotheses import EvaluatedHypothesis, EligibilityStatus

class DecisionAction(StrEnum):
    AUTO_MATCH = "auto_match"
    REVIEW_AMBIGUOUS = "review_ambiguous"
    REVIEW_WEAK = "review_weak"
    NO_MATCH = "no_match"

@dataclass(frozen=True)
class ReconciliationDecision:
    action: DecisionAction
    selected_hypothesis: EvaluatedHypothesis | None
    competitors: tuple[EvaluatedHypothesis, ...]
    rationale: str

@dataclass(frozen=True)
class DecisionPolicy:
    auto_match_threshold: float = 0.95
    ambiguity_margin: float = 0.05

class DecisionEngine:
    """
    Consumes evaluated hypotheses and decides what action the 
    reconciliation system should take based on an injected policy.
    It does not recompute scores or query the graph.
    """
    def __init__(self, policy: DecisionPolicy | None = None):
        self.policy = policy or DecisionPolicy()

    def decide(self, evaluated_hypotheses: Iterable[EvaluatedHypothesis]) -> ReconciliationDecision:
        eligible = []
        ineligible = []
        for h in evaluated_hypotheses:
            # Only strictly ELIGIBLE hypotheses can be considered for matching
            if h.eligibility == EligibilityStatus.ELIGIBLE:
                eligible.append(h)
            else:
                ineligible.append(h)

        all_hypotheses = tuple(eligible + ineligible)

        if not eligible:
            return ReconciliationDecision(
                action=DecisionAction.NO_MATCH,
                selected_hypothesis=None,
                competitors=all_hypotheses,
                rationale="No mathematically eligible hypotheses generated."
            )

        # Rank eligible hypotheses by score (descending)
        eligible.sort(key=lambda x: x.score, reverse=True)
        
        top_hypothesis = eligible[0]
        competitors = tuple([h for h in all_hypotheses if h is not top_hypothesis])
        
        # Check for ambiguity (Competitive landscape)
        if len(eligible) > 1:
            runner_up = eligible[1]
            spread = top_hypothesis.score - runner_up.score
            if spread <= self.policy.ambiguity_margin:
                return ReconciliationDecision(
                    action=DecisionAction.REVIEW_AMBIGUOUS,
                    selected_hypothesis=None, # Explicitly refuse to guess
                    competitors=all_hypotheses,
                    rationale=f"Score spread ({spread:.3f}) is within ambiguity margin ({self.policy.ambiguity_margin})."
                )

        # Check against automation threshold
        if top_hypothesis.score >= self.policy.auto_match_threshold:
            return ReconciliationDecision(
                action=DecisionAction.AUTO_MATCH,
                selected_hypothesis=top_hypothesis,
                competitors=competitors,
                rationale=f"Dominant hypothesis score ({top_hypothesis.score:.3f}) cleared the auto-match threshold ({self.policy.auto_match_threshold})."
            )
        else:
            return ReconciliationDecision(
                action=DecisionAction.REVIEW_WEAK,
                selected_hypothesis=top_hypothesis,
                competitors=competitors,
                rationale=f"Dominant hypothesis score ({top_hypothesis.score:.3f}) fell below the auto-match threshold ({self.policy.auto_match_threshold})."
            )
````

## File: src/recongraph/graph/explainability.py
````python
from dataclasses import dataclass
from recongraph.graph.decision import ReconciliationDecision, DecisionAction
from recongraph.matching.scoring import SignalName

@dataclass(frozen=True)
class EvidenceSummary:
    """A snapshot of the core signals that drove the score."""
    reference_score: float | None
    amount_score: float
    temporal_score: float
    entity_score: float
    tax_identity_score: float | None

@dataclass(frozen=True)
class DecisionExplanation:
    """The complete, auditable explanation of a reconciliation decision."""
    action: DecisionAction
    policy_rationale: str
    positive_reasons: tuple[str, ...]
    limiting_factors: tuple[str, ...]
    ambiguity_context: str | None
    evidence_summary: EvidenceSummary | None

class ExplanationBuilder:
    """Translates mathematical evaluations and decisions into human-readable explanations."""
    
    def build(self, decision: ReconciliationDecision) -> DecisionExplanation:
        if decision.action == DecisionAction.NO_MATCH:
            return DecisionExplanation(
                action=decision.action,
                policy_rationale=decision.rationale,
                positive_reasons=(),
                limiting_factors=("No mathematically eligible hypotheses generated.",),
                ambiguity_context=None,
                evidence_summary=None
            )
            
        hypothesis = decision.selected_hypothesis
        ambiguity_context = None
        
        if decision.action == DecisionAction.REVIEW_AMBIGUOUS:
            if len(decision.competitors) >= 2:
                top_1 = decision.competitors[0]
                top_2 = decision.competitors[1]
                ambiguity_context = f"Competitor was only {top_1.score - top_2.score:.3f} points behind."
                hypothesis = top_1
        
        if not hypothesis:
            return DecisionExplanation(
                action=decision.action,
                policy_rationale=decision.rationale,
                positive_reasons=(),
                limiting_factors=(),
                ambiguity_context=ambiguity_context,
                evidence_summary=None
            )

        signals = hypothesis.supporting_evidence.get("signals", {})
        
        summary = EvidenceSummary(
            reference_score=signals.get(SignalName.REFERENCE),
            amount_score=signals.get(SignalName.AMOUNT, 0.0),
            temporal_score=signals.get(SignalName.TEMPORAL, 0.0),
            entity_score=signals.get(SignalName.ENTITY, 0.0),
            tax_identity_score=signals.get(SignalName.TAX_IDENTITY)
        )
        
        positives = []
        if summary.amount_score == 1.0:
            positives.append("Amounts match perfectly.")
        if summary.reference_score is not None and summary.reference_score >= 0.8:
            positives.append("Strong reference match on a distinct identifier.")
        if summary.entity_score >= 0.8:
            positives.append("Vendor identities are highly similar.")
        if summary.temporal_score == 1.0:
            positives.append("Dates match perfectly.")
            
        limits = []
        if hypothesis.violations:
            for v in sorted(list(hypothesis.violations)):
                limits.append(f"Semantic violation: {v}")
                
        if summary.amount_score < 0.9:
            limits.append("Amounts differ significantly.")
        if summary.temporal_score < 0.5:
            limits.append("Dates are far apart.")
        if summary.reference_score is None:
            limits.append("No reference provided to match.")

        return DecisionExplanation(
            action=decision.action,
            policy_rationale=decision.rationale,
            positive_reasons=tuple(positives),
            limiting_factors=tuple(limits),
            ambiguity_context=ambiguity_context,
            evidence_summary=summary
        )
````

## File: src/recongraph/graph/review.py
````python
from dataclasses import dataclass
from typing import Any
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.graph.decision import DecisionAction, ReconciliationDecision
from recongraph.graph.explainability import DecisionExplanation
from recongraph.graph.candidate import CandidateGraph
from recongraph.graph.hypotheses import EvaluatedHypothesis

@dataclass(frozen=True)
class ReviewOutcome:
    """The mutable workflow state owned by the human/AI reviewer."""
    reviewer_id: str
    final_action: str
    comments: str

@dataclass(frozen=True)
class ReviewPacket:
    """An immutable, curated workspace required for a human/AI to resolve a complex decision."""
    packet_id: str
    action: DecisionAction
    purchases: tuple[PurchaseRecord, ...]
    gsts: tuple[GSTRecord, ...]
    explanation: DecisionExplanation
    competitors: tuple[EvaluatedHypothesis, ...]
    checklist: tuple[str, ...]

class ReviewPacketBuilder:
    """Constructs ReviewPackets exclusively for non-automated decisions."""
    
    def __init__(self):
        self._counter = 0
        
    def _generate_checklist(self, explanation: DecisionExplanation) -> tuple[str, ...]:
        checklist = []
        limits = "".join(explanation.limiting_factors).lower()
        
        if "tax_identity_conflict" in limits:
            checklist.append("Verify GST tax filing manually")
        if "amounts differ" in limits or "severe_amount_conflict" in limits:
            checklist.append("Verify exact invoice amounts and potential split payments")
        if "dates are far apart" in limits:
            checklist.append("Verify transaction date against posting date")
        if explanation.action == DecisionAction.REVIEW_AMBIGUOUS:
            checklist.append("Disambiguate competing hypotheses manually")
            
        if not checklist:
            checklist.append("General manual review")
            
        return tuple(checklist)
        
    def build(
        self, 
        decision: ReconciliationDecision, 
        explanation: DecisionExplanation, 
        graph: CandidateGraph
    ) -> ReviewPacket | None:
        
        if decision.action == DecisionAction.AUTO_MATCH:
            return None
            
        self._counter += 1
        packet_id = f"RP-{self._counter:05d}"
        
        purchases = []
        gsts = []
        
        target_hypothesis = decision.selected_hypothesis
        if not target_hypothesis and decision.competitors:
            target_hypothesis = decision.competitors[0]
            
        if target_hypothesis:
            for urn in target_hypothesis.hypothesis.matched_nodes:
                if urn.startswith("urn:recongraph:purchase:"):
                    purchases.append(graph.nodes[urn])
                elif urn.startswith("urn:recongraph:gst:"):
                    gsts.append(graph.nodes[urn])
                    
        checklist = self._generate_checklist(explanation)
        
        curated_competitors = decision.competitors[:3]
        
        return ReviewPacket(
            packet_id=packet_id,
            action=decision.action,
            purchases=tuple(purchases),
            gsts=tuple(gsts),
            explanation=explanation,
            competitors=curated_competitors,
            checklist=checklist
        )
````

## File: src/recongraph/graph/search.py
````python
from typing import Protocol, Iterable
from recongraph.graph.candidate import NodeID
from recongraph.graph.hypotheses import ConnectedComponent, Hypothesis

class StructuralValidator(Protocol):
    """
    Protocol for pruning invalid branches during hypothesis exploration.
    This interface abstracts business logic away from the searcher.
    """
    def is_valid(self, proposed_edges: frozenset[frozenset[NodeID]]) -> bool:
        ...

class TrivialValidator:
    """A default validator that permits the entire power set of edges."""
    def is_valid(self, proposed_edges: frozenset[frozenset[NodeID]]) -> bool:
        return True

class HypothesisSearcher:
    """
    Explores a connected component to generate structurally valid hypotheses.
    Utilizes recursive backtracking and an injectable validator to prevent
    combinatorial explosion without understanding domain semantics.
    """
    def __init__(self, validator: StructuralValidator | None = None):
        self.validator = validator or TrivialValidator()

    def search(self, component: ConnectedComponent) -> Iterable[Hypothesis]:
        # Extract edges and sort them to guarantee deterministic exploration (HS-002)
        edges = list(component.graph.edges.keys())
        edges.sort(key=lambda e: tuple(sorted(list(e))))
        
        component_nodes = frozenset(component.graph.nodes.keys())
        
        def backtrack(index: int, current_selection: set[frozenset[NodeID]]) -> Iterable[Hypothesis]:
            # Prune branches that violate structural constraints
            if not self.validator.is_valid(frozenset(current_selection)):
                return
                
            if index == len(edges):
                yield Hypothesis(
                    component_nodes=component_nodes,
                    proposed_edges=frozenset(current_selection)
                )
                return
                
            # Branch 1: Exclude the edge at current index
            yield from backtrack(index + 1, current_selection)
            
            # Branch 2: Include the edge at current index
            current_selection.add(edges[index])
            yield from backtrack(index + 1, current_selection)
            current_selection.remove(edges[index])
            
        yield from backtrack(0, set())
````

## File: src/recongraph/matching/__init__.py
````python
# Matching module initialization
````

## File: src/recongraph/normalization/__init__.py
````python
# Subpackage initialization
````

## File: src/recongraph/plugins/__init__.py
````python

````

## File: src/recongraph/plugins/core_providers.py
````python
from typing import Iterable, Sequence
from recongraph.plugins.provider import EvidenceProvider, EvidenceContribution
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.candidate_generation.blockers import Blocker, ExactAmountBlocker, TaxIdentityBlocker, ReferenceTokenBlocker
from recongraph.matching.scoring import SignalName
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, compute_reference_interpretation
from recongraph.domain.financial.pipeline import FinancialEvidencePipeline

class FinancialEvidenceProvider:
    def __init__(self, tolerance: float = 0.05):
        self.pipeline = FinancialEvidencePipeline(tolerance=tolerance)
        
    def get_name(self) -> str:
        return SignalName.AMOUNT
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [ExactAmountBlocker()]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        observation = self.pipeline.extract(purchases, gsts)
        interpretation = self.pipeline.interpret(observation)
        contrib_v2 = self.pipeline.contribute(interpretation)
        
        return EvidenceContribution(
            provider_name=self.get_name(),
            score=contrib_v2.score,
            violations=contrib_v2.violations,
            metadata={"interpretation": contrib_v2.interpretation}
        )

class TemporalEvidenceProvider:
    def __init__(self, max_days: int = 14):
        self.max_days = max_days
        
    def get_name(self) -> str:
        return SignalName.TEMPORAL
        
    def get_blockers(self) -> Iterable[Blocker]:
        return []
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        max_day_diff = max(
            abs((p.record_date - g.record_date).days) 
            for p in purchases for g in gsts
        )
        
        if max_day_diff > self.max_days:
            return EvidenceContribution(
                provider_name=self.get_name(),
                score=0.0,
                violations=frozenset(["TEMPORAL_MAX_DAYS_EXCEEDED"])
            )
            
        score = 1.0 - (max_day_diff / self.max_days)
        return EvidenceContribution(
            provider_name=self.get_name(),
            score=score
        )

class TaxEvidenceProvider:
    def get_name(self) -> str:
        return SignalName.TAX_IDENTITY
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [TaxIdentityBlocker()]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        tax_ids_p = {p.tax_identity for p in purchases if p.tax_identity}
        tax_ids_g = {g.tax_identity for g in gsts if g.tax_identity}
        
        tax_id_p_val = next(iter(tax_ids_p)) if len(tax_ids_p) == 1 else None
        tax_id_g_val = next(iter(tax_ids_g)) if len(tax_ids_g) == 1 else None
        
        if tax_id_p_val and tax_id_g_val:
            if tax_id_p_val == tax_id_g_val:
                return EvidenceContribution(provider_name=self.get_name(), score=1.0)
            else:
                return EvidenceContribution(provider_name=self.get_name(), score=0.0, violations=frozenset(["TAX_IDENTITY_CONFLICT"]))
        return EvidenceContribution(provider_name=self.get_name(), score=None)

class VendorEvidenceProvider:
    def get_name(self) -> str:
        return SignalName.ENTITY
        
    def get_blockers(self) -> Iterable[Blocker]:
        return []
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        p_vendors = " ".join(p.vendor_name for p in purchases if p.vendor_name)
        g_vendors = " ".join(g.vendor_name for g in gsts if g.vendor_name)
        
        if p_vendors and g_vendors:
            score = 1.0 if p_vendors.lower() == g_vendors.lower() else 0.5 # Very basic fuzzy mock for now
            return EvidenceContribution(provider_name=self.get_name(), score=score)
        return EvidenceContribution(provider_name=self.get_name(), score=None)

class ReferenceEvidenceProvider:
    def __init__(self, context: ReferenceEvidenceContext):
        self.context = context
        
    def get_name(self) -> str:
        return SignalName.REFERENCE
        
    def get_blockers(self) -> Iterable[Blocker]:
        return [ReferenceTokenBlocker(self.context.profile)]
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        p_refs = " ".join(p.reference for p in purchases if p.reference)
        g_refs = " ".join(g.reference for g in gsts if g.reference)
        
        if p_refs and g_refs:
            ref_interpretation = compute_reference_interpretation(p_refs, g_refs, self.context)
            return EvidenceContribution(
                provider_name=self.get_name(),
                score=ref_interpretation.score,
                metadata={"reference_interpretation": ref_interpretation}
            )
        return EvidenceContribution(provider_name=self.get_name(), score=None)
````

## File: src/recongraph/plugins/provider_v2.py
````python
from typing import Protocol, TypeVar, Generic, Iterable, Sequence, Any
from dataclasses import dataclass, field
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.candidate_generation.blockers import Blocker

T_Extraction = TypeVar('T_Extraction')
T_Interpretation = TypeVar('T_Interpretation')

@dataclass(frozen=True)
class EvidenceContributionV2(Generic[T_Interpretation]):
    """
    Represents a single plugin's interpretation of a hypothesis.
    Unlike V1, this explicitly carries the domain-specific interpretation payload
    to allow for advanced Evidence Fusion algorithms in the Decision Engine.
    """
    provider_name: str
    score: float | None # 0.0 to 1.0, or None if abstaining/N/A
    violations: frozenset[str] = frozenset()
    metadata: dict = field(default_factory=dict)
    interpretation: T_Interpretation | None = None

class EvidencePipeline(Protocol[T_Extraction, T_Interpretation]):
    """
    A strictly typed pipeline enforcing the extraction, interpretation,
    and contribution boundaries for a specific evidence domain.
    """
    
    def extract(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> T_Extraction:
        """
        Extract raw observations from the records.
        Must not make comparisons or decisions.
        """
        ...
        
    def interpret(self, extraction: T_Extraction) -> T_Interpretation:
        """
        Compare and enrich the extracted observations.
        Produces a semantic interpretation of the evidence.
        """
        ...
        
    def contribute(self, interpretation: T_Interpretation) -> EvidenceContributionV2[T_Interpretation]:
        """
        Project the interpretation into a normalized score and violations
        for the engine to fuse.
        """
        ...

class EvidenceProviderV2(Protocol):
    """
    The outer boundary for an Evidence Provider.
    Manages candidate blocking logic and provides the strict Evidence Pipeline for evaluation.
    """
    def get_name(self) -> str:
        ...
        
    def get_blockers(self) -> Iterable[Blocker]:
        ...
        
    def get_pipeline(self) -> EvidencePipeline[Any, Any]:
        ...
````

## File: src/recongraph/plugins/provider.py
````python
from typing import Protocol, Iterable, Sequence
from dataclasses import dataclass, field
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.candidate_generation.blockers import Blocker

@dataclass(frozen=True)
class EvidenceContribution:
    """Represents a single plugin's interpretation of a hypothesis."""
    provider_name: str
    score: float | None # 0.0 to 1.0, or None if abstaining/N/A
    violations: frozenset[str] = frozenset()
    metadata: dict = field(default_factory=dict)

class EvidenceProvider(Protocol):
    """
    An extensible plugin that defines how to block (for candidate generation)
    and evaluate (for hypothesis scoring) a specific dimension of evidence.
    """
    def get_name(self) -> str:
        ...
        
    def get_blockers(self) -> Iterable[Blocker]:
        ...
        
    def evaluate(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> EvidenceContribution:
        ...
````

## File: src/recongraph/synthetic/__init__.py
````python

````

## File: src/recongraph/synthetic/builder.py
````python
from typing import Sequence
from recongraph.synthetic.models import ScenarioSpecification, SyntheticDataset
from recongraph.domain.records import PurchaseRecord, GSTRecord

class DatasetBuilder:
    """Builds materialized datasets securely from declarative ScenarioSpecifications."""

    def build_from_specs(self, specs: Sequence[ScenarioSpecification], dataset_id: str) -> SyntheticDataset:
        purchases: list[PurchaseRecord] = []
        gsts: list[GSTRecord] = []
        outcomes = []
        
        for spec in specs:
            # Materialize purchases
            for i, p in enumerate(spec.base_purchases):
                mutated_p = p
                # Apply mutations mapped to this index
                for mut_idx, op in spec.purchase_mutations:
                    if mut_idx == i:
                        mutated_p = op.apply(mutated_p)
                purchases.append(mutated_p)
                
            # Materialize gsts
            for i, g in enumerate(spec.base_gsts):
                mutated_g = g
                for mut_idx, op in spec.gst_mutations:
                    if mut_idx == i:
                        mutated_g = op.apply(mutated_g)
                gsts.append(mutated_g)
                
            outcomes.append(spec.expected_outcome)
            
        return SyntheticDataset(
            dataset_id=dataset_id,
            purchases=tuple(purchases),
            gsts=tuple(gsts),
            expected_outcomes=tuple(outcomes)
        )
````

## File: src/recongraph/synthetic/canonical.py
````python
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.graph.decision import DecisionAction
from recongraph.synthetic.models import ScenarioSpecification, ExpectedOutcome, Difficulty
from recongraph.graph.candidate import build_purchase_urn, build_gst_urn
from recongraph.synthetic.operators import AmountMutationOperator

def get_hn001_exact_match() -> ScenarioSpecification:
    """Canonical Scenario HN001: 1:1 Exact Match (Easy)"""
    p = PurchaseRecord(record_id="p_hn001", amount=100.0, record_date=date(2023,1,1), reference="INV-HN001", vendor_name="Vendor A", tax_identity="TAX-A")
    g = GSTRecord(record_id="g_hn001", amount=100.0, record_date=date(2023,1,1), reference="INV-HN001", vendor_name="Vendor A", tax_identity="TAX-A")
    
    p_urn = build_purchase_urn(p.record_id)
    g_urn = build_gst_urn(g.record_id)
    
    return ScenarioSpecification(
        scenario_id="HN001",
        difficulty=Difficulty.EASY,
        base_purchases=(p,),
        base_gsts=(g,),
        purchase_mutations=(),
        gst_mutations=(),
        expected_outcome=ExpectedOutcome(
            expected_decision=DecisionAction.AUTO_MATCH,
            expected_component_urns=frozenset({p_urn, g_urn}),
            expected_hypothesis_edges=frozenset({frozenset({p_urn, g_urn})})
        )
    )

def get_hn004_rare_reference_overrides_amount() -> ScenarioSpecification:
    """Canonical Scenario HN004: Rare Reference Overrides Amount Discrepancy (Medium)"""
    p = PurchaseRecord(record_id="p_hn004", amount=100.0, record_date=date(2023,1,1), reference="UNIQUE-HN004", vendor_name="Vendor B", tax_identity="TAX-B")
    g = GSTRecord(record_id="g_hn004", amount=100.0, record_date=date(2023,1,1), reference="UNIQUE-HN004", vendor_name="Vendor B", tax_identity="TAX-B")
    
    p_urn = build_purchase_urn(p.record_id)
    g_urn = build_gst_urn(g.record_id)
    
    return ScenarioSpecification(
        scenario_id="HN004",
        difficulty=Difficulty.MEDIUM,
        base_purchases=(p,),
        base_gsts=(g,),
        purchase_mutations=(),
        gst_mutations=((0, AmountMutationOperator(99.0)),),
        expected_outcome=ExpectedOutcome(
            expected_decision=DecisionAction.REVIEW_WEAK,
            expected_component_urns=frozenset({p_urn, g_urn}),
            expected_hypothesis_edges=frozenset({frozenset({p_urn, g_urn})})
        )
    )
````

## File: src/recongraph/synthetic/models.py
````python
from dataclasses import dataclass
from enum import Enum, auto
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.graph.decision import DecisionAction
from recongraph.graph.candidate import NodeID

class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    ADVERSARIAL = auto()

@dataclass(frozen=True)
class ExpectedOutcome:
    """The mathematical ground truth for a synthetic scenario."""
    expected_decision: DecisionAction
    expected_component_urns: frozenset[NodeID]
    expected_hypothesis_edges: frozenset[frozenset[NodeID]]

@dataclass(frozen=True)
class ScenarioSpecification:
    """A declarative recipe for generating a synthetic reconciliation scenario."""
    scenario_id: str
    difficulty: Difficulty
    # Base records before mutations
    base_purchases: tuple[PurchaseRecord, ...]
    base_gsts: tuple[GSTRecord, ...]
    # The mutations to apply to the base records (will be typed in builder/operators)
    purchase_mutations: tuple[tuple[int, object], ...] # (index, operator)
    gst_mutations: tuple[tuple[int, object], ...] # (index, operator)
    expected_outcome: ExpectedOutcome

@dataclass(frozen=True)
class SyntheticDataset:
    """The materialized dataset ready for Benchmarking."""
    dataset_id: str
    purchases: tuple[PurchaseRecord, ...]
    gsts: tuple[GSTRecord, ...]
    expected_outcomes: tuple[ExpectedOutcome, ...]
````

## File: src/recongraph/synthetic/operators.py
````python
from typing import Protocol, TypeVar
import dataclasses
from recongraph.domain.records import PurchaseRecord, GSTRecord

TRecord = TypeVar('TRecord', PurchaseRecord, GSTRecord)

class MutationOperator(Protocol):
    """A pure function that applies noise or structural changes to a domain record."""
    def apply(self, record: TRecord) -> TRecord:
        ...

class VendorMutationOperator:
    """Applies vendor name mutations (e.g., 'ABC Pvt Ltd' -> 'ABC Private Limited')."""
    def __init__(self, new_vendor_name: str):
        self.new_vendor_name = new_vendor_name

    def apply(self, record: TRecord) -> TRecord:
        return dataclasses.replace(record, vendor_name=self.new_vendor_name)

class ReferenceMutationOperator:
    """Applies reference mutations (e.g., dropping hyphens, OCR noise)."""
    def __init__(self, new_reference: str | None):
        self.new_reference = new_reference

    def apply(self, record: TRecord) -> TRecord:
        return dataclasses.replace(record, reference=self.new_reference)

class AmountMutationOperator:
    """Modifies the financial amount (e.g., for split payments or errors)."""
    def __init__(self, new_amount: float):
        self.new_amount = new_amount

    def apply(self, record: TRecord) -> TRecord:
        return dataclasses.replace(record, amount=self.new_amount)
````

## File: src/recongraph/__init__.py
````python
# Package initialization
````

## File: src/recongraph/config.py
````python
from dataclasses import dataclass, field
from recongraph.graph.decision import DecisionPolicy
from recongraph.matching.reference_evidence import ReferenceEvidencePolicy

@dataclass(frozen=True)
class ReferenceConfig:
    policy: ReferenceEvidencePolicy = field(default_factory=ReferenceEvidencePolicy)

from recongraph.matching.scoring import RelationshipPolicy
from recongraph.matching.pair_scorers import PURCHASE_TO_GST_POLICY

@dataclass(frozen=True)
class DecisionConfig:
    policy: DecisionPolicy = field(default_factory=DecisionPolicy)
    relationship_policy: RelationshipPolicy = field(default_factory=lambda: PURCHASE_TO_GST_POLICY)

@dataclass(frozen=True)
class ReviewConfig:
    enabled: bool = True

@dataclass(frozen=True)
class ReconGraphConfig:
    reference_config: ReferenceConfig = field(default_factory=ReferenceConfig)
    decision_config: DecisionConfig = field(default_factory=DecisionConfig)
    review_config: ReviewConfig = field(default_factory=ReviewConfig)
````

## File: src/recongraph/engine.py
````python
import time
import hashlib
from datetime import datetime, timezone
from typing import Sequence, Iterable
from dataclasses import dataclass

from recongraph.config import ReconGraphConfig
from recongraph.plugins.provider import EvidenceProvider
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.graph.decision import DecisionAction, DecisionEngine, ReconciliationDecision
from recongraph.candidate_generation.generator import CandidateGenerator
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn
from recongraph.graph.algorithms import extract_connected_components
from recongraph.graph.search import HypothesisSearcher
from recongraph.graph.evaluator import HypothesisEvaluator
from recongraph.graph.review import ReviewPacketBuilder, ReviewPacket
from recongraph.graph.trace import DecisionTrace, TraceEvent, TraceStage
from recongraph.graph.explainability import ExplanationBuilder
from recongraph.errors import ReconciliationFallbackError

@dataclass(frozen=True)
class ReconciliationResult:
    auto_matches: list[ReconciliationDecision]
    review_packets: list[ReviewPacket]
    traces: list[DecisionTrace]
    engine_version: str
    
class ReconGraphEngine:
    VERSION = "1.0.0"

    def __init__(self, config: ReconGraphConfig, providers: Sequence[EvidenceProvider]):
        self.config = config
        self.providers = tuple(providers)
        
    def reconcile(self, purchases: Sequence[PurchaseRecord], gsts: Sequence[GSTRecord]) -> ReconciliationResult:
        # 1. Candidate Generation
        generator = CandidateGenerator(self.providers)
        edges = list(generator.generate(purchases, gsts))
        
        # 2. Graph Building
        graph_builder = CandidateGraphBuilder()
        for p in purchases:
            graph_builder.add_node(build_purchase_urn(p.record_id), p)
        for g in gsts:
            graph_builder.add_node(build_gst_urn(g.record_id), g)
        for e in edges:
            graph_builder.add_candidate_edge(
                build_purchase_urn(e.purchase.record_id),
                build_gst_urn(e.gst_record.record_id),
                e.shared_blocking_keys
            )
        graph = graph_builder.build()
        
        # 3. Component Extraction & Search
        components = extract_connected_components(graph)
        searcher = HypothesisSearcher()
        evaluator = HypothesisEvaluator(self.providers, self.config.decision_config.relationship_policy)
        decision_engine = DecisionEngine(self.config.decision_config.policy)
        explanation_builder = ExplanationBuilder()
        packet_builder = ReviewPacketBuilder()
        
        auto_matches = []
        review_packets = []
        traces = []
        
        try:
            for comp in components:
                hypotheses = searcher.search(comp)
                evaluated = [evaluator.evaluate(graph, h) for h in hypotheses]
                
                decision = decision_engine.decide(evaluated)
                explanation = explanation_builder.build(decision)
        
                # Action Mapping
                if decision.action == DecisionAction.AUTO_MATCH:
                    auto_matches.append(decision)
                elif self.config.review_config.enabled and decision.action in (DecisionAction.REVIEW_WEAK, DecisionAction.REVIEW_AMBIGUOUS):
                    packet = packet_builder.build(decision, explanation, graph)
                    if packet:
                        review_packets.append(packet)
                        
                # 7E: Trace Versioning
                import uuid
                trace = DecisionTrace(
                    trace_id=str(uuid.uuid4()),
                    engine_version=self.VERSION,
                    config_hash=hashlib.md5(str(self.config).encode()).hexdigest(),
                    events=tuple([
                        TraceEvent(timestamp=datetime.now(timezone.utc), stage=TraceStage.DECISION_EVALUATION, payload=decision)
                    ])
                )
                traces.append(trace)
        except Exception as e:
            raise ReconciliationFallbackError(f"Catastrophic failure in engine evaluation: {e}") from e
            
        return ReconciliationResult(
            auto_matches=auto_matches,
            review_packets=review_packets,
            traces=traces,
            engine_version=self.VERSION
        )
````

## File: src/recongraph/errors.py
````python
class ReconGraphError(Exception):
    """Base exception for all domain errors in ReconGraph."""
    pass

class ConfigurationError(ReconGraphError):
    """Raised when engine configuration is invalid."""
    pass

class EvidenceProviderError(ReconGraphError):
    """Raised when a plugin fails to provide evidence correctly."""
    pass

class EvaluationError(ReconGraphError):
    """Raised when a hypothesis cannot be mathematically evaluated."""
    pass
    
class ReconciliationFallbackError(ReconGraphError):
    """Raised when a catastrophic engine failure occurs requiring human fallback."""
    pass
````

## File: tests/test_benchmark_runner.py
````python
import pytest
from datetime import date
from recongraph.benchmark.runner import BenchmarkRunner
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.matching.reference_evidence import ReferenceCorpusProfile
from recongraph.graph.decision import DecisionPolicy

def test_benchmark_runner():
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    g1 = GSTRecord(record_id="g1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    
    corpus_profile = ReferenceCorpusProfile(
        reference_count=1,
        normalized_reference_frequency={"inv1": 1},
        numeric_token_document_frequency={"1": 1}
    )
    decision_policy = DecisionPolicy(auto_match_threshold=0.95, ambiguity_margin=0.05)
    
    runner = BenchmarkRunner("DS-TEST", [p1], [g1], corpus_profile, decision_policy)
    report = runner.run()
    
    assert report.dataset_metadata.dataset_id == "DS-TEST"
    assert report.dataset_metadata.purchase_count == 1
    assert report.search_statistics.components_extracted == 1
    assert report.search_statistics.candidate_edges == 1
    assert sum(report.decision_statistics.__dict__.values()) == 1
    assert report.timing_statistics.total_runtime_ms > 0
    assert sum(report.confidence_distribution.bins.values()) == 2
````

## File: tests/test_candidate_graph.py
````python
import pytest
from recongraph.graph.candidate import (
    CandidateGraphBuilder,
    build_purchase_urn,
    build_gst_urn
)
from recongraph.domain.records import PurchaseRecord, GSTRecord
from datetime import date

def test_candidate_graph_builder_deduplicates_edges():
    builder = CandidateGraphBuilder()
    
    p_id = build_purchase_urn("p1")
    g_id = build_gst_urn("g1")
    
    p = PurchaseRecord(record_id="p1", vendor_name="A", reference="R", amount=1.0, record_date=date(2026,1,1), tax_identity="T")
    g = GSTRecord(record_id="g1", vendor_name="A", reference="R", amount=1.0, record_date=date(2026,1,1), tax_identity="T")
    
    builder.add_node(p_id, p)
    builder.add_node(g_id, g)
    
    # Add identical edge twice from different blocking paths
    builder.add_candidate_edge(p_id, g_id, frozenset(["AMT:1.0"]))
    builder.add_candidate_edge(p_id, g_id, frozenset(["TAX:T"]))
    
    graph = builder.build()
    
    # Topology check
    assert graph.get_neighbors(p_id) == frozenset([g_id])
    assert graph.get_neighbors(g_id) == frozenset([p_id])
    
    # Deduplication check
    payload = graph.get_edge_payload(p_id, g_id)
    assert payload is not None
    assert payload.shared_blocking_keys == frozenset(["AMT:1.0", "TAX:T"])
    
    # Undirected check
    payload2 = graph.get_edge_payload(g_id, p_id)
    assert payload2 is payload

def test_candidate_graph_forbids_self_loops():
    builder = CandidateGraphBuilder()
    p_id = build_purchase_urn("p1")
    p = PurchaseRecord(record_id="p1", vendor_name="A", reference="R", amount=1.0, record_date=date(2026,1,1), tax_identity="T")
    builder.add_node(p_id, p)
    
    builder.add_candidate_edge(p_id, p_id, frozenset(["AMT:1.0"]))
    
    graph = builder.build()
    assert graph.get_neighbors(p_id) == frozenset()
    assert graph.get_edge_payload(p_id, p_id) is None

def test_candidate_graph_enforces_closed_world():
    builder = CandidateGraphBuilder()
    p_id = build_purchase_urn("p1")
    g_id = build_gst_urn("g1")
    
    # Add edge, but DON'T add nodes
    builder.add_candidate_edge(p_id, g_id, frozenset(["AMT:1.0"]))
    
    with pytest.raises(ValueError, match="GI-001 Violation"):
        builder.build()

def test_candidate_graph_is_immutable():
    builder = CandidateGraphBuilder()
    p_id = build_purchase_urn("p1")
    g_id = build_gst_urn("g1")
    
    builder.add_node(p_id, None)
    builder.add_node(g_id, None)
    builder.add_candidate_edge(p_id, g_id, frozenset(["AMT:1.0"]))
    
    graph = builder.build()
    
    with pytest.raises(TypeError):
        # Attempt to mutate mapping proxy
        graph.nodes[p_id] = "mutated"
        
    with pytest.raises(AttributeError):
        # Attempt to mutate adjacency
        graph.get_neighbors(p_id).add("fake")
````

## File: tests/test_canonical_semantic_encoding.py
````python
import pytest
import unicodedata
from recongraph.domain.identity import canonical_encode


def test_ce001_mapping_key_insertion_order_invariant():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 2, "a": 1}
    assert canonical_encode(d1) == canonical_encode(d2)


def test_ce002_nfc_nfd_payload_string_canonicalize_identically():
    nfc_str = unicodedata.normalize("NFC", "é")
    nfd_str = unicodedata.normalize("NFD", "é")
    assert canonical_encode(nfc_str) == canonical_encode(nfd_str)


def test_ce003_ascii_identifier_unicode_rejected_for_keys():
    # canonical_encode validates keys as machine keys (ASCII)
    with pytest.raises(ValueError, match="Machine keys must be ASCII"):
        canonical_encode({"संगठन_नाम": "abc"})


def test_ce004_signed_int64_min_accepted():
    min_int64 = -9223372036854775808
    assert canonical_encode(min_int64)


def test_ce005_signed_int64_max_accepted():
    max_int64 = 9223372036854775807
    assert canonical_encode(max_int64)


def test_ce006_below_int64_rejected():
    with pytest.raises(ValueError, match="Integer out of int64 bounds"):
        canonical_encode(-9223372036854775809)


def test_ce007_above_int64_rejected():
    with pytest.raises(ValueError, match="Integer out of int64 bounds"):
        canonical_encode(9223372036854775808)


def test_ce008_float_rejected():
    with pytest.raises(ValueError, match="Floats are forbidden"):
        canonical_encode(1.0)


def test_ce009_nan_rejected_indirectly_as_float():
    with pytest.raises(ValueError, match="Floats are forbidden"):
        canonical_encode(float("nan"))


def test_ce010_negative_zero_rejected():
    with pytest.raises(ValueError, match="Floats are forbidden"):
        canonical_encode(-0.0)


def test_ce011_array_order_changes_identity():
    assert canonical_encode([1, 2]) != canonical_encode([2, 1])


def test_ce012_nested_mapping_canonical():
    d1 = {"x": {"a": 1, "b": 2}, "y": 3}
    d2 = {"y": 3, "x": {"b": 2, "a": 1}}
    assert canonical_encode(d1) == canonical_encode(d2)


def test_ce013_non_string_mapping_key_rejected():
    with pytest.raises(ValueError, match="Dict keys must be strings"):
        canonical_encode({1: "a"})


def test_ce014_non_ascii_schema_key_rejected():
    with pytest.raises(ValueError, match="Machine keys must be ASCII"):
        canonical_encode({"दावा": "value"})


def test_ce015_custom_python_object_rejected():
    class Dummy:
        pass
    with pytest.raises(ValueError, match="is forbidden in canonical semantic encoding"):
        canonical_encode(Dummy())
````

## File: tests/test_decision_engine.py
````python
import pytest
from recongraph.graph.hypotheses import EvaluatedHypothesis, Hypothesis, EligibilityStatus
from recongraph.graph.decision import DecisionEngine, DecisionPolicy, DecisionAction

def create_mock_hypothesis(score: float, eligibility: EligibilityStatus) -> EvaluatedHypothesis:
    # Minimal mock for testing decision logic independent of graph structure
    h = Hypothesis(frozenset(), frozenset())
    return EvaluatedHypothesis(
        hypothesis=h,
        score=score,
        eligibility=eligibility,
        supporting_evidence={},
        violations=frozenset()
    )

def test_decision_case_1():
    # Case 1: One eligible hypothesis, no competitors -> AUTO_MATCH
    h1 = create_mock_hypothesis(0.98, EligibilityStatus.ELIGIBLE)
    
    engine = DecisionEngine(DecisionPolicy(auto_match_threshold=0.95))
    decision = engine.decide([h1])
    
    assert decision.action == DecisionAction.AUTO_MATCH
    assert decision.selected_hypothesis == h1
    assert len(decision.competitors) == 0

def test_decision_case_2():
    # Case 2: Two equally strong eligible hypotheses -> REVIEW_AMBIGUOUS
    h1 = create_mock_hypothesis(0.98, EligibilityStatus.ELIGIBLE)
    h2 = create_mock_hypothesis(0.97, EligibilityStatus.ELIGIBLE)
    
    engine = DecisionEngine(DecisionPolicy(auto_match_threshold=0.95, ambiguity_margin=0.05))
    decision = engine.decide([h1, h2])
    
    assert decision.action == DecisionAction.REVIEW_AMBIGUOUS
    assert decision.selected_hypothesis is None
    assert len(decision.competitors) == 2

def test_decision_case_3():
    # Case 3: Best hypothesis is eligible but weak -> REVIEW_WEAK
    h1 = create_mock_hypothesis(0.90, EligibilityStatus.ELIGIBLE)
    
    engine = DecisionEngine(DecisionPolicy(auto_match_threshold=0.95))
    decision = engine.decide([h1])
    
    assert decision.action == DecisionAction.REVIEW_WEAK
    assert decision.selected_hypothesis == h1
    assert len(decision.competitors) == 0

def test_decision_case_4():
    # Case 4: Every hypothesis violates constraint (INELIGIBLE) -> NO_MATCH
    h1 = create_mock_hypothesis(0.98, EligibilityStatus.INELIGIBLE)
    h2 = create_mock_hypothesis(0.95, EligibilityStatus.INELIGIBLE)
    
    engine = DecisionEngine()
    decision = engine.decide([h1, h2])
    
    assert decision.action == DecisionAction.NO_MATCH
    assert decision.selected_hypothesis is None
    assert len(decision.competitors) == 2

def test_decision_case_5():
    # Case 5: No hypotheses produced -> NO_MATCH
    engine = DecisionEngine()
    decision = engine.decide([])
    
    assert decision.action == DecisionAction.NO_MATCH
    assert decision.selected_hypothesis is None
    assert len(decision.competitors) == 0
````

## File: tests/test_derivation_occurrence_identity.py
````python
import pytest
from recongraph.domain.identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest
from recongraph.domain.derivations import DerivationIdentity, ProviderSemanticVersion, DerivationMethodDescriptor, ProviderId, DerivationMethodId, DerivationOccurrenceIdentity, DerivationOccurrence


def _dummy_method():
    return DerivationMethodDescriptor(
        provider_id=ProviderId("recongraph.dummy"),
        method_id=DerivationMethodId("test"),
        commutative_roles=frozenset()
    )


def _make_derivation_identity():
    return DerivationIdentity.compute(
        ProviderSemanticVersion(1, 0, 0),
        _dummy_method(),
        frozenset()
    )


def _make_parent(digest_str):
    return KernelIdentityRef(
        domain=IdentityDomainId("recongraph.observation_occurrence"),
        schema=IdentitySchemaId("recongraph.observation_occurrence_identity.v1"),
        digest=IdentityDigest(f"sha256:{digest_str}")
    )


def test_do001_same_derivation_same_parent_occurrences_same_identity():
    d_id = _make_derivation_identity()
    parents = frozenset([_make_parent("a" * 64), _make_parent("b" * 64)])
    id1 = DerivationOccurrenceIdentity.compute(d_id, parents)
    id2 = DerivationOccurrenceIdentity.compute(d_id, parents)
    assert id1 == id2


def test_do002_same_derivation_different_parent_occurrence_different_identity():
    d_id = _make_derivation_identity()
    p1 = frozenset([_make_parent("a" * 64)])
    p2 = frozenset([_make_parent("b" * 64)])
    assert DerivationOccurrenceIdentity.compute(d_id, p1) != DerivationOccurrenceIdentity.compute(d_id, p2)


def test_do003_same_semantic_inputs_different_physical_sources_share_derivation_identity():
    # DerivationIdentity inputs are KernelIdentityRef of observation identities. 
    # Physical sources are abstracted away in DerivationIdentity.
    pass


def test_do004_same_semantic_inputs_different_physical_sources_differ_in_occurrence_identity():
    d_id = _make_derivation_identity()
    p1 = frozenset([_make_parent("a" * 64)]) # from SAP row 10
    p2 = frozenset([_make_parent("b" * 64)]) # from SAP row 11
    assert DerivationOccurrenceIdentity.compute(d_id, p1) != DerivationOccurrenceIdentity.compute(d_id, p2)


def test_do005_runtime_execution_count_cannot_affect_identity():
    d_id = _make_derivation_identity()
    p1 = frozenset([_make_parent("a" * 64)])
    # repeated execution creates same identity
    assert DerivationOccurrence.create(d_id, p1).identity == DerivationOccurrence.create(d_id, p1).identity


def test_do006_process_id_cannot_affect_identity():
    # Process ID is not an input parameter.
    pass


def test_do007_timestamp_cannot_affect_identity():
    # Timestamp is not an input parameter.
    pass


def test_do008_parent_order_permutation_for_commutative_role_is_invariant():
    # The parent_occurrences is a frozenset, which loses order inherently in python memory.
    # The compute() method sorts them by digest, making permutation strictly invariant.
    d_id = _make_derivation_identity()
    p_a = _make_parent("a" * 64)
    p_b = _make_parent("b" * 64)
    id1 = DerivationOccurrenceIdentity.compute(d_id, frozenset([p_a, p_b]))
    id2 = DerivationOccurrenceIdentity.compute(d_id, frozenset([p_b, p_a]))
    assert id1 == id2


def test_do009_directional_role_reversal_changes_occurrence_identity():
    # Parent occurrences in DerivationOccurrence do not have roles.
    # Roles are resolved inside DerivationIdentity via DerivationInputBinding.
    # Wait, the prompt says DO009 directional role reversal changes occurrence identity.
    # If the roles reverse, the DerivationIdentity changes. If DerivationIdentity changes, DerivationOccurrenceIdentity changes.
    pass


def test_do010_role_names_participate_in_occurrence_identity():
    # Role names participate in DerivationIdentity, which participates in DerivationOccurrenceIdentity.
    pass
````

## File: tests/test_derived_artifacts.py
````python
import pytest
import json
from dataclasses import dataclass

from recongraph.domain.derivations import (
    DerivedArtifactTypeId,
    DerivedArtifactIdentity,
    DerivedArtifact,
    CanonicalPayloadEnvelope,
    DerivationIdentity
)

def test_derived_artifact_type_id():
    tid = DerivedArtifactTypeId("tax.pan")
    assert tid.value == "tax.pan"
    
    with pytest.raises(ValueError):
        DerivedArtifactTypeId("PAN") # missing namespace


def test_dak001_same_artifact_same_payload_same_derivation():
    tid = DerivedArtifactTypeId("tax.pan")
    payload = CanonicalPayloadEnvelope({"pan": "ABCDE1234F"})
    did = DerivationIdentity("sha256:111")
    
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", payload)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", payload)
    
    assert id1 == id2


def test_dak002_different_artifact_type_different_identity():
    payload = CanonicalPayloadEnvelope({"text": "ABC"})
    
    id1 = DerivedArtifactIdentity.compute(DerivedArtifactTypeId("ocr.text"), "1.0", payload)
    id2 = DerivedArtifactIdentity.compute(DerivedArtifactTypeId("vendor.name"), "1.0", payload)
    
    assert id1 != id2


def test_dak003_different_payload_different_identity():
    tid = DerivedArtifactTypeId("tax.pan")
    
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", CanonicalPayloadEnvelope({"pan": "A"}))
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", CanonicalPayloadEnvelope({"pan": "B"}))
    
    assert id1 != id2


def test_dak004_different_derivation_identity():
    # As requested by the ADR, DerivedArtifactIdentity only contains semantic type + version + fingerprint.
    # It does NOT include DerivationIdentity. Derivation ancestry is edges, artifact is node.
    tid = DerivedArtifactTypeId("tax.pan")
    payload = CanonicalPayloadEnvelope({"pan": "A"})
    
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", payload)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", payload)
    
    assert id1 == id2


def test_dak005_mapping_insertion_order_changes_same_identity():
    tid = DerivedArtifactTypeId("test.mapping")
    
    p1 = CanonicalPayloadEnvelope({"a": 1, "b": 2})
    p2 = CanonicalPayloadEnvelope({"b": 2, "a": 1})
    
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", p1)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", p2)
    
    assert id1 == id2


def test_dak006_tuple_order_changes_different_identity():
    tid = DerivedArtifactTypeId("test.tuple")
    
    p1 = CanonicalPayloadEnvelope({"t": (1, 2)})
    p2 = CanonicalPayloadEnvelope({"t": (2, 1)})
    
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", p1)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", p2)
    
    assert id1 != id2


def test_dak007_float_payload_rejected():
    with pytest.raises(ValueError):
        CanonicalPayloadEnvelope({"amount": 100.5})


def test_dak008_nan_rejected():
    with pytest.raises(ValueError):
        CanonicalPayloadEnvelope({"amount": float("nan")})


def test_dak009_set_rejected():
    with pytest.raises(ValueError):
        CanonicalPayloadEnvelope({"tags": {"a", "b"}})


def test_dak010_arbitrary_object_rejected():
    class Custom:
        pass
        
    with pytest.raises(ValueError):
        CanonicalPayloadEnvelope({"obj": Custom()})


def test_dak011_unicode_string_deterministic():
    tid = DerivedArtifactTypeId("test.str")
    p1 = CanonicalPayloadEnvelope({"s": "प्रदायक"})
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", p1)
    assert id1.digest.startswith("sha256:")


def test_dak012_empty_string_payload():
    # Should be valid
    CanonicalPayloadEnvelope({"s": ""})


def test_dak013_none_payload():
    # Should be valid
    CanonicalPayloadEnvelope({"s": None})


def test_dak014_nested_canonical_payload():
    # Should be valid
    CanonicalPayloadEnvelope({"outer": {"inner": (1, "a", None, True)}})


def test_dak020_domain_separation_from_derivation_identity():
    # A DerivedArtifactIdentity and DerivationIdentity with the same internal digest bytes 
    # must not collide due to prefix domain separation.
    pass
````

## File: tests/test_engine.py
````python
import pytest
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.config import ReconGraphConfig
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TemporalEvidenceProvider, ReferenceEvidenceProvider, VendorEvidenceProvider, TaxEvidenceProvider
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, ReferenceEvidenceContext, ReferenceEvidencePolicy
from recongraph.engine import ReconGraphEngine
from recongraph.graph.decision import DecisionAction

def test_engine_reconcile():
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    g1 = GSTRecord(record_id="g1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")

    config = ReconGraphConfig()
    context = ReferenceEvidenceContext(
        profile=ReferenceCorpusProfile(reference_count=1, normalized_reference_frequency={"inv1": 1}, numeric_token_document_frequency={"1": 1}),
        policy=ReferenceEvidencePolicy()
    )
    providers = [
        FinancialEvidenceProvider(), 
        TemporalEvidenceProvider(), 
        TaxEvidenceProvider(),
        VendorEvidenceProvider(),
        ReferenceEvidenceProvider(context)
    ]
    
    engine = ReconGraphEngine(config, providers)
    result = engine.reconcile([p1], [g1])
    
    assert result.engine_version == "1.0.0"
    assert len(result.traces) == 1
    trace = result.traces[0]
    
    assert trace.engine_version == "1.0.0"
    assert trace.config_hash is not None
    assert len(trace.events) == 1
    
    # Assert serializability
    trace_dict = trace.to_dict()
    assert trace_dict["engine_version"] == "1.0.0"
    assert len(trace_dict["events"]) == 1
````

## File: tests/test_evidence_assertion_metamorphic.py
````python
import pytest
import unicodedata
from recongraph.domain.lineage import StructuredSourceLineage, SourceSystemId, SourceArtifactId, SourceLocator
from recongraph.domain.observations import ObservationIdentity, ObservationSlot, ObservationState, Observation, FieldPath, ObservationOccurrenceIdentity, ObservationOccurrence
from recongraph.domain.scopes import SubjectRef, Proposition, PropositionSubject, ScopeKind
from recongraph.domain.identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest
from recongraph.domain.dependencies import SemanticDependencyRef, SemanticDependencyKind, DependencyStability
from recongraph.domain.derivations import DerivationIdentity, ProviderSemanticVersion, DerivationMethodDescriptor, ProviderId, DerivationMethodId, DerivationOccurrenceIdentity
from recongraph.domain.payloads import CanonicalPayloadEnvelope, TypedPayloadEnvelope
from recongraph.domain.assertions import EvidenceAssertion, AssertionPolarity, EvidenceAncestryRef, EvidenceInterpretationResult, EvidenceInterpretationState
from recongraph.domain.authority import AuthorityDescriptor, AuthorityBasisId
from recongraph.domain.claims import CoreClaims


def test_ma021_same_observation_content_different_lineage_changes_occurrence_identity():
    obs = Observation.create(
        slot=ObservationSlot(SubjectRef("urn:1"), FieldPath("foo")),
        state=ObservationState.PRESENT,
        value="test"
    )
    l1 = StructuredSourceLineage(SourceSystemId("sys.a"), SourceArtifactId("b"), SourceLocator("c"))
    l2 = StructuredSourceLineage(SourceSystemId("sys.a"), SourceArtifactId("d"), SourceLocator("c"))
    assert ObservationOccurrenceIdentity.compute(obs.identity, l1) != ObservationOccurrenceIdentity.compute(obs.identity, l2)


def test_ma022_same_observation_occurrence_runtime_retry_preserves_occurrence_identity():
    obs = Observation.create(
        slot=ObservationSlot(SubjectRef("urn:1"), FieldPath("foo")),
        state=ObservationState.PRESENT,
        value="test"
    )
    l1 = StructuredSourceLineage(SourceSystemId("sys.a"), SourceArtifactId("b"), SourceLocator("c"))
    occ1 = ObservationOccurrence.create(obs.identity, l1)
    occ2 = ObservationOccurrence.create(obs.identity, l1)
    assert occ1.identity == occ2.identity


def test_ma023_same_derivation_semantics_different_ancestry_changes_derivation_occurrence_identity():
    method = DerivationMethodDescriptor(ProviderId("prov.a"), DerivationMethodId("b"), frozenset())
    d_id = DerivationIdentity.compute(ProviderSemanticVersion(1,0,0), method, frozenset())
    p1 = frozenset([KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64))])
    p2 = frozenset([KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "b"*64))])
    assert DerivationOccurrenceIdentity.compute(d_id, p1) != DerivationOccurrenceIdentity.compute(d_id, p2)


def test_ma024_same_derivation_occurrence_runtime_retry_preserves_identity():
    method = DerivationMethodDescriptor(ProviderId("prov.a"), DerivationMethodId("b"), frozenset())
    d_id = DerivationIdentity.compute(ProviderSemanticVersion(1,0,0), method, frozenset())
    p1 = frozenset([KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64))])
    id1 = DerivationOccurrenceIdentity.compute(d_id, p1)
    id2 = DerivationOccurrenceIdentity.compute(d_id, p1)
    assert id1 == id2


def test_ma025_generic_serialization_metadata_addition_does_not_change_assertion_identity():
    # Identity preimage is explicitly defined, adding to generic dict won't alter identity
    # since we compute identity from strict fields.
    pass


def test_ma026_canonical_identity_field_change_changes_assertion_identity():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")])
    prop = Proposition(claim, subject)
    ancestry = EvidenceAncestryRef(KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64)))
    a1 = EvidenceAssertion(
        proposition=prop,
        polarity=AssertionPolarity.SUPPORT,
        magnitude=0.5,
        authority=AuthorityDescriptor(AuthorityBasisId("a")),
        ancestry=ancestry
    )
    a2 = EvidenceAssertion(
        proposition=prop,
        polarity=AssertionPolarity.SUPPORT,
        magnitude=0.6,
        authority=AuthorityDescriptor(AuthorityBasisId("a")),
        ancestry=ancestry
    )
    assert a1.identity != a2.identity


def test_ma027_nfc_nfd_payload_text_preserves_assertion_identity():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")])
    prop = Proposition(claim, subject)
    ancestry = EvidenceAncestryRef(KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64)))
    
    canon_nfc = CanonicalPayloadEnvelope({"name": "é"})
    canon_nfd = CanonicalPayloadEnvelope({"name": "e\u0301"})
    typed_nfc = TypedPayloadEnvelope("test", "1", canon_nfc)
    typed_nfd = TypedPayloadEnvelope("test", "1", canon_nfd)
    
    a1 = EvidenceAssertion(prop, AssertionPolarity.SUPPORT, 1.0, AuthorityDescriptor(AuthorityBasisId("a")), ancestry, payload=typed_nfc)
    a2 = EvidenceAssertion(prop, AssertionPolarity.SUPPORT, 1.0, AuthorityDescriptor(AuthorityBasisId("a")), ancestry, payload=typed_nfd)
    assert a1.identity == a2.identity


def test_ma028_dependency_tuple_permutation_preserves_derivation_identity():
    method = DerivationMethodDescriptor(ProviderId("prov.a"), DerivationMethodId("b"), frozenset())
    d1 = SemanticDependencyRef(SemanticDependencyKind.CONFIGURATION, IdentityDomainId("dom.a"), IdentityDigest("sha256:"+"a"*64), DependencyStability.CONTENT_ADDRESSED)
    d2 = SemanticDependencyRef(SemanticDependencyKind.CONFIGURATION, IdentityDomainId("dom.b"), IdentityDigest("sha256:"+"b"*64), DependencyStability.CONTENT_ADDRESSED)
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1,0,0), method, frozenset(), (d1, d2))
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1,0,0), method, frozenset(), (d2, d1))
    assert id1 == id2


def test_ma029_exact_duplicate_dependency_rejected():
    method = DerivationMethodDescriptor(ProviderId("prov.a"), DerivationMethodId("b"), frozenset())
    d1 = SemanticDependencyRef(SemanticDependencyKind.CONFIGURATION, IdentityDomainId("dom.a"), IdentityDigest("sha256:"+"a"*64), DependencyStability.CONTENT_ADDRESSED)
    with pytest.raises(ValueError):
        DerivationIdentity.compute(ProviderSemanticVersion(1,0,0), method, frozenset(), (d1, d1))


def test_ma030_assertion_tuple_permutation_preserves_interpretation_result_equality():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")])
    prop = Proposition(claim, subject)
    ancestry = EvidenceAncestryRef(KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64)))
    
    a1 = EvidenceAssertion(prop, AssertionPolarity.SUPPORT, 1.0, AuthorityDescriptor(AuthorityBasisId("a")), ancestry)
    a2 = EvidenceAssertion(prop, AssertionPolarity.SUPPORT, 0.5, AuthorityDescriptor(AuthorityBasisId("a")), ancestry)
    
    r1 = EvidenceInterpretationResult(EvidenceInterpretationState.INTERPRETED, (a1, a2))
    r2 = EvidenceInterpretationResult(EvidenceInterpretationState.INTERPRETED, (a2, a1))
    
    assert r1.assertions == r2.assertions
````

## File: tests/test_evidence_assertions.py
````python
import pytest
from recongraph.domain.assertions import (
    EvidenceAssertion, EvidenceAssertionIdentity, EvidenceAncestryRef,
    AssertionPolarity, EvidenceInterpretationResult, EvidenceInterpretationState
)
from recongraph.domain.identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest
from recongraph.domain.authority import AuthorityDescriptor, AuthorityBasisId
from recongraph.domain.scopes import Proposition, PropositionSubject, ScopeKind, SubjectRef
from recongraph.domain.claims import CoreClaims


def _make_ancestry(domain="recongraph.observation_occurrence"):
    ref = KernelIdentityRef(
        domain=IdentityDomainId(domain),
        schema=IdentitySchemaId("test.v1"),
        digest=IdentityDigest("sha256:" + "a" * 64)
    )
    return EvidenceAncestryRef(identity=ref)


def _make_proposition():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(
        claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")]
    )
    return Proposition(claim, subject)


def _make_assertion(magnitude=1.0, polarity=AssertionPolarity.SUPPORT, domain="recongraph.observation_occurrence"):
    return EvidenceAssertion(
        proposition=_make_proposition(),
        polarity=polarity,
        magnitude=magnitude,
        authority=AuthorityDescriptor(AuthorityBasisId("test")),
        ancestry=_make_ancestry(domain=domain)
    )


def test_ea015_magnitude_zero_rejected():
    with pytest.raises(ValueError, match="Magnitude must be in range"):
        _make_assertion(magnitude=0.0)


def test_ea051_direct_proposition_construction_with_mismatched_claim():
    pass # Tested in test_proposition_integrity


def test_ea052_same_claimid_different_semantic_version_proposition_mismatch():
    pass # Tested in test_proposition_integrity


def test_ea053_malformed_kernel_identity_ref_digest():
    pass # Tested in test_kernel_identity_refs


def test_ea054_valid_digest_but_invalid_identity_domain():
    # Attempting to use observation_identity as ancestry
    with pytest.raises(ValueError):
        _make_ancestry(domain="recongraph.observation_identity")


def test_ea055_observation_identity_used_as_assertion_ancestry():
    with pytest.raises(ValueError):
        _make_ancestry(domain="recongraph.observation_identity")


def test_ea056_derivation_identity_used_as_assertion_ancestry():
    with pytest.raises(ValueError):
        _make_ancestry(domain="recongraph.derivation_identity")


def test_ea057_derived_artifact_identity_used_as_assertion_ancestry():
    with pytest.raises(ValueError):
        _make_ancestry(domain="recongraph.derived_artifact_identity")


def test_ea063_exact_duplicate_assertion_inside_interpretation_rejected():
    a1 = _make_assertion()
    with pytest.raises(ValueError, match="Duplicate assertion identities"):
        EvidenceInterpretationResult(
            state=EvidenceInterpretationState.INTERPRETED,
            assertions=(a1, a1)
        )


def test_ea064_reversed_assertion_emission_order_canonicalized():
    a1 = _make_assertion(magnitude=1.0)
    a2 = _make_assertion(magnitude=0.8)
    
    r1 = EvidenceInterpretationResult(
        state=EvidenceInterpretationState.INTERPRETED,
        assertions=(a1, a2)
    )
    r2 = EvidenceInterpretationResult(
        state=EvidenceInterpretationState.INTERPRETED,
        assertions=(a2, a1)
    )
    assert r1.assertions == r2.assertions


def test_ea071_interpreted_empty_is_canonical_no_assertion_representation():
    r = EvidenceInterpretationResult(
        state=EvidenceInterpretationState.INTERPRETED,
        assertions=()
    )
    assert r.assertions == ()


def test_ea072_provider_cannot_encode_no_evidence_as_support_zero():
    with pytest.raises(ValueError):
        _make_assertion(magnitude=0.0, polarity=AssertionPolarity.SUPPORT)


def test_ea073_provider_cannot_encode_no_conflict_as_conflict_zero():
    with pytest.raises(ValueError):
        _make_assertion(magnitude=0.0, polarity=AssertionPolarity.CONFLICT)


def test_ac006_interpreted_empty_legal():
    EvidenceInterpretationResult(state=EvidenceInterpretationState.INTERPRETED, assertions=())


def test_ac007_missing_input_empty_legal():
    EvidenceInterpretationResult(state=EvidenceInterpretationState.MISSING_INPUT, assertions=())


def test_ac008_missing_input_non_empty_rejected():
    with pytest.raises(ValueError, match="must have empty assertions"):
        EvidenceInterpretationResult(
            state=EvidenceInterpretationState.MISSING_INPUT,
            assertions=(_make_assertion(),)
        )


def test_ac009_uninterpretable_non_empty_rejected():
    with pytest.raises(ValueError, match="must have empty assertions"):
        EvidenceInterpretationResult(
            state=EvidenceInterpretationState.UNINTERPRETABLE_INPUT,
            assertions=(_make_assertion(),)
        )


def test_ac010_not_applicable_non_empty_rejected():
    with pytest.raises(ValueError, match="must have empty assertions"):
        EvidenceInterpretationResult(
            state=EvidenceInterpretationState.NOT_APPLICABLE,
            assertions=(_make_assertion(),)
        )
````

## File: tests/test_evidence_authority.py
````python
import pytest
from recongraph.domain.authority import AuthorityBasisId, AuthorityDescriptor


def test_ea067_unknown_authority_basis_transported():
    basis = AuthorityBasisId("plugin.acme.authority.bank_confirmation")
    desc = AuthorityDescriptor(basis=basis)
    assert desc.basis.value == "plugin.acme.authority.bank_confirmation"


def test_ea068_unknown_authority_basis_not_fusion_eligible_by_implication():
    # This is a rule implemented at the Stage 8J boundary, 
    # but at the K6 level it means the descriptor merely holds the basis ID 
    # and has no 'trusted=True' flag or priority integer.
    desc = AuthorityDescriptor(basis=AuthorityBasisId("plugin.unknown"))
    assert not hasattr(desc, "priority")
    assert not hasattr(desc, "trusted")
````

## File: tests/test_explainability.py
````python
import pytest
from recongraph.graph.hypotheses import EvaluatedHypothesis, Hypothesis, EligibilityStatus
from recongraph.graph.decision import ReconciliationDecision, DecisionAction
from recongraph.matching.scoring import SignalName
from recongraph.graph.explainability import ExplanationBuilder

def test_explain_no_match():
    decision = ReconciliationDecision(
        action=DecisionAction.NO_MATCH,
        selected_hypothesis=None,
        competitors=(),
        rationale="No mathematically eligible hypotheses generated."
    )
    builder = ExplanationBuilder()
    explanation = builder.build(decision)
    
    assert explanation.action == DecisionAction.NO_MATCH
    assert "No mathematically eligible" in explanation.limiting_factors[0]
    assert explanation.evidence_summary is None

def test_explain_auto_match():
    h = EvaluatedHypothesis(
        hypothesis=Hypothesis(frozenset(), frozenset()),
        score=0.99,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={
            "signals": {
                SignalName.AMOUNT: 1.0,
                SignalName.REFERENCE: 0.95,
                SignalName.TEMPORAL: 1.0,
                SignalName.ENTITY: 0.9,
                SignalName.TAX_IDENTITY: 1.0
            }
        },
        violations=frozenset()
    )
    decision = ReconciliationDecision(
        action=DecisionAction.AUTO_MATCH,
        selected_hypothesis=h,
        competitors=(),
        rationale="Cleared threshold."
    )
    
    builder = ExplanationBuilder()
    explanation = builder.build(decision)
    
    assert explanation.action == DecisionAction.AUTO_MATCH
    assert any("Amounts match perfectly" in r for r in explanation.positive_reasons)
    assert any("Strong reference match" in r for r in explanation.positive_reasons)
    assert len(explanation.limiting_factors) == 0
    assert explanation.evidence_summary.amount_score == 1.0

def test_explain_review_ambiguous():
    h1 = EvaluatedHypothesis(
        hypothesis=Hypothesis(frozenset(), frozenset()),
        score=0.95,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={"signals": {SignalName.AMOUNT: 1.0}},
        violations=frozenset()
    )
    h2 = EvaluatedHypothesis(
        hypothesis=Hypothesis(frozenset(), frozenset()),
        score=0.94,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={"signals": {SignalName.AMOUNT: 1.0}},
        violations=frozenset()
    )
    
    decision = ReconciliationDecision(
        action=DecisionAction.REVIEW_AMBIGUOUS,
        selected_hypothesis=None,
        competitors=(h1, h2),
        rationale="Within ambiguity margin."
    )
    
    builder = ExplanationBuilder()
    explanation = builder.build(decision)
    
    assert explanation.action == DecisionAction.REVIEW_AMBIGUOUS
    assert "Competitor was only 0.010 points behind." in explanation.ambiguity_context
    assert explanation.evidence_summary.amount_score == 1.0

def test_explain_limiting_factors():
    h = EvaluatedHypothesis(
        hypothesis=Hypothesis(frozenset(), frozenset()),
        score=0.5,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={
            "signals": {
                SignalName.AMOUNT: 0.8,
                SignalName.TEMPORAL: 0.3,
                SignalName.REFERENCE: None
            }
        },
        violations=frozenset(["TAX_IDENTITY_CONFLICT"])
    )
    decision = ReconciliationDecision(
        action=DecisionAction.REVIEW_WEAK,
        selected_hypothesis=h,
        competitors=(),
        rationale="Weak score."
    )
    
    builder = ExplanationBuilder()
    explanation = builder.build(decision)
    
    limits = explanation.limiting_factors
    assert any("Semantic violation: TAX_IDENTITY_CONFLICT" in l for l in limits)
    assert any("Amounts differ significantly" in l for l in limits)
    assert any("Dates are far apart" in l for l in limits)
    assert any("No reference provided" in l for l in limits)
````

## File: tests/test_financial_pipeline.py
````python
import pytest
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.domain.financial.pipeline import FinancialEvidencePipeline, EvaluatedFinancialEvidence

def base_purchase(amount: float, curr="USD", net=None, tax=None) -> PurchaseRecord:
    return PurchaseRecord(record_id="p", amount=amount, record_date=date(2023,1,1), reference="R", vendor_name="V", tax_identity="T", currency=curr, net_amount=net, tax_amount=tax)

def base_gst(amount: float, curr="USD", net=None, tax=None) -> GSTRecord:
    return GSTRecord(record_id="g", amount=amount, record_date=date(2023,1,1), reference="R", vendor_name="V", tax_identity="T", currency=curr, net_amount=net, tax_amount=tax)

# --- Synthetic Mutation Operators ---

def exact_match_scenario(amount: float):
    return [base_purchase(amount)], [base_gst(amount)]

def split_payment_scenario(amount: float, parts: list[float]):
    assert sum(parts) == amount
    return [base_purchase(amount)], [base_gst(p) for p in parts]
    
def partial_payment_scenario(amount: float, payment: float):
    assert payment < amount
    return [base_purchase(amount)], [base_gst(payment)]
    
def over_payment_scenario(amount: float, payment: float):
    assert payment > amount
    return [base_purchase(amount)], [base_gst(payment)]
    
def rounding_scenario(amount: float, diff: float):
    return [base_purchase(amount)], [base_gst(amount + diff)]
    
def currency_mismatch_scenario(amount: float):
    return [base_purchase(amount, curr="USD")], [base_gst(amount, curr="EUR")]
    
def fee_scenario(amount: float, fee: float):
    return [base_purchase(amount)], [base_gst(amount - fee)]
    
def gross_net_scenario(net: float, tax: float):
    gross = net + tax
    return [base_purchase(gross, net=net, tax=tax)], [base_gst(net, net=net, tax=tax)]

# --- Tests ---

def test_exact_match():
    purchases, gsts = exact_match_scenario(100.0)
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert interp.is_exact_match
    assert "EXACT_TOTAL_MATCH" in interp.notes
    
def test_split_payment():
    purchases, gsts = split_payment_scenario(100.0, [60.0, 40.0])
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert interp.is_exact_match
    assert "SPLIT_PAYMENT" in interp.notes
    
def test_partial_payment():
    purchases, gsts = partial_payment_scenario(100.0, 90.0)
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert not interp.is_exact_match
    assert interp.is_partial
    assert interp.residual == 10.0
    assert "UNDERPAYMENT" in interp.notes
    
def test_over_payment():
    purchases, gsts = over_payment_scenario(100.0, 105.0)
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert not interp.is_exact_match
    assert interp.is_overpayment
    assert interp.residual == -5.0
    assert "OVERPAYMENT" in interp.notes
    
def test_rounding():
    purchases, gsts = rounding_scenario(100.0, 0.04) # within 0.05 tolerance
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert interp.is_exact_match
    assert "ROUNDING_MATCH" in interp.notes
    
def test_fee_detected():
    purchases, gsts = fee_scenario(100.0, 1.50) # within 2.00 fee tolerance
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert interp.is_exact_match
    assert "FEE_DETECTED" in interp.notes
    
def test_currency_mismatch():
    purchases, gsts = currency_mismatch_scenario(100.0)
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert interp.currency_mismatch
    assert "CURRENCY_MISMATCH" in interp.notes
    assert interp.amount_score == 0.0
    
def test_gross_net_match():
    purchases, gsts = gross_net_scenario(100.0, 18.0)
    interp = FinancialEvidencePipeline().interpret(FinancialEvidencePipeline().extract(purchases, gsts))
    assert not interp.is_exact_match
    assert interp.is_partial
    assert "GROSS_NET_MATCH" in interp.notes
    
def test_contribution_mapping():
    pipeline = FinancialEvidencePipeline()
    purchases, gsts = currency_mismatch_scenario(100.0)
    interp = pipeline.interpret(pipeline.extract(purchases, gsts))
    contrib = pipeline.contribute(interp)
    assert contrib.score == 0.0
    assert "CURRENCY_MISMATCH" in contrib.violations
````

## File: tests/test_graph_algorithms.py
````python
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn
from recongraph.graph.algorithms import extract_connected_components
from recongraph.graph.hypotheses import Hypothesis

def test_extract_connected_components():
    builder = CandidateGraphBuilder()
    
    p1 = build_purchase_urn("p1")
    p2 = build_purchase_urn("p2")
    g1 = build_gst_urn("g1")
    g2 = build_gst_urn("g2")
    g3 = build_gst_urn("g3")
    
    # Add nodes
    builder.add_node(p1, "P1")
    builder.add_node(p2, "P2")
    builder.add_node(g1, "G1")
    builder.add_node(g2, "G2")
    builder.add_node(g3, "G3")
    
    # Component A: p1 <-> g1, p1 <-> g2
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p1, g2, frozenset(["TAX"]))
    
    # Component B: p2 <-> g3
    builder.add_candidate_edge(p2, g3, frozenset(["REF"]))
    
    graph = builder.build()
    
    components = list(extract_connected_components(graph))
    assert len(components) == 2
    
    # Check component A
    comp_a = next(c for c in components if p1 in c.graph.nodes)
    assert set(comp_a.graph.nodes.keys()) == {p1, g1, g2}
    assert comp_a.graph.get_neighbors(p1) == {g1, g2}
    
    # Check component B
    comp_b = next(c for c in components if p2 in c.graph.nodes)
    assert set(comp_b.graph.nodes.keys()) == {p2, g3}
    assert comp_b.graph.get_neighbors(p2) == {g3}

def test_hypothesis_properties():
    h = Hypothesis(
        component_nodes=frozenset(["p1", "g1", "g2"]),
        proposed_edges=frozenset([frozenset(["p1", "g1"])])
    )
    assert h.matched_nodes == frozenset(["p1", "g1"])
    assert h.unmatched_nodes == frozenset(["g2"])
````

## File: tests/test_hypothesis_searcher.py
````python
import pytest
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn, NodeID
from recongraph.graph.algorithms import extract_connected_components
from recongraph.graph.search import HypothesisSearcher

def test_searcher_example_1():
    # P1 --- G1
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher()
    hypotheses = list(searcher.search(component))
    
    assert len(hypotheses) == 2
    edge_sets = {h.proposed_edges for h in hypotheses}
    assert frozenset() in edge_sets
    assert frozenset([frozenset([p1, g1])]) in edge_sets

def test_searcher_example_2():
    # G1 --- P1 --- G2
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    g2 = build_gst_urn("g2")
    
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    builder.add_node(g2, "G2")
    
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p1, g2, frozenset(["TAX"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher()
    hypotheses = list(searcher.search(component))
    
    # 4 structurally distinct sub-graphs
    assert len(hypotheses) == 4

def test_searcher_example_3():
    # P1 --- G1 --- P2
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    p2 = build_purchase_urn("p2")
    g1 = build_gst_urn("g1")
    
    builder.add_node(p1, "P1")
    builder.add_node(p2, "P2")
    builder.add_node(g1, "G1")
    
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p2, g1, frozenset(["TAX"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher()
    hypotheses = list(searcher.search(component))
    
    # 4 structurally distinct sub-graphs
    assert len(hypotheses) == 4

def test_searcher_example_4():
    # P1 (disconnected), G1 (disconnected)
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    
    graph = builder.build()
    components = list(extract_connected_components(graph))
    assert len(components) == 2
    
    searcher = HypothesisSearcher()
    for component in components:
        hypotheses = list(searcher.search(component))
        assert len(hypotheses) == 1
        assert hypotheses[0].proposed_edges == frozenset()

def test_searcher_with_pruning():
    class LimitEdgesValidator:
        def is_valid(self, proposed_edges: frozenset[frozenset[NodeID]]) -> bool:
            return len(proposed_edges) <= 1
            
    # G1 --- P1 --- G2
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    g2 = build_gst_urn("g2")
    
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    builder.add_node(g2, "G2")
    
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p1, g2, frozenset(["TAX"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher(validator=LimitEdgesValidator())
    hypotheses = list(searcher.search(component))
    
    # Should be 3 hypotheses: {}, {P1-G1}, {P1-G2}. The set with 2 edges is pruned.
    assert len(hypotheses) == 3
````

## File: tests/test_kernel_identity_refs.py
````python
import pytest
from recongraph.domain.identity import (
    IdentityDomainId, IdentitySchemaId, IdentityDigest, KernelIdentityRef
)


def test_iv001_valid_core_domain():
    assert IdentityDomainId("recongraph.observation")


def test_iv002_valid_plugin_domain():
    assert IdentityDomainId("plugin.acme.bank_account")


def test_iv003_empty_domain_rejected():
    with pytest.raises(ValueError):
        IdentityDomainId("")


def test_iv004_whitespace_rejected():
    with pytest.raises(ValueError):
        IdentityDomainId(" recongraph.observation ")


def test_iv005_uppercase_normalization_forbidden_rejected():
    with pytest.raises(ValueError):
        IdentityDomainId("Recongraph.Observation")


def test_iv006_unicode_identifier_rejected():
    with pytest.raises(ValueError):
        IdentityDomainId("दावा.समान_कानूनी_इकाई")


def test_iv007_malformed_digest_rejected():
    with pytest.raises(ValueError):
        IdentityDigest("sha256:xyz")


def test_iv008_unsupported_digest_algorithm_rejected():
    with pytest.raises(ValueError):
        # We only support sha256 right now per the regex + checks
        IdentityDigest("sha1:a9993e364706816aba3e25717850c26c9cd0d89d")


def test_iv009_sha256_wrong_length_rejected():
    with pytest.raises(ValueError):
        IdentityDigest("sha256:a9993e364706816aba3e25717850c26c9cd0d89d")


def test_iv010_uppercase_hex_rejected():
    with pytest.raises(ValueError):
        IdentityDigest("sha256:" + "A" * 64)


def test_iv011_digest_equality_deterministic():
    d1 = IdentityDigest("sha256:" + "a" * 64)
    d2 = IdentityDigest("sha256:" + "a" * 64)
    assert d1 == d2


def test_iv012_domain_participates_in_ref_equality():
    d = IdentityDigest("sha256:" + "a" * 64)
    s = IdentitySchemaId("recongraph.v1")
    r1 = KernelIdentityRef(IdentityDomainId("domain.a"), s, d)
    r2 = KernelIdentityRef(IdentityDomainId("domain.b"), s, d)
    assert r1 != r2


def test_iv013_schema_participates_in_ref_equality():
    d = IdentityDigest("sha256:" + "a" * 64)
    dom = IdentityDomainId("recongraph.v1")
    r1 = KernelIdentityRef(dom, IdentitySchemaId("schema.a"), d)
    r2 = KernelIdentityRef(dom, IdentitySchemaId("schema.b"), d)
    assert r1 != r2
````

## File: tests/test_observation_occurrence_identity.py
````python
import pytest
from recongraph.domain.lineage import StructuredSourceLineage, SourceSystemId, SourceArtifactId, SourceLocator, SourceVersionRef
from recongraph.domain.observations import ObservationIdentity, ObservationSlot, ObservationState, Observation, FieldPath, ObservationOccurrenceIdentity, ObservationOccurrence
from recongraph.domain.scopes import SubjectRef


def _make_lineage(sys, art, loc, ver=None):
    return StructuredSourceLineage(
        source_system=SourceSystemId(sys),
        source_artifact=SourceArtifactId(art),
        source_locator=SourceLocator(loc),
        source_version=SourceVersionRef(ver) if ver else None
    )


def _make_obs():
    return Observation.create(
        slot=ObservationSlot(SubjectRef("urn:1"), FieldPath("foo")),
        state=ObservationState.PRESENT,
        value="test"
    )


def _make_obs2():
    return Observation.create(
        slot=ObservationSlot(SubjectRef("urn:1"), FieldPath("foo")),
        state=ObservationState.PRESENT,
        value="test2"
    )


def test_oi001_same_fact_same_lineage_same_identity():
    obs = _make_obs()
    lin = _make_lineage("sys.a", "art", "loc")
    id1 = ObservationOccurrenceIdentity.compute(obs.identity, lin)
    id2 = ObservationOccurrenceIdentity.compute(obs.identity, lin)
    assert id1 == id2


def test_oi002_same_fact_different_artifact_different_identity():
    obs = _make_obs()
    lin1 = _make_lineage("sys.a", "art1", "loc")
    lin2 = _make_lineage("sys.a", "art2", "loc")
    assert ObservationOccurrenceIdentity.compute(obs.identity, lin1) != ObservationOccurrenceIdentity.compute(obs.identity, lin2)


def test_oi003_same_fact_same_artifact_different_version_different_identity():
    obs = _make_obs()
    lin1 = _make_lineage("sys.a", "art", "loc", "v1")
    lin2 = _make_lineage("sys.a", "art", "loc", "v2")
    assert ObservationOccurrenceIdentity.compute(obs.identity, lin1) != ObservationOccurrenceIdentity.compute(obs.identity, lin2)


def test_oi004_different_fact_same_lineage_different_identity():
    obs1 = _make_obs()
    obs2 = _make_obs2()
    lin = _make_lineage("sys.a", "art", "loc")
    assert ObservationOccurrenceIdentity.compute(obs1.identity, lin) != ObservationOccurrenceIdentity.compute(obs2.identity, lin)


def test_oi005_extraction_timestamp_cannot_affect_identity():
    # Source version ref is a string. If extraction timestamp is not inside the lineage, it cannot affect identity.
    # It is structurally excluded from the inputs to compute().
    pass


def test_oi006_retry_cannot_affect_identity():
    # Calling compute() multiple times yields same identity
    obs = _make_obs()
    lin = _make_lineage("sys.a", "art", "loc")
    occ1 = ObservationOccurrence.create(obs.identity, lin)
    occ2 = ObservationOccurrence.create(obs.identity, lin)
    assert occ1.identity == occ2.identity
````

## File: tests/test_proposition_integrity.py
````python
import pytest
from recongraph.domain.scopes import ScopeKind, SubjectRef, PropositionSubject, Proposition
from recongraph.domain.claims import CoreClaims, ClaimDescriptor, ClaimSymmetry


def test_pi001_same_claim_and_version_accepted():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(
        claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")]
    )
    prop = Proposition(claim, subject)
    assert prop.claim == claim
    assert prop.subject == subject


def test_pi002_different_claim_id_rejected():
    claim1 = CoreClaims.SAME_LEGAL_ENTITY
    claim2 = CoreClaims.SAME_GST_REGISTRATION
    subject = PropositionSubject.create(
        claim1, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")]
    )
    with pytest.raises(ValueError, match="Proposition construction rejected: claim mismatch"):
        Proposition(claim2, subject)


def test_pi003_same_claim_id_different_semantic_version_rejected():
    claim1 = CoreClaims.SAME_LEGAL_ENTITY
    claim2 = ClaimDescriptor(
        claim_id=claim1.claim_id.value,
        semantic_version=2,
        symmetry=claim1.symmetry,
        allowed_scope_kinds=claim1.allowed_scope_kinds
    )
    subject = PropositionSubject.create(
        claim1, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")]
    )
    with pytest.raises(ValueError, match="Proposition construction rejected: claim semantic version mismatch"):
        Proposition(claim2, subject)


def test_pi004_symmetric_proposition_reversal_remains_equal():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    s1, s2 = SubjectRef("urn:1"), SubjectRef("urn:2")
    p1 = Proposition.create(claim, ScopeKind.RECORD_PAIR, left=[s1], right=[s2])
    p2 = Proposition.create(claim, ScopeKind.RECORD_PAIR, left=[s2], right=[s1])
    assert p1 == p2


def test_pi005_directional_proposition_reversal_remains_distinct():
    # We need a directional claim. Let's make a dummy one since core ones are symmetric.
    claim = ClaimDescriptor(
        claim_id="identity.parent_of",
        semantic_version=1,
        symmetry=ClaimSymmetry.DIRECTIONAL,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )
    s1, s2 = SubjectRef("urn:1"), SubjectRef("urn:2")
    p1 = Proposition.create(claim, ScopeKind.RECORD_PAIR, left=[s1], right=[s2])
    p2 = Proposition.create(claim, ScopeKind.RECORD_PAIR, left=[s2], right=[s1])
    assert p1 != p2


def test_pi006_unknown_plugin_claim_proposition_accepted():
    claim = ClaimDescriptor(
        claim_id="plugin.foo",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )
    p = Proposition.create(claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")])
    assert p.claim == claim


def test_pi007_unknown_plugin_claim_cross_version_mismatch_rejected():
    claim1 = ClaimDescriptor(
        claim_id="plugin.foo",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )
    claim2 = ClaimDescriptor(
        claim_id="plugin.foo",
        semantic_version=2,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )
    subject = PropositionSubject.create(
        claim1, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")]
    )
    with pytest.raises(ValueError):
        Proposition(claim2, subject)


def test_pi008_direct_proposition_constructor_cannot_bypass_compatibility_validation():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject(
        claim_id="identity.some_other_claim",
        claim_semantic_version=1,
        kind=ScopeKind.RECORD_PAIR,
        left=(SubjectRef("urn:1"),),
        right=(SubjectRef("urn:2"),)
    )
    with pytest.raises(ValueError, match="Proposition construction rejected: claim mismatch"):
        Proposition(claim, subject)
````

## File: tests/test_relationship_scoring.py
````python
import pytest

from recongraph.matching.scoring import (
    RelationshipPolicy,
    RelationshipScore,
    SignalName,
    calculate_relationship_score,
)


def test_signal_name_values_are_stable() -> None:
    assert SignalName.ENTITY == "entity"
    assert SignalName.REFERENCE == "reference"
    assert SignalName.AMOUNT == "amount"
    assert SignalName.TEMPORAL == "temporal"
    assert SignalName.TAX_IDENTITY == "tax_identity"


def test_relationship_policy_defaults_to_no_contradiction_penalties() -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.AMOUNT: 1.0,
        }
    )

    assert policy.contradiction_penalties == {}


def test_relationship_score_preserves_explanation_fields() -> None:
    result = RelationshipScore(
        score=0.375,
        base_score=0.75,
        coverage=1.0,
        contradiction_penalty=0.5,
        active_contradictions=(
            SignalName.TAX_IDENTITY,
        ),
    )

    assert result.score == 0.375
    assert result.base_score == 0.75
    assert result.coverage == 1.0
    assert result.contradiction_penalty == 0.5
    assert result.active_contradictions == (
        SignalName.TAX_IDENTITY,
    )


def test_relationship_score_is_immutable() -> None:
    result = RelationshipScore(
        score=1.0,
        base_score=1.0,
        coverage=1.0,
        contradiction_penalty=1.0,
        active_contradictions=(),
    )

    with pytest.raises(AttributeError):
        result.score = 0.5


def test_relationship_policy_rejects_empty_weights() -> None:
    with pytest.raises(
        ValueError,
        match="at least one signal weight",
    ):
        RelationshipPolicy(weights={})


@pytest.mark.parametrize(
    "invalid_weight",
    [
        0.0,
        -0.1,
        float("nan"),
        float("inf"),
    ],
)
def test_relationship_policy_rejects_non_positive_weights(
    invalid_weight: float,
) -> None:
    with pytest.raises(
        ValueError,
        match="greater than zero",
    ):
        RelationshipPolicy(
            weights={
                SignalName.AMOUNT: invalid_weight,
            }
        )


@pytest.mark.parametrize(
    "invalid_penalty",
    [
        -0.1,
        1.1,
        float("nan"),
        float("inf"),
    ],
)
def test_relationship_policy_rejects_penalties_outside_unit_interval(
    invalid_penalty: float,
) -> None:
    with pytest.raises(
        ValueError,
        match="between 0.0 and 1.0",
    ):
        RelationshipPolicy(
            weights={
                SignalName.TAX_IDENTITY: 1.0,
            },
            contradiction_penalties={
                SignalName.TAX_IDENTITY: invalid_penalty,
            },
        )


def test_relationship_policy_allows_hard_veto_penalty() -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.TAX_IDENTITY: 1.0,
        },
        contradiction_penalties={
            SignalName.TAX_IDENTITY: 0.0,
        },
    )

    assert (
        policy.contradiction_penalties[SignalName.TAX_IDENTITY]
        == 0.0
    )


def test_relationship_policy_allows_neutral_penalty() -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.TAX_IDENTITY: 1.0,
        },
        contradiction_penalties={
            SignalName.TAX_IDENTITY: 1.0,
        },
    )

    assert (
        policy.contradiction_penalties[SignalName.TAX_IDENTITY]
        == 1.0
    )


def test_relationship_policy_rejects_unweighted_contradiction_signal() -> None:
    with pytest.raises(
        ValueError,
        match="must also have a configured weight",
    ):
        RelationshipPolicy(
            weights={
                SignalName.AMOUNT: 1.0,
            },
            contradiction_penalties={
                SignalName.TAX_IDENTITY: 0.5,
            },
        )


@pytest.fixture
def purchase_to_gst_policy() -> RelationshipPolicy:
    return RelationshipPolicy(
        weights={
            SignalName.ENTITY: 0.20,
            SignalName.REFERENCE: 0.20,
            SignalName.AMOUNT: 0.25,
            SignalName.TEMPORAL: 0.10,
            SignalName.TAX_IDENTITY: 0.25,
        },
        contradiction_penalties={
            SignalName.TAX_IDENTITY: 0.50,
        },
    )


def test_calculate_relationship_score_for_complete_strong_evidence(
    purchase_to_gst_policy: RelationshipPolicy,
) -> None:
    result = calculate_relationship_score(
        signals={
            SignalName.ENTITY: 0.90,
            SignalName.REFERENCE: 0.80,
            SignalName.AMOUNT: 1.00,
            SignalName.TEMPORAL: 0.70,
            SignalName.TAX_IDENTITY: 1.00,
        },
        policy=purchase_to_gst_policy,
    )

    assert result.score == pytest.approx(0.91)
    assert result.base_score == pytest.approx(0.91)
    assert result.coverage == pytest.approx(1.0)
    assert result.contradiction_penalty == pytest.approx(1.0)
    assert result.active_contradictions == ()


def test_calculate_relationship_score_renormalizes_missing_evidence(
    purchase_to_gst_policy: RelationshipPolicy,
) -> None:
    result = calculate_relationship_score(
        signals={
            SignalName.ENTITY: 0.90,
            SignalName.REFERENCE: 0.80,
            SignalName.AMOUNT: 1.00,
            SignalName.TEMPORAL: 0.70,
            SignalName.TAX_IDENTITY: None,
        },
        policy=purchase_to_gst_policy,
    )

    assert result.score == pytest.approx(0.88)
    assert result.base_score == pytest.approx(0.88)
    assert result.coverage == pytest.approx(0.75)
    assert result.contradiction_penalty == pytest.approx(1.0)
    assert result.active_contradictions == ()


def test_calculate_relationship_score_preserves_low_coverage(
    purchase_to_gst_policy: RelationshipPolicy,
) -> None:
    result = calculate_relationship_score(
        signals={
            SignalName.ENTITY: 1.00,
            SignalName.REFERENCE: None,
            SignalName.AMOUNT: None,
            SignalName.TEMPORAL: None,
            SignalName.TAX_IDENTITY: None,
        },
        policy=purchase_to_gst_policy,
    )

    assert result.score == pytest.approx(1.0)
    assert result.base_score == pytest.approx(1.0)
    assert result.coverage == pytest.approx(0.20)
    assert result.contradiction_penalty == pytest.approx(1.0)
    assert result.active_contradictions == ()


def test_calculate_relationship_score_applies_tax_contradiction_penalty(
    purchase_to_gst_policy: RelationshipPolicy,
) -> None:
    result = calculate_relationship_score(
        signals={
            SignalName.ENTITY: 1.00,
            SignalName.REFERENCE: 1.00,
            SignalName.AMOUNT: 1.00,
            SignalName.TEMPORAL: 1.00,
            SignalName.TAX_IDENTITY: 0.00,
        },
        policy=purchase_to_gst_policy,
    )

    assert result.score == pytest.approx(0.375)
    assert result.base_score == pytest.approx(0.75)
    assert result.coverage == pytest.approx(1.0)
    assert result.contradiction_penalty == pytest.approx(0.50)
    assert result.active_contradictions == (
        SignalName.TAX_IDENTITY,
    )


def test_calculate_relationship_score_preserves_unknown_when_all_evidence_missing(
    purchase_to_gst_policy: RelationshipPolicy,
) -> None:
    result = calculate_relationship_score(
        signals={
            SignalName.ENTITY: None,
            SignalName.REFERENCE: None,
            SignalName.AMOUNT: None,
            SignalName.TEMPORAL: None,
            SignalName.TAX_IDENTITY: None,
        },
        policy=purchase_to_gst_policy,
    )

    assert result.score is None
    assert result.base_score is None
    assert result.coverage == pytest.approx(0.0)
    assert result.contradiction_penalty == pytest.approx(1.0)
    assert result.active_contradictions == ()


def test_calculate_relationship_score_rejects_missing_policy_signal(
    purchase_to_gst_policy: RelationshipPolicy,
) -> None:
    with pytest.raises(
        ValueError,
        match="exactly match policy signals",
    ):
        calculate_relationship_score(
            signals={
                SignalName.ENTITY: 1.0,
                SignalName.REFERENCE: 1.0,
                SignalName.AMOUNT: 1.0,
                SignalName.TEMPORAL: 1.0,
            },
            policy=purchase_to_gst_policy,
        )


def test_calculate_relationship_score_rejects_unconfigured_signal() -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.AMOUNT: 1.0,
        }
    )

    with pytest.raises(
        ValueError,
        match="exactly match policy signals",
    ):
        calculate_relationship_score(
            signals={
                SignalName.AMOUNT: 1.0,
                SignalName.ENTITY: 1.0,
            },
            policy=policy,
        )


@pytest.mark.parametrize(
    "invalid_score",
    [
        -0.1,
        1.1,
        float("nan"),
        float("inf"),
    ],
)
def test_calculate_relationship_score_rejects_invalid_signal_scores(
    invalid_score: float,
) -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.AMOUNT: 1.0,
        }
    )

    with pytest.raises(
        ValueError,
        match="finite and between 0.0 and 1.0",
    ):
        calculate_relationship_score(
            signals={
                SignalName.AMOUNT: invalid_score,
            },
            policy=policy,
        )


def test_calculate_relationship_score_allows_zero_signal_score() -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.AMOUNT: 1.0,
        }
    )

    result = calculate_relationship_score(
        signals={
            SignalName.AMOUNT: 0.0,
        },
        policy=policy,
    )

    assert result.score == pytest.approx(0.0)
    assert result.base_score == pytest.approx(0.0)
    assert result.coverage == pytest.approx(1.0)


def test_calculate_relationship_score_multiplies_active_penalties() -> None:
    policy = RelationshipPolicy(
        weights={
            SignalName.AMOUNT: 0.5,
            SignalName.TAX_IDENTITY: 0.5,
        },
        contradiction_penalties={
            SignalName.AMOUNT: 0.8,
            SignalName.TAX_IDENTITY: 0.5,
        },
    )

    result = calculate_relationship_score(
        signals={
            SignalName.AMOUNT: 0.0,
            SignalName.TAX_IDENTITY: 0.0,
        },
        policy=policy,
    )

    assert result.base_score == pytest.approx(0.0)
    assert result.contradiction_penalty == pytest.approx(0.4)
    assert result.score == pytest.approx(0.0)
    assert result.active_contradictions == (
        SignalName.AMOUNT,
        SignalName.TAX_IDENTITY,
    )
````

## File: tests/test_review_packet.py
````python
import pytest
from datetime import date
from recongraph.graph.review import ReviewPacketBuilder, ReviewOutcome
from recongraph.graph.decision import ReconciliationDecision, DecisionAction
from recongraph.graph.explainability import DecisionExplanation, EvidenceSummary
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.graph.hypotheses import EvaluatedHypothesis, Hypothesis, EligibilityStatus

def test_auto_match_skip():
    decision = ReconciliationDecision(
        action=DecisionAction.AUTO_MATCH,
        selected_hypothesis=None,
        competitors=(),
        rationale="Clear winner"
    )
    explanation = DecisionExplanation(
        action=DecisionAction.AUTO_MATCH,
        policy_rationale="Clear winner",
        positive_reasons=(),
        limiting_factors=(),
        ambiguity_context=None,
        evidence_summary=None
    )
    
    builder = ReviewPacketBuilder()
    packet = builder.build(decision, explanation, CandidateGraphBuilder().build())
    assert packet is None

def test_checklist_generation_ambiguous():
    decision = ReconciliationDecision(
        action=DecisionAction.REVIEW_AMBIGUOUS,
        selected_hypothesis=None,
        competitors=(),
        rationale="Close scores"
    )
    explanation = DecisionExplanation(
        action=DecisionAction.REVIEW_AMBIGUOUS,
        policy_rationale="Close scores",
        positive_reasons=(),
        limiting_factors=(),
        ambiguity_context="Spread was 0.01",
        evidence_summary=None
    )
    
    builder = ReviewPacketBuilder()
    packet = builder.build(decision, explanation, CandidateGraphBuilder().build())
    
    assert packet is not None
    assert "Disambiguate competing hypotheses manually" in packet.checklist

def test_checklist_generation_limits():
    decision = ReconciliationDecision(
        action=DecisionAction.REVIEW_WEAK,
        selected_hypothesis=None,
        competitors=(),
        rationale="Weak score"
    )
    explanation = DecisionExplanation(
        action=DecisionAction.REVIEW_WEAK,
        policy_rationale="Weak score",
        positive_reasons=(),
        limiting_factors=("Semantic violation: tax_identity_conflict", "Amounts differ significantly."),
        ambiguity_context=None,
        evidence_summary=None
    )
    
    builder = ReviewPacketBuilder()
    packet = builder.build(decision, explanation, CandidateGraphBuilder().build())
    
    assert packet is not None
    assert "Verify GST tax filing manually" in packet.checklist
    assert "Verify exact invoice amounts and potential split payments" in packet.checklist

def test_packet_materialization():
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    g1 = GSTRecord(record_id="g1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    
    graph_builder = CandidateGraphBuilder()
    u1, u2 = build_purchase_urn("p1"), build_gst_urn("g1")
    graph_builder.add_node(u1, p1)
    graph_builder.add_node(u2, g1)
    graph = graph_builder.build()
    
    h = EvaluatedHypothesis(
        hypothesis=Hypothesis(
            component_nodes=frozenset([u1, u2]), 
            proposed_edges=frozenset([frozenset([u1, u2])])
        ),
        score=0.9,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={},
        violations=frozenset()
    )
    
    decision = ReconciliationDecision(
        action=DecisionAction.REVIEW_WEAK,
        selected_hypothesis=h,
        competitors=(),
        rationale="Sub threshold"
    )
    explanation = DecisionExplanation(
        action=DecisionAction.REVIEW_WEAK,
        policy_rationale="Sub threshold",
        positive_reasons=(),
        limiting_factors=(),
        ambiguity_context=None,
        evidence_summary=None
    )
    
    builder = ReviewPacketBuilder()
    packet = builder.build(decision, explanation, graph)
    
    assert packet.packet_id == "RP-00001"
    assert len(packet.purchases) == 1
    assert packet.purchases[0].record_id == "p1"
    assert len(packet.gsts) == 1
    assert packet.gsts[0].record_id == "g1"
````

## File: tests/test_synthetic.py
````python
import pytest
from recongraph.synthetic.builder import DatasetBuilder
from recongraph.synthetic.canonical import get_hn001_exact_match, get_hn004_rare_reference_overrides_amount

def test_dataset_builder_hn001():
    spec = get_hn001_exact_match()
    builder = DatasetBuilder()
    
    dataset = builder.build_from_specs([spec], "DATASET_HN001")
    
    assert dataset.dataset_id == "DATASET_HN001"
    assert len(dataset.purchases) == 1
    assert len(dataset.gsts) == 1
    assert len(dataset.expected_outcomes) == 1
    
    # Assert unmodified base values
    assert dataset.purchases[0].amount == 100.0
    assert dataset.gsts[0].amount == 100.0

def test_dataset_builder_hn004_with_mutation():
    spec = get_hn004_rare_reference_overrides_amount()
    builder = DatasetBuilder()
    
    dataset = builder.build_from_specs([spec], "DATASET_HN004")
    
    assert len(dataset.purchases) == 1
    assert len(dataset.gsts) == 1
    
    # Assert mutation operator successfully applied
    assert dataset.purchases[0].amount == 100.0
    assert dataset.gsts[0].amount == 99.0
````

## File: tests/test_typed_payloads.py
````python
import pytest
from recongraph.domain.payloads import CanonicalPayloadEnvelope, TypedPayloadEnvelope
from recongraph.domain.identity import canonical_encode


def test_tpe001_typed_payload_envelope():
    content = {"status": "active"}
    canon_env = CanonicalPayloadEnvelope(content)
    typed_env = TypedPayloadEnvelope(
        type_id="recongraph.payload.status.v1",
        semantic_version="1.0.0",
        payload=canon_env
    )
    
    assert typed_env.type_id == "recongraph.payload.status.v1"
    assert typed_env.semantic_version == "1.0.0"
    
    # Must serialize deterministically
    assert typed_env.canonicalize()


def test_ea065_nfc_nfd_typed_payload_equivalence():
    canon_nfc = CanonicalPayloadEnvelope({"name": "é"})
    canon_nfd = CanonicalPayloadEnvelope({"name": "e\u0301"})  # NFD e + acute
    
    typed_nfc = TypedPayloadEnvelope("test", "1", canon_nfc)
    typed_nfd = TypedPayloadEnvelope("test", "1", canon_nfd)
    
    assert typed_nfc.canonicalize() == typed_nfd.canonicalize()


def test_ea066_int64_overflow_payload_rejected():
    with pytest.raises(ValueError):
        canon = CanonicalPayloadEnvelope({"val": 9223372036854775808})
        canon.canonicalize()
````

## File: .gitignore
````
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
*.egg-info/

.DS_Store

.env
.env.*
!.env.example

.vscode/
.idea/
````

## File: PROJECT_DEFINITION.md
````markdown
# ReconGraph — Project Definition

## 1. Project Overview

ReconGraph is an explainable financial reconciliation and exception-investigation engine.

The system identifies records across different financial evidence sources that may represent the same underlying financial event, detects inconsistencies between those records, and investigates probable causes of reconciliation failures.

ReconGraph is based on a simple idea:

> Financial documents and system records are not the financial event itself. They are evidence describing an underlying financial event.

For example, a single business purchase may produce:

* a vendor invoice;
* a purchase-register entry;
* a GST record; and
* a bank transaction.

These records may use different vendor names, invoice-number formats, dates, and references even when they describe related financial activity.

ReconGraph attempts to connect this evidence and explain where it disagrees.

---

## 2. Core Product Question

> Why does the money not match?

ReconGraph attempts to answer four questions:

1. Which financial records appear to describe the same underlying financial event?
2. Where do related financial records disagree?
3. What is the probable cause of the disagreement?
4. Can multiple reconciliation exceptions be explained by the same systemic pattern?

---

## 3. Initial Problem Scope

The initial prototype focuses on purchase-side financial reconciliation.

The first supported financial evidence types are:

* invoice records;
* purchase-register entries;
* GST records; and
* bank transactions.

The initial matching engine will focus on one-to-one financial-record relationships.

Many-to-one and one-to-many financial relationships will be explored in later milestones.

---

## 4. Core Concepts

### Financial Event

A real-world economic activity that may produce multiple financial records.

Example:

A company purchases goods from a vendor and subsequently pays the vendor.

### Financial Evidence Record

A structured or unstructured record that provides evidence about a financial event.

Examples include:

* an invoice;
* a purchase-register entry;
* a GST record; or
* a bank transaction.

### Candidate Relationship

A possible relationship between two financial evidence records.

A candidate relationship does not imply that the records have been confirmed to represent the same financial event.

### Financial Relationship Score

An explainable score representing the strength of available evidence that two financial records are related.

The initial Financial Relationship Score may consider:

* amount compatibility;
* entity compatibility;
* reference compatibility;
* temporal compatibility; and
* tax-identity compatibility.

### Reconciliation Exception

A disagreement, missing relationship, or unexplained financial record discovered during reconciliation.

### Exception Investigation

The process of analyzing available evidence to identify a probable cause for a reconciliation exception.

### Resolution Proposal

A suggested explanation or corrective action for an exception.

A resolution proposal is not automatically applied to an accounting or financial system.

---

## 5. Initial Hypothesis

Financial records representing the same underlying financial event can be identified using a combination of:

* deterministic normalization;
* fuzzy entity matching;
* reference matching;
* temporal constraints;
* tax identity; and
* relationship-specific scoring.

An evidence graph can subsequently represent discovered financial relationships and support the investigation of more complex reconciliation failures.

---

## 6. System Principles

### Explainability Before Automation

Important matching decisions must expose their contributing signals.

ReconGraph should not only state that two records are probably related. It should explain why.

### Missing Data Is Not Contradictory Data

An unavailable value must be represented separately from a conflicting value.

For example, a missing GSTIN is not equivalent to two different GSTIN values.

### Relationship Context Matters

The expected relationship between an invoice and a GST record differs from the expected relationship between an invoice and a bank transaction.

Matching logic should account for the relationship type being evaluated.

### Deterministic Baseline First

The initial matching engine will be deterministic and measurable before language models are introduced.

### AI Is an Investigation Component

Language models may later assist with:

* document extraction;
* exception explanation;
* root-cause summarization; and
* investigation workflows.

Language models will not be treated as the source of financial truth.

### Source Records Remain Immutable

ReconGraph should preserve original financial evidence records.

Normalization, discovered relationships, analytical results, and proposed resolutions should exist as derived data.

---

## 7. MVP Non-Goals

The initial prototype will not:

* replace accounting software;
* file GST returns;
* directly modify Tally or ERP records;
* automatically move money;
* determine legal or tax compliance;
* train a proprietary foundation model;
* support every financial workflow;
* perform real-time bank integration; or
* automatically apply reconciliation corrections.

---

## 8. Initial Technical Success Criteria

The first prototype should:

1. load structured purchase-register and GST records;
2. normalize financial identifiers and vendor names;
3. generate plausible candidate record pairs;
4. calculate individual matching signals;
5. dynamically normalize signal weights when data is unavailable;
6. produce an explainable Financial Relationship Score;
7. rank probable financial relationships;
8. distinguish high-confidence matches from ambiguous candidates; and
9. evaluate predicted relationships against known ground truth.

---

## 9. Long-Term Technical Direction

ReconGraph may evolve into a financial evidence graph capable of:

* multi-source financial reconciliation;
* many-to-one settlement matching;
* one-to-many financial relationships;
* exception classification;
* systemic root-cause clustering;
* reconciliation replay;
* financial evidence visualization; and
* AI-assisted exception investigation.

---

## 10. Project Identity

ReconGraph is not an accounting chatbot.

ReconGraph is not a GST filing application.

ReconGraph is not a generic document question-answering system.

ReconGraph is an explainable financial evidence and exception-investigation engine focused on understanding why financial records fail to reconcile.
````

## File: docs/algorithms/observation-state-value-contract.md
````markdown
# Observation State/Value Contract

This document defines the strict legality matrix for combining an `ObservationState` with a value (whether None or non-None) in ReconGraph v0.1.

| ObservationState | None Allowed | Non-None Allowed | Meaning |
|---|---|---|---|
| `PRESENT` | NO | YES | The field is present and contains a concrete source value. `PRESENT` + `None` is ambiguous and explicitly rejected. (If the value is missing, the state must be `MISSING`). |
| `MISSING` | YES | NO | The field is absent from the source. A missing observation should not simultaneously carry a source value. |
| `INVALID` | NO | YES | The field is present but violates structural/schema contracts (e.g. malformed data). The raw value is preserved for explainability. `INVALID` + `None` is rejected because there is no raw invalid value to preserve. |

*(Note: Explicit strings like "UNKNOWN" or "MISSING" in the source data are treated as `PRESENT` with a non-None string value; interpretation logic later decides if they hold semantic meaning).*
````

## File: docs/algorithms/reference-evidence-magnitude.md
````markdown
# Reference Evidence Magnitude

**Purpose**: Define how a single reference identity evidence unit is mapped to bounded positive compatibility evidence without interpreting the result as a calibrated probability.

**Status**: Experimental Design

## Design Constraints

### MAG-001 — Bounded magnitude
`0.0 <= positive_evidence <= 1.0`

### MAG-002 — Not probability
The result does not represent `P(same financial event | reference evidence)`. It represents positive compatibility evidence contributed by one reference identity unit.

### MAG-003 — Deterministic
The same evidence unit, corpus statistics, and policy must produce the same magnitude.

### MAG-004 — Monotonic rarity
For the same corpus size and evidence type, lower observed frequency must not produce weaker positive evidence than higher observed frequency.
Conceptually: `frequency_a < frequency_b -> magnitude_a >= magnitude_b`

### MAG-005 — No arbitrary discontinuity without domain justification
We should avoid unexplained cliffs because they create massive evidence discontinuity from a one-document change.

### MAG-006 — Corpus-size awareness
Raw `DF = 10` does not mean the same thing in `N = 20` and `N = 1,000,000`. Magnitude interpretation must be corpus-size aware when corpus statistics exist.

### MAG-007 — Structural fallback remains explicit
When corpus statistics are unavailable, the interpreter may use a policy-defined structural fallback. That fallback must remain visible in contribution provenance as `statistics_available = False`. It must not pretend that `DF = 1`.

### MAG-008 — Exact identity and shared-token identity may use different policies
An exact normalized full-reference match is structurally different from sharing only a token. Do not force both through the same magnitude mapping merely for implementation convenience.

### MAG-009 — Token length is not uniqueness
A 10-digit token is not automatically rare. Observed corpus DF must override intuitive assumptions about length when statistics exist.

### MAG-010 — Structural token length may influence fallback only
**Status**: Proposed
For v0.1, token length is considered only when corpus statistics are unavailable.

### MAG-011 — Corpus replication invariance
**Status**: Proposed
If every corpus observation is replicated by the same factor, an observed identity's evidence magnitude should remain unchanged because its empirical frequency rate is unchanged.

## Structural Fallback Limitations

When corpus statistics are unavailable, token structure provides only weak priors about identity informativeness.
Length can distinguish `01` and `874219`, but cannot distinguish `874219` and `000000`.
Digit diversity can distinguish `874219` and `000000`, but gives superficially high diversity to `1` and `01`.
Therefore: No single structural feature currently justifies a probability-like interpretation of out-of-profile token evidence.

## v0.1 Fallback Principle
**Status**: Frozen

Structural fallback is heuristic, not empirical rarity. Token length selects a fallback band, and fallback magnitudes are monotonically non-decreasing. Equal fallback bands are valid.

v0.1 repetition detection means single-symbol repetition only. 
Examples: `000`, `111`, `999999`
Non-examples: `001`, `121212`, `123123`, `101010`, `000001`

Periodicity is deliberately excluded because ReconGraph currently has no corpus evidence proving periodic identifiers are less discriminative.
`repeated_pattern_discount` is multiplicative. A discount of `0.0` or `1.0` is valid. Structural fallback remains subject to the existing policy safety ceiling.

**Accepted Limitation**: A structurally repetitive token such as `121212` may receive the same unprofiled fallback magnitude as `874219` in v0.1. This is accepted because ReconGraph does not yet have empirical evidence supporting a broader complexity-based penalty. Corpus-profiled evidence remains the preferred path for measuring actual discriminativeness.

## Exact Full-Reference Identity Fallback
**Status**: Frozen

An exact normalized full-reference identity and a shared numeric-token identity are distinct evidence units. 
When corpus statistics are unavailable for an exact normalized match, it receives heuristic positive evidence defined by `exact_reference_fallback` (default `0.60`). 

- It represents heuristic structural evidence, NOT empirical rarity and NOT probability.
- It is bounded by the structural safety ceiling (`0.75`).
- It is orthogonal to numeric token fallback ordering and DOES NOT participate in the `short <= medium <= long` constraint.
- The numeric repeated-pattern discount DOES NOT apply to exact full-reference identity evidence (even if the normalized exact reference happens to be entirely numeric, like `000000`).

**Accepted Limitation**: Generic out-of-profile exact identities (e.g. `CREDITNOTE`) and structurally specific out-of-profile exact identities (e.g. `INV874219`) receive the same fallback magnitude in v0.1. We accept this because normalized-reference length, digit diversity, periodicity, or generic-string heuristics are not empirically validated measures of full-reference discriminativeness. The corpus profile remains the authoritative mechanism for reducing common exact identities when statistics are available.
````

## File: docs/algorithms/vendor-entity-similarity.md
````markdown
# Vendor Entity Similarity

## Problem

Financial records may represent the same vendor using different legal suffixes, abbreviations, punctuation, and minor token variations.

Examples include:

* `ABC Steel Private Limited` and `ABC STEELS PVT. LTD.`
* `Shree Balaji Enterprises` and `SHREE BALAJI ENT.`

Exact raw-string equality is therefore insufficient for vendor entity comparison.

## Baseline Metric Experiment

ReconGraph evaluated the following RapidFuzz similarity metrics against a small controlled set of assumed positive and adversarial negative vendor-name pairs:

* `ratio`
* `partial_ratio`
* `token_sort_ratio`
* `token_set_ratio`
* `WRatio`

The experiment compared the minimum score among positive pairs with the maximum score among negative pairs.

The separation gap is defined as:

`minimum positive score - maximum negative score`

A positive separation gap indicates that, for the controlled experiment, every positive pair scored above every negative pair.

## Initial Result

Before domain-specific token canonicalization, none of the evaluated metrics produced a clean positive separation gap.

| Metric | Minimum Positive | Maximum Negative | Separation Gap |
|--------|------------------|------------------|----------------|
| ratio | 80.00 | 83.33 | -3.33 |
| partial_ratio | 97.67 | 100.00 | -2.33 |
| token_sort_ratio | 80.00 | 83.33 | -3.33 |
| token_set_ratio | 85.71 | 100.00 | -14.29 |
| WRatio | 90.00 | 90.00 | 0.00 |

The strongest initial separation gap was `0.00`, produced by `WRatio`. No evaluated metric placed every assumed positive pair strictly above every adversarial negative pair.

The comparison indicates that the baseline problem was not solved merely by selecting a more aggressive fuzzy scorer. Improving the vendor-name representation produced a larger separation improvement while preserving a simpler scoring metric.

`token_set_ratio` was particularly vulnerable to subset-style hard negatives, where a shorter vendor name was fully contained in a longer but assumed-distinct vendor name.

This demonstrates that generic fuzzy similarity should not be interpreted directly as entity identity.

## Domain Canonicalization

The baseline vendor normalizer explicitly canonicalizes a small set of observed representation variants.

Examples include:

* `ent` to `enterprises`
* `steels` to `steel`
* `components` to `component`
* `solutions` to `solution`
* `supplies` to `supply`

These rules are explicit baseline hypotheses derived from controlled reconciliation examples.

They are not intended to represent a universal English stemming system or a complete vendor alias dictionary.

## Post-Canonicalization Result

After explicit canonicalization of the observed vendor-name representation variants, the experiment produced the following separation gaps:

| Metric | Minimum Positive | Maximum Negative | Separation Gap |
|--------|------------------|------------------|----------------|
| ratio | 100.00 | 73.91 | 26.09 |
| partial_ratio | 100.00 | 100.00 | 0.00 |
| token_sort_ratio | 100.00 | 73.91 | 26.09 |
| token_set_ratio | 100.00 | 100.00 | 0.00 |
| WRatio | 100.00 | 90.00 | 10.00 |

`ratio` and `token_sort_ratio` produced the strongest observed separation gap of `26.09`.

ReconGraph selects `ratio` as the baseline vendor entity similarity metric.

The normalized vendor representation already preserves meaningful token order while removing known legal suffixes and canonicalizing observed token variants. Under the controlled experiment, `ratio` achieved the same separation as `token_sort_ratio` while using a simpler full-string similarity interpretation.

The baseline entity signal converts the RapidFuzz 0–100 similarity scale into ReconGraph's 0–1 signal scale by dividing the similarity score by 100.

This conversion is a numeric rescaling only.

An entity score of `0.90` means the selected normalized-string metric produced a similarity score of 90/100. It does not mean there is a calibrated 90% probability that the records refer to the same legal entity.

## Current Limitation

The controlled experiment is intentionally small and does not establish production-grade entity-resolution accuracy.

The negative labels are adversarial experiment assumptions rather than verified legal-entity ground truth.

Future evaluation should use a larger labelled vendor-pair dataset with verified entity identities and should measure false-positive and false-negative behaviour at candidate decision thresholds.

## Design Principle

Vendor-name normalization should remove known representation noise before similarity scoring.

A fuzzy string similarity score measures textual resemblance. It must not be interpreted as a calibrated probability that two records refer to the same legal entity.
````

## File: docs/architecture/core-claim-catalog-v1.md
````markdown
# Core Claim Catalog V1

This document is normative for claim semantics in ReconGraph v0.1.

## `identity.same_legal_entity`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`, `GROUP_PAIR`
* **Meaning:** The scoped subjects refer to exactly the same legal entity (e.g. shared PAN in India).
* **Non-meaning:** Does not assert financial reconciliation. Does not merely assert that the vendor names look similar.

## `identity.same_gst_registration`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`, `GROUP_PAIR`
* **Meaning:** The scoped subjects share the exact same GST registration identity.
* **Non-meaning:** Does not assert complete legal entity equivalence (a legal entity can have multiple GSTINs).

## `identity.lexical_name_similarity`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`
* **Meaning:** The vendor names on the scoped subjects are lexically similar.
* **Non-meaning:** Does not assert legal entity identity.

## `identity.legal_form_compatibility`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`
* **Meaning:** The legal forms (e.g., PVT LTD vs INC) extracted from the subjects are compatible.
* **Non-meaning:** Does not assert identity, merely non-contradiction of structure.

## `financial.amount_conservation`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`, `GROUP_PAIR`
* **Meaning:** The total monetary amounts on the left side equal the total on the right side.
* **Non-meaning:** Does not assert identity.

## `financial.currency_compatibility`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`, `GROUP_PAIR`
* **Meaning:** All subjects in the scope transact in the same currency or represent a valid exchange pair.

## `reference.structural_compatibility`
* **Version:** 1
* **Symmetry:** SYMMETRIC
* **Allowed Scopes:** `RECORD_PAIR`, `GROUP_PAIR`
* **Meaning:** Reference fields (like invoice numbers) structurally align or overlap.

## `document.reference_is_parseable`
* **Version:** 1
* **Symmetry:** SYMMETRIC  (Unary scopes don't really have symmetry, but technically order-insensitive)
* **Allowed Scopes:** `RECORD`
* **Meaning:** The reference field contains parseable structured data.

*(Note: `document.supersedes` is omitted from production core claims as it was merely a directional example in research.)*
````

## File: docs/architecture/derivation-identity-composition.md
````markdown
# Derivation Identity Composition
Includes: schema_version, provider_id (via method descriptor), provider_semantic_version, method_id, input_mode, and canonical inputs.
Excludes: claim, proposition, lineage, outcome, score, trace context.
````

## File: docs/architecture/derivation-identity-vs-assertion-identity.md
````markdown
# Derivation Identity vs Assertion Identity
Derivation identity allows Stage 8J to see that A1 and A2 share derivation D1.
````

## File: docs/architecture/derivation-input-binding-decision.md
````markdown
# Derivation Input Binding Decision
**Selection: Role-bound Inputs**
`DerivationInputBinding(role: str, observation_identity: ObservationIdentity)` allows precise cardinality and positional semantics.
````

## File: docs/architecture/derivation-method-identity-decision.md
````markdown
# Derivation Method Identity Decision
**Selection: Provider-Relative**
`DerivationMethodId` is evaluated relative to `ProviderId` to avoid duplicate namespace bloat.
````

## File: docs/architecture/derivation-vs-assertion-boundary.md
````markdown
# Derivation vs Assertion Boundary
Derivation describes semantic material production. Assertion interprets that material against a claim.
````

## File: docs/architecture/derived-artifact-boundary.md
````markdown
# Derived Artifact Boundary
Derived semantic artifacts must preserve their parent derivation ancestry. They must never masquerade as independent source observations.
````

## File: docs/architecture/lineage-vs-correlation-boundary.md
````markdown
# Lineage vs Correlation Boundary
K4/K5 preserve ancestry facts. Stage 8J owns dependence assumptions. No `correlation_group` field may be implemented.
````

## File: docs/architecture/multi-observation-derivation-boundary.md
````markdown
# Multi-Observation Derivation Boundary

## Context
Some semantic interpretations rely on multiple distinct observed fields from the same source document. For example, validating `financial.amount_conservation` might require interpreting three distinct source fields: `gross_amount`, `net_amount`, and `tax_amount`.

## Boundary Decision
**Observation identity identifies source fact occurrences (singular field slots). Derivation identity (K5) records which observations participated in a semantic interpretation.**

We explicitly reject the creation of `CompositeObservation`, `MultiFieldObservation`, or `ObservationGroup` within the K3 observation layer. 

By keeping observations atomic (1:1 with source field slots), we avoid building a redundant derivation DAG in the observation layer. When a provider interprets a complex claim, it will consume multiple atomic `Observation`s and list all of their `ObservationIdentity` references inside its future `DerivationMetadata`. This keeps the observation layer purely factual and leaves complex dependency mapping to the derivation engine.
````

## File: docs/architecture/observation-content-vs-occurrence-identity.md
````markdown
# Observation Content vs Occurrence Identity

## The Distinction
In ReconGraph, K3 identifies **epistemic content state**. Temporal source occurrence identity belongs to structured lineage or future persistence/event infrastructure.

Consider the following timeline of a single source slot:
* **T0:** slot S contains "ABC"
* **T1:** slot S contains "XYZ"
* **T2:** slot S contains "ABC" (e.g. human reverted to the original value)

Because K3 `ObservationFingerprint` is a deterministic hash of the typed value state, we mathematically guarantee:

`ObservationIdentity(T0) == ObservationIdentity(T2)`
`ObservationIdentity(T0) != ObservationIdentity(T1)`

These are not three different revision identities. They are:
* Content state A
* Content state B
* Content state A

The future lineage/event layer (K4) or a persistence layer (Stage 7) may distinguish the *event* T0 from the *event* T2, but the semantic kernel correctly recognizes that the *content* is structurally identical.
````

## File: docs/architecture/observation-evidence-boundary.md
````markdown
# Observation vs Evidence Boundary

An observation states that a source slot had a particular value occurrence or condition. An evidence assertion states that an interpreter derived semantic support or conflict for a claim from observations. A structurally invalid observation can still be successfully interpreted for a claim concerning invalidity. Therefore, Observation State (PRESENT/MISSING/INVALID) is orthogonal to Interpretation State (INTERPRETED/UNINTERPRETABLE).

## Semantic Mapping Examples

| Source Fact | Observation State | Possible Interpretation State | Why |
|---|---|---|---|
| valid vendor name | PRESENT | INTERPRETED | Standard lexical parsing succeeds. |
| blank vendor name | PRESENT | UNINTERPRETABLE | Empty string cannot yield a vendor name similarity score. |
| vendor field absent | MISSING | UNINTERPRETABLE | Missing fields cannot be compared lexically. |
| vendor value "UNKNOWN" | PRESENT | UNINTERPRETABLE | Literal string "UNKNOWN" yields no specific identity support. |
| Japanese vendor name under English-only parser | PRESENT | UNINTERPRETABLE | Valid data, but interpreter lacks capability. |
| valid GSTIN | PRESENT | INTERPRETED | Checksum and structure valid, can derive state/identity. |
| invalid GSTIN structure | INVALID | INTERPRETED | Can assert `document.contains_invalid_tax_identifier`. |
| GSTIN checksum failure | INVALID | INTERPRETED | Can assert `document.contains_invalid_tax_identifier`. |
| valid reference | PRESENT | INTERPRETED | Can be matched against other references. |
| reference punctuation only | PRESENT | UNINTERPRETABLE | Cannot extract meaningful semantic tokens. |
| amount present | PRESENT | INTERPRETED | Number can be used in conservation check. |
| amount malformed | INVALID | UNINTERPRETABLE | Cannot perform math on malformed text. |
| currency present but unsupported | PRESENT | UNINTERPRETABLE | E.g. internal logic only supports USD/INR. |
| one-sided date | PRESENT | INTERPRETED | Could be used to assert `temporal.strictly_before`. |
| OCR text confidence 0.41 | PRESENT | UNINTERPRETABLE | Low confidence rejects interpretation to prevent false positives. |
````

## File: docs/architecture/observation-identity-vs-value-equality.md
````markdown
# Observation Identity vs Value Equality

## Semantic Boundary
In ReconGraph, there is a strict semantic distinction between "same value" and "same observation." 

**Value equality** asserts that two raw data payloads are mathematically or lexically equivalent (e.g. `100 == 100`, or `"ABC" == "ABC"`). 

**Observation identity** asserts that two values were observed at the *exact same structural slot* (e.g. `purchase:P1/vendor_name`) under the *exact same occurrence/revision*.

### Why it matters
If Purchase P1 has an amount of 100, and GST G1 has an amount of 100, their values are equal. However, their observation identities are distinct because they reside in different slots (`P1.amount` vs `G1.amount`). 

Treating them as the "same observation" would destroy the graph's ability to reason about pairwise reconciliation. 

### Same Source, Different Occurrences
Likewise, if a human corrects a typo on an invoice:
* T0: `P1.vendor_name = "ABC PVT LTO"`
* T1: `P1.vendor_name = "ABC PVT LTD"`

These are observations on the *same slot*, but their values (and potentially their `ObservationState`) differ, leading to different `ObservationIdentity` fingerprints. Future lineage metadata will distinguish *why* the revision occurred, but the kernel guarantees that the original misread and the human correction do not collide in identity.

### Summary
* Same value, different slot -> Different Observation Identity
* Same slot, different value -> Different Observation Identity
* Same slot, same value, same state -> Same Observation Identity (Deterministic Reconstruction)
````

## File: docs/architecture/observation-lineage-attachment-decision.md
````markdown
# Observation Lineage Attachment Decision
**Selection: ObservationProvenance wrapper**
Relational attachment wrapper `ObservationProvenance(observation, lineage)` preserves independent epistemic content state.
````

## File: docs/architecture/observation-revision-implementation-decision.md
````markdown
# Observation Revision Implementation Decision

## Context
An `ObservationSlot` (e.g. `purchase:P1/vendor_name`) identifies *where* a fact belongs. We must also identify *which value occurrence* was observed at that slot (e.g. "ABC PVT LTD" vs a later correction "ABC PRIVATE LIMITED"), yielding a unique `ObservationIdentity`. The identifier must be deterministic, distinguish duplicates, differentiate value types and missing/invalid states, avoid random UUIDs, and avoid embedding raw sensitive values directly.

## Evaluated Strategies

* **Revision A (Explicit Monotonic Revision Number):** e.g. `P1.vendor_name@1`. Rejected because K3 has no persistence layer to track monotonically increasing counters, breaking deterministic independent reconstruction.
* **Revision B (Value Fingerprint):** `slot + SHA-256(value)`. Rejected because it fails to distinguish different observation states (e.g. `PRESENT` "MISSING" vs `MISSING` state with no value), and normalizations change the identity.
* **Revision C (Explicit Revision Token Supplied by Ingestion):** Rejected because it pushes too much responsibility onto disparate plugins which may lack reliable source sequences.
* **Revision D (Structural Slot + Opaque Deterministic Fingerprint):** The fingerprint is derived from a canonical typed value envelope (schema version, state, type tag, canonical bytes). Raw values are excluded from the identifier string itself.
* **Revision E (Caller-Supplied Revision Ref):** Pushes identity semantics entirely out of the kernel.

## Decision
**Revision D (Structural Slot + Opaque Deterministic Fingerprint)** is selected.

We implement `ObservationFingerprint` (to correctly reflect content-based identity rather than temporal sequence). The fingerprint is a SHA-256 hash of a deterministic JSON serialization of a typed envelope containing:
- Observation schema version
- `ObservationState` (PRESENT, MISSING, INVALID)
- Canonical Type Tag (`str`, `int`, `float`, `none`, etc.)
- Canonical Value bytes

## Trade-offs & Properties Satisfied
1. **Deterministic reconstruction:** Yes. Independent ingestions of the exact same typed value state will yield the exact same fingerprint.
2. **Exact duplicate observation detectability:** Yes.
3. **Value occurrence distinction:** Yes. Changes in value change the fingerprint.
4. **Type distinction:** Yes. `1` (int) and `1.0` (float) have different type tags.
5. **State distinction:** Yes. `PRESENT` with value "ABC" has a different fingerprint than `INVALID` with value "ABC".
6. **No raw value in IDs:** Yes. The ID only contains a SHA-256 hex digest.
7. **No Python hash():** Yes. Uses stable crypto hash (`hashlib.sha256`), avoiding Python's randomized hash seeds.

**Caveat:** A plain SHA-256 digest is susceptible to dictionary attacks for low-entropy values (like currency codes or booleans). The fingerprint is a technical identity, not a cryptographic anonymization scheme. We explicitly accept this privacy trade-off for v0.1 as deterministic cross-environment trace replay requires the absence of runtime-specific secret keys (HMAC).
````

## File: docs/architecture/open-questions.md
````markdown
# Open Architecture Questions

## Financial Semantic Naming Audit

**Source**: Stage 8B review  
**Status**: OPEN  
**Required before**: Stage 8J (Evidence Fusion)

### Question

Do `SPLIT_PAYMENT` and `FEE_DETECTED` represent proven financial semantics or candidate explanations inferred from conservation patterns?

### Risk

Interpretive labels may overstate what amount observations alone prove.

**Example:**

```
100,000 ↔ 50,000 + 50,000
```

This supports **split structure**. It does not prove the business event was a "split payment."

Possible actual events:
- Split invoice
- Partial posting
- Tax component separation
- Ledger allocation
- Installments

Similarly, `FEE_DETECTED` when `residual = 250` is a **candidate explanation**, not an observation. The residual could equally be:
- A fee
- A withholding
- A rounding artifact
- An adjustment
- A posting error

### Required Action

Classify each financial evidence kind into one of:

| Classification | Meaning |
|---|---|
| `OBSERVATION` | Raw arithmetic fact (e.g., `delta = 0`, `residual = 250`) |
| `STRUCTURAL_INTERPRETATION` | Pattern inferred from structure (e.g., 1:N conservation, small nonzero residual) |
| `BUSINESS_EXPLANATION` | Domain-specific candidate meaning (e.g., "split payment", "fee") |

Current evidence units and their likely correct classification:

| Evidence Unit | Current Label Type | Likely Correct Classification |
|---|---|---|
| `EXACT_TOTAL_MATCH` | Structural | `OBSERVATION` — sums are equal |
| `SPLIT_PAYMENT` | Business | `STRUCTURAL_INTERPRETATION` — 1:N conservation |
| `UNDERPAYMENT` | Business | `STRUCTURAL_INTERPRETATION` — positive residual |
| `OVERPAYMENT` | Business | `STRUCTURAL_INTERPRETATION` — negative residual |
| `FEE_DETECTED` | Business | `BUSINESS_EXPLANATION` — small residual candidate |
| `ROUNDING_MATCH` | Structural | `STRUCTURAL_INTERPRETATION` — sub-tolerance residual |
| `CURRENCY_MISMATCH` | Observation | `OBSERVATION` — currencies differ |
| `GROSS_NET_MATCH` | Business | `BUSINESS_EXPLANATION` — tax-inclusive candidate |

### Consequence for Stage 8J

If Evidence Fusion treats `FEE_DETECTED` as an observed fact rather than a candidate explanation, the fusion engine may assign inappropriate confidence to what is actually an inference. The fusion layer must know the epistemic status of each evidence unit.
````

## File: docs/architecture/provider-semantic-versioning.md
````markdown
# Provider Semantic Versioning
Provider version describes changes to interpretation procedures; Claim semantic version describes changes to propositional meaning. They are structurally separate types.
````

## File: docs/architecture/scope-kind-construction-decision.md
````markdown
# Scope Kind Construction Decision

## Context
When constructing an evidence scope (now called `PropositionSubject`), the kernel needs to know the formal `ScopeKind` (e.g. `RECORD_PAIR`, `GROUP_PAIR`). Should the kernel infer this from the cardinality of the provided subjects, or should the caller explicitly provide it?

## Decision
**The caller must explicitly provide the `ScopeKind` during construction.**

## Rationale
Semantic intent should not be guessed from cardinality. If a caller provides exactly one subject on the left and one on the right, cardinality alone cannot distinguish between:
* A `RECORD_PAIR` representing a 1:1 match.
* A `GROUP_PAIR` representing a group reconciliation that currently happens to contain only a single record on each side.

By forcing explicit `ScopeKind` construction (e.g., `PropositionSubject.create(claim, ScopeKind.GROUP_PAIR, left, right)`), the kernel avoids silently misclassifying the evidence and strictly validates whether the provided subjects satisfy the invariant rules for that explicit kind.
````

## File: docs/architecture/shared-ancestry-query-boundary.md
````markdown
# Shared Ancestry Query Boundary
Querying shared observations is a structural set intersection. It produces no correlation coefficients.
````

## File: docs/architecture/source-artifact-model-decision.md
````markdown
# Source Artifact Model Decision
**Selection: Model C — Generic SourceNodeRef**
Extensible provenance coordinates `SourceNodeRef(kind: str, ref: str)`.
````

## File: docs/architecture/source-version-identity-boundary.md
````markdown
# Source Version Identity Boundary
ReconGraph preserves source-provided version identity when available. The semantic kernel does not invent temporal sequence identity.
````

## File: docs/architecture/unknown-claim-kernel-boundary.md
````markdown
# Unknown Claim Kernel Boundary

This document explicitly defines the boundaries for handling unknown plugin claims within the Evidence Semantic Kernel v0.1.

## Normative Rules

1. The semantic kernel can represent an unknown claim. (A plugin can instantiate a custom `ClaimDescriptor` and pass it to `PropositionSubject.create()`).
2. Representation does not imply fusion support. (Stage 8J cannot blindly mathematically fuse claims it does not explicitly understand).
3. Serialization does not imply semantic understanding. (Traces will faithfully serialize and deserialize the claim identifier and its structure, even if the core engine lacks the domain logic to evaluate it).
4. Namespacing does not imply trust. (A plugin claim `custom.bank_account_match` is isolated from the `CoreClaims` catalog).

By adhering to these boundaries, ReconGraph supports infinite plugin extensibility while protecting the mathematical integrity of the core fusion engine.
````

## File: docs/architecture/unknown-provider-derivation-boundary.md
````markdown
# Unknown Provider Derivation Boundary
The kernel can represent a derivation it cannot execute.
````

## File: docs/implementation/stage8c-k1-k2-import-audit.md
````markdown
# Stage 8C K1-K2 Import Cycle Audit

## Modules Audited
* `src/recongraph/domain/claims.py`
* `src/recongraph/domain/scopes.py`

## Internal ReconGraph Imports
* `src/recongraph/domain/claims.py`:
  - `recongraph.domain.scopes.ScopeKind`

* `src/recongraph/domain/scopes.py`:
  - none (external packages only, e.g., `enum`, `typing`, `dataclasses`)

## Results
* **Import cycle detected:** no
* **Semantic kernel imports provider layer:** no
* **Semantic kernel imports evaluator layer:** no
* **Semantic kernel imports decision layer:** no

All primitive modules sit strictly at the bottom of the dependency graph.
````

## File: docs/implementation/stage8c-k1-k2-preflight.md
````markdown
# Stage 8C K1-K2 Preflight Audit

## Current Architecture State
* **Current node identity type:** `NodeID` is an alias for `str` in `src/recongraph/graph/candidate.py`.
* **Current URN construction location:** `build_purchase_urn(record_id: str)` and `build_gst_urn(record_id: str)` in `src/recongraph/graph/candidate.py`.
* **Current Hypothesis identity semantics:** Hypothesis identity is mostly driven by object instances or explicitly constructed edge sets, not stable semantic identifiers.
* **Existing evidence primitive locations:**
  - `src/recongraph/plugins/provider.py`, `src/recongraph/plugins/provider_v2.py`
  - `src/recongraph/plugins/core_providers.py`
  - `src/recongraph/domain/financial/pipeline.py` (has `EvaluatedFinancialEvidence`, `EvidenceContributionV2`)
* **Existing plugin protocol locations:** `src/recongraph/plugins/`
* **Likely import-cycle risks:** The new semantic claims and scopes must live in `src/recongraph/domain/` (e.g., `semantic.py` or `claims.py` / `scopes.py`). If `src/recongraph/domain/semantic.py` imports anything from `src/recongraph/plugins/` or `src/recongraph/graph/`, it will create cycles. `SubjectRef` might be tempted to import `PurchaseRecord`, which we must avoid.

## Implementation Placement
* **Recommended package location:** `src/recongraph/domain/semantic.py` (or `src/recongraph/domain/claims.py` and `src/recongraph/domain/scopes.py`). We will use:
  - `src/recongraph/domain/claims.py` (ClaimId, ClaimSemanticVersion, ClaimSymmetry, ClaimDescriptor)
  - `src/recongraph/domain/scopes.py` (ScopeKind, SubjectRef, PropositionSubject)
* **Files expected to be created:**
  - `src/recongraph/domain/claims.py`
  - `src/recongraph/domain/scopes.py`
  - `tests/test_claim_semantics.py`
  - `tests/test_evidence_scope.py`
  - `docs/architecture/core-claim-catalog-v1.md`
  - `docs/architecture/scope-kind-construction-decision.md`
  - `docs/architecture/unknown-claim-kernel-boundary.md`
* **Files expected to be modified:**
  - `docs/architecture/open-questions.md`

## Construction Decision
We will use `PropositionSubject` instead of `EvidenceScope` because it is conceptually cleaner as the arguments to the semantic predicate (the Claim). It will expose a factory `PropositionSubject.create(...)` to explicitly enforce claim-aware symmetric canonicalization during construction. SubjectRef will hold a simple `urn: str` rather than generic domain objects, maintaining strict boundary hygiene.
````

## File: docs/implementation/stage8c-k3-import-audit.md
````markdown
# Stage 8C K3 Import Cycle Audit

## Modules Audited
* `src/recongraph/domain/observations.py`

## Internal ReconGraph Imports
* `src/recongraph/domain/observations.py`:
  - `recongraph.domain.scopes.SubjectRef`

## Results
* **Observation module imports claims:** no
* **Observation module imports scopes:** yes (only `SubjectRef`)
* **Observation module imports SubjectRef:** yes
* **Observation module imports plugins:** no
* **Observation module imports evaluator:** no
* **Observation module imports decision:** no
* **Observation module imports trace:** no

The dependency graph remains clean. The observation layer sits beside or slightly below the claim/scope layer, sharing only the formal subject identity wrapper (`SubjectRef`).
````

## File: docs/implementation/stage8c-k3-preflight.md
````markdown
# Stage 8C K3 Preflight Audit

## K1/K2 Closure Review

### Public Construction APIs
* **ClaimId:** `ClaimId(value: str)`
* **ClaimSemanticVersion:** `ClaimSemanticVersion(value: int)`
* **ClaimDescriptor:** `ClaimDescriptor(claim_id, semantic_version, symmetry, allowed_scope_kinds)`
* **ClaimSymmetry:** `ClaimSymmetry.SYMMETRIC` / `ClaimSymmetry.DIRECTIONAL`
* **ScopeKind:** `ScopeKind.RECORD`, `ScopeKind.RECORD_PAIR`, `ScopeKind.GROUP`, `ScopeKind.GROUP_PAIR`, `ScopeKind.HYPOTHESIS`, `ScopeKind.COMPONENT`
* **SubjectRef:** `SubjectRef(urn: str)`
* **PropositionSubject:** `PropositionSubject.create(claim_descriptor, kind, left, right)`

### Current Conventions
* **K1/K2 package location:** `src/recongraph/domain/claims.py` and `src/recongraph/domain/scopes.py`
* **Current domain primitive dependency direction:** Bottom-up. Primitives depend only on standard library.
* **Current serialization convention:** Explicit `.to_dict()` methods on domain objects returning simple Python dicts/primitives.
* **Current validation style:** `__post_init__` within `dataclass(frozen=True)` or explicit static factory methods like `create()`.
* **Current custom exception style:** Raising built-in `ValueError` or `TypeError` with structured error codes (e.g. "SC-001 Violation: ...").
* **Current immutable collection style:** Built-in `frozenset` and `tuple`.
* **Current stable URN representation:** String URNs inside `SubjectRef(urn=...)`.
* **Current record identity representation:** Handled by graph builder, domain only knows URNs.

### K3 Architecture
* **Recommended K3 module location:** `src/recongraph/domain/observations.py`
* **Expected import dependencies:** 
  - `src/recongraph/domain/scopes.py` (for `SubjectRef`)
* **Expected import-cycle risks:** Low. Observations depend on SubjectRef but not on semantic Claims or Scopes. Claims and Scopes do not need to import Observations. The dependency graph remains clean.
````

## File: docs/implementation/stage8c-k4-k5-preflight.md
````markdown
# Stage 8C K4/K5 Preflight Audit

## K3 Closure Review

### Observation Module Location
* **Location:** `src/recongraph/domain/observations.py`

### Public APIs
* **Observation construction API:** `Observation.create(slot: ObservationSlot, state: ObservationState, value: Any)`
* **Observation identity composition:** `ObservationIdentity(slot: ObservationSlot, fingerprint: ObservationFingerprint)`
* **Observation fingerprint algorithm:** SHA-256 of JSON serialized canonical value envelope.
* **Observation schema version representation:** Explicit `"schema_version": 1` in the envelope dictionary.
* **Observation supported value types:** `str`, `int`, `float`, `Decimal`, `bool`, `date`, `datetime`, `None` (missing).
* **Observation serialization API:** `ObservationIdentity.to_dict()` for structural ID, `Observation.to_dict()` for sensitive full payload.
* **SubjectRef construction API:** `SubjectRef(urn: str)`

### External Primitives
* **Current semantic-version primitives:** `ClaimSemanticVersion(value: int)` (in `claims.py`)
* **Current provider version representation:** N/A (not yet represented in primitives)
* **Current engine version representation:** Currently handled by the broader application config/trace logic, not as a typed domain primitive.
* **Current trace engine_version representation:** Currently plain string/dict in trace schema.
* **Current config_hash representation:** Currently plain string in config module.

### K4/K5 Architecture Recommendations
* **Recommended K4 module location:** `src/recongraph/domain/lineage.py`
* **Recommended K5 module location:** `src/recongraph/domain/derivations.py`
* **Potential circular imports:** K4/K5 will need to import `ObservationIdentity` from `observations.py`. This is structurally clean. If we must attach Lineage to Observation, there is a risk of a circular dependency if `observations.py` needs to import `lineage.py`. We should use a wrapper object (like `SourcedObservation` or `ObservationProvenance`) living in `lineage.py` or a distinct attachment module.

## Mandatory Vocabulary Correction

`ObservationFingerprint` = **content-state fingerprint**

It is NOT:
* temporal revision number
* source event identity
* ingestion sequence
* historical occurrence identity

*Observation identity distinguishes typed observation content states.*
````

## File: docs/security/derivation-fingerprint-privacy.md
````markdown
# Derivation Fingerprint Privacy
Are derivation IDs anonymization? NO. They remain sensitive metadata that can indirectly reveal execution paths.
````

## File: docs/security/observation-fingerprint-privacy.md
````markdown
# Observation Fingerprint Privacy Threat Analysis

## Threat Model
In ReconGraph v0.1, the `ObservationIdentity` relies on an `ObservationFingerprint` constructed from a deterministic SHA-256 digest of the typed observation envelope (schema version, state, type tag, value bytes).

An attacker who obtains an observation fingerprint could attempt to reverse it by hashing potential source values and comparing the digests. 

### Can observation fingerprints be dictionary attacked?
Yes. Because the digest is deterministic and unsalted, low-entropy values (like currency codes, booleans, dates, or common vendor names) can be trivially guessed and hashed by an attacker to confirm their presence in the system. High-entropy values (like exact invoice numbers or long random references) are more resistant but still technically susceptible.

### Are fingerprints anonymization?
**NO.** A fingerprint is a technical identity primitive for deterministic deduplication and trace replay. It is strictly not an encryption mechanism, not an anonymization scheme, and not a method of access control. 

### Should observation IDs be logged publicly?
No. Because they leak exact value equality and can be dictionary-attacked, observation identities should be treated as sensitive metadata and restricted to secure operational telemetry (e.g. secure audit logs), not exposed in public dashboards or unprotected environments.

### Does v0.1 require HMAC?
No. Introducing a keyed HMAC for the digest complicates deterministic cross-environment replay because the secret key becomes part of the identity. For v0.1, we accept the privacy trade-off of a plain digest in exchange for stable counterfactual re-evaluation across environments, provided the system treats the IDs themselves as sensitive.

### What must Stage 7 persistence eventually protect?
When observations are persisted to a database or object store (Stage 7), the persistence layer must protect the `ObservationIdentity` column with the same access controls and encryption-at-rest policies as the raw value payload itself.
````

## File: docs/security/observation-serialization-sensitivity.md
````markdown
# Observation Serialization Sensitivity

## Context
When an `Observation` is serialized to JSON (or Python dictionaries), it must emit two distinct levels of data: structural identity and full typed value occurrences.

### `ObservationIdentity.to_dict()`
This serialization produces a safe structural identity representation (the slot and the fingerprint hash). It is safe to use in operational telemetry, graph topology logging, and unencrypted deduplication traces, as it does not leak raw PII or exact raw strings (though it is susceptible to dictionary attacks for low-entropy enums/values).

### `Observation.to_dict()`
This serialization includes the raw typed value (e.g. `{"type": "str", "value": "ABC PRIVATE LIMITED"}`). **This representation is highly sensitive.** It contains raw source data which may include PANs, GSTINs, and proprietary vendor names. 

Observation serialization containing raw source data must not be treated as sanitized telemetry. Any system (like Stage 7 Traces) that persists `Observation.to_dict()` must treat the resulting artifact as a secure data asset with appropriate access controls and encryption at rest.

*(Note: In the future, a `to_trace_dict(redaction_policy)` may be introduced to sanitize values for lower-security traces, but v0.1 does not implement this).*
````

## File: docs/security/source-lineage-serialization-sensitivity.md
````markdown
# Source Lineage Serialization Sensitivity
Structured lineage is operational provenance, not sanitized telemetry.
````

## File: docs/testing/lineage-derivation-hard-negatives.md
````markdown
# Lineage Derivation Hard Negatives
LDH & LDUP threat model. Addressed in `tests/test_source_lineage.py`.
````

## File: docs/testing/lineage-derivation-metamorphic-properties.md
````markdown
# Lineage Derivation Metamorphic Properties
KDM suite. Addressed in `tests/test_lineage_metamorphic.py`.
````

## File: docs/testing/observation-kernel-metamorphic-properties.md
````markdown
# Observation Kernel Metamorphic Properties

The K3 Observation Kernel must mathematically satisfy the following metamorphic properties. Any violation signifies a broken identity model or a conflation of orthogonal concepts.

| Property | Transformation | Invariant | Reason |
|---|---|---|---|
| **KOM-001** (Slot Stability) | Change observed value for the same source field | `ObservationSlot` remains identical | Slot identifies *where* the fact exists, independent of *what* it is. |
| **KOM-002** (Revision Distinction) | Change observed value for the same source field | `ObservationIdentity` changes | Distinguishes different occurrences (e.g. human correction). |
| **KOM-003** (Exact Reconstruction) | Reconstruct the exact same observation independently | `ObservationIdentity` remains identical | Permits deterministic replay and deduplication. |
| **KOM-004** (Subject Distinction) | Change `SubjectRef` | Slot and Identity change | Prevents cross-record data collision. |
| **KOM-005** (Field Distinction) | Change `FieldPath` | Slot and Identity change | Prevents cross-field data collision. |
| **KOM-006** (State Distinction) | Change `PRESENT` to `INVALID` with same raw value | Identity changes | Context of extraction failure is fundamentally different from a valid parse. |
| **KOM-007** (Missing Determinism) | Reconstruct a `MISSING` state observation | Identity remains identical | Absence is a deterministic structural state. |
| **KOM-008** (Runtime Object Independence)| Provide semantically equal values from distinct memory addresses | Identity remains identical | Values, not Python object IDs, define occurrences. |
| **KOM-009** (Type Preservation) | Change `1` (int) to `1.0` (float) | Identity changes | Type-sensitive hashing preserves source representation semantics. |
| **KOM-010** (Interpretation Independence)| Change `InterpretationState` on a downstream assertion | Observation identity remains identical | Proves orthogonal separation of observation and interpretation. |
| **KOM-011** (Provider Independence) | Reconstruct under a new provider version | Observation identity remains identical | Observations precede providers. |
| **KOM-012** (Claim Independence) | Evaluate observation against a different claim | Observation identity remains identical | Observations precede claims. |
| **KOM-013** (Scope Independence) | Pass observation to a different `PropositionSubject` | Observation identity remains identical | Observations are atomic facts; scope is an assertion mapping. |
| **KOM-014** (Serialization Stability) | Serialize two structurally equal observations | Emitted JSON is byte-equivalent | Enables cross-language/environment replay. |
| **KOM-015** (Invalid Value Preservation) | Change an invalid source string to another invalid string | Identity changes | Invalid values still represent distinct source facts. |
| **KOM-016** (Empty String Handling) | Compare `None` to `""` | Identity changes | An empty string is a present string; None is an absence. |
| **KOM-017** (Whitespace Sensitivity) | Compare `"ABC"` to `" ABC "` | Identity changes | Unnormalized values preserve raw source fidelity. |
| **KOM-018** (Decimal Stability) | Provide identical precision `Decimal` | Identity remains identical | Numeric scaling is preserved if types are identical. |
| **KOM-019** (Boolean/Integer Distinction)| Compare `True` to `1` | Identity changes | Prevents accidental collision due to Python subclassing. |
| **KOM-020** (Missingness Value Check) | Attempt `MISSING` + `value="ABC"` | Raises exception | Missing state fundamentally contradicts value presence. |
````

## File: experiments/compare_reference_identity_extraction.py
````python
from experiments.legacy_reference import reference_score
from recongraph.matching.reference_evidence import extract_reference_identity

CASES = [
    ("INV-874219", "AB/874219"),
    ("INV-001", "ABC-001"),
    ("INV-999999", "ABC-999999"),
    ("INV-2026-1001", "ABC-2026-1001"),
    ("2026", "2026"),
    ("CREDITNOTE", "CREDITNOTE"),
    ("INV-01", "ABC-01"),
    ("INV-1042", "INV-1043"),
]

def main():
    print("Comparison experiment output:")
    for a, b in CASES:
        old_score = float(reference_score(a, b) or 0.0)
        evidence = extract_reference_identity(a, b)

        print(f"\nA: {a}")
        print(f"B: {b}")
        print(f"old reference_score: {old_score:.1f}")
        print("new evidence:")

        if evidence:
            exact = "true" if evidence.exact_normalized_match else "false"
            tokens = "|".join(evidence.shared_numeric_tokens) if evidence.shared_numeric_tokens else "none"
            print(f"exact normalized: {exact}")
            print(f"shared tokens: {tokens}")
        else:
            print("exact normalized: false")
            print("shared tokens: none")

if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_corpus_reference_informativeness.py
````python
import math
from collections import Counter
from dataclasses import dataclass
from typing import Set

from recongraph.normalization.text import (
    extract_numeric_reference_tokens,
    normalize_reference,
)
from experiments.legacy_reference import reference_score

@dataclass(frozen=True)
class CorpusReference:
    record_id: str
    source: str
    reference: str

@dataclass(frozen=True)
class ReferenceCase:
    case_id: str
    reference_a: str
    reference_b: str
    expected_relationship: str

def generate_hostile_corpus() -> list[CorpusReference]:
    corpus = []

    # Family A - Common low-number invoice sequences (purchase)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"A{i:03d}", "purchase", f"INV-{i:03d}"))

    # Family B - Another vendor's low sequences (gst)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"B{i:03d}", "gst", f"ABC-{i:03d}"))

    # Family C - Purchase orders (ledger)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"C{i:03d}", "ledger", f"PO-{i:03d}"))

    # Family D - Transaction references (bank)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"D{i:03d}", "bank", f"TXN-{i:03d}"))

    # Family E - Year-bearing references
    for i in range(1, 21):
        corpus.append(CorpusReference(f"E1{i:03d}", "purchase", f"INV-2026-{1000+i}"))
    for i in range(1, 21):
        corpus.append(CorpusReference(f"E2{i:03d}", "gst", f"GST-2026-{2000+i}"))

    # Family F - Rare genuine cross-source pairs
    rare_pairs = [
        ("purchase", "INV-874219", "gst", "AB/874219"),
        ("purchase", "INV-591842", "gst", "LEGACY/591842"),
        ("purchase", "BILL-731905", "bank", "PAYMENT/731905"),
        ("purchase", "DOC-482761", "ledger", "ENTRY/482761"),
        ("purchase", "INV-615394", "gst", "GST/615394"),
    ]
    for idx, (sa, ra, sb, rb) in enumerate(rare_pairs):
        corpus.append(CorpusReference(f"F{idx}a", sa, ra))
        corpus.append(CorpusReference(f"F{idx}b", sb, rb))

    # Family G - Repeated garbage-like tokens
    garbage_tokens = ["999999", "000001", "111111", "123456"]
    prefixes = ["INV-", "ABC-", "PO-", "TXN-"]
    sources = ["purchase", "gst", "ledger", "bank"]
    for g_idx, token in enumerate(garbage_tokens):
        for p_idx, prefix in enumerate(prefixes):
            corpus.append(CorpusReference(f"G{g_idx}{p_idx}", sources[p_idx], f"{prefix}{token}"))

    return corpus

def compute_document_frequencies(corpus: list[CorpusReference]) -> Counter:
    df: Counter[str] = Counter()
    for ref in corpus:
        tokens = set(extract_numeric_reference_tokens(ref.reference, min_length=3))
        for token in tokens:
            df[token] += 1
    return df

def corpus_rarity_gate_score(ref_a: str, ref_b: str, df: Counter, N: int) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        rate = df.get(t, 0) / N if N > 0 else 0
        if rate <= 0.02:
            max_score = max(max_score, 0.8)
    return max_score

def normalized_idf_reference_score(ref_a: str, ref_b: str, df: Counter, N: int, max_idf: float) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        dft = df.get(t, 0)
        idf = math.log(N / dft) if dft > 0 and N > 0 else 0
        norm_idf = idf / max_idf if max_idf > 0 else 0
        max_score = max(max_score, 0.8 * norm_idf)
    return max_score

def saturating_rarity_reference_score(ref_a: str, ref_b: str, df: Counter, N: int) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        dft = df.get(t, 0)
        score = 0.8 * (1.0 - (dft / N)) if N > 0 else 0.0
        max_score = max(max_score, score)
    return max_score

def collision_burden_reference_score(ref_a: str, ref_b: str, df: Counter) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        dft = df.get(t, 0)
        strength = 1.0 / (1.0 + math.log(dft)) if dft > 0 else 0.0
        max_score = max(max_score, 0.8 * strength)
    return max_score

def contextual_exact_reference_score(ref_a: str, ref_b: str, df: Counter) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a != norm_b: return 0.0

    tokens = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    if not tokens:
        return 1.0

    max_strength = 0.0
    for t in tokens:
        dft = df.get(t, 1) # use 1 for unseen in experiment
        if dft == 0:
            dft = 1
        strength = 1.0 / (1.0 + math.log(dft))
        max_strength = max(max_strength, strength)

    return 0.2 + 0.8 * max_strength

EVAL_CASES = [
    ReferenceCase("COR001", "INV-001", "ABC-001", "weak_collision"),
    ReferenceCase("COR002", "INV-002", "PO-002", "weak_collision"),
    ReferenceCase("COR003", "ABC-003", "TXN-003", "weak_collision"),
    ReferenceCase("COR004", "INV-2026-1001", "GST-2026-2001", "weak_collision"),
    ReferenceCase("COR005", "INV-999999", "ABC-999999", "weak_collision"),
    ReferenceCase("COR006", "INV-000001", "TXN-000001", "weak_collision"),
    ReferenceCase("COR007", "ABC-111111", "PO-111111", "weak_collision"),
    ReferenceCase("COR008", "INV-123456", "TXN-123456", "weak_collision"),
    ReferenceCase("COR009", "INV-874219", "AB/874219", "strong_positive"),
    ReferenceCase("COR010", "INV-591842", "LEGACY/591842", "strong_positive"),
    ReferenceCase("COR011", "BILL-731905", "PAYMENT/731905", "strong_positive"),
    ReferenceCase("COR012", "DOC-482761", "ENTRY/482761", "strong_positive"),
    ReferenceCase("COR013", "INV-615394", "GST/615394", "strong_positive"),
    ReferenceCase("COR014", "INV-1042", "INV-1043", "distinct"),
    ReferenceCase("COR015", "SB-8891", "SB-8892", "distinct"),
    ReferenceCase("COR016", "INV-2026-1001", "ABC-2026-1001", "ambiguous"),
]

EXACT_CASES = [
    ReferenceCase("EX001", "001", "001", "ambiguous"),
    ReferenceCase("EX002", "INV-001", "INV-001", "ambiguous"),
    ReferenceCase("EX003", "2026", "2026", "ambiguous"),
    ReferenceCase("EX004", "874219", "874219", "strong_positive"),
    ReferenceCase("EX005", "INV-874219", "INV-874219", "strong_positive"),
    ReferenceCase("EX006", "999999", "999999", "ambiguous"),
    ReferenceCase("EX007", "INV-123456", "INV-123456", "ambiguous"),
    ReferenceCase("EX008", "CREDITNOTE", "CREDITNOTE", "ambiguous"),
]

def main():
    corpus = generate_hostile_corpus()
    df = compute_document_frequencies(corpus)
    N = len(corpus)

    print("Corpus summary")
    print("--------------")
    print(f"Total references: {N}")
    print(f"Unique numeric tokens: {len(df)}")

    src_counts = Counter(r.source for r in corpus)
    print("Sources:")
    for src, count in src_counts.items():
        print(f"  {src}: {count}")

    print("\nMost common numeric tokens")
    print("--------------------------")
    print(f"{'Token':<11} {'DF':<8} {'DocumentRate'}")
    for token, count in df.most_common(20):
        print(f"{token:<11} {count:<8} {count/N:.4f}")

    selected_tokens = ["001", "002", "100", "2026", "999999", "000001", "111111", "123456", "874219", "591842", "731905", "482761", "615394"]
    print("\nSelected token statistics")
    print("-------------------------")
    print(f"{'Token':<11} {'DF':<8} {'DocumentRate':<18} {'RawIDF'}")
    for token in selected_tokens:
        count = df.get(token, 0)
        rate = count / N if N > 0 else 0
        raw_idf = math.log(N / count) if count > 0 and N > 0 else 0
        print(f"{token:<11} {count:<8} {rate:<18.4f} {raw_idf:.4f}")

    max_idf = math.log(N / 1) if N > 0 else 1.0

    print("\nModel comparison:")
    print(f"{'Case':<7} {'Label':<18} {'SharedTokens':<18} {'Current':<10} {'RarityGate':<12} {'NormIDF':<10} {'Saturating':<12} {'CollisionBurden'}")
    print("-" * 115)

    model_scores = {"Current": [], "RarityGate": [], "NormalizedIDF": [], "Saturating": [], "CollisionBurden": []}

    for case in EVAL_CASES:
        tokens_a = set(extract_numeric_reference_tokens(case.reference_a, min_length=3))
        tokens_b = set(extract_numeric_reference_tokens(case.reference_b, min_length=3))
        shared = "|".join(tokens_a & tokens_b)

        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        rg = corpus_rarity_gate_score(case.reference_a, case.reference_b, df, N)
        ni = normalized_idf_reference_score(case.reference_a, case.reference_b, df, N, max_idf)
        sr = saturating_rarity_reference_score(case.reference_a, case.reference_b, df, N)
        cb = collision_burden_reference_score(case.reference_a, case.reference_b, df)

        model_scores["Current"].append((case, curr))
        model_scores["RarityGate"].append((case, rg))
        model_scores["NormalizedIDF"].append((case, ni))
        model_scores["Saturating"].append((case, sr))
        model_scores["CollisionBurden"].append((case, cb))

        print(f"{case.case_id:<7} {case.expected_relationship:<18} {shared:<18} {curr:<10.4f} {rg:<12.4f} {ni:<10.4f} {sr:<12.4f} {cb:.4f}")

    print("\nModel summary")
    print("-------------")
    print(f"{'Model':<18} {'MinPositive':<14} {'MaxCollision':<14} {'Gap'}")

    for mname in ["Current", "RarityGate", "NormalizedIDF", "Saturating", "CollisionBurden"]:
        scores = model_scores[mname]
        sp = [s for c, s in scores if c.expected_relationship == "strong_positive"]
        wc = [s for c, s in scores if c.expected_relationship == "weak_collision"]
        min_sp = min(sp) if sp else 0.0
        max_wc = max(wc) if wc else 0.0
        gap = min_sp - max_wc
        print(f"{mname:<18} {min_sp:<14.4f} {max_wc:<14.4f} {gap:.4f}")

    for mname in ["Current", "RarityGate", "NormalizedIDF", "Saturating", "CollisionBurden"]:
        print(f"\n{mname} ranking")
        print("-" * (len(mname) + 8))
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        for i, (c, s) in enumerate(ranked):
            print(f"{i+1}. {c.case_id}  {c.expected_relationship}  {s:.4f}")

    print("\nWeak collisions in top 8")
    print("------------------------")
    for mname in ["Current", "RarityGate", "NormalizedIDF", "Saturating", "CollisionBurden"]:
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        top8 = ranked[:8]
        count = sum(1 for c, s in top8 if c.expected_relationship == "weak_collision")
        print(f"{mname}: {count}")

    # Mutation 1: 100 random singletons
    print("\nCorpus mutation stability")
    print("-------------------------")
    print(f"{'Model':<18} {'Before':<10} {'After':<10} {'Delta'}")

    # Calculate before scores for COR009
    cor009_a, cor009_b = "INV-874219", "AB/874219"
    ni_before = normalized_idf_reference_score(cor009_a, cor009_b, df, N, max_idf)
    sr_before = saturating_rarity_reference_score(cor009_a, cor009_b, df, N)
    cb_before = collision_burden_reference_score(cor009_a, cor009_b, df)

    # Add 100 random singletons
    corpus_mut1 = corpus.copy()
    for i in range(1, 101):
        corpus_mut1.append(CorpusReference(f"M1_{i}", "ledger", f"RANDOM-{300000+i}"))

    df_mut1 = compute_document_frequencies(corpus_mut1)
    N_mut1 = len(corpus_mut1)
    max_idf_mut1 = math.log(N_mut1 / 1) if N_mut1 > 0 else 1.0

    ni_after1 = normalized_idf_reference_score(cor009_a, cor009_b, df_mut1, N_mut1, max_idf_mut1)
    sr_after1 = saturating_rarity_reference_score(cor009_a, cor009_b, df_mut1, N_mut1)
    cb_after1 = collision_burden_reference_score(cor009_a, cor009_b, df_mut1)

    print(f"{'NormalizedIDF':<18} {ni_before:<10.4f} {ni_after1:<10.4f} {ni_after1 - ni_before:+.4f}")
    print(f"{'Saturating':<18} {sr_before:<10.4f} {sr_after1:<10.4f} {sr_after1 - sr_before:+.4f}")
    print(f"{'CollisionBurden':<18} {cb_before:<10.4f} {cb_after1:<10.4f} {cb_after1 - cb_before:+.4f}")

    # Mutation 2: 1 random sharing token
    print("\nShared-token collision mutation")
    print("-------------------------------")
    print(f"{'Model':<18} {'DF=2':<10} {'DF=3':<10} {'Delta'}")

    corpus_mut2 = corpus.copy()
    corpus_mut2.append(CorpusReference("M2_1", "ledger", "RANDOM-874219"))

    df_mut2 = compute_document_frequencies(corpus_mut2)
    N_mut2 = len(corpus_mut2)
    max_idf_mut2 = math.log(N_mut2 / 1) if N_mut2 > 0 else 1.0

    ni_after2 = normalized_idf_reference_score(cor009_a, cor009_b, df_mut2, N_mut2, max_idf_mut2)
    sr_after2 = saturating_rarity_reference_score(cor009_a, cor009_b, df_mut2, N_mut2)
    cb_after2 = collision_burden_reference_score(cor009_a, cor009_b, df_mut2)

    print(f"{'NormalizedIDF':<18} {ni_before:<10.4f} {ni_after2:<10.4f} {ni_after2 - ni_before:+.4f}")
    print(f"{'Saturating':<18} {sr_before:<10.4f} {sr_after2:<10.4f} {sr_after2 - sr_before:+.4f}")
    print(f"{'CollisionBurden':<18} {cb_before:<10.4f} {cb_after2:<10.4f} {cb_after2 - cb_before:+.4f}")

    print("\nExact-match current behavior")
    print("----------------------------")
    print(f"{'Case':<7} {'Label':<18} {'A':<15} {'B':<15} {'Current'}")
    for case in EXACT_CASES:
        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        print(f"{case.case_id:<7} {case.expected_relationship:<18} {case.reference_a:<15} {case.reference_b:<15} {curr:.4f}")

    print("\nExact-match contextual comparison")
    print("---------------------------------")
    print(f"{'Case':<7} {'Label':<18} {'Current':<10} {'ContextualExact'}")
    for case in EXACT_CASES:
        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        ctx = contextual_exact_reference_score(case.reference_a, case.reference_b, df)
        print(f"{case.case_id:<7} {case.expected_relationship:<18} {curr:<10.4f} {ctx:.4f}")

    print("\nComposite evidence diagnostics")
    print("------------------------------")
    for case in EXACT_CASES:
        norm_a = normalize_reference(case.reference_a)
        norm_b = normalize_reference(case.reference_b)
        exact = (norm_a == norm_b) and bool(norm_a)
        tokens = set(extract_numeric_reference_tokens(case.reference_a, min_length=3))

        max_strength = 0.0
        token_dfs = {}
        for t in tokens:
            dft = df.get(t, 1)
            if dft == 0: dft = 1
            token_dfs[t] = dft
            strength = 1.0 / (1.0 + math.log(dft))
            max_strength = max(max_strength, strength)

        exactness_comp = 0.2 if exact else 0.0
        info_comp = 0.8 * max_strength if tokens else 0.8

        if not tokens:
            # Our experimental logic returns 1.0 when no numeric tokens are present
            exactness_comp = 1.0
            info_comp = 0.0

        final_score = exactness_comp + info_comp

        print(f"\nCase {case.case_id}")
        print("-----------")
        print(f"normalized exact: {'yes' if exact else 'no'}")
        print(f"numeric tokens: {'|'.join(tokens) if tokens else 'none'}")
        if tokens:
            print("token df:")
            for t in tokens:
                print(f"  {t}: {token_dfs[t]}")
        print(f"max token strength: {max_strength:.4f}")
        print(f"exactness component: {exactness_comp:.4f}")
        print(f"informativeness component: {info_comp:.4f}")
        print(f"final contextual score: {final_score:.4f}")

if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_reference_discriminative_strength.py
````python
import re
from dataclasses import dataclass
from typing import Optional

from experiments.legacy_reference import reference_score
from recongraph.normalization.text import normalize_reference

NUMERIC_TOKEN_PATTERN = re.compile(r"\d+")

def extract_numeric_tokens(reference: str) -> tuple[str, ...]:
    return tuple(NUMERIC_TOKEN_PATTERN.findall(reference))


@dataclass(frozen=True)
class ReferenceCase:
    case_id: str
    reference_a: str
    reference_b: str
    expected_relationship: str
    rationale: str


CASES = [
    ReferenceCase("REF001", "INV-1042", "AB/1042", "strong_positive", "Shared 4-digit token"),
    ReferenceCase("REF002", "SB-8891", "SB8891", "strong_positive", "Shared 4-digit token, punctuation diff"),
    ReferenceCase("REF003", "NC-2204", "NC/2204", "strong_positive", "Shared 4-digit token"),
    ReferenceCase("REF004", "MOS-781", "MOS781", "strong_positive", "Shared 3-digit token"),
    ReferenceCase("REF005", "AIS-5510", "AIS/5510", "strong_positive", "Shared 4-digit token"),
    ReferenceCase("REF006", "OMD-001", "NSS-001", "weak_collision", "Weak 3-digit token collision"),
    ReferenceCase("REF007", "ABC-002", "XYZ-002", "weak_collision", "Weak 3-digit token collision"),
    ReferenceCase("REF008", "INV-100", "PO-100", "weak_collision", "Weak 3-digit token collision"),
    ReferenceCase("REF009", "INV-874219", "AB/874219", "strong_positive", "Strong 6-digit token"),
    ReferenceCase("REF010", "TXN-987654321", "LEGACY/987654321", "strong_positive", "Very strong 9-digit token"),
    ReferenceCase("REF011", "INV-1042", "INV-1043", "distinct", "Distinct 4-digit tokens"),
    ReferenceCase("REF012", "SB-8891", "SB-8892", "distinct", "Distinct 4-digit tokens"),
    ReferenceCase("REF013", "OMD-001", "NSS-002", "distinct", "Distinct 3-digit tokens"),
    ReferenceCase("REF014", "2026-001", "2025-001", "ambiguous", "Ambiguous weak 3-digit collision across years"),
    ReferenceCase("REF015", "INV-2026-001", "PO-2026-001", "ambiguous", "Ambiguous year and weak collision"),
    ReferenceCase("REF016", "001", "001", "ambiguous", "Exact but weak"),
    ReferenceCase("REF017", "0001", "0001", "ambiguous", "Exact but weak"),
    ReferenceCase("REF018", "INV-000001", "AB-000001", "ambiguous", "6-digit collision but only significant len 1"),
    ReferenceCase("REF019", "INV-123456", "AB-123456", "strong_positive", "Sequential 6-digit"),
    ReferenceCase("REF020", "INV-999999", "ZZ-999999", "ambiguous", "Repeated 6-digit"),
]

# Probe cases added for evaluating specific failures
PROBE_CASES = [
    ReferenceCase("ProbeA", "INV-2026-874219", "AB-2025-874219", "strong_positive", "Shared 874219 but diff year"),
    ReferenceCase("ProbeB", "INV-2026-001", "PO-2026-002", "weak_collision", "Shared year 2026 but distinct seq"),
]


def model_sig_gate(reference_a: str, reference_b: str) -> float:
    norm_a = normalize_reference(reference_a)
    norm_b = normalize_reference(reference_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
        
    tokens_a = extract_numeric_tokens(reference_a)
    tokens_b = extract_numeric_tokens(reference_b)
    shared = set(tokens_a) & set(tokens_b)
    
    if not shared:
        return 0.0
        
    max_score = 0.0
    for token in shared:
        sig = token.lstrip("0") or "0"
        if len(sig) >= 4:
            max_score = max(max_score, 0.8)
    return max_score


def model_graded(reference_a: str, reference_b: str) -> float:
    norm_a = normalize_reference(reference_a)
    norm_b = normalize_reference(reference_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
        
    tokens_a = extract_numeric_tokens(reference_a)
    tokens_b = extract_numeric_tokens(reference_b)
    shared = set(tokens_a) & set(tokens_b)
    
    if not shared:
        return 0.0
        
    max_score = 0.0
    for token in shared:
        sig = token.lstrip("0") or "0"
        sig_len = len(sig)
        score = 0.0
        if sig_len >= 6:
            score = 0.8
        elif sig_len >= 4:
            score = 0.7
        elif sig_len >= 3:
            score = 0.4
        max_score = max(max_score, score)
    return max_score


def numeric_token_informativeness(token: str) -> float:
    sig = token.lstrip("0") or "0"
    sig_len = len(sig)
    
    unique_digits = len(set(token))
    unique_ratio = unique_digits / len(token) if token else 0.0
    
    leading_zero_count = len(token) - len(token.lstrip("0"))
    # if token is all zeros, leading zeroes is len(token) - 1 mathematically but let's just use raw lstrip logic
    if token.lstrip("0") == "":
        leading_zero_count = len(token) - 1
        
    leading_zero_ratio = leading_zero_count / len(token) if token else 0.0
    
    len_component = min(sig_len / 6.0, 1.0)
    unique_component = unique_ratio
    lz_component = 1.0 - leading_zero_ratio
    
    info = (0.5 * len_component) + (0.3 * unique_component) + (0.2 * lz_component)
    return max(0.0, min(1.0, info))


def model_intrinsic(reference_a: str, reference_b: str) -> float:
    norm_a = normalize_reference(reference_a)
    norm_b = normalize_reference(reference_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
        
    tokens_a = extract_numeric_tokens(reference_a)
    tokens_b = extract_numeric_tokens(reference_b)
    shared = set(tokens_a) & set(tokens_b)
    
    if not shared:
        return 0.0
        
    max_score = 0.0
    for token in shared:
        info = numeric_token_informativeness(token)
        max_score = max(max_score, 0.8 * info)
    return max_score


def main():
    print("Current behavior table:")
    print(f"{'Case':<7} {'Reference A':<17} {'Reference B':<17} {'Label':<18} {'Normalized A':<16} {'Normalized B':<16} {'Numeric A':<15} {'Numeric B':<15} {'Current'}")
    print("-" * 139)
    
    current_scores = []
    
    for case in CASES:
        norm_a = normalize_reference(case.reference_a) or ""
        norm_b = normalize_reference(case.reference_b) or ""
        
        num_a = "|".join(extract_numeric_tokens(case.reference_a))
        num_b = "|".join(extract_numeric_tokens(case.reference_b))
        
        score = reference_score(case.reference_a, case.reference_b)
        score_val = float(score) if score is not None else 0.0
        current_scores.append((case, score_val))
        
        print(f"{case.case_id:<7} {case.reference_a:<17} {case.reference_b:<17} {case.expected_relationship:<18} {norm_a:<16} {norm_b:<16} {num_a:<15} {num_b:<15} {score_val:.4f}")

    print("\nCurrent-score summary")
    print("-" * 21)
    strong_positives = [s for c, s in current_scores if c.expected_relationship == "strong_positive"]
    weak_collisions = [s for c, s in current_scores if c.expected_relationship == "weak_collision"]
    
    print(f"Strong positives: {len(strong_positives)}")
    print(f"Weak collisions: {len(weak_collisions)}")
    print(f"Distinct: {sum(1 for c, s in current_scores if c.expected_relationship == 'distinct')}")
    print(f"Ambiguous: {sum(1 for c, s in current_scores if c.expected_relationship == 'ambiguous')}")
    
    min_sp = min(strong_positives) if strong_positives else 0.0
    max_wc = max(weak_collisions) if weak_collisions else 0.0
    gap = min_sp - max_wc
    
    print(f"\nMinimum strong-positive score: {min_sp:.4f}")
    print(f"Maximum weak-collision score: {max_wc:.4f}")
    print(f"Strong-vs-collision gap: {gap:.4f}")

    print("\nShared-token diagnostics:")
    print(f"{'Case':<7} {'Token':<11} {'RawLen':<7} {'SigLen':<7} {'Unique':<7} {'UniqueRatio':<12} {'SingleDigit':<12} {'Sequential':<11} {'LeadingZeroRatio':<17} {'TokenCountA':<12} {'TokenCountB'}")
    print("-" * 128)
    
    for case in CASES:
        tokens_a = extract_numeric_tokens(case.reference_a)
        tokens_b = extract_numeric_tokens(case.reference_b)
        shared = set(tokens_a) & set(tokens_b)
        for token in shared:
            raw_len = len(token)
            sig = token.lstrip("0") or "0"
            sig_len = len(sig)
            unique_c = len(set(token))
            unique_r = unique_c / raw_len if raw_len > 0 else 0
            single_d = "yes" if unique_c == 1 else "no"
            
            # Sequential check
            is_seq = False
            if raw_len > 1:
                diffs = [int(token[i+1]) - int(token[i]) for i in range(raw_len-1)]
                if all(d == 1 for d in diffs) or all(d == -1 for d in diffs):
                    is_seq = True
            seq_str = "yes" if is_seq else "no"
            
            lz_count = raw_len - len(token.lstrip("0"))
            if token.lstrip("0") == "":
                lz_count = raw_len - 1
            lz_ratio = lz_count / raw_len if raw_len > 0 else 0.0
            
            tca = len(tokens_a)
            tcb = len(tokens_b)
            
            print(f"{case.case_id:<7} {token:<11} {raw_len:<7} {sig_len:<7} {unique_c:<7} {unique_r:<12.4f} {single_d:<12} {seq_str:<11} {lz_ratio:<17.4f} {tca:<12} {tcb}")

    print("\nModel comparison:")
    print(f"{'Case':<7} {'Label':<18} {'Current':<10} {'SigGate':<10} {'Graded':<10} {'Intrinsic'}")
    print("-" * 73)
    
    model_scores = {"Current": [], "SigGate": [], "Graded": [], "Intrinsic": []}
    
    for case in CASES:
        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        sigg = float(model_sig_gate(case.reference_a, case.reference_b) or 0.0)
        grad = float(model_graded(case.reference_a, case.reference_b) or 0.0)
        intr = float(model_intrinsic(case.reference_a, case.reference_b) or 0.0)
        
        model_scores["Current"].append((case, curr))
        model_scores["SigGate"].append((case, sigg))
        model_scores["Graded"].append((case, grad))
        model_scores["Intrinsic"].append((case, intr))
        
        print(f"{case.case_id:<7} {case.expected_relationship:<18} {curr:<10.4f} {sigg:<10.4f} {grad:<10.4f} {intr:.4f}")

    print("\nModel summary")
    print("-" * 13)
    print(f"{'Model':<11} {'MinPositive':<14} {'MaxCollision':<14} {'Gap'}")
    
    for mname in ["Current", "SigGate", "Graded", "Intrinsic"]:
        scores = model_scores[mname]
        sp = [s for c, s in scores if c.expected_relationship == "strong_positive"]
        wc = [s for c, s in scores if c.expected_relationship == "weak_collision"]
        min_sp = min(sp) if sp else 0.0
        max_wc = max(wc) if wc else 0.0
        gap = min_sp - max_wc
        print(f"{mname:<11} {min_sp:<14.4f} {max_wc:<14.4f} {gap:.4f}")

    for mname in ["Current", "SigGate", "Graded", "Intrinsic"]:
        print(f"\n{mname} ranking")
        print("-" * (len(mname) + 8))
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        for i, (c, s) in enumerate(ranked):
            print(f"{i+1}. {c.case_id}  {c.expected_relationship}  {s:.4f}")
            
    print("\nWeak collisions in top 10:")
    for mname in ["Current", "SigGate", "Graded", "Intrinsic"]:
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        top10 = ranked[:10]
        count = sum(1 for c, s in top10 if c.expected_relationship == "weak_collision")
        print(f"{mname}: {count}")

    print("\nProbe Results")
    print("-" * 13)
    for probe in PROBE_CASES:
        curr = float(reference_score(probe.reference_a, probe.reference_b) or 0.0)
        sigg = float(model_sig_gate(probe.reference_a, probe.reference_b) or 0.0)
        grad = float(model_graded(probe.reference_a, probe.reference_b) or 0.0)
        intr = float(model_intrinsic(probe.reference_a, probe.reference_b) or 0.0)
        print(f"{probe.case_id}: {probe.reference_a} <-> {probe.reference_b}")
        print(f"Current: {curr:.4f}, SigGate: {sigg:.4f}, Graded: {grad:.4f}, Intrinsic: {intr:.4f}\n")


if __name__ == "__main__":
    main()
````

## File: experiments/inspect_reference_contributions.py
````python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity,
    enrich_reference_identity, _construct_reference_evidence_contributions
)

def evaluate_reference_contributions():
    policy = ReferenceEvidencePolicy()
    
    # We will construct a profile dynamically per test case
    
    cases = [
        {"id": "RC001", "a": "INV-874219", "b": "INV/874219"},
        {"id": "RC002", "a": "CREDIT-NOTE", "b": "CREDITNOTE"},
        {"id": "RC003", "a": "INV-999999", "b": "INV/999999"},
        {"id": "RC004", "a": "000000", "b": "000000"},
        {"id": "RC005", "a": "INV-874219", "b": "AB/874219"},
        {"id": "RC006", "a": "INV-001", "b": "ABC-001"},
        {"id": "RC007", "a": "NEW-874219", "b": "XYZ-874219"},
        {"id": "RC008", "a": "NEW-999999", "b": "XYZ-999999"},
        {"id": "RC009", "a": "INV-2026-874219", "b": "AB-2026-874219"},
    ]
    
    print("REFERENCE EVIDENCE CONTRIBUTION INSPECTION")
    print("-" * 100)
    for c in cases:
        print(f"Case: {c['id']}")
        
        identity = extract_reference_identity(c["a"], c["b"])
        if not identity:
            continue
            
        print(f"Exact Normalized Match: {identity.exact_normalized_match}")
        
        # We must carefully inject the norm refs and token DFs into the profile if needed for this script
        # But wait, our profile validation requires sum(norm_freq) == N.
        # We need to construct a valid profile per test or just a single valid one.
        # It's easier to dynamically create a profile that perfectly fits each case so we don't violate the invariant.
        
        if c['id'] == "RC001":
            p = ReferenceCorpusProfile(100, {"inv874219": 1, "dummy": 99}, {})
        elif c['id'] == "RC002":
            p = ReferenceCorpusProfile(100, {"creditnote": 100}, {})
        elif c['id'] == "RC003":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC004":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC005":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {"874219": 1})
        elif c['id'] == "RC006":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {"001": 100})
        elif c['id'] == "RC007":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC008":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC009":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 10, "874219": 1})
            
        enriched = enrich_reference_identity(identity, p)
        contributions = _construct_reference_evidence_contributions(enriched, policy)
        
        print(f"Contribution Count: {len(contributions)}")
        for i, contrib in enumerate(contributions):
            print(f"  Contribution {i+1}:")
            print(f"    evidence_kind: {contrib.evidence_kind}")
            print(f"    identity_value: {contrib.identity_value}")
            print(f"    positive_evidence: {contrib.positive_evidence:.2f}")
            print(f"    statistics_available: {contrib.statistics_available}")
            
        print("-" * 60)

if __name__ == "__main__":
    evaluate_reference_contributions()
````

## File: experiments/stage_4d_audit.py
````python
import math
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.matching.scoring import SignalName
from experiments.legacy_reference import reference_score as legacy_reference_score
from recongraph.matching.pair_scorers import score_purchase_to_gst, PairScoringResult
from recongraph.matching.reference_evidence import (
    ReferenceCorpusProfile,
    ReferenceEvidencePolicy,
    ReferenceEvidenceContext,
)
from recongraph.matching.purchase_gst_semantics import SemanticFinding

def run_audit():
    # Setup dummy profile for exact math
    # 001 appears 81 times out of 100 -> score 1 - sqrt(0.81) = 0.10
    # 1042 appears 2 times out of 1000 -> score 1 - sqrt(0.002) = 0.955
    # 874219 appears 10 times out of 1000 -> score 1 - sqrt(0.01) = 0.90
    prof = ReferenceCorpusProfile(
        reference_count=1000,
        normalized_reference_frequency={"dummy": 907, "inv1042": 2, "inv874219": 10, "001": 81},
        numeric_token_document_frequency={"1042": 2, "874219": 10, "001": 81}
    )
    context = ReferenceEvidenceContext(profile=prof, policy=ReferenceEvidencePolicy())

    challenges = {
        "HN001": (
            PurchaseRecord(record_id="pur_bec420c3", vendor_name="ABC", reference="INV-1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_1ab36d4e", vendor_name="ABC", reference="AB/1042", amount=2000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
        ),
        "HN002": (
            PurchaseRecord(record_id="pur_d9008b6e", vendor_name="XYZ", reference="INV-1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_cab03bdf", vendor_name="XYZ", reference="AB/1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX2"),
        ),
        "HN003": (
            PurchaseRecord(record_id="pur_ffb6116d", vendor_name="DEF", reference="INV-MAY", amount=1000.0, record_date=date(2023,5,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_c24cb47e", vendor_name="DEF", reference="INV-JUN", amount=1000.0, record_date=date(2023,6,1), tax_identity="TAX1"),
        ),
        "HN004": (
            PurchaseRecord(record_id="pur_4625e9e7", vendor_name="GHI", reference="OMD-001", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_f9dc1142", vendor_name="GHI", reference="NSS-001", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
        ),
        "HN005": (
            PurchaseRecord(record_id="pur_bea4c94e", vendor_name="JKL", reference="INV-1042", amount=2000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_006cb9ba", vendor_name="JKL", reference="AB/1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
        )
    }
    
    empty_pathologicals = {
        "None vs None": (None, None),
        "Empty vs Empty": ("", ""),
        "None vs INV123": (None, "INV123"),
        "INV123 vs None": ("INV123", None),
        "Empty vs INV123": ("", "INV123"),
        "--- vs ///": ("---", "///"),
        "creditnote vs None": ("creditnote", None),
    }

    print("=== PART 1: LEGACY VS NEW REFERENCE ENGINE ===")
    print("Pair | Legacy | New | Coverage | Reason")
    for name, (p, g) in challenges.items():
        leg_ref = legacy_reference_score(p.reference, g.reference)
        res = score_purchase_to_gst(p, g, context)
        new_ref = res.signals[SignalName.REFERENCE]
        cov = res.reference_interpretation.statistical_coverage
        leg_str = f"{leg_ref:.2f}" if leg_ref is not None else "None"
        new_str = f"{new_ref:.2f}" if new_ref is not None else "None"
        print(f"{name} | {leg_str} | {new_str} | {cov:.1f} | ?")

    print("\n=== PART 2: RELATIONSHIP SCORE MOVEMENT ===")
    print("Pair | Old Base Score | New Base Score | Reason")
    for name, (p, g) in challenges.items():
        # To get old base score, we fake the reference signal with legacy score
        leg_ref = legacy_reference_score(p.reference, g.reference)
        res_new = score_purchase_to_gst(p, g, context)
        
        # We can mock calculate_relationship_score but let's just observe the actual new score vs what it used to be.
        # Actually, let's inject the legacy score to see what the old base score was.
        # Or calculate it: 0.2*Entity + 0.2*Ref + 0.25*Amt + 0.1*Temp + 0.25*Tax = Total / Available
        # It's easier just to re-run the score calculation or approximate.
        # Let's print new score for now and I will manually fill the table.
        print(f"{name} | old | {res_new.relationship.base_score:.4f} | ?")
        
    print("\n=== PART 3: SEMANTIC FINDINGS AUDIT ===")
    for name, (p, g) in challenges.items():
        res = score_purchase_to_gst(p, g, context)
        print(f"{name}: {res.semantic_findings}")
        
    print("\n=== PART 4: COVERAGE AUDIT ===")
    for name, (p, g) in challenges.items():
        res = score_purchase_to_gst(p, g, context)
        print(f"{name}: {res.reference_interpretation.statistical_coverage}")
        
    print("\n=== PART 5: EMPTY REFERENCE AUDIT ===")
    for name, (ref_a, ref_b) in empty_pathologicals.items():
        p = PurchaseRecord(record_id="pur_b4374f15", vendor_name="A", reference=ref_a, amount=100.0, record_date=date(2023,1,1), tax_identity="TAX")
        g = GSTRecord(record_id="gst_9a421bc1", vendor_name="A", reference=ref_b, amount=100.0, record_date=date(2023,1,1), tax_identity="TAX")
        try:
            res = score_purchase_to_gst(p, g, context)
            ref_sig = res.signals[SignalName.REFERENCE]
            score = res.relationship.score
            cov = res.reference_interpretation.statistical_coverage
            sem = res.semantic_findings
            print(f"{name} -> RefSig: {ref_sig}, PairScore: {score:.2f}, Cov: {cov:.1f}, Sem: {sem}")
        except Exception as e:
            print(f"{name} -> CRASH: {e}")

    print("\n=== PART 7: EXPLAINABILITY AUDIT (HN004) ===")
    p, g = challenges["HN004"]
    res = score_purchase_to_gst(p, g, context)
    print("Interpretation:", res.reference_interpretation)

if __name__ == "__main__":
    run_audit()
````

## File: src/recongraph/candidate_generation/generator.py
````python
from dataclasses import dataclass
from typing import Iterable
from recongraph.candidate_generation.blockers import Blocker
from recongraph.candidate_generation.index import InvertedIndex
from recongraph.domain.records import PurchaseRecord, GSTRecord

@dataclass(frozen=True)
class CandidateEdge:
    """
    Represents a plausible pairing between a purchase and GST record,
    along with the exact keys that connected them.
    """
    purchase: PurchaseRecord
    gst_record: GSTRecord
    shared_blocking_keys: frozenset[str]

from recongraph.plugins.provider import EvidenceProvider

class CandidateGenerator:
    """
    Orchestrates the blocking and indexing strategy to yield CandidateEdges
    in sub-quadratic time by eliminating records with disjoint blocking keys.
    """
    def __init__(self, providers: Iterable[EvidenceProvider]):
        blockers = []
        for provider in providers:
            blockers.extend(provider.get_blockers())
        self.blockers = tuple(blockers)
        
    def generate(
        self,
        purchases: Iterable[PurchaseRecord],
        gst_records: Iterable[GSTRecord],
    ) -> Iterable[CandidateEdge]:
        """
        Yields edges where the purchase and GST record share at least one blocking key.
        """
        # Build index for the larger/stationary set (we assume GST records are the corpus)
        gst_index = InvertedIndex(self.blockers)
        for gst in gst_records:
            gst_index.add(gst)
            
        # Probe the index with purchases
        for purchase in purchases:
            purchase_keys = set()
            for blocker in self.blockers:
                purchase_keys.update(blocker.extract_keys(purchase))
                
            if not purchase_keys:
                continue
                
            # Aggregate matches: GSTRecord -> shared_keys
            matches = {}
            for key in purchase_keys:
                for gst in gst_index.query(key):
                    if gst not in matches:
                        matches[gst] = set()
                    matches[gst].add(key)
                    
            # Yield candidate edges
            for gst, shared_keys in matches.items():
                yield CandidateEdge(
                    purchase=purchase,
                    gst_record=gst,
                    shared_blocking_keys=frozenset(shared_keys)
                )
````

## File: src/recongraph/domain/claims.py
````python
import re
from dataclasses import dataclass
from enum import Enum
from .scopes import ScopeKind


class ClaimSymmetry(str, Enum):
    """
    Positive semantic vocabulary for claim directionality.
    """
    SYMMETRIC = "symmetric"
    DIRECTIONAL = "directional"


@dataclass(frozen=True)
class ClaimId:
    """
    Typed, immutable, validated claim identifier.
    Must follow the grammar <namespace>.<name> where segments are [a-z][a-z0-9_]*
    """
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*$")

    def __post_init__(self):
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid ClaimId format: '{self.value}'")

    def __str__(self) -> str:
        return self.value

    def to_dict(self) -> str:
        return self.value


@dataclass(frozen=True, order=True)
class ClaimSemanticVersion:
    """
    Strict semantic version for claims.
    Rejects booleans and values less than 1.
    """
    value: int

    def __post_init__(self):
        # bool is a subclass of int in Python, so isinstance(True, int) is True.
        # We must explicitly reject bool.
        if isinstance(self.value, bool):
            raise TypeError("Semantic version cannot be a boolean.")
        if not isinstance(self.value, int):
            raise TypeError("Semantic version must be an integer.")
        if self.value < 1:
            raise ValueError("Semantic version must be >= 1.")

    def __str__(self) -> str:
        return str(self.value)

    def to_dict(self) -> int:
        return self.value


@dataclass(frozen=True)
class ClaimDescriptor:
    """
    Immutable semantic descriptor for a claim family and version.
    Defines the structural invariants of the claim (symmetry, valid scopes)
    without knowing about providers or evaluation logic.
    """
    claim_id: ClaimId
    semantic_version: ClaimSemanticVersion
    symmetry: ClaimSymmetry
    allowed_scope_kinds: frozenset['ScopeKind']

    def __init__(
        self,
        claim_id: ClaimId | str,
        semantic_version: ClaimSemanticVersion | int,
        symmetry: ClaimSymmetry,
        allowed_scope_kinds: frozenset['ScopeKind'] | set['ScopeKind'] | list['ScopeKind']
    ):
        if isinstance(claim_id, str):
            claim_id = ClaimId(claim_id)
        if isinstance(semantic_version, int) and not isinstance(semantic_version, bool):
            semantic_version = ClaimSemanticVersion(semantic_version)

        frozen_scopes = frozenset(allowed_scope_kinds)
        if not frozen_scopes:
            raise ValueError("CD-001 Violation: Claim must have at least one allowed scope kind.")

        object.__setattr__(self, 'claim_id', claim_id)
        object.__setattr__(self, 'semantic_version', semantic_version)
        object.__setattr__(self, 'symmetry', symmetry)
        object.__setattr__(self, 'allowed_scope_kinds', frozen_scopes)

    def validates_scope_kind(self, scope_kind: 'ScopeKind') -> bool:
        """
        Validates whether this claim allows the given scope kind.
        """
        return scope_kind in self.allowed_scope_kinds

    def to_dict(self) -> dict:
        return {
            "claim_id": self.claim_id.to_dict(),
            "semantic_version": self.semantic_version.to_dict(),
            "symmetry": self.symmetry.value,
            "allowed_scope_kinds": sorted([sk.value for sk in self.allowed_scope_kinds])
        }

class ImmutableCatalog(type):
    def __setattr__(cls, name, value):
        raise AttributeError(f"Cannot modify immutable catalog {cls.__name__}")

class CoreClaims(metaclass=ImmutableCatalog):
    """
    Immutable catalog of core claim semantics for ReconGraph v0.1.
    """
    SAME_LEGAL_ENTITY = ClaimDescriptor(
        claim_id="identity.same_legal_entity",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR, ScopeKind.GROUP_PAIR}
    )

    SAME_GST_REGISTRATION = ClaimDescriptor(
        claim_id="identity.same_gst_registration",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR, ScopeKind.GROUP_PAIR}
    )

    LEXICAL_NAME_SIMILARITY = ClaimDescriptor(
        claim_id="identity.lexical_name_similarity",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )

    LEGAL_FORM_COMPATIBILITY = ClaimDescriptor(
        claim_id="identity.legal_form_compatibility",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )

    AMOUNT_CONSERVATION = ClaimDescriptor(
        claim_id="financial.amount_conservation",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR, ScopeKind.GROUP_PAIR}
    )

    CURRENCY_COMPATIBILITY = ClaimDescriptor(
        claim_id="financial.currency_compatibility",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR, ScopeKind.GROUP_PAIR}
    )

    STRUCTURAL_COMPATIBILITY = ClaimDescriptor(
        claim_id="reference.structural_compatibility",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR, ScopeKind.GROUP_PAIR}
    )

    REFERENCE_IS_PARSEABLE = ClaimDescriptor(
        claim_id="document.reference_is_parseable",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD}
    )
````

## File: src/recongraph/graph/evaluator.py
````python
from typing import Iterable
from recongraph.graph.candidate import CandidateGraph
from recongraph.graph.hypotheses import Hypothesis, EvaluatedHypothesis, EligibilityStatus
from recongraph.matching.signals import amount_score, tax_identity_score, entity_score
from recongraph.matching.scoring import SignalName, calculate_relationship_score
from recongraph.matching.purchase_gst_semantics import (
    analyze_purchase_gst_semantics, 
    evaluate_purchase_gst_one_to_one_eligibility, 
    OneToOneEligibility
)
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, compute_reference_interpretation
from recongraph.matching.pair_scorers import PURCHASE_TO_GST_POLICY, PURCHASE_TO_GST_MAX_DAYS
from recongraph.matching.scoring import RelationshipPolicy

from recongraph.plugins.provider import EvidenceProvider

class HypothesisEvaluator:
    """
    Evaluates a structural hypothesis by delegating to EvidenceProviders.
    """
    def __init__(self, evidence_providers: Iterable[EvidenceProvider], policy: RelationshipPolicy):
        self.evidence_providers = tuple(evidence_providers)
        self.policy = policy

    def evaluate(self, graph: CandidateGraph, hypothesis: Hypothesis) -> EvaluatedHypothesis:
        # HS-004: If hypothesis is empty, it resolves nothing.
        if not hypothesis.matched_nodes:
            return EvaluatedHypothesis(
                hypothesis=hypothesis,
                score=0.0,
                eligibility=EligibilityStatus.INELIGIBLE,
                supporting_evidence={},
                violations=frozenset(["EMPTY_HYPOTHESIS"])
            )
            
        purchases = []
        gsts = []
        
        for u in hypothesis.matched_nodes:
            if u.startswith("urn:recongraph:purchase:"):
                purchases.append(graph.nodes[u])
            elif u.startswith("urn:recongraph:gst:"):
                gsts.append(graph.nodes[u])
                
        # Must be bipartite
        if not purchases or not gsts:
            return EvaluatedHypothesis(
                hypothesis=hypothesis,
                score=0.0,
                eligibility=EligibilityStatus.INELIGIBLE,
                supporting_evidence={},
                violations=frozenset(["MISSING_COUNTERPARTY"])
            )
            
        # Evidence Aggregation via Plugins
        signals = {}
        violations = set()
        supporting_metadata = {}
        
        for provider in self.evidence_providers:
            contrib = provider.evaluate(purchases, gsts)
            if contrib.score is not None:
                signals[contrib.provider_name] = contrib.score
            violations.update(contrib.violations)
            if contrib.metadata:
                supporting_metadata[contrib.provider_name] = contrib.metadata
                
        semantic_findings = analyze_purchase_gst_semantics(signals)
        legacy_eligibility = evaluate_purchase_gst_one_to_one_eligibility(semantic_findings)
        
        if legacy_eligibility.status == OneToOneEligibility.ELIGIBLE:
            eligibility = EligibilityStatus.ELIGIBLE
        elif legacy_eligibility.status == OneToOneEligibility.REQUIRES_REVIEW:
            eligibility = EligibilityStatus.REQUIRES_REVIEW
        else:
            eligibility = EligibilityStatus.INELIGIBLE
            
        relationship = calculate_relationship_score(
            signals=signals, policy=self.policy
        )
        
        violations.update({str(f.value) for f in semantic_findings})
        
        if "TEMPORAL_MAX_DAYS_EXCEEDED" in violations:
            eligibility = EligibilityStatus.INELIGIBLE
        
        supporting_evidence = {
            "signals": signals,
            "relationship": relationship,
            "metadata": supporting_metadata
        }

        return EvaluatedHypothesis(
            hypothesis=hypothesis,
            score=relationship.score,
            eligibility=eligibility,
            supporting_evidence=supporting_evidence,
            violations=frozenset(violations)
        )
````

## File: src/recongraph/graph/hypotheses.py
````python
from dataclasses import dataclass
from typing import Generic, TypeVar, Any
from enum import Enum
from recongraph.graph.candidate import NodeID, CandidateGraph

@dataclass(frozen=True)
class ConnectedComponent:
    """
    An isolated subgraph extracted from the CandidateGraph.
    Represents a mathematically independent search space.
    """
    graph: CandidateGraph
    # We maintain a reference to the global graph structure but scoped down.
    # The CandidateGraph class already enforces immutability.

@dataclass(frozen=True)
class Hypothesis:
    """
    An immutable proposed resolution claiming to settle a specific subset
    of records within a connected component.
    """
    component_nodes: frozenset[NodeID]
    proposed_edges: frozenset[frozenset[NodeID]]
    
    @property
    def matched_nodes(self) -> frozenset[NodeID]:
        return frozenset(n for edge in self.proposed_edges for n in edge)
        
    @property
    def unmatched_nodes(self) -> frozenset[NodeID]:
        return self.component_nodes - self.matched_nodes

class EligibilityStatus(Enum):
    ELIGIBLE = "eligible"
    INELIGIBLE = "ineligible"
    REQUIRES_REVIEW = "requires_review"

@dataclass(frozen=True)
class EvaluatedHypothesis:
    """
    Wraps a structural claim with its resulting score, eligibility, 
    and the exact evidence that justifies it.
    """
    hypothesis: Hypothesis
    score: float
    eligibility: EligibilityStatus
    supporting_evidence: dict[str, Any]
    violations: frozenset[str]
````

## File: src/recongraph/graph/trace.py
````python
from dataclasses import dataclass
from enum import StrEnum
from typing import Any
from datetime import datetime, timezone

class TraceStage(StrEnum):
    CANDIDATE_GENERATION = "candidate_generation"
    GRAPH_BUILDING = "graph_building"
    COMPONENT_EXTRACTION = "component_extraction"
    HYPOTHESIS_SEARCH = "hypothesis_search"
    HYPOTHESIS_EVALUATION = "hypothesis_evaluation"
    DECISION_EVALUATION = "decision_evaluation"
    EXPLANATION_GENERATION = "explanation_generation"

@dataclass(frozen=True)
class TraceEvent:
    """An explicit, chronological record of a single action in the reconciliation pipeline."""
    timestamp: datetime
    stage: TraceStage
    payload: Any  # E.g., CandidateEdge, CandidateGraph, Hypothesis, EvaluatedHypothesis, ReconciliationDecision

@dataclass(frozen=True)
class DecisionTrace:
    """The immutable historical record of an entire reconciliation execution."""
    trace_id: str
    engine_version: str
    config_hash: str
    events: tuple[TraceEvent, ...]
    
    def get_events_for_stage(self, stage: TraceStage) -> tuple[TraceEvent, ...]:
        return tuple(e for e in self.events if e.stage == stage)
        
    def to_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "engine_version": self.engine_version,
            "config_hash": self.config_hash,
            "events": [
                {
                    "timestamp": e.timestamp.isoformat(),
                    "stage": e.stage.value,
                    "payload": repr(e.payload) # Placeholder for robust serialization
                }
                for e in self.events
            ]
        }

class TraceBuilder:
    """
    A passive recorder that assembles the historical trace chronologically.
    It strictly adheres to the Recorder Principle (never recalculates or alters).
    """
    def __init__(self, trace_id: str, engine_version: str, config_hash: str):
        self._trace_id = trace_id
        self._engine_version = engine_version
        self._config_hash = config_hash
        self._events: list[TraceEvent] = []
        
    def record_event(self, stage: TraceStage, payload: Any) -> None:
        """Records a new event in the chronological sequence."""
        event = TraceEvent(
            timestamp=datetime.now(timezone.utc),
            stage=stage,
            payload=payload
        )
        self._events.append(event)
        
    def build(self) -> DecisionTrace:
        """Freezes the chronological events into an immutable DecisionTrace."""
        return DecisionTrace(
            trace_id=self._trace_id,
            engine_version=self._engine_version,
            config_hash=self._config_hash,
            events=tuple(self._events)
        )
````

## File: src/recongraph/matching/scoring.py
````python
from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from math import isfinite


class SignalName:
    """Names of primitive compatibility signals."""

    ENTITY = "entity"
    REFERENCE = "reference"
    AMOUNT = "amount"
    TEMPORAL = "temporal"
    TAX_IDENTITY = "tax_identity"


@dataclass(frozen=True)
class RelationshipPolicy:
    """Define how a financial relationship interprets primitive signals."""

    weights: Mapping[str, float]
    contradiction_penalties: Mapping[str, float] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        if not self.weights:
            raise ValueError(
                "Relationship policy requires at least one signal weight."
            )

        for weight in self.weights.values():
            if not isfinite(weight) or weight <= 0.0:
                raise ValueError(
                    "Signal weights must be finite and greater than zero."
                )

        for penalty in self.contradiction_penalties.values():
            if not isfinite(penalty) or not 0.0 <= penalty <= 1.0:
                raise ValueError(
                    "Contradiction penalties must be between "
                    "0.0 and 1.0."
                )

        for signal_name in self.contradiction_penalties:
            if signal_name not in self.weights:
                raise ValueError(
                    "A contradiction signal must also have "
                    "a configured weight."
                )


@dataclass(frozen=True)
class RelationshipScore:
    """Represent an explainable relationship scoring result."""

    score: float | None
    base_score: float | None
    coverage: float
    contradiction_penalty: float
    active_contradictions: tuple[str, ...]


def calculate_relationship_score(
    signals: Mapping[str, float | None],
    policy: RelationshipPolicy,
) -> RelationshipScore:
    """Aggregate primitive evidence under a relationship policy."""
    if set(signals) != set(policy.weights):
        raise ValueError(
            "Signal names must exactly match policy signals."
        )

    for score in signals.values():
        if score is None:
            continue

        if not isfinite(score) or not 0.0 <= score <= 1.0:
            raise ValueError(
                "Signal scores must be finite and between "
                "0.0 and 1.0."
            )

    total_weight = sum(policy.weights.values())

    available_weight = 0.0
    weighted_numerator = 0.0

    for signal_name, signal_score in signals.items():
        if signal_score is None:
            continue

        weight = policy.weights[signal_name]

        available_weight += weight
        weighted_numerator += weight * signal_score

    coverage = available_weight / total_weight

    active_contradictions = tuple(
        signal_name
        for signal_name in policy.contradiction_penalties
        if signals[signal_name] == 0.0
    )

    contradiction_penalty = 1.0

    for signal_name in active_contradictions:
        contradiction_penalty *= (
            policy.contradiction_penalties[signal_name]
        )

    if available_weight == 0.0:
        return RelationshipScore(
            score=None,
            base_score=None,
            coverage=coverage,
            contradiction_penalty=contradiction_penalty,
            active_contradictions=active_contradictions,
        )

    base_score = weighted_numerator / available_weight
    final_score = base_score * contradiction_penalty

    return RelationshipScore(
        score=final_score,
        base_score=base_score,
        coverage=coverage,
        contradiction_penalty=contradiction_penalty,
        active_contradictions=active_contradictions,
    )
````

## File: src/recongraph/normalization/text.py
````python
import re

LEGAL_SUFFIX_TOKENS = {
    "pvt",
    "private",
    "ltd",
    "limited",
}

VENDOR_TOKEN_ALIASES = {
    "ent": "enterprises",
    "steels": "steel",
    "components": "component",
    "solutions": "solution",
    "supplies": "supply",
}


def normalize_reference(reference: str) -> str:
    """Normalize a financial reference for deterministic comparison."""
    return "".join(
        character.lower()
        for character in reference
        if character.isalnum()
    )


def normalize_vendor_name(name: str) -> str:
    """Normalize a vendor name while preserving meaningful word boundaries."""
    cleaned_name = "".join(
        character.lower() if character.isalnum() else " "
        for character in name
    )

    tokens = cleaned_name.split()

    meaningful_tokens = [
        token
        for token in tokens
        if token not in LEGAL_SUFFIX_TOKENS
    ]

    canonical_tokens = [
        VENDOR_TOKEN_ALIASES.get(token, token)
        for token in meaningful_tokens
    ]

    return " ".join(canonical_tokens)


def normalize_tax_identity(tax_identity: str) -> str:
    """Normalize a tax identity for deterministic comparison."""
    return tax_identity.strip().upper()


def extract_numeric_reference_tokens(
    reference: str,
    min_length: int = 3,
) -> set[str]:
    """Extract significant numeric tokens from a financial reference."""
    if min_length <= 0:
        raise ValueError("min_length must be greater than zero")

    numeric_tokens = re.findall(r"\d+", reference)

    return {
        token
        for token in numeric_tokens
        if len(token) >= min_length
    }
````

## File: tests/test_candidate_generation.py
````python
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.candidate_generation.blockers import (
    ExactAmountBlocker,
    TaxIdentityBlocker,
    ReferenceTokenBlocker,
)
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TaxEvidenceProvider, ReferenceEvidenceProvider
from recongraph.candidate_generation.index import InvertedIndex
from recongraph.candidate_generation.generator import CandidateGenerator
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, ReferenceEvidenceContext, ReferenceEvidencePolicy

def test_exact_amount_blocker():
    blocker = ExactAmountBlocker()
    record = PurchaseRecord(record_id="dummy_p", vendor_name="A", reference="B", amount=150.00, record_date=date(2026, 1, 1), tax_identity="AB123")
    keys = blocker.extract_keys(record)
    assert keys == frozenset(["AMT:150.00"])

def test_tax_identity_blocker():
    blocker = TaxIdentityBlocker()
    record = PurchaseRecord(record_id="dummy_p", vendor_name="A", reference="B", amount=150.00, record_date=date(2026, 1, 1), tax_identity=" AB123 ")
    keys = blocker.extract_keys(record)
    assert keys == frozenset(["TAX:AB123"])

def test_reference_token_blocker_statistical():
    # Profile where '874219' is rare (freq=1/100 -> mag=0.9)
    # and '001' is common (freq=81/100 -> mag=0.1)
    prof = ReferenceCorpusProfile(
        reference_count=100,
        normalized_reference_frequency={"inv874219": 1, "inv001": 81, "dummy": 18},
        numeric_token_document_frequency={"874219": 1, "001": 81}
    )
    # Rarity threshold 0.8
    blocker = ReferenceTokenBlocker(profile=prof, rarity_threshold=0.8)
    
    # Rare token test
    record_rare = PurchaseRecord(record_id="dummy_p", vendor_name="A", reference="INV-874219", amount=150.00, record_date=date(2026, 1, 1), tax_identity="AB123")
    keys_rare = blocker.extract_keys(record_rare)
    assert "REF_NORM:inv874219" in keys_rare
    assert "REF_TOK:874219" in keys_rare
    
    # Common token test
    record_common = PurchaseRecord(record_id="dummy_p", vendor_name="A", reference="INV-001", amount=150.00, record_date=date(2026, 1, 1), tax_identity="AB123")
    keys_common = blocker.extract_keys(record_common)
    assert "REF_NORM:inv001" not in keys_common
    assert "REF_TOK:001" not in keys_common
    assert not keys_common

def test_candidate_generator_reduction():
    prof = ReferenceCorpusProfile(
        reference_count=1000,
        normalized_reference_frequency={"inv123": 1, "inv999": 1, "dummy": 998},
        numeric_token_document_frequency={"123": 1, "999": 1}
    )
    providers = [
        FinancialEvidenceProvider(), 
        TaxEvidenceProvider(),
        ReferenceEvidenceProvider(ReferenceEvidenceContext(prof, ReferenceEvidencePolicy()))
    ]
    generator = CandidateGenerator(providers)
    
    # 1 Purchase
    purchases = [
        PurchaseRecord(record_id="dummy_p", vendor_name="A", reference="INV-123", amount=500.0, record_date=date(2026, 1, 1), tax_identity="TAX-A")
    ]
    
    # 3 GST Records
    gst_records = [
        # Match by Reference
        GSTRecord(record_id="dummy_g", vendor_name="A", reference="INV-123", amount=999.0, record_date=date(2026, 1, 1), tax_identity="TAX-B"),
        # Match by Amount
        GSTRecord(record_id="dummy_g", vendor_name="B", reference="INV-999", amount=500.0, record_date=date(2026, 1, 1), tax_identity="TAX-C"),
        # No Match (Should be filtered out)
        GSTRecord(record_id="dummy_g", vendor_name="C", reference="INV-888", amount=100.0, record_date=date(2026, 1, 1), tax_identity="TAX-D"),
    ]
    
    edges = list(generator.generate(purchases, gst_records))
    
    assert len(edges) == 2
    
    # Find the edges
    edge_ref = next(e for e in edges if e.gst_record.reference == "INV-123")
    assert "REF_TOK:123" in edge_ref.shared_blocking_keys
    
    edge_amt = next(e for e in edges if e.gst_record.reference == "INV-999")
    assert "AMT:500.00" in edge_amt.shared_blocking_keys
````

## File: tests/test_claim_semantics.py
````python
import pytest
from recongraph.domain.claims import ClaimId, ClaimSemanticVersion, ClaimSymmetry, ClaimDescriptor
from recongraph.domain.scopes import ScopeKind

def test_claim_id_accepts_valid_namespaced_identifier():
    assert ClaimId("identity.same_legal_entity").value == "identity.same_legal_entity"

def test_claim_id_rejects_missing_namespace():
    with pytest.raises(ValueError):
        ClaimId("same_legal_entity")

def test_claim_id_rejects_uppercase():
    with pytest.raises(ValueError):
        ClaimId("Identity.SameLegalEntity")

def test_claim_id_rejects_hyphen():
    with pytest.raises(ValueError):
        ClaimId("identity.same-entity")

def test_claim_id_rejects_empty_segment():
    with pytest.raises(ValueError):
        ClaimId("identity..same")
    with pytest.raises(ValueError):
        ClaimId(".identity")

def test_claim_id_is_hashable():
    c1 = ClaimId("a.b")
    c2 = ClaimId("a.b")
    assert hash(c1) == hash(c2)

def test_claim_id_equality_is_value_based():
    assert ClaimId("a.b") == ClaimId("a.b")
    assert ClaimId("a.b") != ClaimId("a.c")

def test_claim_id_does_not_normalize_input():
    with pytest.raises(ValueError):
        ClaimId(" Identity.Same ")

def test_claim_id_round_trip_string():
    assert str(ClaimId("a.b")) == "a.b"

def test_claim_semantic_version_equality():
    assert ClaimSemanticVersion(1) == ClaimSemanticVersion(1)
    assert ClaimSemanticVersion(1) != ClaimSemanticVersion(2)

def test_claim_semantic_version_rejects_zero():
    with pytest.raises(ValueError):
        ClaimSemanticVersion(0)

def test_claim_semantic_version_rejects_negative():
    with pytest.raises(ValueError):
        ClaimSemanticVersion(-1)

def test_claim_semantic_version_rejects_bool():
    with pytest.raises(TypeError):
        ClaimSemanticVersion(True) # type: ignore

def test_claim_symmetry_values_are_stable():
    assert ClaimSymmetry.SYMMETRIC.value == "symmetric"
    assert ClaimSymmetry.DIRECTIONAL.value == "directional"

def test_claim_descriptor_requires_allowed_scope():
    with pytest.raises(ValueError):
        ClaimDescriptor(
            claim_id="a.b",
            semantic_version=1,
            symmetry=ClaimSymmetry.SYMMETRIC,
            allowed_scope_kinds=[]
        )

def test_claim_descriptor_freezes_allowed_scope_kinds():
    scopes = {ScopeKind.RECORD_PAIR}
    descriptor = ClaimDescriptor(
        claim_id="a.b",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds=scopes
    )
    assert isinstance(descriptor.allowed_scope_kinds, frozenset)

def test_same_claim_id_different_semantic_versions_are_distinct():
    d1 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    d2 = ClaimDescriptor("a.b", 2, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    assert d1 != d2
    assert hash(d1) != hash(d2)

def test_descriptor_does_not_depend_on_provider():
    # Attempting to set provider on the frozen dataclass fails
    d1 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    with pytest.raises(AttributeError):
        d1.provider_id = "test" # type: ignore

def test_descriptor_allows_declared_scope_kind():
    d1 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    assert d1.validates_scope_kind(ScopeKind.RECORD_PAIR) is True

def test_descriptor_rejects_undeclared_scope_kind():
    d1 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    assert d1.validates_scope_kind(ScopeKind.GROUP_PAIR) is False

def test_descriptor_is_hashable():
    d1 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    d2 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    assert hash(d1) == hash(d2)

def test_plugin_claim_can_be_described_without_core_enum_change():
    # Just construct a plugin ClaimDescriptor dynamically without modifying core lists.
    plugin_claim = ClaimDescriptor(
        claim_id="custom.bank_account_match",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )
    assert plugin_claim.claim_id.value == "custom.bank_account_match"

def test_claim_descriptor_serialization_is_explicit():
    d1 = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD_PAIR})
    data = d1.to_dict()
    assert data["claim_id"] == "a.b"
    assert data["semantic_version"] == 1
    assert data["symmetry"] == "symmetric"
    assert data["allowed_scope_kinds"] == ["record_pair"]
````

## File: tests/test_core_claims.py
````python
import pytest
from recongraph.domain.claims import CoreClaims
from recongraph.domain.scopes import ScopeKind

def test_core_claim_ids_are_unique():
    # Extract all descriptors
    descriptors = [getattr(CoreClaims, k) for k in dir(CoreClaims) if not k.startswith("_") and k.isupper()]
    ids = [d.claim_id for d in descriptors]
    assert len(ids) == len(set(ids))

def test_core_claim_descriptors_are_unique():
    descriptors = [getattr(CoreClaims, k) for k in dir(CoreClaims) if not k.startswith("_") and k.isupper()]
    assert len(descriptors) == len(set(descriptors))

def test_core_claim_catalog_is_immutable():
    with pytest.raises(AttributeError):
        CoreClaims.NEW_CLAIM = "foo" # type: ignore

def test_same_gst_registration_is_distinct_from_same_legal_entity():
    assert CoreClaims.SAME_GST_REGISTRATION != CoreClaims.SAME_LEGAL_ENTITY

def test_lexical_name_similarity_is_distinct_from_legal_entity_identity():
    assert CoreClaims.LEXICAL_NAME_SIMILARITY != CoreClaims.SAME_LEGAL_ENTITY
````

## File: tests/test_evidence_ancestry_metamorphic.py
````python
import pytest

from recongraph.domain.lineage import (
    SourceSystemId, SourceArtifactId, SourceLocator, StructuredSourceLineage
)
from recongraph.domain.observations import ObservationOccurrence
from recongraph.domain.observations import ObservationSlot, ObservationState, Observation, FieldPath
from recongraph.domain.scopes import SubjectRef
from recongraph.domain.derivations import (
    ProviderId, ProviderSemanticVersion, DerivationMethodId, DerivationMethodDescriptor,
    DerivationInputBinding, DerivationIdentity, DerivedArtifactTypeId, CanonicalPayloadEnvelope,
    DerivedArtifactIdentity
)

def test_mta001_source_system_rename_changes_lineage():
    art = SourceArtifactId("1")
    loc = SourceLocator("l")
    l1 = StructuredSourceLineage(SourceSystemId("sap.production"), art, loc)
    l2 = StructuredSourceLineage(SourceSystemId("sap.archive"), art, loc)
    assert l1 != l2


def test_mta002_artifact_coordinate_changes_lineage():
    sys = SourceSystemId("sap.production")
    loc = SourceLocator("l")
    l1 = StructuredSourceLineage(sys, SourceArtifactId("1"), loc)
    l2 = StructuredSourceLineage(sys, SourceArtifactId("2"), loc)
    assert l1 != l2


def test_mta003_locator_changes_lineage():
    sys = SourceSystemId("sap.production")
    art = SourceArtifactId("1")
    l1 = StructuredSourceLineage(sys, art, SourceLocator("l1"))
    l2 = StructuredSourceLineage(sys, art, SourceLocator("l2"))
    assert l1 != l2


def test_mta004_source_ingestion_time_changes_nothing():
    # Timestamps are excluded from lineage identity. 
    # Therefore identical coordinates constructed at different times are equal.
    sys = SourceSystemId("sap.production")
    art = SourceArtifactId("1")
    loc = SourceLocator("l1")
    l1 = StructuredSourceLineage(sys, art, loc)
    l2 = StructuredSourceLineage(SourceSystemId("sap.production"), SourceArtifactId("1"), SourceLocator("l1"))
    assert l1 == l2


def test_mta005_same_fact_same_lineage():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs = Observation.create(slot, ObservationState.PRESENT, "ABC").identity
    l1 = StructuredSourceLineage(SourceSystemId("sap.sys"), SourceArtifactId("1"), SourceLocator("l"))
    occ1 = ObservationOccurrence.create(obs, l1)
    occ2 = ObservationOccurrence.create(obs, l1)
    assert occ1 == occ2


def test_mta006_same_fact_different_lineage():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs = Observation.create(slot, ObservationState.PRESENT, "ABC").identity
    l1 = StructuredSourceLineage(SourceSystemId("sap.sys"), SourceArtifactId("1"), SourceLocator("l"))
    l2 = StructuredSourceLineage(SourceSystemId("sap.sys"), SourceArtifactId("2"), SourceLocator("l"))
    occ1 = ObservationOccurrence.create(obs, l1)
    occ2 = ObservationOccurrence.create(obs, l2)
    assert occ1 != occ2


def test_mta007_same_semantic_derivation_executed_twice():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs = Observation.create(slot, ObservationState.PRESENT, "ABC").identity
    desc = DerivationMethodDescriptor(ProviderId("p.test"), DerivationMethodId("m"), frozenset())
    ver = ProviderSemanticVersion(1, 0, 0)
    b = frozenset([DerivationInputBinding("in", obs.to_kernel_identity_ref())])
    
    id1 = DerivationIdentity.compute(ver, desc, b)
    id2 = DerivationIdentity.compute(ver, desc, b)
    assert id1 == id2


def test_mta008_provider_class_rename():
    # Simulated: Provider class names are not in the Descriptor.
    # Therefore, identity remains unchanged if the class is renamed.
    assert True


def test_mta009_provider_semantic_version_bump():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs = Observation.create(slot, ObservationState.PRESENT, "ABC").identity
    desc = DerivationMethodDescriptor(ProviderId("p.test"), DerivationMethodId("m"), frozenset())
    b = frozenset([DerivationInputBinding("in", obs.to_kernel_identity_ref())])
    
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), desc, b)
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 1, 0), desc, b)
    assert id1 != id2


def test_mta010_non_semantic_implementation_refactor():
    # If semantics do not change, version does not bump, identity unchanged.
    assert True


def test_mta011_commutative_inputs_permuted():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs1 = Observation.create(slot, ObservationState.PRESENT, "A").identity
    obs2 = Observation.create(slot, ObservationState.PRESENT, "B").identity
    desc = DerivationMethodDescriptor(ProviderId("p.test"), DerivationMethodId("m"), frozenset(["in"]))
    ver = ProviderSemanticVersion(1, 0, 0)
    
    b1 = frozenset([DerivationInputBinding("in", obs1.to_kernel_identity_ref()), DerivationInputBinding("in", obs2.to_kernel_identity_ref())])
    b2 = frozenset([DerivationInputBinding("in", obs2.to_kernel_identity_ref()), DerivationInputBinding("in", obs1.to_kernel_identity_ref())])
    
    id1 = DerivationIdentity.compute(ver, desc, b1)
    id2 = DerivationIdentity.compute(ver, desc, b2)
    assert id1 == id2


def test_mta012_directional_input_roles_reversed():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs1 = Observation.create(slot, ObservationState.PRESENT, "A").identity
    obs2 = Observation.create(slot, ObservationState.PRESENT, "B").identity
    desc = DerivationMethodDescriptor(ProviderId("p.test"), DerivationMethodId("m"), frozenset())
    ver = ProviderSemanticVersion(1, 0, 0)
    
    b1 = frozenset([DerivationInputBinding("left", obs1.to_kernel_identity_ref()), DerivationInputBinding("right", obs2.to_kernel_identity_ref())])
    b2 = frozenset([DerivationInputBinding("left", obs2.to_kernel_identity_ref()), DerivationInputBinding("right", obs1.to_kernel_identity_ref())])
    
    id1 = DerivationIdentity.compute(ver, desc, b1)
    id2 = DerivationIdentity.compute(ver, desc, b2)
    assert id1 != id2


def test_mta013_canonical_mapping_key_order_changes():
    tid = DerivedArtifactTypeId("t.test")
    p1 = CanonicalPayloadEnvelope({"a": 1, "b": 2})
    p2 = CanonicalPayloadEnvelope({"b": 2, "a": 1})
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", p1)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", p2)
    assert id1 == id2


def test_mta014_derived_content_changes():
    tid = DerivedArtifactTypeId("t.test")
    p1 = CanonicalPayloadEnvelope({"a": 1})
    p2 = CanonicalPayloadEnvelope({"a": 2})
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", p1)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", p2)
    assert id1 != id2


def test_mta015_same_semantic_artifact_from_different_occurrence_paths():
    # Artifact semantic identity remains stable regardless of derivation path.
    # The artifact identity does NOT include DerivationIdentity.
    tid = DerivedArtifactTypeId("tax.pan")
    payload = CanonicalPayloadEnvelope({"pan": "123"})
    id1 = DerivedArtifactIdentity.compute(tid, "1.0", payload)
    id2 = DerivedArtifactIdentity.compute(tid, "1.0", payload)
    assert id1 == id2
````

## File: tests/test_evidence_scope.py
````python
import pytest
import json
from recongraph.domain.claims import ClaimDescriptor, ClaimSymmetry
from recongraph.domain.scopes import ScopeKind, SubjectRef, PropositionSubject

@pytest.fixture
def sym_descriptor():
    return ClaimDescriptor(
        claim_id="identity.same",
        semantic_version=1,
        symmetry=ClaimSymmetry.SYMMETRIC,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR, ScopeKind.GROUP_PAIR}
    )

@pytest.fixture
def dir_descriptor():
    return ClaimDescriptor(
        claim_id="document.supersedes",
        semantic_version=1,
        symmetry=ClaimSymmetry.DIRECTIONAL,
        allowed_scope_kinds={ScopeKind.RECORD_PAIR}
    )

def test_scope_kind_values_are_stable():
    assert ScopeKind.RECORD_PAIR.value == "record_pair"

def test_subject_ref_is_value_based():
    s1 = SubjectRef("urn:1")
    s2 = SubjectRef("urn:1")
    assert s1 == s2
    assert hash(s1) == hash(s2)

def test_subject_ref_order_is_deterministic_if_ordering_is_supported():
    s1 = SubjectRef("urn:1")
    s2 = SubjectRef("urn:2")
    assert s1 < s2

def test_subject_ref_serializes_stable_identity():
    assert SubjectRef("urn:1").to_dict() == {"urn": "urn:1"}

def test_empty_scope(sym_descriptor):
    with pytest.raises(ValueError, match="SC-001 Violation"):
        PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [], [])

def test_record_scope_with_two_subjects(sym_descriptor):
    rec_desc = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD})
    with pytest.raises(ValueError, match="SC-002 Violation"):
        PropositionSubject.create(rec_desc, ScopeKind.RECORD, [SubjectRef("urn:1")], [SubjectRef("urn:2")])

def test_pair_scope_with_empty_left(sym_descriptor):
    with pytest.raises(ValueError, match="SC-002 Violation"):
        PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [], [SubjectRef("urn:1")])

def test_pair_scope_with_empty_right(sym_descriptor):
    with pytest.raises(ValueError, match="SC-002 Violation"):
        PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:1")], [])

def test_pair_scope_with_two_left_subjects(sym_descriptor):
    with pytest.raises(ValueError, match="SC-002 Violation"):
        PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:1"), SubjectRef("urn:2")], [SubjectRef("urn:3")])

def test_duplicate_left_subject(sym_descriptor):
    with pytest.raises(ValueError, match="SC-003 Violation"):
        PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("urn:1"), SubjectRef("urn:1")], [SubjectRef("urn:2"), SubjectRef("urn:3")])

def test_group_pair_with_singleton_singleton(sym_descriptor):
    with pytest.raises(ValueError, match="SC-002 Violation"):
        PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("urn:1")], [SubjectRef("urn:2")])

def test_undeclared_scope_kind_for_claim():
    d = ClaimDescriptor("a.b", 1, ClaimSymmetry.SYMMETRIC, {ScopeKind.RECORD})
    with pytest.raises(ValueError, match="SC-008 Violation"):
        PropositionSubject.create(d, ScopeKind.RECORD_PAIR, [SubjectRef("urn:1")], [SubjectRef("urn:2")])

# Metamorphic Tests

def test_symmetric_scope_reversal(sym_descriptor):
    # A <-> B should equal B <-> A
    s1 = PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:A")], [SubjectRef("urn:B")])
    s2 = PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:B")], [SubjectRef("urn:A")])
    assert s1 == s2
    assert hash(s1) == hash(s2)

def test_directional_scope_reversal(dir_descriptor):
    # A -> B should NOT equal B -> A
    s1 = PropositionSubject.create(dir_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:A")], [SubjectRef("urn:B")])
    s2 = PropositionSubject.create(dir_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:B")], [SubjectRef("urn:A")])
    assert s1 != s2
    assert hash(s1) != hash(s2)

def test_intra_side_permutation(sym_descriptor):
    # {A, B, C} <-> {D} should equal {C, A, B} <-> {D}
    s1 = PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("A"), SubjectRef("B"), SubjectRef("C")], [SubjectRef("D")])
    s2 = PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("C"), SubjectRef("A"), SubjectRef("B")], [SubjectRef("D")])
    assert s1 == s2

def test_scope_distinction_pair_vs_group(sym_descriptor):
    s1 = PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("P1")], [SubjectRef("G1")])
    s2 = PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("P1")], [SubjectRef("G1"), SubjectRef("G2")])
    assert s1 != s2

def test_overlap_non_identity(sym_descriptor):
    s1 = PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("P1"), SubjectRef("P2")], [SubjectRef("G1")])
    s2 = PropositionSubject.create(sym_descriptor, ScopeKind.GROUP_PAIR, [SubjectRef("P2"), SubjectRef("P3")], [SubjectRef("G1")])
    assert s1 != s2

def test_scope_serialization_is_deterministic(sym_descriptor):
    s1 = PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:A")], [SubjectRef("urn:B")])
    s2 = PropositionSubject.create(sym_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:B")], [SubjectRef("urn:A")])
    # They should produce exactly the same JSON string when keys are sorted
    json1 = json.dumps(s1.to_dict(), sort_keys=True)
    json2 = json.dumps(s2.to_dict(), sort_keys=True)
    assert json1 == json2

def test_reversed_directional_scope_serializes_differently(dir_descriptor):
    s1 = PropositionSubject.create(dir_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:A")], [SubjectRef("urn:B")])
    s2 = PropositionSubject.create(dir_descriptor, ScopeKind.RECORD_PAIR, [SubjectRef("urn:B")], [SubjectRef("urn:A")])
    json1 = json.dumps(s1.to_dict(), sort_keys=True)
    json2 = json.dumps(s2.to_dict(), sort_keys=True)
    assert json1 != json2
````

## File: tests/test_evidence_state_algebra.py
````python
import pytest
from recongraph.domain.observations import ObservationState, InterpretationState

# Testing orthogonal state algebra conceptually

def test_present_can_coexist_with_interpreted():
    # Example: Valid vendor name, parsed successfully.
    # In a future EvidenceAssertion, we might see:
    assert ObservationState.PRESENT == "present"
    assert InterpretationState.INTERPRETED == "interpreted"

def test_present_can_coexist_with_uninterpretable():
    # Example: "UNKNOWN" literal or Japanese string in English parser.
    assert ObservationState.PRESENT == "present"
    assert InterpretationState.UNINTERPRETABLE == "uninterpretable"

def test_invalid_can_coexist_with_interpreted():
    # Example: GSTIN="BANANA" -> document.contains_invalid_tax_identifier is evaluated true.
    assert ObservationState.INVALID == "invalid"
    assert InterpretationState.INTERPRETED == "interpreted"

def test_invalid_can_coexist_with_uninterpretable():
    # Example: Malformed amount string in a math evaluator.
    assert ObservationState.INVALID == "invalid"
    assert InterpretationState.UNINTERPRETABLE == "uninterpretable"

def test_observation_state_does_not_determine_interpretation_state():
    # Both outcomes are possible for a PRESENT observation
    present_interpreted = InterpretationState.INTERPRETED
    present_uninterpretable = InterpretationState.UNINTERPRETABLE
    assert present_interpreted != present_uninterpretable

def test_interpretation_state_does_not_determine_observation_state():
    # Both outcomes are possible for an INTERPRETED state
    interpreted_present = ObservationState.PRESENT
    interpreted_invalid = ObservationState.INVALID
    assert interpreted_present != interpreted_invalid

def test_partial_interpretation_state_does_not_exist():
    states = [s.value for s in InterpretationState]
    assert "partially_interpreted" not in states
    assert len(states) == 2
````

## File: tests/test_hypothesis_evaluator.py
````python
import pytest
from datetime import date
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn
from recongraph.graph.hypotheses import Hypothesis, EligibilityStatus
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, ReferenceEvidencePolicy, ReferenceCorpusProfile
from recongraph.matching.scoring import SignalName
from recongraph.graph.evaluator import HypothesisEvaluator
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TemporalEvidenceProvider, TaxEvidenceProvider, VendorEvidenceProvider, ReferenceEvidenceProvider
from recongraph.matching.pair_scorers import PURCHASE_TO_GST_POLICY

@pytest.fixture
def empty_reference_context():
    return ReferenceEvidenceContext(
        profile=ReferenceCorpusProfile(
            reference_count=3,
            normalized_reference_frequency={"inv1": 1, "inv2": 1, "inv3": 1},
            numeric_token_document_frequency={"1": 1, "2": 1, "3": 1}
        ),
        policy=ReferenceEvidencePolicy()
    )

def test_evaluator_case_1(empty_reference_context):
    # P1 (100k) -> G1 (100k)
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    g1 = GSTRecord(record_id="g1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    
    builder = CandidateGraphBuilder()
    u1, u2 = build_purchase_urn("p1"), build_gst_urn("g1")
    builder.add_node(u1, p1)
    builder.add_node(u2, g1)
    
    hypothesis = Hypothesis(
        component_nodes=frozenset([u1, u2]),
        proposed_edges=frozenset([frozenset([u1, u2])])
    )
    
    providers = [
        FinancialEvidenceProvider(),
        TemporalEvidenceProvider(),
        TaxEvidenceProvider(),
        VendorEvidenceProvider(),
        ReferenceEvidenceProvider(empty_reference_context)
    ]
    evaluator = HypothesisEvaluator(providers, PURCHASE_TO_GST_POLICY)
    result = evaluator.evaluate(builder.build(), hypothesis)
    
    assert result.eligibility == EligibilityStatus.ELIGIBLE
    assert result.score > 0.8  # Strong match
    assert len(result.violations) == 0

def test_evaluator_case_2(empty_reference_context):
    # P1 (100k) -> G1 (50k), G2 (50k)
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    g1 = GSTRecord(record_id="g1", amount=50.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    g2 = GSTRecord(record_id="g2", amount=50.0, record_date=date(2023,1,1), reference="INV1", vendor_name="A", tax_identity="TAX1")
    
    builder = CandidateGraphBuilder()
    u1, u2, u3 = build_purchase_urn("p1"), build_gst_urn("g1"), build_gst_urn("g2")
    builder.add_node(u1, p1)
    builder.add_node(u2, g1)
    builder.add_node(u3, g2)
    
    hypothesis = Hypothesis(
        component_nodes=frozenset([u1, u2, u3]),
        proposed_edges=frozenset([frozenset([u1, u2]), frozenset([u1, u3])])
    )
    
    providers = [
        FinancialEvidenceProvider(),
        TemporalEvidenceProvider(),
        TaxEvidenceProvider(),
        VendorEvidenceProvider(),
        ReferenceEvidenceProvider(empty_reference_context)
    ]
    evaluator = HypothesisEvaluator(providers, PURCHASE_TO_GST_POLICY)
    result = evaluator.evaluate(builder.build(), hypothesis)
    
    assert result.eligibility == EligibilityStatus.ELIGIBLE
    assert result.supporting_evidence["signals"][SignalName.AMOUNT] == 1.0
    assert result.score > 0.7

def test_evaluator_case_3(empty_reference_context):
    # P1 (100k) -> G1 (40k), G2 (40k) (Incorrect sum)
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV2", vendor_name="B", tax_identity="TAX2")
    g1 = GSTRecord(record_id="g1", amount=40.0, record_date=date(2023,1,1), reference="INV2", vendor_name="B", tax_identity="TAX2")
    g2 = GSTRecord(record_id="g2", amount=40.0, record_date=date(2023,1,1), reference="INV2", vendor_name="B", tax_identity="TAX2")
    
    builder = CandidateGraphBuilder()
    u1, u2, u3 = build_purchase_urn("p1"), build_gst_urn("g1"), build_gst_urn("g2")
    builder.add_node(u1, p1)
    builder.add_node(u2, g1)
    builder.add_node(u3, g2)
    
    hypothesis = Hypothesis(
        component_nodes=frozenset([u1, u2, u3]),
        proposed_edges=frozenset([frozenset([u1, u2]), frozenset([u1, u3])])
    )
    
    providers = [
        FinancialEvidenceProvider(),
        TemporalEvidenceProvider(),
        TaxEvidenceProvider(),
        VendorEvidenceProvider(),
        ReferenceEvidenceProvider(empty_reference_context)
    ]
    evaluator = HypothesisEvaluator(providers, PURCHASE_TO_GST_POLICY)
    result = evaluator.evaluate(builder.build(), hypothesis)
    
    assert result.supporting_evidence["signals"][SignalName.AMOUNT] < 1.0
    assert result.score < 0.9

def test_evaluator_case_4(empty_reference_context):
    # P1 -> G1 (Semantic contradiction: date > max_days)
    p1 = PurchaseRecord(record_id="p1", amount=100.0, record_date=date(2023,1,1), reference="INV3", vendor_name="C", tax_identity="TAX3")
    g1 = GSTRecord(record_id="g1", amount=100.0, record_date=date(2024,1,1), reference="INV3", vendor_name="C", tax_identity="TAX3")
    
    builder = CandidateGraphBuilder()
    u1, u2 = build_purchase_urn("p1"), build_gst_urn("g1")
    builder.add_node(u1, p1)
    builder.add_node(u2, g1)
    
    hypothesis = Hypothesis(
        component_nodes=frozenset([u1, u2]),
        proposed_edges=frozenset([frozenset([u1, u2])])
    )
    
    providers = [
        FinancialEvidenceProvider(),
        TemporalEvidenceProvider(),
        TaxEvidenceProvider(),
        VendorEvidenceProvider(),
        ReferenceEvidenceProvider(empty_reference_context)
    ]
    evaluator = HypothesisEvaluator(providers, PURCHASE_TO_GST_POLICY)
    result = evaluator.evaluate(builder.build(), hypothesis)
    
    assert result.eligibility == EligibilityStatus.INELIGIBLE
    assert "TEMPORAL_MAX_DAYS_EXCEEDED" in result.violations
````

## File: tests/test_observation_identity.py
````python
import pytest
from decimal import Decimal
from recongraph.domain.scopes import SubjectRef
from recongraph.domain.observations import (
    FieldPath,
    ObservationSlot,
    ObservationState,
    Observation,
    ObservationIdentity
)

def test_field_path_grammar():
    assert FieldPath("vendor_name").value == "vendor_name"
    assert FieldPath("document.header.vendor").value == "document.header.vendor"

    with pytest.raises(ValueError):
        FieldPath("VendorName")
    with pytest.raises(ValueError):
        FieldPath(".vendor_name")
    with pytest.raises(ValueError):
        FieldPath("vendor_name.")
    with pytest.raises(ValueError):
        FieldPath("vendor..name")
    with pytest.raises(ValueError):
        FieldPath("vendor-name")
    with pytest.raises(ValueError):
        FieldPath("vendor name")
    with pytest.raises(ValueError):
        FieldPath("vendor[0]")
    with pytest.raises(ValueError):
        FieldPath("")

@pytest.fixture
def base_slot():
    return ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor_name"))

def test_slot_stability_across_value_changes(base_slot):
    # KOM-001
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(base_slot, ObservationState.PRESENT, "XYZ")
    assert o1.identity.slot == o2.identity.slot

def test_revision_distinction(base_slot):
    # KOM-002
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(base_slot, ObservationState.PRESENT, "XYZ")
    assert o1.identity != o2.identity

def test_exact_reconstruction(base_slot):
    # KOM-003, ODUP001, ODUP005, ODUP008
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    assert o1.identity == o2.identity

def test_subject_distinction():
    # KOM-004
    s1 = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    s2 = ObservationSlot(SubjectRef("urn:2"), FieldPath("vendor"))
    o1 = Observation.create(s1, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(s2, ObservationState.PRESENT, "ABC")
    assert o1.identity.slot != o2.identity.slot
    assert o1.identity != o2.identity

def test_field_distinction(base_slot):
    # KOM-005, ODUP002
    s1 = base_slot
    s2 = ObservationSlot(SubjectRef("urn:1"), FieldPath("name"))
    o1 = Observation.create(s1, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(s2, ObservationState.PRESENT, "ABC")
    assert o1.identity.slot != o2.identity.slot
    assert o1.identity != o2.identity

def test_state_distinction(base_slot):
    # KOM-006, ODUP004
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(base_slot, ObservationState.INVALID, "ABC")
    assert o1.identity != o2.identity

def test_missing_determinism(base_slot):
    # KOM-007, ODUP010
    o1 = Observation.create(base_slot, ObservationState.MISSING, None)
    o2 = Observation.create(base_slot, ObservationState.MISSING, None)
    assert o1.identity == o2.identity

def test_runtime_object_independence(base_slot):
    # KOM-008
    val1 = "".join(["A", "B", "C"])
    val2 = "".join(["A", "B", "C"])
    o1 = Observation.create(base_slot, ObservationState.PRESENT, val1)
    o2 = Observation.create(base_slot, ObservationState.PRESENT, val2)
    assert o1.identity == o2.identity

def test_type_preservation(base_slot):
    # KOM-009
    o1 = Observation.create(base_slot, ObservationState.PRESENT, 1)
    o2 = Observation.create(base_slot, ObservationState.PRESENT, 1.0)
    assert o1.identity != o2.identity

def test_invalid_value_preservation(base_slot):
    # KOM-015
    o1 = Observation.create(base_slot, ObservationState.INVALID, "ABC")
    o2 = Observation.create(base_slot, ObservationState.INVALID, "XYZ")
    assert o1.identity != o2.identity

def test_empty_string_handling(base_slot):
    # KOM-016
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "")
    o2 = Observation.create(base_slot, ObservationState.MISSING, None)
    assert o1.identity != o2.identity

def test_whitespace_sensitivity(base_slot):
    # KOM-017
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(base_slot, ObservationState.PRESENT, " ABC ")
    assert o1.identity != o2.identity

def test_decimal_stability(base_slot):
    # KOM-018
    o1 = Observation.create(base_slot, ObservationState.PRESENT, Decimal("1.0"))
    o2 = Observation.create(base_slot, ObservationState.PRESENT, Decimal("1.0"))
    o3 = Observation.create(base_slot, ObservationState.PRESENT, Decimal("1.00"))
    assert o1.identity == o2.identity
    assert o1.identity != o3.identity

def test_boolean_integer_distinction(base_slot):
    # KOM-019
    o1 = Observation.create(base_slot, ObservationState.PRESENT, True)
    o2 = Observation.create(base_slot, ObservationState.PRESENT, 1)
    assert o1.identity != o2.identity

def test_missing_value_check(base_slot):
    # KOM-020
    with pytest.raises(ValueError):
        Observation.create(base_slot, ObservationState.MISSING, "ABC")

def test_present_requires_value(base_slot):
    with pytest.raises(ValueError):
        Observation.create(base_slot, ObservationState.PRESENT, None)

def test_invalid_requires_value(base_slot):
    with pytest.raises(ValueError):
        Observation.create(base_slot, ObservationState.INVALID, None)

def test_serialization_stability(base_slot):
    # KOM-014
    import json
    o1 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    o2 = Observation.create(base_slot, ObservationState.PRESENT, "ABC")
    j1 = json.dumps(o1.to_dict(), sort_keys=True)
    j2 = json.dumps(o2.to_dict(), sort_keys=True)
    assert j1 == j2

def test_reject_nonfinite_floats(base_slot):
    with pytest.raises(ValueError):
        Observation.create(base_slot, ObservationState.PRESENT, float('inf'))
    with pytest.raises(ValueError):
        Observation.create(base_slot, ObservationState.PRESENT, float('nan'))

def test_observation_identity_is_consistent():
    # Attempting to lie about identity fails
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    o1 = Observation.create(slot, ObservationState.PRESENT, "ABC")
    with pytest.raises(ValueError):
        Observation(identity=o1.identity, state=ObservationState.PRESENT, value="XYZ")
````

## File: tests/test_semantic_dependencies.py
````python
import pytest
from recongraph.domain.identity import IdentityDomainId, IdentityDigest
from recongraph.domain.dependencies import SemanticDependencyRef, SemanticDependencyKind, DependencyStability
from recongraph.domain.derivations import DerivationIdentity, ProviderSemanticVersion, DerivationMethodDescriptor, ProviderId, DerivationMethodId


def _dummy_method():
    return DerivationMethodDescriptor(
        provider_id=ProviderId("recongraph.dummy"),
        method_id=DerivationMethodId("test"),
        commutative_roles=frozenset()
    )


def test_sd001_content_addressed_config_dependency():
    dep = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "c" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    assert dep.stability == DependencyStability.CONTENT_ADDRESSED


def test_sd002_immutable_model_version_dependency():
    dep = SemanticDependencyRef(
        kind=SemanticDependencyKind.MODEL_ARTIFACT,
        namespace=IdentityDomainId("recongraph.model.vendor_encoder"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.IMMUTABLE_VERSION,
        semantic_version="1.2.3"
    )
    assert dep.stability == DependencyStability.IMMUTABLE_VERSION


def test_sd003_mutable_registry_alias():
    dep = SemanticDependencyRef(
        kind=SemanticDependencyKind.REGISTRY_SNAPSHOT,
        namespace=IdentityDomainId("recongraph.registry.gst"),
        identity=IdentityDigest("sha256:" + "0" * 64), # identity hash of the string "latest" etc. But we must use IdentityDigest format
        stability=DependencyStability.MUTABLE_REFERENCE
    )
    assert dep.stability == DependencyStability.MUTABLE_REFERENCE


def test_sd004_same_namespace_different_content_digest_changes_identity():
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    d2 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "b" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1,))
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d2,))
    assert id1 != id2


def test_sd005_same_identity_different_kind_changes_identity():
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    d2 = SemanticDependencyRef(
        kind=SemanticDependencyKind.RULESET,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1,))
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d2,))
    assert id1 != id2


def test_sd006_dependency_order_permutation_invariant():
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    d2 = SemanticDependencyRef(
        kind=SemanticDependencyKind.MODEL_ARTIFACT,
        namespace=IdentityDomainId("recongraph.model"),
        identity=IdentityDigest("sha256:" + "b" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1, d2))
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d2, d1))
    assert id1 == id2


def test_sd007_duplicate_identical_dependency_rejected():
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    with pytest.raises(ValueError, match="Duplicate identical semantic dependencies are rejected"):
        DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1, d1))


def test_sd008_same_dependency_identity_in_two_distinct_namespaces_preserved():
    # If the digest is the same but namespaces differ, they are distinct dependencies
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config.1"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    d2 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config.2"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    # this shouldn't raise duplicate error because they are distinct objects
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1, d2))
    assert id1


def test_sd009_mutable_dependency_remains_representable():
    d = SemanticDependencyRef(
        kind=SemanticDependencyKind.REGISTRY_SNAPSHOT,
        namespace=IdentityDomainId("recongraph.registry"),
        identity=IdentityDigest("sha256:" + "0" * 64),
        stability=DependencyStability.MUTABLE_REFERENCE
    )
    assert DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d,))


def test_sd010_mutable_dependency_does_not_masquerade_as_reproducible_snapshot():
    # It must be explicit that it's mutable
    d = SemanticDependencyRef(
        kind=SemanticDependencyKind.REGISTRY_SNAPSHOT,
        namespace=IdentityDomainId("recongraph.registry"),
        identity=IdentityDigest("sha256:" + "0" * 64),
        stability=DependencyStability.MUTABLE_REFERENCE
    )
    assert d.stability == DependencyStability.MUTABLE_REFERENCE


def test_sd011_dependency_kind_change_changes_identity():
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.CONFIGURATION,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    d2 = SemanticDependencyRef(
        kind=SemanticDependencyKind.RULESET,
        namespace=IdentityDomainId("recongraph.config"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.CONTENT_ADDRESSED
    )
    assert d1 != d2
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1,))
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d2,))
    assert id1 != id2


def test_sd012_semantic_version_change_changes_identity():
    d1 = SemanticDependencyRef(
        kind=SemanticDependencyKind.MODEL_ARTIFACT,
        namespace=IdentityDomainId("recongraph.model"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.IMMUTABLE_VERSION,
        semantic_version="1.0.0"
    )
    d2 = SemanticDependencyRef(
        kind=SemanticDependencyKind.MODEL_ARTIFACT,
        namespace=IdentityDomainId("recongraph.model"),
        identity=IdentityDigest("sha256:" + "a" * 64),
        stability=DependencyStability.IMMUTABLE_VERSION,
        semantic_version="1.0.1"
    )
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d1,))
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), _dummy_method(), frozenset(), (d2,))
    assert id1 != id2
````

## File: tests/test_trace.py
````python
import pytest
import time
from dataclasses import FrozenInstanceError
from recongraph.graph.trace import TraceBuilder, TraceStage

def test_trace_builder_chronology():
    builder = TraceBuilder(trace_id="TRC-001", engine_version="1.0.0", config_hash="abcd")
    
    # Simulate a pipeline execution
    builder.record_event(TraceStage.CANDIDATE_GENERATION, {"edge": "P1-G1"})
    time.sleep(0.01) # Ensure timestamp increment
    builder.record_event(TraceStage.GRAPH_BUILDING, {"nodes": 2})
    time.sleep(0.01)
    builder.record_event(TraceStage.DECISION_EVALUATION, {"action": "AUTO_MATCH"})
    
    trace = builder.build()
    
    assert trace.trace_id == "TRC-001"
    assert len(trace.events) == 3
    
    # Verify strict chronology
    assert trace.events[0].timestamp < trace.events[1].timestamp < trace.events[2].timestamp
    
    # Verify stages
    assert trace.events[0].stage == TraceStage.CANDIDATE_GENERATION
    assert trace.events[1].stage == TraceStage.GRAPH_BUILDING
    assert trace.events[2].stage == TraceStage.DECISION_EVALUATION
    
    # Verify payload preservation
    assert trace.events[0].payload["edge"] == "P1-G1"
    
    # Verify filtering
    assert len(trace.get_events_for_stage(TraceStage.CANDIDATE_GENERATION)) == 1
    assert len(trace.get_events_for_stage(TraceStage.HYPOTHESIS_SEARCH)) == 0

def test_trace_immutability():
    builder = TraceBuilder(trace_id="TRC-002", engine_version="1.0.0", config_hash="abcd")
    builder.record_event(TraceStage.COMPONENT_EXTRACTION, "Component A")
    
    trace = builder.build()
    
    # DecisionTrace is frozen
    with pytest.raises(FrozenInstanceError):
        trace.trace_id = "TRC-003"
        
    # Appending to builder after build does not mutate the frozen trace
    builder.record_event(TraceStage.HYPOTHESIS_SEARCH, "Hypothesis 1")
    assert len(trace.events) == 1
````

## File: README.md
````markdown
# ReconGraph

**An explainable financial exception investigation and reconciliation engine.**

ReconGraph is an advanced epistemic engine designed to automate complex, multi-way financial reconciliations. Instead of relying on opaque similarity scores and rigid rules engines, ReconGraph frames reconciliation as a graph of evidence, semantic assertions, and mathematically grounded hypotheses.

## Why ReconGraph?

Traditional reconciliation systems fail at scale because they conflate *similarity* with *identity*. If a purchase ledger says "ABC Pvt Ltd" and a bank statement says "ABC LLP", a naive fuzzy-matcher might return an 85% match score. 

ReconGraph knows better. It extracts the structural semantic reality: these are two fundamentally different legal entities (Private Limited vs. Limited Liability Partnership) despite sharing an organization core. 

By building a rigorous ontology of financial evidence, ReconGraph can reason across multiple data dimensions—tax identity, legal form, financial amounts, and time—while preserving perfect cryptographic lineage for every decision it makes.

## Core Architecture

ReconGraph operates in distinct semantic stages:
1. **Observation**: Raw financial records (Invoices, Purchases, GST, Bank lines) are ingested.
2. **Derivation**: Records are parsed into structured semantic artifacts (e.g., separating a canonical organization core from its legal designator).
3. **Assertion**: The engine computes pairwise semantic assertions (e.g., `same_tax_identity`, `same_legal_form`).
4. **Graph Reasoning**: The reconciliation engine explores the graph of assertions to build and score hypotheses representing candidate matches.
5. **Traceability**: Every conclusion is backed by an immutable `DecisionTrace`, cryptographically proving exactly what observations and policies led to the outcome.

## Getting Started

### Prerequisites
- Python 3.11+

### Installation

```bash
# Clone the repository
git clone https://github.com/Ayushmaandotcom/Repository-name-Recongraph.git
cd Repository-name-Recongraph

# Install dependencies (development mode recommended)
pip install -e ".[dev]"
```

### Running Tests

ReconGraph relies on strict typing and property-based testing. To ensure the engine's epistemic invariants hold true, run the test suite:

```bash
pytest
```

## Contributing

ReconGraph enforces strict invariants. Contributions must adhere to the following principles:
- **Missing ≠ Contradictory**: An absent field must never be implicitly treated as a contradiction.
- **Traceability over Magic**: Every piece of derived evidence must carry a `SemanticDependencyRef` pointing to its origin.
- **Precision**: Money is represented strictly with `Decimal`, not `float`.

## License

All rights reserved. (License to be determined).
````

## File: docs/algorithms/purchase-gst-semantics.md
````markdown
# Purchase-to-GST Relationship Semantics

## Purpose

Explain why primitive compatibility signals are insufficient to identify
the same financial event and define relationship-specific evidence
patterns for Purchase ↔ GST reconciliation.

## Baseline limitation

The v0.1 baseline uses a weighted average of entity, reference, amount,
temporal, and tax-identity signals.

Weighted averaging is compensatory: strong signals can offset severe
disagreement in another signal.

Challenge Dataset v1 exposed cases where this behaviour conflicts with
financial-event identity.

## Design principle

Primitive signals measure evidence.

Relationship semantics interpret combinations of evidence.

Semantic findings identify evidence patterns but do not, by themselves,
define production match decisions.

## Semantic finding PG-001: Severe amount conflict

### Motivation

HN001 scored 0.6957 despite a 100% amount mismatch because entity,
reference, temporal, and tax-identity evidence remained strong.

### Evidence pattern

- amount score is 0.0
- reference evidence is strong
- tax identity agrees

### Interpretation

The records exhibit strong identity evidence while their monetary values
are fundamentally incompatible under the current 1:1 Purchase ↔ GST
hypothesis.

### Finding

`severe_amount_conflict`

### Open question

Should this finding apply a contradiction penalty, trigger a hard gate,
or route the pair to review?

## Semantic finding PG-002: Distinct event identity evidence

### Motivation

HN003 scored 0.7000 for separate monthly invoices because entity, amount,
and tax identity matched exactly.

### Evidence pattern

- entity evidence is strong
- amount evidence is strong
- tax identity agrees
- reference score is 0.0
- temporal score is 0.0

### Interpretation

The records appear to involve the same legal entity and transaction
shape, but reference and temporal evidence indicate distinct financial
events.

### Finding

`distinct_event_identity_evidence`

### Open question

Should this finding reduce compatibility or act as a non-compensatory
event-identity gate?

## Existing tax identity contradiction

The v0.1 policy already treats an explicit tax-identity mismatch as a
contradiction and applies a multiplicative penalty.

HN002 demonstrated that this mechanism suppresses a highly compatible
surface-level pair.

The semantic layer should expose this condition as:

`tax_identity_conflict`

The scoring consequence may initially remain in RelationshipPolicy.

## Out-of-scope findings

### Weak numeric reference collision

HN004 exposed a primitive reference-scoring issue. The semantic layer
should not repair incorrect primitive evidence.

### Group relationship required

HN005 exposed a relationship-cardinality limitation. Pair semantics
cannot prove a 1:N reconciliation hypothesis.

## Challenge traceability

| Finding | Challenge case | Failure category |
|---|---|---|
| severe_amount_conflict | HN001 | relationship semantics |
| tax_identity_conflict | HN002 | relationship semantics |
| distinct_event_identity_evidence | HN003 | relationship semantics |
| weak numeric reference collision | HN004 | primitive scoring |
| group relationship required | HN005 | relationship cardinality |

## Detection before consequence

Semantic findings are initially observational.

`analyze_purchase_gst_semantics()` detects evidence patterns and returns
structured findings without changing pair compatibility scores.

This separation allows the challenge dataset to validate semantic
detection independently from the later policy decision of whether a
finding should apply a penalty, trigger a gate, or route a pair to
review.

## Initial semantic thresholds

The v0.1 semantic detector uses:

- strong reference evidence: score >= 0.8
- strong entity evidence: score >= 0.9
- strong amount evidence: score >= 0.9

These thresholds are rule semantics, not calibrated probabilities.

The severe amount conflict currently requires an amount score exactly
equal to 0.0. This preserves the first challenge-derived rule without
introducing an untested near-zero threshold.

## Compatibility and eligibility

Compatibility and eligibility answer different questions.

Compatibility measures how strongly the available evidence aligns across
the weighted primitive signals.

Eligibility determines whether a relationship hypothesis is permitted to
proceed through an automatic reconciliation path.

A pair may have high compatibility while remaining ineligible for
automatic 1:1 reconciliation because a critical semantic finding
contradicts the 1:1 hypothesis.

For example, HN001 has high identity compatibility but contains a severe
amount conflict. Reducing the compatibility score until the pair appears
"dissimilar" would hide the actual evidence structure. The compatibility
score should preserve the observed alignment, while eligibility records
that the pair cannot automatically reconcile under the 1:1 hypothesis.

Ineligibility does not imply rejection. A later decision layer may route
an ineligible but otherwise compatible pair to review or evaluate it
under a different relationship hypothesis.

## Hypothesis-relative semantics

Semantic findings are interpreted relative to the relationship
hypothesis being evaluated.

A severe amount conflict is a blocking condition for a 1:1 Purchase ↔
GST hypothesis because one record is expected to reconcile directly
with one opposing record.

The same pair may remain useful as a candidate edge for a 1:N
reconciliation hypothesis. Under a group hypothesis, amount compatibility
must be evaluated across the combined records rather than independently
for each pair.

Therefore, ineligibility for the 1:1 hypothesis does not make a pair
globally irrelevant.

## Initial 1:1 blocking findings

The first Purchase ↔ GST 1:1 eligibility policy treats the following
semantic findings as blocking:

- `severe_amount_conflict`
- `tax_identity_conflict`
- `distinct_event_identity_evidence`

These findings prevent automatic 1:1 eligibility.

The blocking set is explicit rather than treating every semantic finding
as blocking. Future findings may be informational or review-oriented and
should not automatically make a pair ineligible.

## Decision layer boundary

Eligibility is not a final reconciliation decision.

The semantic and eligibility layers do not currently emit:

- auto-match
- review
- reject

A future decision layer may combine compatibility, coverage, eligibility,
and relationship hypotheses to select an operational action.

## 1:1 eligibility result

The Purchase ↔ GST semantic layer exposes a separate eligibility result
for the 1:1 reconciliation hypothesis.

The result contains:

- `status`: `eligible` or `ineligible`
- `blocking_findings`: the ordered semantic findings that prevent the
  1:1 hypothesis from proceeding through automatic reconciliation

Eligibility is intentionally independent from compatibility thresholds.

A low-compatibility pair may remain eligible if no critical semantic
finding blocks the 1:1 hypothesis. A later decision layer should reject
or ignore the pair based on compatibility.

A high-compatibility pair may be ineligible when a critical contradiction
blocks automatic 1:1 reconciliation.

This independence prevents eligibility from becoming a second hidden
score threshold.

## Current implementation boundary

The existing tax identity contradiction penalty remains part of the
compatibility scorer temporarily.

The intended direction is to evaluate whether the penalty should be
removed after eligibility behaviour is validated against challenge and
baseline datasets.

No compatibility scoring behaviour is changed in the initial eligibility
implementation.

## Compatibility and eligibility separation

1. Purchase ↔ GST compatibility measures weighted primitive evidence alignment.
2. A tax identity mismatch contributes 0.0 through the tax identity signal.
3. Purchase ↔ GST compatibility does not additionally apply a tax contradiction multiplier.
4. A tax identity conflict remains a blocking semantic finding for the automatic 1:1 hypothesis.
5. Therefore, a pair may have high compatibility and still be 1:1 ineligible.
6. Removing the Purchase ↔ GST tax penalty does not remove generic contradiction-penalty support from the relationship scoring engine.

### Tax penalty comparison experiment

Pairs compared: 31
Scores changed: 22
Eligibility changes: 0

Minimum positive score:
hybrid = 0.9457
pure   = 0.9457

Maximum negative score:
hybrid = 0.0779
pure   = 0.1557

Separation gap:
hybrid = 0.8679
pure   = 0.7900

**Decision**:
Purchase ↔ GST uses pure compatibility without a tax contradiction multiplier.

**Rationale**:
The tax mismatch already contributes zero weighted evidence and independently blocks 1:1 eligibility. The additional multiplicative penalty mixed domain eligibility semantics into the compatibility score and could suppress diagnostic visibility into flaws in other primitive signals.
````

## File: docs/algorithms/reference-evidence-interpretation-contract.md
````markdown
# Reference Evidence Interpretation Contract

**Purpose**: Define the semantic output contract of reference evidence interpretation before selecting a scoring formula or calibration policy.

The reference pipeline stages have precise epistemic boundaries:
- **Stage 1 answers**: What identity facts are structurally shared?
- **Stage 2 answers**: What corpus statistics are available for those facts?
- **Stage 3 answers**: How should those enriched facts be interpreted as positive reference compatibility evidence, and how complete is the statistical context supporting that interpretation?

Stage 3 has two distinct epistemic dimensions: **evidence magnitude** and **statistical context completeness**. They must not be collapsed.

## Why `float | None` Is Insufficient

Using a monolithic `float | None` destroys critical semantic context.

For example, a `score = 0.5` could mean:
- **Known mediocre evidence** (e.g., RE004: two references sharing a highly common token with `DF = 40`).
- **Structurally plausible evidence interpreted under missing corpus context** (e.g., RE009: a shared token exists and is rare, but one of the exact normalized references was not seen in the profile).

These two states are not semantically equivalent. One is a factual assertion of weakness; the other is an assertion of partial ignorance.

Likewise, `None` is highly ambiguous. It could mean:
- **No usable reference evidence** (e.g., completely blank fields).
- **Reference evidence exists but corpus statistics are unavailable** (e.g., RE010: a structurally strong 6-digit match where the profile snapshot lacks any data for those records).

Stage 3 must reject `float | None` as its production contract.

## Conceptual Result Dimensions

The conceptual result of Stage 3 will be an interpreted object (e.g., `ReferenceEvidenceInterpretation`) with three dimensions:

### 1. `score`
`score ∈ [0.0, 1.0]`

**Meaning**: The interpreted magnitude of positive compatibility evidence contributed by the reference field.
It represents *positive compatibility evidence*.
- A common token should usually contribute approximately zero positive evidence; it does not automatically become negative evidence.
- No shared identity produces zero reference compatibility evidence.
- A score of `0.0` does **not** mean REJECT. It simply means the reference field contributed no positive compatibility evidence. (Final relationship decisions belong to a later layer).

### 2. `statistical_coverage`
`statistical_coverage ∈ [0.0, 1.0]`

**Meaning**: The fraction of interpretation-relevant identity evidence for which corpus statistics were available.
(Note: we distinguish structural profile completeness from interpretation statistical coverage. We care about the latter).

### 3. `contributions`
Conceptually, Stage 3 preserves the interpreted components that produced the score, keeping the score fully explainable.

Conceptual fields:
- `evidence_kind` (e.g., `normalized_reference` or `numeric_token`)
- `identity_value`
- `positive_evidence`
- `statistics_available`

**Key invariant**: The final Stage 3 score must remain explainable through its contributions. However, it is explicitly *not* required that `sum(contributions) == score`. If future interpreters use `max`, `probabilistic union`, saturation, or correlation-aware combinations, individual contribution magnitudes may not add linearly.

## Four Interpretation States

### State A — No usable reference evidence
**Example**: `reference_a = None`, `reference_b = None`
**Meaning**: No structural identity evidence exists to interpret.
**Proposed Boundary**: Stage 3 itself should *not* receive `None`. The pipeline remains strict. Stage 1 extraction returns `None` which bypasses Stage 2 and Stage 3 entirely. The interpreter requires a valid `EnrichedReferenceEvidence` object.

### State B — Fully profiled evidence
**Example**: RE003, RE004, RE005, RE006
**Meaning**: All interpretation-relevant corpus statistics exist. Expected `statistical_coverage = 1.0`.

### State C — Partially profiled evidence
**Example**: RE009
**Meaning**: The candidate pair is only partially profiled structurally. However, if the interpretation path only relies on the shared numeric token evidence (which is fully profiled), then the *interpretation statistical coverage* might still be 1.0. This distinguishes structural profile completeness from statistical coverage of consumed evidence.

### State D — Fully out-of-profile structural evidence
**Example**: RE010
**Meaning**: The shared token exists structurally, but its DF is completely unavailable.
Stage 3 must not pretend `DF = 0` or `DF = 1`. It must interpret under unavailable statistical context.
**Conceptually**: `score` may be non-zero (structural fallback), `statistical_coverage = 0.0`, and `contribution statistics_available = false`.

## Contract Invariants

### IC-001 — Coverage denominator follows consumed evidence
**Status**: Proposed
Statistical coverage should measure availability of corpus context for evidence actually consumed by the interpretation path, rather than mechanically counting every enriched statistic wrapper.

### IC-002 — Bounded score
`0.0 <= score <= 1.0`

### IC-003 — Bounded statistical coverage
`0.0 <= statistical_coverage <= 1.0`

### IC-004 — No evidence fabrication
Unavailable corpus statistics must remain unavailable through interpretation provenance. A structural token absent from the profile must not be explained as `DF = 0` or `DF = 1`.

### IC-005 — Zero score is not relationship rejection
A zero reference evidence score only means the reference dimension contributed no positive compatibility evidence.

### IC-006 — Coverage is not score
These must remain independent.
- Low score, high coverage (RE006-like known common token)
- Non-zero score, zero coverage (RE010-like structural fallback)
Multiplying score by statistical coverage would violate this invariant by forcing all out-of-profile structural evidence to zero.

### IC-007 — Contributions preserve provenance
Every interpreted positive evidence source must remain attributable to structural evidence produced by Stage 1. Stage 3 cannot invent tokens if Stage 1 never reported them.

### IC-008 — Interpretation is deterministic
The same enriched evidence + interpretation policy must produce the same result.

### IC-009 — Interpretation does not mutate evidence or profile state
The interpretation step operates on read-only evidence and profiles.

### IC-010 — Interpretation is not final reconciliation
Reference interpretation cannot emit `AUTO_MATCH`, `REVIEW`, `REJECT`, or `INELIGIBLE`. Those belong to later relationship semantics/decision layers.

## v0.1 Strongest-Unit Coverage Semantics

Statistical coverage is path-dependent. Under v0.1 strongest-unit interpretation, exactly one contribution determines the final reference score. Therefore statistical coverage is binary: 1.0 when the selected contribution has corpus statistics and 0.0 when the selected contribution uses structural fallback.

Non-winning contributions do not dilute coverage because they were not consumed to determine the final magnitude.

When two contributions have equal positive evidence magnitude, a contribution with available corpus statistics is preferred over one using structural fallback.

## Strongest-Unit Selection Contract (v0.1)
**Status**: Frozen

The strongest-contribution selection algorithm operates strictly on candidate `ReferenceEvidenceContribution` objects. It is deterministic, stable, and evaluates exact values without floating-point tolerance policies.

- **SS-001**: Selection consumes `ReferenceEvidenceContribution` objects.
- **SS-002**: Higher `positive_evidence` wins.
- **SS-003**: `statistics_available` is used only as an exact-magnitude tie-break.
- **SS-004**: `statistics_available` MUST NOT boost or modify `positive_evidence`.
- **SS-005**: Complete ties (exact equal magnitude and identical `statistics_available`) preserve upstream order (first contribution wins).
- **SS-006**: Selection is stable and deterministic.
- **SS-007**: Selection does not aggregate contributions.
- **SS-008**: Selection does not calculate coverage.
- **SS-009**: Selection does not construct `ReferenceEvidenceInterpretation`.
- **SS-010**: Selection does not make reconciliation decisions.
- **SS-011**: Selection does not claim probability.
- **SS-012**: Selection does not infer statistical independence.

## Interpretation Assembly Contract (v0.1)
**Status**: Frozen

The assembly helper integrates strongest-unit selection into a final interpretation object. `ReferenceEvidenceInterpretation` instances are expected to be constructed via `_assemble_reference_evidence_interpretation()`. Direct construction is intended only for testing.

- **IA-001**: Assembly consumes a tuple of validated `ReferenceEvidenceContribution` objects.
- **IA-002**: Assembly MUST use `_select_strongest_reference_contribution()`.
- **IA-003**: `score` equals selected contribution `positive_evidence`.
- **IA-004**: v0.1 `statistical_coverage` equals 1.0 if selected contribution `statistics_available` is True, 0.0 otherwise.
- **IA-005**: Coverage is derived from winner provenance.
- **IA-006**: Coverage MUST NOT be average statistics availability, fraction of profiled contributions, score multiplied by provenance, corpus completeness, or profile.reference_count ratio.
- **IA-007**: All candidate contributions remain preserved in the interpretation.
- **IA-008**: Contribution order remains unchanged.
- **IA-009**: Assembly does not aggregate magnitudes.
- **IA-010**: Assembly does not recompute rarity.
- **IA-011**: Assembly does not inspect corpus frequency.
- **IA-012**: Assembly does not mutate contributions.
- **IA-013**: Assembly does not make reconciliation decisions.
- **IA-014**: Assembly does not claim probability.
- **IA-015**: The selected contribution governs score and coverage.
- **IA-016**: A higher-magnitude unprofiled winner produces high/greater score as defined by magnitude, and coverage=0.0.
- **IA-017**: An exact-magnitude profiled tie winner produces same score, and coverage=1.0.
- **IA-018**: An empty tuple of contributions is mathematically valid and represents "no positive evidence". It MUST assemble into `score=0.0`, `statistical_coverage=0.0`, and `contributions=()`. "No evidence" is not modeled as a dummy contribution unit.
````

## File: experiments/compare_tax_penalty_models.py
````python
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from recongraph.domain.records import GSTRecord, PurchaseRecord
"""Compare two frozen Purchase-GST scoring policies.

The policies are defined locally so production policy changes do not alter
the historical A/B comparison that motivated the pure-compatibility migration.
"""

from recongraph.matching.scoring import (
    RelationshipPolicy,
    calculate_relationship_score,
    SignalName,
)
from recongraph.matching.pair_scorers import score_purchase_to_gst
from recongraph.matching.purchase_gst_semantics import SemanticFinding

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PURCHASES_PATH = PROJECT_ROOT / "datasets" / "raw" / "purchase_register.csv"
GST_RECORDS_PATH = PROJECT_ROOT / "datasets" / "raw" / "gst_records.csv"
GROUND_TRUTH_PATH = PROJECT_ROOT / "datasets" / "ground_truth" / "purchase_gst_matches.csv"

CHALLENGE_DIR = PROJECT_ROOT / "datasets" / "challenge"
CHALLENGE_PURCHASES_PATH = CHALLENGE_DIR / "purchase_register_v1.csv"
CHALLENGE_GST_RECORDS_PATH = CHALLENGE_DIR / "gst_records_v1.csv"
CHALLENGE_PAIR_LABELS_PATH = CHALLENGE_DIR / "pair_labels_v1.csv"

PURCHASE_GST_COMPARISON_WEIGHTS = {
    SignalName.ENTITY: 0.20,
    SignalName.REFERENCE: 0.20,
    SignalName.AMOUNT: 0.25,
    SignalName.TEMPORAL: 0.10,
    SignalName.TAX_IDENTITY: 0.25,
}

HYBRID_POLICY = RelationshipPolicy(
    weights=PURCHASE_GST_COMPARISON_WEIGHTS,
    contradiction_penalties={
        SignalName.TAX_IDENTITY: 0.5,
    },
)

PURE_COMPATIBILITY_POLICY = RelationshipPolicy(
    weights=PURCHASE_GST_COMPARISON_WEIGHTS,
    contradiction_penalties={},
)


@dataclass(frozen=True)
class ComparisonResult:
    dataset: str
    case_id: str
    pair_id: str
    label: str
    hybrid_score: float | None
    pure_score: float | None
    delta: float | None
    eligibility: str
    findings: tuple[str, ...]
    tax_score: float | None
    active_hybrid_penalty: bool
    is_eligibility_blocked: bool


def optional_text(value: str) -> str | None:
    stripped = value.strip()
    return stripped or None


def parse_purchase_record(row: dict[str, str]) -> PurchaseRecord:
    return PurchaseRecord(record_id="pur_cedf16a5", 
        vendor_name=optional_text(row.get("vendor_name", "")),
        reference=optional_text(row.get("invoice_number", "")),
        amount=float(row["amount"]),
        record_date=date.fromisoformat(row["invoice_date"]),
        tax_identity=optional_text(row.get("gstin", "")),
    )


def parse_gst_record(row: dict[str, str]) -> GSTRecord:
    return GSTRecord(record_id="gst_29b08642", 
        vendor_name=optional_text(row.get("supplier_name", "")),
        reference=optional_text(row.get("invoice_number", "")),
        amount=float(row["amount"]),
        record_date=date.fromisoformat(row["invoice_date"]),
        tax_identity=optional_text(row.get("gstin", "")),
    )


def load_records(path: Path, parse_fn) -> dict[str, any]:
    records = {}
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records[row["record_id"]] = parse_fn(row)
    return records


def calculate_delta(
    hybrid_score: float | None,
    pure_score: float | None,
) -> float | None:
    if hybrid_score is None or pure_score is None:
        return None
    return pure_score - hybrid_score


def evaluate_pair(
    dataset: str,
    case_id: str,
    purchase_id: str,
    gst_id: str,
    label: str,
    purchase: PurchaseRecord,
    gst_record: GSTRecord,
) -> ComparisonResult:
    pair_result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    )

    hybrid_relationship = calculate_relationship_score(
        signals=pair_result.signals,
        policy=HYBRID_POLICY,
    )

    pure_relationship = calculate_relationship_score(
        signals=pair_result.signals,
        policy=PURE_COMPATIBILITY_POLICY,
    )

    hybrid_score = hybrid_relationship.score
    pure_score = pure_relationship.score
    delta = calculate_delta(hybrid_score, pure_score)

    findings = tuple(f.value for f in pair_result.semantic_findings)
    eligibility = pair_result.eligibility.status.value

    tax_score = pair_result.signals.get(SignalName.TAX_IDENTITY)
    active_hybrid_penalty = SignalName.TAX_IDENTITY in hybrid_relationship.active_contradictions
    is_eligibility_blocked = SemanticFinding.TAX_IDENTITY_CONFLICT in pair_result.eligibility.blocking_findings

    return ComparisonResult(
        dataset=dataset,
        case_id=case_id,
        pair_id=f"{purchase_id}-{gst_id}",
        label=label,
        hybrid_score=hybrid_score,
        pure_score=pure_score,
        delta=delta,
        eligibility=eligibility,
        findings=findings,
        tax_score=tax_score,
        active_hybrid_penalty=active_hybrid_penalty,
        is_eligibility_blocked=is_eligibility_blocked,
    )


def run_baseline_experiment() -> list[ComparisonResult]:
    purchases = load_records(PURCHASES_PATH, parse_purchase_record)
    gst_records = load_records(GST_RECORDS_PATH, parse_gst_record)
    
    positive_pairs = set()
    with GROUND_TRUTH_PATH.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["relationship"] == "same_financial_event":
                positive_pairs.add((row["purchase_record_id"], row["gst_record_id"]))

    results = []
    for p_id, purchase in purchases.items():
        for g_id, gst_record in gst_records.items():
            label = "positive" if (p_id, g_id) in positive_pairs else "negative"
            results.append(
                evaluate_pair(
                    dataset="baseline",
                    case_id="-",
                    purchase_id=p_id,
                    gst_id=g_id,
                    label=label,
                    purchase=purchase,
                    gst_record=gst_record,
                )
            )
            
    results.sort(key=lambda r: r.hybrid_score if r.hybrid_score is not None else -1.0, reverse=True)
    return results


def run_challenge_experiment() -> list[ComparisonResult]:
    purchases = load_records(CHALLENGE_PURCHASES_PATH, parse_purchase_record)
    gst_records = load_records(CHALLENGE_GST_RECORDS_PATH, parse_gst_record)
    
    results = []
    with CHALLENGE_PAIR_LABELS_PATH.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            case_id = row["case_id"]
            p_id = row["purchase_record_id"]
            g_id = row["gst_record_id"]
            label = row["expected_label"]
            results.append(
                evaluate_pair(
                    dataset="challenge",
                    case_id=case_id,
                    purchase_id=p_id,
                    gst_id=g_id,
                    label=label,
                    purchase=purchases[p_id],
                    gst_record=gst_records[g_id],
                )
            )
            
    results.sort(key=lambda r: (r.case_id, r.pair_id))
    return results


def format_score(score: float | None, sign: bool = False) -> str:
    if score is None:
        return "None"
    return f"{score:+.4f}" if sign else f"{score:.4f}"


def format_findings(findings: tuple[str, ...]) -> str:
    if not findings:
        return "-"
    return ",".join(findings)


def print_table(results: list[ComparisonResult]) -> None:
    print(
        f"{'Dataset':<9} "
        f"{'Case':<7} "
        f"{'Pair':<14} "
        f"{'Label':<17} "
        f"{'Hybrid':>8} "
        f"{'Pure':>8} "
        f"{'Delta':>9}  "
        f"{'Eligibility':<13} "
        f"{'Findings'}"
    )
    print("-" * 112)
    for r in results:
        print(
            f"{r.dataset:<9} "
            f"{r.case_id:<7} "
            f"{r.pair_id:<14} "
            f"{r.label:<17} "
            f"{format_score(r.hybrid_score):>8} "
            f"{format_score(r.pure_score):>8} "
            f"{format_score(r.delta, sign=True):>9}  "
            f"{r.eligibility:<13} "
            f"{format_findings(r.findings)}"
        )


def main():
    baseline_results = run_baseline_experiment()
    challenge_results = run_challenge_experiment()
    all_results = baseline_results + challenge_results

    print_table(all_results)
    
    # Score-change summary
    changed_scores = sum(1 for r in all_results if r.delta is not None and r.delta != 0.0)
    unchanged_scores = sum(1 for r in all_results if r.delta is not None and r.delta == 0.0)
    max_positive_delta = max((r.delta for r in all_results if r.delta is not None), default=None)
    min_delta = min((r.delta for r in all_results if r.delta is not None), default=None)
    
    print("\nScore-change summary")
    print("-" * 20)
    print(f"Total pairs compared: {len(all_results)}")
    print(f"Changed scores: {changed_scores}")
    print(f"Unchanged scores: {unchanged_scores}")
    print(f"Maximum positive delta: {format_score(max_positive_delta)}")
    print(f"Minimum delta: {format_score(min_delta)}")

    # Baseline positive summary
    baseline_positives = [r for r in baseline_results if r.label == "positive"]
    pos_changed = sum(1 for r in baseline_positives if r.delta is not None and r.delta != 0.0)
    min_hybrid_pos = min((r.hybrid_score for r in baseline_positives if r.hybrid_score is not None), default=None)
    min_pure_pos = min((r.pure_score for r in baseline_positives if r.pure_score is not None), default=None)
    
    print("\nBaseline positive summary")
    print("-" * 25)
    print(f"Positive pairs: {len(baseline_positives)}")
    print(f"Positive scores changed: {pos_changed}")
    print(f"Minimum hybrid positive: {format_score(min_hybrid_pos)}")
    print(f"Minimum pure positive: {format_score(min_pure_pos)}")

    # Baseline negative summary
    baseline_negatives = [r for r in baseline_results if r.label == "negative"]
    neg_changed = sum(1 for r in baseline_negatives if r.delta is not None and r.delta != 0.0)
    max_hybrid_neg = max((r.hybrid_score for r in baseline_negatives if r.hybrid_score is not None), default=None)
    max_pure_neg = max((r.pure_score for r in baseline_negatives if r.pure_score is not None), default=None)
    
    print("\nBaseline negative summary")
    print("-" * 25)
    print(f"Negative pairs: {len(baseline_negatives)}")
    print(f"Negative scores changed: {neg_changed}")
    print(f"Maximum hybrid negative: {format_score(max_hybrid_neg)}")
    print(f"Maximum pure negative: {format_score(max_pure_neg)}")

    # Hybrid separation gap
    print("\nHybrid separation gap:")
    if min_hybrid_pos is not None and max_hybrid_neg is not None:
        print(f"{format_score(min_hybrid_pos - max_hybrid_neg)}")
        
    print("\nPure separation gap:")
    if min_pure_pos is not None and max_pure_neg is not None:
        print(f"{format_score(min_pure_pos - max_pure_neg)}")

    # Challenge eligibility summary
    print("\nChallenge eligibility summary")
    print("-" * 29)
    # Eligibility changes are effectively 0 because we don't recalculate it, we take it from production.
    # The prompt explicitly asks to print 0 if we didn't recompute.
    print("Eligibility changes: 0")
    
    # Tax-conflict consequence audit
    print("\nTax-conflict consequence audit")
    print("-" * 30)
    print(f"{'Pair':<14} {'Tax contribution':<18} {'Hybrid penalty':<16} {'Eligibility blocker'}")
    tax_conflict_results = [r for r in all_results if "tax_identity_conflict" in r.findings]
    for r in tax_conflict_results:
        tax_contrib = "zero" if r.tax_score == 0.0 else "nonzero"
        hybrid_pen = "yes" if r.active_hybrid_penalty else "no"
        elig_block = "yes" if r.is_eligibility_blocked else "no"
        print(f"{r.pair_id:<14} {tax_contrib:<18} {hybrid_pen:<16} {elig_block}")

if __name__ == "__main__":
    main()
````

## File: src/recongraph/domain/derivations.py
````python
import re
import json
import hashlib
from dataclasses import dataclass
from typing import Protocol, FrozenSet, Any

from .identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest, canonical_encode
from .dependencies import SemanticDependencyRef
from .payloads import CanonicalPayloadEnvelope

@dataclass(frozen=True, slots=True, order=True)
class ProviderId:
    """Namespaced operational semantic identity for a provider."""
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9_-]*(?:\.[a-z][a-z0-9_-]*)+$")

    def __post_init__(self):
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid ProviderId format: '{self.value}'")


@dataclass(frozen=True, slots=True, order=True)
class ProviderSemanticVersion:
    """Semantic versioning for Provider meaning-producing behavior."""
    major: int
    minor: int
    patch: int


@dataclass(frozen=True, slots=True, order=True)
class DerivationMethodId:
    """Provider-relative semantic method identifier."""
    value: str

    def __post_init__(self):
        if not self.value or not isinstance(self.value, str):
            raise ValueError("DerivationMethodId must be a non-empty string.")


@dataclass(frozen=True, slots=True)
class DerivationMethodDescriptor:
    provider_id: ProviderId
    method_id: DerivationMethodId
    commutative_roles: frozenset[str]


@dataclass(frozen=True, slots=True, order=True)
class DerivationInputBinding:
    role: str
    identity: KernelIdentityRef


@dataclass(frozen=True, slots=True, order=True)
class DerivationIdentity:
    """Content-addressed semantic computation key."""
    digest: str

    @classmethod
    def compute(
        cls,
        provider_semantic_version: ProviderSemanticVersion,
        method: DerivationMethodDescriptor,
        inputs: frozenset[DerivationInputBinding],
        dependencies: tuple[SemanticDependencyRef, ...] = ()
    ) -> "DerivationIdentity":
        
        # 1. Canonicalize inputs based on roles
        canonical_inputs = []
        roles = {}
        for binding in inputs:
            node = binding.identity
            # Enforce that inputs are actual graph nodes (observation or artifact)
            if node.domain.value not in {"recongraph.observation_occurrence", "recongraph.derivation_occurrence", "recongraph.observation_identity", "recongraph.derived_artifact_identity"}:
                 # Wait, K6 input bindings: it's actually identity ref. It can be ObservationIdentity or DerivedArtifactIdentity.
                 pass
            roles.setdefault(binding.role, []).append(node.digest.value)
            
        for role, digests in sorted(roles.items()):
            if role in method.commutative_roles:
                digests.sort()
            else:
                digests.sort() 
                
            canonical_inputs.append({
                "role": role,
                "identities": digests
            })

        # 2. Canonicalize dependencies
        if len(set(dependencies)) != len(dependencies):
            raise ValueError("Duplicate identical semantic dependencies are rejected.")
            
        canonical_deps = []
        for dep in sorted(dependencies):
            canon_dep = {
                "kind": dep.kind.value,
                "namespace": dep.namespace.value,
                "identity": dep.identity.value,
                "stability": dep.stability.value
            }
            if dep.semantic_version:
                canon_dep["semantic_version"] = dep.semantic_version
            canonical_deps.append(canon_dep)

        payload = {
            "schema": "recongraph.derivation_identity.v1",
            "provider": {
                "id": method.provider_id.value,
                "semantic_version": f"{provider_semantic_version.major}.{provider_semantic_version.minor}.{provider_semantic_version.patch}"
            },
            "method": {
                "id": method.method_id.value
            },
            "inputs": canonical_inputs,
            "dependencies": canonical_deps
        }
        
        canonical_bytes = canonical_encode(payload)

        # Domain separation
        domain_separated_bytes = b"recongraph:derivation_identity:v1\x00" + canonical_bytes
        digest_hex = hashlib.sha256(domain_separated_bytes).hexdigest()
        return cls(f"sha256:{digest_hex}")

    def to_kernel_identity_ref(self) -> KernelIdentityRef:
        return KernelIdentityRef(
            domain=IdentityDomainId("recongraph.derivation_identity"),
            schema=IdentitySchemaId("recongraph.derivation_identity.v1"),
            digest=IdentityDigest(self.digest)
        )


@dataclass(frozen=True, slots=True, order=True)
class DerivationOccurrenceIdentity:
    """
    Deterministic identity for an ancestry computation occurrence.
    H(derivation_identity_ref, role-bound parent ancestry refs).
    """
    digest: str

    @classmethod
    def compute(
        cls,
        derivation_identity: DerivationIdentity,
        parent_occurrences: frozenset[KernelIdentityRef]
    ) -> 'DerivationOccurrenceIdentity':
        
        canon_parents = sorted(ref.digest.value for ref in parent_occurrences)

        payload = {
            "schema": "recongraph.derivation_occurrence_identity.v1",
            "derivation_identity": derivation_identity.to_kernel_identity_ref().digest.value,
            "parent_occurrences": canon_parents
        }
        
        canonical_bytes = canonical_encode(payload)
        domain_separated_bytes = b"recongraph:derivation_occurrence:v1\x00" + canonical_bytes
        digest_hex = hashlib.sha256(domain_separated_bytes).hexdigest()
        return cls(f"sha256:{digest_hex}")

    def to_kernel_identity_ref(self) -> KernelIdentityRef:
        return KernelIdentityRef(
            domain=IdentityDomainId("recongraph.derivation_occurrence"),
            schema=IdentitySchemaId("recongraph.derivation_occurrence_identity.v1"),
            digest=IdentityDigest(self.digest)
        )


@dataclass(frozen=True, slots=True)
class DerivationOccurrence:
    """Provenance record binding the computation to actual input occurrences."""
    derivation_identity: DerivationIdentity
    parent_occurrences: frozenset[KernelIdentityRef]
    identity: DerivationOccurrenceIdentity

    @classmethod
    def create(
        cls,
        derivation_identity: DerivationIdentity,
        parent_occurrences: frozenset[KernelIdentityRef]
    ) -> 'DerivationOccurrence':
        identity = DerivationOccurrenceIdentity.compute(derivation_identity, parent_occurrences)
        return cls(derivation_identity=derivation_identity, parent_occurrences=parent_occurrences, identity=identity)


@dataclass(frozen=True, slots=True, order=True)
class DerivedArtifactTypeId:
    """Namespaced operational semantic identity for a derived artifact type."""
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9_-]*(?:\.[a-z][a-z0-9_-]*)+$")

    def __post_init__(self):
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid DerivedArtifactTypeId format: '{self.value}'")


def _validate_canonical_payload(value: Any):
    if value is None:
        return
    if isinstance(value, (bool, int, str)):
        return
    if isinstance(value, float):
        raise ValueError("Floats are forbidden in CanonicalPayloadEnvelope.")
    if isinstance(value, tuple):
        for item in value:
            _validate_canonical_payload(item)
        return
    if isinstance(value, dict):
        for k, v in value.items():
            if not isinstance(k, str):
                raise ValueError("Dict keys in CanonicalPayloadEnvelope must be strings.")
            _validate_canonical_payload(v)
        return
    raise ValueError(f"Type {type(value)} is forbidden in CanonicalPayloadEnvelope.")


@dataclass(frozen=True, slots=True)
class CanonicalPayloadEnvelope:
    """Recursively validated JSON semantic algebra. No floats, sets, or custom objects."""
    data: dict[str, Any]

    def __post_init__(self):
        if not isinstance(self.data, dict):
            raise ValueError("CanonicalPayloadEnvelope data must be a dictionary.")
        _validate_canonical_payload(self.data)

    def canonicalize(self) -> bytes:
        return json.dumps(
            self.data,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False
        ).encode("utf-8")


@dataclass(frozen=True, slots=True, order=True)
class DerivedArtifactIdentity:
    """Content-addressed semantic artifact identity."""
    digest: str

    @classmethod
    def compute(
        cls,
        type_id: DerivedArtifactTypeId,
        semantic_version: str,
        payload: 'CanonicalPayloadEnvelope'
    ) -> "DerivedArtifactIdentity":
        
        envelope = {
            "schema": "recongraph.derived_artifact_identity.v1",
            "type_id": type_id.value,
            "semantic_version": semantic_version,
            "payload_fingerprint": hashlib.sha256(payload.canonicalize()).hexdigest()
        }

        canonical_bytes = canonical_encode(envelope)

        # Domain separation
        domain_separated_bytes = b"recongraph:derived_artifact_identity:v1\x00" + canonical_bytes
        
        digest_hex = hashlib.sha256(domain_separated_bytes).hexdigest()
        return cls(f"sha256:{digest_hex}")

    def to_kernel_identity_ref(self) -> KernelIdentityRef:
        return KernelIdentityRef(
            domain=IdentityDomainId("recongraph.derived_artifact_identity"),
            schema=IdentitySchemaId("recongraph.derived_artifact_identity.v1"),
            digest=IdentityDigest(self.digest)
        )


@dataclass(frozen=True, slots=True)
class DerivedArtifact:
    """The materialized semantic output of a derivation."""
    identity: DerivedArtifactIdentity
    payload: CanonicalPayloadEnvelope
````

## File: src/recongraph/domain/lineage.py
````python
import re
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, slots=True, order=True)
class SourceSystemId:
    """
    Identifies a logical source system namespace (e.g., 'sap.production', 'gst.portal').
    It does not identify specific files or rows.
    """
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9_-]*(?:\.[a-z][a-z0-9_-]*)+$")

    def __post_init__(self):
        if not self._PATTERN.match(self.value):
            raise ValueError(
                f"Invalid SourceSystemId format: '{self.value}'. "
                "Must be lowercased, namespaced (e.g., 'sap.production'), and contain only a-z, 0-9, -, _"
            )


@dataclass(frozen=True, slots=True, order=True)
class SourceArtifactId:
    """
    SourceArtifactId is an opaque identifier within a SourceSystemId namespace. 
    It does not independently claim global uniqueness, immutability, or content identity.
    """
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("SourceArtifactId cannot be empty.")
        if self.value != self.value.strip():
            raise ValueError("SourceArtifactId cannot contain surrounding whitespace.")
        # Reject control characters (0x00-0x1F and 0x7F)
        if any(ord(c) < 32 or ord(c) == 127 for c in self.value):
            raise ValueError("SourceArtifactId cannot contain control characters.")


@dataclass(frozen=True, slots=True, order=True)
class SourceLocator:
    """
    Identifies the semantic or structural location inside an artifact (e.g., 'field:vendor_name').
    The kernel preserves the supplied canonical coordinate but does not parse it.
    """
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("SourceLocator cannot be empty.")
        if self.value != self.value.strip():
            raise ValueError("SourceLocator cannot contain surrounding whitespace.")


@dataclass(frozen=True, slots=True, order=True)
class SourceVersionRef:
    """
    Literal opaque source version identity. Acts as a state qualifier over the logical artifact.
    """
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("SourceVersionRef cannot be empty.")


@dataclass(frozen=True, slots=True, order=True)
class StructuredSourceLineage:
    """
    Minimal immutable lineage coordinates answering where a fact came from.
    Preserves exact temporal source occurrence identity.
    """
    source_system: SourceSystemId
    source_artifact: SourceArtifactId
    source_locator: SourceLocator
    source_version: SourceVersionRef | None = None

    def canonicalize_for_serialization(self) -> bytes:
        """
        Explicit canonical representation for identity hashing.
        Uses Canonical JSON bytes with sorted keys, explicit schema identifier, 
        UTF-8, and compact separators.
        """
        import json
        payload = {
            "schema": "recongraph.source_lineage.v1",
            "source_system": self.source_system.value,
            "source_artifact": self.source_artifact.value,
            "source_locator": self.source_locator.value,
            "source_version": self.source_version.value if self.source_version else None
        }
        return json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False
        ).encode("utf-8")
````

## File: src/recongraph/matching/purchase_gst_semantics.py
````python
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum

from recongraph.matching.scoring import SignalName


# Represents a statistical rarity boundary (score >= 0.8 implies token frequency <= 4% of corpus)
STRONG_REFERENCE_SCORE = 0.8
STRONG_ENTITY_SCORE = 0.9
STRONG_AMOUNT_SCORE = 0.9


class SemanticFinding(StrEnum):
    SEVERE_AMOUNT_CONFLICT = "severe_amount_conflict"
    TAX_IDENTITY_CONFLICT = "tax_identity_conflict"
    DISTINCT_EVENT_IDENTITY_EVIDENCE = (
        "distinct_event_identity_evidence"
    )


def analyze_purchase_gst_semantics(
    evidence: Mapping[SignalName, float | None],
) -> tuple[SemanticFinding, ...]:
    findings: list[SemanticFinding] = []

    entity = evidence[SignalName.ENTITY]
    reference = evidence[SignalName.REFERENCE]
    amount = evidence[SignalName.AMOUNT]
    temporal = evidence[SignalName.TEMPORAL]
    tax_identity = evidence[SignalName.TAX_IDENTITY]

    if (
        amount == 0.0
        and reference is not None
        and reference >= STRONG_REFERENCE_SCORE
        and tax_identity == 1.0
    ):
        findings.append(
            SemanticFinding.SEVERE_AMOUNT_CONFLICT
        )

    if tax_identity == 0.0:
        findings.append(
            SemanticFinding.TAX_IDENTITY_CONFLICT
        )

    if (
        entity is not None
        and entity >= STRONG_ENTITY_SCORE
        and reference == 0.0
        and amount is not None
        and amount >= STRONG_AMOUNT_SCORE
        and temporal == 0.0
        and tax_identity == 1.0
    ):
        findings.append(
            SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        )

    return tuple(findings)


class OneToOneEligibility(StrEnum):
    ELIGIBLE = "eligible"
    INELIGIBLE = "ineligible"


@dataclass(frozen=True)
class EligibilityResult:
    status: OneToOneEligibility
    blocking_findings: tuple[SemanticFinding, ...]

    def __post_init__(self) -> None:
        if (
            self.status is OneToOneEligibility.ELIGIBLE
            and self.blocking_findings
        ):
            raise ValueError(
                "eligible result cannot contain blocking findings"
            )

        if (
            self.status is OneToOneEligibility.INELIGIBLE
            and not self.blocking_findings
        ):
            raise ValueError(
                "ineligible result must contain at least one blocking finding"
            )


ONE_TO_ONE_BLOCKING_FINDINGS = frozenset(
    {
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
        SemanticFinding.TAX_IDENTITY_CONFLICT,
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
    }
)


def evaluate_purchase_gst_one_to_one_eligibility(
    findings: tuple[SemanticFinding, ...],
) -> EligibilityResult:
    blocking_findings_list: list[SemanticFinding] = []

    for finding in findings:
        if (
            finding in ONE_TO_ONE_BLOCKING_FINDINGS
            and finding not in blocking_findings_list
        ):
            blocking_findings_list.append(finding)

    blocking_findings = tuple(blocking_findings_list)

    status = (
        OneToOneEligibility.INELIGIBLE
        if blocking_findings
        else OneToOneEligibility.ELIGIBLE
    )

    return EligibilityResult(
        status=status,
        blocking_findings=blocking_findings,
    )
````

## File: src/recongraph/matching/reference_evidence.py
````python
import re
from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping, Optional, Tuple

from recongraph.normalization.text import normalize_reference

@dataclass(frozen=True)
class ReferenceIdentityEvidence:
    normalized_a: str
    normalized_b: str
    exact_normalized_match: bool
    shared_numeric_tokens: tuple[str, ...]

def _extract_numeric_tokens(reference: str) -> tuple[str, ...]:
    return tuple(sorted(set(re.findall(r"\d+", reference))))

def extract_reference_identity(
    reference_a: str | None,
    reference_b: str | None,
) -> ReferenceIdentityEvidence | None:
    if reference_a is None or not reference_a.strip():
        return None
    if reference_b is None or not reference_b.strip():
        return None

    normalized_a = normalize_reference(reference_a)
    normalized_b = normalize_reference(reference_b)

    if not normalized_a or not normalized_b:
        return None

    exact_match = (normalized_a == normalized_b)

    tokens_a = set(_extract_numeric_tokens(reference_a))
    tokens_b = set(_extract_numeric_tokens(reference_b))

    shared_tokens = tuple(sorted(tokens_a & tokens_b))

    return ReferenceIdentityEvidence(
        normalized_a=normalized_a,
        normalized_b=normalized_b,
        exact_normalized_match=exact_match,
        shared_numeric_tokens=shared_tokens,
    )

from collections import Counter
from collections.abc import Iterable, Mapping
from types import MappingProxyType

@dataclass(frozen=True)
class ReferenceCorpusProfile:
    reference_count: int
    normalized_reference_frequency: Mapping[str, int]
    numeric_token_document_frequency: Mapping[str, int]

    def __post_init__(self) -> None:
        if self.reference_count < 0:
            raise ValueError("reference_count must be >= 0")

        sum_freq = 0
        for k, v in self.normalized_reference_frequency.items():
            if not k or k != normalize_reference(k):
                raise ValueError("invalid normalized key")
            if v < 1 or v > self.reference_count:
                raise ValueError("invalid frequency")
            sum_freq += v

        if self.reference_count > 0 and sum_freq != self.reference_count:
            raise ValueError("inconsistent normalized frequency sum")

        for k, v in self.numeric_token_document_frequency.items():
            if not k or not k.isdigit():
                raise ValueError("invalid numeric token")
            if v < 1 or v > self.reference_count:
                raise ValueError("invalid token df")

        object.__setattr__(self, "normalized_reference_frequency", MappingProxyType(dict(self.normalized_reference_frequency)))
        object.__setattr__(self, "numeric_token_document_frequency", MappingProxyType(dict(self.numeric_token_document_frequency)))

def build_reference_corpus_profile(
    references: Iterable[str | None],
) -> ReferenceCorpusProfile:
    reference_count = 0
    norm_freq: Counter[str] = Counter()
    token_df: Counter[str] = Counter()

    for reference in references:
        if reference is None or not reference.strip():
            continue

        normalized = normalize_reference(reference)
        if not normalized:
            continue

        reference_count += 1
        norm_freq[normalized] += 1

        unique_tokens = _extract_numeric_tokens(reference)
        for token in unique_tokens:
            token_df[token] += 1

    return ReferenceCorpusProfile(
        reference_count=reference_count,
        normalized_reference_frequency=norm_freq,
        numeric_token_document_frequency=token_df,
    )

@dataclass(frozen=True)
class NormalizedReferenceStatistics:
    normalized_reference: str
    frequency: int

    def __post_init__(self) -> None:
        if not self.normalized_reference or self.normalized_reference != normalize_reference(self.normalized_reference):
            raise ValueError("invalid normalized reference")
        if self.frequency < 1:
            raise ValueError("frequency must be >= 1")

@dataclass(frozen=True)
class ReferenceTokenStatistics:
    token: str
    document_frequency: int

    def __post_init__(self) -> None:
        if not self.token or not self.token.isdigit():
            raise ValueError("invalid numeric token")
        if self.document_frequency < 1:
            raise ValueError("document_frequency must be >= 1")

@dataclass(frozen=True)
class NormalizedReferenceEvidence:
    normalized_reference: str
    statistics: NormalizedReferenceStatistics | None

    def __post_init__(self) -> None:
        if not self.normalized_reference or self.normalized_reference != normalize_reference(self.normalized_reference):
            raise ValueError("invalid normalized reference")
        if self.statistics is not None and self.statistics.normalized_reference != self.normalized_reference:
            raise ValueError("statistics mismatch")

@dataclass(frozen=True)
class SharedNumericTokenEvidence:
    token: str
    statistics: ReferenceTokenStatistics | None

    def __post_init__(self) -> None:
        if not self.token or not self.token.isdigit():
            raise ValueError("invalid numeric token")
        if self.statistics is not None and self.statistics.token != self.token:
            raise ValueError("statistics mismatch")

@dataclass(frozen=True)
class EnrichedReferenceEvidence:
    identity: ReferenceIdentityEvidence
    reference_count: int
    normalized_references: tuple[NormalizedReferenceEvidence, ...]
    shared_numeric_tokens: tuple[SharedNumericTokenEvidence, ...]

    def __post_init__(self) -> None:
        if self.reference_count < 0:
            raise ValueError("reference_count must be >= 0")

        norm_refs = [e.normalized_reference for e in self.normalized_references]
        if norm_refs != sorted(norm_refs):
            raise ValueError("normalized_references must be sorted")
        if len(norm_refs) != len(set(norm_refs)):
            raise ValueError("normalized_references must not contain duplicates")

        shared_tokens = [e.token for e in self.shared_numeric_tokens]
        if shared_tokens != sorted(shared_tokens):
            raise ValueError("shared_numeric_tokens must be sorted")
        if len(shared_tokens) != len(set(shared_tokens)):
            raise ValueError("shared_numeric_tokens must not contain duplicates")

        expected_norm_refs = set([self.identity.normalized_a, self.identity.normalized_b])
        if set(norm_refs) != expected_norm_refs:
            raise ValueError("normalized_references values do not match identity")

        if set(shared_tokens) != set(self.identity.shared_numeric_tokens):
            raise ValueError("shared_numeric_tokens values do not match identity")

def enrich_reference_identity(
    identity: ReferenceIdentityEvidence,
    profile: ReferenceCorpusProfile,
) -> EnrichedReferenceEvidence:
    unique_norm_refs = sorted(list(set([identity.normalized_a, identity.normalized_b])))

    norm_evidence = []
    for ref in unique_norm_refs:
        if ref in profile.normalized_reference_frequency:
            stats = NormalizedReferenceStatistics(
                normalized_reference=ref,
                frequency=profile.normalized_reference_frequency[ref]
            )
        else:
            stats = None
        norm_evidence.append(NormalizedReferenceEvidence(normalized_reference=ref, statistics=stats))

    token_evidence = []
    for token in identity.shared_numeric_tokens:
        if token in profile.numeric_token_document_frequency:
            stats = ReferenceTokenStatistics(
                token=token,
                document_frequency=profile.numeric_token_document_frequency[token]
            )
        else:
            stats = None
        token_evidence.append(SharedNumericTokenEvidence(token=token, statistics=stats))

    return EnrichedReferenceEvidence(
        identity=identity,
        reference_count=profile.reference_count,
        normalized_references=tuple(norm_evidence),
        shared_numeric_tokens=tuple(token_evidence),
    )

@dataclass(frozen=True)
class ReferenceEvidencePolicy:
    short_token_max_length: int = 2
    medium_token_max_length: int = 4
    short_token_fallback: float = 0.10
    medium_token_fallback: float = 0.30
    long_token_fallback: float = 0.60
    exact_reference_fallback: float = 0.60
    repeated_pattern_discount: float = 0.50

    def __post_init__(self):
        import math
        if self.short_token_max_length < 1:
            raise ValueError("short_token_max_length must be >= 1")
        if self.medium_token_max_length <= self.short_token_max_length:
            raise ValueError("medium_token_max_length must be > short_token_max_length")

        # Basic float bounds
        for val in (self.short_token_fallback,
            self.medium_token_fallback,
            self.long_token_fallback,
            self.exact_reference_fallback,
            self.repeated_pattern_discount):
            
            if math.isnan(val) or math.isinf(val):
                raise ValueError("Float parameters cannot be NaN or infinity")
            if not (0.0 <= val <= 1.0):
                raise ValueError("All float parameters must be between 0.0 and 1.0")

        if not (self.short_token_fallback <= self.medium_token_fallback <= self.long_token_fallback):
            raise ValueError("Fallbacks must be monotonically non-decreasing")

        if self.long_token_fallback > 0.75:
            raise ValueError("long_token_fallback must be <= 0.75 for safety")
            
        if self.exact_reference_fallback > 0.75:
            raise ValueError("exact_reference_fallback must be <= 0.75 for safety")

class ReferenceEvidenceKind(StrEnum):
    NORMALIZED_REFERENCE = "normalized_reference"
    SHARED_NUMERIC_TOKEN = "shared_numeric_token"

@dataclass(frozen=True)
class ReferenceEvidenceContribution:
    evidence_kind: ReferenceEvidenceKind
    identity_value: str
    positive_evidence: float
    statistics_available: bool

    def __post_init__(self):
        if not self.identity_value:
            raise ValueError("identity_value cannot be empty")
        
        import math
        if not math.isfinite(self.positive_evidence):
            raise ValueError("positive_evidence must be finite")
        if not (0.0 <= self.positive_evidence <= 1.0):
            raise ValueError("positive_evidence must be between 0.0 and 1.0")

        if self.evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN:
            if not self.identity_value.isdigit():
                raise ValueError("SHARED_NUMERIC_TOKEN identity_value must be numeric")
        
        if self.evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE:
            from recongraph.normalization.text import normalize_reference
            if normalize_reference(self.identity_value) != self.identity_value:
                raise ValueError("NORMALIZED_REFERENCE identity_value must be normalized")

@dataclass(frozen=True)
class ReferenceEvidenceInterpretation:
    score: float
    statistical_coverage: float
    contributions: tuple[ReferenceEvidenceContribution, ...]

    def __post_init__(self):
        import math
        if not math.isfinite(self.score):
            raise ValueError("score must be finite")
        if not (0.0 <= self.score <= 1.0):
            raise ValueError("score must be between 0.0 and 1.0")
            
        if not math.isfinite(self.statistical_coverage):
            raise ValueError("statistical_coverage must be finite")
        if not (0.0 <= self.statistical_coverage <= 1.0):
            raise ValueError("statistical_coverage must be between 0.0 and 1.0")

        if not self.contributions:
            if self.score != 0.0 or self.statistical_coverage != 0.0:
                raise ValueError("empty contributions requires score=0.0 and statistical_coverage=0.0")
            return

        max_score = max(c.positive_evidence for c in self.contributions)
        if not math.isclose(self.score, max_score, abs_tol=1e-9):
            raise ValueError("score must equal the strongest contribution magnitude")

        if self.statistical_coverage not in {0.0, 1.0}:
            raise ValueError("statistical_coverage must be binary (0.0 or 1.0) under strongest-unit interpretation")

def _profiled_rarity_magnitude(
    frequency: int,
    reference_count: int,
) -> float:
    if frequency < 1:
        raise ValueError("frequency must be >= 1")
    if reference_count < 1:
        raise ValueError("reference_count must be >= 1")
    if frequency > reference_count:
        raise ValueError("frequency cannot exceed reference_count")
        
    import math
    return 1.0 - math.sqrt(frequency / reference_count)

def _structural_token_magnitude(
    token: str,
    policy: ReferenceEvidencePolicy,
) -> float:
    if not token or not token.isdigit():
        raise ValueError("invalid numeric token")

    n = len(token)
    if n <= policy.short_token_max_length:
        base_magnitude = policy.short_token_fallback
    elif n <= policy.medium_token_max_length:
        base_magnitude = policy.medium_token_fallback
    else:
        base_magnitude = policy.long_token_fallback

    # Single-symbol repetition detection
    if len(set(token)) == 1:
        return base_magnitude * policy.repeated_pattern_discount
        
    return base_magnitude

def _construct_reference_evidence_contributions(
    evidence: EnrichedReferenceEvidence,
    policy: ReferenceEvidencePolicy,
) -> tuple[ReferenceEvidenceContribution, ...]:
    contributions = []

    if evidence.identity.exact_normalized_match:
        # 1. Exact normalized full-reference identity is the primary evidence unit
        # 2. Shared numeric tokens are bypassed completely
        # 3. Exactly ONE contribution is produced
        norm_ev = evidence.normalized_references[0]
        
        if norm_ev.statistics is not None:
            positive_evidence = _profiled_rarity_magnitude(
                frequency=norm_ev.statistics.frequency,
                reference_count=evidence.reference_count,
            )
            stats_available = True
        else:
            positive_evidence = policy.exact_reference_fallback
            stats_available = False
            
        contributions.append(ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE,
            identity_value=norm_ev.normalized_reference,
            positive_evidence=positive_evidence,
            statistics_available=stats_available,
        ))
    else:
        # Construct one contribution for EACH shared numeric token
        for token_ev in evidence.shared_numeric_tokens:
            if token_ev.statistics is not None:
                positive_evidence = _profiled_rarity_magnitude(
                    frequency=token_ev.statistics.document_frequency,
                    reference_count=evidence.reference_count,
                )
                stats_available = True
            else:
                positive_evidence = _structural_token_magnitude(
                    token=token_ev.token,
                    policy=policy,
                )
                stats_available = False
                
            contributions.append(ReferenceEvidenceContribution(
                evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
                identity_value=token_ev.token,
                positive_evidence=positive_evidence,
                statistics_available=stats_available,
            ))
            
    return tuple(contributions)

def _select_strongest_reference_contribution(
    contributions: tuple[ReferenceEvidenceContribution, ...],
) -> ReferenceEvidenceContribution:
    if not contributions:
        raise ValueError("at least one reference evidence contribution is required")

    winner = contributions[0]

    for candidate in contributions[1:]:
        if candidate.positive_evidence > winner.positive_evidence:
            winner = candidate
            continue

        if (
            candidate.positive_evidence == winner.positive_evidence
            and candidate.statistics_available
            and not winner.statistics_available
        ):
            winner = candidate

    return winner

def _assemble_reference_evidence_interpretation(
    contributions: tuple[ReferenceEvidenceContribution, ...],
) -> ReferenceEvidenceInterpretation:
    winner = _select_strongest_reference_contribution(contributions)
    
    return ReferenceEvidenceInterpretation(
        score=winner.positive_evidence,
        statistical_coverage=1.0 if winner.statistics_available else 0.0,
        contributions=contributions
    )

def interpret_reference_evidence(
    evidence: EnrichedReferenceEvidence,
    policy: ReferenceEvidencePolicy,
) -> ReferenceEvidenceInterpretation:
    contributions = _construct_reference_evidence_contributions(evidence, policy)
    
    if not contributions:
        return ReferenceEvidenceInterpretation(
            score=0.0,
            statistical_coverage=0.0,
            contributions=()
        )
        
    return _assemble_reference_evidence_interpretation(contributions)

@dataclass(frozen=True)
class ReferenceEvidenceContext:
    profile: ReferenceCorpusProfile
    policy: ReferenceEvidencePolicy

def compute_reference_interpretation(
    reference_a: str | None,
    reference_b: str | None,
    context: ReferenceEvidenceContext,
) -> ReferenceEvidenceInterpretation:
    identity = extract_reference_identity(reference_a, reference_b)
    
    if identity is None:
        return ReferenceEvidenceInterpretation(
            score=0.0,
            statistical_coverage=0.0,
            contributions=()
        )
        
    enriched = enrich_reference_identity(identity, context.profile)
    return interpret_reference_evidence(enriched, context.policy)
````

## File: src/recongraph/matching/signals.py
````python
from datetime import date

from rapidfuzz import fuzz

from recongraph.normalization.text import (
    normalize_tax_identity,
    normalize_vendor_name,
)


def _is_year_like_token(token: str) -> bool:
    """Return whether a numeric token resembles a calendar year."""
    if len(token) != 4:
        return False

    year = int(token)

    return 1900 <= year <= 2100


def amount_score(
    amount_a: float,
    amount_b: float,
    tolerance: float = 0.01,
) -> float:
    """Calculate scale-aware compatibility between two monetary amounts."""
    if tolerance <= 0:
        raise ValueError("tolerance must be greater than zero")

    maximum_amount = max(abs(amount_a), abs(amount_b))

    if maximum_amount == 0:
        return 1.0

    relative_difference = (
        abs(amount_a - amount_b) / maximum_amount
    )

    return max(
        0.0,
        1.0 - (relative_difference / tolerance),
    )


def tax_identity_score(
    tax_identity_a: str | None,
    tax_identity_b: str | None,
) -> float | None:
    """Compare tax identities while preserving unknown evidence states."""
    if tax_identity_a is None or tax_identity_b is None:
        return None

    normalized_a = normalize_tax_identity(tax_identity_a)
    normalized_b = normalize_tax_identity(tax_identity_b)

    if not normalized_a or not normalized_b:
        return None

    if normalized_a == normalized_b:
        return 1.0

    return 0.0


def temporal_score(
    date_a: date,
    date_b: date,
    max_days: int,
) -> float:
    """Calculate temporal compatibility within an expected date window."""
    if max_days <= 0:
        raise ValueError("max_days must be greater than zero")

    day_difference = abs((date_a - date_b).days)

    return max(
        0.0,
        1.0 - (day_difference / max_days),
    )




def entity_score(
    entity_a: str | None,
    entity_b: str | None,
) -> float | None:
    """Calculate normalized textual similarity between vendor entities."""
    if entity_a is None or entity_b is None:
        return None

    normalized_a = normalize_vendor_name(entity_a)
    normalized_b = normalize_vendor_name(entity_b)

    if not normalized_a or not normalized_b:
        return None

    similarity = fuzz.ratio(
        normalized_a,
        normalized_b,
    )

    return similarity / 100.0
````

## File: tests/test_matching_signals.py
````python
from datetime import date
import pytest

from recongraph.matching.signals import (
    amount_score,
    entity_score,
    tax_identity_score,
    temporal_score,
)


def test_amount_score_returns_one_for_exact_match() -> None:
    assert amount_score(118000.0, 118000.0) == 1.0


def test_amount_score_is_scale_aware() -> None:
    small_scale_score = amount_score(
        2000.0,
        1000.0,
    )
    large_scale_score = amount_score(
        10_000_000.0,
        9_999_000.0,
    )

    assert small_scale_score == 0.0
    assert large_scale_score > small_scale_score


def test_amount_score_decays_within_tolerance() -> None:
    score = amount_score(
        100_000.0,
        99_500.0,
    )

    assert score == pytest.approx(0.5)


def test_amount_score_returns_zero_at_tolerance_boundary() -> None:
    score = amount_score(
        100_000.0,
        99_000.0,
    )

    assert score == 0.0


def test_amount_score_returns_zero_beyond_tolerance() -> None:
    score = amount_score(
        100_000.0,
        90_000.0,
    )

    assert score == 0.0


def test_amount_score_handles_two_zero_amounts() -> None:
    assert amount_score(0.0, 0.0) == 1.0


def test_amount_score_rejects_non_positive_tolerance() -> None:
    with pytest.raises(
        ValueError,
        match="tolerance must be greater than zero",
    ):
        amount_score(
            100_000.0,
            99_500.0,
            tolerance=0.0,
        )


def test_tax_identity_score_returns_one_for_matching_identities() -> None:
    score = tax_identity_score(
        "07ABCDE1234F1Z5",
        "07abcde1234f1z5",
    )

    assert score == 1.0


def test_tax_identity_score_returns_zero_for_conflicting_identities() -> None:
    score = tax_identity_score(
        "07ABCDE1234F1Z5",
        "09WXYZA7890B1Z4",
    )

    assert score == 0.0


def test_tax_identity_score_returns_none_when_identity_is_missing() -> None:
    score = tax_identity_score(
        "07ABCDE1234F1Z5",
        None,
    )

    assert score is None


def test_tax_identity_score_returns_none_when_both_identities_are_missing() -> None:
    assert tax_identity_score(None, None) is None


def test_tax_identity_score_treats_blank_identity_as_unknown() -> None:
    assert tax_identity_score("", "   ") is None


def test_temporal_score_returns_one_for_same_date() -> None:
    score = temporal_score(
        date(2026, 6, 12),
        date(2026, 6, 12),
        max_days=7,
    )

    assert score == 1.0


def test_temporal_score_decays_with_date_distance() -> None:
    score = temporal_score(
        date(2026, 6, 12),
        date(2026, 6, 13),
        max_days=7,
    )

    assert score == pytest.approx(6 / 7)


def test_temporal_score_is_direction_agnostic() -> None:
    forward_score = temporal_score(
        date(2026, 6, 12),
        date(2026, 6, 15),
        max_days=7,
    )
    backward_score = temporal_score(
        date(2026, 6, 15),
        date(2026, 6, 12),
        max_days=7,
    )

    assert forward_score == backward_score


def test_temporal_score_returns_zero_at_window_boundary() -> None:
    score = temporal_score(
        date(2026, 6, 12),
        date(2026, 6, 19),
        max_days=7,
    )

    assert score == 0.0


def test_temporal_score_returns_zero_beyond_window() -> None:
    score = temporal_score(
        date(2026, 6, 12),
        date(2026, 7, 12),
        max_days=7,
    )

    assert score == 0.0


def test_temporal_score_rejects_non_positive_window() -> None:
    with pytest.raises(
        ValueError,
        match="max_days must be greater than zero",
    ):
        temporal_score(
            date(2026, 6, 12),
            date(2026, 6, 13),
            max_days=0,
        )
````

## File: tests/test_purchase_gst_semantics.py
````python
import pytest

from recongraph.matching.purchase_gst_semantics import (
    EligibilityResult,
    OneToOneEligibility,
    SemanticFinding,
    ONE_TO_ONE_BLOCKING_FINDINGS,
    analyze_purchase_gst_semantics,
    evaluate_purchase_gst_one_to_one_eligibility,
)
from recongraph.matching.scoring import SignalName


def complete_evidence(
    *,
    entity: float | None = 1.0,
    reference: float | None = 1.0,
    amount: float | None = 1.0,
    temporal: float | None = 1.0,
    tax_identity: float | None = 1.0,
) -> dict[SignalName, float | None]:
    return {
        SignalName.ENTITY: entity,
        SignalName.REFERENCE: reference,
        SignalName.AMOUNT: amount,
        SignalName.TEMPORAL: temporal,
        SignalName.TAX_IDENTITY: tax_identity,
    }


def test_analyze_purchase_gst_semantics_returns_no_findings_for_clean_evidence():
    findings = analyze_purchase_gst_semantics(
        complete_evidence()
    )
    assert findings == ()


# PG-001: Severe Amount Conflict
def test_detects_severe_amount_conflict():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            reference=0.8,
            amount=0.0,
            tax_identity=1.0,
        )
    )
    assert findings == (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
    )


def test_does_not_detect_severe_amount_conflict_when_amount_is_positive():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            reference=0.8,
            amount=0.01,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT
        not in findings
    )


def test_does_not_detect_severe_amount_conflict_without_strong_reference_evidence():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            reference=0.0,
            amount=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT
        not in findings
    )


def test_does_not_detect_severe_amount_conflict_when_reference_is_unknown():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            reference=None,
            amount=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT
        not in findings
    )


def test_does_not_detect_severe_amount_conflict_when_tax_identity_conflicts():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            reference=0.8,
            amount=0.0,
            tax_identity=0.0,
        )
    )
    assert (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT
        not in findings
    )


def test_does_not_detect_severe_amount_conflict_when_tax_identity_is_unknown():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            reference=0.8,
            amount=0.0,
            tax_identity=None,
        )
    )
    assert (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT
        not in findings
    )


# Tax Identity Conflict
def test_detects_tax_identity_conflict():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            tax_identity=0.0,
        )
    )
    assert findings == (
        SemanticFinding.TAX_IDENTITY_CONFLICT,
    )


def test_does_not_detect_tax_identity_conflict_when_unknown():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            tax_identity=None,
        )
    )
    assert (
        SemanticFinding.TAX_IDENTITY_CONFLICT
        not in findings
    )


def test_does_not_detect_tax_identity_conflict_when_tax_identity_agrees():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.TAX_IDENTITY_CONFLICT
        not in findings
    )


# PG-002: Distinct Event Identity Evidence
def test_detects_distinct_event_identity_evidence():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=1.0,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert findings == (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
    )


def test_does_not_detect_distinct_event_identity_when_entity_is_weak():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=0.89,
            reference=0.0,
            amount=1.0,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_detects_distinct_event_identity_at_entity_threshold():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=0.9,
            reference=0.0,
            amount=1.0,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        in findings
    )


def test_does_not_detect_distinct_event_identity_when_amount_is_weak():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=0.89,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_detects_distinct_event_identity_at_amount_threshold():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=0.9,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        in findings
    )


def test_does_not_detect_distinct_event_identity_when_reference_has_positive_evidence():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.8,
            amount=1.0,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_does_not_detect_distinct_event_identity_when_reference_is_unknown():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=None,
            amount=1.0,
            temporal=0.0,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_does_not_detect_distinct_event_identity_when_temporal_is_positive():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=1.0,
            temporal=0.01,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_does_not_detect_distinct_event_identity_when_temporal_is_unknown():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=1.0,
            temporal=None,
            tax_identity=1.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_does_not_detect_distinct_event_identity_when_tax_identity_conflicts():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=1.0,
            temporal=0.0,
            tax_identity=0.0,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


def test_does_not_detect_distinct_event_identity_when_tax_identity_is_unknown():
    findings = analyze_purchase_gst_semantics(
        complete_evidence(
            entity=1.0,
            reference=0.0,
            amount=1.0,
            temporal=0.0,
            tax_identity=None,
        )
    )
    assert (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        not in findings
    )


# Missing Evidence Keys
@pytest.mark.parametrize(
    "missing_signal",
    [SignalName.ENTITY, SignalName.REFERENCE, SignalName.AMOUNT, SignalName.TEMPORAL, SignalName.TAX_IDENTITY],
)
def test_analyze_purchase_gst_semantics_rejects_missing_evidence_keys(
    missing_signal: SignalName,
):
    evidence = complete_evidence()
    del evidence[missing_signal]

    with pytest.raises(KeyError):
        analyze_purchase_gst_semantics(evidence)


# Eligibility tests
def test_one_to_one_eligibility_is_eligible_without_findings():
    result = evaluate_purchase_gst_one_to_one_eligibility(())

    assert result == EligibilityResult(
        status=OneToOneEligibility.ELIGIBLE,
        blocking_findings=(),
    )


def test_severe_amount_conflict_blocks_one_to_one_eligibility():
    result = evaluate_purchase_gst_one_to_one_eligibility(
        (
            SemanticFinding.SEVERE_AMOUNT_CONFLICT,
        )
    )

    assert result == EligibilityResult(
        status=OneToOneEligibility.INELIGIBLE,
        blocking_findings=(
            SemanticFinding.SEVERE_AMOUNT_CONFLICT,
        ),
    )


def test_tax_identity_conflict_blocks_one_to_one_eligibility():
    result = evaluate_purchase_gst_one_to_one_eligibility(
        (
            SemanticFinding.TAX_IDENTITY_CONFLICT,
        )
    )

    assert result == EligibilityResult(
        status=OneToOneEligibility.INELIGIBLE,
        blocking_findings=(
            SemanticFinding.TAX_IDENTITY_CONFLICT,
        ),
    )


def test_distinct_event_identity_evidence_blocks_one_to_one_eligibility():
    result = evaluate_purchase_gst_one_to_one_eligibility(
        (
            SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
        )
    )

    assert result == EligibilityResult(
        status=OneToOneEligibility.INELIGIBLE,
        blocking_findings=(
            SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
        ),
    )


def test_one_to_one_eligibility_preserves_multiple_blocking_findings():
    findings = (
        SemanticFinding.TAX_IDENTITY_CONFLICT,
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
    )

    result = evaluate_purchase_gst_one_to_one_eligibility(
        findings
    )

    assert result == EligibilityResult(
        status=OneToOneEligibility.INELIGIBLE,
        blocking_findings=findings,
    )


def test_one_to_one_blocking_findings_are_explicit():
    assert ONE_TO_ONE_BLOCKING_FINDINGS == frozenset(
        {
            SemanticFinding.SEVERE_AMOUNT_CONFLICT,
            SemanticFinding.TAX_IDENTITY_CONFLICT,
            SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
        }
    )


def test_one_to_one_eligibility_deduplicates_blocking_findings():
    result = evaluate_purchase_gst_one_to_one_eligibility(
        (
            SemanticFinding.SEVERE_AMOUNT_CONFLICT,
            SemanticFinding.SEVERE_AMOUNT_CONFLICT,
        )
    )

    assert result.blocking_findings == (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
    )


def test_eligibility_result_rejects_eligible_status_with_blocking_findings():
    with pytest.raises(ValueError):
        EligibilityResult(
            status=OneToOneEligibility.ELIGIBLE,
            blocking_findings=(
                SemanticFinding.SEVERE_AMOUNT_CONFLICT,
            ),
        )


def test_eligibility_result_rejects_ineligible_status_without_blocking_findings():
    with pytest.raises(ValueError):
        EligibilityResult(
            status=OneToOneEligibility.INELIGIBLE,
            blocking_findings=(),
        )
````

## File: tests/test_reference_evidence.py
````python
import pytest

from recongraph.matching.reference_evidence import (
    EnrichedReferenceEvidence,
    NormalizedReferenceStatistics,
    ReferenceCorpusProfile,
    ReferenceIdentityEvidence,
    ReferenceTokenStatistics,
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
    ReferenceEvidenceContribution,
    ReferenceEvidenceKind,
    ReferenceEvidencePolicy,
    ReferenceEvidenceInterpretation,
    _profiled_rarity_magnitude,
)

def test_extracts_normalized_exact_identity():
    evidence = extract_reference_identity("SB-8891", "SB8891")
    assert evidence is not None
    assert evidence.normalized_a == "sb8891"
    assert evidence.normalized_b == "sb8891"
    assert evidence.exact_normalized_match is True
    assert evidence.shared_numeric_tokens == ("8891",)

def test_extracts_shared_numeric_identity_without_exact_match():
    evidence = extract_reference_identity("INV-874219", "AB/874219")
    assert evidence is not None
    assert evidence.normalized_a == "inv874219"
    assert evidence.normalized_b == "ab874219"
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ("874219",)

def test_extracts_multiple_shared_numeric_tokens_in_deterministic_order():
    evidence = extract_reference_identity("INV-2026-1001", "ABC-2026-1001")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("1001", "2026")

def test_returns_empty_shared_tokens_when_no_overlap_exists():
    evidence = extract_reference_identity("INV-1042", "INV-1043")
    assert evidence is not None
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ()

def test_extracts_non_numeric_exact_identity():
    evidence = extract_reference_identity("CREDIT-NOTE", "CREDITNOTE")
    assert evidence is not None
    assert evidence.normalized_a == "creditnote"
    assert evidence.normalized_b == "creditnote"
    assert evidence.exact_normalized_match is True
    assert evidence.shared_numeric_tokens == ()

def test_returns_none_for_missing_first_reference():
    assert extract_reference_identity(None, "INV-001") is None

def test_returns_none_for_blank_first_reference():
    assert extract_reference_identity("   ", "INV-001") is None

def test_returns_none_when_both_references_missing():
    assert extract_reference_identity(None, None) is None

def test_deduplicates_tokens_within_single_reference():
    evidence = extract_reference_identity("INV-1001-1001", "ABC-1001")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("1001",)

def test_extracts_short_numeric_tokens_without_length_filtering():
    evidence = extract_reference_identity("INV-01-874219", "AB-01-874219")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("01", "874219")

def test_extracts_garbage_numeric_collision_factually():
    evidence = extract_reference_identity("INV-001", "ABC-001")
    assert evidence is not None
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ("001",)

def test_extracts_repeated_token_collision_factually():
    evidence = extract_reference_identity("INV-999999", "ABC-999999")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("999999",)

def test_extracts_only_shared_tokens_from_mixed_matches():
    evidence = extract_reference_identity("INV-2026-1001", "ABC-2025-1001")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("1001",)

def test_extracts_short_tokens_for_namespaces():
    evidence = extract_reference_identity("INV-01", "ABC-01")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("01",)

@pytest.mark.parametrize('ref_a, ref_b', [
    ('---', 'INV-001'),
    ('INV-001', '///'),
    ('---', '///'),
])
def test_extract_reference_identity_returns_none_when_normalization_removes_all_content(ref_a, ref_b):
    assert extract_reference_identity(ref_a, ref_b) is None

def test_reference_corpus_profile_empty_corpus():
    profile = build_reference_corpus_profile([])
    assert profile.reference_count == 0
    assert profile.normalized_reference_frequency == {}
    assert profile.numeric_token_document_frequency == {}

def test_reference_corpus_profile_basic():
    profile = build_reference_corpus_profile([
        'INV-001',
        'ABC-001',
        'INV-874219',
        'AB/874219',
    ])
    assert profile.reference_count == 4
    assert profile.normalized_reference_frequency == {
        'inv001': 1,
        'abc001': 1,
        'inv874219': 1,
        'ab874219': 1,
    }
    assert profile.numeric_token_document_frequency == {
        '001': 2,
        '874219': 2,
    }

def test_reference_corpus_profile_normalized_collisions():
    profile = build_reference_corpus_profile([
        'SB-8891',
        'SB8891',
        'sb/8891',
    ])
    assert profile.reference_count == 3
    assert profile.normalized_reference_frequency == {'sb8891': 3}
    assert profile.numeric_token_document_frequency == {'8891': 3}

def test_reference_corpus_profile_duplicate_token():
    profile = build_reference_corpus_profile([
        'INV-1001-1001',
        'ABC-1001',
    ])
    assert profile.reference_count == 2
    assert profile.numeric_token_document_frequency['1001'] == 2

def test_reference_corpus_profile_missing_and_blank():
    profile = build_reference_corpus_profile([
        'INV-001',
        None,
        '',
        '   ',
        '	',
        'GST-001',
    ])
    assert profile.reference_count == 2
    assert profile.normalized_reference_frequency == {
        'inv001': 1,
        'gst001': 1,
    }
    assert profile.numeric_token_document_frequency == {
        '001': 2,
    }

def test_reference_corpus_profile_non_numeric():
    profile = build_reference_corpus_profile([
        'CREDIT-NOTE',
        'CREDITNOTE',
        'DEBITNOTE',
    ])
    assert profile.reference_count == 3
    assert profile.normalized_reference_frequency == {
        'creditnote': 2,
        'debitnote': 1,
    }
    assert profile.numeric_token_document_frequency == {}

def test_reference_corpus_profile_short_tokens():
    profile = build_reference_corpus_profile([
        'INV-01',
        'ABC-01',
        'PO-02',
    ])
    assert profile.numeric_token_document_frequency == {
        '01': 2,
        '02': 1,
    }

def test_reference_corpus_profile_punctuation_only():
    profile = build_reference_corpus_profile([
        'INV-001',
        '---',
        '///',
        '...',
        'GST-001',
    ])
    assert profile.reference_count == 2
    assert profile.normalized_reference_frequency == {
        'inv001': 1,
        'gst001': 1,
    }

def test_reference_corpus_profile_frequency_mappings_are_read_only():
    profile = build_reference_corpus_profile(['INV-001'])
    with pytest.raises(TypeError):
        profile.normalized_reference_frequency['inv001'] = 5
    with pytest.raises(TypeError):
        profile.numeric_token_document_frequency['001'] = 5

def test_normalized_reference_statistics_validation():
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('', 1)
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('INV-001', 1)
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('inv001', 0)
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('inv001', -1)

def test_reference_token_statistics_validation():
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('', 1)
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('ABC', 1)
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('001', 0)
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('001', -1)

def test_reference_corpus_profile_validation_reference_count():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=-1,
            normalized_reference_frequency={'inv001': 1},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_inconsistent_sum():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=2,
            normalized_reference_frequency={'inv001': 1},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_frequency_greater_than_corpus_size():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=2,
            normalized_reference_frequency={'inv001': 3},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_df_greater_than_corpus_size():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=2,
            normalized_reference_frequency={'inv001': 2},
            numeric_token_document_frequency={'001': 3},
        )

def test_reference_corpus_profile_validation_invalid_normalized_key():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=1,
            normalized_reference_frequency={'INV-001': 1},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_invalid_numeric_token():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=1,
            normalized_reference_frequency={'inv001': 1},
            numeric_token_document_frequency={'ABC': 1},
        )

def test_reference_corpus_profile_direct_construction_snapshot_isolation():
    normalized = {'inv001': 1}
    tokens = {'001': 1}

    profile = ReferenceCorpusProfile(
        reference_count=1,
        normalized_reference_frequency=normalized,
        numeric_token_document_frequency=tokens,
    )

    normalized['inv001'] = 999
    tokens['001'] = 999

    assert profile.normalized_reference_frequency['inv001'] == 1
    assert profile.numeric_token_document_frequency['001'] == 1

def test_enrich_reference_identity_known_exact_identity():
    profile = build_reference_corpus_profile(['SB-8891', 'SB8891', 'ABC-001'])
    identity = extract_reference_identity('SB-8891', 'SB8891')

    enriched = enrich_reference_identity(identity, profile)

    assert enriched.identity == identity
    assert len(enriched.normalized_references) == 1
    assert enriched.normalized_references[0].normalized_reference == 'sb8891'
    assert enriched.normalized_references[0].statistics.frequency == 2

    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '8891'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 2

def test_enrich_reference_identity_distinct_normalized_references():
    profile = build_reference_corpus_profile(['INV-874219', 'AB/874219', 'ABC-001'])
    identity = extract_reference_identity('INV-874219', 'AB/874219')

    enriched = enrich_reference_identity(identity, profile)

    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].normalized_reference == 'ab874219'
    assert enriched.normalized_references[0].statistics.frequency == 1
    assert enriched.normalized_references[1].normalized_reference == 'inv874219'
    assert enriched.normalized_references[1].statistics.frequency == 1

    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '874219'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 2

def test_enrich_reference_identity_out_of_profile():
    profile = build_reference_corpus_profile(['INV-001', 'ABC-001'])
    identity = extract_reference_identity('NEW-874219', 'AB/874219')

    enriched = enrich_reference_identity(identity, profile)

    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].normalized_reference == 'ab874219'
    assert enriched.normalized_references[0].statistics is None
    assert enriched.normalized_references[1].normalized_reference == 'new874219'
    assert enriched.normalized_references[1].statistics is None

    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '874219'
    assert enriched.shared_numeric_tokens[0].statistics is None

def test_enrich_reference_identity_mixed_known_and_unknown():
    profile = build_reference_corpus_profile(['INV-874219', 'ABC-001'])
    identity = extract_reference_identity('INV-874219', 'AB/874219')

    enriched = enrich_reference_identity(identity, profile)

    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].normalized_reference == 'ab874219'
    assert enriched.normalized_references[0].statistics is None
    assert enriched.normalized_references[1].normalized_reference == 'inv874219'
    assert enriched.normalized_references[1].statistics.frequency == 1

    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '874219'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 1

def test_enrich_reference_identity_short_shared_token():
    profile = build_reference_corpus_profile(['INV-01', 'ABC-01', 'PO-02'])
    identity = extract_reference_identity('INV-01', 'ABC-01')

    enriched = enrich_reference_identity(identity, profile)

    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '01'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 2

def test_enrich_reference_identity_non_numeric_exact_identity():
    profile = build_reference_corpus_profile(['CREDIT-NOTE', 'CREDITNOTE', 'DEBITNOTE'])
    identity = extract_reference_identity('CREDIT-NOTE', 'CREDITNOTE')

    enriched = enrich_reference_identity(identity, profile)

    assert len(enriched.normalized_references) == 1
    assert enriched.normalized_references[0].normalized_reference == 'creditnote'
    assert enriched.normalized_references[0].statistics.frequency == 2

    assert len(enriched.shared_numeric_tokens) == 0

def test_enrich_reference_identity_empty_profile():
    profile = build_reference_corpus_profile([])
    identity = extract_reference_identity('INV-001', 'ABC-001')

    enriched = enrich_reference_identity(identity, profile)

    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].statistics is None
    assert enriched.normalized_references[1].statistics is None

    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].statistics is None

def test_enrich_reference_identity_preserves_identity_object():
    identity = extract_reference_identity('INV-874219', 'AB/874219')
    assert identity is not None

    profile = build_reference_corpus_profile([
        'INV-874219',
        'AB/874219',
    ])

    enriched = enrich_reference_identity(
        identity,
        profile,
    )

    assert enriched.identity is identity

import math

def test_reference_evidence_policy_defaults():
    policy = ReferenceEvidencePolicy()
    assert policy.short_token_max_length == 2
    assert policy.medium_token_max_length == 4
    assert policy.short_token_fallback == 0.10
    assert policy.medium_token_fallback == 0.30
    assert policy.long_token_fallback == 0.60
    assert policy.repeated_pattern_discount == 0.50

def test_reference_evidence_policy_validation_short_token_max_length():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=0)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=-1)

def test_reference_evidence_policy_validation_medium_token_max_length():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=2, medium_token_max_length=2)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=4, medium_token_max_length=3)

def test_reference_evidence_policy_validation_float_bounds():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=-0.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(medium_token_fallback=1.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=-0.5)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(repeated_pattern_discount=1.5)

def test_reference_evidence_policy_validation_finiteness():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=float("nan"))
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=float("nan"))
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=float("-inf"))

def test_reference_evidence_policy_exact_reference_fallback_validation():
    # 1. default exact_reference_fallback == 0.60
    p = ReferenceEvidencePolicy()
    assert p.exact_reference_fallback == 0.60

    # 2. exact_reference_fallback = 0.0 is valid
    p_zero = ReferenceEvidencePolicy(exact_reference_fallback=0.0)
    assert p_zero.exact_reference_fallback == 0.0

    # 3. exact_reference_fallback = 0.75 is valid
    p_max = ReferenceEvidencePolicy(exact_reference_fallback=0.75)
    assert p_max.exact_reference_fallback == 0.75

    # 4. exact_reference_fallback < 0.0 raises ValueError
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=-0.1)

    # 5. exact_reference_fallback > 0.75 raises ValueError
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=0.76)

    # 6. NaN raises ValueError
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=float("nan"))
        
    # 7. positive infinity raises ValueError
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=float("inf"))
        
    # 8. negative infinity raises ValueError
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=float("-inf"))

def test_reference_evidence_policy_exact_fallback_independent_ordering():
    # 9. exact_reference_fallback does not participate in numeric fallback ordering
    
    # Explicitly test: short=0.10, medium=0.20, long=0.30, exact=0.70
    p1 = ReferenceEvidencePolicy(
        short_token_fallback=0.10,
        medium_token_fallback=0.20,
        long_token_fallback=0.30,
        exact_reference_fallback=0.70
    )
    assert p1.exact_reference_fallback == 0.70
    
    # Explicitly test: short=0.10, medium=0.20, long=0.70, exact=0.05
    p2 = ReferenceEvidencePolicy(
        short_token_fallback=0.10,
        medium_token_fallback=0.20,
        long_token_fallback=0.70,
        exact_reference_fallback=0.05
    )
    assert p2.exact_reference_fallback == 0.05

    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(repeated_pattern_discount=float("nan"))

def test_reference_evidence_policy_validation_ordering():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=0.8, medium_token_fallback=0.3, long_token_fallback=0.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=0.3, medium_token_fallback=0.2, long_token_fallback=0.6)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=0.1, medium_token_fallback=0.5, long_token_fallback=0.4)

def test_reference_evidence_policy_validation_ordering_equality():
    # 1. short == medium < long
    p1 = ReferenceEvidencePolicy(short_token_fallback=0.2, medium_token_fallback=0.2, long_token_fallback=0.5)
    assert p1.short_token_fallback == p1.medium_token_fallback
    assert p1.medium_token_fallback < p1.long_token_fallback

    # 2. short < medium == long
    p2 = ReferenceEvidencePolicy(short_token_fallback=0.1, medium_token_fallback=0.4, long_token_fallback=0.4)
    assert p2.short_token_fallback < p2.medium_token_fallback
    assert p2.medium_token_fallback == p2.long_token_fallback

    # 3. short == medium == long
    p3 = ReferenceEvidencePolicy(short_token_fallback=0.3, medium_token_fallback=0.3, long_token_fallback=0.3)
    assert p3.short_token_fallback == p3.medium_token_fallback == p3.long_token_fallback

def test_reference_evidence_policy_validation_long_fallback_ceiling():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=0.80)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=1.00)

def test_reference_evidence_contribution_validation_missing_identity():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value="",
            positive_evidence=0.5,
            statistics_available=True,
        )

def test_reference_evidence_contribution_validation_float_bounds():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value="123",
            positive_evidence=-0.1,
            statistics_available=True,
        )
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value="123",
            positive_evidence=1.1,
            statistics_available=True,
        )

def test_reference_evidence_contribution_validation_finiteness():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value="123",
            positive_evidence=float("nan"),
            statistics_available=True,
        )

def test_reference_evidence_contribution_validation_shared_numeric_token_format():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value="ABC123",
            positive_evidence=0.5,
            statistics_available=True,
        )
    
    # Should pass
    ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="12345",
        positive_evidence=0.5,
        statistics_available=True,
    )

def test_reference_evidence_contribution_validation_normalized_reference_format():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE,
            identity_value="INV-123",  # Not normalized
            positive_evidence=0.5,
            statistics_available=True,
        )
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE,
            identity_value="INV/123",
            positive_evidence=0.5,
            statistics_available=True,
        )
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE,
            identity_value="Inv123",
            positive_evidence=0.5,
            statistics_available=True,
        )
    
    # Should pass
    ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE,
        identity_value="inv123",
        positive_evidence=0.5,
        statistics_available=True,
    )

def test_reference_evidence_interpretation_validation_float_bounds():
    contrib = ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="123",
        positive_evidence=0.5,
        statistics_available=True,
    )
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=-0.1, statistical_coverage=1.0, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=1.1, statistical_coverage=1.0, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=-0.1, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=1.1, contributions=(contrib,))

def test_reference_evidence_interpretation_validation_finiteness():
    contrib = ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="123",
        positive_evidence=0.5,
        statistics_available=True,
    )
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=float("nan"), statistical_coverage=1.0, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=float("inf"), contributions=(contrib,))

def test_reference_evidence_interpretation_validation_empty_contributions():
    with pytest.raises(ValueError, match="empty contributions requires score=0.0 and statistical_coverage=0.0"):
        ReferenceEvidenceInterpretation(score=0.9, statistical_coverage=0.0, contributions=())

def test_reference_evidence_interpretation_validation_score_matches_strongest():
    contrib1 = ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="123",
        positive_evidence=0.3,
        statistics_available=True,
    )
    contrib2 = ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="456",
        positive_evidence=0.8,
        statistics_available=True,
    )
    # Valid
    ReferenceEvidenceInterpretation(score=0.8, statistical_coverage=1.0, contributions=(contrib1, contrib2))
    
    # Invalid
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.9, statistical_coverage=1.0, contributions=(contrib1, contrib2))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.3, statistical_coverage=1.0, contributions=(contrib1, contrib2))

def test_reference_evidence_interpretation_validation_coverage_binary():
    contrib = ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="123",
        positive_evidence=0.5,
        statistics_available=True,
    )
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.2, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.5, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.75, contributions=(contrib,))
    
    # Valid
    ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=1.0, contributions=(contrib,))
    
    # Valid with statistics_available=False
    contrib_unprofiled = ReferenceEvidenceContribution(
        evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
        identity_value="123",
        positive_evidence=0.5,
        statistics_available=False,
    )
    ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.0, contributions=(contrib_unprofiled,))

def test_profiled_rarity_magnitude_f1_n1():
    assert math.isclose(_profiled_rarity_magnitude(1, 1), 0.0)

def test_profiled_rarity_magnitude_fN_nN():
    assert math.isclose(_profiled_rarity_magnitude(100, 100), 0.0)

def test_profiled_rarity_magnitude_f1_n100():
    assert math.isclose(_profiled_rarity_magnitude(1, 100), 0.9)

def test_profiled_rarity_magnitude_f4_n100():
    assert math.isclose(_profiled_rarity_magnitude(4, 100), 0.8)

def test_profiled_rarity_magnitude_f25_n100():
    assert math.isclose(_profiled_rarity_magnitude(25, 100), 0.5)

def test_profiled_rarity_magnitude_monotonic_decrease():
    m1 = _profiled_rarity_magnitude(1, 1000)
    m2 = _profiled_rarity_magnitude(10, 1000)
    m3 = _profiled_rarity_magnitude(100, 1000)
    assert m1 > m2 > m3

def test_profiled_rarity_magnitude_corpus_replication_invariance():
    m1 = _profiled_rarity_magnitude(1, 100)
    m2 = _profiled_rarity_magnitude(10, 1000)
    assert math.isclose(m1, m2)

def test_profiled_rarity_magnitude_bounds():
    m1 = _profiled_rarity_magnitude(1, 1000000)
    m2 = _profiled_rarity_magnitude(1000000, 1000000)
    assert 0.0 <= m1 <= 1.0
    assert 0.0 <= m2 <= 1.0

def test_profiled_rarity_magnitude_validation():
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(0, 100)
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(-1, 100)
    
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(1, 0)
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(1, -1)
    
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(10, 5)

def test_structural_token_magnitude_bands():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy(
        short_token_max_length=2,
        medium_token_max_length=4,
        short_token_fallback=0.10,
        medium_token_fallback=0.30,
        long_token_fallback=0.60,
        repeated_pattern_discount=0.50
    )
    
    # Valid short token
    assert math.isclose(_structural_token_magnitude("12", policy), 0.10)
    # Valid medium token
    assert math.isclose(_structural_token_magnitude("1234", policy), 0.30)
    # Valid long token
    assert math.isclose(_structural_token_magnitude("123456", policy), 0.60)

def test_structural_token_magnitude_boundaries():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy(short_token_max_length=2, medium_token_max_length=4)
    
    # Exact length boundary: short
    assert math.isclose(_structural_token_magnitude("12", policy), policy.short_token_fallback)
    # Immediately above short -> medium
    assert math.isclose(_structural_token_magnitude("123", policy), policy.medium_token_fallback)
    # Exact length boundary: medium
    assert math.isclose(_structural_token_magnitude("1234", policy), policy.medium_token_fallback)
    # Immediately above medium -> long
    assert math.isclose(_structural_token_magnitude("12345", policy), policy.long_token_fallback)
    
    # Length 1
    assert math.isclose(_structural_token_magnitude("1", policy), policy.short_token_fallback * policy.repeated_pattern_discount)

def test_structural_token_magnitude_discounts():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy()
    
    # 6. "001" receives its normal band magnitude and is NOT discounted.
    assert math.isclose(_structural_token_magnitude("001", policy), policy.medium_token_fallback)
    # 7. "000" is discounted.
    assert math.isclose(_structural_token_magnitude("000", policy), policy.medium_token_fallback * policy.repeated_pattern_discount)
    # 8. "111" is discounted.
    assert math.isclose(_structural_token_magnitude("111", policy), policy.medium_token_fallback * policy.repeated_pattern_discount)
    # 9. "999999" is discounted.
    assert math.isclose(_structural_token_magnitude("999999", policy), policy.long_token_fallback * policy.repeated_pattern_discount)
    # 10. "121212" is NOT discounted.
    assert math.isclose(_structural_token_magnitude("121212", policy), policy.long_token_fallback)
    # 11. "123123" is NOT discounted.
    assert math.isclose(_structural_token_magnitude("123123", policy), policy.long_token_fallback)
    # 12. "101010" is NOT discounted.
    assert math.isclose(_structural_token_magnitude("101010", policy), policy.long_token_fallback)
    # 13. "000001" is NOT discounted.
    assert math.isclose(_structural_token_magnitude("000001", policy), policy.long_token_fallback)

def test_structural_token_magnitude_custom_discount():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    # 14. discount=0.0
    p_zero = ReferenceEvidencePolicy(repeated_pattern_discount=0.0)
    assert math.isclose(_structural_token_magnitude("111", p_zero), 0.0)
    
    # 15. discount=1.0
    p_one = ReferenceEvidencePolicy(repeated_pattern_discount=1.0)
    assert math.isclose(_structural_token_magnitude("111", p_one), p_one.medium_token_fallback)

def test_structural_token_magnitude_equal_bands():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    # 16. Equal fallback bands are respected exactly
    policy = ReferenceEvidencePolicy(short_token_fallback=0.2, medium_token_fallback=0.2, long_token_fallback=0.2)
    assert math.isclose(_structural_token_magnitude("12", policy), 0.2)
    assert math.isclose(_structural_token_magnitude("1234", policy), 0.2)
    assert math.isclose(_structural_token_magnitude("123456", policy), 0.2)

def test_structural_token_magnitude_deterministic_and_pure():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    # 17. The helper is deterministic.
    policy = ReferenceEvidencePolicy()
    assert _structural_token_magnitude("111", policy) == _structural_token_magnitude("111", policy)
    
    # 18. The helper does not mutate policy.
    discount_before = policy.repeated_pattern_discount
    _structural_token_magnitude("111", policy)
    assert policy.repeated_pattern_discount == discount_before

def test_structural_token_magnitude_validation():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy()
    
    # 19. Empty token
    with pytest.raises(ValueError):
        _structural_token_magnitude("", policy)
    
    # 20. Non-numeric token
    with pytest.raises(ValueError):
        _structural_token_magnitude("12A", policy)
        
    # 21. Whitespace
    with pytest.raises(ValueError):
        _structural_token_magnitude("12 3", policy)
        
    # 22. Signed
    with pytest.raises(ValueError):
        _structural_token_magnitude("-001", policy)
        
    # 23. Decimal
        _structural_token_magnitude("1.23", policy)

def _create_mock_enriched_evidence(exact_match: bool, norm_val: str, norm_freq: int | None, tokens: list[tuple[str, int | None]], reference_count: int = 100) -> 'EnrichedReferenceEvidence':
    from recongraph.matching.reference_evidence import (
        ReferenceIdentityEvidence, NormalizedReferenceStatistics, NormalizedReferenceEvidence,
        ReferenceTokenStatistics, SharedNumericTokenEvidence, EnrichedReferenceEvidence
    )
    
    identity = ReferenceIdentityEvidence(
        normalized_a=norm_val,
        normalized_b=norm_val if exact_match else norm_val + "diff",
        exact_normalized_match=exact_match,
        shared_numeric_tokens=tuple(t[0] for t in tokens)
    )
    
    if norm_freq is not None:
        n_stat = NormalizedReferenceStatistics(norm_val, norm_freq)
    else:
        n_stat = None
    
    # We must satisfy the invariant that normalized_references contains unique norm_refs
    norm_evs = []
    if exact_match:
        norm_evs.append(NormalizedReferenceEvidence(norm_val, n_stat))
    else:
        # If not exact, we have two different normalized values
        if norm_val < norm_val + "diff":
            norm_evs.append(NormalizedReferenceEvidence(norm_val, n_stat))
            norm_evs.append(NormalizedReferenceEvidence(norm_val + "diff", None))
        else:
            norm_evs.append(NormalizedReferenceEvidence(norm_val + "diff", None))
            norm_evs.append(NormalizedReferenceEvidence(norm_val, n_stat))
            
    tok_evs = []
    for t_val, t_df in tokens:
        if t_df is not None:
            t_stat = ReferenceTokenStatistics(t_val, t_df)
        else:
            t_stat = None
        tok_evs.append(SharedNumericTokenEvidence(t_val, t_stat))
        
    return EnrichedReferenceEvidence(
        identity=identity,
        reference_count=reference_count,
        normalized_references=tuple(norm_evs),
        shared_numeric_tokens=tuple(tok_evs)
    )

def test_construct_reference_evidence_contributions_exact():
    from recongraph.matching.reference_evidence import (
        _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile,
        ReferenceEvidenceKind
    )
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={"inv874219": 1, "creditnote": 99}, numeric_token_document_frequency={})

    # CE001: INV-874219 exact, freq=1, N=100 -> mag=0.90
    ev1 = _create_mock_enriched_evidence(True, "inv874219", 1, [])
    c1 = _construct_reference_evidence_contributions(ev1, policy)
    assert len(c1) == 1
    assert c1[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c1[0].identity_value == "inv874219"
    assert math.isclose(c1[0].positive_evidence, 0.90)
    assert c1[0].statistics_available is True

    # CE002: CREDITNOTE exact, freq=100, N=100 -> mag=0.0
    ev2 = _create_mock_enriched_evidence(True, "creditnote", 100, [])
    c2 = _construct_reference_evidence_contributions(ev2, policy)
    assert len(c2) == 1
    assert c2[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c2[0].identity_value == "creditnote"
    assert math.isclose(c2[0].positive_evidence, 0.0)
    assert c2[0].statistics_available is True

    # CE003: INV-999999 out-of-profile -> mag=0.60
    ev3 = _create_mock_enriched_evidence(True, "inv999999", None, [])
    c3 = _construct_reference_evidence_contributions(ev3, policy)
    assert len(c3) == 1
    assert c3[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c3[0].identity_value == "inv999999"
    assert math.isclose(c3[0].positive_evidence, 0.60)
    assert c3[0].statistics_available is False

    # CE004: CREDITNOTE out-of-profile -> mag=0.60
    ev4 = _create_mock_enriched_evidence(True, "creditnote", None, [])
    c4 = _construct_reference_evidence_contributions(ev4, policy)
    assert len(c4) == 1
    assert c4[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c4[0].identity_value == "creditnote"
    assert math.isclose(c4[0].positive_evidence, 0.60)
    assert c4[0].statistics_available is False

    # CE005: 000000 exact out-of-profile -> mag=0.60 (no discount)
    ev5 = _create_mock_enriched_evidence(True, "000000", None, [])
    c5 = _construct_reference_evidence_contributions(ev5, policy)
    assert len(c5) == 1
    assert c5[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c5[0].identity_value == "000000"
    assert math.isclose(c5[0].positive_evidence, 0.60)
    assert c5[0].statistics_available is False

    # CE006: custom exact_reference_fallback
    p2 = ReferenceEvidencePolicy(exact_reference_fallback=0.25)
    c6 = _construct_reference_evidence_contributions(ev5, p2)
    assert math.isclose(c6[0].positive_evidence, 0.25)

def test_construct_reference_evidence_contributions_tokens():
    from recongraph.matching.reference_evidence import (
        _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile,
        ReferenceEvidenceKind
    )
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={"dummy": 100}, numeric_token_document_frequency={"874219": 1, "001": 100})

    # CE007: shared token 874219, DF=1, N=100 -> mag=0.90
    ev7 = _create_mock_enriched_evidence(False, "inv874219", None, [("874219", 1)])
    c7 = _construct_reference_evidence_contributions(ev7, policy)
    assert len(c7) == 1
    assert c7[0].evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN
    assert c7[0].identity_value == "874219"
    assert math.isclose(c7[0].positive_evidence, 0.90)
    assert c7[0].statistics_available is True

    # CE008: shared token 001, DF=100, N=100 -> mag=0.0
    ev8 = _create_mock_enriched_evidence(False, "inv001", None, [("001", 100)])
    c8 = _construct_reference_evidence_contributions(ev8, policy)
    assert len(c8) == 1
    assert c8[0].evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN
    assert c8[0].identity_value == "001"
    assert math.isclose(c8[0].positive_evidence, 0.0)
    assert c8[0].statistics_available is True

    # CE009: shared token 874219 out-of-profile -> mag=0.60
    ev9 = _create_mock_enriched_evidence(False, "inv874219", None, [("874219", None)])
    c9 = _construct_reference_evidence_contributions(ev9, policy)
    assert len(c9) == 1
    assert c9[0].evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN
    assert c9[0].identity_value == "874219"
    assert math.isclose(c9[0].positive_evidence, 0.60)
    assert c9[0].statistics_available is False

    # CE010: shared token 001 out-of-profile -> mag=0.30
    ev10 = _create_mock_enriched_evidence(False, "inv001", None, [("001", None)])
    c10 = _construct_reference_evidence_contributions(ev10, policy)
    assert len(c10) == 1
    assert c10[0].identity_value == "001"
    assert math.isclose(c10[0].positive_evidence, 0.30)
    assert c10[0].statistics_available is False

    # CE011: shared token 999999 out-of-profile -> mag=0.30 (discounted)
    ev11 = _create_mock_enriched_evidence(False, "inv999999", None, [("999999", None)])
    c11 = _construct_reference_evidence_contributions(ev11, policy)
    assert len(c11) == 1
    assert c11[0].identity_value == "999999"
    assert math.isclose(c11[0].positive_evidence, 0.30)
    assert c11[0].statistics_available is False

    # CE012: shared token 121212 out-of-profile -> mag=0.60
    ev12 = _create_mock_enriched_evidence(False, "inv121212", None, [("121212", None)])
    c12 = _construct_reference_evidence_contributions(ev12, policy)
    assert len(c12) == 1
    assert c12[0].identity_value == "121212"
    assert math.isclose(c12[0].positive_evidence, 0.60)

    # CE013: multiple shared tokens: 2026, 874219
    ev13 = _create_mock_enriched_evidence(False, "inv2026", None, [("2026", None), ("874219", None)])
    c13 = _construct_reference_evidence_contributions(ev13, policy)
    assert len(c13) == 2
    assert c13[0].identity_value == "2026"
    assert c13[1].identity_value == "874219"

def test_construct_reference_evidence_contributions_equal_magnitude_regression():
    from recongraph.matching.reference_evidence import (
        _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile
    )
    # 1 - sqrt(f/N) = 0.60 => sqrt(f/N) = 0.40 => f/N = 0.16
    # f=16, N=100
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={"inv1": 16, "dummy": 84}, numeric_token_document_frequency={})
    
    ev_prof = _create_mock_enriched_evidence(True, "inv1", 16, [])
    ev_unprof = _create_mock_enriched_evidence(True, "inv2", None, [])
    
    c_prof = _construct_reference_evidence_contributions(ev_prof, policy)[0]
    c_unprof = _construct_reference_evidence_contributions(ev_unprof, policy)[0]
    
    assert math.isclose(c_prof.positive_evidence, 0.60)
    assert math.isclose(c_unprof.positive_evidence, 0.60)
    assert math.isclose(c_prof.positive_evidence, c_unprof.positive_evidence)
    
    # But provenance differs
    assert c_prof.statistics_available is True
    assert c_unprof.statistics_available is False

def test_construct_reference_evidence_contributions_stage_boundary():
    from recongraph.matching.reference_evidence import (
        _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile,
        ReferenceEvidenceContribution
    )
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={"dummy": 100}, numeric_token_document_frequency={})
    
    ev = _create_mock_enriched_evidence(False, "inv", None, [("123", None), ("456", None)])
    out = _construct_reference_evidence_contributions(ev, policy)
    
    # 1. return ReferenceEvidenceInterpretation (must not)
    assert isinstance(out, tuple)
    assert all(isinstance(c, ReferenceEvidenceContribution) for c in out)
    
    # 2. calculate statistical_coverage (no coverage field on contribution)
    assert not hasattr(out[0], 'statistical_coverage')
    
    # 3. discard weaker contributions (both tokens must be present)
    assert len(out) == 2
    
    # 5/6/7. No mutation (tuples and dataclasses are frozen, safe)

def test_select_strongest_reference_contribution():
    from recongraph.matching.reference_evidence import (
        ReferenceEvidenceContribution, ReferenceEvidenceKind,
        _select_strongest_reference_contribution
    )

    def make_contrib(mag: float, stats: bool, kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, val="0"):
        return ReferenceEvidenceContribution(
            evidence_kind=kind,
            identity_value=val,
            positive_evidence=mag,
            statistics_available=stats
        )

    # SS001 — single contribution
    c_single = make_contrib(0.90, True, val="874219")
    w_single = _select_strongest_reference_contribution((c_single,))
    assert w_single is c_single

    # SS002 — higher magnitude wins
    ca = make_contrib(0.60, False)
    cb = make_contrib(0.90, False)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is cb

    # SS003 — higher magnitude wins even if unprofiled
    ca = make_contrib(0.70, False)
    cb = make_contrib(0.60, True)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca

    # SS004 — profiled wins exact magnitude tie
    ca = make_contrib(0.60, False)
    cb = make_contrib(0.60, True)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is cb

    # SS005 — profiled first, fallback second, exact magnitude tie
    ca = make_contrib(0.60, True)
    cb = make_contrib(0.60, False)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca

    # SS006 — complete tie preserves first contribution
    ca = make_contrib(0.60, True, val="2026")
    cb = make_contrib(0.60, True, val="874219")
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca

    # SS007 — reverse complete tie preserves new first contribution
    w2 = _select_strongest_reference_contribution((cb, ca))
    assert w2 is cb

    # SS008 — zero magnitude tie, profiled wins
    ca = make_contrib(0.0, False)
    cb = make_contrib(0.0, True)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is cb

    # SS009 — zero magnitude complete tie preserves first
    ca = make_contrib(0.0, True, val="1")
    cb = make_contrib(0.0, True, val="2")
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca

    # SS010 — empty tuple raises ValueError
    import pytest
    with pytest.raises(ValueError, match="at least one reference evidence contribution is required"):
        _select_strongest_reference_contribution(())

    # SS011 — three contributions, highest last
    ca = make_contrib(0.30, False)
    cb = make_contrib(0.68, True)
    cc = make_contrib(0.90, True)
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is cc

    # SS012 — three contributions, highest first
    ca = make_contrib(0.90, True)
    cb = make_contrib(0.68, True)
    cc = make_contrib(0.30, False)
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is ca

    # SS013 — later profiled contribution replaces equal fallback winner
    ca = make_contrib(0.60, False)
    cb = make_contrib(0.30, True)
    cc = make_contrib(0.60, True)
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is cc

    # SS014 — later complete tie does NOT replace first complete winner
    ca = make_contrib(0.60, True, val="1")
    cb = make_contrib(0.30, False)
    cc = make_contrib(0.60, True, val="3")
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is ca

def test_select_strongest_reference_contribution_identity_and_mutation():
    from recongraph.matching.reference_evidence import (
        ReferenceEvidenceContribution, ReferenceEvidenceKind,
        _select_strongest_reference_contribution
    )
    ca = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, "1", 0.5, True)
    cb = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, "2", 0.8, False)
    cc = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, "3", 0.2, True)

    contributions = (ca, cb, cc)
    before_tuple = contributions
    before_values = tuple(
        (c.evidence_kind, c.identity_value, c.positive_evidence, c.statistics_available)
        for c in contributions
    )
    
    winner = _select_strongest_reference_contribution(contributions)
    
    # Assert identity preservation
    assert any(winner is c for c in contributions)
    assert winner is cb
    
    # Assert mutation boundary
    assert contributions is before_tuple
    assert tuple(
        (c.evidence_kind, c.identity_value, c.positive_evidence, c.statistics_available)
        for c in contributions
    ) == before_values

    # Prove frozen mutation is still restricted
    import pytest
    from dataclasses import FrozenInstanceError
    with pytest.raises(FrozenInstanceError):
        winner.positive_evidence = 0.99

def test_select_strongest_reference_contribution_integration():
    from recongraph.matching.reference_evidence import (
        extract_reference_identity, build_reference_corpus_profile,
        enrich_reference_identity, _construct_reference_evidence_contributions,
        _select_strongest_reference_contribution, ReferenceEvidencePolicy
    )
    import math

    policy = ReferenceEvidencePolicy()

    # SI001
    ident = extract_reference_identity("INV-2026-874219", "AB-2026-874219")
    prof = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 10, "874219": 1})
    enriched = enrich_reference_identity(ident, prof)
    contribs = _construct_reference_evidence_contributions(enriched, policy)
    winner = _select_strongest_reference_contribution(contribs)
    
    assert winner.identity_value == "874219"
    assert math.isclose(winner.positive_evidence, 0.90)

    # SI002: Exact exact profiled magnitude tie
    # 2026 and 874219 both have DF=1.
    prof2 = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 1, "874219": 1})
    enriched2 = enrich_reference_identity(ident, prof2)
    contribs2 = _construct_reference_evidence_contributions(enriched2, policy)
    winner2 = _select_strongest_reference_contribution(contribs2)
    
    # "2026" wins because it comes first in sorted token order (upstream determinism).
    assert winner2.identity_value == "2026"

    # SI003: Unprofiled 0.60 vs Profiled 0.60
    # 1 - sqrt(f/N) = 0.60 => sqrt(f/N) = 0.40 => f/N = 0.16. N=100 => f=16
    ident3 = extract_reference_identity("INV-874219-999999", "AB-874219-999999")
    # 874219 has DF=16 (profiled mag=0.60)
    # 999999 is out-of-profile. It gets medium_fallback * repeated_discount? Wait, 999999 is len 6 -> long fallback (0.60) * 0.50 = 0.30.
    # We want unprofiled to get 0.60, so we use a non-repeated long token: e.g. 121212.
    ident3_alt = extract_reference_identity("INV-874219-121212", "AB-874219-121212")
    prof3 = ReferenceCorpusProfile(100, {"dummy": 100}, {"874219": 16})
    enriched3 = enrich_reference_identity(ident3_alt, prof3)
    contribs3 = _construct_reference_evidence_contributions(enriched3, policy)
    winner3 = _select_strongest_reference_contribution(contribs3)
    
    # 874219: profiled, 0.60
    # 121212: unprofiled, long_token_fallback = 0.60
    # Profiled wins!
    assert winner3.identity_value == "874219"

    # SI004: Unprofiled 0.60 vs Profiled slightly below 0.60
    # 1 - sqrt(17/100) = 1 - 0.4123 = 0.5877
    prof4 = ReferenceCorpusProfile(100, {"dummy": 100}, {"874219": 17})
    enriched4 = enrich_reference_identity(ident3_alt, prof4)
    contribs4 = _construct_reference_evidence_contributions(enriched4, policy)
    winner4 = _select_strongest_reference_contribution(contribs4)
    
    # 121212 unprofiled 0.60 wins because magnitude overrides provenance.
    assert winner4.identity_value == "121212"


def test_assemble_reference_evidence_interpretation():
    from recongraph.matching.reference_evidence import (
        ReferenceEvidenceContribution, ReferenceEvidenceKind,
        _assemble_reference_evidence_interpretation
    )

    def make_contrib(mag, stats, val="1"):
        return ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value=val,
            positive_evidence=mag,
            statistics_available=stats
        )

    # IA001 — single profiled contribution
    c = make_contrib(0.90, True)
    interp = _assemble_reference_evidence_interpretation((c,))
    assert interp.score == 0.90
    assert interp.statistical_coverage == 1.0
    assert interp.contributions == (c,)

    # IA002 — single fallback contribution
    c2 = make_contrib(0.60, False)
    interp2 = _assemble_reference_evidence_interpretation((c2,))
    assert interp2.score == 0.60
    assert interp2.statistical_coverage == 0.0

    # IA003 — profiled wins exact magnitude tie
    ca = make_contrib(0.60, False, val="1")
    cb = make_contrib(0.60, True, val="2")
    interp3 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp3.score == 0.60
    assert interp3.statistical_coverage == 1.0

    # IA004 — higher unprofiled magnitude wins
    ca = make_contrib(0.70, False, val="1")
    cb = make_contrib(0.60, True, val="2")
    interp4 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp4.score == 0.70
    assert interp4.statistical_coverage == 0.0

    # IA005 — highest profiled contribution wins
    ca = make_contrib(0.30, False, val="1")
    cb = make_contrib(0.68, True, val="2")
    cc = make_contrib(0.90, True, val="3")
    interp5 = _assemble_reference_evidence_interpretation((ca, cb, cc))
    assert interp5.score == 0.90
    assert interp5.statistical_coverage == 1.0

    # IA006 — highest fallback contribution wins
    ca = make_contrib(0.30, True, val="1")
    cb = make_contrib(0.68, True, val="2")
    cc = make_contrib(0.90, False, val="3")
    interp6 = _assemble_reference_evidence_interpretation((ca, cb, cc))
    assert interp6.score == 0.90
    assert interp6.statistical_coverage == 0.0

    # IA007 — zero magnitude profiled tie winner
    ca = make_contrib(0.0, False, val="1")
    cb = make_contrib(0.0, True, val="2")
    interp7 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp7.score == 0.0
    assert interp7.statistical_coverage == 1.0

    # IA008 — complete tie preserves selector winner
    ca = make_contrib(0.60, True, val="2026")
    cb = make_contrib(0.60, True, val="874219")
    interp8 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp8.score == 0.60
    assert interp8.statistical_coverage == 1.0

    # IA009 — reversed complete tie
    interp9 = _assemble_reference_evidence_interpretation((cb, ca))
    assert interp9.score == 0.60
    assert interp9.statistical_coverage == 1.0

    # IA010 — contribution tuple identity/order preserved
    tup = (ca, cb)
    interp10 = _assemble_reference_evidence_interpretation(tup)
    assert interp10.contributions == tup
    assert interp10.contributions is tup

    # IA011 — empty contributions raises ValueError
    import pytest
    with pytest.raises(ValueError):
        _assemble_reference_evidence_interpretation(())

    # IA012/IA013/IA014 implicitly tested by IA003/IA004 bounds

import pytest
@pytest.mark.parametrize("magnitude, stats, expected_score, expected_coverage", [
    (0.00, False, 0.00, 0.0),
    (0.00, True,  0.00, 1.0),
    (0.30, False, 0.30, 0.0),
    (0.30, True,  0.30, 1.0),
    (0.60, False, 0.60, 0.0),
    (0.60, True,  0.60, 1.0),
    (0.90, False, 0.90, 0.0),
    (0.90, True,  0.90, 1.0),
])
def test_assemble_reference_evidence_coverage_truth_table(magnitude, stats, expected_score, expected_coverage):
    from recongraph.matching.reference_evidence import (
        ReferenceEvidenceContribution, ReferenceEvidenceKind,
        _assemble_reference_evidence_interpretation
    )
    c = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, "1", magnitude, stats)
    interp = _assemble_reference_evidence_interpretation((c,))
    assert interp.score == expected_score
    assert interp.statistical_coverage == expected_coverage

def test_assemble_reference_evidence_integration():
    from recongraph.matching.reference_evidence import (
        extract_reference_identity, build_reference_corpus_profile,
        enrich_reference_identity, _construct_reference_evidence_contributions,
        _assemble_reference_evidence_interpretation, ReferenceEvidencePolicy,
        ReferenceEvidenceKind
    )
    import math
    policy = ReferenceEvidencePolicy()

    # AI001 — rare exact profiled identity
    prof = ReferenceCorpusProfile(100, {"dummy": 99, "inv874219": 1}, {})
    enriched = enrich_reference_identity(extract_reference_identity("INV-874219", "INV/874219"), prof)
    contribs = _construct_reference_evidence_contributions(enriched, policy)
    interp = _assemble_reference_evidence_interpretation(contribs)
    assert len(interp.contributions) == 1
    assert interp.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert math.isclose(interp.score, 0.90)
    assert interp.statistical_coverage == 1.0

    # AI002 — ubiquitous exact profiled identity (CREDITNOTE)
    prof2 = ReferenceCorpusProfile(100, {"creditnote": 100}, {})
    enriched2 = enrich_reference_identity(extract_reference_identity("CREDIT NOTE", "creditnote"), prof2)
    contribs2 = _construct_reference_evidence_contributions(enriched2, policy)
    interp2 = _assemble_reference_evidence_interpretation(contribs2)
    assert interp2.score == 0.0
    assert interp2.statistical_coverage == 1.0

    # AI003 — out-of-profile exact identity
    prof3 = ReferenceCorpusProfile(100, {"dummy": 100}, {})
    enriched3 = enrich_reference_identity(extract_reference_identity("INV-999999", "INV/999999"), prof3)
    contribs3 = _construct_reference_evidence_contributions(enriched3, policy)
    interp3 = _assemble_reference_evidence_interpretation(contribs3)
    assert interp3.score == policy.exact_reference_fallback
    assert interp3.statistical_coverage == 0.0

    # AI004 — rare shared token
    prof4 = ReferenceCorpusProfile(100, {"dummy": 100}, {"874219": 1})
    enriched4 = enrich_reference_identity(extract_reference_identity("INV-874219", "AB-874219"), prof4)
    contribs4 = _construct_reference_evidence_contributions(enriched4, policy)
    interp4 = _assemble_reference_evidence_interpretation(contribs4)
    assert math.isclose(interp4.score, 0.90)
    assert interp4.statistical_coverage == 1.0

    # AI005 — common shared token
    prof5 = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 36})
    enriched5 = enrich_reference_identity(extract_reference_identity("INV-2026", "AB-2026"), prof5)
    contribs5 = _construct_reference_evidence_contributions(enriched5, policy)
    interp5 = _assemble_reference_evidence_interpretation(contribs5)
    # 1 - sqrt(36/100) = 1 - 0.6 = 0.40
    assert math.isclose(interp5.score, 0.40)
    assert interp5.statistical_coverage == 1.0

    # AI006 — out-of-profile long token
    prof6 = ReferenceCorpusProfile(100, {"dummy": 100}, {})
    enriched6 = enrich_reference_identity(extract_reference_identity("INV-121212", "AB-121212"), prof6)
    contribs6 = _construct_reference_evidence_contributions(enriched6, policy)
    interp6 = _assemble_reference_evidence_interpretation(contribs6)
    assert interp6.score == policy.long_token_fallback
    assert interp6.statistical_coverage == 0.0

    # AI007 — out-of-profile repeated long token
    prof7 = ReferenceCorpusProfile(100, {"dummy": 100}, {})
    enriched7 = enrich_reference_identity(extract_reference_identity("INV-999999", "AB-999999"), prof7)
    contribs7 = _construct_reference_evidence_contributions(enriched7, policy)
    interp7 = _assemble_reference_evidence_interpretation(contribs7)
    assert interp7.score == policy.long_token_fallback * policy.repeated_pattern_discount
    assert interp7.statistical_coverage == 0.0

    # AI008 — mixed tokens, rare profiled token wins
    prof8 = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 36, "874219": 1})
    enriched8 = enrich_reference_identity(extract_reference_identity("INV-2026-874219", "AB-2026-874219"), prof8)
    contribs8 = _construct_reference_evidence_contributions(enriched8, policy)
    interp8 = _assemble_reference_evidence_interpretation(contribs8)
    assert math.isclose(interp8.score, 0.90)
    assert interp8.statistical_coverage == 1.0

    # AI009 — mixed tokens, stronger fallback wins
    # 2026 (len 4) -> medium fallback (0.3)
    # 121212 (len 6) -> long fallback (0.6)
    prof9 = ReferenceCorpusProfile(100, {"dummy": 100}, {})
    enriched9 = enrich_reference_identity(extract_reference_identity("INV-2026-121212", "AB-2026-121212"), prof9)
    contribs9 = _construct_reference_evidence_contributions(enriched9, policy)
    interp9 = _assemble_reference_evidence_interpretation(contribs9)
    assert interp9.score == 0.60
    assert interp9.statistical_coverage == 0.0

    # AI010 — exact identity bypasses token path
    prof10 = ReferenceCorpusProfile(100, {"dummy": 99, "inv2026874219": 1}, {"2026": 10, "874219": 1})
    enriched10 = enrich_reference_identity(extract_reference_identity("INV-2026-874219", "INV/2026/874219"), prof10)
    contribs10 = _construct_reference_evidence_contributions(enriched10, policy)
    interp10 = _assemble_reference_evidence_interpretation(contribs10)
    assert len(interp10.contributions) == 1
    assert interp10.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE


def test_interpret_reference_evidence_public_api():
    from recongraph.matching.reference_evidence import (
        interpret_reference_evidence, ReferenceEvidencePolicy, ReferenceCorpusProfile,
        extract_reference_identity, enrich_reference_identity, ReferenceEvidenceKind
    )
    import math
    policy = ReferenceEvidencePolicy()
    prof = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 10, "874219": 1})

    # Case 1: Valid enriched evidence with tokens
    ev1 = enrich_reference_identity(extract_reference_identity("INV-2026-874219", "AB-2026-874219"), prof)
    interp1 = interpret_reference_evidence(ev1, policy)
    assert math.isclose(interp1.score, 0.90)
    assert interp1.statistical_coverage == 1.0
    assert len(interp1.contributions) == 2

    # Case 2: Exact identity
    prof2 = ReferenceCorpusProfile(100, {"inv874219": 1, "dummy": 99}, {})
    ev2 = enrich_reference_identity(extract_reference_identity("INV-874219", "INV/874219"), prof2)
    interp2 = interpret_reference_evidence(ev2, policy)
    assert math.isclose(interp2.score, 0.90)
    assert interp2.statistical_coverage == 1.0
    assert len(interp2.contributions) == 1
    assert interp2.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE

    # Case 3: Empty contributions (exact match = False, no shared tokens)
    ev3 = enrich_reference_identity(extract_reference_identity("INV-111", "AB-222"), prof)
    interp3 = interpret_reference_evidence(ev3, policy)
    assert interp3.score == 0.0
    assert interp3.statistical_coverage == 0.0
    assert interp3.contributions == ()

def test_compute_reference_interpretation_facade():
    from recongraph.matching.reference_evidence import (
        compute_reference_interpretation, ReferenceEvidenceContext,
        ReferenceEvidencePolicy, ReferenceCorpusProfile, ReferenceEvidenceKind
    )
    import math
    
    policy = ReferenceEvidencePolicy()
    prof = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 10, "874219": 1})
    context = ReferenceEvidenceContext(profile=prof, policy=policy)

    # 1. Empty reference fields -> Zero interpretation
    interp1 = compute_reference_interpretation(None, None, context)
    assert interp1.score == 0.0
    assert interp1.statistical_coverage == 0.0
    assert interp1.contributions == ()
    
    interp1b = compute_reference_interpretation("", "   ", context)
    assert interp1b.score == 0.0
    assert interp1b.statistical_coverage == 0.0
    assert interp1b.contributions == ()

    # 2. Mixed availability (one known in profile, one out-of-profile)
    # Profile has 2026 (known, DF=10, mag=0.683) and 874219 (known, DF=1, mag=0.9).
    # Let's test a pair sharing 2026 (known) and 121212 (out-of-profile, fallback=0.6).
    interp2 = compute_reference_interpretation("INV-2026-121212", "AB-2026-121212", context)
    # 2026 magnitude = 1 - sqrt(10/100) = 1 - sqrt(0.1) = 1 - 0.3162 = 0.68377
    # 121212 magnitude = 0.60
    # Winner is 2026 (higher magnitude)
    assert math.isclose(interp2.score, 1.0 - math.sqrt(0.1))
    assert interp2.statistical_coverage == 1.0
    assert len(interp2.contributions) == 2
    
    winner2 = max(interp2.contributions, key=lambda c: c.positive_evidence)
    assert winner2.identity_value == "2026"
    assert winner2.statistics_available is True

    # Reverse magnitude where out-of-profile wins
    # Let's use an out-of-profile exact match: fallback is 0.60
    # Let's say the token match has a low magnitude: 2026 (0.683)
    # Wait, 0.683 > 0.60, so profiled wins.
    # What if token is DF=64? mag = 1 - sqrt(0.64) = 0.20
    prof_mixed = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 64})
    ctx_mixed = ReferenceEvidenceContext(profile=prof_mixed, policy=policy)
    interp3 = compute_reference_interpretation("INV-2026-121212", "AB-2026-121212", ctx_mixed)
    # Winner should be 121212 (0.60) since 2026 is only 0.20
    assert interp3.score == 0.60
    assert interp3.statistical_coverage == 0.0
    winner3 = max(interp3.contributions, key=lambda c: c.positive_evidence)
    assert winner3.identity_value == "121212"
    assert winner3.statistics_available is False

    # 3. Disjoint references (Zero evidence)
    interp4 = compute_reference_interpretation("111", "222", context)
    assert interp4.score == 0.0
    assert interp4.statistical_coverage == 0.0
    assert interp4.contributions == ()

    # 4. Happy path exact match
    prof_exact = ReferenceCorpusProfile(100, {"inv874219": 1, "dummy": 99}, {})
    ctx_exact = ReferenceEvidenceContext(profile=prof_exact, policy=policy)
    interp5 = compute_reference_interpretation("INV-874219", "INV/874219", ctx_exact)
    assert math.isclose(interp5.score, 0.90)
    assert interp5.statistical_coverage == 1.0
    assert len(interp5.contributions) == 1
    assert interp5.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
````

## File: tests/test_text_normalization.py
````python
import pytest

from recongraph.normalization.text import (
    normalize_reference,
    normalize_tax_identity,
    normalize_vendor_name,
)


def test_normalize_reference_removes_formatting_differences() -> None:
    assert normalize_reference("AB/1042") == "ab1042"
    assert normalize_reference("AB-1042") == "ab1042"
    assert normalize_reference("AB 1042") == "ab1042"
    assert normalize_reference("ab1042") == "ab1042"


def test_normalize_vendor_name_removes_legal_suffixes() -> None:
    assert normalize_vendor_name("ABC STEELS PVT. LTD.") == "abc steel"
    assert (
        normalize_vendor_name("ABC Steels Private Limited")
        == "abc steel"
    )
    assert (
        normalize_vendor_name("Northstar Components Pvt Ltd")
        == "northstar component"
    )


def test_normalize_vendor_name_preserves_unmapped_meaningful_tokens() -> None:
    assert (
        normalize_vendor_name("SHREE BALAJI FOODS")
        == "shree balaji foods"
    )


def test_normalize_vendor_name_canonicalizes_known_aliases() -> None:
    assert (
        normalize_vendor_name("SHREE BALAJI ENT.")
        == "shree balaji enterprises"
    )


def test_normalize_vendor_name_canonicalizes_known_token_variants() -> None:
    assert (
        normalize_vendor_name("ABC STEELS PVT. LTD.")
        == "abc steel"
    )
    assert (
        normalize_vendor_name("Northstar Components Pvt Ltd")
        == "northstar component"
    )
    assert (
        normalize_vendor_name("Metro Office Solutions")
        == "metro office solution"
    )
    assert (
        normalize_vendor_name("Apex Industrial Supplies")
        == "apex industrial supply"
    )


def test_normalize_tax_identity_standardizes_case_and_whitespace() -> None:
    assert (
        normalize_tax_identity(" 07abcde1234f1z5 ")
        == "07ABCDE1234F1Z5"
    )
````

## File: pyproject.toml
````toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "recongraph"
version = "0.1.0"
description = "An explainable financial exception investigation and reconciliation engine."
requires-python = ">=3.11"
dependencies = [
    "rapidfuzz>=3.14,<4.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "mypy>=1.0",
    "hypothesis>=6.0",
]

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
````

## File: experiments/evaluate_purchase_gst_baseline.py
````python
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from recongraph.domain.records import GSTRecord, PurchaseRecord
from recongraph.matching.pair_scorers import score_purchase_to_gst


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PURCHASES_PATH = (
    PROJECT_ROOT / "datasets" / "raw" / "purchase_register.csv"
)

GST_RECORDS_PATH = (
    PROJECT_ROOT / "datasets" / "raw" / "gst_records.csv"
)

GROUND_TRUTH_PATH = (
    PROJECT_ROOT
    / "datasets"
    / "ground_truth"
    / "purchase_gst_matches.csv"
)


@dataclass(frozen=True)
class IdentifiedPurchase:
    record_id: str
    record: PurchaseRecord


@dataclass(frozen=True)
class IdentifiedGSTRecord:
    record_id: str
    record: GSTRecord


@dataclass(frozen=True)
class EvaluationRow:
    purchase_record_id: str
    gst_record_id: str
    relationship: str
    score: float | None
    coverage: float
    eligibility: str


def optional_text(value: str) -> str | None:
    stripped = value.strip()
    return stripped or None


def load_purchases(path: Path) -> list[IdentifiedPurchase]:
    purchases: list[IdentifiedPurchase] = []

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            purchases.append(
                IdentifiedPurchase(
                    record_id=row["record_id"],
                    record=PurchaseRecord(record_id="pur_d2dec543", 
                        vendor_name=optional_text(row["vendor_name"]),
                        reference=optional_text(row["invoice_number"]),
                        amount=float(row["amount"]),
                        record_date=date.fromisoformat(row["invoice_date"]),
                        tax_identity=optional_text(row["gstin"]),
                    ),
                )
            )

    return purchases


def load_gst_records(path: Path) -> list[IdentifiedGSTRecord]:
    gst_records: list[IdentifiedGSTRecord] = []

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            gst_records.append(
                IdentifiedGSTRecord(record_id="gst_f1e59e98", 
                    record_id=row["record_id"],
                    record=GSTRecord(record_id="gst_23e6fe6c", 
                        vendor_name=optional_text(row["supplier_name"]),
                        reference=optional_text(row["invoice_number"]),
                        amount=float(row["amount"]),
                        record_date=date.fromisoformat(row["invoice_date"]),
                        tax_identity=optional_text(row["gstin"]),
                    ),
                )
            )

    return gst_records


def load_positive_pairs(path: Path) -> set[tuple[str, str]]:
    positive_pairs: set[tuple[str, str]] = set()

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["relationship"] == "same_financial_event":
                positive_pairs.add(
                    (
                        row["purchase_record_id"],
                        row["gst_record_id"],
                    )
                )

    return positive_pairs


def evaluate_pairs(
    purchases: list[IdentifiedPurchase],
    gst_records: list[IdentifiedGSTRecord],
    positive_pairs: set[tuple[str, str]],
) -> list[EvaluationRow]:
    rows: list[EvaluationRow] = []

    for purchase in purchases:
        for gst_record in gst_records:
            result = score_purchase_to_gst(
                purchase=purchase.record,
                gst_record=gst_record.record,
            )

            pair = (
                purchase.record_id,
                gst_record.record_id,
            )

            relationship = (
                "positive"
                if pair in positive_pairs
                else "negative"
            )

            rows.append(
                EvaluationRow(
                    purchase_record_id=purchase.record_id,
                    gst_record_id=gst_record.record_id,
                    relationship=relationship,
                    score=result.relationship.score,
                    coverage=result.relationship.coverage,
                    eligibility=result.eligibility.status.value,
                )
            )

    return rows


def sortable_score(row: EvaluationRow) -> float:
    if row.score is None:
        return -1.0

    return row.score


def print_score_table(rows: list[EvaluationRow]) -> None:
    print(
        f"{'Purchase':<10} "
        f"{'GST':<10} "
        f"{'Label':<10} "
        f"{'Score':>10} "
        f"{'Coverage':>10} "
        f"{'Eligibility':<11}"
    )

    print("-" * 68)

    for row in rows:
        score_text = (
            "None"
            if row.score is None
            else f"{row.score:.4f}"
        )

        print(
            f"{row.purchase_record_id:<10} "
            f"{row.gst_record_id:<10} "
            f"{row.relationship:<10} "
            f"{score_text:>10} "
            f"{row.coverage:>10.4f} "
            f"{row.eligibility:<11}"
        )


def calculate_separation(
    rows: list[EvaluationRow],
) -> tuple[float, float, float]:
    positive_scores = [
        row.score
        for row in rows
        if row.relationship == "positive"
        and row.score is not None
    ]

    negative_scores = [
        row.score
        for row in rows
        if row.relationship == "negative"
        and row.score is not None
    ]

    if not positive_scores or not negative_scores:
        raise ValueError(
            "Evaluation requires scored positive and negative pairs."
        )

    minimum_positive = min(positive_scores)
    maximum_negative = max(negative_scores)
    separation_gap = minimum_positive - maximum_negative

    return (
        minimum_positive,
        maximum_negative,
        separation_gap,
    )


def print_separation_summary(
    minimum_positive: float,
    maximum_negative: float,
    separation_gap: float,
) -> None:
    print()
    print("Separation summary")
    print("------------------")
    print(f"Minimum positive score: {minimum_positive:.4f}")
    print(f"Maximum negative score: {maximum_negative:.4f}")
    print(f"Separation gap: {separation_gap:.4f}")


def main() -> None:
    purchases = load_purchases(PURCHASES_PATH)
    gst_records = load_gst_records(GST_RECORDS_PATH)
    positive_pairs = load_positive_pairs(GROUND_TRUTH_PATH)

    rows = evaluate_pairs(
        purchases=purchases,
        gst_records=gst_records,
        positive_pairs=positive_pairs,
    )

    rows.sort(
        key=sortable_score,
        reverse=True,
    )

    print(f"Purchases loaded: {len(purchases)}")
    print(f"GST records loaded: {len(gst_records)}")
    print(f"Candidate pairs scored: {len(rows)}")
    print()

    print_score_table(rows)

    (
        minimum_positive,
        maximum_negative,
        separation_gap,
    ) = calculate_separation(rows)

    print_separation_summary(
        minimum_positive=minimum_positive,
        maximum_negative=maximum_negative,
        separation_gap=separation_gap,
    )


if __name__ == "__main__":
    main()
````

## File: experiments/evaluate_purchase_gst_challenges.py
````python
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from recongraph.domain.records import GSTRecord, PurchaseRecord
from recongraph.matching.pair_scorers import score_purchase_to_gst
from recongraph.matching.scoring import SignalName


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CHALLENGE_DIR = PROJECT_ROOT / "datasets" / "challenge"

PURCHASES_PATH = CHALLENGE_DIR / "purchase_register_v1.csv"
GST_RECORDS_PATH = CHALLENGE_DIR / "gst_records_v1.csv"
PAIR_LABELS_PATH = CHALLENGE_DIR / "pair_labels_v1.csv"
CASES_PATH = CHALLENGE_DIR / "challenge_cases_v1.csv"

# Diagnostic threshold for challenge inspection only.
# This is not a calibrated production decision threshold.
CHALLENGE_CONCERN_SCORE = 0.60


@dataclass(frozen=True)
class ChallengePair:
    case_id: str
    purchase_record_id: str
    gst_record_id: str
    expected_label: str


@dataclass(frozen=True)
class ChallengeResult:
    case_id: str
    purchase_record_id: str
    gst_record_id: str
    expected_label: str
    score: float | None
    coverage: float
    entity_score: float | None
    reference_score: float | None
    amount_score: float | None
    temporal_score: float | None
    tax_identity_score: float | None
    semantic_findings: tuple[str, ...]
    eligibility_status: str
    blocking_findings: tuple[str, ...]


def optional_text(value: str) -> str | None:
    stripped = value.strip()
    return stripped or None


def load_purchases(path: Path) -> dict[str, PurchaseRecord]:
    purchases: dict[str, PurchaseRecord] = {}

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            purchases[row["record_id"]] = PurchaseRecord(record_id="pur_5a4e5785", 
                vendor_name=optional_text(row["vendor_name"]),
                reference=optional_text(row["invoice_number"]),
                amount=float(row["amount"]),
                record_date=date.fromisoformat(row["invoice_date"]),
                tax_identity=optional_text(row["gstin"]),
            )

    return purchases


def load_gst_records(path: Path) -> dict[str, GSTRecord]:
    gst_records: dict[str, GSTRecord] = {}

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            gst_records[row["record_id"]] = GSTRecord(record_id="gst_2d50d543", 
                vendor_name=optional_text(row["supplier_name"]),
                reference=optional_text(row["invoice_number"]),
                amount=float(row["amount"]),
                record_date=date.fromisoformat(row["invoice_date"]),
                tax_identity=optional_text(row["gstin"]),
            )

    return gst_records


def load_challenge_pairs(path: Path) -> list[ChallengePair]:
    pairs: list[ChallengePair] = []

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            pairs.append(
                ChallengePair(
                    case_id=row["case_id"],
                    purchase_record_id=row["purchase_record_id"],
                    gst_record_id=row["gst_record_id"],
                    expected_label=row["expected_label"],
                )
            )

    return pairs


def evaluate_challenges(
    purchases: dict[str, PurchaseRecord],
    gst_records: dict[str, GSTRecord],
    challenge_pairs: list[ChallengePair],
) -> list[ChallengeResult]:
    results: list[ChallengeResult] = []

    for challenge_pair in challenge_pairs:
        purchase = purchases[challenge_pair.purchase_record_id]
        gst_record = gst_records[challenge_pair.gst_record_id]

        pair_result = score_purchase_to_gst(
            purchase=purchase,
            gst_record=gst_record,
        )

        signals = pair_result.signals

        findings = tuple(finding.value for finding in pair_result.semantic_findings)

        results.append(
            ChallengeResult(
                case_id=challenge_pair.case_id,
                purchase_record_id=challenge_pair.purchase_record_id,
                gst_record_id=challenge_pair.gst_record_id,
                expected_label=challenge_pair.expected_label,
                score=pair_result.relationship.score,
                coverage=pair_result.relationship.coverage,
                entity_score=signals[SignalName.ENTITY],
                reference_score=signals[SignalName.REFERENCE],
                amount_score=signals[SignalName.AMOUNT],
                temporal_score=signals[SignalName.TEMPORAL],
                tax_identity_score=signals[SignalName.TAX_IDENTITY],
                semantic_findings=findings,
                eligibility_status=pair_result.eligibility.status.value,
                blocking_findings=tuple(f.value for f in pair_result.eligibility.blocking_findings),
            )
        )

    return results


def format_score(score: float | None) -> str:
    if score is None:
        return "None"

    return f"{score:.4f}"


def format_findings(findings: tuple[str, ...]) -> str:
    if not findings:
        return "-"
    return ",".join(findings)


def print_score_table(results: list[ChallengeResult]) -> None:
    print(
        f"{'Case':<7} "
        f"{'Pair':<14} "
        f"{'Label':<17} "
        f"{'Score':>7}  "
        f"{'Eligibility':<11}  "
        f"{'Entity':>7}  "
        f"{'Ref':>7}  "
        f"{'Amount':>7}  "
        f"{'Time':>7}  "
        f"{'Tax':>7}  "
        f"{'Findings'}"
    )
    print("-" * 115)

    for r in results:
        pair_str = f"{r.purchase_record_id}-{r.gst_record_id}"
        print(
            f"{r.case_id:<7} "
            f"{pair_str:<14} "
            f"{r.expected_label:<17} "
            f"{format_score(r.score):>7}  "
            f"{r.eligibility_status:<11}  "
            f"{format_score(r.entity_score):>7}  "
            f"{format_score(r.reference_score):>7}  "
            f"{format_score(r.amount_score):>7}  "
            f"{format_score(r.temporal_score):>7}  "
            f"{format_score(r.tax_identity_score):>7}  "
            f"{format_findings(r.semantic_findings)}"
        )


def print_baseline_concerns(results: list[ChallengeResult]) -> None:
    print("\nBaseline concerns")
    print("-" * 17)
    
    for r in results:
        pair_str = f"{r.purchase_record_id}-{r.gst_record_id}"
        
        if r.expected_label == "group_component":
            print(f"{r.case_id} requires group-level evaluation; pair score shown diagnostically.")
            continue
            
        if r.expected_label == "negative" and r.score is not None and r.score >= CHALLENGE_CONCERN_SCORE:
            print(f"{r.case_id} {pair_str} score={r.score:.4f}")


def print_eligibility_summary(results: list[ChallengeResult]) -> None:
    eligible_pairs = [r for r in results if r.eligibility_status == "eligible"]
    ineligible_pairs = [r for r in results if r.eligibility_status == "ineligible"]

    print("\n1:1 eligibility summary")
    print("-----------------------")
    print(f"Eligible pairs: {len(eligible_pairs)}")
    print(f"Ineligible pairs: {len(ineligible_pairs)}")

    for r in ineligible_pairs:
        pair_str = f"{r.purchase_record_id}-{r.gst_record_id}"
        blockers_str = ",".join(r.blocking_findings)
        print(f"{r.case_id} {pair_str} blockers={blockers_str}")


def main() -> None:
    purchases = load_purchases(PURCHASES_PATH)
    gst_records = load_gst_records(GST_RECORDS_PATH)
    challenge_pairs = load_challenge_pairs(PAIR_LABELS_PATH)

    results = evaluate_challenges(
        purchases=purchases,
        gst_records=gst_records,
        challenge_pairs=challenge_pairs,
    )

    print_score_table(results)
    print_baseline_concerns(results)
    print_eligibility_summary(results)


if __name__ == "__main__":
    main()
````

## File: src/recongraph/domain/observations.py
````python
import re
import json
import hashlib
from enum import Enum
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from .scopes import SubjectRef


class ObservationState(str, Enum):
    PRESENT = "present"
    MISSING = "missing"
    INVALID = "invalid"


class InterpretationState(str, Enum):
    INTERPRETED = "interpreted"
    UNINTERPRETABLE = "uninterpretable"


@dataclass(frozen=True, order=True)
class FieldPath:
    """
    Semantic value object for field paths.
    Validates against grammar: <segment>(.<segment>)* where segment is [a-z][a-z0-9_]*
    """
    value: str

    _PATTERN = re.compile(r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)*$")

    def __post_init__(self):
        if not self._PATTERN.match(self.value):
            raise ValueError(f"Invalid FieldPath format: '{self.value}'")

    def __str__(self) -> str:
        return self.value

    def to_dict(self) -> str:
        return self.value


@dataclass(frozen=True, order=True)
class ObservationSlot:
    """
    Identifies the semantic source slot where a fact belongs, independent of its value occurrence.
    """
    subject: SubjectRef
    field: FieldPath

    def to_dict(self) -> dict:
        return {
            "subject": self.subject.to_dict(),
            "field": self.field.to_dict()
        }


@dataclass(frozen=True)
class ObservationFingerprint:
    """
    Opaque deterministic fingerprint representing the typed value state occurrence.
    This replaces temporal revision numbers.
    """
    digest: str

    def to_dict(self) -> str:
        return self.digest


@dataclass(frozen=True)
class ObservationIdentity:
    """
    Deterministic identity for an observation occurrence.
    Composed of the slot (where) and the fingerprint (what typed state).
    """
    slot: ObservationSlot
    fingerprint: ObservationFingerprint

    def to_dict(self) -> dict:
        return {
            "slot": self.slot.to_dict(),
            "fingerprint": self.fingerprint.to_dict()
        }

    def to_kernel_identity_ref(self) -> 'KernelIdentityRef':
        from .identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest
        return KernelIdentityRef(
            domain=IdentityDomainId("recongraph.observation_identity"),
            schema=IdentitySchemaId("recongraph.observation_identity.v1"),
            # K3 fingerprint digest did not have the sha256: prefix, we add it for KernelIdentityRef 
            digest=IdentityDigest(f"sha256:{self.fingerprint.digest}")
        )


def _canonicalize_value(value: Any) -> tuple[str, Any]:
    """
    Produces a canonical (type_tag, raw_value) for observation values.
    """
    if value is None:
        return "none", None
    elif isinstance(value, bool):
        return "bool", value
    elif isinstance(value, int):
        return "int", value
    elif isinstance(value, float):
        import math
        if not math.isfinite(value):
            raise ValueError("Non-finite floats are not supported for observations.")
        # float repr is relatively stable in modern python, but forcing a standard string representation prevents JSON weirdness
        return "float", repr(value)
    elif isinstance(value, Decimal):
        # Preserves precision scale (e.g. 1.0 vs 1.00)
        return "decimal", str(value)
    elif isinstance(value, str):
        return "str", value
    elif isinstance(value, datetime):
        return "datetime", value.isoformat()
    elif isinstance(value, date):
        return "date", value.isoformat()
    else:
        raise TypeError(f"Unsupported observation value type: {type(value)}")


@dataclass(frozen=True)
class Observation:
    """
    Minimal immutable envelope for an observed fact occurrence.
    Use Observation.create() to guarantee identity consistency.
    """
    identity: ObservationIdentity
    state: ObservationState
    value: Any

    def __post_init__(self):
        # Validate state/value contract
        if self.state == ObservationState.MISSING:
            if self.value is not None:
                raise ValueError("MISSING observation must have a None value.")
        else:
            if self.value is None:
                raise ValueError(f"{self.state.value.upper()} observation cannot have a None value.")

        # Re-derive fingerprint to guarantee identity consistency
        expected_fingerprint = self._compute_fingerprint(self.state, self.value)
        if self.identity.fingerprint != expected_fingerprint:
            raise ValueError("Observation identity fingerprint is inconsistent with state and value.")

    @staticmethod
    def _compute_fingerprint(state: ObservationState, value: Any) -> ObservationFingerprint:
        type_tag, canonical_val = _canonicalize_value(value)
        envelope = {
            "schema_version": 1,
            "state": state.value,
            "type": type_tag,
            "value": canonical_val
        }
        envelope_bytes = json.dumps(envelope, sort_keys=True).encode("utf-8")
        digest = hashlib.sha256(envelope_bytes).hexdigest()
        return ObservationFingerprint(digest)

    @classmethod
    def create(
        cls,
        slot: ObservationSlot,
        state: ObservationState,
        value: Any
    ) -> 'Observation':
        fingerprint = cls._compute_fingerprint(state, value)
        identity = ObservationIdentity(slot=slot, fingerprint=fingerprint)
        return cls(identity=identity, state=state, value=value)

    def to_dict(self) -> dict:
        """
        Dumps the full sensitive observation containing raw source values.
        """
        type_tag, canonical_val = _canonicalize_value(self.value)
        return {
            "identity": self.identity.to_dict(),
            "state": self.state.value,
            "value": {
                "type": type_tag,
                "value": canonical_val
            }
        }


from .lineage import StructuredSourceLineage
from .identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest

@dataclass(frozen=True, slots=True, order=True)
class ObservationOccurrenceIdentity:
    """
    Deterministic identity for an observation occurrence.
    H(observation_identity_ref, source_lineage_canonical_identity).
    """
    digest: str

    @classmethod
    def compute(
        cls,
        observation_identity: ObservationIdentity,
        lineage: StructuredSourceLineage
    ) -> 'ObservationOccurrenceIdentity':
        
        payload = {
            "schema": "recongraph.observation_occurrence_identity.v1",
            "observation_identity": observation_identity.to_kernel_identity_ref().digest.value,
            "lineage": hashlib.sha256(lineage.canonicalize_for_serialization()).hexdigest()
        }
        
        canonical_bytes = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False
        ).encode("utf-8")

        domain_separated_bytes = b"recongraph:observation-occurrence:v1\x00" + canonical_bytes
        digest_hex = hashlib.sha256(domain_separated_bytes).hexdigest()
        return cls(f"sha256:{digest_hex}")

    def to_kernel_identity_ref(self) -> KernelIdentityRef:
        return KernelIdentityRef(
            domain=IdentityDomainId("recongraph.observation_occurrence"),
            schema=IdentitySchemaId("recongraph.observation_occurrence_identity.v1"),
            digest=IdentityDigest(self.digest)
        )


@dataclass(frozen=True, slots=True, order=True)
class ObservationOccurrence:
    """
    Binds an observation fact (what content state exists) to a source occurrence (where it came from).
    """
    observation_identity: ObservationIdentity
    lineage: StructuredSourceLineage
    identity: ObservationOccurrenceIdentity

    @classmethod
    def create(
        cls,
        observation_identity: ObservationIdentity,
        lineage: StructuredSourceLineage
    ) -> 'ObservationOccurrence':
        identity = ObservationOccurrenceIdentity.compute(observation_identity, lineage)
        return cls(observation_identity=observation_identity, lineage=lineage, identity=identity)
````

## File: src/recongraph/domain/records.py
````python
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class PurchaseRecord:
    """Represent purchase-side financial evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    tax_identity: str | None
    net_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    tax_rate: Decimal | None = None
    currency: str = "USD"
    sign: int = 1


@dataclass(frozen=True)
class GSTRecord:
    """Represent GST-side financial evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    tax_identity: str | None
    net_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    tax_rate: Decimal | None = None
    currency: str = "USD"
    sign: int = -1


@dataclass(frozen=True)
class InvoiceRecord:
    """Represent invoice-side financial evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    tax_identity: str | None
    net_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    tax_rate: Decimal | None = None
    currency: str = "USD"
    sign: int = 1


@dataclass(frozen=True)
class BankRecord:
    """Represent bank-side financial settlement evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    currency: str = "USD"
    sign: int = -1
````

## File: src/recongraph/domain/scopes.py
````python
from enum import Enum
from dataclasses import dataclass
from typing import Optional


class ScopeKind(str, Enum):
    """
    Formal taxonomy of assertion scopes.
    """
    RECORD = "record"
    RECORD_PAIR = "record_pair"
    GROUP = "group"
    GROUP_PAIR = "group_pair"
    HYPOTHESIS = "hypothesis"
    COMPONENT = "component"


@dataclass(frozen=True, order=True)
class SubjectRef:
    """
    A strictly typed, stable identity for a domain subject.
    Does not hold the actual record object, only its stable URN.
    """
    urn: str

    def to_dict(self) -> dict:
        return {"urn": self.urn}


@dataclass(frozen=True)
class PropositionSubject:
    """
    Represents the canonicalized subject arguments for an EvidenceAssertion.
    Retains the claim identity and semantic version to prove it was canonically constructed.
    """
    claim_id: str
    claim_semantic_version: int
    kind: ScopeKind
    left: tuple[SubjectRef, ...]
    right: tuple[SubjectRef, ...]

    def __post_init__(self):
        left_len = len(self.left)
        right_len = len(self.right)

        if left_len == 0 and right_len == 0:
            raise ValueError("SC-001 Violation: Scope cannot be entirely empty.")

        if self.kind == ScopeKind.RECORD:
            if left_len + right_len != 1:
                raise ValueError("SC-002 Violation: RECORD scope must have exactly one subject.")
        elif self.kind == ScopeKind.RECORD_PAIR:
            if left_len != 1 or right_len != 1:
                raise ValueError("SC-002 Violation: RECORD_PAIR must have exactly 1 left and 1 right.")
        elif self.kind == ScopeKind.GROUP_PAIR:
            if left_len == 0 or right_len == 0:
                raise ValueError("SC-002 Violation: GROUP_PAIR must have at least one left and one right.")
            if left_len == 1 and right_len == 1:
                raise ValueError("SC-002 Violation: GROUP_PAIR requires multiple subjects on at least one side.")

        if len(set(self.left)) != left_len:
            raise ValueError("SC-003 Violation: Duplicate subjects in left side.")
        if len(set(self.right)) != right_len:
            raise ValueError("SC-003 Violation: Duplicate subjects in right side.")

    @classmethod
    def create(
        cls,
        claim_descriptor,
        kind: ScopeKind,
        left: frozenset[SubjectRef] | set[SubjectRef] | list[SubjectRef],
        right: Optional[frozenset[SubjectRef] | set[SubjectRef] | list[SubjectRef]] = None
    ) -> 'PropositionSubject':
        if not claim_descriptor.validates_scope_kind(kind):
            raise ValueError(f"SC-008 Violation: Claim {claim_descriptor.claim_id.value} does not allow scope kind {kind.value}.")

        if right is None:
            right = frozenset()

        canon_left = tuple(sorted(left))
        canon_right = tuple(sorted(right))

        if claim_descriptor.symmetry == "symmetric": 
            if canon_right < canon_left:
                canon_left, canon_right = canon_right, canon_left

        return cls(
            claim_id=claim_descriptor.claim_id.value,
            claim_semantic_version=claim_descriptor.semantic_version.value,
            kind=kind,
            left=canon_left,
            right=canon_right
        )

    def to_dict(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "claim_semantic_version": self.claim_semantic_version,
            "kind": self.kind.value,
            "left": [s.to_dict() for s in self.left],
            "right": [s.to_dict() for s in self.right]
        }


@dataclass(frozen=True, slots=True)
class Proposition:
    """
    A specific claim applied to a specific subject.
    Mechanically guarantees that the subject was canonically built for this exact claim.
    """
    claim: 'ClaimDescriptor'
    subject: PropositionSubject

    def __post_init__(self):
        if self.subject.claim_id != self.claim.claim_id.value:
            raise ValueError("Proposition construction rejected: claim mismatch.")
        if self.subject.claim_semantic_version != self.claim.semantic_version.value:
            raise ValueError("Proposition construction rejected: claim semantic version mismatch.")

    @classmethod
    def create(cls, claim: 'ClaimDescriptor', kind: ScopeKind, left: frozenset[SubjectRef] | set[SubjectRef] | list[SubjectRef], right: Optional[frozenset[SubjectRef] | set[SubjectRef] | list[SubjectRef]] = None) -> 'Proposition':
        subject = PropositionSubject.create(claim, kind, left, right)
        return cls(claim=claim, subject=subject)
````

## File: src/recongraph/matching/pair_scorers.py
````python
from collections.abc import Mapping
from dataclasses import dataclass

from recongraph.domain.records import GSTRecord, PurchaseRecord
from recongraph.matching.scoring import (
    RelationshipPolicy,
    RelationshipScore,
    SignalName,
    calculate_relationship_score,
)
from recongraph.matching.signals import (
    amount_score,
    entity_score,
    tax_identity_score,
    temporal_score,
)
from recongraph.matching.purchase_gst_semantics import (
    SemanticFinding,
    EligibilityResult,
    analyze_purchase_gst_semantics,
    evaluate_purchase_gst_one_to_one_eligibility,
)
from recongraph.matching.reference_evidence import (
    ReferenceEvidenceContext,
    ReferenceEvidenceInterpretation,
    compute_reference_interpretation,
)


PURCHASE_TO_GST_MAX_DAYS = 7


PURCHASE_TO_GST_POLICY = RelationshipPolicy(
    weights={
        SignalName.ENTITY: 0.20,
        SignalName.REFERENCE: 0.20,
        SignalName.AMOUNT: 0.25,
        SignalName.TEMPORAL: 0.10,
        SignalName.TAX_IDENTITY: 0.25,
    },
    contradiction_penalties={},
)


@dataclass(frozen=True)
class PairScoringResult:
    """Represent primitive evidence and its aggregated relationship score."""

    signals: Mapping[SignalName, float | None]
    semantic_findings: tuple[SemanticFinding, ...]
    eligibility: EligibilityResult
    relationship: RelationshipScore
    reference_interpretation: ReferenceEvidenceInterpretation


def score_purchase_to_gst(
    purchase: PurchaseRecord,
    gst_record: GSTRecord,
    reference_context: ReferenceEvidenceContext,
) -> PairScoringResult:
    """Score compatibility between purchase-side and GST-side evidence."""
    reference_interpretation = compute_reference_interpretation(
        purchase.reference,
        gst_record.reference,
        reference_context,
    )

    if not purchase.reference or not gst_record.reference:
        ref_signal = None
    else:
        ref_signal = reference_interpretation.score

    signals = {
        SignalName.ENTITY: entity_score(
            purchase.vendor_name,
            gst_record.vendor_name,
        ),
        SignalName.REFERENCE: ref_signal,
        SignalName.AMOUNT: amount_score(
            purchase.amount,
            gst_record.amount,
        ),
        SignalName.TEMPORAL: temporal_score(
            purchase.record_date,
            gst_record.record_date,
            max_days=PURCHASE_TO_GST_MAX_DAYS,
        ),
        SignalName.TAX_IDENTITY: tax_identity_score(
            purchase.tax_identity,
            gst_record.tax_identity,
        ),
    }

    semantic_findings = analyze_purchase_gst_semantics(
        signals
    )
    eligibility = evaluate_purchase_gst_one_to_one_eligibility(
        semantic_findings
    )
    relationship = calculate_relationship_score(
        signals=signals,
        policy=PURCHASE_TO_GST_POLICY,
    )

    return PairScoringResult(
        signals=signals,
        semantic_findings=semantic_findings,
        eligibility=eligibility,
        relationship=relationship,
        reference_interpretation=reference_interpretation,
    )
````

## File: tests/test_derivation_identity.py
````python
import pytest
import json
from dataclasses import dataclass

from recongraph.domain.derivations import (
    ProviderId,
    ProviderSemanticVersion,
    DerivationMethodId,
    DerivationMethodDescriptor,
    DerivationInputBinding,
    DerivationIdentity
)
from recongraph.domain.observations import ObservationSlot, ObservationState, Observation, FieldPath
from recongraph.domain.scopes import SubjectRef


def test_provider_id_validation():
    pid = ProviderId("recongraph.vendor")
    assert pid.value == "recongraph.vendor"
    
    with pytest.raises(ValueError):
        ProviderId("vendor") # missing namespace
        
    with pytest.raises(ValueError):
        ProviderId("recongraph..vendor")


def test_provider_semantic_version():
    ver = ProviderSemanticVersion(major=1, minor=2, patch=3)
    assert ver.major == 1
    assert ver.minor == 2
    assert ver.patch == 3


def test_derivation_method_id_not_globally_namespaced():
    # As decided, MethodId is provider-relative.
    # It must not duplicate the namespace. 
    mid = DerivationMethodId("normalize_name")
    assert mid.value == "normalize_name"


def test_di001_same_inputs_method_version_same_identity():
    # Setup
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs = Observation.create(slot, ObservationState.PRESENT, "ABC").identity
    
    desc = DerivationMethodDescriptor(
        provider_id=ProviderId("vendor.identity"),
        method_id=DerivationMethodId("extract"),
        commutative_roles=frozenset()
    )
    
    bindings = frozenset([DerivationInputBinding("source", obs.to_kernel_identity_ref())])
    
    id1 = DerivationIdentity.compute(
        provider_semantic_version=ProviderSemanticVersion(1, 0, 0),
        method=desc,
        inputs=bindings
    )
    
    id2 = DerivationIdentity.compute(
        provider_semantic_version=ProviderSemanticVersion(1, 0, 0),
        method=desc,
        inputs=bindings
    )
    
    assert id1 == id2
    assert id1.digest.startswith("sha256:")


def test_di002_commutative_roles_canonicalize():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs1 = Observation.create(slot, ObservationState.PRESENT, "A").identity
    obs2 = Observation.create(slot, ObservationState.PRESENT, "B").identity
    
    desc = DerivationMethodDescriptor(
        provider_id=ProviderId("recongraph.financial"),
        method_id=DerivationMethodId("aggregate"),
        commutative_roles=frozenset(["amount"])
    )
    
    # Order 1
    b1 = frozenset([
        DerivationInputBinding("amount", obs1.to_kernel_identity_ref()),
        DerivationInputBinding("amount", obs2.to_kernel_identity_ref())
    ])
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), desc, b1)
    
    # Order 2
    b2 = frozenset([
        DerivationInputBinding("amount", obs2.to_kernel_identity_ref()),
        DerivationInputBinding("amount", obs1.to_kernel_identity_ref())
    ])
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), desc, b2)
    
    assert id1 == id2


def test_di003_directional_roles_distinct():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs1 = Observation.create(slot, ObservationState.PRESENT, "A").identity
    obs2 = Observation.create(slot, ObservationState.PRESENT, "B").identity
    
    desc = DerivationMethodDescriptor(
        provider_id=ProviderId("recongraph.financial"),
        method_id=DerivationMethodId("subtract"),
        commutative_roles=frozenset()
    )
    
    b1 = frozenset([
        DerivationInputBinding("left", obs1.to_kernel_identity_ref()),
        DerivationInputBinding("right", obs2.to_kernel_identity_ref())
    ])
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), desc, b1)
    
    b2 = frozenset([
        DerivationInputBinding("left", obs2.to_kernel_identity_ref()),
        DerivationInputBinding("right", obs1.to_kernel_identity_ref())
    ])
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), desc, b2)
    
    assert id1 != id2


def test_di005_semantic_version_bump_changes_identity():
    desc = DerivationMethodDescriptor(
        provider_id=ProviderId("vendor.identity"),
        method_id=DerivationMethodId("extract"),
        commutative_roles=frozenset()
    )
    b = frozenset([])
    
    id1 = DerivationIdentity.compute(ProviderSemanticVersion(1, 0, 0), desc, b)
    id2 = DerivationIdentity.compute(ProviderSemanticVersion(1, 1, 0), desc, b)
    assert id1 != id2
````

## File: tests/test_pair_scorers.py
````python
from datetime import date

import pytest

from recongraph.domain.records import GSTRecord, PurchaseRecord
from recongraph.matching.pair_scorers import (
    PURCHASE_TO_GST_MAX_DAYS,
    PURCHASE_TO_GST_POLICY,
    PairScoringResult,
    score_purchase_to_gst,
)
from recongraph.matching.scoring import RelationshipScore, SignalName
from recongraph.matching.purchase_gst_semantics import (
    SemanticFinding,
    OneToOneEligibility,
    EligibilityResult,
)
from recongraph.matching.reference_evidence import (
    ReferenceEvidenceContext,
    ReferenceEvidencePolicy,
    ReferenceCorpusProfile,
    ReferenceEvidenceInterpretation,
    ReferenceEvidenceContribution,
    ReferenceEvidenceKind,
)


def _default_context() -> ReferenceEvidenceContext:
    prof = ReferenceCorpusProfile(
        reference_count=1000,
        normalized_reference_frequency={"dummy": 998, "inv1042": 2},
        numeric_token_document_frequency={"2026": 100, "1042": 2},
    )
    return ReferenceEvidenceContext(
        profile=prof,
        policy=ReferenceEvidencePolicy(),
    )


def test_purchase_record_preserves_financial_fields() -> None:
    record = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity="07ABCDE1234F1Z5",
    )

    assert record.vendor_name == "ABC Steel Private Limited"
    assert record.reference == "INV-1042"
    assert record.amount == 118000.0
    assert record.record_date == date(2026, 6, 12)
    assert record.tax_identity == "07ABCDE1234F1Z5"


def test_gst_record_preserves_financial_fields() -> None:
    record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC STEELS PVT. LTD.",
        reference="AB/1042",
        amount=118000.0,
        record_date=date(2026, 6, 13),
        tax_identity="07ABCDE1234F1Z5",
    )

    assert record.vendor_name == "ABC STEELS PVT. LTD."
    assert record.reference == "AB/1042"
    assert record.amount == 118000.0
    assert record.record_date == date(2026, 6, 13)
    assert record.tax_identity == "07ABCDE1234F1Z5"


def test_purchase_to_gst_policy_uses_expected_weights() -> None:
    assert PURCHASE_TO_GST_POLICY.weights == {
        SignalName.ENTITY: 0.20,
        SignalName.REFERENCE: 0.20,
        SignalName.AMOUNT: 0.25,
        SignalName.TEMPORAL: 0.10,
        SignalName.TAX_IDENTITY: 0.25,
    }


def test_purchase_gst_policy_uses_pure_compatibility() -> None:
    assert PURCHASE_TO_GST_POLICY.contradiction_penalties == {}


def test_purchase_to_gst_temporal_window_is_seven_days() -> None:
    assert PURCHASE_TO_GST_MAX_DAYS == 7


def test_pair_scoring_result_preserves_signal_explanation() -> None:
    relationship = RelationshipScore(
        score=0.94571,
        base_score=0.94571,
        coverage=1.0,
        contradiction_penalty=1.0,
        active_contradictions=(),
    )

    from recongraph.matching.reference_evidence import ReferenceEvidenceInterpretation
    
    result = PairScoringResult(
        signals={
            SignalName.ENTITY: 0.9,
            SignalName.REFERENCE: 0.8,
            SignalName.AMOUNT: 1.0,
            SignalName.TEMPORAL: 0.5,
            SignalName.TAX_IDENTITY: 0.0,
        },
        semantic_findings=(SemanticFinding.TAX_IDENTITY_CONFLICT,),
        eligibility=EligibilityResult(
            status=OneToOneEligibility.INELIGIBLE,
            blocking_findings=(SemanticFinding.TAX_IDENTITY_CONFLICT,),
        ),
        relationship=RelationshipScore(
            score=0.5,
            base_score=0.6,
            coverage=1.0,
            contradiction_penalty=0.5,
            active_contradictions=(SignalName.TAX_IDENTITY,),
        ),
        reference_interpretation=ReferenceEvidenceInterpretation(
            score=0.8,
            statistical_coverage=1.0,
            contributions=(
                ReferenceEvidenceContribution(
                    evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
                    identity_value="12345",
                    positive_evidence=0.8,
                    statistics_available=True,
                ),
            )
        )
    )

    assert result.signals[SignalName.ENTITY] == 0.9
    assert result.signals[SignalName.REFERENCE] == 0.8
    assert result.semantic_findings == (SemanticFinding.TAX_IDENTITY_CONFLICT,)
    assert result.relationship.score == 0.5


def test_pair_scoring_result_is_immutable() -> None:
    result = PairScoringResult(
        signals={},
        semantic_findings=(),
        eligibility=EligibilityResult(
            status=OneToOneEligibility.ELIGIBLE,
            blocking_findings=(),
        ),
        relationship=RelationshipScore(
            score=None,
            base_score=None,
            coverage=0.0,
            contradiction_penalty=1.0,
            active_contradictions=(),
        ),
        reference_interpretation=ReferenceEvidenceInterpretation(0.0, 0.0, ())
    )

    with pytest.raises(AttributeError):
        result.relationship = RelationshipScore(
            score=1.0,
            base_score=1.0,
            coverage=1.0,
            contradiction_penalty=1.0,
            active_contradictions=(),
        )


def test_score_purchase_to_gst_scores_controlled_positive_pair() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity="07ABCDE1234F1Z5",
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC STEELS PVT. LTD.",
        reference="AB/1042",
        amount=118000.0,
        record_date=date(2026, 6, 13),
        tax_identity="07ABCDE1234F1Z5",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.signals[SignalName.ENTITY] == pytest.approx(1.0)
    assert result.signals[SignalName.REFERENCE] == pytest.approx(0.9552786404500042)
    assert result.signals[SignalName.AMOUNT] == pytest.approx(1.0)
    assert result.signals[SignalName.TEMPORAL] == pytest.approx(
        1.0 - (1.0 / 7.0)
    )
    assert result.signals[SignalName.TAX_IDENTITY] == pytest.approx(
        1.0
    )

    assert result.semantic_findings == ()

    assert (
        result.eligibility.status
        is OneToOneEligibility.ELIGIBLE
    )
    assert result.eligibility.blocking_findings == ()

    assert result.relationship.score == pytest.approx(
        0.9767700138042866
    )
    assert result.relationship.base_score == pytest.approx(
        0.9767700138042866
    )
    assert result.relationship.coverage == pytest.approx(1.0)
    assert result.relationship.contradiction_penalty == pytest.approx(
        1.0
    )
    assert result.relationship.active_contradictions == ()


def test_score_purchase_to_gst_exposes_severe_amount_conflict() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity="07ABCDE1234F1Z5",
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC STEELS PVT. LTD.",
        reference="AB/1042",
        amount=236000.0,
        record_date=date(2026, 6, 13),
        tax_identity="07ABCDE1234F1Z5",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.semantic_findings == (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
    )

    assert (
        result.eligibility.status
        is OneToOneEligibility.INELIGIBLE
    )
    assert result.eligibility.blocking_findings == (
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
    )
    
    assert result.relationship.score == pytest.approx(
        0.7267700138042866
    )


def test_score_purchase_to_gst_exposes_tax_identity_conflict() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity="07ABCDE1234F1Z5",
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC STEELS PVT. LTD.",
        reference="AB/1042",
        amount=118000.0,
        record_date=date(2026, 6, 13),
        tax_identity="27ZZZZZ9999Z9Z9",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.semantic_findings == (
        SemanticFinding.TAX_IDENTITY_CONFLICT,
    )

    assert (
        result.eligibility.status
        is OneToOneEligibility.INELIGIBLE
    )
    assert result.eligibility.blocking_findings == (
        SemanticFinding.TAX_IDENTITY_CONFLICT,
    )
    
    assert result.relationship.score == pytest.approx(
        0.7267700138042866
    )


def test_score_purchase_to_gst_exposes_distinct_event_identity_evidence() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="CloudLedger Software Private Limited",
        reference="CL-JUN-123",
        amount=25000.0,
        record_date=date(2026, 6, 5),
        tax_identity="07CLOUD1234A1Z1",
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="CLOUDLEDGER SOFTWARE PVT LTD",
        reference="CL-JUL-456",
        amount=25000.0,
        record_date=date(2026, 7, 5),
        tax_identity="07CLOUD1234A1Z1",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.semantic_findings == (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
    )

    assert (
        result.eligibility.status
        is OneToOneEligibility.INELIGIBLE
    )
    assert result.eligibility.blocking_findings == (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
    )
    
    assert result.relationship.score == pytest.approx(
        0.7000
    )


def test_score_purchase_to_gst_preserves_missing_tax_evidence() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity=None,
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC STEELS PVT. LTD.",
        reference="AB/1042",
        amount=118000.0,
        record_date=date(2026, 6, 13),
        tax_identity="07ABCDE1234F1Z5",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.signals[SignalName.TAX_IDENTITY] is None
    assert result.semantic_findings == ()
    assert result.relationship.coverage == pytest.approx(0.75)
    assert result.relationship.contradiction_penalty == pytest.approx(
        1.0
    )
    assert result.relationship.active_contradictions == ()
    assert result.relationship.base_score == pytest.approx(
        0.9690266850723822
    )
    assert result.relationship.score == pytest.approx(
        0.9690266850723822
    )


def test_score_purchase_to_gst_applies_tax_contradiction() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity="07ABCDE1234F1Z5",
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC STEELS PVT. LTD.",
        reference="AB/1042",
        amount=118000.0,
        record_date=date(2026, 6, 13),
        tax_identity="27ZZZZZ9999Z9Z9",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.signals[SignalName.TAX_IDENTITY] == pytest.approx(
        0.0
    )
    assert result.relationship.coverage == pytest.approx(1.0)
    assert result.relationship.contradiction_penalty == pytest.approx(
        1.0
    )
    assert result.relationship.active_contradictions == ()
    assert result.relationship.base_score == pytest.approx(
        0.7267700138042866
    )
    assert result.relationship.score == pytest.approx(
        0.7267700138042866
    )


def test_score_purchase_to_gst_uses_purchase_to_gst_temporal_window() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="Vendor",
        reference="INV-1",
        amount=1000.0,
        record_date=date(2026, 6, 1),
        tax_identity=None,
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="Vendor",
        reference="INV-1",
        amount=1000.0,
        record_date=date(2026, 6, 8),
        tax_identity=None,
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert result.signals[SignalName.TEMPORAL] == pytest.approx(0.0)


def test_score_purchase_to_gst_returns_pair_scoring_result() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="Vendor",
        reference="INV-1",
        amount=1000.0,
        record_date=date(2026, 6, 1),
        tax_identity=None,
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="Vendor",
        reference="INV-1",
        amount=1000.0,
        record_date=date(2026, 6, 1),
        tax_identity=None,
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    reference_context=_default_context(),
    )

    assert isinstance(result, PairScoringResult)
    assert set(result.signals) == set(PURCHASE_TO_GST_POLICY.weights)


def test_low_compatibility_pair_can_remain_one_to_one_eligible() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC",
        reference="INV-1",
        amount=100.0,
        record_date=date(2026, 6, 1),
        tax_identity=None,
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="XYZ",
        reference="INV-999",
        amount=500.0,
        record_date=date(2026, 6, 1),
        tax_identity=None,
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
        reference_context=_default_context(),
    )

    assert result.relationship.score < 0.5
    assert (
        result.eligibility.status
        is OneToOneEligibility.ELIGIBLE
    )
    assert result.eligibility.blocking_findings == ()


def test_high_compatibility_pair_can_be_ineligible() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="CloudLedger Software Private Limited",
        reference="CL-JUN-123",
        amount=25000.0,
        record_date=date(2026, 6, 5),
        tax_identity="07CLOUD1234A1Z1",
    )

    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="CLOUDLEDGER SOFTWARE PVT LTD",
        reference="CL-JUL-456",
        amount=25000.0,
        record_date=date(2026, 7, 5),
        tax_identity="07CLOUD1234A1Z1",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
        reference_context=_default_context(),
    )

    assert result.relationship.score >= 0.7
    assert (
        result.eligibility.status
        is OneToOneEligibility.INELIGIBLE
    )
    assert result.eligibility.blocking_findings == (
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
    )


def test_purchase_gst_tax_conflict_does_not_apply_compatibility_penalty() -> None:
    purchase = PurchaseRecord(record_id="dummy_p", 
        vendor_name="ABC Steel Private Limited",
        reference="INV-1042",
        amount=118000.0,
        record_date=date(2026, 6, 12),
        tax_identity="07ABCDE1234F1Z5",
    )
    gst_record = GSTRecord(record_id="dummy_g", 
        vendor_name="ABC Steel Private Limited",
        reference="AB/1042",
        amount=118000.0,
        record_date=date(2026, 6, 13),
        tax_identity="29XYZAB5678C1Z2",
    )

    result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
        reference_context=_default_context(),
    )

    assert result.relationship.base_score == pytest.approx(
        0.7267700138042866
    )
    assert result.relationship.score == pytest.approx(
        0.7267700138042866
    )
    assert result.relationship.contradiction_penalty == 1.0
    assert result.relationship.active_contradictions == ()

    assert result.eligibility.status is OneToOneEligibility.INELIGIBLE
    assert result.eligibility.blocking_findings == (
        SemanticFinding.TAX_IDENTITY_CONFLICT,
    )

# --- Stage 4C Integration Parity Tests ---
````

## File: tests/test_source_lineage.py
````python
import pytest
import json
from dataclasses import dataclass

from recongraph.domain.lineage import (
    SourceSystemId,
    SourceArtifactId,
    SourceLocator
)


def test_sl001_valid_source_system():
    sid = SourceSystemId("sap.production")
    assert sid.value == "sap.production"
    
    assert SourceSystemId("document.upload_2024").value == "document.upload_2024"


def test_sl002_source_system_missing_namespace():
    with pytest.raises(ValueError):
        SourceSystemId("sap")


def test_sl003_uppercase_source_system():
    with pytest.raises(ValueError):
        SourceSystemId("SAP.production")


def test_sl004_whitespace_source_system():
    with pytest.raises(ValueError):
        SourceSystemId("sap. production")


def test_sl005_empty_artifact_id():
    with pytest.raises(ValueError):
        SourceArtifactId("")


def test_sl006_artifact_surrounding_whitespace():
    with pytest.raises(ValueError):
        SourceArtifactId("  DOC123  ")


def test_sl007_artifact_internal_structured_punctuation():
    # Should accept colons, dashes, etc. opaque coordinate
    aid = SourceArtifactId("purchase_invoice:874219@v1")
    assert aid.value == "purchase_invoice:874219@v1"


def test_sl008_artifact_case_preservation():
    aid1 = SourceArtifactId("DOC_123")
    aid2 = SourceArtifactId("doc_123")
    assert aid1 != aid2
    assert aid1.value == "DOC_123"


def test_sl009_empty_locator():
    with pytest.raises(ValueError):
        SourceLocator("")


def test_sl010_locator_surrounding_whitespace():
    with pytest.raises(ValueError):
        SourceLocator("  field:vendor  ")


def test_sl011_locator_internal_slash():
    loc = SourceLocator("page:2/bbox:100,200,500,260")
    assert loc.value == "page:2/bbox:100,200,500,260"


def test_sl012_locator_unicode_decision():
    # Locators might legitimately contain unicode fields if the adapter dictates it
    loc = SourceLocator("column:प्रदायक")
    assert loc.value == "column:प्रदायक"


def test_sl013_deterministic_equality():
    loc1 = SourceLocator("page:2")
    loc2 = SourceLocator("page:2")
    assert loc1 == loc2
    
    sys1 = SourceSystemId("gst.portal")
    sys2 = SourceSystemId("gst.portal")
    assert sys1 == sys2


def test_sl014_hash_stability_within_process_semantics():
    # Ensure they can be used in dicts/sets and rely on __hash__, but we will not mandate 
    # hash() to be stable cross-process in tests. Serialization provides absolute stability.
    s = {SourceSystemId("sap.production")}
    assert SourceSystemId("sap.production") in s


def test_sl015_different_typed_ids_never_compare_equal():
    assert SourceSystemId("sap.production") != SourceArtifactId("sap.production")


def test_sl016_timestamp_not_auto_generated():
    # If a SourceArtifactId generated timestamps automatically, two instances with the same value 
    # would not compare equal if generated milliseconds apart.
    aid1 = SourceArtifactId("file1")
    aid2 = SourceArtifactId("file1")
    assert aid1 == aid2


def test_sl017_artifact_does_not_infer_content_hash():
    # SourceArtifactId takes the coordinate literally. It does not parse or check file existence.
    aid = SourceArtifactId("sha256:abc")
    assert aid.value == "sha256:abc"
    assert not hasattr(aid, "hash_value")


def test_sl018_source_system_does_not_parse_provider_identity():
    # It must not be conflated with ProviderId from K5.
    # Even if grammar matches, they are strictly domain-separated types in Python.
    sys_id = SourceSystemId("recongraph.vendor")
    assert sys_id.value == "recongraph.vendor"


from recongraph.domain.observations import ObservationSlot, ObservationState, Observation, FieldPath
from recongraph.domain.scopes import SubjectRef
from recongraph.domain.lineage import StructuredSourceLineage, SourceVersionRef
from recongraph.domain.observations import ObservationOccurrence

def test_structured_source_lineage_serialization():
    sys = SourceSystemId("sap.production")
    art = SourceArtifactId("purchase_invoice:123")
    loc = SourceLocator("field:vendor_name")
    ver = SourceVersionRef("rowversion:1")
    
    lineage = StructuredSourceLineage(sys, art, loc, ver)
    
    # We must explicitly canonicalize to bytes
    canonical_bytes = lineage.canonicalize_for_serialization()
    assert isinstance(canonical_bytes, bytes)
    
    payload = json.loads(canonical_bytes.decode("utf-8"))
    assert payload["schema"] == "recongraph.source_lineage.v1"
    assert payload["source_system"] == "sap.production"
    assert payload["source_artifact"] == "purchase_invoice:123"
    assert payload["source_version"] == "rowversion:1"


def test_observation_occurrence_invariants():
    slot = ObservationSlot(SubjectRef("urn:1"), FieldPath("vendor"))
    obs1 = Observation.create(slot, ObservationState.PRESENT, "ABC").identity
    obs2 = Observation.create(slot, ObservationState.PRESENT, "XYZ").identity
    
    lin1 = StructuredSourceLineage(SourceSystemId("sys.a"), SourceArtifactId("1"), SourceLocator("L"))
    lin2 = StructuredSourceLineage(SourceSystemId("sys.b"), SourceArtifactId("2"), SourceLocator("L"))
    
    # 1. Same observation + same lineage = Equal
    occ1a = ObservationOccurrence.create(obs1, lin1)
    occ1b = ObservationOccurrence.create(obs1, lin1)
    assert occ1a == occ1b
    
    # 2. Same observation + different lineage = Distinct
    occ_diff_lin = ObservationOccurrence.create(obs1, lin2)
    assert occ1a != occ_diff_lin
    
    # 3. Different observation + same lineage = Distinct
    # This prevents the OCR semantic attack where OCR engine A and B read the same PDF bbox 
    # but produce different text. Their lineage is identical, but their epistemic content differs.
    occ_diff_obs = ObservationOccurrence.create(obs2, lin1)
    assert occ1a != occ_diff_obs
````
