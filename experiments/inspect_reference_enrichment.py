from recongraph.matching.reference_evidence import (
    build_reference_corpus_profile,
    enrich_reference_identity,
    extract_reference_identity,
)

PROFILE_REFS = [
    "INV-001",
    "ABC-001",
    "INV-874219",
    "CREDIT-NOTE",
    "CREDITNOTE",
]

PAIRS = [
    ("INV-001", "ABC-001"),
    ("INV-874219", "AB/874219"),
    ("NEW-999999", "XYZ-999999"),
    ("CREDIT-NOTE", "CREDITNOTE"),
    ("INV-01", "ABC-01"),
]

def main():
    profile = build_reference_corpus_profile(PROFILE_REFS)

    for a, b in PAIRS:
        print(f"\nA: {a}")
        print(f"B: {b}")

        identity = extract_reference_identity(a, b)
        if not identity:
            print("no identity evidence")
            continue

        enriched = enrich_reference_identity(identity, profile)
        print(f"exact normalized match: {enriched.identity.exact_normalized_match}")

        print("\nnormalized references:")
        for norm_ev in enriched.normalized_references:
            freq = norm_ev.statistics.frequency if norm_ev.statistics else "unavailable"
            print(f"    {norm_ev.normalized_reference}\n    {freq}")

        print("\nshared numeric tokens:")
        if not enriched.shared_numeric_tokens:
            print("    none")
        for token_ev in enriched.shared_numeric_tokens:
            df = token_ev.statistics.document_frequency if token_ev.statistics else "unavailable"
            print(f"    {token_ev.token}\n    {df}")

if __name__ == "__main__":
    main()
