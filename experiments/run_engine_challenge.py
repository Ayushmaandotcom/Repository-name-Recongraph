from recongraph.config import ReconGraphConfig
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TemporalEvidenceProvider, TaxEvidenceProvider, VendorEvidenceProvider, ReferenceEvidenceProvider
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, ReferenceEvidenceContext, ReferenceEvidencePolicy
from recongraph.domain.vendor.context import VendorIdentityContext, VendorCorpusProfile

def _get_vendor_context():
    return VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )

import csv
from pathlib import Path
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.engine import ReconGraphEngine
from datetime import date
from decimal import Decimal

def optional_text(value: str) -> str | None:
    stripped = value.strip()
    return stripped or None

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHALLENGE_DIR = PROJECT_ROOT / "datasets" / "challenge"

def main():
    purchases = []
    with (CHALLENGE_DIR / "purchase_register_v1.csv").open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            purchases.append(PurchaseRecord(
                record_id=row["record_id"],
                vendor_name=optional_text(row["vendor_name"]),
                reference=optional_text(row["invoice_number"]),
                amount=Decimal(row["amount"]),
                record_date=date.fromisoformat(row["invoice_date"]),
                tax_identity=optional_text(row["gstin"]),
            ))
            
    gst_records = []
    with (CHALLENGE_DIR / "gst_records_v1.csv").open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gst_records.append(GSTRecord(
                record_id=row["record_id"],
                vendor_name=optional_text(row["supplier_name"]),
                reference=optional_text(row["invoice_number"]),
                amount=Decimal(row["amount"]),
                record_date=date.fromisoformat(row["invoice_date"]),
                tax_identity=optional_text(row["gstin"]),
            ))
            
    from recongraph.config import ReconGraphConfig
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TemporalEvidenceProvider, TaxEvidenceProvider, VendorEvidenceProvider, ReferenceEvidenceProvider
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, ReferenceEvidenceContext, ReferenceEvidencePolicy
from recongraph.domain.vendor.context import VendorIdentityContext, VendorCorpusProfile

def _get_vendor_context():
    return VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )

    config = ReconGraphConfig()
    corpus_profile = ReferenceCorpusProfile(
        reference_count=1,
        normalized_reference_frequency={},
        numeric_token_document_frequency={}
    )
    providers = [
        FinancialEvidenceProvider(), 
        TemporalEvidenceProvider(), 
        TaxEvidenceProvider(),
        VendorEvidenceProvider(_get_vendor_context()),
        ReferenceEvidenceProvider(ReferenceEvidenceContext(corpus_profile, ReferenceEvidencePolicy()))
    ]
    engine = ReconGraphEngine(config, providers)
    result = engine.reconcile(purchases, gst_records)
    
    print(f"Total Decisions: {len(result.decisions)}")
    
    # We want to specifically check HN001 or any severe amount conflict
    for d in result.decisions:
        # We can just print the decisions for HN001 pairs if we know the IDs
        print(f"Decision: {d.action}, Rationale: {d.rationale}")
        if d.selected_hypothesis:
            h = d.selected_hypothesis
            signals = h.supporting_evidence.get('signals', {})
            metadata = h.supporting_evidence.get('metadata', {})
            amount_interp = metadata.get('AMOUNT', {}).get('interpretation')
            amount_proj = metadata.get('AMOUNT', {}).get('projection')
            print(f"  Score: {h.score}, Cov: {h.relationship.coverage}")
            print(f"  Findings: {[f.value for f in h.semantic_findings]}")
            if amount_interp:
                print(f"  Amount Interp: {amount_interp.relationship.value}, Diff: {amount_interp.absolute_difference}")
            if amount_proj:
                print(f"  Amount Proj: {amount_proj.similarity}")
            
if __name__ == "__main__":
    main()
