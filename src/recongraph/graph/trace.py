from dataclasses import dataclass
from enum import StrEnum
from typing import Any
from datetime import datetime, timezone

class TraceStage(StrEnum):
    CANDIDATE_GENERATION = "candidate_generation"
    GRAPH_BUILDING = "graph_building"
    COMPONENT_EXTRACTION = "component_extraction"
    HYPOTHESIS_SEARCH = "hypothesis_search"
    HYPOTHESIS_EVALUATION = "hypothesis_evaluation"
    DECISION_EVALUATION = "decision_evaluation"
    EXPLANATION_GENERATION = "explanation_generation"

@dataclass(frozen=True)
class TraceEvent:
    """An explicit, chronological record of a single action in the reconciliation pipeline."""
    timestamp: datetime
    stage: TraceStage
    payload: Any  # E.g., CandidateEdge, CandidateGraph, Hypothesis, EvaluatedHypothesis, ReconciliationDecision

@dataclass(frozen=True)
class DecisionTrace:
    """The immutable historical record of an entire reconciliation execution."""
    trace_id: str
    events: tuple[TraceEvent, ...]
    
    def get_events_for_stage(self, stage: TraceStage) -> tuple[TraceEvent, ...]:
        return tuple(e for e in self.events if e.stage == stage)

class TraceBuilder:
    """
    A passive recorder that assembles the historical trace chronologically.
    It strictly adheres to the Recorder Principle (never recalculates or alters).
    """
    def __init__(self, trace_id: str):
        self._trace_id = trace_id
        self._events: list[TraceEvent] = []
        
    def record_event(self, stage: TraceStage, payload: Any) -> None:
        """Records a new event in the chronological sequence."""
        event = TraceEvent(
            timestamp=datetime.now(timezone.utc),
            stage=stage,
            payload=payload
        )
        self._events.append(event)
        
    def build(self) -> DecisionTrace:
        """Freezes the chronological events into an immutable DecisionTrace."""
        return DecisionTrace(
            trace_id=self._trace_id,
            events=tuple(self._events)
        )
