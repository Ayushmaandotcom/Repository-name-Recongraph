import math

def calculate_token_idf(doc_freq: int, total_docs: int = 1000000) -> float:
    # Adding +1 to avoid division by zero and smooth
    return math.log(total_docs / (doc_freq + 1))

def token_rarity_experiment():
    print("--- Vendor Common Token Collision Experiment ---\n")
    
    # Hypothetical document frequencies in a 1M document corpus
    frequencies = {
        "ENTERPRISES": 45000,
        "TRADERS": 38000,
        "INDIA": 85000,
        "SERVICES": 62000,
        "TATA": 1500,
        "MAHINDRA": 800,
        "ZOMATO": 15,
        "RELIANCE": 2000
    }
    
    print(f"{'Token':<15} | {'Doc Freq':<10} | {'IDF Score':<10}")
    print("-" * 40)
    for token, freq in frequencies.items():
        idf = calculate_token_idf(freq)
        print(f"{token:<15} | {freq:<10} | {idf:.4f}")
        
    print("\nObservation: High frequency tokens like INDIA or ENTERPRISES have very low IDF scores, ")
    print("meaning partial matches on these tokens provide almost no semantic evidence of identity.")

if __name__ == "__main__":
    token_rarity_experiment()
