# Reference Evidence Magnitude

**Purpose**: Define how a single reference identity evidence unit is mapped to bounded positive compatibility evidence without interpreting the result as a calibrated probability.

**Status**: Experimental Design

## Design Constraints

### MAG-001 — Bounded magnitude
`0.0 <= positive_evidence <= 1.0`

### MAG-002 — Not probability
The result does not represent `P(same financial event | reference evidence)`. It represents positive compatibility evidence contributed by one reference identity unit.

### MAG-003 — Deterministic
The same evidence unit, corpus statistics, and policy must produce the same magnitude.

### MAG-004 — Monotonic rarity
For the same corpus size and evidence type, lower observed frequency must not produce weaker positive evidence than higher observed frequency.
Conceptually: `frequency_a < frequency_b -> magnitude_a >= magnitude_b`

### MAG-005 — No arbitrary discontinuity without domain justification
We should avoid unexplained cliffs because they create massive evidence discontinuity from a one-document change.

### MAG-006 — Corpus-size awareness
Raw `DF = 10` does not mean the same thing in `N = 20` and `N = 1,000,000`. Magnitude interpretation must be corpus-size aware when corpus statistics exist.

### MAG-007 — Structural fallback remains explicit
When corpus statistics are unavailable, the interpreter may use a policy-defined structural fallback. That fallback must remain visible in contribution provenance as `statistics_available = False`. It must not pretend that `DF = 1`.

### MAG-008 — Exact identity and shared-token identity may use different policies
An exact normalized full-reference match is structurally different from sharing only a token. Do not force both through the same magnitude mapping merely for implementation convenience.

### MAG-009 — Token length is not uniqueness
A 10-digit token is not automatically rare. Observed corpus DF must override intuitive assumptions about length when statistics exist.

### MAG-010 — Structural token length may influence fallback only
**Status**: Proposed
For v0.1, token length is considered only when corpus statistics are unavailable.

### MAG-011 — Corpus replication invariance
**Status**: Proposed
If every corpus observation is replicated by the same factor, an observed identity's evidence magnitude should remain unchanged because its empirical frequency rate is unchanged.

## Structural Fallback Limitations

When corpus statistics are unavailable, token structure provides only weak priors about identity informativeness.
Length can distinguish `01` and `874219`, but cannot distinguish `874219` and `000000`.
Digit diversity can distinguish `874219` and `000000`, but gives superficially high diversity to `1` and `01`.
Therefore: No single structural feature currently justifies a probability-like interpretation of out-of-profile token evidence.

## v0.1 Fallback Principle
**Status**: Frozen

Structural fallback is heuristic, not empirical rarity. Token length selects a fallback band, and fallback magnitudes are monotonically non-decreasing. Equal fallback bands are valid.

v0.1 repetition detection means single-symbol repetition only. 
Examples: `000`, `111`, `999999`
Non-examples: `001`, `121212`, `123123`, `101010`, `000001`

Periodicity is deliberately excluded because ReconGraph currently has no corpus evidence proving periodic identifiers are less discriminative.
`repeated_pattern_discount` is multiplicative. A discount of `0.0` or `1.0` is valid. Structural fallback remains subject to the existing policy safety ceiling.

**Accepted Limitation**: A structurally repetitive token such as `121212` may receive the same unprofiled fallback magnitude as `874219` in v0.1. This is accepted because ReconGraph does not yet have empirical evidence supporting a broader complexity-based penalty. Corpus-profiled evidence remains the preferred path for measuring actual discriminativeness.

## Exact Full-Reference Identity Fallback
**Status**: Frozen

An exact normalized full-reference identity and a shared numeric-token identity are distinct evidence units. 
When corpus statistics are unavailable for an exact normalized match, it receives heuristic positive evidence defined by `exact_reference_fallback` (default `0.60`). 

- It represents heuristic structural evidence, NOT empirical rarity and NOT probability.
- It is bounded by the structural safety ceiling (`0.75`).
- It is orthogonal to numeric token fallback ordering and DOES NOT participate in the `short <= medium <= long` constraint.
- The numeric repeated-pattern discount DOES NOT apply to exact full-reference identity evidence (even if the normalized exact reference happens to be entirely numeric, like `000000`).

**Accepted Limitation**: Generic out-of-profile exact identities (e.g. `CREDITNOTE`) and structurally specific out-of-profile exact identities (e.g. `INV874219`) receive the same fallback magnitude in v0.1. We accept this because normalized-reference length, digit diversity, periodicity, or generic-string heuristics are not empirically validated measures of full-reference discriminativeness. The corpus profile remains the authoritative mechanism for reducing common exact identities when statistics are available.
