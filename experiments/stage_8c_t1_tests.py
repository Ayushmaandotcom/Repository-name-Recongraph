import sys
from recongraph.matching.signals import tax_identity_score
from recongraph.normalization.text import normalize_tax_identity
from recongraph.domain.records import PurchaseRecord, GSTRecord
from datetime import date
from decimal import Decimal
from recongraph.engine import ReconGraphEngine
from recongraph.config import ReconGraphConfig
from recongraph.plugins.core_providers import FinancialEvidenceProvider, TemporalEvidenceProvider, TaxEvidenceProvider, VendorEvidenceProvider, ReferenceEvidenceProvider
from recongraph.matching.reference_evidence import ReferenceCorpusProfile, ReferenceEvidenceContext, ReferenceEvidencePolicy
from recongraph.domain.vendor.context import VendorIdentityContext, VendorCorpusProfile

def _get_engine():
    config = ReconGraphConfig()
    corpus_profile = ReferenceCorpusProfile(reference_count=0, normalized_reference_frequency={}, numeric_token_document_frequency={})
    ctx = VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0.0", fuzzy_minimum_length=6, fuzzy_threshold=0.85, distinctiveness_threshold=0.01
    )
    providers = [
        FinancialEvidenceProvider(), 
        TemporalEvidenceProvider(), 
        TaxEvidenceProvider(),
        VendorEvidenceProvider(ctx),
        ReferenceEvidenceProvider(ReferenceEvidenceContext(corpus_profile, ReferenceEvidencePolicy()))
    ]
    return ReconGraphEngine(config, providers)

def test_states():
    cases = [
        ("STATE-001", None, None),
        ("STATE-002", None, "27AAAAA0000A1Z5"),
        ("STATE-003", "27AAAAA0000A1Z5", None),
        ("STATE-004", "MALFORMED1", "MALFORMED2"),
        ("STATE-005", "MALFORMED1", "27AAAAA0000A1Z5"),
        ("STATE-006", "27AAAAA0000A1Z5", "MALFORMED1"),
        ("STATE-007", "27AAAAA0000A1Z5", "07AAAAA0000A1Z5"),
        ("STATE-008", "MALFORMED", "MALFORMED"),
        ("STATE-009", "   ", "   "),
        ("STATE-010", "UNKNOWN", "UNKNOWN"),
        ("STATE-011", "N/A", "N/A"),
        ("STATE-012", "27AAAAAOOOOA1Z5", "27AAAAAOOOOA1Z5"),
    ]
    for name, left, right in cases:
        score = tax_identity_score(left, right)
        print(f"{name}: {left} vs {right} -> {score}")

def test_mutations():
    base = "27AAAAA0000A1Z5"
    mutations = [
        ("O <-> 0", "27AAAAAOOOOA1Z5"),
        ("I <-> 1", "27AAAAA0000AIZ5"),
        ("B <-> 8", "27AAAAA0000A8Z5"),
        ("S <-> 5", "27AAAAA0000A1ZS"),
    ]
    for name, mut in mutations:
        score = tax_identity_score(base, mut)
        print(f"MUTATION {name}: {base} vs {mut} -> {score}")

def test_integration():
    engine = _get_engine()
    print("\n--- E2E: DIFFERENT PAN (in GSTIN) ---")
    p1 = PurchaseRecord("p1", amount=Decimal(100), record_date=date(2023,1,1), reference="INV1", vendor_name="Vendor", tax_identity="27AAAAA0000A1Z5")
    g1 = GSTRecord("g1", amount=Decimal(100), record_date=date(2023,1,1), reference="INV1", vendor_name="Vendor", tax_identity="27BBBBB0000B1Z5")
    res1 = engine.reconcile([p1], [g1])
    for trace in res1.traces:
        d = trace.events[0].payload
        print(f"DECISION: {d.action}, h_score: {d.selected_hypothesis.score if d.selected_hypothesis else 'None'}")

    print("\n--- E2E: DIFFERENT EVENT ---")
    p2 = PurchaseRecord("p2", amount=Decimal(100), record_date=date(2023,1,1), reference="INV1", vendor_name="Vendor", tax_identity="27AAAAA0000A1Z5")
    g2 = GSTRecord("g2", amount=Decimal(500), record_date=date(2023,5,5), reference="INV99", vendor_name="Vendor", tax_identity="27AAAAA0000A1Z5")
    res2 = engine.reconcile([p2], [g2])
    for trace in res2.traces:
        d = trace.events[0].payload
        h = d.selected_hypothesis
        if h:
            print(f"DECISION: {d.action}, h_score: {h.score}, coverage: {h.coverage}")
            print(f"FINDINGS: {[f.value for f in h.semantic_findings]}")
        else:
            print(f"DECISION: {d.action}")

if __name__ == "__main__":
    with open("challenge_out.txt", "w") as f:
        sys.stdout = f
        test_states()
        test_mutations()
        test_integration()
        sys.stdout = sys.__stdout__
