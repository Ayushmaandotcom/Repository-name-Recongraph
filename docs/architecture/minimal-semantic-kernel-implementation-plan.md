# Minimal Semantic Kernel Implementation Plan

This is the exact implementation blueprint for Stage 8C (Part O). 
**Note:** This is a plan only. Do not execute until authorized.

## Phases

### Phase K1 — Claim primitives
* **Create:** `src/recongraph/domain/claims.py`
* **Implement:** `ClaimDescriptor` value object with `is_symmetric`, `semantic_version`, `allowed_scope_kinds`.
* **RED Test Order:** 1. Instantiation. 2. Immutability.

### Phase K2 — Scope primitives
* **Create:** `src/recongraph/domain/scopes.py`
* **Implement:** `AssertionScope` dataclass (Left/Right nodes).
* **RED Test Order:** 1. Basic equality. 2. Symmetry canonicalization (relies on ClaimDescriptor). 3. Directionality preservation. 4. Overlap non-equality.

### Phase K3 — Observation identity/state
* **Create:** `src/recongraph/domain/observations.py`
* **Implement:** `ObservationIdentity`, `ObservationState` Enum, `InterpretationState` Enum.
* **RED Test Order:** 1. State distinctness. 2. Structural ID formatting.

### Phase K4 — Lineage
* **Create:** `src/recongraph/domain/lineage.py`
* **Implement:** `StructuredSourceLineage`.
* **RED Test Order:** 1. Serialization round-trip.

### Phase K5 — Derivation metadata
* **Create:** `src/recongraph/domain/derivation.py`
* **Implement:** `DerivationMetadata` (Provider ID, semantic version, policy hash).
* **RED Test Order:** 1. Equality.

### Phase K6 — Quality context
* **Create:** `src/recongraph/domain/quality.py`
* **Implement:** `EvidenceQualityContext` (Source trust, extraction trust).
* **RED Test Order:** 1. Distinct layers of trust.

### Phase K7 — Typed payload envelope
* **Create:** `src/recongraph/domain/payload.py`
* **Implement:** `TaggedPayload` base protocol/union.
* **RED Test Order:** 1. JSON Serialization. 2. Unknown payload fallback.

### Phase K8 — EvidenceAssertion
* **Create:** `src/recongraph/domain/assertion.py`
* **Implement:** `EvidenceAssertion` dataclass combining all primitives.
* **RED Test Order:** 1. Full structural equality. 2. Magnitude boundary validation. 3. Missingness/Conflict constraints (EM2-011 through EM2-013).

### Phase K9 — Trace serialization
* **Modify:** `src/recongraph/graph/trace.py`
* **Implement:** JSON encoding/decoding for `EvidenceAssertion`.
* **RED Test Order:** 1. Full round-trip of an assertion. 2. Graceful degradation on unknown claims/payloads.

### Phase K10 — V1 compatibility adapter boundary
* **Modify:** `src/recongraph/plugins/core_providers.py`
* **Implement:** An explicit adapter that takes a mock `EvidenceAssertion` and projects its `support_magnitude` down to the legacy scalar score output for the Decision Engine to consume.
* **RED Test Order:** 1. Projection mathematically matches legacy behavior.

## Impact & Rollback
* **Config hash impact:** Minimal (new structures don't alter legacy scoring config yet).
* **Serialization impact:** V2 Trace schema will evolve, but V1 trace readers will not break as long as we bump the schema version.
* **Rollback strategy:** Git reset. No production dependencies are broken because we do not wire V2 into the core Decision Engine until Stage 8J.
