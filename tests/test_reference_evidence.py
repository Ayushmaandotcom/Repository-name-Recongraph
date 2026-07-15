import pytest
from recongraph.matching.reference_evidence import EnrichedReferenceEvidence, NormalizedReferenceStatistics, ReferenceCorpusProfile, ReferenceIdentityEvidence, ReferenceTokenStatistics, build_reference_corpus_profile, enrich_reference_identity, extract_reference_identity, ReferenceEvidenceContribution, ReferenceEvidenceKind, ReferenceEvidencePolicy, ReferenceEvidenceInterpretation, _profiled_rarity_magnitude

def test_extracts_normalized_exact_identity():
    evidence = extract_reference_identity('SB-8891', 'SB8891')
    assert evidence is not None
    assert evidence.normalized_a == 'sb8891'
    assert evidence.normalized_b == 'sb8891'
    assert evidence.exact_normalized_match is True
    assert evidence.shared_numeric_tokens == ('8891',)

def test_extracts_shared_numeric_identity_without_exact_match():
    evidence = extract_reference_identity('INV-874219', 'AB/874219')
    assert evidence is not None
    assert evidence.normalized_a == 'inv874219'
    assert evidence.normalized_b == 'ab874219'
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ('874219',)

def test_extracts_multiple_shared_numeric_tokens_in_deterministic_order():
    evidence = extract_reference_identity('INV-2026-1001', 'ABC-2026-1001')
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ('1001', '2026')

def test_returns_empty_shared_tokens_when_no_overlap_exists():
    evidence = extract_reference_identity('INV-1042', 'INV-1043')
    assert evidence is not None
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ()

def test_extracts_non_numeric_exact_identity():
    evidence = extract_reference_identity('CREDIT-NOTE', 'CREDITNOTE')
    assert evidence is not None
    assert evidence.normalized_a == 'creditnote'
    assert evidence.normalized_b == 'creditnote'
    assert evidence.exact_normalized_match is True
    assert evidence.shared_numeric_tokens == ()

def test_returns_none_for_missing_first_reference():
    assert extract_reference_identity(None, 'INV-001') is None

def test_returns_none_for_blank_first_reference():
    assert extract_reference_identity('   ', 'INV-001') is None

def test_returns_none_when_both_references_missing():
    assert extract_reference_identity(None, None) is None

def test_deduplicates_tokens_within_single_reference():
    evidence = extract_reference_identity('INV-1001-1001', 'ABC-1001')
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ('1001',)

def test_extracts_short_numeric_tokens_without_length_filtering():
    evidence = extract_reference_identity('INV-01-874219', 'AB-01-874219')
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ('01', '874219')

def test_extracts_garbage_numeric_collision_factually():
    evidence = extract_reference_identity('INV-001', 'ABC-001')
    assert evidence is not None
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ('001',)

def test_extracts_repeated_token_collision_factually():
    evidence = extract_reference_identity('INV-999999', 'ABC-999999')
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ('999999',)

def test_extracts_only_shared_tokens_from_mixed_matches():
    evidence = extract_reference_identity('INV-2026-1001', 'ABC-2025-1001')
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ('1001',)

def test_extracts_short_tokens_for_namespaces():
    evidence = extract_reference_identity('INV-01', 'ABC-01')
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ('01',)

@pytest.mark.parametrize('ref_a, ref_b', [('---', 'INV-001'), ('INV-001', '///'), ('---', '///')])
def test_extract_reference_identity_returns_none_when_normalization_removes_all_content(ref_a, ref_b):
    assert extract_reference_identity(ref_a, ref_b) is None

def test_reference_corpus_profile_empty_corpus():
    profile = build_reference_corpus_profile([])
    assert profile.reference_count == 0
    assert profile.normalized_reference_frequency == {}
    assert profile.numeric_token_document_frequency == {}

def test_reference_corpus_profile_basic():
    profile = build_reference_corpus_profile(['INV-001', 'ABC-001', 'INV-874219', 'AB/874219'])
    assert profile.reference_count == 4
    assert profile.normalized_reference_frequency == {'inv001': 1, 'abc001': 1, 'inv874219': 1, 'ab874219': 1}
    assert profile.numeric_token_document_frequency == {'001': 2, '874219': 2}

def test_reference_corpus_profile_normalized_collisions():
    profile = build_reference_corpus_profile(['SB-8891', 'SB8891', 'sb/8891'])
    assert profile.reference_count == 3
    assert profile.normalized_reference_frequency == {'sb8891': 3}
    assert profile.numeric_token_document_frequency == {'8891': 3}

def test_reference_corpus_profile_duplicate_token():
    profile = build_reference_corpus_profile(['INV-1001-1001', 'ABC-1001'])
    assert profile.reference_count == 2
    assert profile.numeric_token_document_frequency['1001'] == 2

def test_reference_corpus_profile_missing_and_blank():
    profile = build_reference_corpus_profile(['INV-001', None, '', '   ', '\t', 'GST-001'])
    assert profile.reference_count == 2
    assert profile.normalized_reference_frequency == {'inv001': 1, 'gst001': 1}
    assert profile.numeric_token_document_frequency == {'001': 2}

def test_reference_corpus_profile_non_numeric():
    profile = build_reference_corpus_profile(['CREDIT-NOTE', 'CREDITNOTE', 'DEBITNOTE'])
    assert profile.reference_count == 3
    assert profile.normalized_reference_frequency == {'creditnote': 2, 'debitnote': 1}
    assert profile.numeric_token_document_frequency == {}

def test_reference_corpus_profile_short_tokens():
    profile = build_reference_corpus_profile(['INV-01', 'ABC-01', 'PO-02'])
    assert profile.numeric_token_document_frequency == {'01': 2, '02': 1}

def test_reference_corpus_profile_punctuation_only():
    profile = build_reference_corpus_profile(['INV-001', '---', '///', '...', 'GST-001'])
    assert profile.reference_count == 2
    assert profile.normalized_reference_frequency == {'inv001': 1, 'gst001': 1}

def test_reference_corpus_profile_frequency_mappings_are_read_only():
    profile = build_reference_corpus_profile(['INV-001'])
    with pytest.raises(TypeError):
        profile.normalized_reference_frequency['inv001'] = 5
    with pytest.raises(TypeError):
        profile.numeric_token_document_frequency['001'] = 5

