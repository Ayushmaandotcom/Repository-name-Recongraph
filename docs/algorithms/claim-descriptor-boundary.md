# Claim Descriptor Boundary

This document challenges the previously recommended "Identifier Only" Claim Model B.

## Properties of Claims
**CI-001 Does a claim identifier need metadata?**
Yes. Without metadata, the kernel cannot know if the claim is symmetric (for canonicalization) or what scopes it applies to.

**CI-002 Can metadata be provider-owned?**
No. Two providers emitting the same claim must agree on its symmetry and scope cardinality. The claim owns its semantics.

**CI-003 If two plugins independently use `identity.same_legal_entity` but define different symmetry semantics, what happens?**
Catastrophic failure in Stage 8J. One canonicalizes `B↔A` to `A↔B`, the other treats them as distinct directional assertions.

**CI-004 Who owns canonical claim semantics?**
The Claim Descriptor itself.

**CI-005 Does a global claim registry violate plugin extensibility?**
A *static, hardcoded* registry does. A *dynamic* registry (where plugins register new ClaimDescriptors on boot) does not. However, we can avoid global state entirely by passing the `ClaimDescriptor` value object inside the assertion.

**CI-006 Can core claims be registered while plugins define namespaced extension claims?**
Yes.

**CI-007 Can unknown claims remain traceable but non-fusible?**
Yes. If a trace contains a serialized `ClaimDescriptor` with a `claim_id` that Stage 8J doesn't recognize, Stage 8J can log it, skip fusing it, and preserve it in the output trace.

**CI-008 Should Stage 8J refuse to combine assertions for unknown claim semantics?**
Absolutely. Fusing unknown claims is semantically blind.

**CI-009 Should claim schema version be separate from payload schema version?**
Yes. The proposition's semantics (Claim version) are independent of the data structures used to prove it (Payload version).

**CI-010 Can the semantics of `identity.same_legal_entity` change in place?**
No. If v2 defines it as strictly "PAN equality" and v1 defined it as "PAN or Name equality", historical assertions lose their meaning. It must become `identity.same_legal_entity_v2`.

## Evaluation
* **Claim B1 (Identifier Only):** Fails to handle symmetry canonicalization safely.
* **Claim B2 (Assertion-Local Metadata):** Creates split-brain where different assertions define the same claim differently.
* **Claim B3 (Identifier + ClaimDescriptor):** A frozen value object defining the proposition's invariant rules (symmetry, allowed scopes, version).

## Recommendation
**Claim B3 (Identifier + ClaimDescriptor).** 

```python
@dataclass(frozen=True)
class ClaimDescriptor:
    claim_id: str
    semantic_version: int
    is_symmetric: bool
    allowed_scope_types: frozenset[ScopeType]
```
**Can unknown plugin claims be recorded, serialized, explained, and traced even if the core cannot fuse them?**
Yes. The `ClaimDescriptor` contains all necessary structural metadata (`is_symmetric`) for the trace reader and the graph engine to handle the assertion mechanically, even if Stage 8J lacks the domain knowledge to fuse that specific `claim_id`.
