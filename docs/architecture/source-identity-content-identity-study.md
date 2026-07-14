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
