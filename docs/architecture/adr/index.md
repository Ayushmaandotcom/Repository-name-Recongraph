# Architecture Decision Records (ADRs)

This directory contains the historical sequence of architectural decisions that shaped ReconGraph V2.

## Active Decisions (V2 Architecture)

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-008](./ADR-008-execution-lifecycle-invariants.md) | Execution Lifecycle Invariants | **Active** | Defines the strict 4-phase Extract → Interpret → Project → Contribute lifecycle for all evidence domains. Enforces order independence. |
| [ADR-007](./ADR-007-epistemic-strictness.md) | Epistemic Strictness | **Active** | Forbids interpretation layers from re-parsing raw strings. Enforces deterministic separation of extraction and evaluation. |
| [ADR-009](./ADR-009-evidence-fusion-ontology.md) | Evidence Fusion Ontology | **Active** | Adopts the Canonical Evidence Ontology for fusion operations. |
| [ADR-010](./ADR-010-evidence-dependence-model.md) | Evidence Dependence Model | **Active** | Formally adopts a Topological Dependency Model to prevent double-counting. |
| [ADR-011](./ADR-011-contradiction-algebra.md) | Contradiction Algebra | **Active** | Defines Veto Supremacy and Orthogonal Conflict rules. |
| [ADR-012](./ADR-012-missingness-semantics.md) | Missingness Semantics | **Active** | Categorizes missing evidence into 5 ontological states and defines propagation rules. |
| [ADR-013](./ADR-013-fusion-decision-semantics.md) | Fusion Decision Semantics | **Active** | Defines `Compatibility` as the core metric, rejecting "Confidence" or "Probability". |

## Deprecated / Historical Decisions

These documents describe earlier iterations of the engine and are retained only for historical context.

*(No deprecated ADRs currently tracked in V2)*
