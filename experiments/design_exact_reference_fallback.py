import sys
import os

# Ensure the src directory is in the path for importing recongraph
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import ReferenceEvidencePolicy

def evaluate_exact_reference_fallback_design():
    policy = ReferenceEvidencePolicy()
    
    # Candidate Option B values
    candidate_exact_fallbacks = [0.40, 0.50, 0.60, 0.70]
    
    # Candidate Option C lengths
    # short: <= 5, medium: <= 8, long: > 8
    def opt_c_magnitude(ref: str) -> float:
        n = len(ref)
        if n <= 5: return 0.20
        if n <= 8: return 0.40
        return 0.60

    cases = [
        {
            "id": "EF001",
            "ref_a": "INV-999999", "ref_b": "INV/999999",
            "exact": True,
            "norm_val": "inv999999",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF002",
            "ref_a": "CREDIT-NOTE", "ref_b": "CREDITNOTE",
            "exact": True,
            "norm_val": "creditnote",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF003",
            "ref_a": "SB-8891", "ref_b": "SB8891",
            "exact": True,
            "norm_val": "sb8891",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF004",
            "ref_a": "A", "ref_b": "A",
            "exact": True,
            "norm_val": "a",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF005",
            "ref_a": "000000", "ref_b": "000000",
            "exact": True,
            "norm_val": "000000",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF006",
            "ref_a": "INV-001", "ref_b": "INV/001",
            "exact": True,
            "norm_val": "inv001",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF007",
            "ref_a": "A-VERY-LONG-GENERIC-REFERENCE", "ref_b": "AVERYLONGGENERICREFERENCE",
            "exact": True,
            "norm_val": "averylonggenericreference",
            "primary": "exact normalized identity"
        },
        {
            "id": "EF008",
            "ref_a": "INV-874219", "ref_b": "AB/874219",
            "exact": False,
            "norm_val": "874219 (token)",
            "primary": "shared numeric token"
        },
        {
            "id": "EF009",
            "ref_a": "INV-001", "ref_b": "ABC-001",
            "exact": False,
            "norm_val": "001 (token)",
            "primary": "shared numeric token"
        }
    ]
    
    print("EXACT REFERENCE FALLBACK DESIGN EXPERIMENT")
    print("-" * 120)
    
    for c in cases:
        print(f"Case: {c['id']}")
        print(f"Norm Ref/Token: {c['norm_val']}")
        print(f"Exact Match: {c['exact']}")
        print(f"Primary Unit: {c['primary']}")
        
        if c['exact']:
            opt_a = policy.long_token_fallback
            opt_c = opt_c_magnitude(c['norm_val'])
            opt_d = 0.0
            opt_e = "refused"
            print(f"Option A (reuse long_token_fallback): {opt_a}")
            print(f"Option B (candidate exact_reference_fallback values): {candidate_exact_fallbacks}")
            print(f"Option C (length derived diagnostic): {opt_c}")
            print(f"Option D (zero magnitude): {opt_d}")
            print(f"Option E (refuse interpretation): {opt_e}")
        else:
            # For numeric token, just use the token fallback
            # but extract just the digits for length
            tok = c['norm_val'].split(" ")[0]
            if len(tok) <= policy.short_token_max_length: mag = policy.short_token_fallback
            elif len(tok) <= policy.medium_token_max_length: mag = policy.medium_token_fallback
            else: mag = policy.long_token_fallback
            print(f"Standard numeric token magnitude: {mag}")
            
        print("-" * 60)

if __name__ == "__main__":
    evaluate_exact_reference_fallback_design()
