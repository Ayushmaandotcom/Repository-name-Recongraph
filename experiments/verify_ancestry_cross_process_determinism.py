import subprocess
import sys
import os

SCRIPT = """
import sys
from recongraph.domain.lineage import SourceSystemId, SourceArtifactId, SourceLocator, StructuredSourceLineage
from recongraph.domain.derivations import (
    DerivedArtifactTypeId, CanonicalPayloadEnvelope, DerivedArtifactIdentity
)

sys_id = SourceSystemId("sap.production")
art_id = SourceArtifactId("invoice:123")
loc = SourceLocator("field:vendor_name")
lineage = StructuredSourceLineage(sys_id, art_id, loc)

tid = DerivedArtifactTypeId("tax.pan")
payload = CanonicalPayloadEnvelope({"pan": "ABCDE1234F", "nested": {"a": (1, 2, 3), "b": None, "c": True}})
aid = DerivedArtifactIdentity.compute(tid, "1.0.0", payload)

print(lineage.canonicalize_for_serialization().hex())
print(aid.digest)
"""

def run_experiment():
    print("Running process 1...")
    p1 = subprocess.run([sys.executable, "-c", SCRIPT], capture_output=True, text=True, check=True)
    out1 = p1.stdout.strip()
    
    # We can enforce hash randomization in Python, though it's on by default in 3.3+
    env = os.environ.copy()
    env["PYTHONHASHSEED"] = "random"
    
    print("Running process 2...")
    p2 = subprocess.run([sys.executable, "-c", SCRIPT], env=env, capture_output=True, text=True, check=True)
    out2 = p2.stdout.strip()

    print(f"Process 1 output:\n{out1}")
    print(f"Process 2 output:\n{out2}")
    
    if out1 == out2:
        print("\nSUCCESS: Outputs are byte-identical across processes.")
    else:
        print("\nFAILURE: Non-deterministic serialization detected.")
        sys.exit(1)

if __name__ == "__main__":
    run_experiment()
