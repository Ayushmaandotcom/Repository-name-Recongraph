# Reference Evidence Model

## Status

Experimental architecture note. No production implementation is implied by this document.

## Problem

A scalar reference score collapses multiple distinct questions into one value:

1. Do the normalized references match exactly?
2. Which numeric tokens are shared?
3. How discriminative are those shared tokens in the ledger?
4. Are the surrounding reference namespaces compatible?
5. Why did the final reference evidence receive its strength?

Example A — Genuine rare shared identifier
```
INV-874219
AB/874219
```
Current: 0.8
Desired decomposition:
- exact normalized identity: false
- shared tokens: 874219
- token df: 2
- collision burden: 1
- namespace compatibility: unknown

Example B — Common collision
```
INV-001
ABC-001
```
Current: 0.8
Desired decomposition:
- exact normalized identity: false
- shared tokens: 001
- token df: 4
- collision burden: 3
- namespace compatibility: unknown

Example C — Rare but contextually ambiguous
```
INV-2026-1001
ABC-2026-1001
```
Current: 0.8
Desired decomposition:
- exact normalized identity: false
- shared tokens:
  2026:
    df: 40
  1001:
    df: ?
- namespace compatibility: unknown

Why is a single scalar insufficient as the intermediate representation?
A single scalar permanently deletes the provenance of the evidence. If the scoring engine just receives `0.8`, it cannot know if this was a rare shared identifier (strong genuine evidence) or a structurally long but commonly repeated token like "999999" (weak collision). By collapsing these facts into one scalar early in the pipeline, every subsequent semantic or decision layer is robbed of the ability to reason about *why* the references match, making nuanced semantic rules or namespace compatibility checks impossible.

## Similarity vs Identity Evidence
Is `reference_similarity()` actually the correct abstraction?
Probably not. We are not measuring string similarity. `INV-874219` and `AB/874219` are textually dissimilar but share a highly discriminative identity-bearing structure. Conversely, `INVOICE-2026` and `INVOICE-2025` are highly textually similar (Levenshtein distance is tiny) but they represent distinct financial events. We are measuring *reference identity evidence*, not raw textual similarity.

## Candidate Data Model

```python
@dataclass(frozen=True)
class SharedReferenceToken:
    token: str
    document_frequency: int

@dataclass(frozen=True)
class ReferenceIdentityEvidence:
    normalized_a: str
    normalized_b: str
    exact_match: bool
    shared_numeric_tokens: tuple[SharedReferenceToken, ...]
```

### Critique
**Q1: Should document_frequency live inside SharedReferenceToken?**
No. Putting corpus statistics directly inside the extraction layer tightly couples pure string manipulation (identity extraction) with database lookups (corpus statistics). It prevents testing extraction independently of the corpus and violates separation of concerns.

**Q2: Should ReferenceIdentityEvidence contain raw references?**
No. The caller (the scoring engine) already owns the source `PurchaseRecord` and `GSTRecord`. Duplicating `raw_a` and `raw_b` inside the evidence object just creates redundant payload and risks desync.

**Q3: Should exact match be `exact_match: bool` vs `MatchKind` enum?**
It should remain `exact_match: bool` (or a separate factual dimension). An enum implies mutual exclusivity, but a pair can easily have *both* an exact normalized match (`INV-001` and `INV-001`) *and* shared numeric tokens (`001`). Using an enum would force us to pick a "primary" match kind and hide the other facts.

**Q4: Should shared tokens be `tuple[str, ...]` vs evidence objects?**
They should be `tuple[str, ...]`. Identity extraction should purely report structural overlap (facts). A subsequent enrichment layer can pair those structural facts with corpus statistics (`ReferenceTokenStatistics`), and then produce an `EnrichedReferenceEvidence` object.

## Exact Identity Is Not Necessarily Unique Identity
Consider exact matches:
- 001 ↔ 001
- INV-001 ↔ INV-001
- 2026 ↔ 2026
- 874219 ↔ 874219

Should all four receive `1.0`?
No. An exact normalized match on "001" or "INV-001" is weak evidence if "INV-001" is used by 50 different vendors in the ledger. Exactness and uniqueness represent two perfectly orthogonal dimensions. A string can match exactly but still carry zero uniqueness (like "CREDITNOTE"). Thus, exact normalized identity is a structural fact (`true`), but its evidentiary strength must still be judged by its corpus uniqueness.

## Corpus Scope
Which scope should document frequency be calculated over?
Scope D (Per relationship source pair). By computing DF across only the sources involved in the relationship hypothesis (e.g., Purchase + GST), we ask: "How discriminative is this identifier among the records that could plausibly participate in this exact type of reconciliation?" This avoids diluting or polluting the statistics with namespaces from completely unrelated domains (like bank transactions).

## Temporal Scope and Double Counting
Should v0.1 reference corpus statistics use the full tenant relationship corpus or a temporal candidate window?
Full corpus. If reference informativeness is evaluated using a ±30 day candidate window, the DF effectively becomes a proxy for time (a common token might look rare if we zoom in enough). But we *already* have a dedicated temporal similarity signal. If both reference evidence and temporal evidence incorporate time, we are double-counting the temporal dimension. Reference informativeness should measure absolute identifier collision across the ledger.
