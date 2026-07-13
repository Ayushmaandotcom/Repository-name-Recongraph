import sys
import os

# Ensure the src directory is in the path for importing recongraph
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from recongraph.matching.reference_evidence import ReferenceEvidencePolicy

def shortest_repeating_unit(token: str) -> str:
    n = len(token)
    for unit_length in range(1, n // 2 + 1):
        if n % unit_length == 0:
            candidate = token[:unit_length]
            if candidate * (n // unit_length) == token:
                return candidate
    return "none"

def evaluate_structural_magnitude():
    policy = ReferenceEvidencePolicy()
    
    tokens = [
        "01",
        "001",
        "000",
        "111",
        "123",
        "2026",
        "1001",
        "9999",
        "874219",
        "999999",
        "123456",
        "121212",
        "000001",
        "87421982",
        "123123",
        "101010",
        "987654321"
    ]
    
    results = []
    
    for token in tokens:
        n = len(token)
        unique_digit_count = len(set(token))
        digit_diversity_ratio = unique_digit_count / n
        single_symbol_repeated = (unique_digit_count == 1)
        repeating_unit = shortest_repeating_unit(token)
        periodic = (repeating_unit != "none")
        
        # Determine fallback band
        if n <= policy.short_token_max_length:
            fallback_band = "short"
            base_magnitude = policy.short_token_fallback
        elif n <= policy.medium_token_max_length:
            fallback_band = "medium"
            base_magnitude = policy.medium_token_fallback
        else:
            fallback_band = "long"
            base_magnitude = policy.long_token_fallback
            
        single_symbol_discounted = base_magnitude * policy.repeated_pattern_discount if single_symbol_repeated else base_magnitude
        periodic_discounted = base_magnitude * policy.repeated_pattern_discount if periodic else base_magnitude
        
        results.append({
            "token": token,
            "length": n,
            "unique_digit_count": unique_digit_count,
            "digit_diversity_ratio": digit_diversity_ratio,
            "single_symbol_repeated": single_symbol_repeated,
            "shortest_repeating_unit": repeating_unit,
            "periodic": periodic,
            "fallback_band": fallback_band,
            "base_fallback_magnitude": base_magnitude,
            "magnitude_if_single_symbol_discount": single_symbol_discounted,
            "magnitude_if_periodic_discount": periodic_discounted
        })
        
    # Assertions
    # 1. 000 is single-symbol repeated and periodic.
    t000 = next(r for r in results if r["token"] == "000")
    assert t000["single_symbol_repeated"] and t000["periodic"]
    
    # 2. 999999 is single-symbol repeated and periodic.
    t999999 = next(r for r in results if r["token"] == "999999")
    assert t999999["single_symbol_repeated"] and t999999["periodic"]
    
    # 3. 121212 is periodic but not single-symbol repeated.
    t121212 = next(r for r in results if r["token"] == "121212")
    assert t121212["periodic"] and not t121212["single_symbol_repeated"]
    
    # 4. 123123 has shortest repeating unit "123".
    t123123 = next(r for r in results if r["token"] == "123123")
    assert t123123["shortest_repeating_unit"] == "123"
    
    # 5. 874219 is not periodic.
    t874219 = next(r for r in results if r["token"] == "874219")
    assert not t874219["periodic"]
    
    # 6. 000001 is not periodic.
    t000001 = next(r for r in results if r["token"] == "000001")
    assert not t000001["periodic"]
    
    # 7. Discounting never increases magnitude.
    # 8. All diagnostic magnitudes remain in [0.0, 1.0].
    # 9. A token with no detected pattern has identical base, single-symbol-discount, and periodic-discount magnitudes.
    for r in results:
        assert r["magnitude_if_single_symbol_discount"] <= r["base_fallback_magnitude"]
        assert r["magnitude_if_periodic_discount"] <= r["base_fallback_magnitude"]
        assert 0.0 <= r["base_fallback_magnitude"] <= 1.0
        assert 0.0 <= r["magnitude_if_single_symbol_discount"] <= 1.0
        assert 0.0 <= r["magnitude_if_periodic_discount"] <= 1.0
        
        if not r["single_symbol_repeated"] and not r["periodic"]:
            assert r["base_fallback_magnitude"] == r["magnitude_if_single_symbol_discount"] == r["magnitude_if_periodic_discount"]
    
    # 10. The experiment does not mutate ReferenceEvidencePolicy.
    # Dataclass is frozen, so it can't mutate. But we can assert the defaults remain identical to fresh instantiation.
    policy2 = ReferenceEvidencePolicy()
    assert policy.short_token_max_length == policy2.short_token_max_length
    assert policy.repeated_pattern_discount == policy2.repeated_pattern_discount
    
    print("ALL ASSERTIONS PASSED\n")
    
    print("FULL DIAGNOSTIC TABLE")
    print(f"{'Token':<12} | {'Len':<3} | {'Uniq':<4} | {'Div':<5} | {'SingleRep':<9} | {'ShortUnit':<10} | {'Periodic':<8} | {'Band':<6} | {'Base':<4} | {'SingleDisc':<10} | {'PeriodDisc':<10}")
    print("-" * 120)
    for r in results:
        print(f"{r['token']:<12} | {r['length']:<3} | {r['unique_digit_count']:<4} | {r['digit_diversity_ratio']:<5.2f} | {str(r['single_symbol_repeated']):<9} | {str(r['shortest_repeating_unit']):<10} | {str(r['periodic']):<8} | {r['fallback_band']:<6} | {r['base_fallback_magnitude']:<4.2f} | {r['magnitude_if_single_symbol_discount']:<10.2f} | {r['magnitude_if_periodic_discount']:<10.2f}")
    
    print("\n\nHN004 STRUCTURAL COMPARISON")
    print(f"{'Token':<12} | {'Fallback Band':<15} | {'Base Mag':<8} | {'Single-Symbol Disc':<18} | {'Periodic Disc':<15}")
    print("-" * 75)
    compare_tokens = ["001", "874219", "999999", "121212"]
    for r in results:
        if r["token"] in compare_tokens:
            print(f"{r['token']:<12} | {r['fallback_band']:<15} | {r['base_fallback_magnitude']:<8.2f} | {r['magnitude_if_single_symbol_discount']:<18.2f} | {r['magnitude_if_periodic_discount']:<15.2f}")

if __name__ == "__main__":
    evaluate_structural_magnitude()