def test_normalized_reference_statistics_validation():
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('', 1)
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('INV-001', 1)
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('inv001', 0)
    with pytest.raises(ValueError):
        NormalizedReferenceStatistics('inv001', -1)

def test_reference_token_statistics_validation():
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('', 1)
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('ABC', 1)
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('001', 0)
    with pytest.raises(ValueError):
        ReferenceTokenStatistics('001', -1)

def test_reference_corpus_profile_validation_reference_count():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(reference_count=-1, normalized_reference_frequency={'inv001': 1}, numeric_token_document_frequency={'001': 1})

def test_reference_corpus_profile_validation_inconsistent_sum():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(reference_count=2, normalized_reference_frequency={'inv001': 1}, numeric_token_document_frequency={'001': 1})

def test_reference_corpus_profile_validation_frequency_greater_than_corpus_size():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(reference_count=2, normalized_reference_frequency={'inv001': 3}, numeric_token_document_frequency={'001': 1})

def test_reference_corpus_profile_validation_df_greater_than_corpus_size():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(reference_count=2, normalized_reference_frequency={'inv001': 2}, numeric_token_document_frequency={'001': 3})

def test_reference_corpus_profile_validation_invalid_normalized_key():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(reference_count=1, normalized_reference_frequency={'INV-001': 1}, numeric_token_document_frequency={'001': 1})

def test_reference_corpus_profile_validation_invalid_numeric_token():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(reference_count=1, normalized_reference_frequency={'inv001': 1}, numeric_token_document_frequency={'ABC': 1})

def test_reference_corpus_profile_direct_construction_snapshot_isolation():
    normalized = {'inv001': 1}
    tokens = {'001': 1}
    profile = ReferenceCorpusProfile(reference_count=1, normalized_reference_frequency=normalized, numeric_token_document_frequency=tokens)
    normalized['inv001'] = 999
    tokens['001'] = 999
    assert profile.normalized_reference_frequency['inv001'] == 1
    assert profile.numeric_token_document_frequency['001'] == 1

def test_enrich_reference_identity_known_exact_identity():
    profile = build_reference_corpus_profile(['SB-8891', 'SB8891', 'ABC-001'])
    identity = extract_reference_identity('SB-8891', 'SB8891')
    enriched = enrich_reference_identity(identity, profile)
    assert enriched.identity == identity
    assert len(enriched.normalized_references) == 1
    assert enriched.normalized_references[0].normalized_reference == 'sb8891'
    assert enriched.normalized_references[0].statistics.frequency == 2
    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '8891'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 2

def test_enrich_reference_identity_distinct_normalized_references():
    profile = build_reference_corpus_profile(['INV-874219', 'AB/874219', 'ABC-001'])
    identity = extract_reference_identity('INV-874219', 'AB/874219')
    enriched = enrich_reference_identity(identity, profile)
    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].normalized_reference == 'ab874219'
    assert enriched.normalized_references[0].statistics.frequency == 1
    assert enriched.normalized_references[1].normalized_reference == 'inv874219'
    assert enriched.normalized_references[1].statistics.frequency == 1
    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '874219'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 2

def test_enrich_reference_identity_out_of_profile():
    profile = build_reference_corpus_profile(['INV-001', 'ABC-001'])
    identity = extract_reference_identity('NEW-874219', 'AB/874219')
    enriched = enrich_reference_identity(identity, profile)
    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].normalized_reference == 'ab874219'
    assert enriched.normalized_references[0].statistics is None
    assert enriched.normalized_references[1].normalized_reference == 'new874219'
    assert enriched.normalized_references[1].statistics is None
    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '874219'
    assert enriched.shared_numeric_tokens[0].statistics is None

def test_enrich_reference_identity_mixed_known_and_unknown():
    profile = build_reference_corpus_profile(['INV-874219', 'ABC-001'])
    identity = extract_reference_identity('INV-874219', 'AB/874219')
    enriched = enrich_reference_identity(identity, profile)
    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].normalized_reference == 'ab874219'
    assert enriched.normalized_references[0].statistics is None
    assert enriched.normalized_references[1].normalized_reference == 'inv874219'
    assert enriched.normalized_references[1].statistics.frequency == 1
    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '874219'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 1

def test_enrich_reference_identity_short_shared_token():
    profile = build_reference_corpus_profile(['INV-01', 'ABC-01', 'PO-02'])
    identity = extract_reference_identity('INV-01', 'ABC-01')
    enriched = enrich_reference_identity(identity, profile)
    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].token == '01'
    assert enriched.shared_numeric_tokens[0].statistics.document_frequency == 2

def test_enrich_reference_identity_non_numeric_exact_identity():
    profile = build_reference_corpus_profile(['CREDIT-NOTE', 'CREDITNOTE', 'DEBITNOTE'])
    identity = extract_reference_identity('CREDIT-NOTE', 'CREDITNOTE')
    enriched = enrich_reference_identity(identity, profile)
    assert len(enriched.normalized_references) == 1
    assert enriched.normalized_references[0].normalized_reference == 'creditnote'
    assert enriched.normalized_references[0].statistics.frequency == 2
    assert len(enriched.shared_numeric_tokens) == 0

def test_enrich_reference_identity_empty_profile():
    profile = build_reference_corpus_profile([])
    identity = extract_reference_identity('INV-001', 'ABC-001')
    enriched = enrich_reference_identity(identity, profile)
    assert len(enriched.normalized_references) == 2
    assert enriched.normalized_references[0].statistics is None
    assert enriched.normalized_references[1].statistics is None
    assert len(enriched.shared_numeric_tokens) == 1
    assert enriched.shared_numeric_tokens[0].statistics is None

def test_enrich_reference_identity_preserves_identity_object():
    identity = extract_reference_identity('INV-874219', 'AB/874219')
    assert identity is not None
    profile = build_reference_corpus_profile(['INV-874219', 'AB/874219'])
    enriched = enrich_reference_identity(identity, profile)
    assert enriched.identity is identity
import math

def test_reference_evidence_policy_defaults():
    policy = ReferenceEvidencePolicy()
    assert policy.short_token_max_length == 2
    assert policy.medium_token_max_length == 4
    assert policy.short_token_fallback == 0.1
    assert policy.medium_token_fallback == 0.3
    assert policy.long_token_fallback == 0.6
    assert policy.repeated_pattern_discount == 0.5

def test_reference_evidence_policy_validation_short_token_max_length():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=0)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=-1)

