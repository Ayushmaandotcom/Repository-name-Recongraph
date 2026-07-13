# Reference Evidence Interpretation Contract

**Purpose**: Define the semantic output contract of reference evidence interpretation before selecting a scoring formula or calibration policy.

The reference pipeline stages have precise epistemic boundaries:
- **Stage 1 answers**: What identity facts are structurally shared?
- **Stage 2 answers**: What corpus statistics are available for those facts?
- **Stage 3 answers**: How should those enriched facts be interpreted as positive reference compatibility evidence, and how complete is the statistical context supporting that interpretation?

Stage 3 has two distinct epistemic dimensions: **evidence magnitude** and **statistical context completeness**. They must not be collapsed.

## Why `float | None` Is Insufficient

Using a monolithic `float | None` destroys critical semantic context.

For example, a `score = 0.5` could mean:
- **Known mediocre evidence** (e.g., RE004: two references sharing a highly common token with `DF = 40`).
- **Structurally plausible evidence interpreted under missing corpus context** (e.g., RE009: a shared token exists and is rare, but one of the exact normalized references was not seen in the profile).

These two states are not semantically equivalent. One is a factual assertion of weakness; the other is an assertion of partial ignorance.

Likewise, `None` is highly ambiguous. It could mean:
- **No usable reference evidence** (e.g., completely blank fields).
- **Reference evidence exists but corpus statistics are unavailable** (e.g., RE010: a structurally strong 6-digit match where the profile snapshot lacks any data for those records).

Stage 3 must reject `float | None` as its production contract.

## Conceptual Result Dimensions

The conceptual result of Stage 3 will be an interpreted object (e.g., `ReferenceEvidenceInterpretation`) with three dimensions:

### 1. `score`
`score ∈ [0.0, 1.0]`

**Meaning**: The interpreted magnitude of positive compatibility evidence contributed by the reference field.
It represents *positive compatibility evidence*.
- A common token should usually contribute approximately zero positive evidence; it does not automatically become negative evidence.
- No shared identity produces zero reference compatibility evidence.
- A score of `0.0` does **not** mean REJECT. It simply means the reference field contributed no positive compatibility evidence. (Final relationship decisions belong to a later layer).

### 2. `statistical_coverage`
`statistical_coverage ∈ [0.0, 1.0]`

**Meaning**: The fraction of interpretation-relevant identity evidence for which corpus statistics were available.
(Note: we distinguish structural profile completeness from interpretation statistical coverage. We care about the latter).

### 3. `contributions`
Conceptually, Stage 3 preserves the interpreted components that produced the score, keeping the score fully explainable.

Conceptual fields:
- `evidence_kind` (e.g., `normalized_reference` or `numeric_token`)
- `identity_value`
- `positive_evidence`
- `statistics_available`

**Key invariant**: The final Stage 3 score must remain explainable through its contributions. However, it is explicitly *not* required that `sum(contributions) == score`. If future interpreters use `max`, `probabilistic union`, saturation, or correlation-aware combinations, individual contribution magnitudes may not add linearly.

## Four Interpretation States

### State A — No usable reference evidence
**Example**: `reference_a = None`, `reference_b = None`
**Meaning**: No structural identity evidence exists to interpret.
**Proposed Boundary**: Stage 3 itself should *not* receive `None`. The pipeline remains strict. Stage 1 extraction returns `None` which bypasses Stage 2 and Stage 3 entirely. The interpreter requires a valid `EnrichedReferenceEvidence` object.

### State B — Fully profiled evidence
**Example**: RE003, RE004, RE005, RE006
**Meaning**: All interpretation-relevant corpus statistics exist. Expected `statistical_coverage = 1.0`.

### State C — Partially profiled evidence
**Example**: RE009
**Meaning**: The candidate pair is only partially profiled structurally. However, if the interpretation path only relies on the shared numeric token evidence (which is fully profiled), then the *interpretation statistical coverage* might still be 1.0. This distinguishes structural profile completeness from statistical coverage of consumed evidence.

### State D — Fully out-of-profile structural evidence
**Example**: RE010
**Meaning**: The shared token exists structurally, but its DF is completely unavailable.
Stage 3 must not pretend `DF = 0` or `DF = 1`. It must interpret under unavailable statistical context.
**Conceptually**: `score` may be non-zero (structural fallback), `statistical_coverage = 0.0`, and `contribution statistics_available = false`.

## Contract Invariants

### IC-001 — Coverage denominator follows consumed evidence
**Status**: Proposed
Statistical coverage should measure availability of corpus context for evidence actually consumed by the interpretation path, rather than mechanically counting every enriched statistic wrapper.

### IC-002 — Bounded score
`0.0 <= score <= 1.0`

### IC-003 — Bounded statistical coverage
`0.0 <= statistical_coverage <= 1.0`

### IC-004 — No evidence fabrication
Unavailable corpus statistics must remain unavailable through interpretation provenance. A structural token absent from the profile must not be explained as `DF = 0` or `DF = 1`.

### IC-005 — Zero score is not relationship rejection
A zero reference evidence score only means the reference dimension contributed no positive compatibility evidence.

### IC-006 — Coverage is not score
These must remain independent.
- Low score, high coverage (RE006-like known common token)
- Non-zero score, zero coverage (RE010-like structural fallback)
Multiplying score by statistical coverage would violate this invariant by forcing all out-of-profile structural evidence to zero.

### IC-007 — Contributions preserve provenance
Every interpreted positive evidence source must remain attributable to structural evidence produced by Stage 1. Stage 3 cannot invent tokens if Stage 1 never reported them.

### IC-008 — Interpretation is deterministic
The same enriched evidence + interpretation policy must produce the same result.

### IC-009 — Interpretation does not mutate evidence or profile state
The interpretation step operates on read-only evidence and profiles.

### IC-010 — Interpretation is not final reconciliation
Reference interpretation cannot emit `AUTO_MATCH`, `REVIEW`, `REJECT`, or `INELIGIBLE`. Those belong to later relationship semantics/decision layers.
