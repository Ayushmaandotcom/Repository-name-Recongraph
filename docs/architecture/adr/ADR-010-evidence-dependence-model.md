# ADR-010: Evidence Dependence Model

## Status
Active

## Context
When aggregating multiple sources of evidence (e.g., matching a Vendor Name and matching a Tax GSTIN), naively adding their scores together causes "double-counting" if the two sources are heavily correlated or derived from the same real-world phenomenon. 

## Decision
We formally adopt a Topological Dependency Model for Evidence Fusion. 

All pieces of evidence must be mapped into an `EvidenceGraph` using the following edge definitions:
1. `IndependentEdge`: Additive support (e.g., Amount and Date).
2. `DerivedEdge`: Sub-additive support (e.g., Vendor Name extracted from Tax PAN).
3. `DuplicateEdge`: Constant support (e.g., GSTIN from Invoice and GSTIN from E-way bill).
4. `CorrelatedEdge`: Sub-additive support.

## Consequences
- The Fusion engine will be implemented as a Topological Constraint Satisfaction graph, not a simple weighted sum.
- Adding a new `EvidenceProvider` in the future requires explicitly mapping its topological relationship to all existing providers to prevent double-counting.
