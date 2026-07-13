# Open Architecture Questions

## Financial Semantic Naming Audit

**Source**: Stage 8B review  
**Status**: OPEN  
**Required before**: Stage 8J (Evidence Fusion)

### Question

Do `SPLIT_PAYMENT` and `FEE_DETECTED` represent proven financial semantics or candidate explanations inferred from conservation patterns?

### Risk

Interpretive labels may overstate what amount observations alone prove.

**Example:**

```
100,000 ↔ 50,000 + 50,000
```

This supports **split structure**. It does not prove the business event was a "split payment."

Possible actual events:
- Split invoice
- Partial posting
- Tax component separation
- Ledger allocation
- Installments

Similarly, `FEE_DETECTED` when `residual = 250` is a **candidate explanation**, not an observation. The residual could equally be:
- A fee
- A withholding
- A rounding artifact
- An adjustment
- A posting error

### Required Action

Classify each financial evidence kind into one of:

| Classification | Meaning |
|---|---|
| `OBSERVATION` | Raw arithmetic fact (e.g., `delta = 0`, `residual = 250`) |
| `STRUCTURAL_INTERPRETATION` | Pattern inferred from structure (e.g., 1:N conservation, small nonzero residual) |
| `BUSINESS_EXPLANATION` | Domain-specific candidate meaning (e.g., "split payment", "fee") |

Current evidence units and their likely correct classification:

| Evidence Unit | Current Label Type | Likely Correct Classification |
|---|---|---|
| `EXACT_TOTAL_MATCH` | Structural | `OBSERVATION` — sums are equal |
| `SPLIT_PAYMENT` | Business | `STRUCTURAL_INTERPRETATION` — 1:N conservation |
| `UNDERPAYMENT` | Business | `STRUCTURAL_INTERPRETATION` — positive residual |
| `OVERPAYMENT` | Business | `STRUCTURAL_INTERPRETATION` — negative residual |
| `FEE_DETECTED` | Business | `BUSINESS_EXPLANATION` — small residual candidate |
| `ROUNDING_MATCH` | Structural | `STRUCTURAL_INTERPRETATION` — sub-tolerance residual |
| `CURRENCY_MISMATCH` | Observation | `OBSERVATION` — currencies differ |
| `GROSS_NET_MATCH` | Business | `BUSINESS_EXPLANATION` — tax-inclusive candidate |

### Consequence for Stage 8J

If Evidence Fusion treats `FEE_DETECTED` as an observed fact rather than a candidate explanation, the fusion engine may assign inappropriate confidence to what is actually an inference. The fusion layer must know the epistemic status of each evidence unit.
