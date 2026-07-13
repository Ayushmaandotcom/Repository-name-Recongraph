import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity,
    enrich_reference_identity, _construct_reference_evidence_contributions,
    _select_strongest_reference_contribution
)

def evaluate_reference_selection():
    policy = ReferenceEvidencePolicy()
    
    cases = [
        {"id": "RS001", "a": "INV-874219", "b": "INV/874219", "prof": {"inv874219": 1}, "tok_prof": {}},
        {"id": "RS002", "a": "INV-999999", "b": "INV/999999", "prof": {}, "tok_prof": {}},
        {"id": "RS003", "a": "INV-2026-874219", "b": "AB-2026-874219", "prof": {}, "tok_prof": {"2026": 10, "874219": 1}},
        {"id": "RS004", "a": "INV-2026-874219", "b": "AB-2026-874219", "prof": {}, "tok_prof": {"2026": 1, "874219": 1}},
        {"id": "RS005", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 16}}, # 16/100 -> 0.6 profiled vs 121212 fallback 0.6
        {"id": "RS006", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 17}}, # 17/100 -> <0.6 profiled vs 121212 fallback 0.6
    ]
    
    print("REFERENCE EVIDENCE SELECTION INSPECTION")
    print("-" * 100)
    for c in cases:
        print(f"Case: {c['id']}")
        
        identity = extract_reference_identity(c["a"], c["b"])
        if not identity:
            continue
            
        sum_norm = sum(c["prof"].values())
        norm_prof = c["prof"].copy()
        if sum_norm < 100:
            norm_prof["dummy"] = 100 - sum_norm
            
        p = ReferenceCorpusProfile(
            reference_count=100,
            normalized_reference_frequency=norm_prof,
            numeric_token_document_frequency=c["tok_prof"]
        )
            
        enriched = enrich_reference_identity(identity, p)
        contributions = _construct_reference_evidence_contributions(enriched, policy)
        
        print("Ordered Contributions:")
        for i, contrib in enumerate(contributions):
            print(f"  Index {i}:")
            print(f"    evidence_kind: {contrib.evidence_kind}")
            print(f"    identity_value: {contrib.identity_value}")
            print(f"    positive_evidence: {repr(contrib.positive_evidence)}")
            print(f"    statistics_available: {contrib.statistics_available}")
            
        winner = _select_strongest_reference_contribution(contributions)
        print("Selected Contribution:")
        print(f"  evidence_kind: {winner.evidence_kind}")
        print(f"  identity_value: {winner.identity_value}")
        print(f"  positive_evidence: {repr(winner.positive_evidence)}")
        print(f"  statistics_available: {winner.statistics_available}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate_reference_selection()
