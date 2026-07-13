import math
from collections import Counter
from dataclasses import dataclass
from typing import Set

from recongraph.normalization.text import (
    extract_numeric_reference_tokens,
    normalize_reference,
)
from recongraph.matching.signals import reference_score

@dataclass(frozen=True)
class CorpusReference:
    record_id: str
    source: str
    reference: str

@dataclass(frozen=True)
class ReferenceCase:
    case_id: str
    reference_a: str
    reference_b: str
    expected_relationship: str

def generate_hostile_corpus() -> list[CorpusReference]:
    corpus = []

    # Family A - Common low-number invoice sequences (purchase)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"A{i:03d}", "purchase", f"INV-{i:03d}"))

    # Family B - Another vendor's low sequences (gst)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"B{i:03d}", "gst", f"ABC-{i:03d}"))

    # Family C - Purchase orders (ledger)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"C{i:03d}", "ledger", f"PO-{i:03d}"))

    # Family D - Transaction references (bank)
    for i in range(1, 31):
        corpus.append(CorpusReference(f"D{i:03d}", "bank", f"TXN-{i:03d}"))

    # Family E - Year-bearing references
    for i in range(1, 21):
        corpus.append(CorpusReference(f"E1{i:03d}", "purchase", f"INV-2026-{1000+i}"))
    for i in range(1, 21):
        corpus.append(CorpusReference(f"E2{i:03d}", "gst", f"GST-2026-{2000+i}"))

    # Family F - Rare genuine cross-source pairs
    rare_pairs = [
        ("purchase", "INV-874219", "gst", "AB/874219"),
        ("purchase", "INV-591842", "gst", "LEGACY/591842"),
        ("purchase", "BILL-731905", "bank", "PAYMENT/731905"),
        ("purchase", "DOC-482761", "ledger", "ENTRY/482761"),
        ("purchase", "INV-615394", "gst", "GST/615394"),
    ]
    for idx, (sa, ra, sb, rb) in enumerate(rare_pairs):
        corpus.append(CorpusReference(f"F{idx}a", sa, ra))
        corpus.append(CorpusReference(f"F{idx}b", sb, rb))

    # Family G - Repeated garbage-like tokens
    garbage_tokens = ["999999", "000001", "111111", "123456"]
    prefixes = ["INV-", "ABC-", "PO-", "TXN-"]
    sources = ["purchase", "gst", "ledger", "bank"]
    for g_idx, token in enumerate(garbage_tokens):
        for p_idx, prefix in enumerate(prefixes):
            corpus.append(CorpusReference(f"G{g_idx}{p_idx}", sources[p_idx], f"{prefix}{token}"))

    return corpus

def compute_document_frequencies(corpus: list[CorpusReference]) -> Counter:
    df: Counter[str] = Counter()
    for ref in corpus:
        tokens = set(extract_numeric_reference_tokens(ref.reference, min_length=3))
        for token in tokens:
            df[token] += 1
    return df

def corpus_rarity_gate_score(ref_a: str, ref_b: str, df: Counter, N: int) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        rate = df.get(t, 0) / N if N > 0 else 0
        if rate <= 0.02:
            max_score = max(max_score, 0.8)
    return max_score

def normalized_idf_reference_score(ref_a: str, ref_b: str, df: Counter, N: int, max_idf: float) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        dft = df.get(t, 0)
        idf = math.log(N / dft) if dft > 0 and N > 0 else 0
        norm_idf = idf / max_idf if max_idf > 0 else 0
        max_score = max(max_score, 0.8 * norm_idf)
    return max_score

def saturating_rarity_reference_score(ref_a: str, ref_b: str, df: Counter, N: int) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        dft = df.get(t, 0)
        score = 0.8 * (1.0 - (dft / N)) if N > 0 else 0.0
        max_score = max(max_score, score)
    return max_score

def collision_burden_reference_score(ref_a: str, ref_b: str, df: Counter) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a == norm_b: return 1.0

    tokens_a = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    tokens_b = set(extract_numeric_reference_tokens(ref_b, min_length=3))
    shared = tokens_a & tokens_b
    if not shared: return 0.0

    max_score = 0.0
    for t in shared:
        dft = df.get(t, 0)
        strength = 1.0 / (1.0 + math.log(dft)) if dft > 0 else 0.0
        max_score = max(max_score, 0.8 * strength)
    return max_score

