# Scope Model Design Tournament

## Evaluated Designs

### Scope A — Flat Subject Tuple
* `subjects: tuple[str, ...]`
* Destroys Left/Right bipartite structure. Fails N:M graph compatibility.

### Scope B — Left and Right Subject Sets
* `left_subjects: frozenset[str]`
* `right_subjects: frozenset[str]`
* Retains bipartite structure, but cannot explicitly declare if a claim is symmetric or directional. A reader doesn't know if swapping left/right changes semantics.

### Scope C — Typed EvidenceScope Union
* e.g., `RecordScope`, `PairScope`, `GroupPairScope`
* Extensible but forces downcasting everywhere. Doesn't inherently solve directionality.

### Scope D — Canonical Proposition Subject
```python
@dataclass(frozen=True)
class AssertionSubject:
    subject_type: SubjectType # RECORD, PAIR, GROUP_PAIR
    left: frozenset[str]      # URNs
    right: frozenset[str]     # URNs
    directional: bool
```

## Challenge Answers

**SD-001 Should symmetric claims canonicalize left/right ordering?**
Yes. For symmetric claims (e.g. `same_legal_entity`), `A↔B` and `B↔A` must yield identical assertion scopes to prevent duplicate reasoning. 

**SD-002 If yes, who declares that the claim is symmetric?**
The claim definition itself must know this. It is an inherent property of the proposition.

**SD-003 Does the typed Claim Identifier currently know claim symmetry?**
No. A bare string `identity.same_legal_entity` carries no runtime metadata about its symmetry.

**SD-004 If not, is the claim model too weak?**
Yes. If the kernel cannot ask the claim "are you symmetric?", it cannot safely canonicalize the scope.

**SD-005 Should directionality belong to the claim definition or assertion scope?**
The Claim Definition. The *nature of the proposition* determines if it is directional (`supersedes`) or symmetric (`equals`). The scope merely instantiates it for specific nodes.

**SD-006 What happens if a plugin emits `same_legal_entity` but sets `directional=True`?**
If scope holds directionality independently of the claim, the plugin creates an illegal semantic state.

**SD-007 Can the kernel validate semantic properties of an extensible claim without a claim registry?**
No. Without a minimal descriptor (e.g. a dataclass pairing the string ID with its symmetry flag), the kernel must trust the plugin blindly, which defeats the purpose of the kernel.

## Recommendation
**Scope D (Canonical Proposition Subject)**, but it requires a **ClaimDescriptor** (a revision to Claim Model B) so the kernel can enforce canonicalization on symmetric claims automatically.
