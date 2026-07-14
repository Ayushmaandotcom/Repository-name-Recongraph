import re

LEGAL_SUFFIX_TOKENS = {
    "pvt",
    "private",
    "ltd",
    "limited",
}

VENDOR_TOKEN_ALIASES = {
    "ent": "enterprises",
    "steels": "steel",
    "components": "component",
    "solutions": "solution",
    "supplies": "supply",
}


def normalize_reference(reference: str) -> str:
    """Normalize a financial reference for deterministic comparison."""
    return "".join(
        character.lower()
        for character in reference
        if character.isalnum()
    )


def normalize_tax_identity(tax_identity: str) -> str:
    """Normalize a tax identity for deterministic comparison."""
    return tax_identity.strip().upper()


def extract_numeric_reference_tokens(
    reference: str,
    min_length: int = 3,
) -> set[str]:
    """Extract significant numeric tokens from a financial reference."""
    if min_length <= 0:
        raise ValueError("min_length must be greater than zero")

    numeric_tokens = re.findall(r"\d+", reference)

    return {
        token
        for token in numeric_tokens
        if len(token) >= min_length
    }
