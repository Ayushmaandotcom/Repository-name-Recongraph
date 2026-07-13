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
