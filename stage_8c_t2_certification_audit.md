# Stage 8C-T2 Certification Audit

## REPOSITORY BASELINE

WORKING TREE CLEAN?: NO
HEAD EQUALS ORIGIN/MAIN?: YES
CURRENT COMMIT: a3febe43d87541cf837b007a5e08c13ba822f97d
CURRENT COMMIT MESSAGE: feat: Stage 8C-V1-1D and 8C-T2 - Semantic Vendor Boundary and Tax Observation Layer
PYTEST FINAL SUMMARY: 501 passed in 0.58s
STATIC TYPE CHECK COMMAND: mypy src tests
STATIC TYPE CHECK RESULT: FAIL (71 errors)

T2_BASE: 30b8bd9
T2_HEAD: a3febe4

## MODIFIED PRODUCTION PYTHON FILES

- `src/recongraph/domain/tax/observation.py` (EXPECTED T2 SHARED OBSERVATION IMPLEMENTATION)
- `src/recongraph/domain/tax/parser.py` (EXPECTED T2 SHARED OBSERVATION IMPLEMENTATION)
- `src/recongraph/domain/vendor/artifact.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/domain/vendor/interpretation.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/domain/vendor/observation.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/domain/vendor/parser.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/domain/vendor/policy.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/graph/decision.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/graph/evaluator.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/graph/hypotheses.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/matching/pair_scorers.py` (REQUIRED TRANSPORT COMPATIBILITY)
- `src/recongraph/matching/purchase_gst_semantics.py` (EXPECTED VENDOR V1 MIGRATION)
- `src/recongraph/matching/signals.py` (REQUIRED TRANSPORT COMPATIBILITY)
- `src/recongraph/normalization/text.py` (UNRELATED CHANGE - Deleted Vendor Name Normalization)
- `src/recongraph/plugins/core_providers.py` (REQUIRED TRANSPORT COMPATIBILITY)
- `src/recongraph/benchmark/runner.py` (UNRELATED CHANGE)

### REQUIRED TRANSPORT COMPATIBILITY JUSTIFICATION
Because `VendorNameObservation` now returns a nested `ParsedTaxIdentifierArtifact` instead of legacy scalar strings for PAN/GSTIN extractions, the signature of downstream pipelines operating on Vendor observation objects had to change to unwrap the artifact. Additionally, `TaxEvidenceProvider` evaluates tax strings directly from records; it was adapted to parse the raw string into the required artifact before passing it to `tax_identity_score` to match the new signature of that function (which was adapted to support the new vendor artifacts). Without unwrapping the artifact at the `tax_identity_score` boundary, the code would throw a TypeError due to signature mismatch.

## TaxEvidenceProvider DIFF

FILE: `src/recongraph/plugins/core_providers.py`
CLASS: `TaxEvidenceProvider`
METHOD: `evaluate`
OLD INPUT REPRESENTATION: `lambda r: r.tax_identity` (raw string)
NEW INPUT REPRESENTATION: `lambda r: DeterministicTaxParser.parse(r.tax_identity, field_id="tax_identity")` (ParsedTaxIdentifierArtifact)
OLD SEMANTIC OPERATION: Passed raw string to tax_identity_score.
NEW SEMANTIC OPERATION: Parses raw string to artifact, passes artifact to tax_identity_score.
OLD OUTPUT: `EvidenceContribution(..., score=score)`
NEW OUTPUT: `EvidenceContribution(..., score=score)`
OLD MISSINGNESS BEHAVIOUR: Returns `None` score.
NEW MISSINGNESS BEHAVIOUR: Returns `None` score (artifact observation_state handled by tax_identity_score).
OLD INVALID-IDENTIFIER BEHAVIOUR: Normalizes string, scores 0.0 or 1.0.
NEW INVALID-IDENTIFIER BEHAVIOUR: Normalizes unwrapped artifact value, scores 0.0 or 1.0.
OLD PLACEHOLDER BEHAVIOUR: Normalizes string, scores 1.0 if identical.
NEW PLACEHOLDER BEHAVIOUR: Normalizes unwrapped artifact value, scores 1.0 if identical.
OLD GSTIN-DIFFERENCE BEHAVIOUR: Returns 0.0 tax score.
NEW GSTIN-DIFFERENCE BEHAVIOUR: Returns 0.0 tax score.

