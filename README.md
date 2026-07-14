# ReconGraph

**An explainable financial exception investigation and reconciliation engine.**

ReconGraph is an advanced epistemic engine designed to automate complex, multi-way financial reconciliations. Instead of relying on opaque similarity scores and rigid rules engines, ReconGraph frames reconciliation as a graph of evidence, semantic assertions, and mathematically grounded hypotheses.

## Why ReconGraph?

Traditional reconciliation systems fail at scale because they conflate *similarity* with *identity*. If a purchase ledger says "ABC Pvt Ltd" and a bank statement says "ABC LLP", a naive fuzzy-matcher might return an 85% match score. 

ReconGraph knows better. It extracts the structural semantic reality: these are two fundamentally different legal entities (Private Limited vs. Limited Liability Partnership) despite sharing an organization core. 

By building a rigorous ontology of financial evidence, ReconGraph can reason across multiple data dimensions—tax identity, legal form, financial amounts, and time—while preserving perfect cryptographic lineage for every decision it makes.

## Core Architecture

ReconGraph operates in distinct semantic stages:
1. **Observation**: Raw financial records (Invoices, Purchases, GST, Bank lines) are ingested.
2. **Derivation**: Records are parsed into structured semantic artifacts (e.g., separating a canonical organization core from its legal designator).
3. **Assertion**: The engine computes pairwise semantic assertions (e.g., `same_tax_identity`, `same_legal_form`).
4. **Graph Reasoning**: The reconciliation engine explores the graph of assertions to build and score hypotheses representing candidate matches.
5. **Traceability**: Every conclusion is backed by an immutable `DecisionTrace`, cryptographically proving exactly what observations and policies led to the outcome.

## Getting Started

### Prerequisites
- Python 3.11+

### Installation

```bash
# Clone the repository
git clone https://github.com/Ayushmaandotcom/Repository-name-Recongraph.git
cd Repository-name-Recongraph

# Install dependencies (development mode recommended)
pip install -e ".[dev]"
```

### Running Tests

ReconGraph relies on strict typing and property-based testing. To ensure the engine's epistemic invariants hold true, run the test suite:

```bash
pytest
```

## Contributing

ReconGraph enforces strict invariants. Contributions must adhere to the following principles:
- **Missing ≠ Contradictory**: An absent field must never be implicitly treated as a contradiction.
- **Traceability over Magic**: Every piece of derived evidence must carry a `SemanticDependencyRef` pointing to its origin.
- **Precision**: Money is represented strictly with `Decimal`, not `float`.

## License

All rights reserved. (License to be determined).
