from dataclasses import dataclass
from typing import Generic, TypeVar
from recongraph.graph.candidate import NodeID, CandidateGraph

@dataclass(frozen=True)
class ConnectedComponent:
    """
    An isolated subgraph extracted from the CandidateGraph.
    Represents a mathematically independent search space.
    """
    graph: CandidateGraph
    # We maintain a reference to the global graph structure but scoped down.
    # The CandidateGraph class already enforces immutability.

@dataclass(frozen=True)
class Hypothesis:
    """
    An immutable proposed resolution claiming to settle a specific subset
    of records within a connected component.
    """
    component_nodes: frozenset[NodeID]
    proposed_edges: frozenset[frozenset[NodeID]]
    
    @property
    def matched_nodes(self) -> frozenset[NodeID]:
        return frozenset(n for edge in self.proposed_edges for n in edge)
        
    @property
    def unmatched_nodes(self) -> frozenset[NodeID]:
        return self.component_nodes - self.matched_nodes