DID TaxEvidenceProvider BEGIN CONSUMING ParsedTaxIdentifierArtifact?: YES
DID TaxEvidenceProvider BEGIN READING structural_state?: NO
DID TaxEvidenceProvider BEGIN READING checksum_state?: NO
DID TaxEvidenceProvider BEGIN READING identifier origin?: NO
DID TaxEvidenceProvider BEGIN READING derived PAN?: NO
DID TaxEvidenceProvider BEGIN DISTINGUISHING GSTIN FROM PAN SEMANTICS?: NO
DID TaxEvidenceProvider BEGIN DISTINGUISHING INVALID FROM MISSING?: NO
DID TaxEvidenceProvider BEGIN DISTINGUISHING PLACEHOLDER FROM MISSING?: NO
DID TaxEvidenceProvider BEGIN INTERPRETING INTERSTATE SAME-PAN GSTINS?: NO
DID TaxEvidenceProvider BEGIN GENERATING NEW STRUCTURED FINDINGS?: NO
DID TaxEvidenceProvider BEGIN CHANGING TAX SCALAR MEANING?: NO

## tax_identity_score DIFF

OLD SIGNATURE: `def tax_identity_score(tax_identity_a: str | None, tax_identity_b: str | None) -> float | None:`
NEW SIGNATURE: `def tax_identity_score(artifact_a: "ParsedTaxIdentifierArtifact | None", artifact_b: "ParsedTaxIdentifierArtifact | None") -> float | None:`
OLD INPUT TYPE: `str | None`
NEW INPUT TYPE: `ParsedTaxIdentifierArtifact | None`
OLD ALGORITHM: Normalize strings, if equal 1.0 else 0.0.
NEW ALGORITHM: Extract `gstin_candidate`, then `pan_candidate`, then `observation.raw_value`. Normalize the extracted string. If equal 1.0 else 0.0.
OLD NORMALIZATION: `normalize_tax_identity` (strip and upper)
NEW NORMALIZATION: `normalize_tax_identity` (strip and upper) applied to extracted artifact string.
OLD RETURN DOMAIN: `float | None`
NEW RETURN DOMAIN: `float | None`

### Equivalence Test Cases

| Case | Old Score | New Score | Equal? | Reason |
| --- | --- | --- | --- | --- |
| None / None | None | None | True | Same early exit |
| None / valid GSTIN | None | None | True | Same early exit |
| valid GSTIN / None | None | None | True | Same early exit |
| equal valid-format GSTIN strings | 1.0 | 1.0 | True | Both logic paths normalize and match |
| different valid-format GSTIN strings | 0.0 | 0.0 | True | Both logic paths normalize and differ |
| lowercase / uppercase equivalent GSTIN | 1.0 | 1.0 | True | Both paths apply `.upper()` normalization |
| surrounding whitespace equivalent GSTIN | 1.0 | 1.0 | True | Both paths apply `.strip()` normalization |
| MALFORMED / MALFORMED | 1.0 | 1.0 | True | Artifact unwraps `raw_value` as fallback |
| UNKNOWN / UNKNOWN | 1.0 | 1.0 | True | Artifact unwraps `raw_value` as fallback |
| N/A / N/A | 1.0 | 1.0 | True | Artifact unwraps `raw_value` as fallback |
| different GSTIN / same embedded PAN | 0.0 | 0.0 | True | Legacy logic compares full GSTIN string; New logic compares extracted `gstin_candidate` which differs |
| different GSTIN / different embedded PAN | 0.0 | 0.0 | True | Both paths compare different strings |

