# Explainability in ReconGraph

ReconGraph replaces traditional heuristic-based string explanations with a robust **Multi-Layer Explainability Framework**. When the Fusion Engine makes a decision, it generates a deterministic `ExplanationArtifact` derived strictly from the `FusionResult` and the `EvidenceGraph`.

## The Explanation Artifact

The `ExplanationArtifact` is designed to serve multiple personas concurrently without losing precision or clarity. It consists of four distinct layers:

### Layer 1: Executive Summary
**Audience:** Operations Managers, Business Analysts
**Purpose:** High-level summary of what happened.
**Content:**
- Final decision action (e.g., `AUTO_MATCH`, `REVIEW_WEAK`).
- Overall coverage and hypothesis score.
- High-level rationale.

### Layer 2: Domain Summaries
**Audience:** Domain Experts (e.g., Tax Analysts)
**Purpose:** Understand how specific domains behaved.
**Content:**
- Aggregated state per domain (e.g., Tax identity is supported, Vendor name has contradictions).
- Provider scores isolated from the whole.

### Layer 3: Technical Details
**Audience:** L1/L2 Support Engineers
**Purpose:** Debug anomalies and pinpoint contradictions.
**Content:**
- A list of explicit `missing_domains`.
- A list of explicitly `contradicted` nodes (e.g., `TAX_NODE`).
- Node status states.

### Layer 4: Audit Nodes
**Audience:** System Auditors, Machine Learning models, Graph Visualizers
**Purpose:** Provide full cryptographic provenance.
**Content:**
- Raw serialized `ExplanationNode` representations.
- Includes `TraceExplanation`, `DecisionExplanation`, `FusionExplanation`, `PropagationExplanation`, and `ContributionExplanation`.
- Serves as the immutable backend for rendering interactive Mermaid diagrams.

## Explainability Generation
Explanations are generated via the `ExplanationGenerator` which takes the `DecisionTrace`, `EvidenceGraph`, and `FusionResult` as input.

```python
from recongraph.graph.explanation_generator import ExplanationGenerator

generator = ExplanationGenerator(trace, evidence_graph, fusion_result)
explanation_artifact = generator.generate()
```

By keeping the generation logic purely deterministic, ReconGraph ensures that explanations are never "hallucinated" and always match the executed code perfectly.
