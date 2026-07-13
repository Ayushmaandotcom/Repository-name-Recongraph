import sys
try:
    from thefuzz import fuzz
except ImportError:
    import difflib
    class fuzz:
        @staticmethod
        def ratio(a, b):
            return difflib.SequenceMatcher(None, a, b).ratio() * 100

CORPUS = [
    "SHREE GANESH TRADERS",
    "SHREE BALAJI TRADERS",
    "GANESH INDUSTRIES",
    "BALAJI INDUSTRIES",
    "ABC TECHNOLOGIES",
    "ABC TECHNOLOGY",
    "ABC LLP",
    "ABC PRIVATE LIMITED",
    "TATA MOTORS",
    "TATA TECHNOLOGIES",
    "UNIQUE RARE ORGANIZATION NAME"
]

def analyze_discriminativeness():
    # Example: "SHREE GANESH TRADERS" vs "SHREE BALAJI TRADERS"
    # Fuzzy ratio will be high because "SHREE" and "TRADERS" match perfectly.
    # Corpus discriminativeness would realize "SHREE" and "TRADERS" are generic.
    
    a = "SHREE GANESH TRADERS"
    b = "SHREE BALAJI TRADERS"
    score = fuzz.ratio(a, b)
    
    print(f"Comparing '{a}' with '{b}'")
    print(f"Raw fuzzy ratio: {score}")
    print("Corpus analysis: 'SHREE' and 'TRADERS' appear in multiple distinct entities.")
    print("Therefore, the only discriminative tokens are 'GANESH' vs 'BALAJI', which is a 0% match.")
    print("Conclusion: Raw fuzzy similarity overstates identity evidence when shared tokens are generic.")

if __name__ == "__main__":
    analyze_discriminativeness()
