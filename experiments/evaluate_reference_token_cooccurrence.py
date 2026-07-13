import re
from dataclasses import dataclass
from typing import Tuple

from recongraph.matching.reference_evidence import build_reference_corpus_profile

@dataclass(frozen=True)
class TokenCooccurrenceScenario:
    scenario_id: str
    description: str
    token_a: str
    token_b: str
    corpus_references: tuple[str, ...]

def unrelated_references(count: int, *, start: int = 500_000) -> tuple[str, ...]:
    return tuple(f"OTHER-{start + i}" for i in range(count))

def token_document_sets(references: tuple[str, ...]) -> dict[str, set[int]]:
    token_docs = {}
    for i, ref in enumerate(references):
        if ref:
            tokens = set(re.findall(r"\d+", ref))
            for t in tokens:
                if t not in token_docs:
                    token_docs[t] = set()
                token_docs[t].add(i)
    return token_docs

def main():
    scenarios = []

    # CO001 - Perfect co-occurrence
    # 20 both, 80 unrelated
    # Avoid creating '000001' as a numeric token. We will use letters instead for unique identifiers.
    # E.g. DOC-2026-874219-A, DOC-2026-874219-B...
    # But letters alone might run out, so let's just use a prefix: DOCA-2026-874219, DOCB-2026-874219, etc.
    # Wait, python can just do chr() or just use a non-numeric suffix like -x1... no wait, \d+ catches 1.
    # Just use alphabetic suffix: DOC-2026-874219-a, DOC-2026-874219-b
    import string
    alphabet = string.ascii_lowercase
    docs_co001 = [f"DOC-{2026}-{874219}-{alphabet[i]}" for i in range(20)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO001", "Perfect co-occurrence",
        "2026", "874219",
        tuple(docs_co001) + unrelated_references(80)
    ))

    # CO002 - Independent-looking marginals with zero overlap
    # 20 only 2026, 20 only 874219, 60 unrelated
    docs_co002_a = [f"DOCA-{2026}-{alphabet[i]}" for i in range(20)]
    docs_co002_b = [f"DOCB-{874219}-{alphabet[i]}" for i in range(20)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO002", "Independent-looking marginals with zero overlap",
        "2026", "874219",
        tuple(docs_co002_a + docs_co002_b) + unrelated_references(60)
    ))

    # CO003 - Partial co-occurrence
    # 10 both, 10 only 2026, 10 only 874219, 70 unrelated
    docs_co003_both = [f"DOC-{2026}-{874219}-{alphabet[i]}" for i in range(10)]
    docs_co003_a = [f"DOCA-{2026}-{alphabet[i]}" for i in range(10)]
    docs_co003_b = [f"DOCB-{874219}-{alphabet[i]}" for i in range(10)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO003", "Partial co-occurrence",
        "2026", "874219",
        tuple(docs_co003_both + docs_co003_a + docs_co003_b) + unrelated_references(70)
    ))

    # CO004 - Rare token nested inside common token
    # DF(2026) = 80, DF(874219) = 2, joint = 2
    # 2 both, 78 only 2026, 20 unrelated
    docs_co004_both = [f"DOC-{2026}-{874219}-{alphabet[i]}" for i in range(2)]
    # We need 78 for 2026 only, alphabet is only 26, so we can use letters multiple times or just random words.
    # To avoid numeric suffixes:
    docs_co004_a = [f"DOCA-{2026}-" + ("a" * (i//26 + 1)) + alphabet[i%26] for i in range(78)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO004", "Rare token nested inside common token",
        "2026", "874219",
        tuple(docs_co004_both + docs_co004_a) + unrelated_references(20)
    ))

    # CO005 - Two rare tokens with limited overlap
    # DF(991827) = 5, DF(874219) = 5, joint = 1
    # 1 both, 4 only 991827, 4 only 874219, 91 unrelated
    docs_co005_both = [f"DOC-{991827}-{874219}-a"]
    docs_co005_a = [f"DOCA-{991827}-{alphabet[i]}" for i in range(4)]
    docs_co005_b = [f"DOCB-{874219}-{alphabet[i]}" for i in range(4)]
    scenarios.append(TokenCooccurrenceScenario(
        "CO005", "Two rare tokens with limited overlap",
        "991827", "874219",
        tuple(docs_co005_both + docs_co005_a + docs_co005_b) + unrelated_references(91)
    ))

    print(f"{'Case':<7}{'Token A':<9}{'DF(A)':<7}{'Token B':<9}{'DF(B)':<7}{'Joint DF':<10}{'Rate(B|A)':<11}{'Rate(A|B)'}")
    print("-" * 76)

    profiles = {}
    joint_dfs = {}

    for sc in scenarios:
        assert len(sc.corpus_references) == 100

        token_docs = token_document_sets(sc.corpus_references)
        docs_a = token_docs.get(sc.token_a, set())
        docs_b = token_docs.get(sc.token_b, set())

        df_a = len(docs_a)
        df_b = len(docs_b)
        joint_df = len(docs_a & docs_b)

        if sc.scenario_id == "CO001":
            assert df_a == 20
            assert df_b == 20
            assert joint_df == 20
        elif sc.scenario_id == "CO002":
            assert df_a == 20
            assert df_b == 20
            assert joint_df == 0
        elif sc.scenario_id == "CO003":
            assert df_a == 20
            assert df_b == 20
            assert joint_df == 10
        elif sc.scenario_id == "CO004":
            assert df_a == 80
            assert df_b == 2
            assert joint_df == 2
        elif sc.scenario_id == "CO005":
            assert df_a == 5
            assert df_b == 5
            assert joint_df == 1

        rate_b_given_a = joint_df / df_a if df_a > 0 else 0.0
        rate_a_given_b = joint_df / df_b if df_b > 0 else 0.0

        profiles[sc.scenario_id] = build_reference_corpus_profile(sc.corpus_references)
        joint_dfs[sc.scenario_id] = joint_df

        print(f"{sc.scenario_id:<7}{sc.token_a:<9}{df_a:<7}{sc.token_b:<9}{df_b:<7}{joint_df:<10}{rate_b_given_a:<11.4f}{rate_a_given_b:.4f}")

    profile_co001 = profiles["CO001"]
    profile_co002 = profiles["CO002"]

    assert profile_co001.reference_count == profile_co002.reference_count
    assert (
        profile_co001.numeric_token_document_frequency["2026"]
        ==
        profile_co002.numeric_token_document_frequency["2026"]
    )
    assert (
        profile_co001.numeric_token_document_frequency["874219"]
        ==
        profile_co002.numeric_token_document_frequency["874219"]
    )
    assert joint_dfs["CO001"] != joint_dfs["CO002"]

if __name__ == '__main__':
    main()
