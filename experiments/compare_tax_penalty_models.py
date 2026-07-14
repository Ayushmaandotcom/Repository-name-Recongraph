import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from recongraph.domain.records import GSTRecord, PurchaseRecord
"""Compare two frozen Purchase-GST scoring policies.

The policies are defined locally so production policy changes do not alter
the historical A/B comparison that motivated the pure-compatibility migration.
"""

from recongraph.matching.scoring import (
    RelationshipPolicy,
    calculate_relationship_score,
    SignalName,
)
from recongraph.matching.pair_scorers import score_purchase_to_gst
from recongraph.matching.purchase_gst_semantics import SemanticFinding

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PURCHASES_PATH = PROJECT_ROOT / "datasets" / "raw" / "purchase_register.csv"
GST_RECORDS_PATH = PROJECT_ROOT / "datasets" / "raw" / "gst_records.csv"
GROUND_TRUTH_PATH = PROJECT_ROOT / "datasets" / "ground_truth" / "purchase_gst_matches.csv"

CHALLENGE_DIR = PROJECT_ROOT / "datasets" / "challenge"
CHALLENGE_PURCHASES_PATH = CHALLENGE_DIR / "purchase_register_v1.csv"
CHALLENGE_GST_RECORDS_PATH = CHALLENGE_DIR / "gst_records_v1.csv"
CHALLENGE_PAIR_LABELS_PATH = CHALLENGE_DIR / "pair_labels_v1.csv"

PURCHASE_GST_COMPARISON_WEIGHTS = {
    SignalName.ENTITY: 0.20,
    SignalName.REFERENCE: 0.20,
    SignalName.AMOUNT: 0.25,
    SignalName.TEMPORAL: 0.10,
    SignalName.TAX_IDENTITY: 0.25,
}

HYBRID_POLICY = RelationshipPolicy(
    weights=PURCHASE_GST_COMPARISON_WEIGHTS,
    contradiction_penalties={
        SignalName.TAX_IDENTITY: 0.5,
    },
)

PURE_COMPATIBILITY_POLICY = RelationshipPolicy(
    weights=PURCHASE_GST_COMPARISON_WEIGHTS,
    contradiction_penalties={},
)


@dataclass(frozen=True)
class ComparisonResult:
    dataset: str
    case_id: str
    pair_id: str
    label: str
    hybrid_score: float | None
    pure_score: float | None
    delta: float | None
    eligibility: str
    findings: tuple[str, ...]
    tax_score: float | None
    active_hybrid_penalty: bool
    is_eligibility_blocked: bool


def optional_text(value: str) -> str | None:
    stripped = value.strip()
    return stripped or None


def parse_purchase_record(row: dict[str, str]) -> PurchaseRecord:
    return PurchaseRecord(record_id="pur_cedf16a5", 
        vendor_name=optional_text(row.get("vendor_name", "")),
        reference=optional_text(row.get("invoice_number", "")),
        amount=float(row["amount"]),
        record_date=date.fromisoformat(row["invoice_date"]),
        tax_identity=optional_text(row.get("gstin", "")),
    )


def parse_gst_record(row: dict[str, str]) -> GSTRecord:
    return GSTRecord(record_id="gst_29b08642", 
        vendor_name=optional_text(row.get("supplier_name", "")),
        reference=optional_text(row.get("invoice_number", "")),
        amount=float(row["amount"]),
        record_date=date.fromisoformat(row["invoice_date"]),
        tax_identity=optional_text(row.get("gstin", "")),
    )


def load_records(path: Path, parse_fn) -> dict[str, any]:
    records = {}
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records[row["record_id"]] = parse_fn(row)
    return records


def calculate_delta(
    hybrid_score: float | None,
    pure_score: float | None,
) -> float | None:
    if hybrid_score is None or pure_score is None:
        return None
    return pure_score - hybrid_score


