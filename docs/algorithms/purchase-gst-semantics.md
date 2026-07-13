# Purchase-to-GST Relationship Semantics

## Purpose

Explain why primitive compatibility signals are insufficient to identify
the same financial event and define relationship-specific evidence
patterns for Purchase ↔ GST reconciliation.

## Baseline limitation

The v0.1 baseline uses a weighted average of entity, reference, amount,
temporal, and tax-identity signals.

Weighted averaging is compensatory: strong signals can offset severe
disagreement in another signal.

Challenge Dataset v1 exposed cases where this behaviour conflicts with
financial-event identity.

## Design principle

Primitive signals measure evidence.

Relationship semantics interpret combinations of evidence.

Semantic findings identify evidence patterns but do not, by themselves,
define production match decisions.

## Semantic finding PG-001: Severe amount conflict

### Motivation

HN001 scored 0.6957 despite a 100% amount mismatch because entity,
reference, temporal, and tax-identity evidence remained strong.

### Evidence pattern

- amount score is 0.0
- reference evidence is strong
- tax identity agrees

### Interpretation

The records exhibit strong identity evidence while their monetary values
are fundamentally incompatible under the current 1:1 Purchase ↔ GST
hypothesis.

### Finding

`severe_amount_conflict`

### Open question

Should this finding apply a contradiction penalty, trigger a hard gate,
or route the pair to review?

## Semantic finding PG-002: Distinct event identity evidence

### Motivation

HN003 scored 0.7000 for separate monthly invoices because entity, amount,
and tax identity matched exactly.

### Evidence pattern

- entity evidence is strong
- amount evidence is strong
- tax identity agrees
- reference score is 0.0
- temporal score is 0.0

### Interpretation

The records appear to involve the same legal entity and transaction
shape, but reference and temporal evidence indicate distinct financial
events.

### Finding

`distinct_event_identity_evidence`

### Open question

Should this finding reduce compatibility or act as a non-compensatory
event-identity gate?

## Existing tax identity contradiction

The v0.1 policy already treats an explicit tax-identity mismatch as a
contradiction and applies a multiplicative penalty.

HN002 demonstrated that this mechanism suppresses a highly compatible
surface-level pair.

The semantic layer should expose this condition as:

`tax_identity_conflict`

The scoring consequence may initially remain in RelationshipPolicy.

## Out-of-scope findings

### Weak numeric reference collision

HN004 exposed a primitive reference-scoring issue. The semantic layer
should not repair incorrect primitive evidence.

### Group relationship required

HN005 exposed a relationship-cardinality limitation. Pair semantics
cannot prove a 1:N reconciliation hypothesis.

## Challenge traceability

| Finding | Challenge case | Failure category |
|---|---|---|
| severe_amount_conflict | HN001 | relationship semantics |
| tax_identity_conflict | HN002 | relationship semantics |
| distinct_event_identity_evidence | HN003 | relationship semantics |
| weak numeric reference collision | HN004 | primitive scoring |
| group relationship required | HN005 | relationship cardinality |

## Detection before consequence

Semantic findings are initially observational.

`analyze_purchase_gst_semantics()` detects evidence patterns and returns
structured findings without changing pair compatibility scores.

This separation allows the challenge dataset to validate semantic
detection independently from the later policy decision of whether a
finding should apply a penalty, trigger a gate, or route a pair to
review.

## Initial semantic thresholds

The v0.1 semantic detector uses:

- strong reference evidence: score >= 0.8
- strong entity evidence: score >= 0.9
- strong amount evidence: score >= 0.9

These thresholds are rule semantics, not calibrated probabilities.

The severe amount conflict currently requires an amount score exactly
equal to 0.0. This preserves the first challenge-derived rule without
introducing an untested near-zero threshold.

## Compatibility and eligibility

Compatibility and eligibility answer different questions.

Compatibility measures how strongly the available evidence aligns across
the weighted primitive signals.

Eligibility determines whether a relationship hypothesis is permitted to
proceed through an automatic reconciliation path.

