from recongraph.matching.signals import reference_score
from recongraph.matching.reference_evidence import extract_reference_identity

CASES = [
    ("INV-874219", "AB/874219"),
    ("INV-001", "ABC-001"),
    ("INV-999999", "ABC-999999"),
    ("INV-2026-1001", "ABC-2026-1001"),
    ("2026", "2026"),
    ("CREDITNOTE", "CREDITNOTE"),
    ("INV-01", "ABC-01"),
    ("INV-1042", "INV-1043"),
]

def main():
    print("Comparison experiment output:")
    for a, b in CASES:
        old_score = float(reference_score(a, b) or 0.0)
        evidence = extract_reference_identity(a, b)

        print(f"\nA: {a}")
        print(f"B: {b}")
        print(f"old reference_score: {old_score:.1f}")
        print("new evidence:")

        if evidence:
            exact = "true" if evidence.exact_normalized_match else "false"
            tokens = "|".join(evidence.shared_numeric_tokens) if evidence.shared_numeric_tokens else "none"
            print(f"exact normalized: {exact}")
            print(f"shared tokens: {tokens}")
        else:
            print("exact normalized: false")
            print("shared tokens: none")

if __name__ == "__main__":
    main()
