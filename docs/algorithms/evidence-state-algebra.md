# Evidence State Algebra

This document formalizes the states of evidence and challenges the use of scalar values for distinguishing absence, ignorance, and neutral evidence.

## State Definitions
* **Absence:** The data required to form an observation does not exist. (e.g. SA001 - Missing Vendor Names).
* **Ignorance:** The data exists, but the provider's logic cannot interpret it. (e.g. SA002 - Multilingual text that the normalizer cannot parse).
* **Neutral Evidence:** The data exists, is interpretable, but mathematically provides zero discriminative power (e.g. SA005 - Ubiquitous `CREDITNOTE`).
* **Conflict:** The data exists, is interpretable, and actively contradicts the claim. (e.g. SA003 - Mismatched Tax IDs).

## The Adequacy of `(support: float, conflict: float, availability: bool)`
Is this tuple sufficient? No.
Consider `availability=True, support=0.0, conflict=0.0`. 
This could represent:
1. **Ignorance:** The provider crashed or returned early because it couldn't parse the string.
2. **Neutrality:** The token was so common (e.g. `TRADERS`) that the corpus math yielded exactly `0.0` support.
The fusion engine must know if the provider *failed* to analyze, or *successfully* analyzed and found zero value.

## Truth Table

| Observation State | Interpretation Capability | Support | Conflict | Meaning |
|---|---|---|---|---|
| MISSING | N/A | 0.0 | 0.0 | True absence of data. No evidence exists. |
| OBSERVED | INCAPABLE | 0.0 | 0.0 | Epistemic ignorance. We have data, but no tools to understand it. |
| OBSERVED | CAPABLE | 1.0 | 0.0 | Perfect support for the claim. |
| OBSERVED | CAPABLE | 0.0 | 1.0 | Total contradiction of the claim. |
| OBSERVED | CAPABLE | 0.5 | 0.0 | Partial support (e.g. subset match). |
| OBSERVED | CAPABLE | 0.0 | 0.5 | Partial conflict (e.g. one digit off). |
| OBSERVED | CAPABLE | 0.5 | 0.5 | Bipolar evidence (supports one part, contradicts another). |
| OBSERVED | CAPABLE | 0.0 | 0.0 | Zero discriminative value (e.g. ubiquitous generic term). |

**Can support/conflict numbers be interpreted correctly without an explicit observation/interpretation state?**
No. `0.0/0.0` is severely overloaded without an explicit enum declaring whether the provider succeeded in analyzing the observation.

Therefore, an explicit state enum (`MISSING`, `UNINTERPRETABLE`, `OBSERVED`) is strictly mathematically required before interpreting the floats.