def contextual_exact_reference_score(ref_a: str, ref_b: str, df: Counter) -> float:
    norm_a = normalize_reference(ref_a)
    norm_b = normalize_reference(ref_b)
    if not norm_a or not norm_b: return 0.0
    if norm_a != norm_b: return 0.0

    tokens = set(extract_numeric_reference_tokens(ref_a, min_length=3))
    if not tokens:
        return 1.0

    max_strength = 0.0
    for t in tokens:
        dft = df.get(t, 1) # use 1 for unseen in experiment
        if dft == 0:
            dft = 1
        strength = 1.0 / (1.0 + math.log(dft))
        max_strength = max(max_strength, strength)

    return 0.2 + 0.8 * max_strength

EVAL_CASES = [
    ReferenceCase("COR001", "INV-001", "ABC-001", "weak_collision"),
    ReferenceCase("COR002", "INV-002", "PO-002", "weak_collision"),
    ReferenceCase("COR003", "ABC-003", "TXN-003", "weak_collision"),
    ReferenceCase("COR004", "INV-2026-1001", "GST-2026-2001", "weak_collision"),
    ReferenceCase("COR005", "INV-999999", "ABC-999999", "weak_collision"),
    ReferenceCase("COR006", "INV-000001", "TXN-000001", "weak_collision"),
    ReferenceCase("COR007", "ABC-111111", "PO-111111", "weak_collision"),
    ReferenceCase("COR008", "INV-123456", "TXN-123456", "weak_collision"),
    ReferenceCase("COR009", "INV-874219", "AB/874219", "strong_positive"),
    ReferenceCase("COR010", "INV-591842", "LEGACY/591842", "strong_positive"),
    ReferenceCase("COR011", "BILL-731905", "PAYMENT/731905", "strong_positive"),
    ReferenceCase("COR012", "DOC-482761", "ENTRY/482761", "strong_positive"),
    ReferenceCase("COR013", "INV-615394", "GST/615394", "strong_positive"),
    ReferenceCase("COR014", "INV-1042", "INV-1043", "distinct"),
    ReferenceCase("COR015", "SB-8891", "SB-8892", "distinct"),
    ReferenceCase("COR016", "INV-2026-1001", "ABC-2026-1001", "ambiguous"),
]

EXACT_CASES = [
    ReferenceCase("EX001", "001", "001", "ambiguous"),
    ReferenceCase("EX002", "INV-001", "INV-001", "ambiguous"),
    ReferenceCase("EX003", "2026", "2026", "ambiguous"),
    ReferenceCase("EX004", "874219", "874219", "strong_positive"),
    ReferenceCase("EX005", "INV-874219", "INV-874219", "strong_positive"),
    ReferenceCase("EX006", "999999", "999999", "ambiguous"),
    ReferenceCase("EX007", "INV-123456", "INV-123456", "ambiguous"),
    ReferenceCase("EX008", "CREDITNOTE", "CREDITNOTE", "ambiguous"),
]