def evaluate_pair(
    dataset: str,
    case_id: str,
    purchase_id: str,
    gst_id: str,
    label: str,
    purchase: PurchaseRecord,
    gst_record: GSTRecord,
) -> ComparisonResult:
    pair_result = score_purchase_to_gst(
        purchase=purchase,
        gst_record=gst_record,
    )

    hybrid_relationship = calculate_relationship_score(
        signals=pair_result.signals,
        policy=HYBRID_POLICY,
    )

    pure_relationship = calculate_relationship_score(
        signals=pair_result.signals,
        policy=PURE_COMPATIBILITY_POLICY,
    )

    hybrid_score = hybrid_relationship.score
    pure_score = pure_relationship.score
    delta = calculate_delta(hybrid_score, pure_score)

    findings = tuple(f.value for f in pair_result.semantic_findings)
    eligibility = pair_result.eligibility.status.value

    tax_score = pair_result.signals.get(SignalName.TAX_IDENTITY)
    active_hybrid_penalty = SignalName.TAX_IDENTITY in hybrid_relationship.active_contradictions
    is_eligibility_blocked = SemanticFinding.TAX_IDENTITY_CONFLICT in pair_result.eligibility.blocking_findings

    return ComparisonResult(
        dataset=dataset,
        case_id=case_id,
        pair_id=f"{purchase_id}-{gst_id}",
        label=label,
        hybrid_score=hybrid_score,
        pure_score=pure_score,
        delta=delta,
        eligibility=eligibility,
        findings=findings,
        tax_score=tax_score,
        active_hybrid_penalty=active_hybrid_penalty,
        is_eligibility_blocked=is_eligibility_blocked,
    )


def run_baseline_experiment() -> list[ComparisonResult]:
    purchases = load_records(PURCHASES_PATH, parse_purchase_record)
    gst_records = load_records(GST_RECORDS_PATH, parse_gst_record)
    
    positive_pairs = set()
    with GROUND_TRUTH_PATH.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["relationship"] == "same_financial_event":
                positive_pairs.add((row["purchase_record_id"], row["gst_record_id"]))

    results = []
    for p_id, purchase in purchases.items():
        for g_id, gst_record in gst_records.items():
            label = "positive" if (p_id, g_id) in positive_pairs else "negative"
            results.append(
                evaluate_pair(
                    dataset="baseline",
                    case_id="-",
                    purchase_id=p_id,
                    gst_id=g_id,
                    label=label,
                    purchase=purchase,
                    gst_record=gst_record,
                )
            )
            
    results.sort(key=lambda r: r.hybrid_score if r.hybrid_score is not None else -1.0, reverse=True)
    return results


def run_challenge_experiment() -> list[ComparisonResult]:
    purchases = load_records(CHALLENGE_PURCHASES_PATH, parse_purchase_record)
    gst_records = load_records(CHALLENGE_GST_RECORDS_PATH, parse_gst_record)
    
    results = []
    with CHALLENGE_PAIR_LABELS_PATH.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            case_id = row["case_id"]
            p_id = row["purchase_record_id"]
            g_id = row["gst_record_id"]
            label = row["expected_label"]
            results.append(
                evaluate_pair(
                    dataset="challenge",
                    case_id=case_id,
                    purchase_id=p_id,
                    gst_id=g_id,
                    label=label,
                    purchase=purchases[p_id],
                    gst_record=gst_records[g_id],
                )
            )
            
    results.sort(key=lambda r: (r.case_id, r.pair_id))
    return results


def format_score(score: float | None, sign: bool = False) -> str:
    if score is None:
        return "None"
    return f"{score:+.4f}" if sign else f"{score:.4f}"


def format_findings(findings: tuple[str, ...]) -> str:
    if not findings:
        return "-"
    return ",".join(findings)


def print_table(results: list[ComparisonResult]) -> None:
    print(
        f"{'Dataset':<9} "
        f"{'Case':<7} "
        f"{'Pair':<14} "
        f"{'Label':<17} "
        f"{'Hybrid':>8} "
        f"{'Pure':>8} "
        f"{'Delta':>9}  "
        f"{'Eligibility':<13} "
        f"{'Findings'}"
    )
    print("-" * 112)
    for r in results:
        print(
            f"{r.dataset:<9} "
            f"{r.case_id:<7} "
            f"{r.pair_id:<14} "
            f"{r.label:<17} "
            f"{format_score(r.hybrid_score):>8} "
            f"{format_score(r.pure_score):>8} "
            f"{format_score(r.delta, sign=True):>9}  "
            f"{r.eligibility:<13} "
            f"{format_findings(r.findings)}"
        )