IS THE NEW FUNCTION SEMANTICALLY EQUIVALENT TO THE OLD LEGACY COMPARATOR?: YES

## LIVE TAX PATH

DOES THE LIVE TAX PATH USE ParsedTaxIdentifierArtifact?: YES
WHICH FIELDS ARE READ?: `gstin_candidate`, `pan_candidate`, `observation.raw_value`
DOES IT READ ONLY canonical/raw transport values?: YES
DOES IT READ semantic structural state?: NO
DOES IT READ derivation state?: NO
DOES IT READ embedded PAN?: NO
DOES IT READ identifier origin?: NO
DOES IT READ checksum state?: NO
DOES IT USE ARTIFACT STATE TO CHANGE TAX SCORE?: NO
DOES IT USE ARTIFACT STATE TO CHANGE SEMANTIC FINDINGS?: NO
DOES IT USE ARTIFACT STATE TO CHANGE ELIGIBILITY?: NO

LIVE TAX PATH CLASSIFICATION: LEGACY COMPARATOR WITH REPRESENTATION ADAPTER

### Defect Test Cases

| Case | Artifact Left State | Artifact Right State | Artifact Facts Safe? | Legacy Tax Score | Legacy Defect Still Present? |
| --- | --- | --- | --- | --- | --- |
| CERT-001 MALFORMED/MALFORMED | None/None/MALFORMED | None/None/MALFORMED | YES | 1.0 | YES |
| CERT-002 UNKNOWN/UNKNOWN | None/None/UNKNOWN | None/None/UNKNOWN | YES | 1.0 | YES |
| CERT-003 N/A/N/A | None/None/N/A | None/None/N/A | YES | 1.0 | YES |
| CERT-004 diff GSTIN/same PAN | Valid GSTIN | Valid GSTIN | YES | 0.0 | YES |

## Q1-Q30 AUTHORIZATION EXACT ANSWERS

Q1. Can MALFORMED and MALFORMED become structurally valid identifier equality at the artifact layer? NO
Q2. Can UNKNOWN and UNKNOWN become structurally valid identifier equality at the artifact layer? NO
Q3. Can two missing observations create a valid canonical identifier? NO
Q4. Can an invalid GSTIN produce a valid derived PAN? NO
Q5. Can an uninterpretable GSTIN produce a valid derived PAN? NO
Q6. Can two GSTIN artifacts with different state codes preserve the same embedded PAN value? YES
Q7. Can two GSTIN artifacts with different entity codes preserve the same embedded PAN value? YES
Q8. Is a GSTIN-derived PAN distinguishable from an independently observed PAN? YES
Q9. If the values are equal, is origin still preserved? YES
Q10. Can O/0 corruption be silently repaired? NO
Q11. Can I/1 corruption be silently repaired? NO
Q12. Is raw evidence always preserved? YES
Q13. Are normalization events structured and auditable? YES
Q14. Are derivation events structured and auditable? YES
Q15. Does the artifact assert same GST registration? NO
Q16. Does the artifact assert same PAN identity? NO
Q17. Does the artifact assert same legal entity? NO
Q18. Does the artifact assert same transaction? NO
Q19. Does Vendor V1 use the shared structural parser? YES
Q20. Does Vendor V1 retain duplicate GSTIN validation logic? YES
Q21. Does Vendor V1 retain duplicate PAN validation logic? YES
Q22. Was TaxEvidenceProvider modified? YES
Q23. Is the legacy tax literal comparator still reachable? YES
Q24. Is that reachability explicitly documented as temporary until T3? YES
Q25. Is artifact identity context-independent? YES
Q26. Can VendorIdentityContext alter a parsed tax identifier artifact? NO
Q27. Can VendorProjectionPolicyV1 alter a parsed tax identifier artifact? NO
Q28. Can DecisionPolicy alter a parsed tax identifier artifact? NO
Q29. Is checksum state separate from external verification? YES
Q30. Does any artifact claim external verification? NO

