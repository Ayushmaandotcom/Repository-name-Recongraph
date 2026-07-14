# Vendor Corpus Statistics V1

A fuzzy name matcher that does not understand frequency will drastically overvalue common terms (e.g. `TRADERS`, `ENTERPRISES`). Stage 8C requires a `VendorCorpusProfile` to weigh evidence by distinctiveness.

## Section A — Required Statistics

The corpus profile should compute:
- `document_frequency_per_token`: The number of unique vendor records that contain a specific canonical token (e.g. `ENTERPRISES` = 45,000).
- `document_frequency_per_organization_core`: The frequency of an entire canonical core (e.g. `BALAJI ENTERPRISES` = 4,000).
- `token_inverse_frequency`: An IDF analog indicating token rarity.
- `core_collision_count`: The number of *distinct* legal entities (verified by distinct PANs/GSTINs) that share the exact same organization core.
- `legal_form_distribution`: Frequency of each canonical legal form in the corpus.
- `acronym_collision_frequency`: How often a given acronym maps to distinct organization cores.

## Section B — What Corpus Statistics Can and Cannot Do

**CAN:**
- Reduce support magnitude for partial matches involving common tokens (e.g. sharing the token `TRADERS` provides less support than sharing the token `MAHINDRA`).
- Withhold assertions entirely when a token is too common to be informative (e.g., sharing only `INDIA` yields no assertion).
- Distinguish high-rarity cores from low-rarity cores to adjust exact-match support confidence.

**CAN NOT:**
- Create conflict evidence. Low distinctiveness represents an absence of information, not a contradiction.
- Override exact canonical equality support (if two records are exactly `ABC PRIVATE LIMITED`, they support each other regardless of how common `ABC` is, though the magnitude may be capped).
- Make two things different just because many things look similar.

**Key Invariant:** Corpus statistics can reduce or withhold support. They must never create conflict evidence.

## Section C — Token Rarity vs. Whole-Core Similarity

Consider the `TATA` group of companies:
- `TATA CONSULTANCY SERVICES` ↔ `TATA POWER`
  - Sharing `TATA` should **not** provide strong `same_organization_core` support, because `TATA` is a highly common token in the Indian corporate corpus that spans dozens of distinct entities.
- `TATA CONSULTANCY SERVICES` ↔ `TATA CONSULTANCY SERVICE`
  - The complete core similarity remains highly informative. The entire phrase is highly distinctive.

This proves that token-level rarity and whole-core similarity are **SEPARATE observations** that must not be collapsed into a single metric. 

### Proposed Separation of Claims

Instead of forcing both into `same_organization_core`, we should evaluate:
1. `identity.same_organization_core`: Evaluates the full core match.
2. `identity.shared_distinctive_organization_token`: Evaluates partial token overlap, tightly gated by a high rarity threshold.
