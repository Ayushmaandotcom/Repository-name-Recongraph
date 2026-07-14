from recongraph.domain.derivations import (
    DerivedArtifactTypeId,
    DerivedArtifactIdentity,
    CanonicalPayloadEnvelope,
    DerivedArtifact
)
from recongraph.domain.vendor.observation import VendorNameObservation
from recongraph.domain.vendor.parser import DeterministicVendorParser


def observation_to_canonical_payload(observation: VendorNameObservation) -> CanonicalPayloadEnvelope:
    """
    Serializes a VendorNameObservation into a CanonicalPayloadEnvelope,
    ensuring it contains only deterministic, context-independent facts.
    """
    events_payload = []
    for ev in observation.normalization_events:
        span = None
        if ev.affected_span:
            span = {
                "start_index": ev.affected_span.start_index,
                "end_index": ev.affected_span.end_index,
                "label": ev.affected_span.label
            }
        events_payload.append({
            "transformation_type": ev.transformation_type.name,
            "affected_span": span,
            "before_value": ev.before_value,
            "after_value": ev.after_value,
            "rule_name": ev.rule_name
        })
        
    spans_payload = []
    for span in observation.token_spans:
        spans_payload.append({
            "start_index": span.start_index,
            "end_index": span.end_index,
            "label": span.label
        })

    payload_data = {
        "raw_name": observation.raw_name,
        "observation_state": observation.observation_state.name,
        "canonical_core_text": observation.canonical_core_text,
        "organization_tokens": tuple(observation.organization_tokens),
        "legal_form_category": observation.legal_form_category.name if observation.legal_form_category else None,
        "recognized_designators": tuple(observation.recognized_designators),
        "token_spans": tuple(spans_payload),
        "normalization_events": tuple(events_payload),
        "gstin_candidate": observation.gstin_candidate,
        "gstin_structurally_valid": observation.gstin_structurally_valid,
        "pan_candidate": observation.pan_candidate,
        "pan_structurally_valid": observation.pan_structurally_valid,
        "pan_derived_from_gstin": observation.pan_derived_from_gstin
    }
    
    return CanonicalPayloadEnvelope(payload_data)


def build_vendor_observation_artifact(observation: VendorNameObservation) -> DerivedArtifact:
    """
    Constructs a deterministic DerivedArtifact containing the VendorNameObservation.
    The artifact identity changes if the parser version changes or the raw input changes.
    """
    type_id = DerivedArtifactTypeId("recongraph.vendor.observation")
    payload = observation_to_canonical_payload(observation)
    
    identity = DerivedArtifactIdentity.compute(
        type_id=type_id,
        semantic_version=DeterministicVendorParser.VERSION,
        payload=payload
    )
    
    return DerivedArtifact(
        identity=identity,
        payload=payload
    )
