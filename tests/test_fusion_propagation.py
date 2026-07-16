import pytest
import time
from recongraph.plugins.provider_v2 import EvidenceContributionV2
from recongraph.graph.fusion import (
    FusionNode, EvidenceGraph, DependencyEdge, 
    ContradictionEdge, CorroborationEdge
)
from recongraph.graph.propagation import SemanticPropagator, TopologicalCycleError, PropagationStatus

def test_graph_serialization_stability():
    contrib_tax = EvidenceContributionV2(provider_name="TAX", score=1.0, interpretation="EXACT")
    contrib_ven = EvidenceContributionV2(provider_name="VENDOR", score=0.9, interpretation="FUZZY")
    
    node_tax = FusionNode.from_contribution(contrib_tax)
    node_ven = FusionNode.from_contribution(contrib_ven)
    dep_edge = DependencyEdge(_source_id=node_tax.node_id, _target_id=node_ven.node_id)
    
    graph = EvidenceGraph()
    graph.add_node(node_tax)
    graph.add_node(node_ven)
    graph.add_edge(dep_edge)
    
    original_identity = graph.identity
    
    # Serialize
    serialized = graph.to_dict()
    
    # Deserialize
    reconstructed = EvidenceGraph.from_dict(serialized)
    
    # Verify stability
    assert reconstructed.identity == original_identity
    assert len(reconstructed.nodes) == 2
    assert len(reconstructed.edges) == 1

def test_duplicate_suppression():
    contrib_tax = EvidenceContributionV2(provider_name="TAX", score=1.0, interpretation="EXACT")
    node_tax = FusionNode.from_contribution(contrib_tax)
    
    graph = EvidenceGraph()
    graph.add_node(node_tax)
    graph.add_node(node_tax) # Should be a no-op
    
    assert len(graph.nodes) == 1

def test_topological_cycle_detection():
    node_a = FusionNode.from_contribution(EvidenceContributionV2(provider_name="A", score=1.0))
    node_b = FusionNode.from_contribution(EvidenceContributionV2(provider_name="B", score=1.0))
    
    graph = EvidenceGraph()
    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_edge(DependencyEdge(_source_id=node_a.node_id, _target_id=node_b.node_id))
    graph.add_edge(DependencyEdge(_source_id=node_b.node_id, _target_id=node_a.node_id))
    
    with pytest.raises(TopologicalCycleError):
        SemanticPropagator.propagate(graph)

def test_contradiction_upstream_propagation():
    """
    If A (TAX) derives B (VENDOR), and C (FINANCIAL) contradicts B, 
    then B is CONTRADICTED, and the veto must propagate upstream to A as QUESTIONED.
    """
    node_tax = FusionNode.from_contribution(EvidenceContributionV2(provider_name="TAX", score=1.0))
    node_ven = FusionNode.from_contribution(EvidenceContributionV2(provider_name="VENDOR", score=0.9))
    node_fin = FusionNode.from_contribution(EvidenceContributionV2(provider_name="FINANCIAL", score=1.0))
    
    graph = EvidenceGraph()
    graph.add_node(node_tax)
    graph.add_node(node_ven)
    graph.add_node(node_fin)
    
    # Tax derives Vendor
    graph.add_edge(DependencyEdge(_source_id=node_tax.node_id, _target_id=node_ven.node_id))
    # Financial contradicts Vendor
    graph.add_edge(ContradictionEdge(node_a=node_fin.node_id, node_b=node_ven.node_id))
    
    propagated = SemanticPropagator.propagate(graph)
    
    assert propagated[node_ven.node_id].status == PropagationStatus.CONTRADICTED
    assert propagated[node_fin.node_id].status == PropagationStatus.CONTRADICTED
    # Upstream propagation: since Vendor was derived from Tax, Tax is QUESTIONED
    assert propagated[node_tax.node_id].status == PropagationStatus.QUESTIONED

