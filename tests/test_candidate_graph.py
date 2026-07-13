import pytest
from recongraph.graph.candidate import (
    CandidateGraphBuilder,
    build_purchase_urn,
    build_gst_urn
)
from recongraph.domain.records import PurchaseRecord, GSTRecord
from datetime import date

def test_candidate_graph_builder_deduplicates_edges():
    builder = CandidateGraphBuilder()
    
    p_id = build_purchase_urn("p1")
    g_id = build_gst_urn("g1")
    
    p = PurchaseRecord(record_id="p1", vendor_name="A", reference="R", amount=1.0, record_date=date(2026,1,1), tax_identity="T")
    g = GSTRecord(record_id="g1", vendor_name="A", reference="R", amount=1.0, record_date=date(2026,1,1), tax_identity="T")
    
    builder.add_node(p_id, p)
    builder.add_node(g_id, g)
    
    # Add identical edge twice from different blocking paths
    builder.add_candidate_edge(p_id, g_id, frozenset(["AMT:1.0"]))
    builder.add_candidate_edge(p_id, g_id, frozenset(["TAX:T"]))
    
    graph = builder.build()
    
    # Topology check
    assert graph.get_neighbors(p_id) == frozenset([g_id])
    assert graph.get_neighbors(g_id) == frozenset([p_id])
    
    # Deduplication check
    payload = graph.get_edge_payload(p_id, g_id)
    assert payload is not None
    assert payload.shared_blocking_keys == frozenset(["AMT:1.0", "TAX:T"])
    
    # Undirected check
    payload2 = graph.get_edge_payload(g_id, p_id)
    assert payload2 is payload

def test_candidate_graph_forbids_self_loops():
    builder = CandidateGraphBuilder()
    p_id = build_purchase_urn("p1")
    p = PurchaseRecord(record_id="p1", vendor_name="A", reference="R", amount=1.0, record_date=date(2026,1,1), tax_identity="T")
    builder.add_node(p_id, p)
    
    builder.add_candidate_edge(p_id, p_id, frozenset(["AMT:1.0"]))
    
    graph = builder.build()
    assert graph.get_neighbors(p_id) == frozenset()
    assert graph.get_edge_payload(p_id, p_id) is None

def test_candidate_graph_enforces_closed_world():
    builder = CandidateGraphBuilder()
    p_id = build_purchase_urn("p1")
    g_id = build_gst_urn("g1")
    
    # Add edge, but DON'T add nodes
    builder.add_candidate_edge(p_id, g_id, frozenset(["AMT:1.0"]))
    
    with pytest.raises(ValueError, match="GI-001 Violation"):
        builder.build()

def test_candidate_graph_is_immutable():
    builder = CandidateGraphBuilder()
    p_id = build_purchase_urn("p1")
    g_id = build_gst_urn("g1")
    
    builder.add_node(p_id, None)
    builder.add_node(g_id, None)
    builder.add_candidate_edge(p_id, g_id, frozenset(["AMT:1.0"]))
    
    graph = builder.build()
    
    with pytest.raises(TypeError):
        # Attempt to mutate mapping proxy
        graph.nodes[p_id] = "mutated"
        
    with pytest.raises(AttributeError):
        # Attempt to mutate adjacency
        graph.get_neighbors(p_id).add("fake")
