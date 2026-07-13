# Assertion Authority Placement

This document refines the concept of "Authority" into an Epistemic/Quality context and determines its correct architectural placement.

## Deconstructing Authority
"Authority" is too vague. It conflates structural trust (government registry) with machine capability (OCR confidence).

**AU-001 Can assertion authority be derived from observation metadata?**
Largely yes. If the `ObservationIdentity` points to a government registry API, the structural authority is implicit. 

**AU-002 Should the assertion duplicate it?**
Yes, because Stage 8J fusion needs to quickly index assertions by their quality without doing deep lookups into the source system's schema.

**AU-003 Can one observation produce assertions with different authority?**
Yes. An invoice might explicitly state `PAN X` (High authority) but we run an NLP model to infer `Brand Y` (Low reliability interpretation).

**AU-004 Can interpretation logic affect authority?**
Yes. An inferred claim has lower epistemic quality than an explicitly asserted claim on the same document.

**AU-005 Is AuthorityDescriptor actually evidence-quality context rather than authority?**
Yes. Authority implies "who is in charge." Epistemic quality implies "how much can we trust this derivation."

## Property Placement Table

| Property | Observation | Assertion | Lineage | Payload | Trace |
|---|---|---|---|---|---|
| **Source authority** | Primary | Required (as context) | | | Preserved |
| **Extraction reliability** | Primary | Required (as context) | | | Preserved |
| **Verification status** | | Required (as context) | | | Preserved |
| **Temporal validity** | | Required (as context) | | | Preserved |
| **Interpreter confidence**| | | | Primary | Preserved |

## Interpreter Confidence vs Support Magnitude
**If interpreter confidence is introduced, explicitly distinguish it from support magnitude.**
* **Interpreter Confidence:** "I am 41% sure the text says `MICR0SOFT`."
* **Support Magnitude:** "Assuming it says `MICR0SOFT`, it provides 0.8 support for the claim `SAME_LEGAL_ENTITY`."
Mixing these into `support = 0.8 * 0.41 = 0.328` destroys the epistemic boundary.

## Recommendation
Rename `AuthorityDescriptor` to **`EvidenceQualityContext`**. This object lives on the `EvidenceAssertion` and explicitly declares:
* `source_trust` (e.g. `SYSTEM_OF_RECORD`, `USER_SUPPLIED`)
* `extraction_trust` (e.g. `STRUCTURED`, `UNSTRUCTURED_ML`)
* `verification_trust` (e.g. `UNVERIFIED`, `HUMAN_REVIEWED`)

This separates *epistemic quality* from the *mathematical magnitude* of the claim.
