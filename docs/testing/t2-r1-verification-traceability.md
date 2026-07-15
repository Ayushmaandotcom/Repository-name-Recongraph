# T2-R1 Verification Traceability Matrix

This document maps every T2 observation/parser invariant to its production symbol, evidence source, and test target.

## Observation State Boundary

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| OBS-001 | T2 AUTHORIZATION | `DeterministicTaxParser.parse(None)` | `stage_8c_t1_tests.py` STATE-001 | `test_tax_identifier_observation.py::test_obs_001_none_input` | CONFORMANCE | PASS |
| OBS-002 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("")` | None | `test_tax_identifier_observation.py::test_obs_002_empty_string` | CONFORMANCE | PASS |
| OBS-003 | T2 AUTHORIZATION | `DeterministicTaxParser.parse(" ")` | `stage_8c_t1_tests.py` STATE-009 | `test_tax_identifier_observation.py::test_obs_003_single_space` | CONFORMANCE | PASS |
| OBS-004 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("   ")` | None | `test_tax_identifier_observation.py::test_obs_004_multiple_spaces` | CONFORMANCE | PASS |
| OBS-005 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("\t")` | None | `test_tax_identifier_observation.py::test_obs_005_tab_only` | CONFORMANCE | PASS |
| OBS-006 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("\n")` | None | `test_tax_identifier_observation.py::test_obs_006_newline_only` | CONFORMANCE | PASS |
| OBS-007 | T1 FALSIFICATION | `DeterministicTaxParser.parse("UNKNOWN")` | `stage_8c_t1_tests.py` STATE-010 | `test_tax_identifier_observation.py::test_obs_007_unknown_upper` | CONFORMANCE | PASS |
| OBS-008 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("unknown")` | None | `test_tax_identifier_observation.py::test_obs_008_unknown_lower` | CONFORMANCE | PASS |
| OBS-009 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("Unknown")` | None | `test_tax_identifier_observation.py::test_obs_009_unknown_mixed` | CONFORMANCE | PASS |
| OBS-010 | T1 FALSIFICATION | `DeterministicTaxParser.parse("N/A")` | `stage_8c_t1_tests.py` STATE-011 | `test_tax_identifier_observation.py::test_obs_010_na_slash` | CONFORMANCE | PASS |
| OBS-011 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("n/a")` | None | `test_tax_identifier_observation.py::test_obs_011_na_lower` | CONFORMANCE | PASS |
| OBS-012 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("NA")` | None | `test_tax_identifier_observation.py::test_obs_012_na_upper` | CONFORMANCE | PASS |
| OBS-013 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("na")` | None | `test_tax_identifier_observation.py::test_obs_013_na_lower_plain` | CONFORMANCE | PASS |
| OBS-014 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("NULL")` | None | `test_tax_identifier_observation.py::test_obs_014_null_upper` | CONFORMANCE | PASS |
| OBS-015 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("null")` | None | `test_tax_identifier_observation.py::test_obs_015_null_lower` | CONFORMANCE | PASS |
| OBS-016 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("-")` | None | `test_tax_identifier_observation.py::test_obs_016_hyphen` | CONFORMANCE | PASS |
| OBS-017 | T1 FALSIFICATION | `DeterministicTaxParser.parse("MALFORMED")` | `stage_8c_t1_tests.py` STATE-008 | `test_tax_identifier_observation.py::test_obs_017_malformed` | CONFORMANCE | PASS |
| OBS-018 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("This is random text")` | None | `test_tax_identifier_observation.py::test_obs_018_random_prose` | CONFORMANCE | PASS |
| OBS-019 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("ABCDE1234F")` | None | `test_tax_identifier_observation.py::test_obs_019_pan_shaped` | CONFORMANCE | PASS |
| OBS-020 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("07ABCDE1234F1Z5")` | `stage_8c_t1_audit.py` TEQ-001 | `test_tax_identifier_observation.py::test_obs_020_gstin_shaped` | CONFORMANCE | PASS |

## GSTIN Structural Conformance

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| GST-001 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("07ABCDE1234F1Z5")` | TEQ-001 | `test_tax_identifier_parser.py::test_gst_001_accepted_gstin` | CONFORMANCE | PASS |
| GST-002 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("07abcde1234f1z5")` | TEQ-003 | `test_tax_identifier_parser.py::test_gst_002_lowercase_gstin` | CONFORMANCE | PASS |
| GST-003 | T2 AUTHORIZATION | `DeterministicTaxParser.parse(" 07ABCDE1234F1Z5 ")` | TEQ-002 | `test_tax_identifier_parser.py::test_gst_003_whitespace_gstin` | CONFORMANCE | PASS |
| GST-004 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("07ABCDE1234F1Z")` | None | `test_tax_identifier_parser.py::test_gst_004_14_char_not_gstin` | CONFORMANCE | PASS |
| GST-005 | T2 AUTHORIZATION | `DeterministicTaxParser.parse("07ABCDE1234F1Z55")` | None | `test_tax_identifier_parser.py::test_gst_005_16_char_not_gstin` | CONFORMANCE | PASS |
| GST-006..020 | T2 AUTHORIZATION | Various structural mutation fixtures | None | `test_tax_identifier_parser.py::test_gst_*` | CONFORMANCE | PASS |

