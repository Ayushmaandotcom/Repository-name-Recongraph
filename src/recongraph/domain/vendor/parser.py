import re
import unicodedata
from typing import Any, Tuple, Optional, List

from recongraph.domain.vendor.observation import (
    VendorNameObservation,
    VendorObservationState,
    LegalFormCategory,
    VendorNormalizationEvent,
    TransformationType,
    TokenSpan
)

GSTIN_PATTERN = re.compile(r"^([0-9]{2})([A-Z]{5}[0-9]{4}[A-Z]{1})([1-9A-Z]{1})(Z)([0-9A-Z]{1})$")
PAN_PATTERN = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")

from recongraph.domain.tax.parser import DeterministicTaxParser

# We map known suffixes to their canonical legal form category.
# These must match at the END of the string.
LEGAL_FORM_SUFFIXES = {
    "PRIVATE LIMITED": LegalFormCategory.PRIVATE_LIMITED,
    "PVT LTD": LegalFormCategory.PRIVATE_LIMITED,
    "PVT. LTD.": LegalFormCategory.PRIVATE_LIMITED,
    "PVT.LTD.": LegalFormCategory.PRIVATE_LIMITED,
    "(P) LTD": LegalFormCategory.PRIVATE_LIMITED,
    "(P) LTD.": LegalFormCategory.PRIVATE_LIMITED,
    "PTY LTD": LegalFormCategory.PRIVATE_LIMITED,
    
    "PUBLIC LIMITED": LegalFormCategory.PUBLIC_LIMITED,
    "LIMITED": LegalFormCategory.PUBLIC_LIMITED,
    "LTD": LegalFormCategory.PUBLIC_LIMITED,
    "LTD.": LegalFormCategory.PUBLIC_LIMITED,
    
    "LIMITED LIABILITY PARTNERSHIP": LegalFormCategory.LIMITED_LIABILITY_PARTNERSHIP,
    "LLP": LegalFormCategory.LIMITED_LIABILITY_PARTNERSHIP,
    "L.L.P.": LegalFormCategory.LIMITED_LIABILITY_PARTNERSHIP,
    
    "ONE PERSON COMPANY": LegalFormCategory.ONE_PERSON_COMPANY,
    "OPC": LegalFormCategory.ONE_PERSON_COMPANY,
    
    "HUF": LegalFormCategory.HUF,
    "H.U.F.": LegalFormCategory.HUF,
}

# Sort by length descending to match longest suffixes first
SORTED_LEGAL_FORMS = sorted(LEGAL_FORM_SUFFIXES.items(), key=lambda x: len(x[0]), reverse=True)


