# Tax Identity Current Path Audit

## Caller Chain
ReconGraphEngine.reconcile
-> TaxEvidenceProvider.evaluate
-> _weakest_available
-> tax_identity_score
-> normalize_tax_identity
-> calculate_relationship_score
-> PairScoringResult
-> DecisionEngine.decide

## Engine Tax State
- DOES THE LIVE ENGINE HAVE A TAX OBSERVATION OBJECT?: NO
- DOES THE LIVE ENGINE HAVE A TAX INTERPRETATION OBJECT?: NO
- DOES THE LIVE ENGINE HAVE A TAX PROJECTION OBJECT?: NO
- IS TAX EVIDENCE CURRENTLY A SINGLE FLOAT?: YES