def main():
    corpus = generate_hostile_corpus()
    df = compute_document_frequencies(corpus)
    N = len(corpus)

    print("Corpus summary")
    print("--------------")
    print(f"Total references: {N}")
    print(f"Unique numeric tokens: {len(df)}")

    src_counts = Counter(r.source for r in corpus)
    print("Sources:")
    for src, count in src_counts.items():
        print(f"  {src}: {count}")

    print("\nMost common numeric tokens")
    print("--------------------------")
    print(f"{'Token':<11} {'DF':<8} {'DocumentRate'}")
    for token, count in df.most_common(20):
        print(f"{token:<11} {count:<8} {count/N:.4f}")

    selected_tokens = ["001", "002", "100", "2026", "999999", "000001", "111111", "123456", "874219", "591842", "731905", "482761", "615394"]
    print("\nSelected token statistics")
    print("-------------------------")
    print(f"{'Token':<11} {'DF':<8} {'DocumentRate':<18} {'RawIDF'}")
    for token in selected_tokens:
        count = df.get(token, 0)
        rate = count / N if N > 0 else 0
        raw_idf = math.log(N / count) if count > 0 and N > 0 else 0
        print(f"{token:<11} {count:<8} {rate:<18.4f} {raw_idf:.4f}")

    max_idf = math.log(N / 1) if N > 0 else 1.0

    print("\nModel comparison:")
    print(f"{'Case':<7} {'Label':<18} {'SharedTokens':<18} {'Current':<10} {'RarityGate':<12} {'NormIDF':<10} {'Saturating':<12} {'CollisionBurden'}")
    print("-" * 115)

    model_scores = {"Current": [], "RarityGate": [], "NormalizedIDF": [], "Saturating": [], "CollisionBurden": []}

    for case in EVAL_CASES:
        tokens_a = set(extract_numeric_reference_tokens(case.reference_a, min_length=3))
        tokens_b = set(extract_numeric_reference_tokens(case.reference_b, min_length=3))
        shared = "|".join(tokens_a & tokens_b)

        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        rg = corpus_rarity_gate_score(case.reference_a, case.reference_b, df, N)
        ni = normalized_idf_reference_score(case.reference_a, case.reference_b, df, N, max_idf)
        sr = saturating_rarity_reference_score(case.reference_a, case.reference_b, df, N)
        cb = collision_burden_reference_score(case.reference_a, case.reference_b, df)

        model_scores["Current"].append((case, curr))
        model_scores["RarityGate"].append((case, rg))
        model_scores["NormalizedIDF"].append((case, ni))
        model_scores["Saturating"].append((case, sr))
        model_scores["CollisionBurden"].append((case, cb))

        print(f"{case.case_id:<7} {case.expected_relationship:<18} {shared:<18} {curr:<10.4f} {rg:<12.4f} {ni:<10.4f} {sr:<12.4f} {cb:.4f}")

    print("\nModel summary")
    print("-------------")
    print(f"{'Model':<18} {'MinPositive':<14} {'MaxCollision':<14} {'Gap'}")

    for mname in ["Current", "RarityGate", "NormalizedIDF", "Saturating", "CollisionBurden"]:
        scores = model_scores[mname]
        sp = [s for c, s in scores if c.expected_relationship == "strong_positive"]
        wc = [s for c, s in scores if c.expected_relationship == "weak_collision"]
        min_sp = min(sp) if sp else 0.0
        max_wc = max(wc) if wc else 0.0
        gap = min_sp - max_wc
        print(f"{mname:<18} {min_sp:<14.4f} {max_wc:<14.4f} {gap:.4f}")

    for mname in ["Current", "RarityGate", "NormalizedIDF", "Saturating", "CollisionBurden"]:
        print(f"\n{mname} ranking")
        print("-" * (len(mname) + 8))
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        for i, (c, s) in enumerate(ranked):
            print(f"{i+1}. {c.case_id}  {c.expected_relationship}  {s:.4f}")

    print("\nWeak collisions in top 8")
    print("------------------------")
    for mname in ["Current", "RarityGate", "NormalizedIDF", "Saturating", "CollisionBurden"]:
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        top8 = ranked[:8]
        count = sum(1 for c, s in top8 if c.expected_relationship == "weak_collision")
        print(f"{mname}: {count}")

    # Mutation 1: 100 random singletons
    print("\nCorpus mutation stability")
    print("-------------------------")
    print(f"{'Model':<18} {'Before':<10} {'After':<10} {'Delta'}")

    # Calculate before scores for COR009
    cor009_a, cor009_b = "INV-874219", "AB/874219"
    ni_before = normalized_idf_reference_score(cor009_a, cor009_b, df, N, max_idf)
    sr_before = saturating_rarity_reference_score(cor009_a, cor009_b, df, N)
    cb_before = collision_burden_reference_score(cor009_a, cor009_b, df)

    # Add 100 random singletons
    corpus_mut1 = corpus.copy()
    for i in range(1, 101):
        corpus_mut1.append(CorpusReference(f"M1_{i}", "ledger", f"RANDOM-{300000+i}"))

    df_mut1 = compute_document_frequencies(corpus_mut1)
    N_mut1 = len(corpus_mut1)
    max_idf_mut1 = math.log(N_mut1 / 1) if N_mut1 > 0 else 1.0

    ni_after1 = normalized_idf_reference_score(cor009_a, cor009_b, df_mut1, N_mut1, max_idf_mut1)
    sr_after1 = saturating_rarity_reference_score(cor009_a, cor009_b, df_mut1, N_mut1)
    cb_after1 = collision_burden_reference_score(cor009_a, cor009_b, df_mut1)

    print(f"{'NormalizedIDF':<18} {ni_before:<10.4f} {ni_after1:<10.4f} {ni_after1 - ni_before:+.4f}")
    print(f"{'Saturating':<18} {sr_before:<10.4f} {sr_after1:<10.4f} {sr_after1 - sr_before:+.4f}")
    print(f"{'CollisionBurden':<18} {cb_before:<10.4f} {cb_after1:<10.4f} {cb_after1 - cb_before:+.4f}")

    # Mutation 2: 1 random sharing token
    print("\nShared-token collision mutation")
    print("-------------------------------")
    print(f"{'Model':<18} {'DF=2':<10} {'DF=3':<10} {'Delta'}")

    corpus_mut2 = corpus.copy()
    corpus_mut2.append(CorpusReference("M2_1", "ledger", "RANDOM-874219"))

    df_mut2 = compute_document_frequencies(corpus_mut2)
    N_mut2 = len(corpus_mut2)
    max_idf_mut2 = math.log(N_mut2 / 1) if N_mut2 > 0 else 1.0

    ni_after2 = normalized_idf_reference_score(cor009_a, cor009_b, df_mut2, N_mut2, max_idf_mut2)
    sr_after2 = saturating_rarity_reference_score(cor009_a, cor009_b, df_mut2, N_mut2)
    cb_after2 = collision_burden_reference_score(cor009_a, cor009_b, df_mut2)

    print(f"{'NormalizedIDF':<18} {ni_before:<10.4f} {ni_after2:<10.4f} {ni_after2 - ni_before:+.4f}")
    print(f"{'Saturating':<18} {sr_before:<10.4f} {sr_after2:<10.4f} {sr_after2 - sr_before:+.4f}")
    print(f"{'CollisionBurden':<18} {cb_before:<10.4f} {cb_after2:<10.4f} {cb_after2 - cb_before:+.4f}")

    print("\nExact-match current behavior")
    print("----------------------------")
    print(f"{'Case':<7} {'Label':<18} {'A':<15} {'B':<15} {'Current'}")
    for case in EXACT_CASES:
        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        print(f"{case.case_id:<7} {case.expected_relationship:<18} {case.reference_a:<15} {case.reference_b:<15} {curr:.4f}")

    print("\nExact-match contextual comparison")
    print("---------------------------------")
    print(f"{'Case':<7} {'Label':<18} {'Current':<10} {'ContextualExact'}")
    for case in EXACT_CASES:
        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        ctx = contextual_exact_reference_score(case.reference_a, case.reference_b, df)
        print(f"{case.case_id:<7} {case.expected_relationship:<18} {curr:<10.4f} {ctx:.4f}")

    print("\nComposite evidence diagnostics")
    print("------------------------------")
    for case in EXACT_CASES:
        norm_a = normalize_reference(case.reference_a)
        norm_b = normalize_reference(case.reference_b)
        exact = (norm_a == norm_b) and bool(norm_a)
        tokens = set(extract_numeric_reference_tokens(case.reference_a, min_length=3))

        max_strength = 0.0
        token_dfs = {}
        for t in tokens:
            dft = df.get(t, 1)
            if dft == 0: dft = 1
            token_dfs[t] = dft
            strength = 1.0 / (1.0 + math.log(dft))
            max_strength = max(max_strength, strength)

        exactness_comp = 0.2 if exact else 0.0
        info_comp = 0.8 * max_strength if tokens else 0.8

        if not tokens:
            # Our experimental logic returns 1.0 when no numeric tokens are present
            exactness_comp = 1.0
            info_comp = 0.0

        final_score = exactness_comp + info_comp

        print(f"\nCase {case.case_id}")
        print("-----------")
        print(f"normalized exact: {'yes' if exact else 'no'}")
        print(f"numeric tokens: {'|'.join(tokens) if tokens else 'none'}")
        if tokens:
            print("token df:")
            for t in tokens:
                print(f"  {t}: {token_dfs[t]}")
        print(f"max token strength: {max_strength:.4f}")
        print(f"exactness component: {exactness_comp:.4f}")
        print(f"informativeness component: {info_comp:.4f}")
        print(f"final contextual score: {final_score:.4f}")

if __name__ == "__main__":
    main()
