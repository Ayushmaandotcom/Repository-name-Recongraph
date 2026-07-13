# Reference Evidence Ordering Constraints

Before selecting an interpretation formula, ReconGraph defines qualitative ordering constraints that any valid reference evidence interpretation must satisfy. These constraints act as the invariants of the interpretation formula.

## RO-001 — Corpus rarity should increase discriminative evidence
`RE003 > RE004`
`RE005 > RE006`

All else equal, a shared identity token observed in fewer corpus documents should provide stronger positive evidence.

## RO-002 — Exact identity is not universally perfect evidence
`RE001 > RE012`

An exact normalized identity that is rare in the corpus should provide stronger evidence than an exact identity appearing in most corpus observations. This explicitly rejects the idea that an exact match should unconditionally result in `1.0`.

## RO-003 — Repeated generic exact identities should be discounted
`RE001 > RE002`
`RE011 > RE002`

Rare full-reference identity should be more discriminative than frequently repeated generic reference labels (e.g. `CREDITNOTE`).

## RO-004 — Token length may provide a prior, but cannot replace corpus evidence
Proposed ordering: `RE003 > RE005` (even though both have `DF = 2`)

A six-digit identifier may be more discriminative than a three-digit sequence due to a larger identifier space.

**Status**: hypothesis requiring explicit policy decision. The corpus already gives us empirical collision context, we need to decide whether length contributes independent information or double-counts rarity.

## RO-005 — Common evidence should be weak, not contradictory
Proposed: `RE008 ≈ RE003` (if 874219 is the dominant rare shared token and 2026 is extremely common).

The common token should contribute little or no additional positive evidence. It should not automatically negate the rare token.

**Status**: proposed.

## RO-006 — Multiple informative shared tokens should not reduce evidence
`RE007 >= RE003`

Assuming both tokens provide non-negative identity evidence. However, tokens like `2026` and `874219` may not be statistically independent, so naive addition may double count evidence.

## RO-007 — Missing corpus context must not be interpreted as rarity
`RE010 != "maximally rare"`

No profile statistics cannot imply maximal discriminativeness.

## RO-008 — Partial corpus context must remain observable
`RE009` must be distinguishable from fully profiled evidence and fully out-of-profile evidence.

This means Stage 3 may need more than a scalar to represent statistical coverage and interpretation.

## RO-009 — Non-numeric exact identities remain valid evidence
`RE011` must receive positive identity evidence despite having no numeric tokens.

## RO-010 — Interpretation must be deterministic and bounded
Any eventual scalar compatibility component must satisfy:
`0.0 <= score <= 1.0`

for the same evidence + profile + policy, and produce the same result deterministically without random calibration or corpus mutation.
