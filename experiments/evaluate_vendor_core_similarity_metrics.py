import difflib

def exact_match(a: str, b: str) -> float:
    return 1.0 if a == b else 0.0

def token_set_match(a: str, b: str) -> float:
    set_a = set(a.split())
    set_b = set(b.split())
    return 1.0 if set_a == set_b else 0.0

def sequence_matcher_ratio(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b).ratio()

def evaluate_metrics(a: str, b: str):
    print(f"Comparing: '{a}' <-> '{b}'")
    print(f"  Exact Match : {exact_match(a, b):.2f}")
    print(f"  Token Set   : {token_set_match(a, b):.2f}")
    print(f"  Seq Matcher : {sequence_matcher_ratio(a, b):.2f}")
    print()

def main():
    print("--- Vendor Core Similarity Experiment ---\n")
    
    pairs = [
        ("ABC", "ABC"),
        ("ABC TRADERS", "ABC TRADERS"),
        ("BALAJI ENTERPRISES", "ENTERPRISES BALAJI"),
        ("TATA MOTORS", "TATA POWER"),
        ("ABC", "ADC"),
        ("NEW INDIA TRADING CO", "NEW INDIA TRADERS"),
    ]
    
    for a, b in pairs:
        evaluate_metrics(a, b)

if __name__ == "__main__":
    main()
