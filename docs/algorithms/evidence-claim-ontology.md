# Evidence Claim Ontology

This document evaluates whether ReconGraph requires formal Evidence Claims, how they should be structured, and what semantics they carry.

## Answers to Fundamental Questions

**CO-001 Is an enum sufficient?**
No. Enums are closed. A plugin architecture needs an extensible namespace where third-party developers can assert new claims (e.g. `CUSTOM_BANK_ACCOUNT_MATCH`) without modifying the core enum.

**CO-002 Are claims merely labels?**
No. They define the semantic target for fusion. If two providers emit evidence for `SAME_LEGAL_ENTITY`, the fusion engine knows they are corroborating or contradicting the *exact same fact*.

**CO-003 Can claims have logical relationships?**
Yes. `SAME_LEGAL_ENTITY` logically necessitates `SAME_CORPORATE_FAMILY`. But `SAME_CORPORATE_FAMILY` does not necessitate `SAME_LEGAL_ENTITY`. Contradicting the family implies contradicting the entity.

**CO-004 Should support and contradiction target the same proposition?**
Yes. `DIFFERENT_LEGAL_ENTITY` is just strong conflict against the claim `SAME_LEGAL_ENTITY`. Introducing negative claims creates an uncontrolled explosion of variables where `conflict(SAME_LEGAL_ENTITY)` and `support(DIFFERENT_LEGAL_ENTITY)` have to be synchronized.

**CO-005 Should ReconGraph represent negative claims explicitly?**
No, per above. Conflict against a positive claim is semantically sufficient and mathematically cleaner.

**CO-006 Can absence of support for a claim be treated as support for its negation?**
Absolutely not. "I have no proof they are the same" is entirely distinct from "I have proof they are different".

**CO-007 Can one observation bear evidence on multiple claims?**
Yes. `ABC LLP` vs `ABC PVT LTD` provides lexical support for `SAME_ORGANIZATIONAL_CORE` but absolute contradiction for `SAME_LEGAL_ENTITY`. 

**CO-008 Can claims be hierarchical?**
Yes, conceptually. However, logical entailment (if A is true, B is true) is mathematically complex for fusion engines unless strictly formalized.

**CO-009 Should claim semantics live in code or documentation?**
The *name* and *namespace* live in code. The *logical rules* between claims should be encoded in a registry if Stage 8J is expected to fuse hierarchically.

**CO-010 What happens when a future plugin introduces `SAME_BANK_ACCOUNT_OWNER`?**
If claims are a flat enum, the core code breaks. If claims are a registry/value-object, the plugin registers it, and the fusion engine dynamically binds providers targeting that claim.

## Candidate Designs

### Claim Model A — Flat Enum
* Simple `Enum`.
* Fails extensibility and hierarchy.

### Claim Model B — Typed Claim Identifier
* `identity.same_legal_entity`, `financial.conservation`
* String-backed value object. Extensible, typed, serializable.

### Claim Model C — Formal Claim Registry
* Claims register logical relationships (`entails`, `excludes`).
* Perfect for Stage 8J, but massive over-engineering for Stage 8C.

## Recommendation for v0.1
**Claim Model B — Typed Claim Identifier.** 
We need a formal, extensible target for evidence assertions. A string-backed typed identifier (e.g., `Claim("identity.legal_entity")`) prevents enum-locking while forcing providers to explicitly name what they are proving.
