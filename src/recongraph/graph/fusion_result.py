from dataclasses import dataclass
from typing import Mapping, List, Set, FrozenSet, TYPE_CHECKING
from recongraph.graph.propagation import PropagationStatus

if TYPE_CHECKING:
    from recongraph.graph.propagation import PropagatedNode

@dataclass(frozen=True)
class FusionResult:
    """
    A descriptive summary of the EvidenceGraph after Semantic Propagation.
    This does NOT compute a final MATCH/REVIEW decision.
    """
    independent_support: frozenset[str]
    derived_support: frozenset[str]
    contradictions: frozenset[str]
    dependency_groups: tuple[frozenset[str], ...]
    missingness: Mapping[str, str]
    propagation_status: Mapping[str, PropagationStatus]
    coverage: float
    
    @classmethod
    def from_propagated_graph(cls, 
                              nodes: Mapping[str, 'PropagatedNode'], 
                              dependency_groups: List[Set[str]],
                              missingness: Mapping[str, str],
                              coverage: float) -> 'FusionResult':
        
        independent = set()
        derived = set()
        contradictions = set()
        status_map = {}
        
        for node_id, p_node in nodes.items():
            status_map[node_id] = p_node.status
            
            if p_node.status == PropagationStatus.CONTRADICTED:
                contradictions.add(node_id)
                
            if p_node.status in (PropagationStatus.UNAFFECTED, PropagationStatus.SUPPORTED):
                if not p_node.derived_support_sources:
                    independent.add(node_id)
                else:
                    derived.add(node_id)
                    
        return cls(
            independent_support=frozenset(independent),
            derived_support=frozenset(derived),
            contradictions=frozenset(contradictions),
            dependency_groups=tuple(frozenset(g) for g in dependency_groups),
            missingness=missingness,
            propagation_status=status_map,
            coverage=coverage
        )
