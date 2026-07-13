import re
from dataclasses import dataclass
from typing import Optional

from recongraph.matching.signals import reference_score
from recongraph.normalization.text import normalize_reference

NUMERIC_TOKEN_PATTERN = re.compile(r"\d+")

def extract_numeric_tokens(reference: str) -> tuple[str, ...]:
    return tuple(NUMERIC_TOKEN_PATTERN.findall(reference))


@dataclass(frozen=True)
class ReferenceCase:
    case_id: str
    reference_a: str
    reference_b: str
    expected_relationship: str
    rationale: str


CASES = [
    ReferenceCase("REF001", "INV-1042", "AB/1042", "strong_positive", "Shared 4-digit token"),
    ReferenceCase("REF002", "SB-8891", "SB8891", "strong_positive", "Shared 4-digit token, punctuation diff"),
    ReferenceCase("REF003", "NC-2204", "NC/2204", "strong_positive", "Shared 4-digit token"),
    ReferenceCase("REF004", "MOS-781", "MOS781", "strong_positive", "Shared 3-digit token"),
    ReferenceCase("REF005", "AIS-5510", "AIS/5510", "strong_positive", "Shared 4-digit token"),
    ReferenceCase("REF006", "OMD-001", "NSS-001", "weak_collision", "Weak 3-digit token collision"),
    ReferenceCase("REF007", "ABC-002", "XYZ-002", "weak_collision", "Weak 3-digit token collision"),
    ReferenceCase("REF008", "INV-100", "PO-100", "weak_collision", "Weak 3-digit token collision"),
    ReferenceCase("REF009", "INV-874219", "AB/874219", "strong_positive", "Strong 6-digit token"),
    ReferenceCase("REF010", "TXN-987654321", "LEGACY/987654321", "strong_positive", "Very strong 9-digit token"),
    ReferenceCase("REF011", "INV-1042", "INV-1043", "distinct", "Distinct 4-digit tokens"),
    ReferenceCase("REF012", "SB-8891", "SB-8892", "distinct", "Distinct 4-digit tokens"),
    ReferenceCase("REF013", "OMD-001", "NSS-002", "distinct", "Distinct 3-digit tokens"),
    ReferenceCase("REF014", "2026-001", "2025-001", "ambiguous", "Ambiguous weak 3-digit collision across years"),
    ReferenceCase("REF015", "INV-2026-001", "PO-2026-001", "ambiguous", "Ambiguous year and weak collision"),
    ReferenceCase("REF016", "001", "001", "ambiguous", "Exact but weak"),
    ReferenceCase("REF017", "0001", "0001", "ambiguous", "Exact but weak"),
    ReferenceCase("REF018", "INV-000001", "AB-000001", "ambiguous", "6-digit collision but only significant len 1"),
    ReferenceCase("REF019", "INV-123456", "AB-123456", "strong_positive", "Sequential 6-digit"),
    ReferenceCase("REF020", "INV-999999", "ZZ-999999", "ambiguous", "Repeated 6-digit"),
]

# Probe cases added for evaluating specific failures
PROBE_CASES = [
    ReferenceCase("ProbeA", "INV-2026-874219", "AB-2025-874219", "strong_positive", "Shared 874219 but diff year"),
    ReferenceCase("ProbeB", "INV-2026-001", "PO-2026-002", "weak_collision", "Shared year 2026 but distinct seq"),
]


