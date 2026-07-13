import math
from dataclasses import dataclass

@dataclass(frozen=True)
class RarityScenario:
    scenario_id: str
    corpus_size: int
    frequency: int
    description: str

    def __post_init__(self):
        if self.corpus_size < 1:
            raise ValueError("corpus_size must be >= 1")
        if not (1 <= self.frequency <= self.corpus_size):
            raise ValueError("frequency must be between 1 and corpus_size")

def linear_rarity(f: int, n: int) -> float:
    return 1.0 - (f / n)

def normalized_log_rarity(f: int, n: int) -> float:
    if n <= 1:
        return 0.0
    return math.log(n / f) / math.log(n)

def sqrt_rarity(f: int, n: int) -> float:
    return 1.0 - math.sqrt(f / n)

def main():
    scenarios = [
        RarityScenario("RM001", 100, 1, "singleton in small corpus"),
        RarityScenario("RM002", 100, 2, "rare in small corpus"),
        RarityScenario("RM003", 100, 5, "uncommon in small corpus"),
        RarityScenario("RM004", 100, 20, "moderately common"),
        RarityScenario("RM005", 100, 80, "very common"),
        RarityScenario("RM006", 100, 100, "universal"),
        RarityScenario("RM007", 1000000, 1, "singleton in large corpus"),
        RarityScenario("RM008", 1000000, 10, "very rare in large corpus"),
        RarityScenario("RM009", 1000000, 100, "rare in large corpus"),
        RarityScenario("RM010", 1000000, 10000, "one percent frequency"),
        RarityScenario("RM011", 1000000, 500000, "half corpus"),
        RarityScenario("RM012", 1000000, 1000000, "universal"),
        RarityScenario("RM013", 100, 1, "1 percent base corpus"),
        RarityScenario("RM014", 1000, 10, "1 percent replicated corpus"),
    ]

    print(f"{'Case':<7}{'N':<11}{'f':<11}{'Rate':<11}{'Linear':<11}{'NormLog':<11}{'Sqrt':<11}{'Description'}")
    print("-" * 90)

    results = {}

    for sc in scenarios:
        n = sc.corpus_size
        f = sc.frequency
        rate = f / n

        lin = linear_rarity(f, n)
        nlog = normalized_log_rarity(f, n)
        sq = sqrt_rarity(f, n)

        results[sc.scenario_id] = {"lin": lin, "nlog": nlog, "sq": sq}

        assert 0.0 <= lin <= 1.0
        assert 0.0 <= nlog <= 1.0
        assert 0.0 <= sq <= 1.0

        if f == n:
            assert math.isclose(lin, 0.0, abs_tol=1e-9)
            assert math.isclose(nlog, 0.0, abs_tol=1e-9)
            assert math.isclose(sq, 0.0, abs_tol=1e-9)

        if sc.scenario_id == "RM001":
            assert math.isclose(lin, 0.99, abs_tol=1e-9)
            assert math.isclose(nlog, 1.0, abs_tol=1e-9)
            assert math.isclose(sq, 0.9, abs_tol=1e-9)

        print(f"{sc.scenario_id:<7}{n:<11}{f:<11}{rate:<11.6f}{lin:<11.6f}{nlog:<11.6f}{sq:<11.6f}{sc.description}")

    # Monotonicity checks
    small_cases = [s for s in scenarios if s.corpus_size == 100 and s.scenario_id.startswith("RM00")]
    small_cases.sort(key=lambda x: x.frequency)
    for i in range(1, len(small_cases)):
        prev = small_cases[i-1].scenario_id
        curr = small_cases[i].scenario_id
        assert results[prev]["lin"] >= results[curr]["lin"]
        assert results[prev]["nlog"] >= results[curr]["nlog"]
        assert results[prev]["sq"] >= results[curr]["sq"]

    large_cases = [s for s in scenarios if s.corpus_size == 1000000]
    large_cases.sort(key=lambda x: x.frequency)
    for i in range(1, len(large_cases)):
        prev = large_cases[i-1].scenario_id
        curr = large_cases[i].scenario_id
        assert results[prev]["lin"] >= results[curr]["lin"]
        assert results[prev]["nlog"] >= results[curr]["nlog"]
        assert results[prev]["sq"] >= results[curr]["sq"]

    print("\nRare-end resolution diagnostics")
    print("-" * 31)

    def print_diff(id1, id2):
        print(f"{id1} vs {id2}")
        print(f"  Linear difference: {results[id1]['lin'] - results[id2]['lin']:.6f}")
        print(f"  NormLog difference: {results[id1]['nlog'] - results[id2]['nlog']:.6f}")
        print(f"  Sqrt difference: {results[id1]['sq'] - results[id2]['sq']:.6f}")

    print_diff("RM001", "RM002")
    print_diff("RM002", "RM003")
    print_diff("RM007", "RM008")
    print_diff("RM008", "RM009")

    print("\nSame frequency-rate diagnostics")
    print("-" * 31)
    print("RM001 (N=100, f=1):")
    print(f"  Linear: {results['RM001']['lin']:.6f}")
    print(f"  NormLog: {results['RM001']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM001']['sq']:.6f}")
    print("RM010 (N=1,000,000, f=10,000):")
    print(f"  Linear: {results['RM010']['lin']:.6f}")
    print(f"  NormLog: {results['RM010']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM010']['sq']:.6f}")

    print("\nCorpus replication diagnostic")
    print("-" * 29)
    print("RM013 (N=100, f=1):")
    print(f"  Linear: {results['RM013']['lin']:.6f}")
    print(f"  NormLog: {results['RM013']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM013']['sq']:.6f}")
    print("RM014 (N=1000, f=10):")
    print(f"  Linear: {results['RM014']['lin']:.6f}")
    print(f"  NormLog: {results['RM014']['nlog']:.6f}")
    print(f"  Sqrt: {results['RM014']['sq']:.6f}")

if __name__ == "__main__":
    main()
