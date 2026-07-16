import pytest
from hypothesis import given, strategies as st
from datetime import date
from decimal import Decimal

from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.config import ReconGraphConfig, DecisionConfig, DecisionMode
from recongraph.engine import ReconGraphEngine
from recongraph.plugins.core_providers import (
    FinancialEvidenceProvider,
    TemporalEvidenceProvider,
    TaxEvidenceProvider,
    VendorEvidenceProvider,
    ReferenceEvidenceProvider
)
from recongraph.matching.reference_evidence import ReferenceEvidenceContext, ReferenceCorpusProfile, ReferenceEvidencePolicy
from recongraph.domain.vendor.context import VendorIdentityContext, VendorCorpusProfile
from recongraph.graph.decision import DecisionAction
from recongraph.domain.vendor.parser import DeterministicVendorParser

# 1. Score bounded (scores always between 0 and 1, or None)
@given(
    st.floats(min_value=0.0, max_value=1000000.0),
    st.floats(min_value=0.0, max_value=1000000.0)
)
def test_property_score_bounded(amount1, amount2):
    p = PurchaseRecord(record_id="p1", amount=Decimal(str(amount1)), record_date=date(2023, 1, 1), reference="INV", vendor_name="A", tax_identity="TAX")
    g = GSTRecord(record_id="g1", amount=Decimal(str(amount2)), record_date=date(2023, 1, 1), reference="INV", vendor_name="A", tax_identity="TAX")
    
    provider = FinancialEvidenceProvider()
    contrib = provider.evaluate([p], [g])
    if contrib.score is not None:
        assert 0.0 <= contrib.score <= 1.0

# 2. Coverage bounded (coverage always between 0 and 1)
def test_property_coverage_bounded():
    p1 = PurchaseRecord(record_id="p1", amount=Decimal("10.0"), record_date=date(2023,1,1), reference="A", vendor_name="V", tax_identity="T")
    g1 = GSTRecord(record_id="g1", amount=Decimal("10.0"), record_date=date(2023,1,1), reference="A", vendor_name="V", tax_identity="T")
    
    config = ReconGraphConfig()
    context = ReferenceEvidenceContext(
        profile=ReferenceCorpusProfile(reference_count=1, normalized_reference_frequency={"a":1}, numeric_token_document_frequency={}),
        policy=ReferenceEvidencePolicy()
    )
    vendor_context = VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    providers = [TemporalEvidenceProvider(), FinancialEvidenceProvider(), TaxEvidenceProvider(), ReferenceEvidenceProvider(context), VendorEvidenceProvider(vendor_context)]
    
    from recongraph.graph.evaluator import HypothesisEvaluator
    from recongraph.graph.candidate import CandidateGraphBuilder
    from recongraph.graph.hypotheses import Hypothesis
    
    gb = CandidateGraphBuilder()
    gb.add_node("urn:recongraph:purchase:p1", p1)
    gb.add_node("urn:recongraph:gst:g1", g1)
    graph = gb.build()
    
    h = Hypothesis(
        component_nodes=frozenset(["urn:recongraph:purchase:p1", "urn:recongraph:gst:g1"]),
        proposed_edges=frozenset([frozenset(["urn:recongraph:purchase:p1", "urn:recongraph:gst:g1"])])
    )
    
    evaluator = HypothesisEvaluator(providers, config.decision_config.relationship_policy)
    eval_h = evaluator.evaluate(graph, h)
    assert 0.0 <= eval_h.coverage <= 1.0

# 3. Permutation invariance (reordering records does not change trace IDs)
@given(st.permutations([
    PurchaseRecord(record_id="p1", amount=Decimal("10.0"), record_date=date(2023,1,1), reference="A", vendor_name="V", tax_identity="T"),
    PurchaseRecord(record_id="p2", amount=Decimal("20.0"), record_date=date(2023,1,1), reference="B", vendor_name="V", tax_identity="T"),
    PurchaseRecord(record_id="p3", amount=Decimal("30.0"), record_date=date(2023,1,1), reference="C", vendor_name="V", tax_identity="T")
]))
def test_property_permutation_invariance(shuffled_purchases):
    g1 = GSTRecord(record_id="g1", amount=Decimal("10.0"), record_date=date(2023,1,1), reference="A", vendor_name="V", tax_identity="T")
    g2 = GSTRecord(record_id="g2", amount=Decimal("20.0"), record_date=date(2023,1,1), reference="B", vendor_name="V", tax_identity="T")
    
    config = ReconGraphConfig()
    context = ReferenceEvidenceContext(
        profile=ReferenceCorpusProfile(reference_count=3, normalized_reference_frequency={"a":1, "b":1, "c":1}, numeric_token_document_frequency={}),
        policy=ReferenceEvidencePolicy()
    )
    vendor_context = VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    providers = [TemporalEvidenceProvider(), FinancialEvidenceProvider(), TaxEvidenceProvider(), ReferenceEvidenceProvider(context), VendorEvidenceProvider(vendor_context)]
    
    engine = ReconGraphEngine(config, providers)
    result = engine.reconcile(shuffled_purchases, [g1, g2])
    
    # Sort traces for deterministic comparison
    trace_ids = sorted([t.trace_id for t in result.traces])
    
    # Run again with standard order
    standard = sorted(shuffled_purchases, key=lambda x: x.record_id)
    result2 = engine.reconcile(standard, [g1, g2])
    trace_ids2 = sorted([t.trace_id for t in result2.traces])
    
    assert trace_ids == trace_ids2

# 4. Trace determinism (exact same inputs always produce exact same trace ID)
def test_property_trace_determinism():
    p1 = PurchaseRecord(record_id="p1", amount=Decimal("10.0"), record_date=date(2023,1,1), reference="A", vendor_name="V", tax_identity="T")
    g1 = GSTRecord(record_id="g1", amount=Decimal("10.0"), record_date=date(2023,1,1), reference="A", vendor_name="V", tax_identity="T")
    
    config = ReconGraphConfig()
    context = ReferenceEvidenceContext(
        profile=ReferenceCorpusProfile(reference_count=1, normalized_reference_frequency={"a":1}, numeric_token_document_frequency={}),
        policy=ReferenceEvidencePolicy()
    )
    vendor_context = VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    providers = [TemporalEvidenceProvider(), FinancialEvidenceProvider(), TaxEvidenceProvider(), ReferenceEvidenceProvider(context), VendorEvidenceProvider(vendor_context)]
    
    engine1 = ReconGraphEngine(config, providers)
    res1 = engine1.reconcile([p1], [g1])
    
    engine2 = ReconGraphEngine(config, providers)
    res2 = engine2.reconcile([p1], [g1])
    
    assert res1.traces[0].trace_id == res2.traces[0].trace_id

# 5. Normalization idempotence (running the parser on already parsed identities yields the same result)
@given(st.text(min_size=1, max_size=50))
def test_property_normalization_idempotence(vendor_name):
    parser = DeterministicVendorParser()
    first_pass = parser.parse(vendor_name)
    if first_pass:
        second_pass = parser.parse(first_pass.canonical_core_text)
        assert first_pass.canonical_core_text == second_pass.canonical_core_text