def model_sig_gate(reference_a: str, reference_b: str) -> float:
    norm_a = normalize_reference(reference_a)
    norm_b = normalize_reference(reference_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
        
    tokens_a = extract_numeric_tokens(reference_a)
    tokens_b = extract_numeric_tokens(reference_b)
    shared = set(tokens_a) & set(tokens_b)
    
    if not shared:
        return 0.0
        
    max_score = 0.0
    for token in shared:
        sig = token.lstrip("0") or "0"
        if len(sig) >= 4:
            max_score = max(max_score, 0.8)
    return max_score


def model_graded(reference_a: str, reference_b: str) -> float:
    norm_a = normalize_reference(reference_a)
    norm_b = normalize_reference(reference_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
        
    tokens_a = extract_numeric_tokens(reference_a)
    tokens_b = extract_numeric_tokens(reference_b)
    shared = set(tokens_a) & set(tokens_b)
    
    if not shared:
        return 0.0
        
    max_score = 0.0
    for token in shared:
        sig = token.lstrip("0") or "0"
        sig_len = len(sig)
        score = 0.0
        if sig_len >= 6:
            score = 0.8
        elif sig_len >= 4:
            score = 0.7
        elif sig_len >= 3:
            score = 0.4
        max_score = max(max_score, score)
    return max_score


def numeric_token_informativeness(token: str) -> float:
    sig = token.lstrip("0") or "0"
    sig_len = len(sig)
    
    unique_digits = len(set(token))
    unique_ratio = unique_digits / len(token) if token else 0.0
    
    leading_zero_count = len(token) - len(token.lstrip("0"))
    # if token is all zeros, leading zeroes is len(token) - 1 mathematically but let's just use raw lstrip logic
    if token.lstrip("0") == "":
        leading_zero_count = len(token) - 1
        
    leading_zero_ratio = leading_zero_count / len(token) if token else 0.0
    
    len_component = min(sig_len / 6.0, 1.0)
    unique_component = unique_ratio
    lz_component = 1.0 - leading_zero_ratio
    
    info = (0.5 * len_component) + (0.3 * unique_component) + (0.2 * lz_component)
    return max(0.0, min(1.0, info))


def model_intrinsic(reference_a: str, reference_b: str) -> float:
    norm_a = normalize_reference(reference_a)
    norm_b = normalize_reference(reference_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
        
    tokens_a = extract_numeric_tokens(reference_a)
    tokens_b = extract_numeric_tokens(reference_b)
    shared = set(tokens_a) & set(tokens_b)
    
    if not shared:
        return 0.0
        
    max_score = 0.0
    for token in shared:
        info = numeric_token_informativeness(token)
        max_score = max(max_score, 0.8 * info)
    return max_score


def main():
    print("Current behavior table:")
    print(f"{'Case':<7} {'Reference A':<17} {'Reference B':<17} {'Label':<18} {'Normalized A':<16} {'Normalized B':<16} {'Numeric A':<15} {'Numeric B':<15} {'Current'}")
    print("-" * 139)
    
    current_scores = []
    
    for case in CASES:
        norm_a = normalize_reference(case.reference_a) or ""
        norm_b = normalize_reference(case.reference_b) or ""
        
        num_a = "|".join(extract_numeric_tokens(case.reference_a))
        num_b = "|".join(extract_numeric_tokens(case.reference_b))
        
        score = reference_score(case.reference_a, case.reference_b)
        score_val = float(score) if score is not None else 0.0
        current_scores.append((case, score_val))
        
        print(f"{case.case_id:<7} {case.reference_a:<17} {case.reference_b:<17} {case.expected_relationship:<18} {norm_a:<16} {norm_b:<16} {num_a:<15} {num_b:<15} {score_val:.4f}")

    print("\nCurrent-score summary")
    print("-" * 21)
    strong_positives = [s for c, s in current_scores if c.expected_relationship == "strong_positive"]
    weak_collisions = [s for c, s in current_scores if c.expected_relationship == "weak_collision"]
    
    print(f"Strong positives: {len(strong_positives)}")
    print(f"Weak collisions: {len(weak_collisions)}")
    print(f"Distinct: {sum(1 for c, s in current_scores if c.expected_relationship == 'distinct')}")
    print(f"Ambiguous: {sum(1 for c, s in current_scores if c.expected_relationship == 'ambiguous')}")
    
    min_sp = min(strong_positives) if strong_positives else 0.0
    max_wc = max(weak_collisions) if weak_collisions else 0.0
    gap = min_sp - max_wc
    
    print(f"\nMinimum strong-positive score: {min_sp:.4f}")
    print(f"Maximum weak-collision score: {max_wc:.4f}")
    print(f"Strong-vs-collision gap: {gap:.4f}")

    print("\nShared-token diagnostics:")
    print(f"{'Case':<7} {'Token':<11} {'RawLen':<7} {'SigLen':<7} {'Unique':<7} {'UniqueRatio':<12} {'SingleDigit':<12} {'Sequential':<11} {'LeadingZeroRatio':<17} {'TokenCountA':<12} {'TokenCountB'}")
    print("-" * 128)
    
    for case in CASES:
        tokens_a = extract_numeric_tokens(case.reference_a)
        tokens_b = extract_numeric_tokens(case.reference_b)
        shared = set(tokens_a) & set(tokens_b)
        for token in shared:
            raw_len = len(token)
            sig = token.lstrip("0") or "0"
            sig_len = len(sig)
            unique_c = len(set(token))
            unique_r = unique_c / raw_len if raw_len > 0 else 0
            single_d = "yes" if unique_c == 1 else "no"
            
            # Sequential check
            is_seq = False
            if raw_len > 1:
                diffs = [int(token[i+1]) - int(token[i]) for i in range(raw_len-1)]
                if all(d == 1 for d in diffs) or all(d == -1 for d in diffs):
                    is_seq = True
            seq_str = "yes" if is_seq else "no"
            
            lz_count = raw_len - len(token.lstrip("0"))
            if token.lstrip("0") == "":
                lz_count = raw_len - 1
            lz_ratio = lz_count / raw_len if raw_len > 0 else 0.0
            
            tca = len(tokens_a)
            tcb = len(tokens_b)
            
            print(f"{case.case_id:<7} {token:<11} {raw_len:<7} {sig_len:<7} {unique_c:<7} {unique_r:<12.4f} {single_d:<12} {seq_str:<11} {lz_ratio:<17.4f} {tca:<12} {tcb}")

    print("\nModel comparison:")
    print(f"{'Case':<7} {'Label':<18} {'Current':<10} {'SigGate':<10} {'Graded':<10} {'Intrinsic'}")
    print("-" * 73)
    
    model_scores = {"Current": [], "SigGate": [], "Graded": [], "Intrinsic": []}
    
    for case in CASES:
        curr = float(reference_score(case.reference_a, case.reference_b) or 0.0)
        sigg = float(model_sig_gate(case.reference_a, case.reference_b) or 0.0)
        grad = float(model_graded(case.reference_a, case.reference_b) or 0.0)
        intr = float(model_intrinsic(case.reference_a, case.reference_b) or 0.0)
        
        model_scores["Current"].append((case, curr))
        model_scores["SigGate"].append((case, sigg))
        model_scores["Graded"].append((case, grad))
        model_scores["Intrinsic"].append((case, intr))
        
        print(f"{case.case_id:<7} {case.expected_relationship:<18} {curr:<10.4f} {sigg:<10.4f} {grad:<10.4f} {intr:.4f}")

    print("\nModel summary")
    print("-" * 13)
    print(f"{'Model':<11} {'MinPositive':<14} {'MaxCollision':<14} {'Gap'}")
    
    for mname in ["Current", "SigGate", "Graded", "Intrinsic"]:
        scores = model_scores[mname]
        sp = [s for c, s in scores if c.expected_relationship == "strong_positive"]
        wc = [s for c, s in scores if c.expected_relationship == "weak_collision"]
        min_sp = min(sp) if sp else 0.0
        max_wc = max(wc) if wc else 0.0
        gap = min_sp - max_wc
        print(f"{mname:<11} {min_sp:<14.4f} {max_wc:<14.4f} {gap:.4f}")

    for mname in ["Current", "SigGate", "Graded", "Intrinsic"]:
        print(f"\n{mname} ranking")
        print("-" * (len(mname) + 8))
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        for i, (c, s) in enumerate(ranked):
            print(f"{i+1}. {c.case_id}  {c.expected_relationship}  {s:.4f}")
            
    print("\nWeak collisions in top 10:")
    for mname in ["Current", "SigGate", "Graded", "Intrinsic"]:
        ranked = sorted(model_scores[mname], key=lambda x: x[1], reverse=True)
        top10 = ranked[:10]
        count = sum(1 for c, s in top10 if c.expected_relationship == "weak_collision")
        print(f"{mname}: {count}")

    print("\nProbe Results")
    print("-" * 13)
    for probe in PROBE_CASES:
        curr = float(reference_score(probe.reference_a, probe.reference_b) or 0.0)
        sigg = float(model_sig_gate(probe.reference_a, probe.reference_b) or 0.0)
        grad = float(model_graded(probe.reference_a, probe.reference_b) or 0.0)
        intr = float(model_intrinsic(probe.reference_a, probe.reference_b) or 0.0)
        print(f"{probe.case_id}: {probe.reference_a} <-> {probe.reference_b}")
        print(f"Current: {curr:.4f}, SigGate: {sigg:.4f}, Graded: {grad:.4f}, Intrinsic: {intr:.4f}\n")


if __name__ == "__main__":
    main()
