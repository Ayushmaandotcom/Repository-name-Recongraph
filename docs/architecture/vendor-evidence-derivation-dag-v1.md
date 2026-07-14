# Vendor Evidence Derivation DAG V1

The Vendor Pipeline must be modeled as an explicit directed acyclic graph of observations, derivations, and assertions.

## 1. Vendor Name Branch

```text
       Raw Vendor Name (ObservationOccurrence)
                  │
                  ▼
       Unicode Canonicalization
                  │
                  ▼
         Lexical Tokenization
                  │
                  ▼
       vendor.parse_name.v1 (DerivationOccurrence)
                  │
                  ▼
     Structured Vendor Name (DerivedArtifact)
                  │
         ┌────────┴────────┐
         ▼                 ▼
 Organization Core    Legal Form
 Observation          Observation
         │                 │
         ▼                 ▼
  Core Comparison    Form Comparison (DerivationOccurrence)
         │                 │
         ▼                 ▼
 EvidenceAssertion   EvidenceAssertion
  (same_org_core)    (same_legal_form)
```

## 2. GSTIN Branch

```text
       Raw GSTIN Observation (ObservationOccurrence)
                  │
                  ├───────────────────────┐
                  ▼                       ▼
           GSTIN Validation        PAN Extraction
                  │                       │
           [IF VALID]              [IF VALID]
                  │                       │
                  ▼                       ▼
         GST Registration       Legal Entity Tax
            Comparison         Identity Comparison
                  │                       │
                  ▼                       ▼
          EvidenceAssertion       EvidenceAssertion
      (same_gst_registration)   (same_tax_identity)
```
*Note: If validation fails, the pipeline immediately halts and produces `UNINTERPRETABLE_INPUT` for both factors.*

## 3. Integration Level

All assertions feed into the `VendorIdentityInterpretation` (factorized, NOT fused).

```text
 EvidenceAssertion(same_org_core)
 EvidenceAssertion(same_legal_form)
 EvidenceAssertion(same_gst_registration)
 EvidenceAssertion(same_tax_identity)
                  │
                  ▼
     VendorIdentityInterpretation (Tuple of Factor Results)
                  │
                  ▼
       [STAGE 8J: SEMANTIC FUSION]
                  │
                  ▼
 EvidenceAssertion(same_legal_entity)
```

## CRUCIAL RULE

**Do not directly derive `same_legal_entity` from normalized vendor name similarity.**

Lexical similarity only produces factor-level assertions (`same_organization_core`, `same_legal_form`). Only the Semantic Fusion engine (Stage 8J) is permitted to reason over the ensemble of factors to evaluate legal-entity identity.
