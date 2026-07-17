import pytest
from datetime import date
from decimal import Decimal

from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.domain.vendor.context import VendorIdentityContext
from recongraph.domain.vendor.knowledge import OrganizationalKnowledgeBase
from recongraph.plugins.core_providers import VendorEvidenceProvider

def test_vendor_evidence_assertions():
    # Exactly matching vendor names, so Lexical match -> ALIAS_MATCH (SUPPORT)
    # No GSTINs/PANs provided, so no legal/tax match.
    
    p1 = PurchaseRecord(
        record_id="p1", vendor_name="Acme Corp PVT LTD", reference="1", 
        amount=Decimal("100"), record_date=date(2023,1,1),
        tax_identity=None, net_amount=None, tax_amount=None, tax_rate=None
    )
    g1 = GSTRecord(
        record_id="g1", vendor_name="Acme Corp PVT LTD", reference="1", 
        amount=Decimal("100"), record_date=date(2023,1,1),
        tax_identity=None, net_amount=None, tax_amount=None, tax_rate=None
    )
    
    context = VendorIdentityContext(
        corpus_profile=None,
        knowledge_base=OrganizationalKnowledgeBase.empty()
    )
    
    provider = VendorEvidenceProvider(context=context)
    contrib = provider.evaluate([p1], [g1])
    
    assertions = contrib.metadata.get("assertions", tuple())
    
    # Expecting 2 support assertions: alias_match and same_economic_entity (KNOWN_ALIAS)
    assert len(assertions) == 2
    
    a1 = assertions[0]
    assert a1.proposition.claim.claim_id.value == "vendor.alias_match"
    assert a1.polarity.value == "support"
    
    a2 = assertions[1]
    assert a2.proposition.claim.claim_id.value == "vendor.same_economic_entity"
    assert a2.polarity.value == "support"

def test_vendor_evidence_conflict_assertions():
    # Completely different names, expecting ALIAS_MATCH (CONFLICT)
    p1 = PurchaseRecord(
        record_id="p1", vendor_name="Acme Corp PVT LTD", reference="1", 
        amount=Decimal("100"), record_date=date(2023,1,1),
        tax_identity=None, net_amount=None, tax_amount=None, tax_rate=None
    )
    g1 = GSTRecord(
        record_id="g1", vendor_name="Globex Inc", reference="1", 
        amount=Decimal("100"), record_date=date(2023,1,1),
        tax_identity=None, net_amount=None, tax_amount=None, tax_rate=None
    )
    
    context = VendorIdentityContext(
        corpus_profile=None,
        knowledge_base=OrganizationalKnowledgeBase.empty()
    )
    
    provider = VendorEvidenceProvider(context=context)
    contrib = provider.evaluate([p1], [g1])
    
    assertions = contrib.metadata.get("assertions", tuple())
    
    assert len(assertions) == 1
    a1 = assertions[0]
    assert a1.proposition.claim.claim_id.value == "vendor.alias_match"
    assert a1.polarity.value == "conflict"
