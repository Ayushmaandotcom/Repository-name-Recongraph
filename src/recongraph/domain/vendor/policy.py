from typing import List

from recongraph.domain.vendor.factors import (
    GSTRegistrationRelationState, PANRelationState, PANEvidenceDependence,
    LexicalRelationState, LegalFormRelationState, CorpusDistinctivenessState,
    OrganizationalRelationState
)
from recongraph.domain.vendor.interpretation import VendorIdentityInterpretation
from recongraph.domain.vendor.projection import VendorEvidenceProjection

class VendorProjectionPolicyV1:
    """
    Implements a lossy projection from VendorIdentityInterpretation into a legacy scalar.
    It intentionally caps similarity when unresolvable conflict or uninformative lexical
    equality occurs.
    """
    
    VERSION = "1.0.0"
    
    # Legacy threshold is 0.90
    PAN_CONFLICT_CAP = 0.40
    LEGAL_FORM_CONFLICT_CAP = 0.85
    ATTENUATED_SUPPORT_CAP = 0.85
    
    @classmethod
    def project(cls, interpretation: VendorIdentityInterpretation) -> VendorEvidenceProjection:
        considered_factors: List[str] = []
        missing_factors: List[str] = []
        uninterpretable_factors: List[str] = []
        dependence_groups: List[str] = []
        contradiction_markers: List[str] = []
        warnings: List[str] = []
        
        # 1. Evaluate Lexical Relation for Base Similarity
        lex = interpretation.lexical_relation
        base_similarity = None
        
        if lex.state == LexicalRelationState.BOTH_MISSING:
            missing_factors.append("lexical_relation")
        elif lex.state == LexicalRelationState.EXACT_NORMALIZED_CORE_EQUALITY:
            considered_factors.append("lexical_relation")
            base_similarity = 1.0
        elif lex.state == LexicalRelationState.TOKEN_SET_EQUALITY:
            considered_factors.append("lexical_relation")
            base_similarity = 0.95
        elif lex.state == LexicalRelationState.BOUNDED_SUBSET:
            considered_factors.append("lexical_relation")
            base_similarity = 0.90
        elif lex.state == LexicalRelationState.BOUNDED_FUZZY_SIMILARITY:
            considered_factors.append("lexical_relation")
            base_similarity = lex.similarity_score
        elif lex.state == LexicalRelationState.DIFFERENT:
            considered_factors.append("lexical_relation")
            base_similarity = lex.similarity_score if lex.similarity_score is not None else 0.0
            
        # 1.5 Evaluate Organizational Knowledge Base (Overrides Lexical)
        org = interpretation.organizational_relation
        if org.state in (OrganizationalRelationState.KNOWN_ALIAS, OrganizationalRelationState.PARENT_SUBSIDIARY, OrganizationalRelationState.HISTORICAL_RENAME):
            considered_factors.append("organizational_relation")
            base_similarity = 1.0
            contradiction_markers = [m for m in contradiction_markers if m != "LEGAL_FORM_LEXICAL_DIFFERENCE"] # Clear lexical-based warnings
        elif org.state == OrganizationalRelationState.UNAFFILIATED:
            considered_factors.append("organizational_relation")
            base_similarity = 0.0
            contradiction_markers.append("KNOWN_UNAFFILIATED_ENTITIES")
            
        # 2. Evaluate Distinctiveness (Attenuator)
        dist = interpretation.corpus_distinctiveness
        if dist.state == CorpusDistinctivenessState.ATTENUATED_SUPPORT:
            considered_factors.append("corpus_distinctiveness")
            if base_similarity is not None and base_similarity > cls.ATTENUATED_SUPPORT_CAP:
                base_similarity = cls.ATTENUATED_SUPPORT_CAP
        elif dist.state == CorpusDistinctivenessState.DISTINCTIVE_SUPPORT:
            considered_factors.append("corpus_distinctiveness")
            
        # 3. Evaluate Legal Form
        legal = interpretation.legal_form_relation
        if legal.state == LegalFormRelationState.BOTH_MISSING or \
           legal.state == LegalFormRelationState.LEFT_MISSING or \
           legal.state == LegalFormRelationState.RIGHT_MISSING:
            missing_factors.append("legal_form_relation")
        elif legal.state == LegalFormRelationState.OBSERVED_COMPATIBLE:
            considered_factors.append("legal_form_relation")
        elif legal.state == LegalFormRelationState.OBSERVED_INCOMPATIBLE:
            considered_factors.append("legal_form_relation")
            contradiction_markers.append("LEGAL_FORM_LEXICAL_DIFFERENCE")
            if base_similarity is not None and base_similarity > cls.LEGAL_FORM_CONFLICT_CAP:
                base_similarity = cls.LEGAL_FORM_CONFLICT_CAP
                

        # 4. Evaluate Tax Identifiers & Dependence
        gst = interpretation.gst_registration_relation
        pan = interpretation.pan_relation
        
        # Missingness & Uninterpretable
        if gst.state == GSTRegistrationRelationState.BOTH_MISSING:
            missing_factors.append("gst_registration_relation")
        elif gst.state in (GSTRegistrationRelationState.BOTH_UNINTERPRETABLE, GSTRegistrationRelationState.LEFT_UNINTERPRETABLE, GSTRegistrationRelationState.RIGHT_UNINTERPRETABLE):
            uninterpretable_factors.append("gst_registration_relation")
        else:
            considered_factors.append("gst_registration_relation")
            
        if pan.state == PANRelationState.BOTH_MISSING:
            missing_factors.append("pan_relation")
        elif pan.state in (PANRelationState.BOTH_UNINTERPRETABLE, PANRelationState.LEFT_UNINTERPRETABLE, PANRelationState.RIGHT_UNINTERPRETABLE):
            uninterpretable_factors.append("pan_relation")
        else:
            considered_factors.append("pan_relation")
            
        # Contradictions & Capping
        if pan.state == PANRelationState.VALID_AND_DIFFERENT:
            contradiction_markers.append("PAN_IDENTIFIER_CONFLICT")
            # Enforce 0.72 problem cap
            if base_similarity is not None and base_similarity > cls.PAN_CONFLICT_CAP:
                base_similarity = cls.PAN_CONFLICT_CAP
                
        if gst.state == GSTRegistrationRelationState.VALID_AND_DIFFERENT:
            contradiction_markers.append("GST_REGISTRATION_IDENTIFIER_DIFFERENCE")
            # Note: We do not necessarily cap base_similarity heavily for GST difference 
            # if PAN matches, because different state GSTINs for same PAN is common.
            
        # Dependence Groups
        if pan.dependence == PANEvidenceDependence.SAME_SOURCE_DERIVATION:
            dependence_groups.append("TAX_EVIDENCE_GROUP")
            
        return VendorEvidenceProjection(
            similarity=base_similarity,
            policy_identity=f"VendorProjectionPolicyV1_{cls.VERSION}",
            source_interpretation_identity=interpretation.context_identity, # the tuple context identity represents the source semantics
            considered_factors=tuple(considered_factors),
            missing_factors=tuple(missing_factors),
            uninterpretable_factors=tuple(uninterpretable_factors),
            dependence_groups=tuple(dependence_groups),
            contradiction_markers=tuple(contradiction_markers),
            warnings=tuple(warnings)
        )
