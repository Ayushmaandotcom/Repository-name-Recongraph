# Typed Payload Envelope Decision

## Summary
`TypedPayloadEnvelope` wraps `CanonicalPayloadEnvelope` to provide semantic type and version.

## TPE Questions
**TPE001 What exactly does CanonicalPayloadEnvelope guarantee?**
Deterministic JSON serialization. It does not guarantee domain semantics.

**TPE002 Does it identify semantic type?**
No.

**TPE005 Should payload type participate in assertion identity?**
Yes.

## Decision
Implement `TypedPayloadEnvelope(type_id, semantic_version, content)`.
Assertions take an optional `TypedPayloadEnvelope`.
