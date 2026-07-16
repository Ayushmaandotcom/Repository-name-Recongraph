from dataclasses import dataclass
from typing import Any
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.graph.decision import DecisionAction, ReconciliationDecision
from recongraph.graph.fusion_explainability import ExplanationArtifact
from recongraph.graph.candidate import CandidateGraph
from recongraph.graph.hypotheses import EvaluatedHypothesis

@dataclass(frozen=True)
class ReviewOutcome:
    """The mutable workflow state owned by the human/AI reviewer."""
    reviewer_id: str
    final_action: str
    comments: str

@dataclass(frozen=True)
class ReviewPacket:
    """An immutable, curated workspace required for a human/AI to resolve a complex decision."""
    packet_id: str
    action: DecisionAction
    purchases: tuple[PurchaseRecord, ...]
    gsts: tuple[GSTRecord, ...]
    explanation: ExplanationArtifact | None
    competitors: tuple[EvaluatedHypothesis, ...]
    checklist: tuple[str, ...]

class ReviewPacketBuilder:
    """Constructs ReviewPackets exclusively for non-automated decisions."""
    
    def __init__(self):
        self._counter = 0
        
    def _generate_checklist(self, explanation: ExplanationArtifact | None) -> tuple[str, ...]:
        checklist = []
        if explanation is None:
            return ("General manual review",)
            
        # Use Layer 3 missingness and contradictions
        contradicted = explanation.technical_details.get("contradicted", [])
        if "TAX_NODE" in contradicted:
            checklist.append("Verify GST tax filing manually")
        if "FINANCIAL_NODE" in contradicted:
            checklist.append("Verify exact invoice amounts and potential split payments")
        if "TEMPORAL_NODE" in contradicted:
            checklist.append("Verify transaction date against posting date")
            
        action_str = explanation.executive_summary.get("decision")
        if action_str == DecisionAction.REVIEW_AMBIGUOUS.value:
            checklist.append("Disambiguate competing hypotheses manually")
            
        if not checklist:
            checklist.append("General manual review")
            
        return tuple(checklist)
        
    def build(
        self, 
        decision: ReconciliationDecision, 
        explanation: ExplanationArtifact | None, 
        graph: CandidateGraph
    ) -> ReviewPacket | None:
        
        if decision.action == DecisionAction.AUTO_MATCH:
            return None
            
        self._counter += 1
        packet_id = f"RP-{self._counter:05d}"
        
        purchases = []
        gsts = []
        
        target_hypothesis = decision.selected_hypothesis
        if not target_hypothesis and decision.competitors:
            target_hypothesis = decision.competitors[0]
            
        if target_hypothesis:
            for urn in target_hypothesis.hypothesis.matched_nodes:
                if urn.startswith("urn:recongraph:purchase:"):
                    purchases.append(graph.nodes[urn])
                elif urn.startswith("urn:recongraph:gst:"):
                    gsts.append(graph.nodes[urn])
                    
        checklist = self._generate_checklist(explanation)
        
        curated_competitors = decision.competitors[:3]
        
        return ReviewPacket(
            packet_id=packet_id,
            action=decision.action,
            purchases=tuple(purchases),
            gsts=tuple(gsts),
            explanation=explanation,
            competitors=curated_competitors,
            checklist=checklist
        )

    def build_leftover(self, unmatched_nodes: frozenset[str], graph: CandidateGraph) -> ReviewPacket | None:
        if not unmatched_nodes:
            return None
            
        self._counter += 1
        packet_id = f"RP-{self._counter:05d}"
        
        purchases = []
        gsts = []
        
        for urn in unmatched_nodes:
            if urn.startswith("urn:recongraph:purchase:"):
                purchases.append(graph.nodes[urn])
            elif urn.startswith("urn:recongraph:gst:"):
                gsts.append(graph.nodes[urn])
                
        if not purchases and not gsts:
            return None
            
        return ReviewPacket(
            packet_id=packet_id,
            action=DecisionAction.REVIEW_INSUFFICIENT_EVIDENCE,
            purchases=tuple(purchases),
            gsts=tuple(gsts),
            explanation=None,
            competitors=(),
            checklist=("Review unmatched records left over from an auto-match component",)
        )
