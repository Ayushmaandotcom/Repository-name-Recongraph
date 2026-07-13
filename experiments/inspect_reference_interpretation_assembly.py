import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity,
    enrich_reference_identity, _construct_reference_evidence_contributions,
    _select_strongest_reference_contribution, _assemble_reference_evidence_interpretation
)

def evaluate_reference_interpretation_assembly():
    policy = ReferenceEvidencePolicy()
    
    cases = [
        {"id": "RA001", "desc": "rare profiled exact identity", "a": "INV-874219", "b": "INV/874219", "prof": {"inv874219": 1}, "tok_prof": {}},
        {"id": "RA002", "desc": "ubiquitous profiled exact identity", "a": "CREDIT NOTE", "b": "creditnote", "prof": {"creditnote": 100}, "tok_prof": {}},
        {"id": "RA003", "desc": "out-of-profile exact identity", "a": "INV-999999", "b": "INV/999999", "prof": {}, "tok_prof": {}},
        {"id": "RA004", "desc": "rare profiled shared token", "a": "INV-874219", "b": "AB-874219", "prof": {}, "tok_prof": {"874219": 1}},
        {"id": "RA005", "desc": "common profiled shared token", "a": "INV-2026", "b": "AB-2026", "prof": {}, "tok_prof": {"2026": 36}},
        {"id": "RA006", "desc": "out-of-profile long token", "a": "INV-121212", "b": "AB-121212", "prof": {}, "tok_prof": {}},
        {"id": "RA007", "desc": "out-of-profile repeated long token", "a": "INV-999999", "b": "AB-999999", "prof": {}, "tok_prof": {}},
        {"id": "RA008", "desc": "profiled 0.60 vs fallback 0.60", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 16}}, 
        {"id": "RA009", "desc": "profiled slightly below 0.60 vs fallback 0.60", "a": "INV-874219-121212", "b": "AB-874219-121212", "prof": {}, "tok_prof": {"874219": 17}}, 
        {"id": "RA010", "desc": "complete profiled tie with two tokens", "a": "INV-2026-874219", "b": "AB-2026-874219", "prof": {}, "tok_prof": {"2026": 1, "874219": 1}},
    ]
    
    print("REFERENCE EVIDENCE INTERPRETATION ASSEMBLY INSPECTION")
    print("-" * 100)
    for c in cases:
        print(f"Case: {c['id']} - {c['desc']}")
        
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
        
        print("Ordered contributions:")
        for i, contrib in enumerate(contributions):
            print(f"  Index {i}:")
            print(f"    evidence_kind: {contrib.evidence_kind}")
            print(f"    identity_value: {contrib.identity_value}")
            print(f"    positive_evidence: {repr(contrib.positive_evidence)}")
            print(f"    statistics_available: {contrib.statistics_available}")
            
        winner = _select_strongest_reference_contribution(contributions)
        print("Frozen selector winner:")
        print(f"  evidence_kind: {winner.evidence_kind}")
        print(f"  identity_value: {winner.identity_value}")
        print(f"  positive_evidence: {repr(winner.positive_evidence)}")
        print(f"  statistics_available: {winner.statistics_available}")
        
        interp = _assemble_reference_evidence_interpretation(contributions)
        print("Interpretation:")
        print(f"  score: {repr(interp.score)}")
        print(f"  statistical_coverage: {repr(interp.statistical_coverage)}")
        print(f"  contribution count: {len(interp.contributions)}")
        print("-" * 60)

if __name__ == "__main__":
    evaluate_reference_interpretation_assembly()
