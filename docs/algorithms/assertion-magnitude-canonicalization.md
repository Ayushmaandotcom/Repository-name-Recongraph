# Assertion Magnitude Canonicalization

## Summary
Evidence magnitude must be robustly cross-process deterministic and immune to floating-point formatting inconsistencies.

## Rule
Magnitude identity uses the exact IEEE-754 binary64 bit representation of the finite Python float, packed as hex: `binary64:<hex>`.

`-0.0` is explicitly canonicalized to positive `0.0`. (Note: zero is forbidden as a final assertion magnitude, but this canonicalization is enforced at the identity layer).
Adjacent floats (e.g. `nextafter(0.8, 1.0)`) will correctly hash to distinct identities.
