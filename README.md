# ReconGraph

[![Tests](https://github.com/Ayushmaandotcom/Repository-name-Recongraph/actions/workflows/test.yml/badge.svg)](https://github.com/Ayushmaandotcom/Repository-name-Recongraph/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version: v1.0.0](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Ayushmaandotcom/Repository-name-Recongraph/releases)

**A deterministic, graph-based evidence reasoning framework for financial reconciliation.**

ReconGraph is a fundamentally different approach to financial reconciliation. Instead of relying on opaque similarity scores and rigid heuristic rules, ReconGraph frames reconciliation as a formal reasoning problem. It builds a semantic graph of evidence, strictly enforces provenance, and deterministically derives an auditable explanation for every match, mismatch, and anomaly.

## 🌟 Why ReconGraph?

Traditional reconciliation systems fail at scale because they conflate *similarity* with *identity*. If a purchase ledger says "ABC Pvt Ltd" and a bank statement says "ABC LLP", a naive fuzzy-matcher might return an 85% match score. 

**ReconGraph knows better.** It extracts the structural semantic reality: these are two fundamentally different legal entities (Private Limited vs. Limited Liability Partnership) despite sharing a token root. 

With ReconGraph, you don't get magic black-box ML. You get **provable reasoning**.

- **Epistemic Honesty:** Missing evidence is never treated as a contradiction. 
- **Graph-Based Fusion:** It merges Vendor, Tax, Financial, and Temporal evidence streams into a unified DAG to detect corroboration and contradictions.
- **Deterministic Explainability:** The explanation engine is a structural mirror of the reasoning engine. Every "Why?" is answered by a cryptographic link to the exact node that caused the decision. No hallucinations.
- **Shadow Mode Native:** Deploy legacy models and the Fusion Engine side-by-side. ReconGraph produces differential reports out of the box.

## 🏗 Architecture at a Glance

ReconGraph replaces pipelines with a Multi-Evidence Fusion Graph:

1. **Observations:** Raw financial records (Purchases, GST, Bank lines) are ingested.
2. **Contributions:** Providers generate bipolar evidence (Support, Conflict, Unknown).
3. **Graph Building:** Evidence is structured into a DAG (Directed Acyclic Graph) based on dependencies and semantic relationships.
4. **Propagation:** State propagates through the graph, resolving conflicts and validating corroborations.
5. **Explainability:** The engine yields an `ExplanationArtifact` covering Executive, Domain, Technical, and Audit layers.

*(See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed Mermaid diagrams and system flows).*

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- `pip` or `uv`

### Installation

```bash
git clone https://github.com/Ayushmaandotcom/Repository-name-Recongraph.git
cd Repository-name-Recongraph

# Install the engine and its dependencies
pip install -e .
```

### Running the Engine (Example)

```python
from datetime import date
from decimal import Decimal
from recongraph.engine import ReconGraphEngine
from recongraph.config import ReconGraphConfig
from recongraph.domain.records import PurchaseRecord, GSTRecord

# 1. Initialize Engine
engine = ReconGraphEngine(config=ReconGraphConfig(shadow_mode=False))

# 2. Define Evidence
purchase = PurchaseRecord(
    record_id="P-001",
    vendor_name="TechCorp Private Limited",
    reference="INV-2026-A",
    amount=Decimal("15000.00"),
    record_date=date(2026, 1, 15),
    tax_identity="07TECHC1234A1Z5"
)

gst = GSTRecord(
    record_id="G-001",
    vendor_name="TECHCORP PVT LTD",
    reference="2026-A",
    amount=Decimal("15000.00"),
    record_date=date(2026, 1, 16),
    tax_identity="07TECHC1234A1Z5"
)

# 3. Evaluate Match
packet = engine.reconcile(purchase, [gst])

print(f"Action: {packet.action.value}")
print(f"Explanation: {packet.explanation.executive_summary['decision']}")
```

## 📊 Benchmarks

ReconGraph is built to scale while preserving strict determinism. The reasoning graph typically propagates in `< 1ms` per hypothesis. 

See [BENCHMARKS.md](BENCHMARKS.md) for a complete breakdown of parser, interpretation, graph-building, and fusion performance.

## 📖 Documentation

Dive deeper into ReconGraph's design philosophy and internal APIs:

- [API Reference](docs/API.md)
- [Architecture & Diagrams](docs/ARCHITECTURE.md)
- [Multi-Layer Explainability](docs/explainability.md)
- [The Provenance Contract](docs/provenance.md)
- [Traceability](docs/traceability.md)

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new Evidence Providers, submitting bug reports, and ensuring your code passes the rigorous property-based test suite.

## 🗺 Roadmap

ReconGraph v1.0 solidifies the deterministic reasoning engine. Future versions (v2.x) will explore ML ranking, distributed execution, and external graph persistence. See [ROADMAP.md](ROADMAP.md) for what's next.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
