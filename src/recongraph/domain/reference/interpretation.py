from dataclasses import dataclass

from recongraph.domain.reference.artifact import ReferenceIdentifierArtifact
from recongraph.domain.reference.factors import ReferenceRelation, ReferenceRelationState

@dataclass(frozen=True)
class ReferencePairInterpretation:
    left_artifact: ReferenceIdentifierArtifact
    right_artifact: ReferenceIdentifierArtifact
    relation: ReferenceRelation

class ReferencePairInterpreter:
    @classmethod
    def interpret(
        cls,
        left: ReferenceIdentifierArtifact,
        right: ReferenceIdentifierArtifact
    ) -> ReferencePairInterpretation:
        
        l_valid = left.parsed_result.is_valid
        r_valid = right.parsed_result.is_valid
        
        if not l_valid and not r_valid:
            rel = ReferenceRelation(ReferenceRelationState.BOTH_MISSING, frozenset())
        elif not l_valid or not r_valid:
            rel = ReferenceRelation(ReferenceRelationState.ONE_MISSING, frozenset())
        else:
            shared = left.parsed_result.numeric_tokens & right.parsed_result.numeric_tokens
            if left.parsed_result.normalized_value == right.parsed_result.normalized_value:
                rel = ReferenceRelation(ReferenceRelationState.EXACT_MATCH, shared)
            else:
                rel = ReferenceRelation(ReferenceRelationState.DISTINCT, shared)
                
        return ReferencePairInterpretation(
            left_artifact=left,
            right_artifact=right,
            relation=rel
        )
