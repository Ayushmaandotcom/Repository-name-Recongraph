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
