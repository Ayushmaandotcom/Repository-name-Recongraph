# Stage 8J Vendor Fusion Pre-Mortem

**Scenario:** It is six months from now. Stage 8J Evidence Fusion has failed. The system is hallucinating identity links and missing obvious matches. Why did it fail?

## 1. Vendor and Tax Identity were double-counted
* **Failure:** The engine treated a matched vendor name and a matched GSTIN as two independent pieces of evidence, artificially inflating the hypothesis score beyond the truth.
* **Root Architectural Cause:** Flat scalar evidence model lacking correlation groups.
* **Early Warning Signal:** Synthetic tests show 100% confidence for single-document matches.
* **Test That Could Have Caught It:** A test proving that observing the same document twice doesn't double the score.
* **Design Seam Required Today:** Structured Source Lineage.

## 2. Correlation groups were too coarse
* **Failure:** All vendor evidence was dumped into `correlation_group='vendor'`. When the ERP name and the Invoice name matched, the fusion engine treated them as perfectly correlated and threw away the ERP corroboration.
* **Root Architectural Cause:** `correlation_group: str | None` is a flat string.
* **Early Warning Signal:** Inability to express "these two signals corroborate each other across systems".
* **Test That Could Have Caught It:** Cross-system corroboration metric.
* **Design Seam Required Today:** Multi-dimensional provenance (Source System + Document).

## 3. Correlation groups were too static
* **Failure:** Hardcoded correlation groups failed when plugins generated dynamic evidence paths.
* **Root Architectural Cause:** Defining correlation at the plugin class level rather than the observation level.
* **Early Warning Signal:** Plugin registry gets polluted with pseudo-plugins just to alter correlation behavior.
* **Test That Could Have Caught It:** Dynamic plugin loading test.
* **Design Seam Required Today:** Lineage assigned at the `EvidenceContribution` construction time.

## 4. Vendor score collapsed support and conflict
* **Failure:** A vendor name mismatch (conflict) and a missing tax ID (absence) were both treated as a `0.5` score. The engine couldn't tell what was dangerous.
* **Root Architectural Cause:** Using a single `float` to represent multidimensional epistemic states.
* **Early Warning Signal:** Explanation summaries reading "Vendor Score: 0.5".
* **Test That Could Have Caught It:** Metamorphic Authoritative Conflict Preservation test.
* **Design Seam Required Today:** Bipolar evidence (`support`, `conflict`).

## 5. Authority was confused with magnitude
* **Failure:** An exact match on `TRADERS` (high magnitude, low authority) overrode a mismatched GSTIN (high authority).
* **Root Architectural Cause:** No mechanism to express that some evidence types legally veto other evidence types.
* **Early Warning Signal:** The need to add arbitrary `if` statements in the scoring function for tax IDs.
* **Test That Could Have Caught It:** Adversarial pair `ABC LTD (TAX-A)` vs `ABC LTD (TAX-B)`.
* **Design Seam Required Today:** Separation of Lexical Identity and Legal Identity as distinct variables.

## 6. Missing evidence was treated as negative evidence
* **Failure:** Invoices without OCR'd vendor names were actively rejected by the decision engine as conflicts.
* **Root Architectural Cause:** `EvidenceSummary` projecting `None` to `0.0`.
* **Early Warning Signal:** High false negative rates on sparse data.
* **Test That Could Have Caught It:** Missingness Non-Contradiction test.
* **Design Seam Required Today:** Explicit `Unknown` or `Missing` state in the summary.

## 7. Generic names created false identity confidence
* **Failure:** Hundreds of different companies named `XYZ ENTERPRISES` were matched together.
* **Root Architectural Cause:** Treating all tokens as equally discriminative (Levenshtein ratio over strings).
* **Early Warning Signal:** `SHREE GANESH` matches `SHREE BALAJI` with 70% confidence.
* **Test That Could Have Caught It:** Hard-negative corpus testing.
* **Design Seam Required Today:** Corpus profile / token discriminativeness weighting.

## 8. Corporate family similarity was treated as legal identity
* **Failure:** Payments to `TATA MOTORS` were reconciled against invoices for `TATA TECHNOLOGIES`.
* **Root Architectural Cause:** Normalization stripped `MOTORS` and `TECHNOLOGIES` as noise, leaving only `TATA`.
* **Early Warning Signal:** Destructive normalization in `normalize_vendor_name`.
* **Test That Could Have Caught It:** Normalization Destructiveness Audit.
* **Design Seam Required Today:** Strict preservation of organizational core.

## 9. Structured metadata could not be safely deserialized
* **Failure:** Traces from last month crashed the benchmark runner because the `metadata` dict schema changed.
* **Root Architectural Cause:** Untyped `dict[str, Any]` for vendor evidence.
* **Early Warning Signal:** `KeyError` in explanation builders.
* **Test That Could Have Caught It:** Trace replay with schema migration.
* **Design Seam Required Today:** Typed `EvidencePayload` with versions.

## 10. Synthetic calibration corpus failed to represent real vendor ambiguity
* **Failure:** The engine passed all synthetic tests but failed in production because the synthetics only tested exact matches and random typos, not generic tokens or corporate families.
* **Root Architectural Cause:** The synthetic generator lacked knowledge of the real-world statistical distribution of vendor names.
* **Early Warning Signal:** 100% precision on synthetics, 60% on real data.
* **Test That Could Have Caught It:** Corpus-driven adversarial synthetics.
* **Design Seam Required Today:** Hard-negative case injection into the synthetic framework.
