# Evidence Derivation Identity

This document defines Derivation Identity—how an assertion remembers *who* and *how* it was derived from an observation.

## Identity Questions

**DI-001 Does `provider_id` identify the derivation algorithm?**
No, it identifies the module.

**DI-002 Does `engine_version` identify it?**
It's too broad. The core engine can update while the provider logic remains identical.

**DI-003 Can one provider change behavior without engine version changing?**
Yes, if it's a plugin on an independent release cycle.

**DI-004 Does config hash identify algorithm semantics?**
It identifies threshold and policy inputs, but not the Python code itself.

**DI-005 Does payload schema version identify interpretation semantics?**
No. A provider could rewrite its NLP algorithm entirely without changing the output schema.

**DI-006 What exact metadata is needed to answer: "Why did this historical assertion exist?"**
1. What was the observation? (`ObservationID`)
2. What was the configuration? (`PolicyHash`)
3. What was the algorithm? (`ProviderSemanticVersion`)

**DI-007 Should assertions carry: `provider_id`, `provider_version`, `interpreter_id`, `interpreter_version`, `policy_hash`. Are all necessary?**
`interpreter_id` and `interpreter_version` are largely synonymous with `provider` in this architecture. 

**DI-008 What is redundant?**
`interpreter` vs `provider`. We only need `ProviderIdentity` (name) and `ProviderSemanticVersion` (version).

**DI-009 Can provider version be semantic rather than package version?**
Yes. It should be bumped when the epistemic logic changes.

**DI-010 Should a provider version change when thresholds change?**
No, thresholds are configuration.

**DI-011 Should policy hash capture threshold changes instead?**
Yes.

**DI-012 What happens if code changes but provider version is not incremented?**
The trace lies. Two traces with identical derivation metadata will contain different assertion outputs.

**DI-013 Can tests detect this?**
Yes, by hashing the AST of the provider's inference module and failing if it changes without a version bump.

**DI-014 Should trace replay guarantee:**
**A.** Explain historical output (Explainability)
**B.** Run exact old algorithm (Re-execution)
**C.** Run current logic against old inputs (Counterfactual)

ReconGraph v0.1 must guarantee **A** (via serialized assertions) and **C** (via serialized raw observations). **B** is practically impossible in Python without persisting exact environment states (Docker images per trace).

## Reproducibility Contract for ReconGraph v0.1
The trace explicitly guarantees **Historical Explanation** (by serializing the output Assertion with its `ProviderSemanticVersion` and `PolicyHash`) and **Counterfactual Re-evaluation** (by serializing the raw inputs). It explicitly **abandons** exact Re-execution, meaning we do not try to dynamically load old Python code.

Therefore, `DerivationMetadata` strictly needs:
* `provider_id`: str
* `provider_semantic_version`: str
* `policy_hash`: str
