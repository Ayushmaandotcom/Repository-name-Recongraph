# Explanation Layer Epistemic Bug: The Missingness Default

## State Trace

1. **Vendor Name Missing:** Record is ingested without a vendor name.
2. **Provider Output:** `VendorEvidenceProvider` returns `None` (or empty list of contributions) because it cannot compute a match.
3. **Evaluated Hypothesis:** The hypothesis object contains no vendor evidence contributions.
4. **Decision:** The decision engine does not see a vendor penalty. It operates purely on the available evidence (e.g. Reference matches, amounts).
5. **Explanation Builder:** `EvidenceSummary.from_hypothesis()` is called. It attempts to populate `entity_score`. Because there is no vendor contribution, it defaults to `0.0`.
6. **Evidence Summary:** `entity_score = 0.0`.

## Analysis

1. **At which exact boundary is absence converted to zero?**
   In `EvidenceSummary.from_hypothesis()` (or equivalent DTO builder) where `entity_score` falls back to `0.0` if no entity contribution is found.
2. **Is zero interpreted anywhere as contradiction?**
   Yes. In the core scalar logic (and to any human reading the report), `0.0` means "100% contradiction / definitely different".
3. **Does the Decision Engine see this zero?**
   No. The Decision Engine sees the *absence* of evidence. The engine correctly doesn't penalize.
4. **Does only the explanation layer see it?**
   Yes. The bug is in the projection from the rich graph back to the flat scalar summary.
5. **Can traces distinguish missing from observed zero?**
   The internal graph trace can (by the absence of a `SignalName.ENTITY` node). The flat `DecisionTrace` JSON export usually relies on the `EvidenceSummary`, so it *loses* the distinction.
6. **Can benchmark reports distinguish them?**
   No. Benchmarks reading the `entity_score` see `0.0` and cannot tell if it was missing or contradictory.
7. **Can synthetic ground truth express missing vendor evidence?**
   Currently, the synthetic generator always populates a vendor name unless explicitly omitted, but the framework's evaluation layer doesn't test for "absence" specifically.
8. **Are human review packets receiving misleading information?**
   **YES.** A human reviewer sees "Vendor Score: 0.0" and assumes the engine found conflicting names, when in reality one document simply lacked a name field. This destroys trust.