def test_reference_evidence_policy_validation_medium_token_max_length():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=2, medium_token_max_length=2)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_max_length=4, medium_token_max_length=3)

def test_reference_evidence_policy_validation_float_bounds():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=-0.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(medium_token_fallback=1.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=-0.5)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(repeated_pattern_discount=1.5)

def test_reference_evidence_policy_validation_finiteness():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=float('nan'))
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=float('nan'))
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=float('-inf'))

def test_reference_evidence_policy_exact_reference_fallback_validation():
    p = ReferenceEvidencePolicy()
    assert p.exact_reference_fallback == 0.6
    p_zero = ReferenceEvidencePolicy(exact_reference_fallback=0.0)
    assert p_zero.exact_reference_fallback == 0.0
    p_max = ReferenceEvidencePolicy(exact_reference_fallback=0.75)
    assert p_max.exact_reference_fallback == 0.75
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=-0.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=0.76)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=float('nan'))
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=float('inf'))
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(exact_reference_fallback=float('-inf'))

def test_reference_evidence_policy_exact_fallback_independent_ordering():
    p1 = ReferenceEvidencePolicy(short_token_fallback=0.1, medium_token_fallback=0.2, long_token_fallback=0.3, exact_reference_fallback=0.7)
    assert p1.exact_reference_fallback == 0.7
    p2 = ReferenceEvidencePolicy(short_token_fallback=0.1, medium_token_fallback=0.2, long_token_fallback=0.7, exact_reference_fallback=0.05)
    assert p2.exact_reference_fallback == 0.05
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(repeated_pattern_discount=float('nan'))

def test_reference_evidence_policy_validation_ordering():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=0.8, medium_token_fallback=0.3, long_token_fallback=0.1)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=0.3, medium_token_fallback=0.2, long_token_fallback=0.6)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(short_token_fallback=0.1, medium_token_fallback=0.5, long_token_fallback=0.4)

def test_reference_evidence_policy_validation_ordering_equality():
    p1 = ReferenceEvidencePolicy(short_token_fallback=0.2, medium_token_fallback=0.2, long_token_fallback=0.5)
    assert p1.short_token_fallback == p1.medium_token_fallback
    assert p1.medium_token_fallback < p1.long_token_fallback
    p2 = ReferenceEvidencePolicy(short_token_fallback=0.1, medium_token_fallback=0.4, long_token_fallback=0.4)
    assert p2.short_token_fallback < p2.medium_token_fallback
    assert p2.medium_token_fallback == p2.long_token_fallback
    p3 = ReferenceEvidencePolicy(short_token_fallback=0.3, medium_token_fallback=0.3, long_token_fallback=0.3)
    assert p3.short_token_fallback == p3.medium_token_fallback == p3.long_token_fallback

def test_reference_evidence_policy_validation_long_fallback_ceiling():
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=0.8)
    with pytest.raises(ValueError):
        ReferenceEvidencePolicy(long_token_fallback=1.0)

def test_reference_evidence_contribution_validation_missing_identity():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='', positive_evidence=0.5, evidential_weight=0.5, statistics_available=True)

def test_reference_evidence_contribution_validation_float_bounds():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=-0.1, statistics_available=True)
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=1.1, statistics_available=True)

def test_reference_evidence_contribution_validation_finiteness():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=float('nan'), statistics_available=True)

def test_reference_evidence_contribution_validation_shared_numeric_token_format():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='ABC123', positive_evidence=0.5, evidential_weight=0.5, statistics_available=True)
    ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='12345', positive_evidence=0.5, evidential_weight=0.5, statistics_available=True)

def test_reference_evidence_contribution_validation_normalized_reference_format():
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE, identity_value='INV-123', positive_evidence=1.0, evidential_weight=0.5, statistics_available=True)
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE, identity_value='INV/123', positive_evidence=1.0, evidential_weight=0.5, statistics_available=True)
    with pytest.raises(ValueError):
        ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE, identity_value='Inv123', positive_evidence=1.0, evidential_weight=0.5, statistics_available=True)
    ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.NORMALIZED_REFERENCE, identity_value='inv123', positive_evidence=1.0, evidential_weight=0.5, statistics_available=True)

def test_reference_evidence_interpretation_validation_float_bounds():
    contrib = ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=0.5, statistics_available=True)
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=-0.1, statistical_coverage=1.0, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=1.1, statistical_coverage=1.0, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=-0.1, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=1.1, contributions=(contrib,))

def test_reference_evidence_interpretation_validation_finiteness():
    contrib = ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=0.5, statistics_available=True)
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=float('nan'), statistical_coverage=1.0, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=float('inf'), contributions=(contrib,))

def test_reference_evidence_interpretation_validation_empty_contributions():
    with pytest.raises(ValueError, match='empty contributions requires score=0.0 and statistical_coverage=0.0'):
        ReferenceEvidenceInterpretation(score=0.9, statistical_coverage=0.0, contributions=())

def test_reference_evidence_interpretation_validation_score_matches_strongest():
    contrib1 = ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=0.3, statistics_available=True)
    contrib2 = ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='456', positive_evidence=0.5, evidential_weight=0.8, statistics_available=True)
    ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=1.0, contributions=(contrib1, contrib2))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.9, statistical_coverage=1.0, contributions=(contrib1, contrib2))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.3, statistical_coverage=1.0, contributions=(contrib1, contrib2))

def test_reference_evidence_interpretation_validation_coverage_binary():
    contrib = ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=0.5, statistics_available=True)
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.2, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.5, contributions=(contrib,))
    with pytest.raises(ValueError):
        ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.75, contributions=(contrib,))
    ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=1.0, contributions=(contrib,))
    contrib_unprofiled = ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value='123', positive_evidence=0.5, evidential_weight=0.5, statistics_available=False)
    ReferenceEvidenceInterpretation(score=0.5, statistical_coverage=0.0, contributions=(contrib_unprofiled,))

def test_profiled_rarity_magnitude_f1_n1():
    assert math.isclose(_profiled_rarity_magnitude(1, 1), 0.0)

def test_profiled_rarity_magnitude_fN_nN():
    assert math.isclose(_profiled_rarity_magnitude(100, 100), 0.0)

def test_profiled_rarity_magnitude_f1_n100():
    assert math.isclose(_profiled_rarity_magnitude(1, 100), 0.9)

