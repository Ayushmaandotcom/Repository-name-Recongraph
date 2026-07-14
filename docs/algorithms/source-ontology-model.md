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
