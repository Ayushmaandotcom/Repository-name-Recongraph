import pytest
from decimal import Decimal
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.domain.semantics.claims import SAME_BUSINESS_PURPOSE_CLAIM
from recongraph.domain.assertions import AssertionPolarity
from recongraph.plugins.semantic_providers import SemanticEvidenceProvider

def test_semantic_provider_support():
    provider = SemanticEvidenceProvider()
    
    p = PurchaseRecord(
        record_id="p1", vendor_name="A", reference="1", amount=Decimal("100"), 
        record_date=date(2023,1,1), tax_identity="T", description="OFFICE SUPPLIES"
    )
    g = GSTRecord(
        record_id="g1", vendor_name="A", reference="1", amount=Decimal("100"), 
        record_date=date(2023,1,1), tax_identity="T", description="STATIONERY"
    )
    
    pipeline = provider.get_pipeline()
    extraction = pipeline.extract([p], [g])
    interpretation = pipeline.interpret(extraction)
    contribution = pipeline.contribute(interpretation)
    
    assert contribution.score == 1.0
    assert len(contribution.violations) == 0
    
    assertions = contribution.metadata["assertions"]
    assert len(assertions) == 1
    
    assertion = assertions[0]
    assert assertion.proposition.claim == SAME_BUSINESS_PURPOSE_CLAIM
    assert assertion.polarity == AssertionPolarity.SUPPORT
    assert assertion.magnitude > 0.9

def test_semantic_provider_conflict():
    provider = SemanticEvidenceProvider()
    
    p = PurchaseRecord(
        record_id="p1", vendor_name="A", reference="1", amount=Decimal("100"), 
        record_date=date(2023,1,1), tax_identity="T", description="LAPTOP"
    )
    g = GSTRecord(
        record_id="g1", vendor_name="A", reference="1", amount=Decimal("100"), 
        record_date=date(2023,1,1), tax_identity="T", description="PLUMBING"
    )
    
    pipeline = provider.get_pipeline()
    extraction = pipeline.extract([p], [g])
    interpretation = pipeline.interpret(extraction)
    contribution = pipeline.contribute(interpretation)
    
    assert contribution.score == 0.0
    assert "SEMANTIC_PURPOSE_CONTRADICTION" in contribution.violations
    
    assertions = contribution.metadata["assertions"]
    assert len(assertions) == 1
    
    assertion = assertions[0]
    assert assertion.proposition.claim == SAME_BUSINESS_PURPOSE_CLAIM
    assert assertion.polarity == AssertionPolarity.CONFLICT
    
def test_semantic_cross_model_drift_protection():
    from recongraph.domain.semantics.interpretation import SemanticPairInterpreter
    from recongraph.domain.semantics.observation import SemanticObservation
    from recongraph.domain.semantics.artifact import DerivedEmbeddingArtifact, EmbeddingProviderIdentity
    
    id1 = EmbeddingProviderIdentity("test", "model1", "1")
    id2 = EmbeddingProviderIdentity("test", "model2", "1")
    
    art1 = DerivedEmbeddingArtifact(id1, "A", (1.0, 0.0))
    art2 = DerivedEmbeddingArtifact(id2, "A", (1.0, 0.0))
    
    obs1 = SemanticObservation.create("A", art1)
    obs2 = SemanticObservation.create("A", art2)
    
    with pytest.raises(ValueError, match="Cross-model semantic interpretation is invalid"):
        SemanticPairInterpreter.interpret(obs1, obs2)