def test_profiled_rarity_magnitude_f4_n100():
    assert math.isclose(_profiled_rarity_magnitude(4, 100), 0.8)

def test_profiled_rarity_magnitude_f25_n100():
    assert math.isclose(_profiled_rarity_magnitude(25, 100), 0.5)

def test_profiled_rarity_magnitude_monotonic_decrease():
    m1 = _profiled_rarity_magnitude(1, 1000)
    m2 = _profiled_rarity_magnitude(10, 1000)
    m3 = _profiled_rarity_magnitude(100, 1000)
    assert m1 > m2 > m3

def test_profiled_rarity_magnitude_corpus_replication_invariance():
    m1 = _profiled_rarity_magnitude(1, 100)
    m2 = _profiled_rarity_magnitude(10, 1000)
    assert math.isclose(m1, m2)

def test_profiled_rarity_magnitude_bounds():
    m1 = _profiled_rarity_magnitude(1, 1000000)
    m2 = _profiled_rarity_magnitude(1000000, 1000000)
    assert 0.0 <= m1 <= 1.0
    assert 0.0 <= m2 <= 1.0

def test_profiled_rarity_magnitude_validation():
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(0, 100)
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(-1, 100)
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(1, 0)
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(1, -1)
    with pytest.raises(ValueError):
        _profiled_rarity_magnitude(10, 5)

def test_structural_token_magnitude_bands():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy(short_token_max_length=2, medium_token_max_length=4, short_token_fallback=0.1, medium_token_fallback=0.3, long_token_fallback=0.6, repeated_pattern_discount=0.5)
    assert math.isclose(_structural_token_magnitude('12', policy), 0.1)
    assert math.isclose(_structural_token_magnitude('1234', policy), 0.3)
    assert math.isclose(_structural_token_magnitude('123456', policy), 0.6)

def test_structural_token_magnitude_boundaries():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy(short_token_max_length=2, medium_token_max_length=4)
    assert math.isclose(_structural_token_magnitude('12', policy), policy.short_token_fallback)
    assert math.isclose(_structural_token_magnitude('123', policy), policy.medium_token_fallback)
    assert math.isclose(_structural_token_magnitude('1234', policy), policy.medium_token_fallback)
    assert math.isclose(_structural_token_magnitude('12345', policy), policy.long_token_fallback)
    assert math.isclose(_structural_token_magnitude('1', policy), policy.short_token_fallback * policy.repeated_pattern_discount)

def test_structural_token_magnitude_discounts():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy()
    assert math.isclose(_structural_token_magnitude('001', policy), policy.medium_token_fallback)
    assert math.isclose(_structural_token_magnitude('000', policy), policy.medium_token_fallback * policy.repeated_pattern_discount)
    assert math.isclose(_structural_token_magnitude('111', policy), policy.medium_token_fallback * policy.repeated_pattern_discount)
    assert math.isclose(_structural_token_magnitude('999999', policy), policy.long_token_fallback * policy.repeated_pattern_discount)
    assert math.isclose(_structural_token_magnitude('121212', policy), policy.long_token_fallback)
    assert math.isclose(_structural_token_magnitude('123123', policy), policy.long_token_fallback)
    assert math.isclose(_structural_token_magnitude('101010', policy), policy.long_token_fallback)
    assert math.isclose(_structural_token_magnitude('000001', policy), policy.long_token_fallback)

def test_structural_token_magnitude_custom_discount():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    p_zero = ReferenceEvidencePolicy(repeated_pattern_discount=0.0)
    assert math.isclose(_structural_token_magnitude('111', p_zero), 0.0)
    p_one = ReferenceEvidencePolicy(repeated_pattern_discount=1.0)
    assert math.isclose(_structural_token_magnitude('111', p_one), p_one.medium_token_fallback)

def test_structural_token_magnitude_equal_bands():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy(short_token_fallback=0.2, medium_token_fallback=0.2, long_token_fallback=0.2)
    assert math.isclose(_structural_token_magnitude('12', policy), 0.2)
    assert math.isclose(_structural_token_magnitude('1234', policy), 0.2)
    assert math.isclose(_structural_token_magnitude('123456', policy), 0.2)

def test_structural_token_magnitude_deterministic_and_pure():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy()
    assert _structural_token_magnitude('111', policy) == _structural_token_magnitude('111', policy)
    discount_before = policy.repeated_pattern_discount
    _structural_token_magnitude('111', policy)
    assert policy.repeated_pattern_discount == discount_before

def test_structural_token_magnitude_validation():
    from recongraph.matching.reference_evidence import _structural_token_magnitude
    policy = ReferenceEvidencePolicy()
    with pytest.raises(ValueError):
        _structural_token_magnitude('', policy)
    with pytest.raises(ValueError):
        _structural_token_magnitude('12A', policy)
    with pytest.raises(ValueError):
        _structural_token_magnitude('12 3', policy)
    with pytest.raises(ValueError):
        _structural_token_magnitude('-001', policy)
        _structural_token_magnitude('1.23', policy)

def _create_mock_enriched_evidence(exact_match: bool, norm_val: str, norm_freq: int | None, tokens: list[tuple[str, int | None]], reference_count: int=100) -> 'EnrichedReferenceEvidence':
    from recongraph.matching.reference_evidence import ReferenceIdentityEvidence, NormalizedReferenceStatistics, NormalizedReferenceEvidence, ReferenceTokenStatistics, SharedNumericTokenEvidence, EnrichedReferenceEvidence
    identity = ReferenceIdentityEvidence(normalized_a=norm_val, normalized_b=norm_val if exact_match else norm_val + 'diff', exact_normalized_match=exact_match, shared_numeric_tokens=tuple((t[0] for t in tokens)))
    if norm_freq is not None:
        n_stat = NormalizedReferenceStatistics(norm_val, norm_freq)
    else:
        n_stat = None
    norm_evs = []
    if exact_match:
        norm_evs.append(NormalizedReferenceEvidence(norm_val, n_stat))
    elif norm_val < norm_val + 'diff':
        norm_evs.append(NormalizedReferenceEvidence(norm_val, n_stat))
        norm_evs.append(NormalizedReferenceEvidence(norm_val + 'diff', None))
    else:
        norm_evs.append(NormalizedReferenceEvidence(norm_val + 'diff', None))
        norm_evs.append(NormalizedReferenceEvidence(norm_val, n_stat))
    tok_evs = []
    for t_val, t_df in tokens:
        if t_df is not None:
            t_stat = ReferenceTokenStatistics(t_val, t_df)
        else:
            t_stat = None
        tok_evs.append(SharedNumericTokenEvidence(t_val, t_stat))
    return EnrichedReferenceEvidence(identity=identity, reference_count=reference_count, normalized_references=tuple(norm_evs), shared_numeric_tokens=tuple(tok_evs))

