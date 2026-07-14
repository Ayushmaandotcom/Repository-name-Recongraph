# Evidence Semantic Compatibility Matrix
## Part Q — Versioning Doctrine

| Change Type | Claim Version Bump? | Provider Semantic Version Bump? | Method Version Bump? | Cache Invalidation? |
|---|---|---|---|---|
| Refactor Implementation | No | No | No | No |
| Bugfix altering outputs | No | Yes | Yes (implicit) | Yes |
| Change Claim Meaning | Yes | N/A | N/A | Yes |
| Threshold config change | No | Yes (if part of method) | N/A | Yes |
