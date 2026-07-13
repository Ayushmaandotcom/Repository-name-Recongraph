# Vendor Corpus Statistics

This document defines a corpus-level research model for vendor names, challenging the assumption that all shared tokens are equally informative.

## VS-001 — Normalized Full Name Frequency
* **What is counted:** Exact matches of the complete normalized string.
* **Denominator:** Total number of distinct authoritative identities (e.g. unique GSTINs) in the corpus.
* **Corpus replication invariance:** Required. Duplicate invoices from the same vendor should not inflate the count.
* **Absence mean zero?** Yes.
* **Require ground-truth entity IDs?** Yes, to avoid counting 100 invoices from the same entity as 100 different entities.
* **What it does NOT prove:** Doesn't help with partial matches or typos.

## VS-002 — Vendor Token Document Frequency
* **What is counted:** Occurrences of a specific token (e.g., `INDIA`, `TRADERS`) across distinct vendor identities.
* **Denominator:** Total number of distinct vendor identities.
* **Corpus replication invariance:** Required.
* **Absence mean zero?** Yes.
* **Require ground-truth entity IDs?** Yes.
* **What it does NOT prove:** Does not prove legal identity. Only proves how discriminative (or useless) a token is.

## VS-003 — Legal Form Frequency
* **What is counted:** Occurrences of tokens like `LLP`, `PVT`, `LTD`.
* **What it does NOT prove:** Does not prove identity. It proves that exact match on `LLP` provides almost zero discriminative evidence.

## VS-004 — Organizational Core Frequency
* **What is counted:** Occurrences of the non-generic, non-legal part of the name (e.g., `SHREE GANESH`).

## VS-005 — Alias Ambiguity
* **What is counted:** Number of distinct authoritative identities sharing the exact same alias (e.g., how many companies map to `TCS`).
* **What it does NOT prove:** An alias with high ambiguity provides weak evidence unless paired with contextual signals (like exact tax amount).

## VS-006 — Abbreviation Collision Rate
* **What is counted:** Number of identities sharing an acronym (e.g. `ABC`).
