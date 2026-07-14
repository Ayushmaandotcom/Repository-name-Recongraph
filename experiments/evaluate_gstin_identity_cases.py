import re

def validate_gstin(gstin: str) -> bool:
    if not gstin or len(gstin) != 15:
        return False
    pattern = r"^[0-3][0-9][A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$"
    return bool(re.match(pattern, gstin))

def extract_pan(gstin: str) -> str | None:
    if not validate_gstin(gstin):
        return None
    return gstin[2:12]

def extract_state_code(gstin: str) -> str | None:
    if not validate_gstin(gstin):
        return None
    return gstin[0:2]

def evaluate_gstin_pair(gstin_a: str, gstin_b: str):
    print(f"Comparing: {gstin_a} <-> {gstin_b}")
    
    val_a = validate_gstin(gstin_a)
    val_b = validate_gstin(gstin_b)
    
    if not val_a or not val_b:
        print("  -> UNINTERPRETABLE_INPUT (Validation Failed)")
        return
        
    pan_a = extract_pan(gstin_a)
    pan_b = extract_pan(gstin_b)
    
    state_a = extract_state_code(gstin_a)
    state_b = extract_state_code(gstin_b)
    
    print(f"  PAN A: {pan_a} | PAN B: {pan_b}")
    print(f"  State A: {state_a} | State B: {state_b}")
    
    if gstin_a == gstin_b:
        print("  -> SUPPORT identity.same_gst_registration 1.0")
    else:
        print("  -> CONFLICT identity.same_gst_registration 1.0")
        
    if pan_a == pan_b:
        print("  -> SUPPORT identity.same_tax_identity 1.0")
    else:
        print("  -> CONFLICT identity.same_tax_identity 1.0")
    print()

def main():
    print("--- GSTIN Identity Experiment ---\n")
    # Same
    evaluate_gstin_pair("07ABCDE1234F1Z5", "07ABCDE1234F1Z5")
    
    # Same PAN, diff state
    evaluate_gstin_pair("07ABCDE1234F1Z5", "29ABCDE1234F1Z5")
    
    # Diff PAN
    evaluate_gstin_pair("07ABCDE1234F1Z5", "07XYZDE9876Q1Z5")
    
    # OCR Error (O instead of 0)
    evaluate_gstin_pair("07ABCDE1234F1Z5", "O7ABCDE1234F1Z5")

if __name__ == "__main__":
    main()
