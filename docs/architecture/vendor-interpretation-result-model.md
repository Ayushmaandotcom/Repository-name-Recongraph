# Vendor Interpretation Result Model V1

## Why a Monolithic Result is Wrong

If we design a single pipeline result object with a global state, we risk destroying valid evidence.

```python
# THE ANTI-PATTERN
@dataclass(frozen=True, slots=True)
class VendorIdentityPipelineResult:
    state: EvidenceState
    assertions: tuple[EvidenceAssertion, ...]
```
If the vendor name is completely missing from one record, but both records contain valid, matching GSTINs, a monolithic pipeline might return `state=MISSING_INPUT` because it cannot compare names. By doing so, it silently discards the valid tax identity and GST registration evidence. 

## The Factorized Model

To be epistemically honest, the result must be factorized. One factor can be missing while another is interpreted.

```python
@dataclass(frozen=True, slots=True)
class VendorFactorInterpretation:
    factor: VendorIdentityFactorId
    result: EvidenceInterpretationResult

@dataclass(frozen=True, slots=True)
class VendorIdentityInterpretation:
    factors: tuple[VendorFactorInterpretation, ...]
```

### Open VendorIdentityFactorId vs. Fixed Fields

We do not use fixed dataclass fields (e.g. `organization_core`, `legal_form`) for factors.
As we learned from `ClaimId`, open semantic vocabularies should use typed namespaced identifiers to prevent dataclass field explosion. 
When a plugin later adds `bank_account_identity`, `registry_legal_name`, or `LEI_identity`, the `VendorIdentityInterpretation` object does not need to change.

Canonical Factor IDs for V1:
- `recongraph.vendor.organization_core`
- `recongraph.vendor.legal_form`
- `recongraph.vendor.tax_identity`
- `recongraph.vendor.gst_registration`
- `recongraph.vendor.trade_name`

### Invariants

1. **Canonical Sorting**: The `factors` tuple MUST be canonically sorted by `factor` ID.
2. **Uniqueness**: Duplicate factor IDs within a single `VendorIdentityInterpretation` MUST be rejected at construction.
3. **K6 Compliance**: Each factor's `EvidenceInterpretationResult` follows the full K6 state algebra (empty assertions for non-`INTERPRETED` states, no zero magnitudes, etc.).
4. **Factor Independence**: One factor returning `MISSING_INPUT` does not corrupt or downgrade other factors.
