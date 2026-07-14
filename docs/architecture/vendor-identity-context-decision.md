# Vendor Identity Context Decision V1

## The Anti-Pattern

When writing a pipeline, the natural instinct is to pass every required object directly to the function:

```python
# THE ANTI-PATTERN - DO NOT DO THIS
def interpret_vendor(
    name_a: str, 
    name_b: str, 
    gstin_a: str, 
    gstin_b: str, 
    corpus: VendorCorpusProfile, 
    policy: VendorIdentityPolicy, 
    aliases: dict, 
    registry: dict, 
    config: dict,
    ...
):
    ...
```

This fails for three reasons:
1. **Unbounded growth**: Every new factor requires new parameters, breaking all existing tests.
2. **Untestable**: Setting up 15 mocks for a simple name comparison becomes impossible.
3. **No identity tracking**: The function has no way to know if `policy` or `aliases` changed between runs, meaning we cannot build an immutable derivation DAG.

## The Context Design

Instead, we bundle the epistemic state of the world into a single, explicitly structured context object.

```python
@dataclass(frozen=True, slots=True)
class VendorIdentityContext:
    corpus_profile: VendorCorpusProfile
    policy: VendorIdentityPolicy
    dependencies: tuple[SemanticDependencyRef, ...]
```

### Field Breakdown

#### 1. `corpus_profile`
- **Why it exists**: Provides the term frequencies necessary to weight organization core distinctiveness.
- **Participates in derivation identity?**: **YES**. If the corpus frequency of a term changes from rare to highly common, the assertion magnitude might drop. Because it alters semantic output, its identity must be explicitly tracked in `dependencies`.
- **Dependency Kind**: `MutableReference` (since corpuses update over time, but we freeze a snapshot).

#### 2. `policy`
- **Why it exists**: Controls mapping of similarity scores to assertion magnitudes (e.g., `similarity_threshold = 0.90`).
- **Participates in derivation identity?**: **YES**. This is the first real test of our K5/K6 dependency model. If the threshold drops to `0.85`, assertions that were previously `INSUFFICIENT_INPUT` might become `SUPPORT`. The exact policy snapshot must participate in the derivation identity.
- **Dependency Kind**: `ConfigurationSnapshot`.

#### 3. `dependencies`
- **Why it exists**: Satisfies the K6 requirement that all external state modifying an assertion must be cryptographically hashed into the `DerivationIdentity`.

### Dealing with Aliases and Registries

If we introduce `alias_snapshot` or `registry_snapshot` into the context later, they must also participate as `MutableReference` dependencies.

We must formally document the semantic difference between an **absent** capability and an **empty** dataset:
- **Absent** (e.g., `alias_snapshot is None`): The system has no capability or configuration to look up aliases. The factor interpretation must return `MISSING_INPUT` because it was never attempted.
- **Empty** (e.g., `alias_snapshot` exists but contains 0 entries): The capability is enabled, but no alias was found for these strings. The factor interpretation returns `INSUFFICIENT_INPUT`.
