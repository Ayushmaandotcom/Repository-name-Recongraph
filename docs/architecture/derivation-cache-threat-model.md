# Derivation Cache Threat Model
## Part N — The Optimization Attack

### Threat Classes
- `PURE_DETERMINISTIC`: Safe to cache globally.
- `EXTERNAL_SNAPSHOT_DEPENDENT` (e.g. registry API): Must cache against the exact API response snapshot hash, NOT just the input GSTIN.
- `NONDETERMINISTIC` (e.g. GPU kernels, time): NEVER cache globally.

DerivationIdentity must embed the snapshot/model hashes to prevent silently turning non-deterministic processes into fake deterministic reasoning.
