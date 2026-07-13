import sys
import os

# Add src to path to import current normalization logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from recongraph.normalization.text import normalize_vendor_name

ADVERSARIAL_PAIRS = [
    ("ABC LLP", "ABC LTD", "Legal form mismatch"),
    ("A&B", "AB", "Ampersand removed"),
    ("Company 1", "Company I", "Numeric vs Roman"),
    ("Müller", "Muller", "Accent behavior"),
    ("MICR0SOFT", "MICROSOFT", "Zero for O substitution"),
    ("TATA PVT LTD", "TATA PRIVATE LIMITED", "Abbreviated vs expanded suffix"),
    ("ABC ENTERPRISES", "ABC", "Generic suffix removal"),
    ("XYZ TRADERS", "XYZ", "Generic suffix removal"),
    ("GLOBAL INDUSTRIES INDIA", "GLOBAL INDUSTRIES BHARAT", "Country/Region aliases"),
]

def run_audit():
    print(f"{'Input A':<25} | {'Input B':<25} | {'Norm A':<20} | {'Norm B':<20} | {'Match?':<6} | {'Risk/Loss'}")
    print("-" * 125)
    for a, b, risk in ADVERSARIAL_PAIRS:
        norm_a = normalize_vendor_name(a)
        norm_b = normalize_vendor_name(b)
        match = "YES" if norm_a == norm_b else "NO"
        print(f"{a:<25} | {b:<25} | {norm_a:<20} | {norm_b:<20} | {match:<6} | {risk}")

if __name__ == "__main__":
    run_audit()
