# ADR-001: Separate Reference Identity Extraction, Corpus Profiling, and Evidence Interpretation

## Status

Accepted

## Date

2026-07-13

## Context

Currently, reference evidence processing is collapsed into a single pipeline flow:

```
PurchaseRecord
      +
GSTRecord
      ↓
score_purchase_to_gst()
      ↓
reference_score()
      ↓
float | None
      ↓
RelationshipPolicy
```

Conceptually, `reference_score()` does the following in one monolithic step:
1. Returns `None` if either input is missing.
2. Returns `1.0` unconditionally if the normalized references match exactly.
3. Returns `0.8` if they share a qualifying numeric token (length >= 3 and not a year-like token).
4. Returns `0.0` otherwise.

This single scalar output fundamentally deletes the provenance of the evidence, making it impossible for the engine to apply contextual intelligence. We have observed the following specific failures resulting from this architecture:

| Case | References | Current | Observed Problem |
|---|---|---|---|
| HN004 | OMD-001 ↔ NSS-001 | 0.8 | generic numeric collision |
| COR001 | INV-001 ↔ ABC-001 | 0.8 | corpus-common token treated as strong |
| COR005 | INV-999999 ↔ ABC-999999 | 0.8 | repeated token treated as strong |
| COR016 | INV-2026-1001 ↔ ABC-2026-1001 | 0.8 | rare token rewarded without namespace context (namespace compatibility is unknown) |
| EX003 | 2026 ↔ 2026 | 1.0 | exactness bypasses uniqueness |
| EX008 | CREDITNOTE ↔ CREDITNOTE | 1.0 | non-numeric generic reference bypasses token profiling |

## Decision Drivers

1. **Evidence provenance must survive until interpretation**: We cannot crush rich factual context (like token counts or exactness flags) into a raw float prematurely. The interpretation layer needs the full factual story to make intelligent semantic decisions.
2. **Pure extraction must remain corpus-independent**: The mechanical process of identifying structural string overlap should not require knowing the global database state. String extraction and statistical lookup are distinct concerns.
3. **Corpus facts must be reproducible and explainable**: An analyst must be able to audit the system and trace exactly *why* a reference received a specific score based on deterministic, queryable facts (like `df=2`) rather than hidden internal math.
4. **Interpretation models must be replaceable**: Because extraction and enrichment are separated as factual steps, we can easily swap out the mathematical interpretation (e.g., collision burden vs. normalized IDF) without rewriting the data pipelines.
5. **RelationshipPolicy should continue consuming scalar signals in v0.1**: We will preserve backwards compatibility with the existing generic reconciliation engine by ultimately outputting a `float | None`. We are evolving the plumbing inside the reference module, not tearing down the entire house.
6. **Reference evidence must not double-count temporal evidence**: Using time-windowed corpus scopes for references risks rewarding temporal proximity twice (once in the time signal, once in reference rarity). Reference informativeness should strictly measure collision rates globally across the source datasets.
7. **The architecture must support future namespace context without requiring it today**: We know namespace compatibility (like `INV` vs `ABC`) is a problem, and preserving provenance now guarantees we will have the structural facts needed to implement namespace evaluation in the future.

## Decision

ReconGraph will separate reference processing into three distinct stages: identity extraction, corpus enrichment, and evidence interpretation.

### Stage 1 — Identity extraction
**Input:** `reference_a`, `reference_b`
**Output conceptually:** `ReferenceIdentityEvidence`

**Responsibilities:**
- preserve normalized references
- record normalized exact identity
- extract shared numeric tokens
- report structural facts only

**Must not:** query corpus statistics, calculate document frequency, decide whether a token is strong or weak, apply relationship-specific rules, or return the final reference scalar.

*Corpus-independent and deterministic.*

### Stage 2 — Corpus enrichment
**Input:** `ReferenceIdentityEvidence`, `ReferenceCorpusProfile`
**Output conceptually:** `EnrichedReferenceEvidence`

**Responsibilities:**
- attach full normalized-reference frequency
- attach statistics for shared numeric tokens
- preserve the original identity evidence
- expose factual collision context