class DeterministicVendorParser:
    """
    Context-independent parser for raw vendor strings.
    Extracts facts and normalizes the string, strictly recording all transformations.
    """
    
    VERSION = "1.0.0"
    
    @classmethod
    def parse(cls, raw: Optional[str]) -> VendorNameObservation:
        if raw is None:
            return cls._empty_observation(raw, VendorObservationState.MISSING)
            
        events: List[VendorNormalizationEvent] = []
        
        # 1. Unicode Normalization
        unicode_norm = unicodedata.normalize("NFKC", raw)
        if unicode_norm != raw:
            events.append(VendorNormalizationEvent(
                transformation_type=TransformationType.UNICODE_NORMALIZATION,
                affected_span=None,
                before_value=raw,
                after_value=unicode_norm,
                rule_name="NFKC"
            ))
            
        current = unicode_norm
        
        # Check empty or whitespace-only
        if not current.strip():
            return cls._empty_observation(raw, VendorObservationState.EMPTY, events)
            
        # Use the shared tax parser to check if this string happens to be a tax identity
        tax_artifact = DeterministicTaxParser.parse(current, field_id="vendor_name")
            
        # 2. Case Normalization
        cased = current.upper()
        if cased != current:
            events.append(VendorNormalizationEvent(
                transformation_type=TransformationType.CASE_NORMALIZATION,
                affected_span=None,
                before_value=current,
                after_value=cased,
                rule_name="UPPERCASE"
            ))
        current = cased
        
        # 3. Punctuation Strip and Whitespace collapse (for org core)
        # We want to keep original token spans if possible, but the string is mutating.
        # For V1-1A, we track the legal form stripping first since it's suffix based.
        
        legal_form = None
        designators = []
        
        # To accurately match suffixes, we look at the stripped version but retain the original 
        # string if it doesn't match to avoid losing trailing spaces incorrectly if no match occurs.
        # Actually, legal forms often appear after spaces or punctuation.
        
        # We will do a regex search at the end of the string for the legal forms.
        for suffix, category in SORTED_LEGAL_FORMS:
            # Match the suffix at the end of the string, allowing optional trailing punctuation/spaces
            escaped = re.escape(suffix)
            # Regex: start of string or preceded by non-word char, the suffix, optional trailing non-word chars, end of string.
            pattern = re.compile(rf"(?:^|(?<=\W)){escaped}[^\w]*$", re.IGNORECASE)
            match = pattern.search(current)
            if match:
                legal_form = category
                designators.append(suffix)
                
                before_val = current
                # Remove the matched portion
                current = current[:match.start()].strip()
                events.append(VendorNormalizationEvent(
                    transformation_type=TransformationType.LEGAL_FORM_EXTRACTION,
                    affected_span=TokenSpan(match.start(), match.end(), "LEGAL_FORM"),
                    before_value=before_val,
                    after_value=current,
                    rule_name=f"EXTRACT_{category.name}"
                ))
                break
                
        # 3b. Geographic Extraction
        GEOGRAPHIC_TOKENS = {"INDIA", "UK", "USA", "APAC", "EMEA", "GLOBAL", "AMERICAS", "EUROPE", "ASIA"}
        for geo in GEOGRAPHIC_TOKENS:
            escaped = re.escape(geo)
            pattern = re.compile(rf"(?:^|(?<=\W)){escaped}[^\w]*$", re.IGNORECASE)
            match = pattern.search(current)
            if match:
                before_val = current
                current = current[:match.start()].strip()
                events.append(VendorNormalizationEvent(
                    transformation_type=TransformationType.GEOGRAPHIC_EXTRACTION,
                    affected_span=TokenSpan(match.start(), match.end(), "GEOGRAPHIC"),
                    before_value=before_val,
                    after_value=current,
                    rule_name=f"EXTRACT_GEO_{geo}"
                ))
                break # Extract only one suffix geo for now
                
        # 3c. Division Extraction
        DIVISION_TOKENS = {"TECHNOLOGIES", "SERVICES", "SOLUTIONS", "ENTERPRISES", "SYSTEMS", "CORP", "CORPORATION", "INC", "LLC"}
        for div in DIVISION_TOKENS:
            escaped = re.escape(div)
            pattern = re.compile(rf"(?:^|(?<=\W)){escaped}[^\w]*$", re.IGNORECASE)
            match = pattern.search(current)
            if match:
                before_val = current
                current = current[:match.start()].strip()
                events.append(VendorNormalizationEvent(
                    transformation_type=TransformationType.DIVISION_EXTRACTION,
                    affected_span=TokenSpan(match.start(), match.end(), "DIVISION"),
                    before_value=before_val,
                    after_value=current,
                    rule_name=f"EXTRACT_DIV_{div}"
                ))
                break # Extract only one division suffix for now
                
        # 4. Punctuation stripping
        # Replace non-alphanumeric with space
        no_punct = re.sub(r"[^\w\s]", " ", current)
        if no_punct != current:
            events.append(VendorNormalizationEvent(
                transformation_type=TransformationType.PUNCTUATION_STRIP,
                affected_span=None,
                before_value=current,
                after_value=no_punct,
                rule_name="STRIP_NON_ALPHANUMERIC"
            ))
        current = no_punct
        
        # 5. Whitespace collapse
        collapsed = re.sub(r"\s+", " ", current).strip()
        if collapsed != current:
            events.append(VendorNormalizationEvent(
                transformation_type=TransformationType.WHITESPACE_COLLAPSE,
                affected_span=None,
                before_value=current,
                after_value=collapsed,
                rule_name="COLLAPSE_SPACES"
            ))
        current = collapsed
        
        org_tokens = tuple(current.split(" ")) if current else ()
        
        # Calculate approximate token spans on the final org tokens vs raw string
        # This is a complex string-alignment problem in full NLP, but for V1 we just store empty spans
        # or simple substring find results. To meet the requirements simply, we'll omit complex alignment
        # and just note the token values for now.
        token_spans: list[Any] = []
        
        # If after everything the core is empty (e.g. string was just "PVT LTD")
        state = VendorObservationState.PRESENT
        if not current:
            state = VendorObservationState.UNINTERPRETABLE
            
        return VendorNameObservation(
            raw_name=raw,
            observation_state=state,
            canonical_core_text=current,
            organization_tokens=org_tokens,
            legal_form_category=legal_form,
            recognized_designators=tuple(designators),
            token_spans=tuple(token_spans),
            normalization_events=tuple(events),
            tax_artifact=tax_artifact
        )

    @classmethod
    def _empty_observation(cls, raw: Optional[str], state: VendorObservationState, events: Optional[List[VendorNormalizationEvent]] = None) -> VendorNameObservation:
        return VendorNameObservation(
            raw_name=raw if raw is not None else "",
            observation_state=state,
            canonical_core_text="",
            organization_tokens=(),
            legal_form_category=None,
            recognized_designators=(),
            token_spans=(),
            normalization_events=tuple(events) if events else (),
            tax_artifact=None
        )
