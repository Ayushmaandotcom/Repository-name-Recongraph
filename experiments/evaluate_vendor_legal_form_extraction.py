import re
from typing import Tuple, Optional, List

# Priority ordered legal form patterns. 
# Multi-token patterns must come first.
LEGAL_FORM_PATTERNS = [
    (r'\bLIMITED LIABILITY PARTNERSHIP\b', 'LIMITED_LIABILITY_PARTNERSHIP'),
    (r'\bPRIVATE LIMITED\b', 'PRIVATE_LIMITED'),
    (r'\bPVT\.?\s*LTD\.?\b', 'PRIVATE_LIMITED'),
    (r'\b\(P\)\s*LTD\.?\b', 'PRIVATE_LIMITED'),
    (r'\bONE PERSON COMPANY\b', 'ONE_PERSON_COMPANY'),
    (r'\bSECTION 8 COMPANY\b', 'SECTION_8_COMPANY'),
    (r'\bPUBLIC LIMITED\b', 'PUBLIC_LIMITED'),
    (r'\bLLP\.?\b', 'LIMITED_LIABILITY_PARTNERSHIP'),
    (r'\bLTD\.?\b', 'LIMITED'),
    (r'\bLIMITED\b', 'LIMITED'),
    (r'\bOPC\b', 'ONE_PERSON_COMPANY'),
    (r'\bHUF\b', 'HINDU_UNDIVIDED_FAMILY'),
]

def extract_legal_form(vendor_name: str) -> Tuple[Optional[str], Optional[str], List[str]]:
    """
    Extracts legal form and organization core from vendor name.
    Information extraction precedes information removal.
    """
    events = []
    
    # 1. Unicode/whitespace canonicalization event simulation
    canonical_name = ' '.join(vendor_name.upper().split())
    if canonical_name != vendor_name:
        events.append(f"WHITESPACE_COLLAPSED: '{vendor_name}' -> '{canonical_name}'")
        
    # We do not extract 'COMPANY' or 'CO' in Indian context due to high ambiguity (e.g. FORD MOTOR COMPANY).
    # We search from the end using regex, but since we want to be safe, we'll try to find the match that's at the end.
    
    best_match = None
    best_form = None
    best_start = -1
    
    for pattern, canonical_form in LEGAL_FORM_PATTERNS:
        # Search for pattern at the end of the string first
        match = re.search(pattern + r'$', canonical_name)
        if match:
            best_match = match
            best_form = canonical_form
            best_start = match.start()
            break
            
        # If not at the end, look anywhere
        if not best_match:
            match = re.search(pattern, canonical_name)
            if match:
                # We'll take the first one we find, but end-matches take priority
                # Actually, let's stick to the simplest priority matching.
                pass 
                # For this experiment, we will just use the first priority match we find, 
                # but we prefer it to be at the end.
                
    for pattern, canonical_form in LEGAL_FORM_PATTERNS:
        matches = list(re.finditer(pattern, canonical_name))
        if matches:
            # Prefer the last match
            best_match = matches[-1]
            best_form = canonical_form
            break
            
    if best_match:
        org_core = canonical_name[:best_match.start()].strip() + " " + canonical_name[best_match.end():].strip()
        org_core = org_core.strip()
        events.append(f"LEGAL_FORM_RECOGNIZED: '{best_match.group()}' -> '{best_form}'")
        return org_core if org_core else None, best_form, events
        
    return canonical_name, None, events


def main():
    test_cases = [
        ("ABC PRIVATE LIMITED", "ABC", "PRIVATE_LIMITED"),
        ("ABC PVT LTD", "ABC", "PRIVATE_LIMITED"),
        ("ABC PVT. LTD.", "ABC", "PRIVATE_LIMITED"),
        ("ABC LLP", "ABC", "LIMITED_LIABILITY_PARTNERSHIP"),
        ("ABC", "ABC", None),
        ("ABC AND COMPANY", "ABC AND COMPANY", None),
        ("MAHINDRA AND MAHINDRA LIMITED", "MAHINDRA AND MAHINDRA", "LIMITED"),
        ("TATA SONS PVT LTD", "TATA SONS", "PRIVATE_LIMITED"),
        ("ABC (P) LTD", "ABC", "PRIVATE_LIMITED"),
        ("(P) LTD", None, "PRIVATE_LIMITED"),
        ("FORD MOTOR COMPANY", "FORD MOTOR COMPANY", None),
        ("STATE BANK OF INDIA", "STATE BANK OF INDIA", None)
    ]
    
    print(f"{'INPUT':<35} | {'EXP_CORE':<25} | {'ACT_CORE':<25} | {'EXP_FORM':<32} | {'ACT_FORM':<32} | {'RESULT'}")
    print("-" * 170)
    
    passes = 0
    for input_val, exp_core, exp_form in test_cases:
        act_core, act_form, _ = extract_legal_form(input_val)
        
        core_pass = act_core == exp_core
        form_pass = act_form == exp_form
        passed = core_pass and form_pass
        
        if passed:
            passes += 1
            
        print(f"{input_val:<35} | {str(exp_core):<25} | {str(act_core):<25} | {str(exp_form):<32} | {str(act_form):<32} | {'PASS' if passed else 'FAIL'}")
        
    print("-" * 170)
    print(f"Pass rate: {passes}/{len(test_cases)} ({passes/len(test_cases)*100:.1f}%)")

if __name__ == "__main__":
    main()