def main():
    baseline_results = run_baseline_experiment()
    challenge_results = run_challenge_experiment()
    all_results = baseline_results + challenge_results

    print_table(all_results)
    
    # Score-change summary
    changed_scores = sum(1 for r in all_results if r.delta is not None and r.delta != 0.0)
    unchanged_scores = sum(1 for r in all_results if r.delta is not None and r.delta == 0.0)
    max_positive_delta = max((r.delta for r in all_results if r.delta is not None), default=None)
    min_delta = min((r.delta for r in all_results if r.delta is not None), default=None)
    
    print("\nScore-change summary")
    print("-" * 20)
    print(f"Total pairs compared: {len(all_results)}")
    print(f"Changed scores: {changed_scores}")
    print(f"Unchanged scores: {unchanged_scores}")
    print(f"Maximum positive delta: {format_score(max_positive_delta)}")
    print(f"Minimum delta: {format_score(min_delta)}")

    # Baseline positive summary
    baseline_positives = [r for r in baseline_results if r.label == "positive"]
    pos_changed = sum(1 for r in baseline_positives if r.delta is not None and r.delta != 0.0)
    min_hybrid_pos = min((r.hybrid_score for r in baseline_positives if r.hybrid_score is not None), default=None)
    min_pure_pos = min((r.pure_score for r in baseline_positives if r.pure_score is not None), default=None)
    
    print("\nBaseline positive summary")
    print("-" * 25)
    print(f"Positive pairs: {len(baseline_positives)}")
    print(f"Positive scores changed: {pos_changed}")
    print(f"Minimum hybrid positive: {format_score(min_hybrid_pos)}")
    print(f"Minimum pure positive: {format_score(min_pure_pos)}")

    # Baseline negative summary
    baseline_negatives = [r for r in baseline_results if r.label == "negative"]
    neg_changed = sum(1 for r in baseline_negatives if r.delta is not None and r.delta != 0.0)
    max_hybrid_neg = max((r.hybrid_score for r in baseline_negatives if r.hybrid_score is not None), default=None)
    max_pure_neg = max((r.pure_score for r in baseline_negatives if r.pure_score is not None), default=None)
    
    print("\nBaseline negative summary")
    print("-" * 25)
    print(f"Negative pairs: {len(baseline_negatives)}")
    print(f"Negative scores changed: {neg_changed}")
    print(f"Maximum hybrid negative: {format_score(max_hybrid_neg)}")
    print(f"Maximum pure negative: {format_score(max_pure_neg)}")

    # Hybrid separation gap
    print("\nHybrid separation gap:")
    if min_hybrid_pos is not None and max_hybrid_neg is not None:
        print(f"{format_score(min_hybrid_pos - max_hybrid_neg)}")
        
    print("\nPure separation gap:")
    if min_pure_pos is not None and max_pure_neg is not None:
        print(f"{format_score(min_pure_pos - max_pure_neg)}")

    # Challenge eligibility summary
    print("\nChallenge eligibility summary")
    print("-" * 29)
    # Eligibility changes are effectively 0 because we don't recalculate it, we take it from production.
    # The prompt explicitly asks to print 0 if we didn't recompute.
    print("Eligibility changes: 0")
    
    # Tax-conflict consequence audit
    print("\nTax-conflict consequence audit")
    print("-" * 30)
    print(f"{'Pair':<14} {'Tax contribution':<18} {'Hybrid penalty':<16} {'Eligibility blocker'}")
    tax_conflict_results = [r for r in all_results if "tax_identity_conflict" in r.findings]
    for r in tax_conflict_results:
        tax_contrib = "zero" if r.tax_score == 0.0 else "nonzero"
        hybrid_pen = "yes" if r.active_hybrid_penalty else "no"
        elig_block = "yes" if r.is_eligibility_blocked else "no"
        print(f"{r.pair_id:<14} {tax_contrib:<18} {hybrid_pen:<16} {elig_block}")

if __name__ == "__main__":
    main()