**Must not:** decide whether evidence is sufficient for matching, calculate pair compatibility, apply purchase↔GST semantics, or return AUTO_MATCH, REVIEW, or REJECT.

*Contextual but non-decisional.*

### Stage 3 — Evidence interpretation
**Input:** `EnrichedReferenceEvidence`, `ReferenceEvidencePolicy`
**Output:** `float | None`

**Responsibilities:**
- interpret exactness and corpus uniqueness together
- convert enriched facts into scalar reference compatibility
- preserve explainability through a result object if necessary
- remain separate from whole-pair relationship semantics

**Must not:** inspect amount evidence, inspect temporal evidence, inspect tax identity, make pair eligibility decisions, or make final reconciliation decisions.

*Interpret reference evidence only.*

## Proposed Data Model

The following types enforce the boundaries designed above.

### `ReferenceIdentityEvidence`
```python
@dataclass(frozen=True)
class ReferenceIdentityEvidence:
    normalized_a: str
    normalized_b: str
    exact_normalized_match: bool
    shared_numeric_tokens: tuple[str, ...]
```
*Note: Renamed from `exact_match` to `exact_normalized_match`. This is a necessary and precise correction. `INV-001` and `INV001` are not exact raw string matches, but they are exact matches under normalization. The variable name must preserve this distinction.*

### `ReferenceCorpusProfile`
```python
@dataclass(frozen=True)
class ReferenceCorpusProfile:
    reference_count: int
    normalized_reference_frequency: Mapping[str, int]
    numeric_token_document_frequency: Mapping[str, int]
```
*Note: Separating full normalized reference frequency from numeric token frequency is critical for solving EX008. It allows us to mathematically prove that an exact alphabetic match like "CREDITNOTE" is extremely common and carries no unique identity weight.*

### `ReferenceTokenStatistics` & `NormalizedReferenceStatistics`
```python
@dataclass(frozen=True)
class ReferenceTokenStatistics:
    token: str
    document_frequency: int

@dataclass(frozen=True)
class NormalizedReferenceStatistics:
    normalized_reference: str
    document_frequency: int
```
*Note: We store pure factual document frequencies here. Derived concepts like collision burden or document rates are excluded because they are interpretation artifacts derivable at runtime.*

### `EnrichedReferenceEvidence`
```python
@dataclass(frozen=True)
class EnrichedReferenceEvidence:
    identity: ReferenceIdentityEvidence
    normalized_reference_statistics: tuple[NormalizedReferenceStatistics, ...]
    shared_token_statistics: tuple[ReferenceTokenStatistics, ...]
```
*Note: This specific design uses a tuple for `normalized_reference_statistics` rather than a mapping. It elegantly models a collection of unique normalized references alongside a collection of unique shared tokens. It perfectly preserves the factual statistics required without enforcing redundant data structures or dict mappings on objects that at most have two items.*

## Implementation Refinement

During implementation of Stage 2 (Corpus Enrichment), the original data model proposal for `EnrichedReferenceEvidence` was refined.

The initial proposal attached known statistics directly (`ReferenceTokenStatistics`, `NormalizedReferenceStatistics`). However, implementation analysis identified a distinct out-of-profile state where identity evidence exists in the candidate pair, but the supplied corpus profile contains no statistic for that identity or token (e.g., the token is genuinely absent from the profile snapshot).

To preserve this factual state without inventing statistics, the wrapper classes (`NormalizedReferenceEvidence`, `SharedNumericTokenEvidence`) were introduced. They contain the identifier and an optional statistics field:

```python
@dataclass(frozen=True)
class SharedNumericTokenEvidence:
    token: str
    statistics: ReferenceTokenStatistics | None
```

Profile absence is preserved as unavailable context, not converted into synthetic rarity. We explicitly do not use `frequency = 0` for absent statistics, nor do we impute `document_frequency = 1` for unseen tokens. The interpretation layer (Stage 3) will handle the semantics of unavailable statistics.
