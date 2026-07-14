# Provider Semantic Identity Study
## Part H — Provider Versioning Attacks

### Versioning Contract
1. **Implementation Version**: Bumps when code changes without affecting semantics (e.g., trie optimization). DOES NOT alter DerivationIdentity.
2. **Semantic Version**: Bumps when output semantics change (e.g., adding `LTD -> LIMITED` to abbreviation tables, or fixing a bug). DOES alter DerivationIdentity.
3. **Model Artifact Identity**: Captured as part of the Method Descriptor if the model dictates semantics.

ProviderSemanticVersion is required to prevent cache poisoning across semantic upgrades.
