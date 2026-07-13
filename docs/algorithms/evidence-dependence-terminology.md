# Correlation Is Not Dependence

This document formalizes terminology for evidence fusion, rejecting premature mathematical assumptions.

## Terminology Definitions

* **Shared Provenance:** Two observations originate from the same physical document, same IT system, or same human action. (A fact).
* **Shared Extraction Process:** Two observations were processed by the same software module (e.g. OCR model X). (A fact).
* **Semantic Overlap:** Two observations provide evidence for the exact same Target Claim. (A logical truth).
* **Statistical Correlation:** A measurable, empirical mathematical relationship (e.g. Pearson correlation coefficient > 0) between the values of two variables across a population. (An empirical measurement).
* **Conditional Dependence:** In a probabilistic model (like Bayesian networks), the probability of observing A changes if we know B is true, given some underlying state. (A probabilistic modeling assumption).
* **Common-Cause Failure:** A single failure event (e.g., a blurry scan) that corrupts multiple observations simultaneously. (An engineering vulnerability).

## The Risk of "Correlation"

**DT-001 Should Stage 8J use the term `correlation_group`?**
No. We do not have statistical correlation data. Calling it a correlation group implies we can apply covariance math.

**DT-002 Would `dependence_context` be more honest?**
Yes. Or strictly `lineage`.

**DT-003 Should lineage be preserved without making a dependence judgment?**
Yes. Lineage is a factual observation. Dependence is a modeling assumption based on that fact.

**DT-004 Can fusion infer possible shared failure context from lineage?**
Yes. The fusion engine can heuristically down-weight evidence from the same `source_document` without needing to prove statistical correlation.

**DT-005 What empirical data would be required to estimate actual dependence?**
A massive, manually annotated ground-truth dataset where both signals fail, succeed, or diverge independently.

**DT-006 Can synthetic scenarios establish real-world dependence?**
No. Synthetics only prove the model behaves as the developer programmed it. They cannot prove the real-world statistical distribution of errors.

**DT-007 What should ReconGraph claim before such data exists?**
ReconGraph should claim: "These two observations share provenance." It must absolutely forbid claiming: "These two observations are statistically correlated."

## Forbidden Terminology
Until empirical data exists, the following terms are forbidden in production fusion logic or documentation:
* Correlation
* Covariance
* Statistical Dependence
* Bayesian Update (unless explicitly modeled as such)
