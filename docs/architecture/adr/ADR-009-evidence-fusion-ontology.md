# ADR-009: Evidence Fusion Ontology

## Status
Active

## Context
ReconGraph's EvidenceProviders currently output a scalar score and metadata via `EvidenceContributionV2`. To achieve true multi-evidence reasoning, we need a formalized ontology to represent the interaction between these isolated pipelines. We must distinguish between raw data, structural interpretation, domain projection, and graph-level fusion.

## Decision
We adopt the Canonical Evidence Ontology for all fusion operations in Stage 8J.

The ontology consists of:
1. `EvidenceObservation`: Raw data strings.
2. `EvidenceInterpretation`: Structural geometry.
3. `EvidenceProjection`: Domain-specific scores.
4. `EvidenceContribution`: The universal interface.
5. `EvidenceGraph`: The DAG of all contributions for a hypothesis.
6. `FusionNode`: A vertex representing a single Contribution.
7. `FusionEdge`: An edge representing corroboration or contradiction.
8. `FusionPolicy`: The accumulation rules.
9. `FusionResult`: The final topological evaluation.
10. `FusionExplanation`: The traceability artifact.

## Consequences
- The legacy `PairScorer` will be completely deprecated in favor of `EvidenceGraph` construction and `FusionPolicy` evaluation.
- All domain providers must conform strictly to emitting `EvidenceContributionV2` so the `FusionNode` can remain provider-agnostic.
