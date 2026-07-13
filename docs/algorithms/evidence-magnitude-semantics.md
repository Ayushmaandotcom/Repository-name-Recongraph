# Evidence Magnitude Semantics

This document formalizes the mathematical meaning of `support_magnitude` and `conflict_magnitude` to prevent a "fake-math" catastrophe in Stage 8J.

## Magnitude Challenge Answers

**MS-001 Magnitude relative to what scale?**
Relative to the specific `magnitude_contract` declared by the claim or the provider.

**MS-002 Does 1.0 mean maximal evidence under the provider's model?**
Yes, but "maximal evidence" for lexical similarity is mathematically different from "maximal evidence" for rare reference matching.

**MS-003 Can magnitudes from different providers be compared?**
Not blindly. 

**MS-004 Can magnitude 0.8 from vendor evidence be compared with 0.8 from financial evidence?**
No. They are fundamentally different axes of observation.

**MS-005 If not, can Stage 8J consume them directly?**
Stage 8J can consume them to apply logical rules (e.g., "if any conflict on tax ID > 0.5, block") but it **must not** naively sum or average them.

**MS-006 Does each claim require a magnitude contract?**
Yes.

**MS-007 Does each provider require calibration?**
Yes, eventually (Stage 8K).

**MS-008 Can structural heuristics and corpus-derived rarity use the same magnitude scale?**
No. Structural heuristics are typically binary or stepped. Corpus rarity is continuous and empirical.

**MS-009 Can Reference Evidence bounded positive compatibility be called support magnitude?**
Yes, as long as its contract explicitly defines that the magnitude represents `rarity_v1`.

**MS-010 Are binary magnitudes valid?**
Yes. An exact mathematical conservation is binary: 1.0 (conserved) or 0.0 (not). A binary flag like `UNDERPAYMENT` translates cleanly to a 1.0 `conflict_magnitude` against the claim `financial.conservation`.

**MS-011 Can an assertion use: `support = 1.0` and `conflict = 1.0`?**
Yes. A claim like `financial.payment_completeness` might see exact invoice net amount matched (support 1.0) but a massive unallocated tax amount variance (conflict 1.0).

**MS-012 Should magnitude semantics be claim-local?**
Yes.

## Candidate Models
* **MM-A (Universal Scale):** Mathematically fraudulent.
* **MM-B (Provider-Local Scale):** Makes cross-provider fusion impossible.
* **MM-C (Claim-Local Magnitude Contract):** Claims define the scale. All providers targeting `identity.same_legal_entity` must project onto its defined contract scale.
* **MM-D (Uncalibrated + Metadata):** Store raw output, push calibration entirely to fusion.

## Recommendation
**MM-C (Claim-Local Magnitude Contract).**
To fuse evidence, Stage 8J must know what the numbers mean. The `ClaimDescriptor` must define the magnitude contract (e.g., "0.0 to 1.0 representing Jaccard similarity").

**What is Stage 8J forbidden from doing before calibration?**
Stage 8J is absolutely forbidden from treating uncalibrated raw magnitudes from different contracts as probabilistic weights in a universal summation or Bayesian update.
