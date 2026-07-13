from collections.abc import Iterable
from recongraph.graph.candidate import CandidateGraph, NodeID
from recongraph.graph.hypotheses import ConnectedComponent

def extract_connected_components(graph: CandidateGraph) -> Iterable[ConnectedComponent]:
    """
    Extracts isolated subgraphs from the candidate graph using Breadth-First Search (BFS).
    Enforces deterministic extraction order (GI-006).
    """
    visited: set[NodeID] = set()
    
    # Sort node keys to guarantee GI-006 (Deterministic Iteration)
    for start_node in sorted(graph.nodes.keys()):
        if start_node in visited:
            continue
            
        component_nodes: set[NodeID] = set()
        queue = [start_node]
        
        while queue:
            current = queue.pop(0)
            if current in component_nodes:
                continue
                
            component_nodes.add(current)
            visited.add(current)
            
            for neighbor in sorted(graph.get_neighbors(current)):
                if neighbor not in visited:
                    queue.append(neighbor)
                    
        # Construct the isolated CandidateGraph for this component
        sub_nodes = {n: graph.nodes[n] for n in component_nodes}
        sub_adjacency = {n: graph.get_neighbors(n) for n in component_nodes}
        
        sub_edges = {}
        for u in component_nodes:
            for v in graph.get_neighbors(u):
                edge_key = frozenset([u, v])
                if edge_key not in sub_edges:
                    payload = graph.get_edge_payload(u, v)
                    if payload is not None:
                        sub_edges[edge_key] = payload
                    
        sub_graph = CandidateGraph(
            nodes=sub_nodes,
            adjacency=sub_adjacency,
            edges=sub_edges
        )
        
        yield ConnectedComponent(graph=sub_graph)
