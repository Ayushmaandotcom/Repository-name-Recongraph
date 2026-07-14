import time

def mock_parse(vendor_name: str):
    # Simulate an expensive parse (canonicalization, tokenization, legal form matching)
    # We will simulate a delay of 0.1ms
    # Using a small loop to simulate CPU work
    for _ in range(1000):
        pass
    return f"parsed_{vendor_name}"

def option_a_pair_level(purchases, gsts, candidates_per_record):
    # Parses the names for every candidate pair dynamically
    start = time.time()
    parses = 0
    
    # 1000 purchases
    for p in purchases:
        # Each has 100 candidates
        for c in range(candidates_per_record):
            # Parse purchase
            mock_parse(p)
            # Parse candidate (from gsts)
            mock_parse(gsts[c % len(gsts)])
            parses += 2
            
    end = time.time()
    return parses, end - start

def option_c_pre_materialized(unique_vendors):
    # Parses exactly once per unique vendor string
    start = time.time()
    parses = 0
    cache = {}
    
    for v in unique_vendors:
        cache[v] = mock_parse(v)
        parses += 1
        
    end = time.time()
    return parses, end - start

def main():
    print("--- Vendor Parse Reuse Benchmark ---\n")
    
    num_purchases = 1000
    num_gsts = 1000
    candidates_per_record = 100
    
    # Generate mock strings
    purchases = [f"Vendor_P_{i}" for i in range(num_purchases)]
    gsts = [f"Vendor_G_{i}" for i in range(num_gsts)]
    
    unique_vendors = set(purchases + gsts)
    
    print(f"Scenario: {num_purchases} Purchases, {num_gsts} GSTs, {candidates_per_record} Candidates per Purchase")
    print(f"Unique vendor strings: {len(unique_vendors)}")
    print("-" * 50)
    
    # Run Option A
    parses_a, time_a = option_a_pair_level(purchases, gsts, candidates_per_record)
    print(f"Option A (Pair-Level Dynamic Parse):")
    print(f"  Parse Executions: {parses_a}")
    print(f"  Simulated Time: {time_a:.4f} seconds")
    
    print("-" * 50)
    
    # Run Option C
    parses_c, time_c = option_c_pre_materialized(unique_vendors)
    print(f"Option C (Pre-Materialized Artifacts):")
    print(f"  Parse Executions: {parses_c}")
    print(f"  Simulated Time: {time_c:.4f} seconds")
    
    print("-" * 50)
    print(f"Amplification Factor: {parses_a / parses_c:.1f}x")

if __name__ == "__main__":
    main()
