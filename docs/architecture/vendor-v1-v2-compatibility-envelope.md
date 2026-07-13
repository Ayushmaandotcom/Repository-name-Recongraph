# V1/V2 Compatibility Envelope

## Answers to Q1-Q10

**Q1. Which exact V1 consumers require a scalar vendor score?**
Benchmarks relying on `EvidenceSummary.entity_score`, human review UIs that expect a `float`, and potentially legacy semantic rules (`score_purchase_to_gst`).

**Q2. Can structured metadata survive through without lossy conversion?**
Yes, if attached to the `EvidenceContribution.metadata` dictionary, but it requires every downstream consumer to know the schema.

**Q3. Is metadata typed?**
No, currently `metadata` is a `dict[str, Any]`.

**Q4. If metadata is `dict[str, Any]`, are we simply recreating an unvalidated semantic dumping ground?**
Yes. Passing latent identity variables inside an untyped dictionary is a massive regression in safety.

**Q5. Would a dedicated payload protocol be safer?**
Yes. A strongly typed `VendorIdentityPayload(BaseModel)` ensures schema validation at the provider boundary.

**Q6. Could Stage 8J reliably inspect arbitrary metadata?**
No. It would require defensive `isinstance` checks and default fallbacks everywhere, leading to silent fusion failures.

**Q7. How would schema evolution work?**
In an untyped dict, it wouldn't. We would get KeyError crashes in production. With a typed payload, we can use `version` fields.

**Q8. Can serialized historical traces be replayed if Vendor payload V2 changes?**
Only if the deserializer maps the old schema version to a compatible state. A flat dict makes this impossible to track.

**Q9. Should evidence payloads carry a schema version?**
Yes, absolutely.

**Q10. Is the proposed scalar-plus-metadata bridge genuinely temporary, or likely to become permanent accidental architecture?**
It is highly likely to become permanent accidental architecture because the UI and benchmark runners will never be motivated to migrate off the scalar if the scalar is "good enough".

## Migration Designs

### Migration A: Scalar + Arbitrary Metadata
* **Description:** Keep returning `score: float`, dump detailed vendor facts into `metadata: dict`.
* **Breaking-change surface:** Zero.
* **Type Safety:** Zero.
* **Stage 8J Integration:** Horrible.
* **Long-term debt:** High. Becomes a permanent dumping ground.

### Migration B: Scalar + Typed Vendor Payload
* **Description:** `EvidenceContribution` gains a generic `payload: EvidencePayload | None` field. `VendorIdentityPayload` implements it. The scalar score remains populated for backwards compatibility.
* **Breaking-change surface:** Low (adds a field).
* **Type Safety:** High.
* **Stage 8J Integration:** Excellent.
* **Long-term debt:** Medium. The scalar is still calculated, risking split-brain bugs where the scalar and the payload drift.

### Migration C: Parallel V1/V2 Contribution Contracts
* **Description:** V1 returns `VendorScoreContribution`. V2 returns `LexicalIdentityContribution` and `LegalIdentityContribution`. The engine accepts both during the migration window, and a dedicated adapter projects V2 contributions down to a V1 scalar for the explanation layer ONLY.
* **Breaking-change surface:** Medium.
* **Type Safety:** Highest.
* **Stage 8J Integration:** Excellent.
* **Long-term debt:** Lowest. The V1 contract can be entirely deleted once the UI updates.

## Recommendation
**Migration C (Parallel V1/V2 Contracts).**
A scalar + metadata approach creates a split-brain architecture where the graph engine operates on metadata but the explanation layer operates on the scalar. Migration C forces the architectural seam exactly where it belongs: an explicit adapter that projects rich evidence down to a legacy scalar ONLY for downstream consumption, protecting the core engine's reasoning.
