import math
from datetime import date
from recongraph.domain.records import PurchaseRecord, GSTRecord
from recongraph.matching.scoring import SignalName
from experiments.legacy_reference import reference_score as legacy_reference_score
from recongraph.matching.pair_scorers import score_purchase_to_gst, PairScoringResult
from recongraph.matching.reference_evidence import (
    ReferenceCorpusProfile,
    ReferenceEvidencePolicy,
    ReferenceEvidenceContext,
)
from recongraph.matching.purchase_gst_semantics import SemanticFinding

def run_audit():
    # Setup dummy profile for exact math
    # 001 appears 81 times out of 100 -> score 1 - sqrt(0.81) = 0.10
    # 1042 appears 2 times out of 1000 -> score 1 - sqrt(0.002) = 0.955
    # 874219 appears 10 times out of 1000 -> score 1 - sqrt(0.01) = 0.90
    prof = ReferenceCorpusProfile(
        reference_count=1000,
        normalized_reference_frequency={"dummy": 907, "inv1042": 2, "inv874219": 10, "001": 81},
        numeric_token_document_frequency={"1042": 2, "874219": 10, "001": 81}
    )
    context = ReferenceEvidenceContext(profile=prof, policy=ReferenceEvidencePolicy())

    challenges = {
        "HN001": (
            PurchaseRecord(record_id="pur_bec420c3", vendor_name="ABC", reference="INV-1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_1ab36d4e", vendor_name="ABC", reference="AB/1042", amount=2000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
        ),
        "HN002": (
            PurchaseRecord(record_id="pur_d9008b6e", vendor_name="XYZ", reference="INV-1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_cab03bdf", vendor_name="XYZ", reference="AB/1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX2"),
        ),
        "HN003": (
            PurchaseRecord(record_id="pur_ffb6116d", vendor_name="DEF", reference="INV-MAY", amount=1000.0, record_date=date(2023,5,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_c24cb47e", vendor_name="DEF", reference="INV-JUN", amount=1000.0, record_date=date(2023,6,1), tax_identity="TAX1"),
        ),
        "HN004": (
            PurchaseRecord(record_id="pur_4625e9e7", vendor_name="GHI", reference="OMD-001", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_f9dc1142", vendor_name="GHI", reference="NSS-001", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
        ),
        "HN005": (
            PurchaseRecord(record_id="pur_bea4c94e", vendor_name="JKL", reference="INV-1042", amount=2000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
            GSTRecord(record_id="gst_006cb9ba", vendor_name="JKL", reference="AB/1042", amount=1000.0, record_date=date(2023,1,1), tax_identity="TAX1"),
        )
    }
    
    empty_pathologicals = {
        "None vs None": (None, None),
        "Empty vs Empty": ("", ""),
        "None vs INV123": (None, "INV123"),
        "INV123 vs None": ("INV123", None),
        "Empty vs INV123": ("", "INV123"),
        "--- vs ///": ("---", "///"),
        "creditnote vs None": ("creditnote", None),
    }

    print("=== PART 1: LEGACY VS NEW REFERENCE ENGINE ===")
    print("Pair | Legacy | New | Coverage | Reason")
    for name, (p, g) in challenges.items():
        leg_ref = legacy_reference_score(p.reference, g.reference)
        res = score_purchase_to_gst(p, g, context)
        new_ref = res.signals[SignalName.REFERENCE]
        cov = res.reference_interpretation.statistical_coverage
        leg_str = f"{leg_ref:.2f}" if leg_ref is not None else "None"
        new_str = f"{new_ref:.2f}" if new_ref is not None else "None"
        print(f"{name} | {leg_str} | {new_str} | {cov:.1f} | ?")

    print("\n=== PART 2: RELATIONSHIP SCORE MOVEMENT ===")
    print("Pair | Old Base Score | New Base Score | Reason")
    for name, (p, g) in challenges.items():
        # To get old base score, we fake the reference signal with legacy score
        leg_ref = legacy_reference_score(p.reference, g.reference)
        res_new = score_purchase_to_gst(p, g, context)
        
        # We can mock calculate_relationship_score but let's just observe the actual new score vs what it used to be.
        # Actually, let's inject the legacy score to see what the old base score was.
        # Or calculate it: 0.2*Entity + 0.2*Ref + 0.25*Amt + 0.1*Temp + 0.25*Tax = Total / Available
        # It's easier just to re-run the score calculation or approximate.
        # Let's print new score for now and I will manually fill the table.
        print(f"{name} | old | {res_new.relationship.base_score:.4f} | ?")
        
    print("\n=== PART 3: SEMANTIC FINDINGS AUDIT ===")
    for name, (p, g) in challenges.items():
        res = score_purchase_to_gst(p, g, context)
        print(f"{name}: {res.semantic_findings}")
        
    print("\n=== PART 4: COVERAGE AUDIT ===")
    for name, (p, g) in challenges.items():
        res = score_purchase_to_gst(p, g, context)
        print(f"{name}: {res.reference_interpretation.statistical_coverage}")
        
    print("\n=== PART 5: EMPTY REFERENCE AUDIT ===")
    for name, (ref_a, ref_b) in empty_pathologicals.items():
        p = PurchaseRecord(record_id="pur_b4374f15", vendor_name="A", reference=ref_a, amount=100.0, record_date=date(2023,1,1), tax_identity="TAX")
        g = GSTRecord(record_id="gst_9a421bc1", vendor_name="A", reference=ref_b, amount=100.0, record_date=date(2023,1,1), tax_identity="TAX")
        try:
            res = score_purchase_to_gst(p, g, context)
            ref_sig = res.signals[SignalName.REFERENCE]
            score = res.relationship.score
            cov = res.reference_interpretation.statistical_coverage
            sem = res.semantic_findings
            print(f"{name} -> RefSig: {ref_sig}, PairScore: {score:.2f}, Cov: {cov:.1f}, Sem: {sem}")
        except Exception as e:
            print(f"{name} -> CRASH: {e}")

    print("\n=== PART 7: EXPLAINABILITY AUDIT (HN004) ===")
    p, g = challenges["HN004"]
    res = score_purchase_to_gst(p, g, context)
    print("Interpretation:", res.reference_interpretation)

if __name__ == "__main__":
    run_audit()