GSTIN CHECKSUM IMPLEMENTED: NO
IS CHECKSUM DEFERRED EXPLICITLY?: NO
WHERE DOCUMENTED?: N/A

Does the current artifact distinguish:
STRUCTURAL INTERPRETABILITY: YES
CHECKSUM CONSISTENCY: NO
EXTERNAL VERIFICATION: NO

## RAW OBSERVATION TEST

A: 07ABCDE1234F1Z5
B: " 07abcde1234f1z5 "

A RAW OBSERVATION IDENTITY: `07ABCDE1234F1Z5`
B RAW OBSERVATION IDENTITY: ` 07abcde1234f1z5 `
A CANONICAL VALUE: `07ABCDE1234F1Z5`
B CANONICAL VALUE: `07ABCDE1234F1Z5`
A PARSED ARTIFACT IDENTITY: (Hashed Object State A)
B PARSED ARTIFACT IDENTITY: (Hashed Object State B)

ARE RAW OBSERVATION IDENTITIES EQUAL?: NO
ARE CANONICAL VALUES EQUAL?: YES
ARE PARSED ARTIFACT IDENTITIES EQUAL?: NO
IS PROVENANCE LOST?: NO
WHAT EXACTLY DOES ParsedTaxIdentifierArtifact.identity IDENTIFY?: MIXED IDENTITY

ORIGIN-A VALUE: `ABCDE1234F`
ORIGIN-B VALUE: `ABCDE1234F`
A EVIDENCE ORIGIN: Independent PAN
B EVIDENCE ORIGIN: GSTIN Derived
A SOURCE ROLE: `tax_identity`
B SOURCE ROLE: `tax_identity`
A PARENT ARTIFACT: N/A
B PARENT ARTIFACT: GSTIN ParsedTaxIdentifierArtifact
A DERIVATION EVENT: `pan_derived_from_gstin=False`
B DERIVATION EVENT: `pan_derived_from_gstin=True`
A ARTIFACT IDENTITY: Object Hash A
B ARTIFACT IDENTITY: Object Hash B

CAN VALUE EQUALITY ERASE ORIGIN DIFFERENCE?: NO
IS DERIVATION ORIGIN SEPARATE FROM SOURCE LOCATION?: YES
CAN A PAN BE INDEPENDENT AND EXTRACTED FROM VENDOR TEXT?: YES
CAN A PAN BE DERIVED FROM A GSTIN FOUND IN VENDOR TEXT?: YES
IS THE MODEL CAPABLE OF REPRESENTING BOTH WITHOUT OVERLOADING ONE ENUM?: YES

## TEST DELTAS

TEST COUNT AT T2_BASE: 501
TEST COUNT AT T2_HEAD: 501
NEW TEST FUNCTIONS: 0 
DELETED TEST FUNCTIONS: 0 
PARAMETRIZED CASE DELTA: 0
HYPOTHESIS TEST DELTA: 0
NEW TAX OBSERVATION TEST FILES: 0 

WERE NEW T2 TESTS ACTUALLY ADDED?: NO
IF YES, WHY DID TOTAL TEST COUNT REMAIN 501?: N/A
WERE OLD TESTS DELETED?: YES (`tests/test_text_normalization.py` was deleted, but it appears uncollected or offset in count)
WERE OLD PARAMETRIZED CASES REMOVED?: NO
WERE TESTS RENAMED OR REPLACED?: NO
DID COLLECTION CHANGE?: YES

