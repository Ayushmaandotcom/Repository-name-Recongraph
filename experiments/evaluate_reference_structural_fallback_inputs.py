def get_diversity(token: str):
    unique = len(set(token))
    length = len(token)
    return unique, unique / length

def is_repeated_pattern(token: str):
    return "yes" if len(set(token)) <= 2 else "no"

def main():
    tokens = [
        "1",
        "01",
        "001",
        "2026",
        "874219",
        "991827",
        "1234567890",
        "000000",
        "111111",
        "123123",
    ]

    print(f"{'Token':<12}{'Length':<9}{'Unique Digits':<16}{'Diversity':<12}{'Repeated-Pattern Candidate'}")
    print("-" * 78)

    for token in tokens:
        unique, diversity = get_diversity(token)
        repeated = is_repeated_pattern(token)
        print(f"{token:<12}{len(token):<9}{unique:<16}{diversity:<12.4f}{repeated}")

if __name__ == '__main__':
    main()
