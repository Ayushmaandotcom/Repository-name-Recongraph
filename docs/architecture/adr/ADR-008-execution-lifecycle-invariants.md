# ADR-008: Execution Lifecycle Invariants

## Status
Accepted

## Context
During the V2 refactor of ReconGraph (Stage 8), it was discovered that `pair_scorers.py` was actively bypassing `EvidenceProviders` and manually invoking legacy scaling functions (`tax_identity_score`, `temporal_score`), parsing strings inline, and executing sub-pipeline logic directly.

This architectural leakage resulted in overlapping authorities, making it impossible to guarantee that legacy string matching algorithms weren't still being executed in production despite the existence of deterministic parsers.

## Decision
We establish a strict Canonical Execution Lifecycle with non-negotiable invariants.

### Invariant 1: Provider Isolation
`EvidenceProvider.evaluate()` is the ONLY acceptable entry point for generating domain evidence. Pair Scorers and Evaluators MUST NOT instantiate inner pipeline components (`extract`, `interpret`, `project`) directly.

### Invariant 2: Pipeline Symmetry
Every domain (Vendor, Tax, Financial, Reference, Temporal) MUST implement four layers:
1. `Artifacts`: Deterministic parsing of raw inputs.
2. `Interpretation`: Generation of Semantic Relations (`EXACT_MATCH`, `DISTINCT`, etc.).
3. `Projection`: Lossy conversion of Semantic Relations into `float` scalars.
4. `Contribution`: Final payload delivered to Pair Scorers.

### Invariant 3: Parser Authority
Parsers are the only modules permitted to use regex, slicing, normalization, or token counting. 

### Invariant 4: Scorer Ignorance
Pair Scorers aggregate scalars. They MUST NOT generate semantic findings or determine match eligibility. 

## Consequences
- Legacy score functions (`tax_identity_score`, `temporal_score`) are strictly forbidden and have been deleted.
- The `DecisionEngine` (`HypothesisEvaluator`) now solely owns `Eligibility` and `SemanticFindings`.
- Any new domain must conform to the 4-layer Pipeline Symmetry or it will fail CI.
