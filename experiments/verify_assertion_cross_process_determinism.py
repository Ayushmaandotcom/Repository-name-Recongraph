import sys
from recongraph.domain.assertions import EvidenceAssertion, AssertionPolarity, EvidenceAncestryRef
from recongraph.domain.identity import KernelIdentityRef, IdentityDomainId, IdentitySchemaId, IdentityDigest
from recongraph.domain.authority import AuthorityDescriptor, AuthorityBasisId
from recongraph.domain.scopes import Proposition, PropositionSubject, ScopeKind, SubjectRef
from recongraph.domain.claims import CoreClaims

def main():
    claim = CoreClaims.SAME_LEGAL_ENTITY
    subject = PropositionSubject.create(claim, ScopeKind.RECORD_PAIR, left=[SubjectRef("urn:1")], right=[SubjectRef("urn:2")])
    prop = Proposition(claim, subject)
    ancestry = EvidenceAncestryRef(KernelIdentityRef(IdentityDomainId("recongraph.observation_occurrence"), IdentitySchemaId("x.v1"), IdentityDigest("sha256:" + "a"*64)))
    
    a1 = EvidenceAssertion(prop, AssertionPolarity.SUPPORT, 1.0, AuthorityDescriptor(AuthorityBasisId("a")), ancestry)
    print(a1.identity.digest)

if __name__ == "__main__":
    main()
