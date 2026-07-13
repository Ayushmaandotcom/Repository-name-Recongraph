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
