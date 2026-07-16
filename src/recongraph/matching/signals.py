from datetime import date

from rapidfuzz import fuzz

from recongraph.normalization.text import (
    normalize_tax_identity,
)


def _is_year_like_token(token: str) -> bool:
    """Return whether a numeric token resembles a calendar year."""
    if len(token) != 4:
        return False

    year = int(token)

    return 1900 <= year <= 2100







