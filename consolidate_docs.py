import os
import shutil

docs_dir = "/Users/ayushmaangupta/Documents/recongraph/docs/architecture"
adr_dir = os.path.join(docs_dir, "adr")
os.makedirs(adr_dir, exist_ok=True)

# Important ADRs to keep and rename
adrs_to_create = {
    "ADR-001-vendor-identity-factorization.md": "vendor-identity-research-decision.md",
    "ADR-002-amount-interpretation-vs-projection.md": "vendor-v1-scalar-projection-boundary.md",
    "ADR-003-decision-trace-semantic-identity.md": "decision-trace-replay-contract.md",
    "ADR-004-evidence-pipeline-v2.md": "pipeline-architecture-v2.md",
    "ADR-005-evidence-kernel.md": "evidence-assertion-kernel-decision-v2.md"
}

for adr_name, old_file in adrs_to_create.items():
    old_path = os.path.join(docs_dir, old_file)
    if os.path.exists(old_path):
        shutil.copy(old_path, os.path.join(adr_dir, adr_name))

# Create ARCHITECTURE.md
architecture_md = """# ReconGraph Architecture

## System Overview
ReconGraph is a semantic decision engine for evaluating hypothesis propositions over Purchase and GST records. It models evidence as immutable facts that are combined, scored, and evaluated.

## Identity Model (K6)
- **Observations**: Immutable reflections of source fields.
- **Derivations**: Algorithms applied to observations (e.g. normalization).
- **Assertions**: Strongly-typed semantic claims with polarity and magnitude (e.g., `identity.same_legal_entity`).
All objects have a strictly deterministic, canonicalized `sha256` identity.

## Pipeline Lifecycle (V2 Protocol)
All evidence domains (`Financial`, `Vendor`, `Tax`, `Reference`, `Temporal`) strictly follow the EvidencePipeline protocol:
1. `extract()` -> Observation
2. `interpret()` -> Interpretation
3. `contribute()` -> EvidenceAssertion

## Evidence Model & Decision Engine
Evidence Assertions are aggregated by `DecisionEngine` and processed into a mathematical score.

## ADR Index
- `ADR-001`: Vendor Identity Factorization
- `ADR-002`: Amount Interpretation vs Projection
- `ADR-003`: Decision Trace Semantic Identity
- `ADR-004`: Evidence Pipeline V2 Contract
- `ADR-005`: Evidence Semantic Kernel V2
"""
with open(os.path.join(docs_dir, "ARCHITECTURE.md"), "w") as f:
    f.write(architecture_md)

# Delete old unstructured markdown files
for file in os.listdir(docs_dir):
    if file.endswith(".md") and file != "ARCHITECTURE.md":
        os.remove(os.path.join(docs_dir, file))

print("Documentation consolidation complete.")
