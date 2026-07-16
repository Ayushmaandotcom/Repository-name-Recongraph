# ReconGraph Architecture

ReconGraph is a pipeline of semantic transformation. Data moves from unstructured, disconnected records into a unified graph of evidence.

## System Flow

The core of ReconGraph executes in these distinct phases:

```mermaid
sequenceDiagram
    participant Engine as ReconGraph Engine
    participant Generator as Candidate Generator
    participant Builder as Graph Builder
    participant Fusion as Fusion Engine
    participant Explain as Explainability Engine

    Engine->>Generator: Input (Purchase, GST[])
    Generator->>Engine: Candidate Graph (Nodes + Blocking Edges)
    Engine->>Builder: Build Semantic Hypotheses
    
    loop For each Hypothesis
        Builder->>Builder: Parse -> Observe -> Interpret -> Project
        Builder->>Builder: Evaluate Provider Contributions
    end
    
    Builder->>Engine: Evidence Graph
    Engine->>Fusion: Propagate and Fuse
    Fusion-->>Engine: FusionResult (Action)
    
    Engine->>Explain: Generate Provenance Artifact
    Explain-->>Engine: ExplanationArtifact
    
    Engine->>User: ReviewPacket
```

## Data Lifecycle

ReconGraph's epistemic guarantee comes from its strict data lifecycle. Data is transformed immutably at each step:

```mermaid
graph TD
    A[Raw Record] -->|Parsers| B[Observation]
    B -->|Interpreter| C[Interpretation]
    C -->|Projector| D[Projection]
    D -->|EvidenceProvider| E[EvidenceContribution]
    
    subgraph Evidence Graph
    E --> F[Fusion Node]
    F -->|Dependency Edge| G[Parent Node]
    F -->|Contradiction Edge| H[Conflicting Node]
    end
    
    F -->|Propagation| I[Fusion Result]
    I --> J[Decision Action]
```

## Differential Shadow Mode Architecture

To support safe deployments, ReconGraph can run Legacy Heuristics and Graph Fusion side-by-side, producing differential reports.

```mermaid
flowchart LR
    A[Input Records] --> B{shadow_mode?}
    B -- Yes --> C[Legacy Engine]
    B -- Yes --> D[Fusion Engine]
    
    C --> E[Legacy Action]
    D --> F[Fusion Action]
    
    E --> G{Compare}
    F --> G
    
    G -- Matches --> H[Differential: OK]
    G -- Mismatches --> I[Differential: Discrepancy]
```

## Evidence Node Taxonomy

A `FusionNode` encapsulates an `EvidenceContribution`. It carries explicit state regarding its role in the graph.

```mermaid
classDiagram
    class FusionNode {
        +String identity_hash
        +String provider_name
        +List~String~ violations
        +PropagationStatus status
    }
    
    class PropagationStatus {
        <<enumeration>>
        UNAFFECTED
        SUPPORTED
        QUESTIONED
        CONTRADICTED
        CORROBORATED
    }

    FusionNode --> PropagationStatus
```
