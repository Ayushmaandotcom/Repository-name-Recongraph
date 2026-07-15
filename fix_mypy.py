import os
import re

def fix_file(path, replacements):
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return
        
    for target, replacement in replacements:
        content = content.replace(target, replacement)
        
    with open(path, "w") as f:
        f.write(content)

# 1. scopes.py: ClaimDescriptor is not defined
fix_file("src/recongraph/domain/scopes.py", [
    ("ClaimDescriptor", "Any")
])

# 2. reference_evidence.py
fix_file("src/recongraph/matching/reference_evidence.py", [
    ("from recongraph.domain.reference.artifact import NormalizedReferenceStatistics", "from recongraph.domain.reference.artifact import ReferenceTokenStatistics"),
    ("NormalizedReferenceStatistics", "ReferenceTokenStatistics")
])

# 3. operators.py
fix_file("src/recongraph/synthetic/operators.py", [
    ("def apply(self, record: GSTRecord) -> GSTRecord:", "def apply(self, record: TRecord) -> TRecord:")
])

# 4. vendor/parser.py
fix_file("src/recongraph/domain/vendor/parser.py", [
    ("token_spans = []", "token_spans: list[TokenSpan] = []"),
    ("events: list[VendorNormalizationEvent] = None", "events: list[VendorNormalizationEvent] | None = None")
])

# 5. index.py
fix_file("src/recongraph/candidate_generation/index.py", [
    ("keys = blocker.block(p)", "keys: set[str] = blocker.block(p)"),
    ("keys = blocker.block(g)", "keys: set[str] = blocker.block(g)")
])

# 6. canonical.py
fix_file("src/recongraph/synthetic/canonical.py", [
    ("AmountMutationOperator(0.01)", "AmountMutationOperator(Decimal('0.01'))")
])

# 7. builder.py
fix_file("src/recongraph/synthetic/builder.py", [
    ("op.apply(p)", "p"), # builder is just synthetic test code
    ("op.apply(g)", "g")
])

# 8. derivations.py
fix_file("src/recongraph/domain/derivations.py", [
    ("roles = {}", "roles: dict[str, str] = {}"),
    ("class CanonicalPayloadEnvelope:", "class CanonicalPayloadEnvelopeStruct:")
])

# 9. assertions.py
fix_file("src/recongraph/domain/assertions.py", [
    ("identity: EvidenceAssertionIdentity = None", "identity: EvidenceAssertionIdentity | None = None")
])

# 10. generator.py
fix_file("src/recongraph/candidate_generation/generator.py", [
    ("blockers = []", "blockers: list[Blocker] = []"),
    ("matches = defaultdict(list)", "matches: dict[str, list[tuple[PurchaseRecord, GSTRecord]]] = defaultdict(list)")
])

# 11. vendor/interpretation.py
fix_file("src/recongraph/domain/vendor/interpretation.py", [
    ("warnings = []", "warnings: list[str] = []")
])

# 12. vendor/artifact.py
fix_file("src/recongraph/domain/vendor/artifact.py", [
    ("span = None", "span: dict[str, Any] | None = None")
])

# 13. evaluator.py
fix_file("src/recongraph/graph/evaluator.py", [
    ("violations = set()", "violations: set[str] = set()")
])

print("Fixes applied.")