## PAN Structural Conformance

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| PAN-001..020 | T2 AUTHORIZATION | `DeterministicTaxParser.parse(...)` | None | `test_tax_identifier_parser.py::test_pan_*` | CONFORMANCE | PASS |

## Derivation Boundary

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DER-001..016 | T2 AUTHORIZATION | `ParsedTaxIdentifierArtifact.pan_derived_from_gstin` | None | `test_tax_identifier_derivation.py::test_der_*` | CONFORMANCE | PASS |

## Artifact Identity

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| AID-001..013 | T2 CERTIFICATION AUDIT | `ParsedTaxIdentifierArtifact` frozen dataclass identity | None | `test_tax_identifier_artifact_identity.py::test_aid_*` | UNIT | PASS |

## Metamorphic / Property Tests

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| MP-001..025 | T2 AUTHORIZATION | Various | None | `test_tax_identifier_properties.py::test_mp_*` | PROPERTY | PASS |
| ADV-001..010 | T2 AUTHORIZATION | `DeterministicTaxParser` | None | `test_tax_identifier_properties.py::test_adversarial_*` | PROPERTY | PASS |
| OCR-001..005 | T2 AUTHORIZATION | `DeterministicTaxParser` | None | `test_tax_identifier_properties.py::test_ocr_*` | PROPERTY | PASS |

## Legacy Boundary Characterization

| Invariant ID | Original Source | Production Symbol | Experiment Evidence | Pytest Target | Test Layer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| LEGACY-001 | T2 CERTIFICATION AUDIT | `tax_identity_score` | `stage_8c_t1_tests.py` STATE-008 | `test_tax_identifier_parser.py::test_legacy_001_malformed_malformed` | LEGACY BOUNDARY CHARACTERIZATION | PASS |
| LEGACY-002 | T2 CERTIFICATION AUDIT | `tax_identity_score` | `stage_8c_t1_tests.py` STATE-010 | `test_tax_identifier_parser.py::test_legacy_002_unknown_unknown` | LEGACY BOUNDARY CHARACTERIZATION | PASS |
| LEGACY-003 | T2 CERTIFICATION AUDIT | `tax_identity_score` | `stage_8c_t1_tests.py` STATE-011 | `test_tax_identifier_parser.py::test_legacy_003_na_na` | LEGACY BOUNDARY CHARACTERIZATION | PASS |
| LEGACY-004 | T2 CERTIFICATION AUDIT | `tax_identity_score` | `stage_8c_t1_audit.py` TEQ-011 | `test_tax_identifier_parser.py::test_legacy_004_interstate_same_pan` | LEGACY BOUNDARY CHARACTERIZATION | PASS |