def test_construct_reference_evidence_contributions_exact():
    from recongraph.matching.reference_evidence import _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile, ReferenceEvidenceKind
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={'inv874219': 1, 'creditnote': 99}, numeric_token_document_frequency={})
    ev1 = _create_mock_enriched_evidence(True, 'inv874219', 1, [])
    c1 = _construct_reference_evidence_contributions(ev1, policy)
    assert len(c1) == 1
    assert c1[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c1[0].identity_value == 'inv874219'
    assert math.isclose(c1[0].evidential_weight, 0.9)
    assert c1[0].statistics_available is True
    ev2 = _create_mock_enriched_evidence(True, 'creditnote', 100, [])
    c2 = _construct_reference_evidence_contributions(ev2, policy)
    assert len(c2) == 1
    assert c2[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c2[0].identity_value == 'creditnote'
    assert math.isclose(c2[0].evidential_weight, 0.0)
    assert c2[0].statistics_available is True
    ev3 = _create_mock_enriched_evidence(True, 'inv999999', None, [])
    c3 = _construct_reference_evidence_contributions(ev3, policy)
    assert len(c3) == 1
    assert c3[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c3[0].identity_value == 'inv999999'
    assert math.isclose(c3[0].evidential_weight, 0.6)
    assert c3[0].statistics_available is False
    ev4 = _create_mock_enriched_evidence(True, 'creditnote', None, [])
    c4 = _construct_reference_evidence_contributions(ev4, policy)
    assert len(c4) == 1
    assert c4[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c4[0].identity_value == 'creditnote'
    assert math.isclose(c4[0].evidential_weight, 0.6)
    assert c4[0].statistics_available is False
    ev5 = _create_mock_enriched_evidence(True, '000000', None, [])
    c5 = _construct_reference_evidence_contributions(ev5, policy)
    assert len(c5) == 1
    assert c5[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert c5[0].identity_value == '000000'
    assert math.isclose(c5[0].evidential_weight, 0.6)
    assert c5[0].statistics_available is False
    p2 = ReferenceEvidencePolicy(exact_reference_fallback=0.25)
    c6 = _construct_reference_evidence_contributions(ev5, p2)
    assert math.isclose(c6[0].evidential_weight, 0.25)

def test_construct_reference_evidence_contributions_tokens():
    from recongraph.matching.reference_evidence import _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile, ReferenceEvidenceKind
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={'dummy': 100}, numeric_token_document_frequency={'874219': 1, '001': 100})
    ev7 = _create_mock_enriched_evidence(False, 'inv874219', None, [('874219', 1)])
    c7 = _construct_reference_evidence_contributions(ev7, policy)
    assert len(c7) == 1
    assert c7[0].evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN
    assert c7[0].identity_value == '874219'
    assert math.isclose(c7[0].evidential_weight, 0.9)
    assert c7[0].statistics_available is True
    ev8 = _create_mock_enriched_evidence(False, 'inv001', None, [('001', 100)])
    c8 = _construct_reference_evidence_contributions(ev8, policy)
    assert len(c8) == 1
    assert c8[0].evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN
    assert c8[0].identity_value == '001'
    assert math.isclose(c8[0].evidential_weight, 0.0)
    assert c8[0].statistics_available is True
    ev9 = _create_mock_enriched_evidence(False, 'inv874219', None, [('874219', None)])
    c9 = _construct_reference_evidence_contributions(ev9, policy)
    assert len(c9) == 1
    assert c9[0].evidence_kind == ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN
    assert c9[0].identity_value == '874219'
    assert math.isclose(c9[0].evidential_weight, 0.6)
    assert c9[0].statistics_available is False
    ev10 = _create_mock_enriched_evidence(False, 'inv001', None, [('001', None)])
    c10 = _construct_reference_evidence_contributions(ev10, policy)
    assert len(c10) == 1
    assert c10[0].identity_value == '001'
    assert math.isclose(c10[0].evidential_weight, 0.3)
    assert c10[0].statistics_available is False
    ev11 = _create_mock_enriched_evidence(False, 'inv999999', None, [('999999', None)])
    c11 = _construct_reference_evidence_contributions(ev11, policy)
    assert len(c11) == 1
    assert c11[0].identity_value == '999999'
    assert math.isclose(c11[0].evidential_weight, 0.3)
    assert c11[0].statistics_available is False
    ev12 = _create_mock_enriched_evidence(False, 'inv121212', None, [('121212', None)])
    c12 = _construct_reference_evidence_contributions(ev12, policy)
    assert len(c12) == 1
    assert c12[0].identity_value == '121212'
    assert math.isclose(c12[0].evidential_weight, 0.6)
    ev13 = _create_mock_enriched_evidence(False, 'inv2026', None, [('2026', None), ('874219', None)])
    c13 = _construct_reference_evidence_contributions(ev13, policy)
    assert len(c13) == 2
    assert c13[0].identity_value == '2026'
    assert c13[1].identity_value == '874219'

def test_construct_reference_evidence_contributions_equal_magnitude_regression():
    from recongraph.matching.reference_evidence import _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={'inv1': 16, 'dummy': 84}, numeric_token_document_frequency={})
    ev_prof = _create_mock_enriched_evidence(True, 'inv1', 16, [])
    ev_unprof = _create_mock_enriched_evidence(True, 'inv2', None, [])
    c_prof = _construct_reference_evidence_contributions(ev_prof, policy)[0]
    c_unprof = _construct_reference_evidence_contributions(ev_unprof, policy)[0]
    assert math.isclose(c_prof.evidential_weight, 0.6)
    assert math.isclose(c_unprof.evidential_weight, 0.6)
    assert math.isclose(c_prof.evidential_weight, c_unprof.evidential_weight)
    assert c_prof.statistics_available is True
    assert c_unprof.statistics_available is False

def test_construct_reference_evidence_contributions_stage_boundary():
    from recongraph.matching.reference_evidence import _construct_reference_evidence_contributions, ReferenceEvidencePolicy, ReferenceCorpusProfile, ReferenceEvidenceContribution
    policy = ReferenceEvidencePolicy()
    profile = ReferenceCorpusProfile(reference_count=100, normalized_reference_frequency={'dummy': 100}, numeric_token_document_frequency={})
    ev = _create_mock_enriched_evidence(False, 'inv', None, [('123', None), ('456', None)])
    out = _construct_reference_evidence_contributions(ev, policy)
    assert isinstance(out, tuple)
    assert all((isinstance(c, ReferenceEvidenceContribution) for c in out))
    assert not hasattr(out[0], 'statistical_coverage')
    assert len(out) == 2

def test_select_strongest_reference_contribution():
    from recongraph.matching.reference_evidence import ReferenceEvidenceContribution, ReferenceEvidenceKind, _select_strongest_reference_contribution

    def make_contrib(mag: float, stats: bool, kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, val='0'):
        return ReferenceEvidenceContribution(evidence_kind=kind, identity_value=val, positive_evidence=1.0, evidential_weight=mag, statistics_available=stats)
    c_single = make_contrib(0.9, True, val='874219')
    w_single = _select_strongest_reference_contribution((c_single,))
    assert w_single is c_single
    ca = make_contrib(0.6, False)
    cb = make_contrib(0.9, False)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is cb
    ca = make_contrib(0.7, False)
    cb = make_contrib(0.6, True)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca
    ca = make_contrib(0.6, False)
    cb = make_contrib(0.6, True)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is cb
    ca = make_contrib(0.6, True)
    cb = make_contrib(0.6, False)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca
    ca = make_contrib(0.6, True, val='2026')
    cb = make_contrib(0.6, True, val='874219')
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca
    w2 = _select_strongest_reference_contribution((cb, ca))
    assert w2 is cb
    ca = make_contrib(0.0, False)
    cb = make_contrib(0.0, True)
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is cb
    ca = make_contrib(0.0, True, val='1')
    cb = make_contrib(0.0, True, val='2')
    w = _select_strongest_reference_contribution((ca, cb))
    assert w is ca
    import pytest
    with pytest.raises(ValueError, match='at least one reference evidence contribution is required'):
        _select_strongest_reference_contribution(())
    ca = make_contrib(0.3, False)
    cb = make_contrib(0.68, True)
    cc = make_contrib(0.9, True)
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is cc
    ca = make_contrib(0.9, True)
    cb = make_contrib(0.68, True)
    cc = make_contrib(0.3, False)
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is ca
    ca = make_contrib(0.6, False)
    cb = make_contrib(0.3, True)
    cc = make_contrib(0.6, True)
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is cc
    ca = make_contrib(0.6, True, val='1')
    cb = make_contrib(0.3, False)
    cc = make_contrib(0.6, True, val='3')
    w = _select_strongest_reference_contribution((ca, cb, cc))
    assert w is ca

def test_select_strongest_reference_contribution_identity_and_mutation():
    from recongraph.matching.reference_evidence import ReferenceEvidenceContribution, ReferenceEvidenceKind, _select_strongest_reference_contribution
    ca = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, '1', 0.5, 0.5, True)
    cb = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, '2', 0.5, 0.8, False)
    cc = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, '3', 0.5, 0.2, True)
    contributions = (ca, cb, cc)
    before_tuple = contributions
    before_values = tuple(((c.evidence_kind, c.identity_value, c.positive_evidence, c.statistics_available) for c in contributions))
    winner = _select_strongest_reference_contribution(contributions)
    assert any((winner is c for c in contributions))
    assert winner is cb
    assert contributions is before_tuple
    assert tuple(((c.evidence_kind, c.identity_value, c.positive_evidence, c.statistics_available) for c in contributions)) == before_values
    import pytest
    from dataclasses import FrozenInstanceError
    with pytest.raises(FrozenInstanceError):
        winner.positive_evidence = 0.99

