import pytest
from recongraph.domain.vendor.observation import (
    VendorObservationState,
    LegalFormCategory,
    TransformationType
)
from recongraph.domain.vendor.parser import DeterministicVendorParser
from recongraph.domain.vendor.artifact import build_vendor_observation_artifact
from recongraph.domain.derivations import DerivedArtifact

def test_missing_and_empty_observations():
    obs_none = DeterministicVendorParser.parse(None)
    assert obs_none.observation_state == VendorObservationState.MISSING
    assert obs_none.raw_name == ""

    obs_empty = DeterministicVendorParser.parse("   ")
    assert obs_empty.observation_state == VendorObservationState.EMPTY
    
    obs_uninterpretable = DeterministicVendorParser.parse("!!") # all punctuation stripped leaves empty core
    assert obs_uninterpretable.observation_state == VendorObservationState.UNINTERPRETABLE
    assert obs_uninterpretable.canonical_core_text == ""


def test_normalization_ordering_and_preservation():
    # Lossless extraction of legal form MUST precede lossy punctuation strip
    # E.g. "ABC (P) LTD." -> legal form extracted -> "ABC"
    obs = DeterministicVendorParser.parse("ABC (P) LTD.")
    
    assert obs.raw_name == "ABC (P) LTD."
    assert obs.canonical_core_text == "ABC"
    assert obs.legal_form_category == LegalFormCategory.PRIVATE_LIMITED
    
    events = obs.normalization_events
    
    # Assert LEGAL_FORM_EXTRACTION exists and happens before PUNCTUATION_STRIP if both exist
    legal_form_idx = next(i for i, ev in enumerate(events) if ev.transformation_type == TransformationType.LEGAL_FORM_EXTRACTION)
    # Check that affected span was captured
    ext_event = events[legal_form_idx]
    assert ext_event.affected_span is not None
    assert ext_event.affected_span.label == "LEGAL_FORM"
    
    # "ABC" doesn't have punctuation left after stripping "(P) LTD.", so punctuation strip might not occur.
    # Let's test one with punctuation in the core:
    obs2 = DeterministicVendorParser.parse("A.B.C. (P) LTD.")
    events2 = obs2.normalization_events
    lf_idx = next(i for i, ev in enumerate(events2) if ev.transformation_type == TransformationType.LEGAL_FORM_EXTRACTION)
    punct_idx = next(i for i, ev in enumerate(events2) if ev.transformation_type == TransformationType.PUNCTUATION_STRIP)
    assert lf_idx < punct_idx


def test_misleading_substrings_do_not_falsely_extract():
    # "PRIVATE LIMITED TRADERS" -> PRIVATE LIMITED is NOT a suffix
    obs = DeterministicVendorParser.parse("PRIVATE LIMITED TRADERS")
    assert obs.legal_form_category is None
    assert obs.canonical_core_text == "PRIVATE LIMITED TRADERS"
    
    # "(P) LTD." at the end should extract, but at the start should not (unless it is the only thing, but we only match suffixes)
    obs2 = DeterministicVendorParser.parse("LTD EDITION")
    assert obs2.legal_form_category is None
    assert obs2.canonical_core_text == "LTD EDITION"


def test_gstin_and_pan_detection():
    # Valid GSTIN
    gstin = "07ABCDE1234F1Z5"
    obs_gstin = DeterministicVendorParser.parse(gstin)
    assert obs_gstin.gstin_candidate == gstin
    assert obs_gstin.gstin_structurally_valid is True
    assert obs_gstin.pan_candidate == "ABCDE1234F"
    assert obs_gstin.pan_structurally_valid is True
    assert obs_gstin.pan_derived_from_gstin is True

    # Invalid GSTIN but looks like one (e.g. wrong length or OCR error)
    invalid_gstin = "07ABCDE1234F1Z5A" # 16 chars
    obs_invalid = DeterministicVendorParser.parse(invalid_gstin)
    assert obs_invalid.gstin_candidate is None # Doesn't match length
    
    # A standalone PAN
    pan = "ABCDE1234F"
    obs_pan = DeterministicVendorParser.parse(pan)
    assert obs_pan.gstin_candidate is None
    assert obs_pan.pan_candidate == pan
    assert obs_pan.pan_structurally_valid is True
    assert obs_pan.pan_derived_from_gstin is False


def test_artifact_identity_properties():
    # Determinism: same input, same version -> same artifact identity
    obs1 = DeterministicVendorParser.parse("ABC PVT LTD")
    art1 = build_vendor_observation_artifact(obs1)
    
    obs2 = DeterministicVendorParser.parse("ABC PVT LTD")
    art2 = build_vendor_observation_artifact(obs2)
    
    assert art1.identity.digest == art2.identity.digest
    
    # Context independence: Different input -> different identity
    obs3 = DeterministicVendorParser.parse("ABC TRADERS")
    art3 = build_vendor_observation_artifact(obs3)
    assert art1.identity.digest != art3.identity.digest

    # Parser version sensitivity: 
    # If we artificially change the parser version, the identity MUST change.
    original_version = DeterministicVendorParser.VERSION
    try:
        DeterministicVendorParser.VERSION = "2.0.0"
        art4 = build_vendor_observation_artifact(obs1)
        assert art1.identity.digest != art4.identity.digest
    finally:
        DeterministicVendorParser.VERSION = original_version
