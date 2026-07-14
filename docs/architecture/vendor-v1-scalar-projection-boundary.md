# Vendor V1 Scalar Projection Boundary

While Stage 8C builds a rich, multi-factor semantic assertion kernel, the existing engine (Stage 8A/8B) still expects a single scalar float (e.g. `vendor_score`). 
Until Stage 8J (Semantic Fusion) is implemented, we must bridge the new assertions back to the legacy engine.

## The Compatibility Adapter

We deliberately use a name that screams its architectural compromise. 

**THIS IS A LOSSY COMPATIBILITY PROJECTION.**

```python
def project_vendor_evidence_to_legacy_scalar(
    interpretation: VendorIdentityInterpretation,
    policy: VendorV1ProjectionPolicy,
) -> float | None:
    ...
```

### What this adapter DISCARDS
This function reduces a multidimensional semantic object to a single float. By doing so, it permanently destroys:
1. **Assertion polarity**: A `CONFLICT` assertion must somehow be folded into a positive scalar or force a zero.
2. **Ancestry information**: The graph loses exactly which sources produced the evidence.
3. **Authority basis**: A 1.0 from a strict government registry looks identical to a 1.0 from fuzzy name matching.
4. **Factor-level granularity**: We lose the distinction between "they have the same PAN" and "they share the name BALAJI".

### Architectural Constraints
1. **Never authoritative**: This adapter is a lossy bridge. The true source of truth remains the `EvidenceAssertion` graph.
2. **Naming**: It must NEVER be called `vendor_score()` or `calculate_vendor_similarity()`. It is a projection.
3. **Deprecation**: This file and function are scheduled for deletion the moment Stage 8J is deployed.

### VendorV1ProjectionPolicy
The policy controls the projection rules:
- Which factors contribute to the score? (e.g., if tax identity supports, force score to 1.0).
- How do `CONFLICT` assertions reduce the scalar? (e.g., if legal forms conflict, cap maximum score at 0.5).
- What to return when no assertions are emitted? (Return `None` to indicate missingness, rather than `0.0` which implies conflict in the legacy engine).
