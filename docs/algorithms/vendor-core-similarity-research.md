# Vendor Core Similarity Research V1

Lexical similarity metrics provide raw observations. They do not directly calculate assertion magnitudes. 

## Similarity Metrics Investigated

1. **Exact canonical equality**
   - **Algorithm**: String equality after canonicalization.
   - **Strengths**: Perfect precision for identical inputs. Zero false positives on exact cores.
   - **False Positive Risk**: Low (unless core is extremely common, e.g., "TRADERS").
   - **Output**: Boolean (1.0 or 0.0).

2. **Token-set equality (order-independent)**
   - **Algorithm**: `set(tokens_a) == set(tokens_b)`.
   - **Strengths**: Handles word reordering (e.g., `ENTERPRISES BALAJI` ↔ `BALAJI ENTERPRISES`).
   - **False Positive Risk**: Low.
   - **Output**: Boolean (1.0 or 0.0).

3. **Token multiset equality**
   - **Algorithm**: Considers token counts (e.g., `MAHINDRA MAHINDRA` != `MAHINDRA`).
   - **Strengths**: Preserves duplicate token semantics.
   - **False Positive Risk**: Very Low.

4. **Token containment (Subset)**
   - **Algorithm**: `set(tokens_a).issubset(set(tokens_b))`.
   - **Strengths**: Handles partial omissions (e.g., `ABC TRADERS` ↔ `ABC TRADERS INDIA`).
   - **False Positive Risk**: High (e.g., `RELIANCE` is a subset of `RELIANCE RETAIL` and `RELIANCE INDUSTRIES`, which are different legal entities).

5. **Levenshtein ratio / Edit distance**
   - **Algorithm**: Edit distance normalized to [0, 1].
   - **Strengths**: Handles typos (`TECHNOLOGIES` ↔ `TECHONLOGIES`).
   - **False Positive Risk**: Medium (can conflate distinct short names, e.g. `ABC` ↔ `ADC`).

6. **Jaro-Winkler**
   - **Algorithm**: Emphasizes prefix matches.
   - **Strengths**: Excellent for names where the most distinct part is at the front.
   - **False Positive Risk**: Medium.

7. **Character trigram similarity**
   - **Algorithm**: Overlap of 3-character sequences.
   - **Strengths**: Robust to spelling variations and OCR errors.
   - **False Positive Risk**: Low to Medium.

8. **Phonetic similarity (Metaphone)**
   - **Algorithm**: Matches words that sound alike.
   - **Strengths**: Good for transcribed names (`SHREE` ↔ `SRI`).
   - **False Positive Risk**: Very High (conflates etymologically distinct but phonetically similar names).

9. **Acronym similarity**
   - **Algorithm**: Compare first letters of major tokens.
   - **False Positive Risk**: Extreme (e.g., `TCS` ↔ `TATA CONSULTANCY SERVICES` vs `TCS LOGISTICS`).

10. **Token IDF-weighted cosine similarity**
    - **Algorithm**: TF-IDF vectors compared via cosine similarity.
    - **Strengths**: Downweights common tokens like `TRADERS`.
    - **False Positive Risk**: Low, requires corpus statistics.

## Adversarial Test Matrix

| Pair | Expected Relationship | Jaro-Winkler | Token-Set | Exact | Acronym | Semantic Risk |
|---|---|---|---|---|---|---|
| ABC ↔ ABC | Same Core | 1.00 | 1.0 | 1.0 | 1.0 | None |
| ABC TRADERS ↔ ABC TRADERS | Same Core | 1.00 | 1.0 | 1.0 | 1.0 | None |
| ABC TRADERS ↔ ABC TECHNOLOGIES | Diff Core | ~0.75 | 0.5 | 0.0 | 1.0 | High FP if threshold low |
| MAHINDRA AND MAHINDRA ↔ MAHINDRA & MAHINDRA | Same Core | 1.00* | 1.0* | 1.0* | 1.0 | None (*after '&' normalization) |
| TATA CONSULTANCY SERVICES ↔ TCS | Alias | ~0.50 | 0.0 | 0.0 | 1.0 | High FN (missed alias) |
| TCS ↔ TCS LOGISTICS | Diff Core | ~0.80 | 0.5 | 0.0 | 0.0 | High FP |
| HDFC BANK ↔ HDFC | Subset | ~0.85 | 0.5 | 0.0 | 0.0 | FP (different entities) |
| RELIANCE INDUSTRIES ↔ RELIANCE RETAIL | Diff Core | ~0.75 | 0.5 | 0.0 | 1.0 | FP |
| AMAZON SELLER SERVICES ↔ AMAZON | Subset | ~0.70 | 0.3 | 0.0 | 0.0 | FP |
| SHREE RAM TRADERS ↔ SRI RAM TRADERS | Phonetic Variant | ~0.90 | 0.6 | 0.0 | 1.0 | FN if exact only |
| BALAJI ENTERPRISES ↔ BALAJI ENTERPRISE | Typo/Variant | 0.98 | 0.5 | 0.0 | 1.0 | None |
| NEW INDIA TRADING CO ↔ NEW INDIA TRADERS | Variant | ~0.90 | 0.5 | 0.0 | 1.0 | None |
| A B C ↔ ABC | Variant | 0.00* | 0.0* | 0.0* | 1.0 | FN (*before whitespace normalization) |
| XYZ INTERNATIONAL ↔ XYZ INTL | Abbreviation | ~0.80 | 0.5 | 0.0 | 1.0 | None |
| GLOBAL TECHNOLOGIES ↔ GLOBAL TECH | Abbreviation | ~0.85 | 0.5 | 0.0 | 1.0 | None |
| BALAJI ENTERPRISES ↔ SHREE BALAJI ENTERPRISES | Subset | ~0.85 | 0.6 | 0.0 | 0.0 | FP |
| TATA MOTORS ↔ TATA POWER | Diff Core | ~0.75 | 0.5 | 0.0 | 1.0 | FP |
| RELIANCE INDUSTRIES ↔ RELIANCE | Subset | ~0.85 | 0.5 | 0.0 | 0.0 | FP |
| STATE BANK OF INDIA ↔ SBI | Alias | ~0.50 | 0.0 | 0.0 | 1.0 | FN |
| HINDUSTAN UNILEVER ↔ HUL | Alias | ~0.40 | 0.0 | 0.0 | 1.0 | FN |

## Interpretation Policy

A similarity metric does not necessarily directly become an assertion magnitude. 
For example, a Jaro-Winkler score of 0.94 does not mean we emit an assertion with `magnitude = 0.94`.

**Metric output is an observation. Assertion magnitude is an interpretation of that observation. They are not inherently identical.**

The interpretation policy mediates this:
- **Exact core equality**: Emits `SUPPORT 1.0`
- **Token-set equality**: Emits `SUPPORT 0.95`
- **High edit similarity (>0.92)**: Emits `SUPPORT 0.75` (a bounded, discrete semantic magnitude, NOT the raw 0.92 metric value).
- **Weak similarity (<0.70)**: No assertion emitted.
