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
**Status**: Proposed
Structural fallback should be conservative, bounded below fully profiled rare identity evidence, and explicitly marked as statistically uncovered.
