import pytest
from datetime import datetime, timezone
import uuid
from recongraph.graph.trace import DecisionTrace, TraceEvent, TraceStage
from recongraph.graph.decision import ReconciliationDecision, DecisionAction
from recongraph.graph.hypotheses import EvaluatedHypothesis, EligibilityStatus

def test_collisions():
    base_id = DecisionTrace.compute_identity("1.0", "hash1", frozenset(["n1", "n2"]))
    
    # CASE 1: decision result changes
    print(f"CASE 1 BASE: {base_id}")
    print(f"CASE 1 MUTATED: {base_id}")
    
test_collisions()
