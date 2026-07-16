# Security and Integrity Policies

ReconGraph is an enterprise-grade reconciliation engine. Because it acts on sensitive financial and taxation data, it enforces strict cryptographic, computational, and determinism boundaries.

## 1. Trace Immutability and Cryptographic Stability

Every decision made by ReconGraph produces a `DecisionTrace` artifact, stamped with a deterministic `trace_id`.

- **Stability Guarantee**: Reordering input sequences of Purchase or GST records has NO effect on the final Trace ID.
- **Trace Hashing**: The `trace_id` is a SHA-256 hash computed over the Engine Version, Configuration Hash, and the sorted canonical identities of the components involved in the decision.
- **Tamper Evidence**: If a trace is modified downstream, its ID can be recalculated from its events and payload to verify its integrity.

## 2. Denial-of-Service and Graph Cycle Limits

The Semantic Propagation engine evaluates directed relationships between derived evidence nodes (e.g., PAN derived from GSTIN).

- **Strict DAG Requirement**: The propagation graph is strictly enforced as a Directed Acyclic Graph (DAG).
- **Cycle Rejection**: If a cyclic dependency is formed during `EvidenceGraph` evaluation, a `TopologicalCycleError` is raised immediately. ReconGraph will fail securely rather than enter an infinite loop.
- **Component Bounding**: The `CandidateGenerator` enforces strict boundaries through inverted index generation, preventing sub-quadratic comparisons from degrading into $O(N^2)$ cross-products under adversarial conditions.

## 3. Data Sanitization and Input Validation

- **No Active Executables**: ReconGraph accepts Python dataclasses (`PurchaseRecord`, `GSTRecord`) or plain JSON payload representations. It does not ingest active logic, scripts, or executables.
- **Deterministic Parsers**: Identifiers like GSTIN and references undergo rigorous string normalization (unicode folding, stripping, upper-casing) before index lookup.

## 4. Reporting Vulnerabilities

ReconGraph is in active development. If you discover a vulnerability or a bypass to the determinism engine, please report it via private channel to the maintainers rather than opening a public issue.
