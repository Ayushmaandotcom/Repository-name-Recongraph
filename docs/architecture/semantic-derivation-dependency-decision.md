# Semantic Derivation Dependency Decision

## Summary
Derivations depend on semantic contexts (models, configs, registries). `SemanticDependencyRef` is introduced as a context modifier for derivations, separate from derivation inputs.

## SDD Questions

**SDD001 Are dependencies DAG nodes?**
No, they are context modifiers.

**SDD002 Do dependencies have kind?**
Yes, `SemanticDependencyKind`.

**SDD003 Can they be mutable?**
Yes. A dependency can be `MUTABLE_REFERENCE` (e.g. "latest").

**SDD004 Does mutability affect execution?**
No, but it prevents global caching and cross-run reproducibility.

**SDD005 Do roles participate in dependency identity?**
Yes.

**SDD006 Are duplicate identical dependencies allowed?**
No, they are explicitly rejected. Validate, don't repair.

**SDD007 Does dependency identity participate in derivation identity?**
Yes.