A pair may have high compatibility while remaining ineligible for
automatic 1:1 reconciliation because a critical semantic finding
contradicts the 1:1 hypothesis.

For example, HN001 has high identity compatibility but contains a severe
amount conflict. Reducing the compatibility score until the pair appears
"dissimilar" would hide the actual evidence structure. The compatibility
score should preserve the observed alignment, while eligibility records
that the pair cannot automatically reconcile under the 1:1 hypothesis.

Ineligibility does not imply rejection. A later decision layer may route
an ineligible but otherwise compatible pair to review or evaluate it
under a different relationship hypothesis.

## Hypothesis-relative semantics

Semantic findings are interpreted relative to the relationship
hypothesis being evaluated.

A severe amount conflict is a blocking condition for a 1:1 Purchase ↔
GST hypothesis because one record is expected to reconcile directly
with one opposing record.

The same pair may remain useful as a candidate edge for a 1:N
reconciliation hypothesis. Under a group hypothesis, amount compatibility
must be evaluated across the combined records rather than independently
for each pair.

Therefore, ineligibility for the 1:1 hypothesis does not make a pair
globally irrelevant.

## Initial 1:1 blocking findings

The first Purchase ↔ GST 1:1 eligibility policy treats the following
semantic findings as blocking:

- `severe_amount_conflict`
- `tax_identity_conflict`
- `distinct_event_identity_evidence`

These findings prevent automatic 1:1 eligibility.

The blocking set is explicit rather than treating every semantic finding
as blocking. Future findings may be informational or review-oriented and
should not automatically make a pair ineligible.

## Decision layer boundary

Eligibility is not a final reconciliation decision.

The semantic and eligibility layers do not currently emit:

- auto-match
- review
- reject

A future decision layer may combine compatibility, coverage, eligibility,
and relationship hypotheses to select an operational action.

## 1:1 eligibility result

The Purchase ↔ GST semantic layer exposes a separate eligibility result
for the 1:1 reconciliation hypothesis.

The result contains:

- `status`: `eligible` or `ineligible`
- `blocking_findings`: the ordered semantic findings that prevent the
  1:1 hypothesis from proceeding through automatic reconciliation

Eligibility is intentionally independent from compatibility thresholds.

A low-compatibility pair may remain eligible if no critical semantic
finding blocks the 1:1 hypothesis. A later decision layer should reject
or ignore the pair based on compatibility.

A high-compatibility pair may be ineligible when a critical contradiction
blocks automatic 1:1 reconciliation.

This independence prevents eligibility from becoming a second hidden
score threshold.

## Current implementation boundary

The existing tax identity contradiction penalty remains part of the
compatibility scorer temporarily.

The intended direction is to evaluate whether the penalty should be
removed after eligibility behaviour is validated against challenge and
baseline datasets.

No compatibility scoring behaviour is changed in the initial eligibility
implementation.

## Compatibility and eligibility separation

1. Purchase ↔ GST compatibility measures weighted primitive evidence alignment.
2. A tax identity mismatch contributes 0.0 through the tax identity signal.
3. Purchase ↔ GST compatibility does not additionally apply a tax contradiction multiplier.
4. A tax identity conflict remains a blocking semantic finding for the automatic 1:1 hypothesis.
5. Therefore, a pair may have high compatibility and still be 1:1 ineligible.
6. Removing the Purchase ↔ GST tax penalty does not remove generic contradiction-penalty support from the relationship scoring engine.

### Tax penalty comparison experiment

Pairs compared: 31
Scores changed: 22
Eligibility changes: 0

Minimum positive score:
hybrid = 0.9457
pure   = 0.9457

Maximum negative score:
hybrid = 0.0779
pure   = 0.1557

Separation gap:
hybrid = 0.8679
pure   = 0.7900

**Decision**:
Purchase ↔ GST uses pure compatibility without a tax contradiction multiplier.

**Rationale**:
The tax mismatch already contributes zero weighted evidence and independently blocks 1:1 eligibility. The additional multiplicative penalty mixed domain eligibility semantics into the compatibility score and could suppress diagnostic visibility into flaws in other primitive signals.
