import pytest
from datetime import date
from decimal import Decimal
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.plugins.core_providers import (
    TaxEvidenceProvider, 
    VendorEvidenceProvider, 
    TemporalEvidenceProvider,
    _weakest_available
)
from recongraph.matching.pair_scorers import PURCHASE_TO_GST_MAX_DAYS

def create_purchase(tax_id=None, vendor_name=None, record_date=date(2024, 1, 1)):
    return PurchaseRecord(
        record_id="p1", 
        vendor_name=vendor_name, 
        reference=None,
        amount=Decimal("100"), 
        record_date=record_date, 
        tax_identity=tax_id, 
        tax_amount=Decimal("10"), 
        tax_rate=Decimal("10")
    )

def create_gst(tax_id=None, vendor_name=None, record_date=date(2024, 1, 1)):
    return GSTRecord(
        record_id="g1", 
        vendor_name=vendor_name, 
        reference=None,
        amount=Decimal("100"), 
        record_date=record_date, 
        tax_identity=tax_id, 
        tax_amount=Decimal("10"), 
        tax_rate=Decimal("10")
    )

def test_equivalent_tax_identities_do_not_produce_a_conflict():
    provider = TaxEvidenceProvider()
    p = create_purchase(tax_id="27ABCDE1234F1Z5")
    g = create_gst(tax_id="27abcde1234f1z5")
    contrib = provider.evaluate([p], [g])
    assert contrib.score == 1.0
    
    p2 = create_purchase(tax_id="27ABCDE1234F1Z5 ")
    contrib2 = provider.evaluate([p2], [g])
    assert contrib2.score == 1.0

def test_genuinely_different_tax_identities_still_conflict():
    provider = TaxEvidenceProvider()
    p = create_purchase(tax_id="27ABCDE1234F1Z5")
    g = create_gst(tax_id="27XXXXX1234F1Z5")
    contrib = provider.evaluate([p], [g])
    assert contrib.score == 0.0
    assert "TAX_IDENTITY_CONFLICT" in contrib.violations

def test_vendor_signal_discriminates_between_matching_and_unrelated_vendors():
    provider = VendorEvidenceProvider()
    
    p = create_purchase(vendor_name="ABC Steel Pvt Ltd")
    g = create_gst(vendor_name="ABC STEELS PVT. LTD.")
    contrib = provider.evaluate([p], [g])
    assert contrib.score > 0.8  
    
    p2 = create_purchase(vendor_name="ABC Steel")
    g2 = create_gst(vendor_name="Zenith Pharma")
    contrib2 = provider.evaluate([p2], [g2])
    assert contrib2.score < 0.2  

def test_group_containing_a_conflicting_tax_identity_conflicts():
    provider = TaxEvidenceProvider()
    p1 = create_purchase(tax_id="27ABC")
    p2 = create_purchase(tax_id="27XYZ")
    g = create_gst(tax_id="27ABC")
    
    contrib = provider.evaluate([p1, p2], [g])
    assert contrib.score == 0.0
    assert "TAX_IDENTITY_CONFLICT" in contrib.violations

def test_vendor_provider_abstains_rather_than_scoring_zero_when_name_absent():
    provider = VendorEvidenceProvider()
    p = create_purchase(vendor_name=None)
    g = create_gst(vendor_name=None)
    contrib = provider.evaluate([p], [g])
    assert contrib.score is None

def test_temporal_window_has_a_single_source_of_truth():
    provider = TemporalEvidenceProvider()
    assert provider.max_days == PURCHASE_TO_GST_MAX_DAYS

def test_weakest_available_reduces_to_the_pairwise_score_for_one_to_one():
    def mock_scorer(a, b):
        return a * b
        
    score = _weakest_available([2], [3], lambda x: x, mock_scorer)
    assert score == 6
