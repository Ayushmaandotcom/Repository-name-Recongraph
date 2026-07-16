import pytest
from recongraph.graph.fusion import FusionNode, EvidenceGraph, DependencyEdge, ContradictionEdge
from recongraph.plugins.provider_v2 import EvidenceContributionV2

def test_fusion_node_determinism():
    contrib1 = EvidenceContributionV2(
        provider_name="TAX_IDENTITY",
        score=1.0,
        metadata={},
        interpretation="GSTIN_EXACT_MATCH"
    )
    
    contrib2 = EvidenceContributionV2(
        provider_name="TAX_IDENTITY",
        score=1.0,
        metadata={},
        interpretation="GSTIN_EXACT_MATCH"
    )
    
    node1 = FusionNode.from_contribution(contrib1)
    node2 = FusionNode.from_contribution(contrib2)
    
    # Deterministic hashing ensures identical evidence produces the same node ID
    assert node1.node_id == node2.node_id
    
def test_fusion_node_distinct():
    contrib1 = EvidenceContributionV2(
        provider_name="TAX_IDENTITY",
        score=1.0,
        metadata={},
        interpretation="GSTIN_EXACT_MATCH"
    )
    
    contrib2 = EvidenceContributionV2(
        provider_name="VENDOR_IDENTITY",
        score=1.0,
        metadata={},
        interpretation="GSTIN_EXACT_MATCH"
    )
    
    node1 = FusionNode.from_contribution(contrib1)
    node2 = FusionNode.from_contribution(contrib2)
    
    assert node1.node_id != node2.node_id

def test_evidence_graph_permutation_invariance():
    contrib_tax = EvidenceContributionV2(provider_name="TAX", score=1.0, interpretation="EXACT")
    contrib_ven = EvidenceContributionV2(provider_name="VENDOR", score=0.9, interpretation="FUZZY")
    contrib_fin = EvidenceContributionV2(provider_name="FINANCIAL", score=1.0, interpretation="EXACT")
    
    node_tax = FusionNode.from_contribution(contrib_tax)
    node_ven = FusionNode.from_contribution(contrib_ven)
    node_fin = FusionNode.from_contribution(contrib_fin)
    
    # Tax derives Vendor
    dep_edge = DependencyEdge(_source_id=node_tax.node_id, _target_id=node_ven.node_id)
    # Tax contradicts Financial (example)
    con_edge = ContradictionEdge(node_a=node_tax.node_id, node_b=node_fin.node_id)
    
    # Graph A (Insertion order 1)
    graph_a = EvidenceGraph()
    graph_a.add_node(node_tax)
    graph_a.add_node(node_ven)
    graph_a.add_node(node_fin)
    graph_a.add_edge(dep_edge)
    graph_a.add_edge(con_edge)
    
    # Graph B (Insertion order 2)
    graph_b = EvidenceGraph()
    graph_b.add_node(node_fin)
    graph_b.add_node(node_tax)
    graph_b.add_node(node_ven)
    graph_b.add_edge(con_edge)
    graph_b.add_edge(dep_edge)
    
    assert graph_a.identity == graph_b.identity
    assert len(graph_a.nodes) == 3
    assert len(graph_a.edges) == 2

def test_evidence_graph_missing_node_edge():
    node = FusionNode.from_contribution(EvidenceContributionV2(provider_name="TAX", score=1.0, interpretation="X"))
    graph = EvidenceGraph()
    
    with pytest.raises(ValueError, match="Cannot add edge"):
        # Target node not in graph
        graph.add_edge(DependencyEdge(_source_id=node.node_id, _target_id="fake_id"))
