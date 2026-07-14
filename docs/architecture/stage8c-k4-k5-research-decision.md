# Final Frozen Decision Report (Stage 8C-K4/K5-0A)
## Part S — Doctrine

### Chosen Architecture
- **Chosen source ontology**: 3-part (SourceSystem, SourceArtifact, SourceLocator).
- **Chosen source identity model**: Extensible opaque coordinates, temporal timestamps explicitly excluded.
- **Chosen observation provenance model**: `ObservationProvenance` relational wrapper (Model C/D variant).
- **K3 amendment required**: NO code changes, but vocabulary formally updated to distinguish "Observation Content State" from "Observation Occurrence".
- **Chosen lineage model**: `StructuredSourceLineage` as a flat immutable composition of the 3-part ontology.
- **Chosen provider identity model**: `ProviderId` + `ProviderSemanticVersion`.
- **Chosen derivation identity model**: Deterministic SHA-256 over Provider, Method, and Canonicalized Inputs.
- **Chosen input binding semantics**: Role-bound `DerivationInputBinding` grouped in a `DerivationInputSet` with Method-dictated sorting rules.
- **DerivedArtifact required**: YES. Strict materialization rule enforced.
- **Evidence DAG accepted**: YES. Strictly acyclic.
- **Privacy identity stance**: Acknowledged leakage; deferring to tenant-scoped salts at persistence layer.

### Allowed Shapes (Next Stage)
```python
@dataclass(frozen=True)
class SourceSystemId:
    value: str

@dataclass(frozen=True)
class SourceNodeRef:
    kind: str
    ref: str

@dataclass(frozen=True)
class StructuredSourceLineage:
    source_system: SourceSystemId
    source_node: SourceNodeRef
    source_version: Optional[str]

@dataclass(frozen=True)
class ObservationProvenance:
    observation: ObservationIdentity
    lineage: StructuredSourceLineage
```