def test_derived_support_downstream_propagation():
    node_tax = FusionNode.from_contribution(EvidenceContributionV2(provider_name="TAX", score=1.0))
    node_ven = FusionNode.from_contribution(EvidenceContributionV2(provider_name="VENDOR", score=0.9))
    
    graph = EvidenceGraph()
    graph.add_node(node_tax)
    graph.add_node(node_ven)
    graph.add_edge(DependencyEdge(_source_id=node_tax.node_id, _target_id=node_ven.node_id))
    
    propagated = SemanticPropagator.propagate(graph)
    
    assert node_tax.node_id in propagated[node_ven.node_id].derived_support_sources
    assert len(propagated[node_tax.node_id].derived_support_sources) == 0
    assert propagated[node_ven.node_id].status == PropagationStatus.SUPPORTED

def test_diamond_graph_deduplication():
    """
    A derives B, A derives C.
    B derives D, C derives D.
    Verify D's derived support deduplicates A.
    """
    node_a = FusionNode.from_contribution(EvidenceContributionV2(provider_name="A", score=1.0))
    node_b = FusionNode.from_contribution(EvidenceContributionV2(provider_name="B", score=1.0))
    node_c = FusionNode.from_contribution(EvidenceContributionV2(provider_name="C", score=1.0))
    node_d = FusionNode.from_contribution(EvidenceContributionV2(provider_name="D", score=1.0))

    graph = EvidenceGraph()
    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_node(node_c)
    graph.add_node(node_d)

    graph.add_edge(DependencyEdge(_source_id=node_a.node_id, _target_id=node_b.node_id))
    graph.add_edge(DependencyEdge(_source_id=node_a.node_id, _target_id=node_c.node_id))
    graph.add_edge(DependencyEdge(_source_id=node_b.node_id, _target_id=node_d.node_id))
    graph.add_edge(DependencyEdge(_source_id=node_c.node_id, _target_id=node_d.node_id))

    propagated = SemanticPropagator.propagate(graph)
    
    # D should have A, B, and C exactly once.
    assert len(propagated[node_d.node_id].derived_support_sources) == 3
    assert node_a.node_id in propagated[node_d.node_id].derived_support_sources

def test_multi_hop_termination():
    """
    A -> B -> C -> D -> E
    Check propagation traces correctly through all 5 hops.
    """
    nodes = []
    for i in range(5):
        nodes.append(FusionNode.from_contribution(EvidenceContributionV2(provider_name=f"N{i}", score=1.0)))

    graph = EvidenceGraph()
    for n in nodes:
        graph.add_node(n)
        
    for i in range(4):
        graph.add_edge(DependencyEdge(_source_id=nodes[i].node_id, _target_id=nodes[i+1].node_id))

    propagated = SemanticPropagator.propagate(graph)
    
    # The last node (E) should have all 4 ancestors.
    assert len(propagated[nodes[4].node_id].derived_support_sources) == 4
    assert nodes[0].node_id in propagated[nodes[4].node_id].derived_support_sources

def test_propagation_complexity():
    """
    Create a moderately large graph (500 nodes) with interconnected dependencies.
    Measure time to ensure we aren't O(N^3) or worse.
    """
    graph = EvidenceGraph()
    nodes = []
    for i in range(500):
        n = FusionNode.from_contribution(EvidenceContributionV2(provider_name=f"Node_{i}", score=1.0))
        graph.add_node(n)
        nodes.append(n)
        
    # Create a linear backbone
    for i in range(499):
        graph.add_edge(DependencyEdge(_source_id=nodes[i].node_id, _target_id=nodes[i+1].node_id))
        
    # Add some side branches
    for i in range(0, 490, 10):
        graph.add_edge(DependencyEdge(_source_id=nodes[i].node_id, _target_id=nodes[i+5].node_id))

    start = time.time()
    SemanticPropagator.propagate(graph)
    end = time.time()
    
    # Should easily complete in under 50ms on modern hardware
    assert (end - start) < 0.1
