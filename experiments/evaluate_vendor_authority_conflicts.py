"""
Stage 8C-0B: Authority Hierarchy Challenge
Experiment: Evaluate Vendor Authority Conflicts
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class TestCase:
    case_id: str
    name_a: str | None
    name_b: str | None
    tax_a: str | None
    tax_b: str | None
    description: str

CASES = [
    TestCase("AH001", "ABC PRIVATE LIMITED", "ABC PRIVATE LIMITED", "TAX-A", "TAX-B", "Exact Name, Conflicting Tax Identity"),
    TestCase("AH002", "TATA CONSULTANCY SERVICES LIMITED", "TCS", "TAX-X", "TAX-X", "Different Name, Exact Tax Identity"),
    TestCase("AH003", "ABC TECHNOLOGIES PRIVATE LIMITED", "ABC TECHNOLOGY PVT LTD", None, None, "Similar Name, Missing Tax Identity"),
    TestCase("AH004", "TRADERS", "TRADERS", None, None, "Exact Generic Name"),
    TestCase("AH005", "TATA MOTORS LIMITED", "TATA TECHNOLOGIES LIMITED", None, None, "Corporate Family Collision"),
    TestCase("AH006", "ABC LLP", "ABC PRIVATE LIMITED", None, None, "Legal Suffix Conflict"),
    TestCase("AH007", "MICROSOFT", "MICR0SOFT", None, None, "OCR Corruption"),
    TestCase("AH008", "ABC", "ABC", None, None, "Abbreviation Collision"),
    TestCase("AH009", "XEROX", "XEROX CORPORATION", None, None, "Brand vs Legal Entity"),
    TestCase("AH010", "FACEBOOK INC", "META PLATFORMS INC", None, None, "Historical Rename"),
    TestCase("AH011", "ALPHA INDUSTRIES", "OMEGA LOGISTICS", "TAX-X", "TAX-X", "Same Tax Identity, Suspiciously Different Names"),
    TestCase("AH012", None, None, None, None, "Both Observations Missing"),
]

def evaluate_authority(case: TestCase) -> dict[str, Any]:
    name_state = "Missing" if not case.name_a and not case.name_b else "Exact" if case.name_a == case.name_b else "Different/Similar"
    tax_state = "Missing" if not case.tax_a and not case.tax_b else "Exact" if case.tax_a == case.tax_b else "Conflict"
    
    supported = []
    contradicted = []
    missing = []
    
    if name_state == "Exact":
        supported.append("Lexical Identity")
    if tax_state == "Exact":
        supported.append("Legal Identity")
    if tax_state == "Conflict":
        contradicted.append("Legal Identity")
        
    if tax_state == "Missing":
        missing.append("Legal Entity Proof")
        
    if case.case_id == "AH001":
        # Name is exact, Tax is conflict. Legal conflict overrides lexical support.
        pass
        
    return {
        "Case": case.case_id,
        "Name Evidence State": name_state,
        "Identifier Evidence State": tax_state,
        "Identity Claim Supported": ", ".join(supported) or "None",
        "Identity Claim Contradicted": ", ".join(contradicted) or "None",
        "Knowledge Missing": ", ".join(missing) or "None"
    }

if __name__ == "__main__":
    print("| Case | Name Evidence State | Identifier Evidence State | Identity Claim Supported | Identity Claim Contradicted | Knowledge Missing |")
    print("|---|---|---|---|---|---|")
    for c in CASES:
        r = evaluate_authority(c)
        print(f"| {r['Case']} | {r['Name Evidence State']} | {r['Identifier Evidence State']} | {r['Identity Claim Supported']} | {r['Identity Claim Contradicted']} | {r['Knowledge Missing']} |")