def test_select_strongest_reference_contribution_integration():
    from recongraph.matching.reference_evidence import extract_reference_identity, build_reference_corpus_profile, enrich_reference_identity, _construct_reference_evidence_contributions, _select_strongest_reference_contribution, ReferenceEvidencePolicy
    import math
    policy = ReferenceEvidencePolicy()
    ident = extract_reference_identity('INV-2026-874219', 'AB-2026-874219')
    prof = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 10, '874219': 1})
    enriched = enrich_reference_identity(ident, prof)
    contribs = _construct_reference_evidence_contributions(enriched, policy)
    winner = _select_strongest_reference_contribution(contribs)
    assert winner.identity_value == '874219'
    assert math.isclose(winner.evidential_weight, 0.9)
    prof2 = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 1, '874219': 1})
    enriched2 = enrich_reference_identity(ident, prof2)
    contribs2 = _construct_reference_evidence_contributions(enriched2, policy)
    winner2 = _select_strongest_reference_contribution(contribs2)
    assert winner2.identity_value == '2026'
    ident3 = extract_reference_identity('INV-874219-999999', 'AB-874219-999999')
    ident3_alt = extract_reference_identity('INV-874219-121212', 'AB-874219-121212')
    prof3 = ReferenceCorpusProfile(100, {'dummy': 100}, {'874219': 16})
    enriched3 = enrich_reference_identity(ident3_alt, prof3)
    contribs3 = _construct_reference_evidence_contributions(enriched3, policy)
    winner3 = _select_strongest_reference_contribution(contribs3)
    assert winner3.identity_value == '874219'
    prof4 = ReferenceCorpusProfile(100, {'dummy': 100}, {'874219': 17})
    enriched4 = enrich_reference_identity(ident3_alt, prof4)
    contribs4 = _construct_reference_evidence_contributions(enriched4, policy)
    winner4 = _select_strongest_reference_contribution(contribs4)
    assert winner4.identity_value == '121212'

