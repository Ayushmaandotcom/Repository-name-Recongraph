from typing import Any
from dataclasses import dataclass
from enum import Enum
from recongraph.graph.decision import DecisionAction

class DifferenceType(Enum):
    EQUIVALENT = "EQUIVALENT"
    EXPECTED_IMPROVEMENT = "EXPECTED_IMPROVEMENT"
    REGRESSION = "REGRESSION"
    UNKNOWN = "UNKNOWN"
    POLICY_DIFFERENCE = "POLICY_DIFFERENCE"
    BUG = "BUG"

@dataclass(frozen=True)
class DifferentialResult:
    legacy_decision: DecisionAction
    fusion_decision: DecisionAction
    agreement: bool
    classification: DifferenceType
    performance_metrics: dict[str, float]
    legacy_explanation: dict[str, Any] | None = None
    fusion_explanation: dict[str, Any] | None = None
    
    @classmethod
    def classify(cls, 
                 legacy: DecisionAction, 
                 fusion: DecisionAction, 
                 perf: dict[str, float],
                 legacy_exp: dict[str, Any] | None = None,
                 fusion_exp: dict[str, Any] | None = None) -> 'DifferentialResult':
        agreement = (legacy == fusion)
        
        if agreement:
            classification = DifferenceType.EQUIVALENT
        else:
            # Example heuristic rules for classifying divergences in SHADOW mode
            if legacy == DecisionAction.REVIEW_AMBIGUOUS and fusion == DecisionAction.NO_MATCH:
                classification = DifferenceType.EXPECTED_IMPROVEMENT
                
            # If Legacy rejected it, but Fusion wants human review
            # This is technically an improvement in recall but regression in precision. 
            # We flag it as an unexpected regression to force human review of the graph rules.
            elif legacy == DecisionAction.NO_MATCH and fusion == DecisionAction.REVIEW_AMBIGUOUS:
                # Legacy matched, but graph detected a contradiction
                classification = DifferenceType.EXPECTED_IMPROVEMENT
            elif legacy == DecisionAction.NO_MATCH and fusion == DecisionAction.REVIEW_AMBIGUOUS:
                classification = DifferenceType.POLICY_DIFFERENCE
            else:
                classification = DifferenceType.UNKNOWN
                
        return cls(
            legacy_decision=legacy,
            fusion_decision=fusion,
            agreement=agreement,
            classification=classification,
            performance_metrics=perf,
            legacy_explanation=legacy_exp,
            fusion_explanation=fusion_exp
        )
