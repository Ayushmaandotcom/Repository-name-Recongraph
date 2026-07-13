from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum

from recongraph.matching.scoring import SignalName


# Represents a statistical rarity boundary (score >= 0.8 implies token frequency <= 4% of corpus)
STRONG_REFERENCE_SCORE = 0.8
STRONG_ENTITY_SCORE = 0.9
STRONG_AMOUNT_SCORE = 0.9


class SemanticFinding(StrEnum):
    SEVERE_AMOUNT_CONFLICT = "severe_amount_conflict"
    TAX_IDENTITY_CONFLICT = "tax_identity_conflict"
    DISTINCT_EVENT_IDENTITY_EVIDENCE = (
        "distinct_event_identity_evidence"
    )


def analyze_purchase_gst_semantics(
    evidence: Mapping[SignalName, float | None],
) -> tuple[SemanticFinding, ...]:
    findings: list[SemanticFinding] = []

    entity = evidence[SignalName.ENTITY]
    reference = evidence[SignalName.REFERENCE]
    amount = evidence[SignalName.AMOUNT]
    temporal = evidence[SignalName.TEMPORAL]
    tax_identity = evidence[SignalName.TAX_IDENTITY]

    if (
        amount == 0.0
        and reference is not None
        and reference >= STRONG_REFERENCE_SCORE
        and tax_identity == 1.0
    ):
        findings.append(
            SemanticFinding.SEVERE_AMOUNT_CONFLICT
        )

    if tax_identity == 0.0:
        findings.append(
            SemanticFinding.TAX_IDENTITY_CONFLICT
        )

    if (
        entity is not None
        and entity >= STRONG_ENTITY_SCORE
        and reference == 0.0
        and amount is not None
        and amount >= STRONG_AMOUNT_SCORE
        and temporal == 0.0
        and tax_identity == 1.0
    ):
        findings.append(
            SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE
        )

    return tuple(findings)


class OneToOneEligibility(StrEnum):
    ELIGIBLE = "eligible"
    INELIGIBLE = "ineligible"


@dataclass(frozen=True)
class EligibilityResult:
    status: OneToOneEligibility
    blocking_findings: tuple[SemanticFinding, ...]

    def __post_init__(self) -> None:
        if (
            self.status is OneToOneEligibility.ELIGIBLE
            and self.blocking_findings
        ):
            raise ValueError(
                "eligible result cannot contain blocking findings"
            )

        if (
            self.status is OneToOneEligibility.INELIGIBLE
            and not self.blocking_findings
        ):
            raise ValueError(
                "ineligible result must contain at least one blocking finding"
            )


ONE_TO_ONE_BLOCKING_FINDINGS = frozenset(
    {
        SemanticFinding.SEVERE_AMOUNT_CONFLICT,
        SemanticFinding.TAX_IDENTITY_CONFLICT,
        SemanticFinding.DISTINCT_EVENT_IDENTITY_EVIDENCE,
    }
)


def evaluate_purchase_gst_one_to_one_eligibility(
    findings: tuple[SemanticFinding, ...],
) -> EligibilityResult:
    blocking_findings_list: list[SemanticFinding] = []

    for finding in findings:
        if (
            finding in ONE_TO_ONE_BLOCKING_FINDINGS
            and finding not in blocking_findings_list
        ):
            blocking_findings_list.append(finding)

    blocking_findings = tuple(blocking_findings_list)

    status = (
        OneToOneEligibility.INELIGIBLE
        if blocking_findings
        else OneToOneEligibility.ELIGIBLE
    )

    return EligibilityResult(
        status=status,
        blocking_findings=blocking_findings,
    )