def test_assemble_reference_evidence_interpretation():
    from recongraph.matching.reference_evidence import ReferenceEvidenceContribution, ReferenceEvidenceKind, _assemble_reference_evidence_interpretation

    def make_contrib(mag, stats, val='1'):
        return ReferenceEvidenceContribution(evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, identity_value=val, positive_evidence=0.5, evidential_weight=mag, statistics_available=stats)
    c = make_contrib(0.9, True)
    interp = _assemble_reference_evidence_interpretation((c,))
    assert interp.score == 0.5
    assert interp.statistical_coverage == 1.0
    assert interp.contributions == (c,)
    c2 = make_contrib(0.6, False)
    interp2 = _assemble_reference_evidence_interpretation((c2,))
    assert interp2.score == 0.5
    assert interp2.statistical_coverage == 0.0
    ca = make_contrib(0.6, False, val='1')
    cb = make_contrib(0.6, True, val='2')
    interp3 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp3.score == 0.5
    assert interp3.statistical_coverage == 1.0
    ca = make_contrib(0.7, False, val='1')
    cb = make_contrib(0.6, True, val='2')
    interp4 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp4.score == 0.5
    assert interp4.statistical_coverage == 0.0
    ca = make_contrib(0.3, False, val='1')
    cb = make_contrib(0.68, True, val='2')
    cc = make_contrib(0.9, True, val='3')
    interp5 = _assemble_reference_evidence_interpretation((ca, cb, cc))
    assert interp5.score == 0.5
    assert interp5.statistical_coverage == 1.0
    ca = make_contrib(0.3, True, val='1')
    cb = make_contrib(0.68, True, val='2')
    cc = make_contrib(0.9, False, val='3')
    interp6 = _assemble_reference_evidence_interpretation((ca, cb, cc))
    assert interp6.score == 0.5
    assert interp6.statistical_coverage == 0.0
    ca = make_contrib(0.0, False, val='1')
    cb = make_contrib(0.0, True, val='2')
    interp7 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp7.score == 0.5
    assert interp7.statistical_coverage == 1.0
    ca = make_contrib(0.6, True, val='2026')
    cb = make_contrib(0.6, True, val='874219')
    interp8 = _assemble_reference_evidence_interpretation((ca, cb))
    assert interp8.score == 0.5
    assert interp8.statistical_coverage == 1.0
    interp9 = _assemble_reference_evidence_interpretation((cb, ca))
    assert interp9.score == 0.5
    assert interp9.statistical_coverage == 1.0
    tup = (ca, cb)
    interp10 = _assemble_reference_evidence_interpretation(tup)
    assert interp10.contributions == tup
    assert interp10.contributions is tup
    import pytest
    with pytest.raises(ValueError):
        _assemble_reference_evidence_interpretation(())
import pytest

@pytest.mark.parametrize('magnitude, stats, expected_score, expected_coverage', [(0.0, False, 0.0, 0.0), (0.0, True, 0.0, 1.0), (0.3, False, 0.3, 0.0), (0.3, True, 0.3, 1.0), (0.6, False, 0.6, 0.0), (0.6, True, 0.6, 1.0), (0.9, False, 0.9, 0.0), (0.9, True, 0.9, 1.0)])
def test_assemble_reference_evidence_coverage_truth_table(magnitude, stats, expected_score, expected_coverage):
    from recongraph.matching.reference_evidence import ReferenceEvidenceContribution, ReferenceEvidenceKind, _assemble_reference_evidence_interpretation
    c = ReferenceEvidenceContribution(ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN, '1', 0.5, magnitude, stats)
    interp = _assemble_reference_evidence_interpretation((c,))
    assert interp.contributions[0].evidential_weight == expected_score
    assert interp.statistical_coverage == expected_coverage

def test_assemble_reference_evidence_integration():
    from recongraph.matching.reference_evidence import extract_reference_identity, build_reference_corpus_profile, enrich_reference_identity, _construct_reference_evidence_contributions, _assemble_reference_evidence_interpretation, ReferenceEvidencePolicy, ReferenceEvidenceKind
    import math
    policy = ReferenceEvidencePolicy()
    prof = ReferenceCorpusProfile(100, {'dummy': 99, 'inv874219': 1}, {})
    enriched = enrich_reference_identity(extract_reference_identity('INV-874219', 'INV/874219'), prof)
    contribs = _construct_reference_evidence_contributions(enriched, policy)
    interp = _assemble_reference_evidence_interpretation(contribs)
    assert len(interp.contributions) == 1
    assert interp.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    assert interp.score == 1.0
    assert math.isclose(interp.contributions[0].evidential_weight, 0.9)
    assert interp.statistical_coverage == 1.0
    prof2 = ReferenceCorpusProfile(100, {'creditnote': 100}, {})
    enriched2 = enrich_reference_identity(extract_reference_identity('CREDIT NOTE', 'creditnote'), prof2)
    contribs2 = _construct_reference_evidence_contributions(enriched2, policy)
    interp2 = _assemble_reference_evidence_interpretation(contribs2)
    assert interp2.score == 1.0
    assert interp2.statistical_coverage == 1.0
    prof3 = ReferenceCorpusProfile(100, {'dummy': 100}, {})
    enriched3 = enrich_reference_identity(extract_reference_identity('INV-999999', 'INV/999999'), prof3)
    contribs3 = _construct_reference_evidence_contributions(enriched3, policy)
    interp3 = _assemble_reference_evidence_interpretation(contribs3)
    assert interp3.score == 1.0
    assert math.isclose(interp3.contributions[0].evidential_weight, policy.exact_reference_fallback)
    assert interp3.statistical_coverage == 0.0
    prof4 = ReferenceCorpusProfile(100, {'dummy': 100}, {'874219': 1})
    enriched4 = enrich_reference_identity(extract_reference_identity('INV-874219', 'AB-874219'), prof4)
    contribs4 = _construct_reference_evidence_contributions(enriched4, policy)
    interp4 = _assemble_reference_evidence_interpretation(contribs4)
    assert interp4.score == 0.5
    assert math.isclose(interp4.contributions[0].evidential_weight, 0.9)
    assert interp4.statistical_coverage == 1.0
    prof5 = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 36})
    enriched5 = enrich_reference_identity(extract_reference_identity('INV-2026', 'AB-2026'), prof5)
    contribs5 = _construct_reference_evidence_contributions(enriched5, policy)
    interp5 = _assemble_reference_evidence_interpretation(contribs5)
    assert interp5.score == 0.5
    assert math.isclose(interp5.contributions[0].evidential_weight, 0.4)
    assert interp5.statistical_coverage == 1.0
    prof6 = ReferenceCorpusProfile(100, {'dummy': 100}, {})
    enriched6 = enrich_reference_identity(extract_reference_identity('INV-121212', 'AB-121212'), prof6)
    contribs6 = _construct_reference_evidence_contributions(enriched6, policy)
    interp6 = _assemble_reference_evidence_interpretation(contribs6)
    assert interp6.score == 0.5
    assert math.isclose(interp6.contributions[0].evidential_weight, policy.long_token_fallback)
    assert interp6.statistical_coverage == 0.0
    prof7 = ReferenceCorpusProfile(100, {'dummy': 100}, {})
    enriched7 = enrich_reference_identity(extract_reference_identity('INV-999999', 'AB-999999'), prof7)
    contribs7 = _construct_reference_evidence_contributions(enriched7, policy)
    interp7 = _assemble_reference_evidence_interpretation(contribs7)
    assert interp7.score == 0.5
    assert math.isclose(interp7.contributions[0].evidential_weight, policy.long_token_fallback * policy.repeated_pattern_discount)
    assert interp7.statistical_coverage == 0.0
    prof8 = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 36, '874219': 1})
    enriched8 = enrich_reference_identity(extract_reference_identity('INV-2026-874219', 'AB-2026-874219'), prof8)
    contribs8 = _construct_reference_evidence_contributions(enriched8, policy)
    interp8 = _assemble_reference_evidence_interpretation(contribs8)
    assert interp8.score == 0.5
    assert math.isclose(max(c.evidential_weight for c in interp8.contributions), 0.9)
    assert interp8.statistical_coverage == 1.0
    prof9 = ReferenceCorpusProfile(100, {'dummy': 100}, {})
    enriched9 = enrich_reference_identity(extract_reference_identity('INV-2026-121212', 'AB-2026-121212'), prof9)
    contribs9 = _construct_reference_evidence_contributions(enriched9, policy)
    interp9 = _assemble_reference_evidence_interpretation(contribs9)
    assert interp9.score == 0.5
    assert interp9.statistical_coverage == 0.0
    prof10 = ReferenceCorpusProfile(100, {'dummy': 99, 'inv2026874219': 1}, {'2026': 10, '874219': 1})
    enriched10 = enrich_reference_identity(extract_reference_identity('INV-2026-874219', 'INV/2026/874219'), prof10)
    contribs10 = _construct_reference_evidence_contributions(enriched10, policy)
    interp10 = _assemble_reference_evidence_interpretation(contribs10)
    assert len(interp10.contributions) == 1
    assert interp10.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE

