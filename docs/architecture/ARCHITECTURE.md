# ReconGraph Architecture

## System Overview
ReconGraph is a semantic decision engine for evaluating hypothesis propositions over Purchase and GST records. It models evidence as immutable facts that are combined, scored, and evaluated.

## Identity Model (K6)
- **Observations**: Immutable reflections of source fields.
- **Derivations**: Algorithms applied to observations (e.g. normalization).
- **Assertions**: Strongly-typed semantic claims with polarity and magnitude (e.g., `identity.same_legal_entity`).
All objects have a strictly deterministic, canonicalized `sha256` identity.

## Pipeline Lifecycle (V2 Protocol)
All evidence domains (`Financial`, `Vendor`, `Tax`, `Reference`, `Temporal`) strictly follow the EvidencePipeline protocol:
1. `extract()` -> Observation
2. `interpret()` -> Interpretation
3. `contribute()` -> EvidenceAssertion

## Evidence Model & Decision Engine
Evidence Assertions are aggregated by `DecisionEngine` and processed into a mathematical score.

## ADR Index
- `ADR-001`: Vendor Identity Factorization
- `ADR-002`: Amount Interpretation vs Projection
- `ADR-003`: Decision Trace Semantic Identity
- `ADR-004`: Evidence Pipeline V2 Contract
- `ADR-005`: Evidence Semantic Kernel V2
- `ADR-006`: Tax Scalar Projection Boundary
- `ADR-007`: Interpreter Parsing Authority
