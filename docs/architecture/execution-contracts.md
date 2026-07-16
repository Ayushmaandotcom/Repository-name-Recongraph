# Execution Contracts

This document formalizes the operational responsibilities of each abstraction in the ReconGraph pipeline. 

## 1. Evidence Provider Contract
`EvidenceProvider.evaluate(purchases, gsts) -> EvidenceContribution`
- **MUST** encapsulate an internal `EvidencePipeline`.
- **MUST** be the sole entry point for domain evaluation.
- **MUST NOT** share internal interpretation state except through the `EvidenceContribution.metadata` payload.

## 2. Pipeline Symmetry Contract
- Every domain pipeline **MUST** implement:
  1. `extract` -> Returns a Domain Observation mapping to `DomainArtifacts`.
  2. `interpret` -> Returns a `DomainPairInterpretation`.
  3. `contribute` -> Projects interpretation and returns `EvidenceContributionV2`.

## 3. Pair Scorer Contract
- **MUST** blindly invoke `Provider.evaluate()` for all registered providers.
- **MUST NOT** execute pipeline subcomponents (e.g. `interpret`, `project`) directly.
- **MUST NOT** derive semantic findings.
- **MUST NOT** determine match eligibility.
- **MUST** strictly aggregate and return a map of `EvidenceContributions`.

## 4. Parser Authority Contract
- **MUST** be the only entity allowed to perform regex matching, substring slicing, text normalization, and lowercasing.
- **MUST** output an immutable `ParsedArtifact` guaranteeing valid structural format.

## 5. Interpretation Authority Contract
- **MUST** consume only `ParsedArtifacts`.
- **MUST NOT** execute string manipulation.
- **MUST NOT** return scalar (`float`) scores. It must return categorical Enums (`RelationState`).

## 6. Projection Authority Contract
- **MUST** be the only entity allowed to convert `RelationState` into a `float` or a list of `violations`.
- **MUST** explicitly document itself as a lossy scalar compression layer for the legacy Decision Engine.
