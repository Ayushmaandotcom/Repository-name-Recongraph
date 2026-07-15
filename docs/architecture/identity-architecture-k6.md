# K6 Identity Architecture

## Overview
Identity across ReconGraph follows the K6 Domain-Separated Hashing Philosophy. 

Identities are derived from domain boundaries (e.g. `recongraph:decision_trace:v1\x00`) prefixed to Canonical JSON serializations.

## Artifact Identities
1. **Decision Trace**: Identifies the complete semantic evaluation scope (Nodes, Config, Version) AND the semantic outcome (Decision, Score, Eligibility).
2. **Derived Artifacts**: e.g., `VendorNameObservation`, `TaxIdentityObservation`. Identifies the parsed interpretation of raw strings. Changes only when parser version or raw text changes.
3. **Core Domain Objects**: Purchase and GST records.

## Rules
- Do NOT use floating point values in identity generation (canonicalized to basis points).
- Do NOT use un-ordered iterables (lists are sorted).
- Always use explicit semantic versioning in schemas (e.g., `recongraph.decision_trace_identity.v1`).
