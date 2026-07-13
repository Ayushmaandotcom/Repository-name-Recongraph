import collections
from dataclasses import dataclass
from typing import Tuple

from recongraph.matching.reference_evidence import (
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

@dataclass(frozen=True)
class ReferenceEvidenceScenario:
    scenario_id: str
    description: str
    reference_a: str
    reference_b: str
    corpus_references: tuple[str, ...]

def unrelated_references(count: int, *, start: int = 500_000) -> tuple[str, ...]:
    return tuple(f"OTHER-{start + i}" for i in range(count))

def format_norm_stats(enriched):
    out = []
    for ev in enriched.normalized_references:
        val = ev.statistics.frequency if ev.statistics else "?"
        out.append(f"{ev.normalized_reference}:{val}")
    return ", ".join(out) if out else "none"

def format_token_stats(enriched):
    out = []
    for ev in enriched.shared_numeric_tokens:
        val = ev.statistics.document_frequency if ev.statistics else "?"
        out.append(f"{ev.token}:{val}")
    return ", ".join(out) if out else "none"


def main():
    scenarios = []

    # RE001
    scenarios.append(ReferenceEvidenceScenario(
        "RE001", "Unique exact normalized identity",
        "INV-874219", "INV/874219",
        ("INV-874219", "INV/874219") + unrelated_references(98)
    ))

    # RE002
    # The pair is CREDIT-NOTE and CREDITNOTE.
    # Total creditnote freq = 40. Pair + 38 more.
    corpus_re002 = ["CREDIT-NOTE", "CREDITNOTE"] + ["CREDIT/NOTE"] * 38
    scenarios.append(ReferenceEvidenceScenario(
        "RE002", "Repeated exact normalized identity",
        "CREDIT-NOTE", "CREDITNOTE",
        tuple(corpus_re002) + unrelated_references(60)
    ))

    # RE003
    scenarios.append(ReferenceEvidenceScenario(
        "RE003", "Rare six-digit shared numeric token",
        "INV-874219", "AB/874219",
        ("INV-874219", "AB/874219") + unrelated_references(98)
    ))

    # RE004
    corpus_re004 = ["INV-874219", "AB/874219"] + [f"DOC{i}-874219" for i in range(38)]
    scenarios.append(ReferenceEvidenceScenario(
        "RE004", "Common six-digit shared numeric token",
        "INV-874219", "AB/874219",
        tuple(corpus_re004) + unrelated_references(60)
    ))

    # RE005
    scenarios.append(ReferenceEvidenceScenario(
        "RE005", "Rare three-digit shared token",
        "OMD-001", "NSS-001",
        ("OMD-001", "NSS-001") + unrelated_references(98)
    ))

    # RE006
    corpus_re006 = ["OMD-001", "NSS-001"] + [f"DOC{i}-001" for i in range(38)]
    scenarios.append(ReferenceEvidenceScenario(
        "RE006", "Common three-digit shared token",
        "OMD-001", "NSS-001",
        tuple(corpus_re006) + unrelated_references(60)
    ))

    # RE007
    corpus_re007 = ["INV-2026-874219", "AB/2026/874219"] + ["XX-2026"] * 3
    scenarios.append(ReferenceEvidenceScenario(
        "RE007", "Multiple rare shared tokens",
        "INV-2026-874219", "AB/2026/874219",
        tuple(corpus_re007) + unrelated_references(95)
    ))

    # RE008
    corpus_re008 = ["INV-2026-874219", "AB/2026/874219"] + ["XX-2026"] * 78
    scenarios.append(ReferenceEvidenceScenario(
        "RE008", "One rare and one common shared token",
        "INV-2026-874219", "AB/2026/874219",
        tuple(corpus_re008) + unrelated_references(20)
    ))

    # RE009
    scenarios.append(ReferenceEvidenceScenario(
        "RE009", "Mixed known and out-of-profile evidence",
        "INV-874219", "NEW-874219",
        ("INV-874219", "DOC-874219") + unrelated_references(98)
    ))

    # RE010
    scenarios.append(ReferenceEvidenceScenario(
        "RE010", "Fully out-of-profile shared identity evidence",
        "NEW-999999", "XYZ-999999",
        unrelated_references(100)
    ))

    # RE011
    scenarios.append(ReferenceEvidenceScenario(
        "RE011", "Non-numeric rare exact identity",
        "SPECIAL-CREDIT", "SPECIALCREDIT",
        ("SPECIAL-CREDIT", "SPECIALCREDIT") + unrelated_references(98)
    ))

    # RE012
    corpus_re012 = ["2026", "2026"] + ["2026"] * 78
    scenarios.append(ReferenceEvidenceScenario(
        "RE012", "Exact identity but highly repeated numeric reference",
        "2026", "2026",
        tuple(corpus_re012) + unrelated_references(20)
    ))

    print(f"{'Case':<7}{'Exact':<8}{'Norm Stats':<45}{'Token Stats'}")
    print("-" * 85)

    for sc in scenarios:
        profile = build_reference_corpus_profile(sc.corpus_references)

        # Assertions
        if sc.scenario_id != "RE009" and sc.scenario_id != "RE010":
            assert profile.reference_count == 100

        if sc.scenario_id == "RE003":
            assert profile.numeric_token_document_frequency["874219"] == 2
        elif sc.scenario_id == "RE004":
            assert profile.numeric_token_document_frequency["874219"] == 40
        elif sc.scenario_id == "RE006":
            assert profile.numeric_token_document_frequency["001"] == 40
        elif sc.scenario_id == "RE007":
            assert profile.numeric_token_document_frequency["2026"] == 5
            assert profile.numeric_token_document_frequency["874219"] == 2
        elif sc.scenario_id == "RE008":
            assert profile.numeric_token_document_frequency["2026"] == 80
            assert profile.numeric_token_document_frequency["874219"] == 2
        elif sc.scenario_id == "RE012":
            assert profile.normalized_reference_frequency["2026"] == 80
            assert profile.numeric_token_document_frequency["2026"] == 80

        identity = extract_reference_identity(sc.reference_a, sc.reference_b)
        assert identity is not None
        enriched = enrich_reference_identity(identity, profile)

        exact_str = "yes" if enriched.identity.exact_normalized_match else "no"
        norm_str = format_norm_stats(enriched)
        token_str = format_token_stats(enriched)

        if "unavailable" not in norm_str and "?" not in norm_str and norm_str != "none":
            norm_str = ", ".join([f"{n}/{profile.reference_count}" if ":" in n else n for n in norm_str.split(", ")])
        else:
            # We add /100 only to valid stats
            parts = norm_str.split(", ")
            new_parts = []
            for p in parts:
                if ":" in p and "?" not in p:
                    new_parts.append(f"{p}/{profile.reference_count}")
                else:
                    new_parts.append(p)
            norm_str = ", ".join(new_parts)

        if "unavailable" not in token_str and "?" not in token_str and token_str != "none":
            token_str = ", ".join([f"{n}/{profile.reference_count}" if ":" in n else n for n in token_str.split(", ")])
        else:
            parts = token_str.split(", ")
            new_parts = []
            for p in parts:
                if ":" in p and "?" not in p:
                    new_parts.append(f"{p}/{profile.reference_count}")
                else:
                    new_parts.append(p)
            token_str = ", ".join(new_parts)

        print(f"{sc.scenario_id:<7}{exact_str:<8}{norm_str:<45}{token_str}")

if __name__ == '__main__':
    main()
