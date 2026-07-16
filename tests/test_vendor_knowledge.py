import pytest
from recongraph.domain.vendor.knowledge import OrganizationalKnowledgeBase, KnowledgeBaseEntry, AliasRelation
from recongraph.domain.vendor.context import VendorIdentityContext
from recongraph.domain.vendor.corpus import VendorCorpusProfile
from recongraph.domain.vendor.factors import OrganizationalRelationState
from recongraph.domain.vendor.interpretation import VendorPairInterpreter
from recongraph.domain.vendor.parser import DeterministicVendorParser

def test_organizational_knowledge_base_relations():
    kb = OrganizationalKnowledgeBase({
        "ALPHABET": {KnowledgeBaseEntry("GOOGLE", AliasRelation.PARENT_SUBSIDIARY)},
        "GOOGLE": {KnowledgeBaseEntry("ALPHABET", AliasRelation.PARENT_SUBSIDIARY)}
    })
    
    # Test known relation
    assert kb.get_relation("ALPHABET", "GOOGLE") == AliasRelation.PARENT_SUBSIDIARY
    assert kb.get_relation("GOOGLE", "ALPHABET") == AliasRelation.PARENT_SUBSIDIARY
    
    # Test identity relation (implicit)
    assert kb.get_relation("GOOGLE", "GOOGLE") == AliasRelation.KNOWN_ALIAS
    
    # Test unknown relation
    assert kb.get_relation("APPLE", "GOOGLE") == AliasRelation.NO_KNOWLEDGE


def test_vendor_context_digest_incorporates_knowledge_base():
    kb1 = OrganizationalKnowledgeBase.empty()
    kb2 = OrganizationalKnowledgeBase({
        "A": {KnowledgeBaseEntry("B", AliasRelation.KNOWN_ALIAS)}
    })
    
    ctx1 = VendorIdentityContext(
        corpus_profile=None,
        knowledge_base=kb1,
        interpreter_policy_version="1.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    
    ctx2 = VendorIdentityContext(
        corpus_profile=None,
        knowledge_base=kb2,
        interpreter_policy_version="1.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    
    assert ctx1.identity.digest != ctx2.identity.digest


def test_interpreter_utilizes_knowledge_base():
    kb = OrganizationalKnowledgeBase({
        "ALPHABET": {KnowledgeBaseEntry("GOOGLE", AliasRelation.PARENT_SUBSIDIARY)}
    })
    
    ctx = VendorIdentityContext(
        corpus_profile=VendorCorpusProfile(100, {}, "empty"),
        knowledge_base=kb,
        interpreter_policy_version="1.0",
        fuzzy_minimum_length=6,
        fuzzy_threshold=0.85,
        distinctiveness_threshold=0.01
    )
    
    left = DeterministicVendorParser.parse("ALPHABET INC")
    right = DeterministicVendorParser.parse("GOOGLE LLC")
    
    interp = VendorPairInterpreter._evaluate_organizational_knowledge(left, right, ctx)
    assert interp.state == OrganizationalRelationState.PARENT_SUBSIDIARY
