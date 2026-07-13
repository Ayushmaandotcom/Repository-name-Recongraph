# Stage 8C-0A: Organizational Identity Epistemic Audit — Full Report
## ReconGraph @ `/Users/ayushmaangupta/Documents/recongraph`

---

## REPOSITORY DIRECTORY STRUCTURE

```
recongraph/
├── PROJECT_DEFINITION.md
├── README.md
├── pyproject.toml
├── stage5c1_refactor.py
├── datasets/
│   ├── challenge/purchase_register_v1.csv
│   └── raw/purchase_register.csv
├── docs/
│   └── architecture/adr-001-reference-evidence-pipeline.md
├── experiments/
│   ├── compare_tax_penalty_models.py
│   ├── evaluate_purchase_gst_baseline.py
│   ├── evaluate_purchase_gst_challenges.py
│   ├── stage_4d_audit.py
│   └── vendor_similarity_metrics.py
├── src/recongraph/
│   ├── config.py
│   ├── engine.py
│   ├── errors.py
│   ├── benchmark/
│   │   ├── models.py
│   │   └── runner.py
│   ├── candidate_generation/
│   │   ├── blockers.py
│   │   ├── generator.py
│   │   └── index.py
│   ├── domain/
│   │   ├── records.py
│   │   └── financial/
│   │       └── pipeline.py
│   ├── graph/
│   │   ├── algorithms.py
│   │   ├── candidate.py
│   │   ├── decision.py
│   │   ├── evaluator.py
│   │   ├── explainability.py
│   │   ├── hypotheses.py
│   │   ├── review.py
│   │   ├── search.py
│   │   └── trace.py
│   ├── matching/
│   │   ├── pair_scorers.py
│   │   ├── purchase_gst_semantics.py
│   │   ├── reference_evidence.py
│   │   ├── scoring.py
│   │   └── signals.py
│   ├── normalization/
│   │   └── text.py
│   ├── plugins/
│   │   ├── core_providers.py
│   │   ├── provider.py
│   │   └── provider_v2.py
│   └── synthetic/
│       ├── builder.py
│       ├── canonical.py
│       ├── models.py
│       └── operators.py
└── tests/ (19 test files)
```

---

## CURRENT DATA MODEL

### PurchaseRecord — [records.py](file:///Users/ayushmaangupta/Documents/recongraph/src/recongraph/domain/records.py#L5-L20)
- `vendor_name: str | None` — raw free-text string. No structure, no aliases, no canonical form, no authority ID.
- `tax_identity: str | None` — opaque string for GSTIN-like matching; not typed as GSTIN.
- No `gstin`, `cin`, `lei`, `pan`, `vendor_id`, `erp_vendor_id`, `jurisdiction`, `legal_name`, `trading_name`, or `alias` fields exist.

### EvaluatedHypothesis — [hypotheses.py](file:///Users/ayushmaangupta/Documents/recongraph/src/recongraph/graph/hypotheses.py#L38-L48)
- `supporting_evidence["signals"]["entity"]` holds vendor score as a plain `float | None`. No vendor observation objects, no provenance, no per-record breakdowns.

### EvidenceSummary — [explainability.py](file:///Users/ayushmaangupta/Documents/recongraph/src/recongraph/graph/explainability.py#L5-L12)
- `entity_score: float` — scalar float, no provenance.

---

## CURRENT VENDOR ALGORITHM

> [!CAUTION]
> **TWO DIVERGENT VENDOR CODE PATHS EXIST**
>
> `VendorEvidenceProvider.evaluate()` uses a hardcoded binary split (exact lowercase match = 1.0, otherwise = 0.5). It does **not** call `entity_score()` or `normalize_vendor_name()`.
>
> The `entity_score()` function using `fuzz.ratio` and normalization is only called from `score_purchase_to_gst()` in `pair_scorers.py` — the **legacy pair-scoring path** used only by experiments, not by the live engine.

**Live engine path:** `VendorEvidenceProvider` → raw `.lower()` comparison → 1.0 or 0.5

**Legacy experiment path:** `entity_score()` → `normalize_vendor_name()` → `fuzz.ratio` → float

---

## CURRENT SCALAR ASSUMPTIONS (8 locations)

