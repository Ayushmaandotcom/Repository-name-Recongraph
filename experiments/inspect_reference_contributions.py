import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import (
    ReferenceEvidencePolicy, ReferenceCorpusProfile, extract_reference_identity,
    enrich_reference_identity, _construct_reference_evidence_contributions
)

def evaluate_reference_contributions():
    policy = ReferenceEvidencePolicy()
    
    # We will construct a profile dynamically per test case
    
    cases = [
        {"id": "RC001", "a": "INV-874219", "b": "INV/874219"},
        {"id": "RC002", "a": "CREDIT-NOTE", "b": "CREDITNOTE"},
        {"id": "RC003", "a": "INV-999999", "b": "INV/999999"},
        {"id": "RC004", "a": "000000", "b": "000000"},
        {"id": "RC005", "a": "INV-874219", "b": "AB/874219"},
        {"id": "RC006", "a": "INV-001", "b": "ABC-001"},
        {"id": "RC007", "a": "NEW-874219", "b": "XYZ-874219"},
        {"id": "RC008", "a": "NEW-999999", "b": "XYZ-999999"},
        {"id": "RC009", "a": "INV-2026-874219", "b": "AB-2026-874219"},
    ]
    
    print("REFERENCE EVIDENCE CONTRIBUTION INSPECTION")
    print("-" * 100)
    for c in cases:
        print(f"Case: {c['id']}")
        
        identity = extract_reference_identity(c["a"], c["b"])
        if not identity:
            continue
            
        print(f"Exact Normalized Match: {identity.exact_normalized_match}")
        
        # We must carefully inject the norm refs and token DFs into the profile if needed for this script
        # But wait, our profile validation requires sum(norm_freq) == N.
        # We need to construct a valid profile per test or just a single valid one.
        # It's easier to dynamically create a profile that perfectly fits each case so we don't violate the invariant.
        
        if c['id'] == "RC001":
            p = ReferenceCorpusProfile(100, {"inv874219": 1, "dummy": 99}, {})
        elif c['id'] == "RC002":
            p = ReferenceCorpusProfile(100, {"creditnote": 100}, {})
        elif c['id'] == "RC003":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC004":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC005":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {"874219": 1})
        elif c['id'] == "RC006":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {"001": 100})
        elif c['id'] == "RC007":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC008":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {})
        elif c['id'] == "RC009":
            p = ReferenceCorpusProfile(100, {"dummy": 100}, {"2026": 10, "874219": 1})
            
        enriched = enrich_reference_identity(identity, p)
        contributions = _construct_reference_evidence_contributions(enriched, policy)
        
        print(f"Contribution Count: {len(contributions)}")
        for i, contrib in enumerate(contributions):
            print(f"  Contribution {i+1}:")
            print(f"    evidence_kind: {contrib.evidence_kind}")
            print(f"    identity_value: {contrib.identity_value}")
            print(f"    positive_evidence: {contrib.positive_evidence:.2f}")
            print(f"    statistics_available: {contrib.statistics_available}")
            
        print("-" * 60)

if __name__ == "__main__":
    evaluate_reference_contributions()
