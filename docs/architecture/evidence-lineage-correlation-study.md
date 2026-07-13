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
