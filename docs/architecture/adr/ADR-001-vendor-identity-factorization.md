# Vendor Identity Research Decision Report

This report finalizes Stage 8C-0B. It answers the 32 critical architectural questions regarding Vendor Identity epistemology.

## Identity Model

**Q1. What exact identity claim should Stage 8C model first?**
Legal Entity Identity (LI-002) as the ultimate target, supported explicitly by Lexical Name Identity (LI-001) observations. They must be tracked as separate concepts.

**Q2. Which latent identity variables are explicitly deferred?**
Historical Identity Continuity (LI-005) and Brand/Trade Name Association (LI-006) are deferred until a temporal knowledge base is available.

**Q3. Is "vendor identity" too broad a name for the actual model?**
Yes. The model is actually a "Counterparty Legal Entity Resolution" model. "Vendor" conflates the operational role with the legal entity.

## Evidence Model

**Q4. What are the primitive vendor evidence units?**
Lexical similarity metrics, exact subset matches, tax ID string equality, legal suffix extraction.

**Q5. Which are observations?**
The raw text string of the vendor name, the raw text of the tax ID, the extracted legal suffix token.

**Q6. Which are interpretations?**
Levenshtein distance, corpus discriminativeness scores, "Exact Tax Match" boolean.

**Q7. Which require external knowledge?**
Alias resolution (e.g. `TCS` -> `TATA CONSULTANCY SERVICES`) and Corpus token frequencies (e.g. knowing `TRADERS` is highly common).

**Q8. Which evidence units can support identity?**
Exact name matches on rare tokens, matched tax IDs, matched aliases.

**Q9. Which can contradict identity?**
Conflicting tax IDs, different legal suffixes on otherwise identical names.

**Q10. Can the same observation create support and conflict for different latent variables?**
Yes. `ABC LLP` vs `ABC LTD` creates strong Lexical Support but total Legal Entity Conflict.

## Authority

**Q11. Is evidence authority required in Stage 8C?**
Yes, conceptually. A tax ID mismatch must override a fuzzy name match.

**Q12. If not implemented now, what seam must exist?**
The architecture must preserve the distinct source of the conflict (e.g. `SignalName.TAX_IDENTITY_CONFLICT`) rather than silently netting it against a positive name score.

**Q13. Can authoritative identifier agreement be treated as infallible?**
No. Data entry errors can duplicate identifiers across unrelated vendor records. (e.g., AH011 - "Same Tax Identity, Suspiciously Different Names").

**Q14. How are suspicious authoritative conflicts preserved?**
By maintaining bipolar evidence: reporting the Tax ID match as support, while explicitly reporting the extreme Name mismatch as conflict, allowing the Decision Engine to flag it as anomalous.

## Correlation

**Q15. Is `correlation_group: str | None` sufficient?**
No. It collapses the distinction between "same document" and "same system".

**Q16. Where does correlation actually originate?**
From shared epistemic sources: the document, the extraction process, or the master data system.

**Q17. What minimum lineage model should be introduced before Stage 8J?**
Structured Source Lineage: `source_system` and `source_document`.

**Q18. Should the lineage seam be implemented now or merely documented?**
It must be implemented as a typed structure in the metadata payload during Stage 8C so Stage 8J can actually use it.

## Statistics

**Q19. Does Vendor Identity require corpus statistics?**
Yes. Without it, exact matches on `TRADERS` generate false confidence.

**Q20. Which statistic provides the strongest immediate value?**
Vendor Token Document Frequency (VS-002) - identifying which tokens are legally discriminative vs generic.

**Q21. Can a rarity transform similar to Reference Evidence be reused mathematically?**
Yes, the IDF-style transform applies perfectly to token frequencies.

**Q22. What would be invalid about blindly reusing `1 - sqrt(f/N)`?**
Applying it to the *entire string* instead of the *tokens*. An exact match on a rare full string is strong; an exact match on a common token is weak.

## Compatibility

**Q23. Should Stage 8C preserve a scalar compatibility projection?**
Only at the final outer boundary (Explanation Builder), not inside the reasoning engine.

**Q24. Is scalar + metadata acceptable?**
No. It creates a split-brain architecture where the graph and the explanations rely on different data structures.

**Q25. Which migration design is recommended?**
Migration C (Parallel V1/V2 Contracts). V2 generates rich typed payloads; an adapter projects to V1 scalars only when forced by legacy consumers.

**Q26. What is the planned deletion condition for the compatibility scalar?**
When the benchmarking framework and review UI can natively render V2 Evidence Payloads.

## Missingness

**Q27. Is the current explanation-layer zero default an epistemic bug?**
Yes. It translates "absence of data" into "contradictory evidence".

**Q28. What exact invariant should replace it?**
`None` or `Missing`. If forced to a float, it should be omitted from the calculation or left strictly `None` so UI renders "Not Found" instead of "0% Match".

## Stage 8C Scope

**Q29. What is the smallest intellectually honest Stage 8C implementation?**
A typed `VendorIdentityPayload` that explicitly separates Name from Tax ID, preserves raw vs normalized strings, removes the missingness bug, and surfaces conflicts to the graph.

**Q30. What tempting feature must explicitly be rejected from v0.1?**
Corpus statistics and dynamic fuzzy matching.

**Q31. What accepted limitations remain?**
The engine will still fail on Historical Renames and Brand Associations.

**Q32. What empirical evidence would justify Stage 8C v0.2?**
A measured false-positive rate on generic names (`TRADERS`, `INDIA`) in production that necessitates building the Corpus Profiler.
