# Vendor Artifact Materialization Boundary

Parsing vendor strings into structured semantic objects is computationally expensive. If the same purchase record participates in 5,000 candidate edges during graph reconciliation, we must not parse "ABC PRIVATE LIMITED" 5,000 times.

We must define where parse execution occurs and how results are reused.

## Three Architectural Options

### Option A: Pair-Level Parse Every Time
- **Mechanism**: Parse vendor A and vendor B dynamically inside the edge evaluation logic for every candidate pair.
- **Cost**: For 1,000 purchases × 1,000 GSTs × 100 candidates = 200,000 parse executions.
- **Memory**: Minimal (garbage collected immediately).
- **Correctness**: Perfect.
- **Problem**: Massive redundancy. The system spends 99% of its time reparsing the same strings.

### Option B: Engine-Local Memoization by ObservationIdentity
- **Mechanism**: Cache parse results in memory, keyed by the `ObservationIdentity` (the hash of the raw string).
- **Cost**: Exact number of unique vendor strings (e.g. 2,000).
- **Memory**: In-process dictionary.
- **Problem**: Cache invalidation is tricky if dependencies (like corpus profiles) change. Caches are not shared across distributed workers.

### Option C: Pre-Materialized DerivedArtifacts (Target Architecture)
- **Mechanism**: Parse ALL unique vendor records once during an explicit materialization phase *before* candidate generation. Store them as content-addressed `DerivedArtifact`s in a persistent store. Graph reasoning simply queries the pre-parsed artifacts.
- **Cost**: Same as B (2,000 parses), but amortized across all future reconciliations.
- **Memory**: Stored in a database/KV store, accessible to all workers.
- **Correctness**: Perfect, because `DerivedArtifact` identities explicitly include `SemanticDependencyRef`s (so a change to the corpus profile yields a new artifact hash).

## Proposed Pipeline for Option C

```text
       Raw Records
            │
            ▼
Observation Materialization
            │
            ▼
Vendor Structured Artifact Materialization 
(Runs ONCE per unique vendor name/dependency hash)
            │
            ▼
   Candidate Generation
            │
            ▼
     Graph Reasoning 
(Consumes pre-parsed DerivedArtifacts via fast lookup)
            │
            ▼
  Hypothesis Evaluation
```

## Comparison

| Option | Parse calls (1K×1K×100) | Memory | Correctness | Impl Complexity | Recommended Phase |
|---|---|---|---|---|---|
| A (Pair-Level) | 200,000 | Low | Perfect | Low | Never |
| B (Memoized) | 2,000 | Medium (Local) | Perfect | Medium | V1 (Transitional) |
| C (Pre-Materialized) | 2,000 | High (Distributed) | Perfect | High | Stage 9 |

## Recommendation
Implement **Option B** (Engine-Local Memoization) for Stage 8C-V1 to prove the semantics without rebuilding the engine core. Target **Option C** for Stage 9 when the engine scales out.
