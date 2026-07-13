import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidenceContribution, ReferenceEvidenceKind,
    ReferenceEvidenceInterpretation, _select_strongest_reference_contribution
)

def evaluate_interpretation_state():
    def make_contrib(mag, stats, val="0"):
        return ReferenceEvidenceContribution(
            evidence_kind=ReferenceEvidenceKind.SHARED_NUMERIC_TOKEN,
            identity_value=val,
            positive_evidence=mag,
            statistics_available=stats
        )

    # IS001: A=0.60 fallback, B=0.60 profiled. Selector winner: B (profiled)
    # Attempt: score=0.60, coverage=0.0
    c_a = make_contrib(0.60, False, val="1")
    c_b = make_contrib(0.60, True, val="2")
    winner1 = _select_strongest_reference_contribution((c_a, c_b))
    
    cases = [
        {
            "id": "IS001",
            "contribs": (c_a, c_b),
            "winner": winner1,
            "score": 0.60,
            "coverage": 0.0
        },
        {
            "id": "IS002",
            "contribs": (c_a, c_b),
            "winner": winner1,
            "score": 0.60,
            "coverage": 1.0
        },
        {
            "id": "IS003",
            "contribs": (make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2"))),
            "score": 0.70,
            "coverage": 1.0
        },
        {
            "id": "IS004",
            "contribs": (make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.70, False, val="1"), make_contrib(0.60, True, val="2"))),
            "score": 0.70,
            "coverage": 0.0
        },
        {
            "id": "IS005",
            "contribs": (make_contrib(0.60, True, val="2026"), make_contrib(0.60, True, val="874219")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.60, True, val="2026"), make_contrib(0.60, True, val="874219"))),
            "score": 0.60,
            "coverage": 1.0
        },
        {
            "id": "IS006",
            "contribs": (make_contrib(0.60, True, val="874219"), make_contrib(0.60, True, val="2026")),
            "winner": _select_strongest_reference_contribution((make_contrib(0.60, True, val="874219"), make_contrib(0.60, True, val="2026"))),
            "score": 0.60,
            "coverage": 1.0
        }
    ]

    for case in cases:
        print(f"Case: {case['id']}")
        print(f"Ordered contribution identities: {[c.identity_value for c in case['contribs']]}")
        print(f"Selector winner: {case['winner'].identity_value} (mag={case['winner'].positive_evidence}, stats={case['winner'].statistics_available})")
        print(f"Attempted score: {case['score']}")
        print(f"Attempted coverage: {case['coverage']}")
        
        try:
            interp = ReferenceEvidenceInterpretation(
                score=case['score'],
                statistical_coverage=case['coverage'],
                contributions=case['contribs']
            )
            print("Construction succeeded? True")
            print("What invariant accepted/rejected the state? Accepted (current model does not fully link coverage/winner provenance)")
        except ValueError as e:
            print("Construction succeeded? False")
            print(f"What invariant accepted/rejected the state? Rejected: {str(e)}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate_interpretation_state()
