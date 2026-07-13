# Evidence Authority Model

This document formally investigates the distinction between evidence magnitude, authority, availability, and conflict.

## Q1: Can two evidence units both have strong magnitude while supporting opposite identity claims?
Yes. Example AH001: `ABC PRIVATE LIMITED` vs `ABC PRIVATE LIMITED` has maximum lexical magnitude (100% similarity). But if they carry `TAX-A` and `TAX-B`, the identifier conflict has maximal conflict magnitude. They strongly support opposite claims (Lexical Identity = YES, Legal Identity = NO).

## Q2: Does stronger authority mean the lower-authority evidence should be deleted?
No. Deleting the lower-authority evidence destroys provenance and makes the system untrustable. If the tax identity was extracted via OCR incorrectly, the system *needs* to know the vendor name was an exact match so a human reviewer can see the conflict and correct the extraction.

## Q3: Should authoritative contradiction become a negative vendor score?
No. Collapsing a multidimensional conflict into a single scalar (e.g. `score = -1.0`) destroys the specific nature of the conflict. A negative score could mean "the names are completely different" or "the names are identical but the tax IDs conflict". These are epistemically different states.

## Q4: Or should contradiction remain an explicit conflict axis?
Yes. Contradiction must be preserved explicitly. The Decision Engine needs to differentiate between "no evidence", "weak evidence", and "strong contradictory evidence".

## Q5: Can `score: float` represent: strong support, strong conflict, no evidence without ambiguity?
No. `0.0` currently means strong conflict (e.g., penalty). `1.0` means strong support. What is no evidence? Currently `None` is mapped to `0.0` or omitted entirely, breaking the arithmetic. A single float cannot distinguish "I know these are different" from "I don't know if these are the same".

## Q6: Would a bipolar model such as `support`, `conflict` solve this?
Partially. It solves the ambiguity between absence (`support=0, conflict=0`) and contradiction (`support=0, conflict=1`).

## Q7: Would bipolar evidence still fail to represent authority?
Yes. Bipolar evidence gives magnitude, but `conflict=1.0` (names look different) vs `conflict=1.0` (authoritative tax identifiers mismatch) carry vastly different authority. We don't just want to know *how much* conflict there is, but *what kind of authority* backs that conflict.

## Q8: Do we potentially require `support`, `conflict`, `authority`, `availability`?
Yes. This dimensional separation prevents epistemic collapse.

## Conceptual Distinctions & Counterexamples

* **Magnitude vs Authority:** An exact match on a generic word like `TRADERS` has high magnitude but zero authority. A mismatch on a government GSTIN has high authority.
* **Provenance vs Availability:** `Availability` means the field was present in the data. `Provenance` means we know *how* it was populated (OCR vs ERP master data). High availability does not mean high quality provenance.
* **Conflict vs Absence:** Missing a vendor name (Absence) is not evidence that the vendors are different (Conflict).
