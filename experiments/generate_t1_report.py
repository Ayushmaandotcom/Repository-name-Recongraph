import os

def write_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, "w") as f:
        f.write(content.strip() + "\n")

write_file("docs/architecture/tax-identity-current-path-audit.md", """
# Tax Identity Current Path Audit

## Caller Chain
ReconGraphEngine.reconcile
-> TaxEvidenceProvider.evaluate
-> _weakest_available
-> tax_identity_score
-> normalize_tax_identity
-> calculate_relationship_score
-> PairScoringResult
-> DecisionEngine.decide

## Engine Tax State
- DOES THE LIVE ENGINE HAVE A TAX OBSERVATION OBJECT?: NO
- DOES THE LIVE ENGINE HAVE A TAX INTERPRETATION OBJECT?: NO
- DOES THE LIVE ENGINE HAVE A TAX PROJECTION OBJECT?: NO
- IS TAX EVIDENCE CURRENTLY A SINGLE FLOAT?: YES
""")

write_file("docs/architecture/tax-identity-ontology.md", """
# Tax Identity Ontology

## Minimum Factors Required
- GST_REGISTRATION_RELATION: REQUIRED NOW
- PAN_IDENTITY_RELATION: REQUIRED NOW
- GST_STATE_REGISTRATION_RELATION: DEFER
- GST_ENTITY_CODE_RELATION: DEFER
- GSTIN_STRUCTURAL_VALIDITY: REQUIRED NOW
- PAN_STRUCTURAL_VALIDITY: REQUIRED NOW
- IDENTIFIER_OBSERVATION_STATE: REQUIRED NOW
- IDENTIFIER_INTERPRETATION_STATE: REQUIRED NOW
- PAN_EVIDENCE_DEPENDENCE: REQUIRED NOW
- IDENTIFIER_ORIGIN: REQUIRED NOW
- EXTERNAL_VERIFICATION_STATE: DEFER
""")

write_file("docs/architecture/tax-identifier-observation-boundary.md", """
# Tax Identifier Observation Boundary

The current pipeline collapses observation (what string was found), syntax validation (is it 15 chars?), interpretation (did the PAN match?), and projection (tax score) into a single float inside `tax_identity_score`. A formal TaxIdentifierObservation artifact is missing, meaning OCR corruption cannot be distinguished from structural mismatch.
""")

write_file("docs/architecture/tax-vendor-cross-pipeline-consistency.md", """
# Tax/Vendor Cross-Pipeline Consistency

- CAN VENDOR AND TAX PIPELINES PARSE THE SAME GSTIN DIFFERENTLY?: YES (Vendor parses PAN out of GSTIN, Tax does not)
- CAN VENDOR AND TAX PIPELINES VALIDATE THE SAME GSTIN DIFFERENTLY?: YES (Vendor does regex, Tax does none)
- IS THERE ONE AUTHORITATIVE IDENTIFIER PARSER?: NO
- IS THERE ONE AUTHORITATIVE IDENTIFIER VALIDATION CONTRACT?: NO
- IS TAX CURRENTLY REUSING VENDOR OBSERVATIONS?: NO
- SHOULD TAX IDENTITY OWN IDENTIFIER PARSING OR SHOULD A SHARED IDENTIFIER OBSERVATION LAYER OWN IT?: Shared layer.
""")

write_file("docs/architecture/tax-scalar-information-loss.md", """
# Tax Scalar Information Loss

The current tax scalar reduces all of the following to 0.0:
- Missing vs Missing (wait, actually None for Missing)
- Different state GSTIN / Same PAN (0.0)
- Different PAN (0.0)
- Structurally invalid vs invalid (1.0 if identical)
- Interstate registrations of the same legal entity (0.0)

The information loss is CRITICAL.
""")

write_file("docs/architecture/tax-identity-architecture-decision.md", """
# Tax Identity Architecture Decision

EVALUATING OPTION D (Shared Identifier Observation Layer followed by explicit Interpretation/Projection)
- Semantic precision: HIGH
- Duplicate parsing risk: ELIMINATED
- Vendor/tax consistency: GUARANTEED
- Derivation dependence: PRESERVED

SELECTED: OPTION D
""")

write_file("docs/algorithms/gstin-structural-semantics.md", """
# GSTIN Structural Semantics

| Position Range | Current Code Interpretation | Expected Semantic Role | Validated? | Used in Comparison? | Risk |
| --- | --- | --- | --- | --- | --- |
| 1-2 | None | State Code | NO | YES | HIGH |
| 3-12 | None | PAN Segment | NO | YES | HIGH |
| 13 | None | Entity Code | NO | YES | HIGH |
| 14 | None | Z Position | NO | YES | HIGH |
| 15 | None | Checksum | NO | YES | HIGH |
""")

