# Evidence Authority Taxonomy

This document answers core questions about authority in evidence models.

## Core Questions

**AT-001 Is authority a property of evidence kind?**
No. Vendor Name evidence from an ERP differs in authority from Vendor Name evidence from a fuzzy OCR scan.

**AT-002 Is authority a property of source?**
Largely yes. A government tax registry has more authority over legal entity structure than an internal CRM.

**AT-003 Is authority a property of extraction process?**
Yes. Structured electronic ingestion has higher epistemic authority than a machine-learning OCR model.

**AT-004 Is authority a property of individual observation?**
Ultimately, yes. Since observations are derived from specific extractions of specific documents, authority is bound to the observation instance.

**AT-005 Can the same GSTIN string have different authority depending on origin?**
Absolutely. If it is scraped from a blurry PDF, it is low authority (subject to OCR corruption). If retrieved via API from the government portal, it is maximum authority.

**AT-006 Can human verification always be considered highest authority?**
No. Humans make mistakes, act on stale data, or click "Approve" without reading. Stale human verification is lower authority than a live API check.

**AT-007 Is mathematical conservation "authoritative"?**
It is structural. If `A = B + C`, that is a mathematical fact, not an asserted authority. It operates on a different axis than epistemic source authority.

**AT-008 Does authority measure truth probability?**
No. This is dangerous. High authority does not mean "99% true". It means "if this contradicts something else, this wins the conflict resolution". Authority is about conflict-breaking rules, not calibration percentages.

**AT-009 Can authority be totally ordered?**
No. You cannot say `DERIVED_CONSERVATION > VERIFIED_REGISTRY` because they apply to different claims.

**AT-010 Should authority be ordinal, categorical, or structured?**
Structured.

## Candidate Models

### Authority Model A — Numeric Rank
* Example: `authority_weight = 0.8`
* Flaw: Turns authority into magnitude. Destroys the semantic difference between support and conflict resolution.

### Authority Model B — Ordered Enum
* Example: `LOW, MEDIUM, HIGH, AUTHORITATIVE`
* Flaw: Extremely vague. What does "HIGH" mean across different subsystems?

### Authority Model C — Structured Authority Descriptor
* Distinguishes `assertion_origin`, `extraction_reliability`.
* Prevents collapsing multidimensional trust into a single float.

## Recommendation
**Authority Model C (Minimal Descriptor seam).** For v0.1, a single semantic `Enum` (e.g., `AuthorityClass(SYSTEM_OF_RECORD, EXTRACTED, INFERRED)`) is the minimum honest seam, avoiding arbitrary numeric weights while preserving the origin type for future fusion rules.
