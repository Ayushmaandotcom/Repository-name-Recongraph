# Evidence Assertion Scope

This document defines the formal assertion scope model for the Evidence Semantic Kernel.

## Can evidence target...

**AS-001 ...a single record?**
Yes. Example: `document.reference_is_parseable`. 

**AS-002 ...a pair of records?**
Yes. Example: `identity.same_gst_registration` for P1 ↔ G1.

**AS-003 ...two groups of records?**
Yes. Example: `financial.amount_conservation` for {P1} ↔ {G1, G2}.

**AS-004 ...an entire hypothesis?**
Yes, but carefully. A hypothesis is a specific set of pairwise edges and nodes. Evidence targeting a hypothesis asserts a property about the *entire* proposed structure, e.g., `structure.contains_circular_reference`. 

**AS-005 ...a connected component?**
Yes, e.g., `component.has_unresolved_financial_imbalance`.

**AS-006 ...a decision?**
No. A decision is a policy output (e.g., `APPROVE`, `REJECT`), not an epistemic proposition. Evidence informs the hypothesis evaluation; the evaluation informs the decision.

**AS-007 Is assertion scope always binary?**
No. Single-record evidence is unary. Group evidence might be comparing sets.

**AS-008 Is left/right direction semantically meaningful?**
For symmetric claims (e.g., `identity.same_legal_entity`), no. For asymmetric claims (e.g., `temporal.strictly_before`), yes.

**AS-009 Can subject scope be represented as: `subjects: tuple[str, ...]`?**
No. A flat tuple destroys the structural boundary between "side A" and "side B". `{P1, P2} ↔ {G1}` is lost if flattened to `(P1, P2, G1)`.

**AS-010 Does the existing URN node system provide a usable identity foundation?**
Yes. The existing system uses URNs like `urn:recongraph:purchase:123` which provides stable, serializable node identities.

**AS-011 Can URNs identify aggregated groups?**
Currently no. We need a way to stably identify a group of nodes, perhaps by sorting and hashing their URNs, or maintaining an explicit `GroupRef`.

**AS-012 Should a hypothesis have a stable identity?**
Yes, likely a hash of its normalized, canonical node URN sets.

**AS-013 Can two structurally equal hypotheses have different runtime identities?**
Only if they are instantiated in memory with random UUIDs. A content-derived ID (canonical hash) prevents this.

**AS-014 What identity survives trace serialization?**
String-based URNs and deterministic content hashes. Python object IDs (`id(obj)`) do not.

**AS-015 Can evidence from scope P1 ↔ G1 be fused with evidence from P1 ↔ {G1, G2}?**
Not without an explicit **projection rule**. A pairwise lexical match does not automatically prove group-level lexical matching without defining how the group aggregate behaves (e.g., is the group valid if *any* pair matches, or if *all* pairs match?).

## Scope Taxonomy

| Scope Type | Example | Cardinality | Directional | Current Stable ID | Evidence Target Valid |
|---|---|---|---|---|---|
| RECORD | `document.is_readable` | Unary (1) | No | Node URN | Yes |
| RECORD_PAIR | `identity.same_gst_registration` | Binary (1:1) | Claim-dependent | Edge ID | Yes |
| GROUP_PAIR | `financial.conservation` | Binary (N:M) | Claim-dependent | None (Requires GroupRef) | Yes |
| HYPOTHESIS | `structure.is_valid_tree` | N-ary Set | No | None (Requires HypHash) | Yes |
| COMPONENT | `anomaly.orphan_node` | N-ary Set | No | None | Yes |
| DECISION | `policy.approved` | N/A | N/A | Trace UUID | **NO** (Policy, not Evidence) |

**Recommendation:** The minimum scope model required before Stage 8J must distinguish Left/Right sets (for N:M) while supporting Unary observations (where Right is empty).
