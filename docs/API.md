# ReconGraph Public API Reference

The ReconGraph library has a clean, curated public API. When interacting with the engine from external systems, you should only need the following core classes.

## Engine Interface

### `ReconGraphEngine`
`recongraph.engine.ReconGraphEngine`

The primary orchestrator of the reconciliation process.

```python
def __init__(self, config: ReconGraphConfig)
```
- Initializes the engine.

```python
def reconcile(
    self, 
    purchase: PurchaseRecord, 
    gst_candidates: Sequence[GSTRecord]
) -> ReviewPacket
```
- Takes a canonical Purchase Record and a list of candidate GST Records.
- Automatically builds the candidate graph, evaluates hypotheses, fuses evidence, and arrives at a decision.
- Returns a `ReviewPacket` containing the final outcome and the cryptographic explanation.

## Configuration

### `ReconGraphConfig`
`recongraph.config.ReconGraphConfig`

Immutable configuration object that determines the semantic policy.

```python
@dataclass
class ReconGraphConfig:
    engine_version: str = "1.0.0"
    shadow_mode: bool = False
    vendor_minimum_length: int = 6
    vendor_fuzzy_threshold: float = 0.85
    financial_tolerance: float = 0.05
```

## Domain Records

### `PurchaseRecord` and `GSTRecord`
`recongraph.domain.records`

The strictly typed representations of financial facts. Both extend `FinancialRecord`.

```python
@dataclass(frozen=True)
class PurchaseRecord(FinancialRecord):
    record_id: str
    vendor_name: str
    reference: str
    amount: Decimal
    record_date: date
    tax_identity: str | None
```

## Review Outcomes

### `ReviewPacket`
`recongraph.graph.review.ReviewPacket`

The final container sent back to the business logic layer.

```python
@dataclass(frozen=True)
class ReviewPacket:
    packet_id: str
    action: DecisionAction
    purchases: tuple[PurchaseRecord, ...]
    gsts: tuple[GSTRecord, ...]
    explanation: ExplanationArtifact | None
    competitors: tuple[str, ...]
    checklist: tuple[str, ...]
```

### `ExplanationArtifact`
`recongraph.graph.fusion_explainability.ExplanationArtifact`

The multi-layer explanation detailing exactly *why* the decision was reached.

```python
@dataclass(frozen=True)
class ExplanationArtifact:
    trace_id: str
    executive_summary: dict[str, str]
    domain_summaries: dict[str, Any]
    technical_details: dict[str, list[str]]
    audit_nodes: dict[str, dict[str, Any]]
```

## Shadow Mode Analytics

### `DifferentialResult`
`recongraph.graph.differential.DifferentialResult`

If `shadow_mode=True`, the engine yields these results to compare legacy vs. fusion execution.

```python
@dataclass(frozen=True)
class DifferentialResult:
    trace_id: str
    legacy_decision: str
    fusion_decision: str
    is_match: bool
    discrepancy_reason: str | None
```