def test_interpret_reference_evidence_public_api():
    from recongraph.matching.reference_evidence import interpret_reference_evidence, ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity, enrich_reference_identity, ReferenceEvidenceKind
    import math
    policy = ReferenceEvidencePolicy()
    prof = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 10, '874219': 1})
    ev1 = enrich_reference_identity(extract_reference_identity('INV-2026-874219', 'AB-2026-874219'), prof)
    interp1 = interpret_reference_evidence(ev1, policy)
    assert interp1.score == 0.5
    assert math.isclose(max(c.evidential_weight for c in interp1.contributions), 0.9)
    assert interp1.statistical_coverage == 1.0
    assert len(interp1.contributions) == 2
    prof2 = ReferenceCorpusProfile(100, {'inv874219': 1, 'dummy': 99}, {})
    ev2 = enrich_reference_identity(extract_reference_identity('INV-874219', 'INV/874219'), prof2)
    interp2 = interpret_reference_evidence(ev2, policy)
    assert math.isclose(interp2.score, 1.0)
    assert interp2.statistical_coverage == 1.0
    assert len(interp2.contributions) == 1
    assert interp2.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE
    ev3 = enrich_reference_identity(extract_reference_identity('INV-111', 'AB-222'), prof)
    interp3 = interpret_reference_evidence(ev3, policy)
    assert interp3.score == 0.0
    assert interp3.statistical_coverage == 0.0
    assert interp3.contributions == ()

def test_compute_reference_interpretation_facade():
    from recongraph.matching.reference_evidence import compute_reference_interpretation, ReferenceEvidenceContext, ReferenceEvidencePolicy, ReferenceCorpusProfile, ReferenceEvidenceKind
    import math
    policy = ReferenceEvidencePolicy()
    prof = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 10, '874219': 1})
    context = ReferenceEvidenceContext(profile=prof, policy=policy)
    interp1 = compute_reference_interpretation(None, None, context)
    assert interp1.score == 0.0
    assert interp1.statistical_coverage == 0.0
    assert interp1.contributions == ()
    interp1b = compute_reference_interpretation('', '   ', context)
    assert interp1b.score == 0.0
    assert interp1b.statistical_coverage == 0.0
    assert interp1b.contributions == ()
    interp2 = compute_reference_interpretation('INV-2026-121212', 'AB-2026-121212', context)
    assert interp2.score == 0.5
    assert math.isclose(max(c.evidential_weight for c in interp2.contributions), 1.0 - math.sqrt(0.1))
    assert interp2.statistical_coverage == 1.0
    assert len(interp2.contributions) == 2
    winner2 = max(interp2.contributions, key=lambda c: c.evidential_weight)
    assert winner2.identity_value == '2026'
    assert winner2.statistics_available is True
    prof_mixed = ReferenceCorpusProfile(100, {'dummy': 100}, {'2026': 64})
    ctx_mixed = ReferenceEvidenceContext(profile=prof_mixed, policy=policy)
    interp3 = compute_reference_interpretation('INV-2026-121212', 'AB-2026-121212', ctx_mixed)
    assert interp3.score == 0.5
    assert interp3.statistical_coverage == 0.0
    winner3 = max(interp3.contributions, key=lambda c: c.positive_evidence)
    assert winner3.identity_value == '121212'
    assert winner3.statistics_available is False
    interp4 = compute_reference_interpretation('111', '222', context)
    assert interp4.score == 0.0
    assert interp4.statistical_coverage == 0.0
    assert interp4.contributions == ()
    prof_exact = ReferenceCorpusProfile(100, {'inv874219': 1, 'dummy': 99}, {})
    ctx_exact = ReferenceEvidenceContext(profile=prof_exact, policy=policy)
    interp5 = compute_reference_interpretation('INV-874219', 'INV/874219', ctx_exact)
    assert math.isclose(interp5.score, 1.0)
    assert interp5.statistical_coverage == 1.0
    assert len(interp5.contributions) == 1
    assert interp5.contributions[0].evidence_kind == ReferenceEvidenceKind.NORMALIZED_REFERENCE