# Evidence Authority Descriptor Decision

## Summary
`AuthorityDescriptor` describes the epistemic basis on which an assertion asks fusion to interpret its evidentiary status. It is explicitly assigned by the provider and not inferred from ancestry.

## AD Questions
**AD001 Is authority globally ordered?** No.
**AD002 Is authority claim-relative?** Yes.
**AD013 Should authority contain a float?** No.
**AD014 Should authority contain priority?** No.
**AD015 Should authority contain override semantics?** No. These belong in Stage 8J fusion policy.

## Implementation
`AuthorityBasisId` is a typed identifier string (open vocabulary) to support plugins (e.g. `recongraph.authority.official_registry`). `AuthorityDescriptor` wraps this basis.
