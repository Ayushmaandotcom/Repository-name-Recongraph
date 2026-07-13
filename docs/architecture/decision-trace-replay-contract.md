# Decision Trace Replay Contract

This document explicitly defines the Replay Contract for ReconGraph Decision Traces in v0.1.

## Replay Modes Evaluated

* **Replay A — Historical Explanation:** Read an old trace and explain what the old engine decided based on the serialized assertions.
* **Replay B — Historical Re-execution:** Rerun the exact Python code from the past to regenerate the assertions from the raw data.
* **Replay C — Counterfactual Re-evaluation:** Run the *current* Python code against the *historical* raw data to see if the new engine makes a better decision.

## Answers to Trace Questions

**TR-001 Which modes must ReconGraph v0.1 support?**
Replay A (Historical Explanation) and Replay C (Counterfactual Re-evaluation).

**TR-002 Does `engine_version` + `config_hash` support Replay A?**
No. They identify the *environment*, but they don't contain the assertions. To explain historical decisions instantly without running code, the trace must serialize the `EvidenceAssertion`s.

**TR-003 Does it support Replay B?**
Practically, no. In Python, old package versions, changed dependency graphs, and unavailable external services make Replay B (exact historical code execution) impossible without containerizing every run. We explicitly abandon Replay B.

**TR-004 Where are raw inputs preserved?**
In the trace, serialized as immutable `Observation` or raw record snapshots. This enables Replay C.

**TR-005 Should traces preserve evidence assertions?**
Yes. Mandatory for Replay A.

**TR-006 Should traces preserve observations?**
Yes. Mandatory for Replay C.

**TR-007 Can historical assertions be trusted if claim semantics changed?**
Only if the claim semantic version is preserved. A trace reading `claim=same_legal_entity, semantic_version=1` is an immutable historical fact. If the engine is currently on `semantic_version=2`, it knows not to apply V2 fusion logic to a V1 historical assertion.

**TR-008 Does claim semantic version solve this?**
Yes.

**TR-009 Can old unknown payloads remain explainable?**
Yes, because the payload is a `Tagged Serializable Union`. It can be dumped as raw JSON for a human to read even if the Python `dataclass` was deleted years ago.

**TR-010 What does trace reader do when it cannot decode payload V1?**
It retains the generic `dict`.

**TR-011 Can it still show assertion core fields?**
Yes. The core fields (claim, scope, magnitude, state) are heavily standardized and independently deserialized.

**TR-012 Should payload decoding failure invalidate the entire trace?**
No. It should gracefully degrade to a raw dictionary display.

## Formal Guarantee
ReconGraph v0.1 traces guarantee **Instant Historical Explanation** via fully serialized `EvidenceAssertion`s. The trace reader will not execute provider code. The trace will tolerate missing Python payload classes gracefully. 
ReconGraph v0.1 traces guarantee **Counterfactual Re-evaluation** by preserving the raw Observations, allowing the current graph engine to produce a parallel set of modern Assertions for benchmarking against the past.
