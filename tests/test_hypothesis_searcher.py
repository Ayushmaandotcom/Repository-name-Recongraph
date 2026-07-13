import pytest
from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn, NodeID
from recongraph.graph.algorithms import extract_connected_components
from recongraph.graph.search import HypothesisSearcher

def test_searcher_example_1():
    # P1 --- G1
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher()
    hypotheses = list(searcher.search(component))
    
    assert len(hypotheses) == 2
    edge_sets = {h.proposed_edges for h in hypotheses}
    assert frozenset() in edge_sets
    assert frozenset([frozenset([p1, g1])]) in edge_sets

def test_searcher_example_2():
    # G1 --- P1 --- G2
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    g2 = build_gst_urn("g2")
    
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    builder.add_node(g2, "G2")
    
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p1, g2, frozenset(["TAX"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher()
    hypotheses = list(searcher.search(component))
    
    # 4 structurally distinct sub-graphs
    assert len(hypotheses) == 4

def test_searcher_example_3():
    # P1 --- G1 --- P2
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    p2 = build_purchase_urn("p2")
    g1 = build_gst_urn("g1")
    
    builder.add_node(p1, "P1")
    builder.add_node(p2, "P2")
    builder.add_node(g1, "G1")
    
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p2, g1, frozenset(["TAX"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher()
    hypotheses = list(searcher.search(component))
    
    # 4 structurally distinct sub-graphs
    assert len(hypotheses) == 4

def test_searcher_example_4():
    # P1 (disconnected), G1 (disconnected)
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    
    graph = builder.build()
    components = list(extract_connected_components(graph))
    assert len(components) == 2
    
    searcher = HypothesisSearcher()
    for component in components:
        hypotheses = list(searcher.search(component))
        assert len(hypotheses) == 1
        assert hypotheses[0].proposed_edges == frozenset()

def test_searcher_with_pruning():
    class LimitEdgesValidator:
        def is_valid(self, proposed_edges: frozenset[frozenset[NodeID]]) -> bool:
            return len(proposed_edges) <= 1
            
    # G1 --- P1 --- G2
    builder = CandidateGraphBuilder()
    p1 = build_purchase_urn("p1")
    g1 = build_gst_urn("g1")
    g2 = build_gst_urn("g2")
    
    builder.add_node(p1, "P1")
    builder.add_node(g1, "G1")
    builder.add_node(g2, "G2")
    
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p1, g2, frozenset(["TAX"]))
    
    graph = builder.build()
    component = next(iter(extract_connected_components(graph)))
    
    searcher = HypothesisSearcher(validator=LimitEdgesValidator())
    hypotheses = list(searcher.search(component))
    
    # Should be 3 hypotheses: {}, {P1-G1}, {P1-G2}. The set with 2 edges is pruned.
    assert len(hypotheses) == 3
