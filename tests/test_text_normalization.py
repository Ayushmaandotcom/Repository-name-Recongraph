import pytest

from recongraph.normalization.text import (
    normalize_reference,
    normalize_tax_identity,
    normalize_vendor_name,
)


def test_normalize_reference_removes_formatting_differences() -> None:
    assert normalize_reference("AB/1042") == "ab1042"
    assert normalize_reference("AB-1042") == "ab1042"
    assert normalize_reference("AB 1042") == "ab1042"
    assert normalize_reference("ab1042") == "ab1042"


def test_normalize_vendor_name_removes_legal_suffixes() -> None:
    assert normalize_vendor_name("ABC STEELS PVT. LTD.") == "abc steel"
    assert (
        normalize_vendor_name("ABC Steels Private Limited")
        == "abc steel"
    )
    assert (
        normalize_vendor_name("Northstar Components Pvt Ltd")
        == "northstar component"
    )


def test_normalize_vendor_name_preserves_unmapped_meaningful_tokens() -> None:
    assert (
        normalize_vendor_name("SHREE BALAJI FOODS")
        == "shree balaji foods"
    )


def test_normalize_vendor_name_canonicalizes_known_aliases() -> None:
    assert (
        normalize_vendor_name("SHREE BALAJI ENT.")
        == "shree balaji enterprises"
    )


def test_normalize_vendor_name_canonicalizes_known_token_variants() -> None:
    assert (
        normalize_vendor_name("ABC STEELS PVT. LTD.")
        == "abc steel"
    )
    assert (
        normalize_vendor_name("Northstar Components Pvt Ltd")
        == "northstar component"
    )
    assert (
        normalize_vendor_name("Metro Office Solutions")
        == "metro office solution"
    )
    assert (
        normalize_vendor_name("Apex Industrial Supplies")
        == "apex industrial supply"
    )


def test_normalize_tax_identity_standardizes_case_and_whitespace() -> None:
    assert (
        normalize_tax_identity(" 07abcde1234f1z5 ")
        == "07ABCDE1234F1Z5"
    )


