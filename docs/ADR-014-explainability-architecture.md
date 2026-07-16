# ADR-014: Multi-Layer Explainability Architecture

## Status
Accepted

## Context
ReconGraph's transition from a heuristic-based engine to a multi-evidence reasoning graph (Fusion Engine) required a fundamental rethinking of how decisions are explained. Previously, explanations were generated using hardcoded text templates based on final scores (e.g., "Semantic violation: tax_identity_conflict"). This approach suffered from several fatal flaws:
1. **Hallucination Risk:** Explanations could diverge from actual reasoning if templates drifted from the logic.
2. **Opacity:** It was impossible to tell *why* a penalty was applied without reading the code.
3. **Loss of Provenance:** The explanation had no cryptographic or deterministic link to the execution state.
4. **Single Audience:** Explanations were either too vague for engineers or too technical for business users.

## Decision
We will implement a **Multi-Layer Explainability Architecture** that generates explanations as deterministic artifacts derived directly from the `FusionResult` and `DecisionTrace`.

The explanation artifact will be structured into four distinct layers, targeting different audiences:
- **Layer 1: Executive Summary** - Non-technical business users. "What was decided?"
- **Layer 2: Domain Summaries** - Domain analysts. "What did the Vendor domain conclude?"
- **Layer 3: Technical Details** - Support engineers. "Which node contradicted the hypothesis?"
- **Layer 4: Audit Nodes** - System auditors & algorithms. Cryptographic node-by-node graph representation.

### Explainability Constraints
1. **No Hallucination:** The explanation generator must only read from `FusionResult` and `EvidenceGraph`. It cannot invent reasons or evaluate rules.
2. **Deterministic:** Given the same `FusionResult` and `DecisionTrace`, the `ExplanationGenerator` must produce an identical `ExplanationArtifact` down to the hash.
3. **Lazy Evaluation:** Layer 4 graph reconstruction is computationally expensive and is stored structurally. It is only serialized to visual formats (e.g., Mermaid) on-demand.
4. **Mirror Image:** The explanation engine is the exact structural inverse of the reasoning engine.

## Consequences
- **Positive:** Explanations are provably correct and mathematically linked to the exact execution trace that generated them.
- **Positive:** UI consumers can request different layers of explanation depending on the user's role.
- **Negative:** The explanation object is larger and more complex than a simple string array.
- **Negative:** Requires storing structural graph nodes instead of localized strings.