| # | File | What assumes scalar |
|---|------|---------------------|
| 1 | `plugins/provider.py:10` | `score: float \| None` |
| 2 | `plugins/core_providers.py:92-94` | `score = 1.0 if ... else 0.5` |
| 3 | `graph/evaluator.py:62-63` | `signals[name] = contrib.score` (dict[str, float]) |
| 4 | `matching/scoring.py:89-96` | `weighted_numerator += weight * signal_score` |
| 5 | `matching/scoring.py:100-103` | `signals[name] == 0.0` |
| 6 | `matching/purchase_gst_semantics.py:48-55` | `entity >= 0.9` |
| 7 | `graph/explainability.py:64,73` | `entity_score: float`, `>= 0.8` |
| 8 | `benchmark/models.py:28` | `Mapping[str, float]` |

---

## CURRENT PROVENANCE GAPS

1. No per-record breakdown (vendor names concatenated and lost)
2. No normalized form stored in evidence metadata
3. No similarity algorithm attribution
4. No confidence interval — point estimate only
5. No support/conflict decomposition
6. No source field attribution (which record_id produced the observation)
7. DecisionTrace uses `repr()` — no structured vendor serialization
8. VendorEvidenceProvider returns no metadata

---

## CURRENT TEMPORAL GAPS

- `record_date` is available to VendorEvidenceProvider but **not accessed**
- No vendor name valid-from / valid-to intervals
- No name change / acquisition / rename temporal support
- TemporalEvidenceProvider is not cross-referenced with vendor identity

---

## CURRENT KNOWLEDGE GAPS

- **GSTIN:** mapped to generic `tax_identity`, no structure/validation
- **CIN, LEI, PAN, ERP Vendor ID:** zero occurrences
- **Alias Graph:** only 5 hardcoded token pairs in `VENDOR_TOKEN_ALIASES`
- **Corpus Profile:** `ReferenceCorpusProfile` exists; no `VendorCorpusProfile`
- **Jurisdiction:** zero occurrences
- **Corporate Hierarchy:** zero occurrences of parent/subsidiary/group

---

## CURRENT BENCHMARK GAPS

No per-signal distributions, no vendor precision/recall, no mutation sensitivity, no entity coverage, no corporate hierarchy scenarios, no rename scenarios, no GSTIN conflict tracking, no normalization effectiveness.

---

## CURRENT SYNTHETIC FRAMEWORK GAPS

- Cannot generate corporate hierarchy scenarios
- Cannot express historical rename intervals (no valid_from/valid_to)
- Cannot express "same economic group, different legal entity"
- Only 3 mutation operators exist (vendor, reference, amount)

---

## STAGE 8J LINEAGE RISKS

1. **Vendor ↔ Tax identity:** GSTIN encodes PAN → both are proxies for same vendor. Combined weight 0.45 treated as independent.
2. **Vendor ↔ Reference:** vendor-specific invoice series → rare reference already implies same vendor.
3. **Amount ↔ Tax amount:** gross ≈ net + tax → structurally correlated.

**Architecture fails to detect correlation:** no covariance matrix, no dependency graph, no `correlation_group` tag, score collapsed to single float before Decision Engine.

---

## BREAKING-CHANGE SURFACE

Bipolar vendor evidence would break **12 files** across providers, evaluator, scoring, semantics, explainability, benchmarks, and tests.

---

## RECOMMENDED MIGRATION SEAMS

1. **VendorNameObservation** → new `domain/vendor_observation.py`, populate via `metadata["vendor_observation"]` — zero breaking changes
2. **StructuredVendorIdentity** → new `domain/organization.py`, injected via `VendorKnowledgeSnapshot` — not placed on records
3. **VendorEvidencePipeline** → new `plugins/vendor_pipeline.py` implementing `EvidencePipeline[VendorObservation, VendorInterpretation]`
4. **Minimum 8J seam** → add `correlation_group: str | None = None` to `EvidenceContribution` — zero test breakage

---

## UNRESOLVED QUESTIONS

1. Is `tax_identity` always a GSTIN?
2. Is `score_purchase_to_gst()` still a production path? (Two divergent vendor algorithms exist)
3. Why does `EvidenceSummary.entity_score` default to 0.0 instead of None? (Missing treated as conflict, not abstain)
4. Is there any ground truth label dataset?
5. Is `EvidenceStatistics({})` always empty intentionally?
6. `VendorEvidenceProviderV2` does not exist — vendor is V1-only
7. `stage5c1_refactor.py` at root — not audited

---

## CRITICAL CONSTRAINTS

- Did I modify production Python? **NO**
- Did I implement VendorNameObservation? **NO**
- Did I implement normalization? **NO**
- Did I add a legal suffix dictionary? **NO**
- Did I add fuzzy matching? **NO**
- Did I add embeddings? **NO**
- Did I alter VendorEvidenceProvider? **NO**
- Did I alter DecisionEngine? **NO**
