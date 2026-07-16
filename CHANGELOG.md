# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-16

This is the initial production release of the ReconGraph engine.

### Added
- **Multi-Evidence Fusion Engine**: Completely overhauled reasoning architecture migrating from legacy heuristics to a formal DAG-based fusion graph.
- **Explainability Engine**: Deterministic `ExplanationArtifact` generation across 4 layers of resolution (Executive, Domain, Technical, Audit).
- **Provenance Contract**: Strict cryptographic `trace_id` generation linked to the underlying `DecisionTrace` and `EvidenceGraph`.
- **Domain Pipelines**: Formal observation, interpretation, and projection pipelines for Vendor, Tax, Financial, Reference, and Temporal domains.
- **Candidate Generator**: Replaced monolithic pairwise looping with O(1) identifier and hash blocking.
- **Shadow Mode**: Differential reporting for A/B testing graph reasoning vs. legacy string-distance execution without impacting live workflows.
- **Mermaid Visualizer**: Export `ExplanationArtifact` audit nodes directly into Mermaid diagrams.

### Removed
- Removed monolithic `PairScorer` logic (`score_purchase_to_gst`).
- Removed text-based hallucination-prone explanation generation.

### Security
- Evaluator loop limits and cycle detection built into `PropagationStatus`.
