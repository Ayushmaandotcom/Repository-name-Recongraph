from recongraph.graph.candidate import CandidateGraph
from recongraph.graph.hypotheses import Hypothesis, EvaluatedHypothesis, EligibilityStatus
from recongraph.matching.signals import amount_score, tax_identity_score, entity_score
from recongraph.matching.scoring import SignalName, calculate_relationship_score
from recongraph.matching.purchase_gst_semantics import (
    analyze_purchase_gst_semantics, 
    evaluate_purchase_gst_one_to_one_eligibility, 
    OneToOneEligibility
)
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, compute_reference_interpretation
from recongraph.matching.pair_scorers import PURCHASE_TO_GST_POLICY, PURCHASE_TO_GST_MAX_DAYS

class HypothesisEvaluator:
    """
    Evaluates a structural hypothesis by resolving its nodes, 
    aggregating domain evidence, and scoring the aggregate entities.
    It does not make final reconciliation decisions.
    """
    def __init__(self, reference_context: ReferenceEvidenceContext):
        self.reference_context = reference_context

    def evaluate(self, graph: CandidateGraph, hypothesis: Hypothesis) -> EvaluatedHypothesis:
        # HS-004: If hypothesis is empty, it resolves nothing.
        if not hypothesis.matched_nodes:
            return EvaluatedHypothesis(
                hypothesis=hypothesis,
                score=0.0,
                eligibility=EligibilityStatus.INELIGIBLE,
                supporting_evidence={},
                violations=frozenset(["EMPTY_HYPOTHESIS"])
            )
            
        purchases = []
        gsts = []
        
        for u in hypothesis.matched_nodes:
            if u.startswith("urn:recongraph:purchase:"):
                purchases.append(graph.nodes[u])
            elif u.startswith("urn:recongraph:gst:"):
                gsts.append(graph.nodes[u])
                
        # Must be bipartite
        if not purchases or not gsts:
            return EvaluatedHypothesis(
                hypothesis=hypothesis,
                score=0.0,
                eligibility=EligibilityStatus.INELIGIBLE,
                supporting_evidence={},
                violations=frozenset(["MISSING_COUNTERPARTY"])
            )
            
        # Evidence Aggregation
        p_amount = sum(p.amount for p in purchases)
        g_amount = sum(g.amount for g in gsts)
        
        max_day_diff = max(
            abs((p.record_date - g.record_date).days) 
            for p in purchases for g in gsts
        )
        
        tax_ids_p = {p.tax_identity for p in purchases if p.tax_identity}
        tax_ids_g = {g.tax_identity for g in gsts if g.tax_identity}
        
        p_refs = " ".join(p.reference for p in purchases if p.reference)
        g_refs = " ".join(g.reference for g in gsts if g.reference)
        
        p_vendors = " ".join(p.vendor_name for p in purchases if p.vendor_name)
        g_vendors = " ".join(g.vendor_name for g in gsts if g.vendor_name)

        # Semantics
        ref_interpretation = compute_reference_interpretation(
            p_refs, g_refs, self.reference_context
        )
        
        ref_signal = ref_interpretation.score if (p_refs and g_refs) else None

        t_score = 0.0 if max_day_diff > PURCHASE_TO_GST_MAX_DAYS else (1.0 - (max_day_diff / PURCHASE_TO_GST_MAX_DAYS))

        tax_id_p_val = next(iter(tax_ids_p)) if len(tax_ids_p) == 1 else None
        tax_id_g_val = next(iter(tax_ids_g)) if len(tax_ids_g) == 1 else None
        
        signals = {
            SignalName.ENTITY: entity_score(p_vendors, g_vendors),
            SignalName.REFERENCE: ref_signal,
            SignalName.AMOUNT: amount_score(p_amount, g_amount),
            SignalName.TEMPORAL: t_score,
            SignalName.TAX_IDENTITY: tax_identity_score(tax_id_p_val, tax_id_g_val),
        }
        
        semantic_findings = analyze_purchase_gst_semantics(signals)
        legacy_eligibility = evaluate_purchase_gst_one_to_one_eligibility(semantic_findings)
        
        if legacy_eligibility.status == OneToOneEligibility.ELIGIBLE:
            eligibility = EligibilityStatus.ELIGIBLE
        elif legacy_eligibility.status == OneToOneEligibility.REQUIRES_REVIEW:
            eligibility = EligibilityStatus.REQUIRES_REVIEW
        else:
            eligibility = EligibilityStatus.INELIGIBLE
            
        relationship = calculate_relationship_score(
            signals=signals, policy=PURCHASE_TO_GST_POLICY
        )
        
        violations = {str(f.value) for f in semantic_findings}
        
        # Extra constraints
        if max_day_diff > PURCHASE_TO_GST_MAX_DAYS:
            violations.add("TEMPORAL_MAX_DAYS_EXCEEDED")
            eligibility = EligibilityStatus.INELIGIBLE
            
        supporting_evidence = {
            "signals": signals,
            "relationship": relationship,
            "reference_interpretation": ref_interpretation
        }

        return EvaluatedHypothesis(
            hypothesis=hypothesis,
            score=relationship.score,
            eligibility=eligibility,
            supporting_evidence=supporting_evidence,
            violations=frozenset(violations)
        )
