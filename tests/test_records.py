import pytest
from decimal import Decimal
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord

def test_purchase_record_description():
    p = PurchaseRecord(
        record_id="p1", amount=Decimal("100.0"), record_date=date(2023,1,1),
        reference="INV1", vendor_name="A", tax_identity="TAX1", description="OFFICE SUPPLIES"
    )
    assert p.description == "OFFICE SUPPLIES"

def test_gst_record_description():
    g = GSTRecord(
        record_id="g1", amount=Decimal("100.0"), record_date=date(2023,1,1),
        reference="INV1", vendor_name="A", tax_identity="TAX1", description="STATIONERY"
    )
    assert g.description == "STATIONERY"
