import pytest

from recongraph.matching.reference_evidence import (
    EnrichedReferenceEvidence,
    NormalizedReferenceStatistics,
    ReferenceCorpusProfile,
    ReferenceIdentityEvidence,
    ReferenceTokenStatistics,
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

def test_extracts_normalized_exact_identity():
    evidence = extract_reference_identity("SB-8891", "SB8891")
    assert evidence is not None
    assert evidence.normalized_a == "sb8891"
    assert evidence.normalized_b == "sb8891"
    assert evidence.exact_normalized_match is True
    assert evidence.shared_numeric_tokens == ("8891",)

def test_extracts_shared_numeric_identity_without_exact_match():
    evidence = extract_reference_identity("INV-874219", "AB/874219")
    assert evidence is not None
    assert evidence.normalized_a == "inv874219"
    assert evidence.normalized_b == "ab874219"
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ("874219",)

def test_extracts_multiple_shared_numeric_tokens_in_deterministic_order():
    evidence = extract_reference_identity("INV-2026-1001", "ABC-2026-1001")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("1001", "2026")

def test_returns_empty_shared_tokens_when_no_overlap_exists():
    evidence = extract_reference_identity("INV-1042", "INV-1043")
    assert evidence is not None
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ()

def test_extracts_non_numeric_exact_identity():
    evidence = extract_reference_identity("CREDIT-NOTE", "CREDITNOTE")
    assert evidence is not None
    assert evidence.normalized_a == "creditnote"
    assert evidence.normalized_b == "creditnote"
    assert evidence.exact_normalized_match is True
    assert evidence.shared_numeric_tokens == ()

def test_returns_none_for_missing_first_reference():
    assert extract_reference_identity(None, "INV-001") is None

def test_returns_none_for_blank_first_reference():
    assert extract_reference_identity("   ", "INV-001") is None

def test_returns_none_when_both_references_missing():
    assert extract_reference_identity(None, None) is None

def test_deduplicates_tokens_within_single_reference():
    evidence = extract_reference_identity("INV-1001-1001", "ABC-1001")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("1001",)

def test_extracts_short_numeric_tokens_without_length_filtering():
    evidence = extract_reference_identity("INV-01-874219", "AB-01-874219")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("01", "874219")

def test_extracts_garbage_numeric_collision_factually():
    evidence = extract_reference_identity("INV-001", "ABC-001")
    assert evidence is not None
    assert evidence.exact_normalized_match is False
    assert evidence.shared_numeric_tokens == ("001",)

def test_extracts_repeated_token_collision_factually():
    evidence = extract_reference_identity("INV-999999", "ABC-999999")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("999999",)

def test_extracts_only_shared_tokens_from_mixed_matches():
    evidence = extract_reference_identity("INV-2026-1001", "ABC-2025-1001")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("1001",)

def test_extracts_short_tokens_for_namespaces():
    evidence = extract_reference_identity("INV-01", "ABC-01")
    assert evidence is not None
    assert evidence.shared_numeric_tokens == ("01",)

@pytest.mark.parametrize('ref_a, ref_b', [
    ('---', 'INV-001'),
    ('INV-001', '///'),
    ('---', '///'),
])
def test_extract_reference_identity_returns_none_when_normalization_removes_all_content(ref_a, ref_b):
    assert extract_reference_identity(ref_a, ref_b) is None

def test_reference_corpus_profile_empty_corpus():
    profile = build_reference_corpus_profile([])
    assert profile.reference_count == 0
    assert profile.normalized_reference_frequency == {}
    assert profile.numeric_token_document_frequency == {}

def test_reference_corpus_profile_basic():
    profile = build_reference_corpus_profile([
        'INV-001',
        'ABC-001',
        'INV-874219',
        'AB/874219',
    ])
    assert profile.reference_count == 4
    assert profile.normalized_reference_frequency == {
        'inv001': 1,
        'abc001': 1,
        'inv874219': 1,
        'ab874219': 1,
    }
    assert profile.numeric_token_document_frequency == {
        '001': 2,
        '874219': 2,
    }

def test_reference_corpus_profile_normalized_collisions():
    profile = build_reference_corpus_profile([
        'SB-8891',
        'SB8891',
        'sb/8891',
    ])
    assert profile.reference_count == 3
    assert profile.normalized_reference_frequency == {'sb8891': 3}
    assert profile.numeric_token_document_frequency == {'8891': 3}

def test_reference_corpus_profile_duplicate_token():
    profile = build_reference_corpus_profile([
        'INV-1001-1001',
        'ABC-1001',
    ])
    assert profile.reference_count == 2
    assert profile.numeric_token_document_frequency['1001'] == 2

def test_reference_corpus_profile_missing_and_blank():
    profile = build_reference_corpus_profile([
        'INV-001',
        None,
        '',
        '   ',
        '	',
        'GST-001',
    ])
    assert profile.reference_count == 2
    assert profile.normalized_reference_frequency == {
        'inv001': 1,
        'gst001': 1,
    }
    assert profile.numeric_token_document_frequency == {
        '001': 2,
    }

def test_reference_corpus_profile_non_numeric():
    profile = build_reference_corpus_profile([
        'CREDIT-NOTE',
        'CREDITNOTE',
        'DEBITNOTE',
    ])
    assert profile.reference_count == 3
    assert profile.normalized_reference_frequency == {
        'creditnote': 2,
        'debitnote': 1,
    }
    assert profile.numeric_token_document_frequency == {}

def test_reference_corpus_profile_short_tokens():
    profile = build_reference_corpus_profile([
        'INV-01',
        'ABC-01',
        'PO-02',
    ])
    assert profile.numeric_token_document_frequency == {
        '01': 2,
        '02': 1,
    }

def test_reference_corpus_profile_punctuation_only():
    profile = build_reference_corpus_profile([
        'INV-001',
        '---',
        '///',
        '...',
        'GST-001',
    ])
    assert profile.reference_count == 2
    assert profile.normalized_reference_frequency == {
        'inv001': 1,
        'gst001': 1,
    }

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
        ReferenceCorpusProfile(
            reference_count=-1,
            normalized_reference_frequency={'inv001': 1},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_inconsistent_sum():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=2,
            normalized_reference_frequency={'inv001': 1},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_frequency_greater_than_corpus_size():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=2,
            normalized_reference_frequency={'inv001': 3},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_df_greater_than_corpus_size():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=2,
            normalized_reference_frequency={'inv001': 2},
            numeric_token_document_frequency={'001': 3},
        )

def test_reference_corpus_profile_validation_invalid_normalized_key():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=1,
            normalized_reference_frequency={'INV-001': 1},
            numeric_token_document_frequency={'001': 1},
        )

def test_reference_corpus_profile_validation_invalid_numeric_token():
    with pytest.raises(ValueError):
        ReferenceCorpusProfile(
            reference_count=1,
            normalized_reference_frequency={'inv001': 1},
            numeric_token_document_frequency={'ABC': 1},
        )

def test_reference_corpus_profile_direct_construction_snapshot_isolation():
    normalized = {'inv001': 1}
    tokens = {'001': 1}

    profile = ReferenceCorpusProfile(
        reference_count=1,
        normalized_reference_frequency=normalized,
        numeric_token_document_frequency=tokens,
    )

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

    profile = build_reference_corpus_profile([
        'INV-874219',
        'AB/874219',
    ])

    enriched = enrich_reference_identity(
        identity,
        profile,
    )

    assert enriched.identity is identity
