from recongraph.graph.candidate import CandidateGraphBuilder, build_purchase_urn, build_gst_urn
from recongraph.graph.algorithms import extract_connected_components
from recongraph.graph.hypotheses import Hypothesis

def test_extract_connected_components():
    builder = CandidateGraphBuilder()
    
    p1 = build_purchase_urn("p1")
    p2 = build_purchase_urn("p2")
    g1 = build_gst_urn("g1")
    g2 = build_gst_urn("g2")
    g3 = build_gst_urn("g3")
    
    # Add nodes
    builder.add_node(p1, "P1")
    builder.add_node(p2, "P2")
    builder.add_node(g1, "G1")
    builder.add_node(g2, "G2")
    builder.add_node(g3, "G3")
    
    # Component A: p1 <-> g1, p1 <-> g2
    builder.add_candidate_edge(p1, g1, frozenset(["AMT"]))
    builder.add_candidate_edge(p1, g2, frozenset(["TAX"]))
    
    # Component B: p2 <-> g3
    builder.add_candidate_edge(p2, g3, frozenset(["REF"]))
    
    graph = builder.build()
    
    components = list(extract_connected_components(graph))
    assert len(components) == 2
    
    # Check component A
    comp_a = next(c for c in components if p1 in c.graph.nodes)
    assert set(comp_a.graph.nodes.keys()) == {p1, g1, g2}
    assert comp_a.graph.get_neighbors(p1) == {g1, g2}
    
    # Check component B
    comp_b = next(c for c in components if p2 in c.graph.nodes)
    assert set(comp_b.graph.nodes.keys()) == {p2, g3}
    assert comp_b.graph.get_neighbors(p2) == {g3}

def test_hypothesis_properties():
    h = Hypothesis(
        component_nodes=frozenset(["p1", "g1", "g2"]),
        proposed_edges=frozenset([frozenset(["p1", "g1"])])
    )
    assert h.matched_nodes == frozenset(["p1", "g1"])
    assert h.unmatched_nodes == frozenset(["g2"])
