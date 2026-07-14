import difflib
from dataclasses import dataclass
from typing import Tuple

from recongraph.domain.vendor.observation import VendorNameObservation, VendorObservationState
from recongraph.domain.vendor.context import VendorIdentityContext
from recongraph.domain.vendor.factors import (
    GSTRegistrationRelation, GSTRegistrationRelationState,
    PANRelation, PANRelationState, PANEvidenceDependence,
    LexicalRelation, LexicalRelationState,
    LegalFormRelation, LegalFormRelationState,
    CorpusDistinctiveness, CorpusDistinctivenessState
)
from recongraph.domain.derivations import DerivedArtifactIdentity

@dataclass(frozen=True)
class VendorIdentityInterpretation:
    left_artifact_identity: DerivedArtifactIdentity
    right_artifact_identity: DerivedArtifactIdentity
    context_identity: str
    
    gst_registration_relation: GSTRegistrationRelation
    pan_relation: PANRelation
    lexical_relation: LexicalRelation
    legal_form_relation: LegalFormRelation
    corpus_distinctiveness: CorpusDistinctiveness
    
    warnings: Tuple[str, ...]


class VendorPairInterpreter:
    """
    Produces factorized, context-dependent comparative evidence.
    Does not score pairwise vendor identity. Does not claim legal entity identity.
    """
    
    VERSION = "1.0.0"

    @classmethod
    def interpret(
        cls,
        left: VendorNameObservation,
        left_identity: DerivedArtifactIdentity,
        right: VendorNameObservation,
        right_identity: DerivedArtifactIdentity,
        context: VendorIdentityContext
    ) -> VendorIdentityInterpretation:
        
        # 1. GSTIN Relation
        gst_rel = cls._compare_gstin(left, right)
        
        # 2. PAN Relation
        pan_rel = cls._compare_pan(left, right)
        
        # 3. Lexical Core Relation
        lexical_rel, shared_tokens = cls._compare_lexical(left, right, context)
        
        # 4. Legal Form Relation
        legal_rel = cls._compare_legal_form(left, right)
        
        # 5. Corpus Distinctiveness
        corpus_rel = cls._evaluate_distinctiveness(shared_tokens, context)
        
        warnings = []
        # If fuzzy was skipped due to length, we might emit a warning, but for now we keep it simple.

        return VendorIdentityInterpretation(
            left_artifact_identity=left_identity,
            right_artifact_identity=right_identity,
            context_identity=context.identity.digest,
            gst_registration_relation=gst_rel,
            pan_relation=pan_rel,
            lexical_relation=lexical_rel,
            legal_form_relation=legal_rel,
            corpus_distinctiveness=corpus_rel,
            warnings=tuple(warnings)
        )

    @classmethod
    def _compare_gstin(cls, left: VendorNameObservation, right: VendorNameObservation) -> GSTRegistrationRelation:
        l_miss = left.gstin_candidate is None
        r_miss = right.gstin_candidate is None
        
        if l_miss and r_miss:
            return GSTRegistrationRelation(GSTRegistrationRelationState.BOTH_MISSING, None, None)
        if l_miss and not r_miss:
            if not right.gstin_structurally_valid:
                return GSTRegistrationRelation(GSTRegistrationRelationState.ONE_UNINTERPRETABLE, None, right.gstin_candidate)
            return GSTRegistrationRelation(GSTRegistrationRelationState.LEFT_MISSING, None, right.gstin_candidate)
        if not l_miss and r_miss:
            if not left.gstin_structurally_valid:
                return GSTRegistrationRelation(GSTRegistrationRelationState.ONE_UNINTERPRETABLE, left.gstin_candidate, None)
            return GSTRegistrationRelation(GSTRegistrationRelationState.RIGHT_MISSING, left.gstin_candidate, None)
            
        # Both present
        l_valid = left.gstin_structurally_valid
        r_valid = right.gstin_structurally_valid
        
        if not l_valid and not r_valid:
            return GSTRegistrationRelation(GSTRegistrationRelationState.BOTH_UNINTERPRETABLE, left.gstin_candidate, right.gstin_candidate)
        if not l_valid:
            return GSTRegistrationRelation(GSTRegistrationRelationState.LEFT_UNINTERPRETABLE, left.gstin_candidate, right.gstin_candidate)
        if not r_valid:
            return GSTRegistrationRelation(GSTRegistrationRelationState.RIGHT_UNINTERPRETABLE, left.gstin_candidate, right.gstin_candidate)
            
        if left.gstin_candidate == right.gstin_candidate:
            return GSTRegistrationRelation(GSTRegistrationRelationState.VALID_AND_EQUAL, left.gstin_candidate, right.gstin_candidate)
        return GSTRegistrationRelation(GSTRegistrationRelationState.VALID_AND_DIFFERENT, left.gstin_candidate, right.gstin_candidate)

    @classmethod
    def _compare_pan(cls, left: VendorNameObservation, right: VendorNameObservation) -> PANRelation:
        l_miss = left.pan_candidate is None
        r_miss = right.pan_candidate is None
        
        if l_miss and r_miss:
            return PANRelation(PANRelationState.BOTH_MISSING, None, None, None)
        if l_miss and not r_miss:
            if not right.pan_structurally_valid:
                return PANRelation(PANRelationState.RIGHT_UNINTERPRETABLE, None, None, right.pan_candidate)
            return PANRelation(PANRelationState.LEFT_MISSING, None, None, right.pan_candidate)
        if not l_miss and r_miss:
            if not left.pan_structurally_valid:
                return PANRelation(PANRelationState.LEFT_UNINTERPRETABLE, None, left.pan_candidate, None)
            return PANRelation(PANRelationState.RIGHT_MISSING, None, left.pan_candidate, None)
            
        l_valid = left.pan_structurally_valid
        r_valid = right.pan_structurally_valid
        
        if not l_valid and not r_valid:
            return PANRelation(PANRelationState.BOTH_UNINTERPRETABLE, None, left.pan_candidate, right.pan_candidate)
        if not l_valid:
            return PANRelation(PANRelationState.LEFT_UNINTERPRETABLE, None, left.pan_candidate, right.pan_candidate)
        if not r_valid:
            return PANRelation(PANRelationState.RIGHT_UNINTERPRETABLE, None, left.pan_candidate, right.pan_candidate)
            
        dep = PANEvidenceDependence.INDEPENDENT
        if left.pan_derived_from_gstin and right.pan_derived_from_gstin:
            if left.gstin_candidate == right.gstin_candidate:
                dep = PANEvidenceDependence.SAME_SOURCE_DERIVATION
        elif left.pan_derived_from_gstin or right.pan_derived_from_gstin:
            dep = PANEvidenceDependence.PARTIALLY_DEPENDENT
            
        if left.pan_candidate == right.pan_candidate:
            return PANRelation(PANRelationState.VALID_AND_EQUAL, dep, left.pan_candidate, right.pan_candidate)
        return PANRelation(PANRelationState.VALID_AND_DIFFERENT, dep, left.pan_candidate, right.pan_candidate)

    @classmethod
    def _compare_lexical(cls, left: VendorNameObservation, right: VendorNameObservation, context: VendorIdentityContext) -> Tuple[LexicalRelation, Tuple[str, ...]]:
        l_empty = not left.canonical_core_text
        r_empty = not right.canonical_core_text
        
        if l_empty or r_empty:
            return LexicalRelation(LexicalRelationState.BOTH_MISSING, None, ()), ()
            
        if left.canonical_core_text == right.canonical_core_text:
            return LexicalRelation(LexicalRelationState.EXACT_NORMALIZED_CORE_EQUALITY, 1.0, left.organization_tokens), left.organization_tokens
            
        l_set = set(left.organization_tokens)
        r_set = set(right.organization_tokens)
        shared = tuple(sorted(l_set & r_set))
        
        if l_set == r_set:
            return LexicalRelation(LexicalRelationState.TOKEN_SET_EQUALITY, None, shared), shared
            
        if l_set.issubset(r_set) or r_set.issubset(l_set):
            return LexicalRelation(LexicalRelationState.BOUNDED_SUBSET, None, shared), shared
            
        # Fuzzy check
        l_len = len(left.canonical_core_text)
        r_len = len(right.canonical_core_text)
        if l_len >= context.fuzzy_minimum_length and r_len >= context.fuzzy_minimum_length:
            ratio = difflib.SequenceMatcher(None, left.canonical_core_text, right.canonical_core_text).ratio()
            if ratio >= context.fuzzy_threshold:
                return LexicalRelation(LexicalRelationState.BOUNDED_FUZZY_SIMILARITY, ratio, shared), shared
                
        return LexicalRelation(LexicalRelationState.DIFFERENT, None, shared), shared

    @classmethod
    def _compare_legal_form(cls, left: VendorNameObservation, right: VendorNameObservation) -> LegalFormRelation:
        l_miss = left.legal_form_category is None
        r_miss = right.legal_form_category is None
        
        if l_miss and r_miss:
            return LegalFormRelation(LegalFormRelationState.BOTH_MISSING, None, None)
        if l_miss and not r_miss:
            return LegalFormRelation(LegalFormRelationState.LEFT_MISSING, None, right.legal_form_category)
        if not l_miss and r_miss:
            return LegalFormRelation(LegalFormRelationState.RIGHT_MISSING, left.legal_form_category, None)
            
        if left.legal_form_category == right.legal_form_category:
            return LegalFormRelation(LegalFormRelationState.OBSERVED_COMPATIBLE, left.legal_form_category, right.legal_form_category)
        return LegalFormRelation(LegalFormRelationState.OBSERVED_INCOMPATIBLE, left.legal_form_category, right.legal_form_category)

    @classmethod
    def _evaluate_distinctiveness(cls, shared_tokens: Tuple[str, ...], context: VendorIdentityContext) -> CorpusDistinctiveness:
        if not shared_tokens:
            return CorpusDistinctiveness(CorpusDistinctivenessState.NOT_APPLICABLE, None, None)
            
        if not context.corpus_profile:
            return CorpusDistinctiveness(CorpusDistinctivenessState.NOT_APPLICABLE, None, None)
            
        best_token = None
        min_df = 1.0
        
        for t in shared_tokens:
            df = context.corpus_profile.document_frequency(t)
            if df <= min_df:
                min_df = df
                best_token = t
                
        if min_df <= context.distinctiveness_threshold:
            return CorpusDistinctiveness(CorpusDistinctivenessState.DISTINCTIVE_SUPPORT, best_token, min_df)
        return CorpusDistinctiveness(CorpusDistinctivenessState.ATTENUATED_SUPPORT, best_token, min_df)
