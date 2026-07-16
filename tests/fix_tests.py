import os
import re

TEST_FILES = [
    "tests/test_benchmark_runner.py",
    "tests/test_candidate_generation.py",
    "tests/test_engine.py",
    "tests/test_golden_path.py",
    "tests/test_hypothesis_evaluator.py",
    "tests/test_properties.py",
    "tests/test_provider_permutation.py",
    "tests/test_trace_identity.py",
    "tests/test_shadow_evaluation.py"
]

for file_path in TEST_FILES:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r") as f:
        content = f.read()

    # Generic replace for any ReferenceEvidenceProvider(...) followed by ]
    content = re.sub(
        r"(ReferenceEvidenceProvider\([^)]*\))\s*\]",
        r"\1, SemanticEvidenceProvider()]",
        content
    )
    
    # Generic replace for any ReferenceEvidenceProvider(...) followed by ,
    # Wait, if it already has SemanticEvidenceProvider(), don't duplicate.
    if "SemanticEvidenceProvider()" not in content:
        content = re.sub(
            r"(ReferenceEvidenceProvider\([^)]*\)),\s*",
            r"\1, SemanticEvidenceProvider(), ",
            content
        )

    with open(file_path, "w") as f:
        f.write(content)

print("Updated tests with regex.")
