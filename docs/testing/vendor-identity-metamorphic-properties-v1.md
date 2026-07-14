# Vendor Identity Metamorphic Properties V1

Metamorphic testing proves that our pipeline behaves predictably across transformations.

### VM001 — Case changes preserve structured identity
- **Property**: `parse(x.lower()) == parse(x.upper())`
- **Test construction**: Input a vendor name in all lower case and all upper case.
- **Example**: `abc pvt ltd` ↔ `ABC PVT LTD`
- **Failure signal**: Case-folding normalization is broken or happens after token matching.

### VM002 — Repeated whitespace preserves structured identity
- **Property**: `parse("A  B") == parse("A B")`
- **Test construction**: Insert multiple spaces and tabs between tokens.
- **Example**: `ABC    PVT   LTD` ↔ `ABC PVT LTD`
- **Failure signal**: Whitespace collapse normalization is failing.

### VM003 — NFC/NFD preserves structured identity
- **Property**: `parse(NFC(x)) == parse(NFD(x))`
- **Test construction**: Provide Unicode strings in both normal forms.
- **Failure signal**: Unicode canonicalization is failing.

### VM004 — Punctuation around legal form preserves legal-form identity
- **Property**: `extract_form("PVT. LTD.") == extract_form("PVT LTD")`
- **Test construction**: Add standard punctuation to legal designators.
- **Example**: `ABC PVT. LTD.` ↔ `ABC PVT LTD`
- **Failure signal**: Punctuation standardization is failing.

### VM005 — PRIVATE LIMITED ↔ PVT LTD preserves legal-form SUPPORT
- **Property**: `compare(PRIVATE_LIMITED, PVT_LTD) -> SUPPORT 1.0`
- **Test construction**: Compare two known aliases of the same canonical legal form.
- **Example**: `ABC PVT LTD` ↔ `ABC PRIVATE LIMITED`
- **Failure signal**: Legal form ontology is not correctly collapsing variants.

### VM006 — LLP ↔ PRIVATE LIMITED produces legal-form CONFLICT
- **Property**: `compare(LLP, PRIVATE_LIMITED) -> CONFLICT 1.0`
- **Test construction**: Compare distinct canonical legal forms.
- **Example**: `ABC LLP` ↔ `ABC PRIVATE LIMITED`
- **Failure signal**: Legal form logic is failing to assert conflict on mismatch.

### VM007 — Vendor comparison reversal preserves symmetric assertion proposition
- **Property**: `compare(A, B).assertions == compare(B, A).assertions` (with symmetric proposition logic)
- **Test construction**: Swap the purchase and GST vendor strings.
- **Failure signal**: The comparison logic is order-dependent.

### VM008 — Comparison reversal preserves magnitude
- **Property**: `compare(A, B).magnitude == compare(B, A).magnitude`
- **Test construction**: Verify magnitude is identical.
- **Failure signal**: Asymmetric similarity metric being used.

### VM009 — Comparison reversal preserves polarity
- **Property**: `compare(A, B).polarity == compare(B, A).polarity`
- **Test construction**: Verify polarity is identical.
- **Failure signal**: Polarity logic is order-dependent.

### VM010 — Source lineage reversal does not collapse ancestry
- **Property**: The `EvidenceAncestryRef` correctly traces back to the distinct `ObservationOccurrence` regardless of comparison order.
- **Failure signal**: Ancestry is being mutated or merged.

### VM011 — Source artifact change changes assertion identity
- **Property**: Running the exact same string from two different source systems yields two distinct `EvidenceAssertion` identities.
- **Failure signal**: Assertion identity is ignoring the `EvidenceAncestryRef`.

### VM012 — Runtime retry preserves assertion identity
- **Property**: `compare(A, B)` run twice yields the exact same assertion cryptographic digests.
- **Failure signal**: Non-determinism in the pipeline (e.g. UUID generation or dict iteration order).

### VM013 — Same semantic parse from different sources shares derived artifact identity
- **Property**: `parse(A_from_SAP)` and `parse(A_from_Oracle)` yield `DerivedArtifact`s with the exact same content digest.
- **Failure signal**: Derived artifact identity is improperly including lineage.

### VM014 — Same semantic parse from different sources differs in derivation occurrence identity
- **Property**: The execution event itself has a distinct identity.
- **Failure signal**: Derivation identity is improperly deduplicated.

### VM015 — Legal-form removal changes legal-form result to MISSING/INSUFFICIENT, not CONFLICT
- **Property**: `compare("ABC PVT LTD", "ABC")` yields `MISSING_INPUT` for legal form.
- **Failure signal**: Absence of data is being treated as negative data.

### VM016 — GSTIN state-code change with same PAN preserves tax identity SUPPORT
- **Property**: `compare("07ABCDE1234F1Z5", "29ABCDE1234F1Z5")` yields `SUPPORT same_tax_identity`.
- **Failure signal**: PAN extraction is failing or tied to state code.

