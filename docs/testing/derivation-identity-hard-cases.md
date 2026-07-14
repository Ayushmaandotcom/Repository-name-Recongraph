# Derivation Identity Adversarial Matrix
## Part K — Hard Cases

### Test Cases Matrix (DI001 - DI040)
- **DI001**: Same inputs, same method, same semantic version. Expected: Same Identity.
- **DI002**: Unordered input reversed. Expected: Same Identity.
- **DI003**: Ordered directional inputs reversed. Expected: Different Identity.
- **DI004**: Provider class renamed (impl detail). Expected: Same Identity.
- **DI005**: Provider semantic version bump. Expected: Different Identity.
- **DI009**: PAN extraction executed twice on same GSTIN Observation. Expected: Same Identity (Derivation is pure).
- **DI010**: PAN extraction executed on identical GSTIN Content but different Source Lineage. Expected: Same Derivation Identity (Derivation consumes Observation Content Identity, not Lineage).
*(Remaining 33 cases covered in implementation matrix)*
