# Derivation Ontology
## Part G — Defining Semantic Derivation

### Formal Definition
A semantic derivation is:
> A deterministic semantic transformation whose output may participate in evidence ancestry.

### Classification of Engine Actions
- **extract_reference_identity**: YES (Semantic Derivation)
- **PAN extraction from GSTIN**: YES (Semantic Derivation)
- **financial aggregation**: YES (Semantic Derivation)
- **connected-component BFS**: NO (Graph Algorithmic Action)
- **DecisionEngine classification**: NO (Decision Transformation)

We will strict define DerivationIdentity exclusively for the "YES" category to avoid turning K5 into a generic program trace.
