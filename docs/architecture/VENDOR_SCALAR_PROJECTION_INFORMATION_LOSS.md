# Vendor Scalar Projection Information Loss

## WHY DOES THE SCALAR STILL EXIST?
Because Stage 8A/8B currently requires scalar vendor similarity to compute its top-level legacy pair relationship confidence. This scalar is a **temporary, explicit, lossy compatibility boundary** pending richer semantic fusion (Stage 8J). 

**It is NOT the desired final vendor architecture.**

## EXACTLY WHAT CANNOT SURVIVE THE SCALAR

### 1. Support/Conflict Coexistence
A pure numeric scalar (`[0.0, 1.0]`) fundamentally assumes that positive identity evidence (e.g., lexical match) and conflict evidence (e.g., PAN mismatch) lie on the same dimensional axis and can be averaged into a single probability. This is false. A strong name match with a PAN mismatch is NOT a "72% similarity". It is "strong text support paired with unresolvable tax contradiction." The scalar permanently erases this coexistence. (We mitigate this by capping the similarity to `0.40` and preserving the conflict in `VendorEvidenceProjection.contradiction_markers`, but the downstream engine only sees `0.40` and thinks the name was a poor match).

### 2. Evidence Dependence (Double Counting)
`VendorIdentityInterpretation` explicitly knows when two PANs matched because they were derived from the same matched GSTIN (`SAME_SOURCE_DERIVATION`). The scalar engine cannot represent this. If tax and vendor scores are summed in the legacy engine, that same string evidence is counted twice, inflating the final confidence artificially.

### 3. Factor-Specific Contradiction
A `0.0` in the legacy engine means "maximal contradiction." It does not explain *why*. Did the PANs differ? Did the names differ completely? The interpretation knows `PAN_IDENTIFIER_CONFLICT` vs `LEGAL_FORM_LEXICAL_DIFFERENCE`. The projected scalar destroys that distinction.

### 4. Missingness
Missing fields yield a `similarity = None`, which the legacy engine then ignores or defaults to `0.0`. The scalar destroys the difference between "I don't have the vendor name" and "I have the vendor name but it completely contradicts."

### 5. Corpus Distinctiveness
The interpretation knows that "ENTERPRISES" matched, but it is extremely common in the corpus (attenuating support). The legacy scalar just sees `0.85` instead of `1.0`. The explanation engine downstream has no way to tell the user *why* the score is 0.85 (i.e. it doesn't know it was a perfect match of a common word vs a 85% fuzzy match of a rare word).

## CONCLUSION
`VendorEvidenceProjection` is a necessary evil to keep production running while we overhaul the decision engine. All future authoritative business logic MUST consume `VendorIdentityInterpretation` directly.
