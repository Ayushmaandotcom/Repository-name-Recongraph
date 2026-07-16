# Dependency Graph

```mermaid
graph TD
    classDef domain fill:#1f77b4,stroke:#fff,stroke-width:2px,color:#fff;
    classDef legacy fill:#d62728,stroke:#fff,stroke-width:2px,color:#fff;
    classDef core fill:#2ca02c,stroke:#fff,stroke-width:2px,color:#fff;

    subgraph Core Engine
        Engine[ReconGraphEngine]:::core
        Evaluator[HypothesisEvaluator]:::core
        PairScorer[pair_scorers.py]:::core
    end

    subgraph Domains
        Vendor[Vendor Provider]:::domain
        Tax[Tax Provider]:::domain
        Reference[Reference Provider]:::domain
        Financial[Financial Provider]:::domain
        Temporal[Temporal Provider]:::domain
    end

    subgraph Artifact Boundaries
        VP[Vendor Artifact]
        TP[Tax Artifact]
        RP[Reference Artifact]
        FP[Financial Artifact]
        TempP[Temporal Artifact]
    end

    Engine --> Evaluator
    Evaluator --> PairScorer
    
    PairScorer --> Vendor
    PairScorer --> Tax
    PairScorer --> Reference
    PairScorer --> Financial
    PairScorer --> Temporal

    Vendor --> VP
    Tax --> TP
    Reference --> RP
    Financial --> FP
    Temporal --> TempP
```

## Anti-Dependencies (Strictly Forbidden)
- PairScorers MUST NOT depend on `signals.py`.
- Evaluators MUST NOT depend on Domain Parsers.
- Domains MUST NOT depend on `DecisionEngine` policies.
