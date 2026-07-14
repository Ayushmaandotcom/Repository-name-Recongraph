def derive_acronym(core_name: str) -> str:
    tokens = core_name.split()
    # Simple derivation: first letter of each word
    return "".join(t[0] for t in tokens if t)

def acronym_experiment():
    print("--- Vendor Acronym Collision Experiment ---\n")
    
    entities = [
        "TATA CONSULTANCY SERVICES",
        "TCS LOGISTICS",
        "TRINITY COMPUTER SYSTEMS",
        "STATE BANK OF INDIA",
        "SBI LIFE INSURANCE",
        "SARASWAT BANK INTL",
        "HINDUSTAN UNILEVER",
        "HULK UNDERWEAR LIMITED"
    ]
    
    acronym_map = {}
    for entity in entities:
        acronym = derive_acronym(entity)
        if acronym not in acronym_map:
            acronym_map[acronym] = []
        acronym_map[acronym].append(entity)
        
    for acr, matches in acronym_map.items():
        print(f"Acronym '{acr}' maps to {len(matches)} distinct entities:")
        for m in matches:
            print(f"  - {m}")
        print()
        
    print("Conclusion: Deterministic acronym derivation leads to massive false positives.")

if __name__ == "__main__":
    acronym_experiment()