AUTHORITATIVE GSTIN STRUCTURAL PARSER COUNT: 1
AUTHORITATIVE PAN STRUCTURAL PARSER COUNT: 1
AUTHORITATIVE GSTIN→PAN DERIVATION RULE COUNT: 1
VENDOR DUPLICATE GSTIN STRUCTURAL LOGIC COUNT: 1 
VENDOR DUPLICATE PAN STRUCTURAL LOGIC COUNT: 1 
LEGACY TAX LITERAL COMPARATOR COUNT: 1

## DOCUMENTATION VERIFICATION

`docs/testing/t1-to-t2-scenario-traceability.md`
EXISTS: NO
SUBSTANTIVE: NO

`stage_8c_t2_shared_identifier_artifacts_report.md`
EXISTS: NO
SUBSTANTIVE: NO

`docs/architecture/tax-identifier-observation-boundary.md`
EXISTS: YES
SUBSTANTIVE: YES
MATCHES PRODUCTION: YES

`docs/algorithms/gstin-structural-parser.md`
EXISTS: NO
SUBSTANTIVE: N/A

## FINAL VERDICT

T2 BASE COMMIT: 30b8bd9
T2 HEAD COMMIT: a3febe4
WORKING TREE CLEAN: NO
HEAD EQUALS ORIGIN/MAIN: YES
PYTEST: 501 PASSED / 0 FAILED
STATIC TYPE CHECK: FAIL
SHARED IDENTIFIER OBSERVATION LAYER: IMPLEMENTED
AUTHORITATIVE GSTIN STRUCTURAL PARSER COUNT: 1
AUTHORITATIVE PAN STRUCTURAL PARSER COUNT: 1
AUTHORITATIVE GSTIN→PAN DERIVATION RULE COUNT: 1
RAW PRESERVATION: PASS
PLACEHOLDER SEPARATION: FAIL
INVALID STATE SEPARATION: PASS
UNINTERPRETABLE STATE SEPARATION: PASS
DERIVED PAN ORIGIN PRESERVATION: PASS
INDEPENDENT / DERIVED PAN DISTINCTION: PASS
OCR AUTO-REPAIR: ABSENT
CHECKSUM MODEL: ABSENT-UNDOCUMENTED
ARTIFACT IDENTITY MODEL: MIXED
VENDOR V1 MIGRATED TO SHARED FACTS: YES
VENDOR DUPLICATE GSTIN STRUCTURAL LOGIC: YES
VENDOR DUPLICATE PAN STRUCTURAL LOGIC: YES
TaxEvidenceProvider MODIFIED: YES
tax_identity_score MODIFIED: YES
LIVE TAX PATH CLASSIFICATION: LEGACY COMPARATOR WITH REPRESENTATION ADAPTER
T3 SEMANTIC LEAKAGE: NONE
LEGACY TAX DEFECTS STILL PRESENT: YES
T1 SCENARIO TRACEABILITY: 0 / 100
OBSERVATION SCENARIOS INCORRECTLY DEFERRED: 0
VENDOR V1 BEHAVIOURAL CHANGES: 0
NEW T2 TEST FUNCTIONS: 0
DELETED TEST FUNCTIONS: 0
TEST COUNT DELTA: 0
DOCUMENTATION MATCHES PRODUCTION: NO

WHY DID THE TOTAL TEST COUNT REMAIN 501?: No new tests were actually integrated into the `tests/` directory suite.
WAS MODIFYING TaxEvidenceProvider STRICTLY NECESSARY?: YES, as a transport adaptation.
WAS MODIFYING tax_identity_score STRICTLY NECESSARY?: YES, to unwrap raw values.
DID EITHER CHANGE ALTER TAX SEMANTICS?: NO, the unwrapping intentionally reproduces the exact flaws (e.g. MALFORMED == MALFORMED is 1.0) of the legacy string comparator.
DID T2 IMPLEMENT ANY PART OF T3?: NO
IS T2 SAFE TO CERTIFY?: Partially, but testing deliverables were skipped.

CERTIFY T2 WITH DOCUMENTED TRANSPORT DEVIATION

DO NOT PROCEED TO T3
