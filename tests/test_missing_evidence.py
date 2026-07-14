import pytest
from recongraph.graph.explainability import ExplanationBuilder, EvidenceSummary
from recongraph.graph.decision import ReconciliationDecision, DecisionAction
from recongraph.graph.hypotheses import EvaluatedHypothesis, Hypothesis, EligibilityStatus
from recongraph.matching.scoring import SignalName

def test_evidence_summary_accepts_none_in_every_field():
    summary = EvidenceSummary(
        reference_score=None,
        amount_score=None,
        temporal_score=None,
        entity_score=None,
        tax_identity_score=None
    )
    assert summary.amount_score is None
    assert summary.temporal_score is None

def test_explanation_reports_unavailable_evidence_as_unavailable_not_as_disagreement():
    builder = ExplanationBuilder()
    
    hypothesis = EvaluatedHypothesis(
        hypothesis=Hypothesis(frozenset(), frozenset()),
        score=0.5,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={"signals": {}},
        violations=frozenset()
    )
    
    decision = ReconciliationDecision(
        action=DecisionAction.REVIEW_AMBIGUOUS,
        rationale="test",
        selected_hypothesis=hypothesis,
        competitors=()
    )
    
    explanation = builder.build(decision)
    
    assert "Amount evidence unavailable." in explanation.limiting_factors
    assert "Date evidence unavailable." in explanation.limiting_factors
    assert "Amounts differ significantly." not in explanation.limiting_factors
    
def test_missing_evidence_reduces_coverage_without_zeroing_the_score():
    # If a signal is present but zero, it's a contradiction.
    # If it's missing, it just limits coverage but doesn't necessarily create a contradiction.
    # The explanation builder should reflect this.
    builder = ExplanationBuilder()
    
    # Simulate missing tax identity but matching amount
    hypothesis = EvaluatedHypothesis(
        hypothesis=Hypothesis(frozenset(), frozenset()),
        score=0.5,
        eligibility=EligibilityStatus.ELIGIBLE,
        supporting_evidence={"signals": {SignalName.AMOUNT: 1.0, SignalName.TEMPORAL: 1.0}},
        violations=frozenset()
    )
    
    decision = ReconciliationDecision(
        action=DecisionAction.AUTO_MATCH,
        rationale="test",
        selected_hypothesis=hypothesis,
        competitors=()
    )
    
    explanation = builder.build(decision)
    
    assert "Amounts match perfectly." in explanation.positive_reasons
    assert "Dates match perfectly." in explanation.positive_reasons
    assert "No reference provided to match." in explanation.limiting_factors
