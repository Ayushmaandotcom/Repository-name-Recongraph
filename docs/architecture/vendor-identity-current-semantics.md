# Vendor Identity Current Semantics

## Semantic Audit of Vendor Architecture

This document audits the current production meaning of "vendor" and related concepts across the ReconGraph codebase. The goal is to identify exactly what is being claimed when a "vendor score" is produced.

### Dependency Table

| Producer | Observation | Transformation | Output Meaning | Missing Semantics | Consumers | Production Authority |
|---|---|---|---|---|---|---|
| `VendorEvidenceProvider` | `vendor_name` from Purchase and GST | Concatenate all names per side, lowercase, exact string equality | A binary structural claim: `1.0` if the raw concatenated string is identical, `0.5` if they differ. This claims NOTHING about semantic organizational identity, only raw byte equivalence of the concatenated payload. | Returns `None` if either side is empty. | `HypothesisEvaluator`, `EvidenceSummary` | **LIVE PRODUCTION** |
| `entity_score()` | `vendor_name` from single Purchase/GST | Lowercase, strip punctuation, remove 4 legal suffixes, apply 5 token aliases, calculate Levenshtein ratio | A scalar magnitude representing the edit distance of lexically filtered strings. Claims that character similarity is a proxy for organizational identity, without regard to token discriminativeness or legal entity structure. | Returns `None` if either side is empty or fully filtered. | `score_purchase_to_gst()` | *Legacy / Experimental* |
| `analyze_purchase_gst_semantics` | `entity` score from legacy pair scorer | Direct comparison `>= 0.9` | Claims that high lexical edit distance (`>= 0.9`) definitively proves `DISTINCT_EVENT_IDENTITY_EVIDENCE`. Confuses textual similarity with legal identity proof. | Implicitly treats `None` as failing the `>= 0.9` check. | `SemanticFinding` | *Legacy / Experimental* |
| `TaxEvidenceProvider` (Missing) | `tax_identity` | None. Currently acts as ExactMatchBlocker / generic string match. | Claims raw string equality. Since `tax_identity` often holds GSTIN, this implicitly proxies Legal Entity Identity, but the engine is blind to this. | Fails to match. | `HypothesisEvaluator` | **LIVE PRODUCTION** |
| `EvidenceSummary` | `entity_score` | Defaults missing values to `0.0` | Claims that the absence of vendor name evidence is equivalent to a maximal authoritative contradiction (0.0). | Converts `None` (absence) to `0.0` (conflict). | Human Review, Explanations | **LIVE PRODUCTION** |

### Critical Semantic Findings

1. **Vendor Score is NOT Organizational Identity:** The live production engine (`VendorEvidenceProvider`) does not even measure similarity. It measures exact byte equivalence of concatenated strings. `1.0` means exact string match. `0.5` means anything else. It is a coarse structural filter, not an identity claim.
2. **Missingness is Confused with Conflict:** The explanation layer (`EvidenceSummary`) translates a missing `vendor_name` into an `entity_score` of `0.0`. In the engine's scalar algebra, `0.0` means active contradiction. Treating "I don't know the vendor name" as "I have proof these are different vendors" is a severe epistemic bug.
3. **Lexical Similarity is Confused with Legal Proof:** The legacy `entity_score()` assumes that a high Levenshtein ratio (e.g., `0.95`) proves they are the same organization. This is false. `ABC LLP` and `ABC LTD` have high lexical similarity but are distinct legal entities.
4. **Tax Identity is Conflated with Vendor Identity:** GSTIN encodes organizational identity. By scoring Tax Identity and Vendor Name as two independent variables in a weighted sum, the engine double-counts organizational identity evidence without realizing they are structurally correlated.
