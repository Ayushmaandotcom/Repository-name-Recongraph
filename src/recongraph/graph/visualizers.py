from recongraph.graph.fusion_explainability import (
    ExplanationArtifact,
    TraceExplanation,
    DecisionExplanation,
    FusionExplanation,
    PropagationExplanation,
    ContributionExplanation
)

class MermaidExporter:
    """
    Exports a deterministic ExplanationArtifact to a visual Mermaid graph.
    """
    
    def export(self, artifact: ExplanationArtifact) -> str:
        lines = ["graph TD"]
        
        # We group by component for cleaner visualization
        trace_nodes = []
        decision_nodes = []
        fusion_nodes = []
        propagation_nodes = []
        contribution_nodes = []
        
        for node_id, node in artifact.audit_nodes.items():
            if isinstance(node, TraceExplanation):
                trace_nodes.append(node)
            elif isinstance(node, DecisionExplanation):
                decision_nodes.append(node)
            elif isinstance(node, FusionExplanation):
                fusion_nodes.append(node)
            elif isinstance(node, PropagationExplanation):
                propagation_nodes.append(node)
            elif isinstance(node, ContributionExplanation):
                contribution_nodes.append(node)
                
        # Subgraph: Contributions
        lines.append("    subgraph Evidence Contributions")
        for node in contribution_nodes:
            label = f"{node.provider_name}<br>Score: {node.score}"
            lines.append(f'        {node.node_id}["{label}"]')
        lines.append("    end")
        
        # Subgraph: Propagation
        lines.append("    subgraph Semantic Propagation")
        for node in propagation_nodes:
            label = f"Status: {node.status}"
            lines.append(f'        {node.node_id}["{label}"]')
        lines.append("    end")
        
        # Engine Logic
        for node in fusion_nodes:
            label = f"Fusion Engine<br>Independent: {node.independent_support}<br>Contradictions: {node.contradictions}"
            lines.append(f'    {node.node_id}{{"{label}"}}')
            
        for node in decision_nodes:
            label = f"Decision: {node.action}"
            lines.append(f'    {node.node_id}(("{label}"))')
            
        for node in trace_nodes:
            label = f"Trace ID: {node.identity_hash[:8]}"
            lines.append(f'    {node.node_id}["{label}"]')
            
        # Draw edges
        for node_id, node in artifact.audit_nodes.items():
            for dep in node.dependencies:
                lines.append(f"    {dep} --> {node_id}")
                
        return "\n".join(lines)
