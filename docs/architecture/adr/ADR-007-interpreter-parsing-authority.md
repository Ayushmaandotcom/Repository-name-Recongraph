# ADR-007: Interpreter Parsing Authority

## Status
Accepted

## Context
When comparing domain artifacts (like GSTINs and PANs), it is tempting to use string-slicing logic inside the PairInterpreter (e.g., `l_gstin[2:12]` to extract PANs) to quickly check semantic equivalence.

## Decision
**A PairInterpreter MUST NOT derive observations by reparsing strings.**
All observations must originate from the deterministic parser artifacts (`ParsedTaxIdentifierArtifact`, `VendorNameArtifact`, etc.).

## Rationale
Allowing the interpreter to reparse strings breaks the "single source of truth" principle. It leads to:
1. Multiple normalization policies across the codebase.
2. Fragmented validation and missingness policies.
3. Hidden data extraction logic in interpretation boundaries.

By enforcing that interpreters strictly consume properties derived by the canonical `DeterministicParser`, we ensure identical behavior for all downstream pipelines (Tax, Vendor, Fusion).

## Consequences
If an interpreter needs structural information (e.g., the state code from a GSTIN), the structure must be explicitly extracted by the Parser and materialized on the Artifact. The interpreter merely evaluates the relationship between these materialized properties.
