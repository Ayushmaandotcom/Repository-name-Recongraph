from dataclasses import dataclass
from recongraph.graph.decision import ReconciliationDecision, DecisionAction
from recongraph.matching.scoring import SignalName

@dataclass(frozen=True)
class EvidenceSummary:
    """A snapshot of the core signals that drove the score."""
    reference_score: float | None
    amount_score: float
    temporal_score: float
    entity_score: float
    tax_identity_score: float | None

@dataclass(frozen=True)
class DecisionExplanation:
    """The complete, auditable explanation of a reconciliation decision."""
    action: DecisionAction
    policy_rationale: str
    positive_reasons: tuple[str, ...]
    limiting_factors: tuple[str, ...]
    ambiguity_context: str | None
    evidence_summary: EvidenceSummary | None

class ExplanationBuilder:
    """Translates mathematical evaluations and decisions into human-readable explanations."""
    
    def build(self, decision: ReconciliationDecision) -> DecisionExplanation:
        if decision.action == DecisionAction.NO_MATCH:
            return DecisionExplanation(
                action=decision.action,
                policy_rationale=decision.rationale,
                positive_reasons=(),
                limiting_factors=("No mathematically eligible hypotheses generated.",),
                ambiguity_context=None,
                evidence_summary=None
            )
            
        hypothesis = decision.selected_hypothesis
        ambiguity_context = None
        
        if decision.action == DecisionAction.REVIEW_AMBIGUOUS:
            if len(decision.competitors) >= 2:
                top_1 = decision.competitors[0]
                top_2 = decision.competitors[1]
                ambiguity_context = f"Competitor was only {top_1.score - top_2.score:.3f} points behind."
                hypothesis = top_1
        
        if not hypothesis:
            return DecisionExplanation(
                action=decision.action,
                policy_rationale=decision.rationale,
                positive_reasons=(),
                limiting_factors=(),
                ambiguity_context=ambiguity_context,
                evidence_summary=None
            )

        signals = hypothesis.supporting_evidence.get("signals", {})
        
        summary = EvidenceSummary(
            reference_score=signals.get(SignalName.REFERENCE),
            amount_score=signals.get(SignalName.AMOUNT, 0.0),
            temporal_score=signals.get(SignalName.TEMPORAL, 0.0),
            entity_score=signals.get(SignalName.ENTITY, 0.0),
            tax_identity_score=signals.get(SignalName.TAX_IDENTITY)
        )
        
        positives = []
        if summary.amount_score == 1.0:
            positives.append("Amounts match perfectly.")
        if summary.reference_score is not None and summary.reference_score >= 0.8:
            positives.append("Strong reference match on a distinct identifier.")
        if summary.entity_score >= 0.8:
            positives.append("Vendor identities are highly similar.")
        if summary.temporal_score == 1.0:
            positives.append("Dates match perfectly.")
            
        limits = []
        if hypothesis.violations:
            for v in sorted(list(hypothesis.violations)):
                limits.append(f"Semantic violation: {v}")
                
        if summary.amount_score < 0.9:
            limits.append("Amounts differ significantly.")
        if summary.temporal_score < 0.5:
            limits.append("Dates are far apart.")
        if summary.reference_score is None:
            limits.append("No reference provided to match.")

        return DecisionExplanation(
            action=decision.action,
            policy_rationale=decision.rationale,
            positive_reasons=tuple(positives),
            limiting_factors=tuple(limits),
            ambiguity_context=ambiguity_context,
            evidence_summary=summary
        )
