# Canonical Semantic Encoding V1

## Summary
To ensure cross-language and cross-platform stable identity hashing, the following canonical JSON subset is adopted.

## Encoding Rules
1. **Null:** Allowed.
2. **Booleans:** Allowed.
3. **Integers:** Strictly signed 64-bit integers. Below min and above max int64 are rejected to prevent arbitrary precision drift.
4. **Floats:** Rejected. (NaN and Infinity are implicitly rejected).
5. **Strings:** Text payload strings MUST be normalized to Unicode NFC. Machine identifiers (e.g. schema keys) MUST be ASCII-only and validated.
6. **Arrays/Tuples:** Order is semantic.
7. **Mappings/Dicts:** String keys only, sorted lexicographically. Custom objects rejected.
