import collections
from dataclasses import dataclass
from typing import Tuple

from recongraph.matching.reference_evidence import (
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

def unrelated_references(count: int, *, start: int = 500_000) -> tuple[str, ...]:
    return tuple(f"OTHER-{start + i}" for i in range(count))

def check_norm_availability(enriched) -> bool:
    if not enriched.normalized_references:
        return True
    return all(ev.statistics is not None for ev in enriched.normalized_references)

def get_norm_availability_count(enriched) -> int:
    return sum(1 for ev in enriched.normalized_references if ev.statistics is not None)

def check_token_availability(enriched) -> bool:
    if not enriched.shared_numeric_tokens:
        return True
    return all(ev.statistics is not None for ev in enriched.shared_numeric_tokens)

def main():
    print(f"{'Case':<6}{'Stage1 Evidence':<17}{'Structural Profile State':<26}{'Interpretation Coverage Question'}")
    print("-" * 82)

    # IC-A
    identity_a = extract_reference_identity(None, None)
    assert identity_a is None
    print(f"{'IC-A':<6}{'none':<17}{'none':<26}{'no interpretation'}")

    # IC-B
    corpus_b = ["OMD-001", "NSS-001"] + [f"DOC{i}-001" for i in range(38)]
    profile_b = build_reference_corpus_profile(tuple(corpus_b) + unrelated_references(60))
    identity_b = extract_reference_identity("OMD-001", "NSS-001")
    enriched_b = enrich_reference_identity(identity_b, profile_b)

    # assertions
    assert profile_b.numeric_token_document_frequency["001"] == 40
    print(f"{'IC-B':<6}{'present':<17}{'fully profiled':<26}{'1.0'}")

    # IC-C
    corpus_c = ["INV-874219", "DOC-874219"] + list(unrelated_references(98))
    profile_c = build_reference_corpus_profile(tuple(corpus_c))
    identity_c = extract_reference_identity("INV-874219", "NEW-874219")
    enriched_c = enrich_reference_identity(identity_c, profile_c)

    # assertions
    assert profile_c.numeric_token_document_frequency["874219"] == 2
    assert get_norm_availability_count(enriched_c) == 1
    assert len(enriched_c.normalized_references) == 2
    print(f"{'IC-C':<6}{'present':<17}{'mixed':<26}{'path-dependent'}")

    # IC-D
    profile_d = build_reference_corpus_profile(unrelated_references(100))
    identity_d = extract_reference_identity("NEW-999999", "XYZ-999999")
    enriched_d = enrich_reference_identity(identity_d, profile_d)

    # assertions
    assert get_norm_availability_count(enriched_d) == 0
    assert enriched_d.shared_numeric_tokens[0].statistics is None
    print(f"{'IC-D':<6}{'present':<17}{'out-of-profile':<26}{'0.0'}")

if __name__ == '__main__':
    main()
