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


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from recongraph.domain.tax.parser import ParsedTaxIdentifierArtifact

def tax_identity_score(
    artifact_a: "ParsedTaxIdentifierArtifact | None",
    artifact_b: "ParsedTaxIdentifierArtifact | None",
) -> float | None:
    """Compare tax identities using rich parsed artifacts."""
    if artifact_a is None or artifact_b is None:
        return None
        
    val_a = artifact_a.gstin_candidate or artifact_a.pan_candidate or artifact_a.observation.raw_value
    val_b = artifact_b.gstin_candidate or artifact_b.pan_candidate or artifact_b.observation.raw_value

    normalized_a = normalize_tax_identity(val_a)
    normalized_b = normalize_tax_identity(val_b)

    if not normalized_a or not normalized_b:
        return None

    if normalized_a == normalized_b:
        return 1.0

    return 0.0


def temporal_score(
    date_a: date,
    date_b: date,
    max_days: int,
) -> float:
    """Calculate temporal compatibility within an expected date window."""
    if max_days <= 0:
        raise ValueError("max_days must be greater than zero")

    day_difference = abs((date_a - date_b).days)

    return max(
        0.0,
        1.0 - (day_difference / max_days),
    )





