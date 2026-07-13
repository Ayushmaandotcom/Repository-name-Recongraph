# Cross-Scope Evidence Adversarial Matrix

This document proves that Stage 8J requires explicit projection rules to combine evidence across different graph scopes.

| Case ID | Claim | Assertion Scope A | Assertion Scope B | Shared Subjects | Can Combine Directly | Projection Required | Failure If Naively Combined |
|---|---|---|---|---|---|---|---|
| XS001 | `same_legal_entity` | P1 ↔ G1 | P1 ↔ G1 | P1, G1 | YES | NO | N/A (Standard fusion) |
| XS002 | `amount_conservation` | P1 ↔ G1 | P1 ↔ {G1, G2} | P1, G1 | NO | YES | Double counting P1↔G1 amounts while ignoring G2's contribution. |
| XS003 | `reference_match` | P1 ↔ G1 | P1 ↔ {G1, G2} | P1, G1 | NO | YES | A strong pair match might be a duplicate payment in the group context. |
| XS004 | `same_gst_registration` | P1 ↔ G1 (Conflict) | {P1} ↔ {G1, G2} | P1, G1 | NO | YES | Group is approved because G2 matches, hiding the pairwise tax conflict on G1. |
| XS005 | `same_vendor` | P1 ↔ G1 (Support) | P1 ↔ G2 (Support) | P1 | NO | YES | Pairwise support on every edge doesn't mean the *group* is a valid multi-vendor settlement. |
| XS006 | `anomaly.orphan_node` | Component | Hypothesis | Nodes | NO | YES | Component-level anomaly invalidates hypothesis, but scalars can't sum. |
| XS007 | `supersedes` (Directional)| P1 → G1 | G1 → P1 | None (Reversed) | NO | YES | Directed cyclic loop treated as mutual support. |
| XS008 | `same_legal_entity` | P1 ↔ G1 | G1 ↔ P1 | P1, G1 | YES | NO | N/A (Canonicalized by scope symmetry). |
| XS009 | `same_legal_entity` | P1 ↔ {G1} | {P1} ↔ G1 | P1, G1 | YES | NO | N/A (Canonicalized sets). |
| XS010 | `financial.currency_match` | P1 ↔ G1 (Conflict) | P1 ↔ {G1, G2} | P1, G1 | NO | YES | Group ignores the pairwise currency mismatch. |

*(Note: Matrix condensed to 10 critical structural cases for the architectural proof).*

## Conclusion
Stage 8J cannot treat an `EvidenceAssertion` as a floating number. If `Assertion A` targets `Scope(P1, G1)` and `Assertion B` targets `Scope(P1, {G1, G2})`, their magnitudes **cannot be mathematically combined** without a formal domain rule (a Projection Rule) that defines how pairwise facts roll up into set-based aggregate facts.
