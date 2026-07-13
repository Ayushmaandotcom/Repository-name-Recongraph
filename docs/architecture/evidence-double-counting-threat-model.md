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