### VM017 — GSTIN state-code change changes GST-registration identity
- **Property**: `compare("07ABCDE1234F1Z5", "29ABCDE1234F1Z5")` yields `CONFLICT same_gst_registration`.
- **Failure signal**: Full GSTIN comparison is ignoring state codes.

### VM018 — PAN change creates tax identity CONFLICT
- **Property**: `compare("07ABCDE1234F1Z5", "07XYZDE9876Q1Z5")` yields `CONFLICT same_tax_identity`.
- **Failure signal**: PAN comparison is failing to assert conflict.

### VM019 — Malformed GSTIN cannot produce PAN SUPPORT
- **Property**: `compare("O7ABCDE1234F1Z5", "07ABCDE1234F1Z5")` yields `UNINTERPRETABLE_INPUT`.
- **Failure signal**: OCR auto-repair is illegally operating in the deterministic pipeline.

### VM020 — Adding a common token cannot increase distinctive-token authority
- **Property**: `support_magnitude(ABC TRADERS) <= support_magnitude(ABC)`
- **Failure signal**: The similarity metric is rewarding noise words.

### VM021 — Corpus frequency increase cannot increase rarity-based support
- **Property**: If `doc_freq(TATA)` increases, `support(TATA)` monotonically decreases or stays flat.
- **Failure signal**: Corpus statistics are inverted.

### VM022 — Exact organization core equality cannot become CONFLICT due solely to corpus frequency
- **Property**: `compare(TRADERS, TRADERS)` never yields `CONFLICT`.
- **Failure signal**: High frequency is being misinterpreted as conflict.

### VM023 — Provider output order does not change interpretation result
- **Property**: The tuple of factor interpretations is canonically sorted regardless of provider execution order.
- **Failure signal**: Non-determinism in the result object.

### VM024 — Duplicate assertion emission is rejected
- **Property**: Emitting `SUPPORT same_legal_form` twice from the same provider fails validation.
- **Failure signal**: The interpretation result is not enforcing uniqueness.

### VM025 — Generic trace metadata cannot change assertion identity
- **Property**: Attaching extra runtime logs to the context does not alter the assertion digest.
- **Failure signal**: Assertion identity is poisoning itself with non-semantic data.

### VM026 — Whitespace variations in GSTIN are rejected
- **Property**: `parse("07 ABCDE 1234F 1Z5")` yields `UNINTERPRETABLE_INPUT`.
- **Failure signal**: GSTIN validation is too loose.

### VM027 — Alias mapping direction is symmetric
- **Property**: If `TCS -> TATA CONSULTANCY SERVICES` is in the snapshot, `TATA CONSULTANCY SERVICES -> TCS` yields the same support.
- **Failure signal**: Alias logic is directional.

### VM028 — Missing alias snapshot yields MISSING_INPUT for alias factor
- **Property**: If no alias snapshot is provided, alias factor returns `MISSING_INPUT`.
- **Failure signal**: Attempting to query non-existent snapshot throws exception or assumes empty.

### VM029 — Empty alias snapshot yields INSUFFICIENT_INPUT for alias factor
- **Property**: If an empty alias snapshot is provided, alias factor returns `INSUFFICIENT_INPUT` for all inputs.
- **Failure signal**: Empty snapshot is treated as missing.

### VM030 — Non-alphanumeric noise does not affect core identity
- **Property**: `parse("ABC @#$ LTD") == parse("ABC LTD")`
- **Failure signal**: Punctuation filtering is incomplete.

### VM031 — Order of legal form tokens does not affect extraction
- **Property**: `parse("LTD PVT") == parse("PVT LTD")` (assuming both map to PRIVATE_LIMITED).
- **Failure signal**: Legal form extraction relies on strict token order within the designator.

### VM032 — Prefix legal forms are not extracted
- **Property**: `parse("PRIVATE LIMITED ABC")` does NOT extract `PRIVATE_LIMITED` if policy dictates suffix-only.
- **Failure signal**: Greedy matching extracting legal forms from the start of a trade name.

### VM033 — Single-character names are treated as insufficient
- **Property**: `compare("A", "A")` yields `INSUFFICIENT_INPUT`.
- **Failure signal**: Too low a threshold for meaningful comparison.

### VM034 — Assertion magnitude is strictly bounded
- **Property**: `0.0 < magnitude <= 1.0` for all emitted assertions.
- **Failure signal**: Policy allowing out-of-bounds or zero magnitudes.

### VM035 — Factor result tuple length is invariant
- **Property**: `len(VendorIdentityInterpretation.factors)` is constant across all inputs.
- **Failure signal**: Missing factors are being omitted from the tuple rather than explicitly set to `MISSING_INPUT`.
