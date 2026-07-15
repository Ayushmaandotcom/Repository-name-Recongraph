# ADR-006: Tax Scalar Projection Boundary

## Status
Accepted

## Context
The `TaxPairInterpreter` evaluates tax relationships observationally (e.g., `GSTINRelationState.DIFFERENT_STATE_SAME_PAN`). However, the legacy Decision Engine (V1) expects a scalar float (0.0 to 1.0) and a set of conflict strings to resolve tax identity scoring.

## Decision
We define a strict Projection Boundary (`TaxV1ProjectionContract`) that acts as a lossy compatibility adapter. This boundary compresses the semantic interpretation into scalar space without allowing the projection layer to make new semantic inferences.

## Information Loss Contract
The transformation into a scalar float (1.0 or 0.0) is a highly destructive operation.

**Information Lost**:
1. **Interstate Matches vs Exact Matches**: The distinction between `GSTINRelationState.EXACT_MATCH` and `GSTINRelationState.DIFFERENT_STATE_SAME_PAN` is destroyed; both collapse into `score = 1.0`.
2. **Missing vs Structural Conflict**: The distinction between missing data and an explicit conflict (`PANRelationState.DISTINCT`) is heavily compressed into `None` vs `0.0`.
3. **Invalid Parsing**: Information regarding strings that failed parsing vs strings that weren't present is destroyed.

**Information Preserved**:
1. A hard conflict exists if and only if two validly parsed identifiers are fundamentally distinct.
2. An exact match exists if any pairwise comparison proves PAN equivalence.

## Consequences
This boundary explicitly isolates the legacy engine's information loss, ensuring the `TaxPairInterpreter` itself retains its high-fidelity ontology for future use in Stage 8J Fusion.
