# Contributing to ReconGraph

ReconGraph is built on a very strict set of epistemic and software engineering principles. If you want to contribute to the core reasoning engine or add a new Evidence Provider, please read this guide carefully.

## The Epistemic Laws of ReconGraph

Every line of code in ReconGraph is bound by these principles:

1. **Missing ≠ Contradictory**: 
   If a record does not have a `tax_identity`, it cannot logically contradict a record that does. The state must be evaluated as `MISSING`, not `CONFLICT`. Do not collapse missing data into negative scores.
   
2. **Traceability over Magic**: 
   Every piece of derived evidence must carry a cryptographically secure `SemanticDependencyRef`. You must be able to trace every node in the graph back to the exact parsed field it came from.
   
3. **Determinism is Non-Negotiable**: 
   Given the same inputs, the same engine version, and the same configuration, ReconGraph MUST output the exact same graph, decision, and trace ID down to the byte. Do not use randomness (`uuid`, `time.now()`) anywhere in the core engine logic.
   
4. **Precision Data Types**: 
   Financial amounts must be strictly parsed into `decimal.Decimal`. Never use `float` for money.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ayushmaandotcom/Repository-name-Recongraph.git
   ```
2. **Install dependencies**
   ```bash
   pip install -e ".[dev]"
   ```
3. **Run Type Checks**
   We enforce strict typing with MyPy.
   ```bash
   mypy src/
   ```
4. **Run the Test Suite**
   We use property-based testing (`hypothesis`) heavily.
   ```bash
   pytest tests/
   ```

## Adding a New Evidence Provider

If you wish to add a new `EvidenceProvider`, it must implement the `EvidenceProviderV2` interface.

1. Implement `get_pipeline()` returning the specific `DomainPipeline`.
2. Ensure your domain parser does not leak state.
3. Write property-based tests that prove your provider is commutative (i.e. `evaluate(A, B) == evaluate(B, A)`).
4. Register your provider in `core_providers.py`.

## Pull Request Process

1. Ensure your code passes all 600+ tests.
2. Ensure `mypy src/` is perfectly clean.
3. Ensure no new fields were added to domain models without updating the hashing/canonicalization functions.
4. Provide a differential shadow-mode report if your PR changes reasoning logic.
