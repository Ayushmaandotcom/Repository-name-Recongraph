import pytest
from recongraph.domain.semantics.artifact import DerivedEmbeddingArtifactIdentity, SimulatedEmbeddingProvider
from recongraph.domain.semantics.observation import SemanticObservation

def test_semantic_embedding_caching_identity():
    # Identical raw strings should have exactly the same embedding artifact identity.
    desc1 = "OFFICE SUPPLIES"
    desc2 = "OFFICE SUPPLIES"
    
    embed1 = SimulatedEmbeddingProvider.embed(desc1)
    embed2 = SimulatedEmbeddingProvider.embed(desc2)
    
    assert embed1.identity.digest == embed2.identity.digest
    assert embed1.vector == embed2.vector

def test_semantic_embedding_different_strings():
    # Different strings should yield different artifact identities
    embed1 = SimulatedEmbeddingProvider.embed("OFFICE SUPPLIES")
    embed2 = SimulatedEmbeddingProvider.embed("STATIONERY")
    
    assert embed1.identity.digest != embed2.identity.digest

def test_semantic_observation_normalization():
    # The SemanticObservation normalizes text but retains raw text
    obs = SemanticObservation.create("Office Supplies!", SimulatedEmbeddingProvider.embed("Office Supplies!"))
    assert obs.raw_text == "Office Supplies!"
    assert obs.normalized_text == "OFFICE SUPPLIES"
    assert obs.tokens == ("OFFICE", "SUPPLIES")
