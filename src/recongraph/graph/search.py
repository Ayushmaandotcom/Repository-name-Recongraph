from typing import Protocol, Iterable
from recongraph.graph.candidate import NodeID
from recongraph.graph.hypotheses import ConnectedComponent, Hypothesis

class StructuralValidator(Protocol):
    """
    Protocol for pruning invalid branches during hypothesis exploration.
    This interface abstracts business logic away from the searcher.
    """
    def is_valid(self, proposed_edges: frozenset[frozenset[NodeID]]) -> bool:
        ...

class TrivialValidator:
    """A default validator that permits the entire power set of edges."""
    def is_valid(self, proposed_edges: frozenset[frozenset[NodeID]]) -> bool:
        return True

class HypothesisSearcher:
    """
    Explores a connected component to generate structurally valid hypotheses.
    Utilizes recursive backtracking and an injectable validator to prevent
    combinatorial explosion without understanding domain semantics.
    """
    def __init__(self, validator: StructuralValidator | None = None):
        self.validator = validator or TrivialValidator()

    def search(self, component: ConnectedComponent) -> Iterable[Hypothesis]:
        # Extract edges and sort them to guarantee deterministic exploration (HS-002)
        edges = list(component.graph.edges.keys())
        edges.sort(key=lambda e: tuple(sorted(list(e))))
        
        component_nodes = frozenset(component.graph.nodes.keys())
        
        def backtrack(index: int, current_selection: set[frozenset[NodeID]]) -> Iterable[Hypothesis]:
            # Prune branches that violate structural constraints
            if not self.validator.is_valid(frozenset(current_selection)):
                return
                
            if index == len(edges):
                yield Hypothesis(
                    component_nodes=component_nodes,
                    proposed_edges=frozenset(current_selection)
                )
                return
                
            # Branch 1: Exclude the edge at current index
            yield from backtrack(index + 1, current_selection)
            
            # Branch 2: Include the edge at current index
            current_selection.add(edges[index])
            yield from backtrack(index + 1, current_selection)
            current_selection.remove(edges[index])
            
        yield from backtrack(0, set())
