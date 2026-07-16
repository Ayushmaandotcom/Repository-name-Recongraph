# ReconGraph Roadmap

## v1.1 - The Explainability Polish
- UI framework for rendering the `ExplanationArtifact` as interactive React components.
- Human-in-the-loop CLI for manual review of `REVIEW_AMBIGUOUS` packets.

## v1.2 - The Missing Data Solver
- Expanding FusionNode capabilities to handle `Missingness`, differentiating between "Evidence is absent" vs. "Evidence contradicts".
- Support for generating automated query prompts to external providers when confidence is low.

## v2.0 - Network-Level Fusion
- Beyond pairwise reconciliations (Purchase -> GST).
- Graph-level reconciliation resolving multi-hop semantic networks (e.g., Purchase -> Invoice -> Ledger -> GST).
