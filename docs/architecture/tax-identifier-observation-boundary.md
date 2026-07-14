# Tax Identifier Observation Boundary

The current pipeline collapses observation (what string was found), syntax validation (is it 15 chars?), interpretation (did the PAN match?), and projection (tax score) into a single float inside `tax_identity_score`. A formal TaxIdentifierObservation artifact is missing, meaning OCR corruption cannot be distinguished from structural mismatch.
