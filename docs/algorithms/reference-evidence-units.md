# Reference Evidence Units

**Purpose**: Define the atomic evidence units consumed by reference interpretation and determine whether the current corpus statistics are sufficient to combine multiple units safely.

## EU-001 — Exact normalized reference identity

The evidence unit is: **normalized full-reference identity**

**Example**:
`INV-874219` and `INV/874219` produces:
`normalized identity = inv874219`

The evidence unit is `inv874219`, NOT `inv874219` + `874219` as two equal independent identity units.
Because the numeric token is structurally contained within the exact full-reference identity, the full normalized identity is the primary evidence unit for the exact interpretation path.

**Status**: Proposed

## EU-002 — Shared numeric token identity

When `exact_normalized_match = False`, each unique shared numeric token is a **candidate evidence unit**.

**Example**:
`INV-2026-874219` and `AB-2026-874219`
candidate units: `2026` and `874219`

Important wording: *candidate evidence unit*, not *independent evidence unit*.

**Status**: Proposed

## Structural Distinctness Is Not Statistical Independence

For an example pair like:
`INV-2026-874219` and `AB-2026-874219`

Stage 1 correctly reports `("2026", "874219")`. They are structurally distinct tokens (`2026 != 874219`).

However, structural distinctness does not prove `P(2026 ∩ 874219) = P(2026)P(874219)` or any independence assumption.

Stage 1 deduplication protects against duplicate structural identity values (e.g., `INV-874219-874219`). It does not protect against correlated distinct identity values. Deduplication does nothing about the possibility that `2026` and `874219` are correlated in the corpus.

## Marginal Document Frequency Is Insufficient for Independence-Aware Combination

Consider two corpus environments for tokens `2026` and `874219`:
- **CO001**: `DF(2026) = 20`, `DF(874219) = 20`, `joint DF = 20` (Perfect co-occurrence)
- **CO002**: `DF(2026) = 20`, `DF(874219) = 20`, `joint DF = 0` (Zero overlap)

Both profiles expose `DF(2026) = 20`, `DF(874219) = 20`, and `N = 100`. But CO001 joint DF is 20 and CO002 joint DF is 0.

Therefore any function `combine(df_a, df_b, reference_count)` must produce the same output for CO001 and CO002, even though the observed corpus co-occurrence structure differs drastically.

**Conclusion**: Marginal document frequency alone is insufficient to support a statistically justified independence-aware multi-token combination rule.

## Architecture Directions for Multi-Token Evidence

### Direction A — Strongest-unit interpretation
For non-exact identity: `score = strongest individual shared-token evidence`
- **Benefits**: uses current marginal DF, avoids correlation double counting, simple explanation, bounded naturally.
- **Cost**: multiple genuinely independent identifiers provide no additional support.
- **Status**: Open

### Direction B — Conservative accumulation with a capped secondary bonus
Primary strongest token + small bounded support from additional informative tokens.
- **Benefits**: multiple evidence can matter, less aggressive than probabilistic union.
- **Cost**: bonus is policy-driven, not statistically independence-justified.
- **Status**: Open

### Direction C — Expand corpus statistics for co-occurrence-aware combination
Track some form of joint token document frequency.
- **Benefits**: can observe token dependence, supports richer multi-token interpretation.
- **Costs**: larger corpus profile, higher profiling complexity, sparse pair statistics, policy becomes mathematically more complex.
- **Status**: Open
