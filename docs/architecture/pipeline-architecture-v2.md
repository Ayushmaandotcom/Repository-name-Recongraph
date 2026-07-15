# Evidence Pipeline Architecture V2

## Introduction
The `EvidencePipeline` strictly separates Epistemic evaluation (extraction, interpretation) from Policy projection (contribution).

## Contract
`EvidencePipeline[T_Extraction, T_Interpretation]` mandates:
1. `extract`: Extract raw observations from records. (No comparisons)
2. `interpret`: Compare and enrich observations into a domain-specific interpretation payload.
3. `contribute`: Project the interpretation into a `EvidenceContributionV2` containing a normalized [0.0, 1.0] score and semantic findings (violations).

## V1 to V2 Bridging
Currently, `FinancialEvidenceProvider` uses V1 `EvidenceProvider` contract internally wrapping `FinancialEvidencePipeline`.
The V1 provider receives the `EvidenceContributionV2` from `pipeline.contribute()` and maps it to `EvidenceContribution` (V1).

## Projection Responsibility
The `contribute()` method resides on the Pipeline layer.
Projection algorithms (e.g. `project_amount_similarity`) are explicitly evaluated within `contribute()` and their output forms the final score contribution injected into the hypothesis evaluator.
