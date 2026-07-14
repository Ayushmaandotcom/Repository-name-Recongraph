# Kernel Identity Reference Decision

## Summary
To prevent structural forgery via duck typing (`hasattr(node, "digest")`), we introduce an explicit `KernelIdentityRef`. This provides a transport boundary for semantic identities.

## KIR Questions

**KIR001 What semantic capability is the derivation kernel actually requiring?**
It requires an explicitly certified, stable identity representing a node in the semantic graph.

**KIR002 Is `.digest` itself sufficient?**
No, a bare digest string loses its semantic domain (e.g. observation vs derived artifact).

**KIR003 Why is hasattr-based identity discovery unsafe?**
It tests structural shape, not semantic capability. Any object with a `.digest` attribute can forge its way into the graph.

**KIR004 Should the kernel consume concrete identity classes?**
No. Consuming concrete classes creates tight coupling and inhibits plugin extensibility.

**KIR005 Would a Union of all identity types scale to plugins?**
No, a closed Union requires central registration, which breaks independent plugin distribution.

**KIR006 Does Protocol structural typing permit accidental semantic admission?**
Yes. A class might implement `.digest` for entirely different reasons (e.g. logging) and be accidentally admitted as an identity node.

**KIR007 Is KernelIdentityRef an owning identity?**
No, it is a transport reference explicitly exported by an owning identity.

**KIR008 Can KernelIdentityRef replace ObservationIdentity?**
No, the domain-specific identity maintains context.

**KIR009 Can it replace DerivedArtifactIdentity?**
No.

**KIR010 Can two identity domains carry identical digest bytes?**
Yes, theoretically, though domain separation null-bytes mitigate this.

**KIR011 If yes, are the refs equal?**
No, `KernelIdentityRef` equality requires the domain and schema to match.

**KIR012 Must identity domain participate in equality?**
Yes.

**KIR013 Must schema participate in equality?**
Yes.

**KIR014 Does digest algorithm participate in identity?**
Yes.

**KIR015 Is sha256 encoded in IdentityDigest or separately?**
Encoded within `IdentityDigest` (e.g. `sha256:...`).

**KIR016 Can plugin identity domains exist?**
Yes.

**KIR017 Can unknown identity domains be transported?**
Yes.

**KIR018 Does unknown mean trusted?**
No. Transportability does not imply trust.

**KIR019 Does transportability imply fusion eligibility?**
No. Stage 8J governs eligibility.

**KIR020 How does an identity object export its ref?**
Via a `.to_kernel_identity_ref()` method.

**KIR021 Does export alter identity?**
No.

**KIR022 Does ref serialization use canonical JSON?**
Yes.

**KIR023 Can DerivationInputBinding accept raw objects?**
No, only `KernelIdentityRef`.

**KIR024 Migration impact on K3/K4/K5?**
Minimal. Identity classes export the reference, and `DerivationIdentity` consumes it.

**KIR025 Final decision.**
Adopt `KernelIdentityRef` constructed from validated value objects (`IdentityDomainId`, `IdentitySchemaId`, `IdentityDigest`).