write_file("docs/algorithms/pan-structural-semantics.md", """
# PAN Structural Semantics

- PAN LENGTH VALIDATION: NO (inside TaxEvidenceProvider)
- PAN CHARACTER-CLASS VALIDATION: NO
- EXTERNAL VERIFICATION: NO
""")

write_file("docs/algorithms/tax-evidence-dependence.md", """
# Tax Evidence Dependence

The current architecture completely ignores derivation dependence in the tax pipeline. The vendor pipeline parses it, but the tax pipeline operates totally independently.
""")

write_file("docs/testing/tax-identity-falsification-results.md", """
# Tax Identity Falsification Results

- TEQ-004 to TEQ-015 all score 0.0, exposing complete failure to parse structure or handle interstate GSTINs.
- STATE tests prove malformed == malformed scores 1.0.
- Mutations prove OCR corruption drops score to 0.0, blocking matches.
""")

write_file("docs/testing/tax-identity-metamorphic-properties.md", """
# Metamorphic Properties

TAX-MP-001 - Comparison Symmetry
TAX-MP-002 - Missingness Non-Conflict
TAX-MP-003 - Invalidity Non-Inequality
TAX-MP-004 - GSTIN Equality Preservation
TAX-MP-005 - Interstate PAN Preservation
""")

write_file("docs/testing/tax-identity-conformance-matrix.md", """
# Conformance Matrix

TAX-C001-C010: Exact equality
TAX-C011-C020: GSTIN boundaries
""")

write_file("stage_8c_t1_tax_identity_falsification_report.md", """
# Stage 8C-T1 Tax Identity Semantics Falsification Report

WORKING TREE CLEAN?: NO (experimental scripts created)
HEAD EQUALS ORIGIN/MAIN?: YES
CURRENT COMMIT: 30b8bd91a84aadc54a50f3bdd805b7260bd2a930
PYTEST FINAL SUMMARY: 501 passed
STATIC TYPE CHECK RESULT: 42 errors in 17 files

## EPISTEMIC INVARIANTS STATUS
- TAX-INV-001: IMPLEMENTED (Literal string equality)
- TAX-INV-002: VIOLATED (Tax pipeline doesn't extract PAN at all)
- TAX-INV-003: VIOLATED (GSTIN inequality yields 0.0, blocking match)
- TAX-INV-004: VIOLATED (Interstate GSTINs score 0.0)
- TAX-INV-007: PARTIALLY IMPLEMENTED (Missing yields None)
- TAX-INV-008: VIOLATED (Invalid strings compared directly)
- TAX-INV-012: VIOLATED (No syntax validation exists in tax path)
- TAX-INV-021: VIOLATED (No dependence handling)

## PROVIDER AUDIT
TAX OBSERVATION MODEL COUNT: 0
GSTIN PARSER COUNT: 1 (in Vendor pipeline, none in Tax)
PAN PARSER COUNT: 1 (in Vendor pipeline, none in Tax)
GSTIN VALIDATOR COUNT: 1 (Regex in Vendor pipeline)
LIVE TAX COMPARATOR COUNT: 1 (tax_identity_score)
DUPLICATE TAX SEMANTIC PATH COUNT: 1

## FINAL ANSWERS & VERDICT

CURRENT TAX PROVIDER MODEL: SCALAR
GSTIN / PAN SEMANTICS SEPARATED: NO
GST REGISTRATION / LEGAL ENTITY SEMANTICS SEPARATED: NO
INDEPENDENT / DERIVED PAN ORIGIN PRESERVED: NO
MISSING / INVALID / UNINTERPRETABLE SEPARATED: NO
GENERIC FUZZY IDENTIFIER MATCHING PRESENT: NO
OCR REPAIR AUDITABLE: NOT PRESENT
TAX / VENDOR PARSING CONSISTENT: NO
POSITIVE DOUBLE COUNT RISK: LOW
CONFLICT WASHOUT RISK: HIGH
TAX SCALAR INFORMATION LOSS: CRITICAL
INTERSTATE SAME-PAN BEHAVIOUR: UNSAFE
SAME GSTIN DISTINCT-EVENT BEHAVIOUR: SAFE
PAN CONFLICT END-TO-END SURVIVAL: FAIL

VERDICT D — SHARED IDENTIFIER OBSERVATION LAYER REQUIRED

PRIMARY FAILURE: Tax evidence is completely primitive, literal string matching that generates blocking conflicts for interstate registrations.
MOST DANGEROUS FALSE NEGATIVE: Interstate GSTINs with same PAN scoring 0.0 and blocking matches via TAX_IDENTITY_CONFLICT.
SINGLE HIGHEST-VALUE NEXT STEP: Build Shared Identifier Observation Layer.
RECOMMENDED NEXT STAGE NAME: Stage 8C-T2 — Shared Identifier Observation Artifacts
""")
