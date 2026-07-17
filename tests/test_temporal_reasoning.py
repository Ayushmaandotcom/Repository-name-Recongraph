import pytest
from datetime import date
from decimal import Decimal

from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.domain.temporal.artifact import TemporalArtifact
from recongraph.domain.temporal.factors import TemporalRelationState
from recongraph.domain.temporal.interpretation import TemporalPairInterpreter
from recongraph.plugins.core_providers import TemporalEvidenceProvider

def test_cross_period_late_filing_support():
    # Invoice created on March 25, 2023, filed in April 2023 (1 month late filing)
    p_art = TemporalArtifact.create(date(2023, 3, 25), "2023-04")
    g_art = TemporalArtifact.create(date(2023, 3, 26), "2023-04")
    
    interp = TemporalPairInterpreter.interpret(p_art, g_art, max_days=7)
    assert interp.relation.state == TemporalRelationState.WITHIN_TOLERANCE
    assert interp.relation.day_difference == 1
    assert interp.relation.period_difference == 0
    
    # What if it's a cross-period (Invoice March 25, GST filed in May, but date is April)
    p_art2 = TemporalArtifact.create(date(2023, 3, 25), "2023-03")
    g_art2 = TemporalArtifact.create(date(2023, 3, 27), "2023-04")
    
    interp2 = TemporalPairInterpreter.interpret(p_art2, g_art2, max_days=7)
    assert interp2.relation.state == TemporalRelationState.LATE_FILING
    assert interp2.relation.period_difference == -1

def test_temporal_decay_function():
    p_art = TemporalArtifact.create(date(2023, 3, 20), "2023-03")
    g_art = TemporalArtifact.create(date(2023, 3, 25), "2023-03")
    interp = TemporalPairInterpreter.interpret(p_art, g_art, max_days=10)
    
    assert interp.relation.state == TemporalRelationState.WITHIN_TOLERANCE
    assert interp.relation.day_difference == 5
    
    # 5 days out of 10 max days should be a decay score of 0.5
    from recongraph.domain.temporal.projection import TemporalV1ProjectionContract
    proj = TemporalV1ProjectionContract.project((interp,))
    assert proj.score == 0.5

def test_k6_temporal_assertions():
    provider = TemporalEvidenceProvider(max_days=7)
    p = PurchaseRecord(
        record_id="p1", vendor_name="V1", reference="1", amount=Decimal("100"),
        record_date=date(2023, 3, 25), tax_identity="T", filing_period="2023-03"
    )
    g = GSTRecord(
        record_id="g1", vendor_name="V1", reference="1", amount=Decimal("100"),
        record_date=date(2023, 3, 26), tax_identity="T", filing_period="2023-04"
    )
    
    contrib = provider.evaluate([p], [g])
    assert contrib.provider_name == "temporal"
    assert "assertions" in contrib.metadata
    
    assertions = contrib.metadata["assertions"]
    assert len(assertions) == 1
    assertion = assertions[0]
    
    # State was LATE_FILING, so it should generate valid_late_filing claim
    assert assertion.proposition.claim.claim_id.value == "temporal.valid_late_filing"
    assert assertion.polarity.value == "support"
