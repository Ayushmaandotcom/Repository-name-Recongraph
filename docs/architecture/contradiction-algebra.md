# Contradiction Algebra (Stage 8I)

This document formally defines contradiction semantics in ReconGraph's Fusion layer. Intuition is never used to handle conflict.

## Phase 5: Contradiction Semantics

A **Contradiction** exists when two active pieces of evidence provide mutually exclusive interpretations of reality.

### Formal Rules of Contradiction

1. **Veto Supremacy Rule**
   If an `IndependentEdge` provides a definitive Contradiction (e.g., Financial Amount mismatch outside of tolerance), it acts as an absolute veto over aligned structural matches (e.g., perfect Vendor PAN match). 
   `Support(A) + Contradict(B) = Ineligible` (where B is a strict identifier).

2. **Orthogonal Conflict Rule**
   If Vendor Identity supports, but Tax Identity contradicts, they are NOT orthogonal. Since Vendor is often derived from Tax, a strict Tax contradiction overrides a fuzzy Vendor support. 
   `TaxContradict + VendorSupport = Contradict`

3. **Missingness vs. Contradiction**
   A Missing attribute NEVER equals a Contradiction.
   `Missing(Tax) + Support(Vendor) = Support(Vendor)`
   *See [Missingness Model](./missingness-model.md) for propagation.*

### Semantic Examples

**Example A:**
- Vendor: `SUPPORT` (Similarity 0.95)
- Tax: `CONTRADICT` (Distinct PAN)
- Financial: `SUPPORT` (Exact Amount)
- **Result:** `INELIGIBLE` (Tax identity vetoes, as exact distinct tax identities logically preclude identical entities, despite fuzzy vendor names aligning).

**Example B:**
- Vendor: `SUPPORT`
- Reference: `CONTRADICT` (Different Invoice Numbers)
- Financial: `SUPPORT`
- **Result:** `REVIEW_AMBIGUOUS`. Reference contradiction is not an absolute veto because reference numbers are frequently mistyped or mapped to different internal fields (PO number vs. Invoice number). It diminishes compatibility but does not veto.

### Mathematical Representation

Let `C_a` be the Compatibility score of dimension `a`.
Let `V_a` be the Veto Boolean of dimension `a` (`True` if definitive contradiction).

`FusionResult = 0 if any(V) else FusionPolicy(C)`

Contradictions are not just "negative scores". They are topological blockages in the EvidenceGraph.
