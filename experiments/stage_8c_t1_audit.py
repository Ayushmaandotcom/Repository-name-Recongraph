import inspect
from dataclasses import dataclass
from typing import Any
import textwrap

from recongraph.plugins.core_providers import TaxEvidenceProvider, VendorEvidenceProvider
from recongraph.matching.signals import tax_identity_score
from recongraph.normalization.text import normalize_tax_identity
from recongraph.domain.records import PurchaseRecord, GSTRecord
from datetime import date
from decimal import Decimal

def _test_teq():
    print("--- TEQ SCENARIOS ---")
    base = "27AAAAA0000A1Z5"
    cases = [
        ("TEQ-001", base, base),
        ("TEQ-002", base, f" {base} "),
        ("TEQ-003", base, base.lower()),
        ("TEQ-004", base, "27 AAAAA 0000 A 1 Z 5"),
        ("TEQ-005", base, "27-AAAAA-0000-A-1Z5"),
        ("TEQ-006", base, base.replace("0", "O")),
        ("TEQ-007", base, base.replace("1", "I")),
        ("TEQ-008", base, "27AAAAA0000A8Z5"),
        ("TEQ-009", base, base.replace("5", "S")),
        ("TEQ-010", base, base[:-1] + "6"),
        ("TEQ-011", base, "07AAAAA0000A1Z5"),
        ("TEQ-012", base, "27AAAAA0000A2Z5"),
        ("TEQ-013", base, "07BBBBB0000B1Z5"),
        ("TEQ-014", base, "27BBBBB0000B1Z5"),
        ("TEQ-015", base, "ABCDEFGHIJKLMNO"),
    ]
    for name, left, right in cases:
        l_norm = normalize_tax_identity(left)
        r_norm = normalize_tax_identity(right)
        score = tax_identity_score(left, right)
        print(f"CASE {name}:")
        print(f"  LEFT RAW: {left} -> {l_norm}")
        print(f"  RIGHT RAW: {right} -> {r_norm}")
        print(f"  TAX SCALAR: {score}")

def _test_vendor_tax_pipeline():
    from recongraph.domain.vendor.context import VendorIdentityContext, VendorCorpusProfile
    ctx = VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(corpus_size=1, token_document_frequencies={}, digest="1"),
        interpreter_policy_version="1.0.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    v_prov = VendorEvidenceProvider(ctx)
    t_prov = TaxEvidenceProvider()
    
    p = PurchaseRecord("p1", amount=Decimal(1), record_date=date(2023,1,1), reference="1", vendor_name="Vendor", tax_identity="27AAAAA0000A1Z5")
    g = GSTRecord("g1", amount=Decimal(1), record_date=date(2023,1,1), reference="1", vendor_name="Vendor", tax_identity="07AAAAA0000A1Z5")
    
    tc = t_prov.evaluate([p], [g])
    vc = v_prov.evaluate([p], [g])
    
    print("--- PIPELINE CROSS CHECK ---")
    print(f"TAX SIGNAL: {tc.score}")
    print(f"VENDOR SIGNAL: {vc.score}")
    print(f"VENDOR METADATA: {vc.metadata}")
    
if __name__ == "__main__":
    _test_teq()
    _test_vendor_tax_pipeline()
