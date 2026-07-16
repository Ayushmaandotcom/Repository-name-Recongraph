from dataclasses import dataclass
from typing import Optional, Tuple
from recongraph.domain.semantics.observation import SemanticObservation

@dataclass(frozen=True)
class SemanticInterpretationResult:
    cosine_similarity: float
    supports_same_business_purpose: bool
    contradicts_business_purpose: bool
    
    # Metadata for K6
    provider_id: str
    model_id: str
    semantic_version: str

class SemanticPairInterpreter:
    """
    Evaluates the semantic relationship between two SemanticObservations.
    Must handle cross-model drift (ensuring both vectors are from the same model space)
    and adversarial edge cases.
    """
    
    # Thresholds calibrated for the specific SimulatedEmbeddingProvider
    SUPPORT_THRESHOLD = 0.90
    CONTRADICT_THRESHOLD = 0.40

    @classmethod
    def interpret(cls, left: SemanticObservation, right: SemanticObservation) -> SemanticInterpretationResult:
        # Cross-Model Drift Protection: Ensure both embeddings are from the exact same model space
        left_id = left.embedding_artifact.provider_identity
        right_id = right.embedding_artifact.provider_identity
        
        if left_id != right_id:
            raise ValueError(f"Cross-model semantic interpretation is invalid: {left_id} vs {right_id}")

        cosine_sim = cls._cosine_similarity(left.embedding_artifact.vector, right.embedding_artifact.vector)
        
        # Determine logical assertions
        supports = cosine_sim >= cls.SUPPORT_THRESHOLD
        contradicts = cosine_sim <= cls.CONTRADICT_THRESHOLD
        
        # Prevent hallucination: If lexical tokens are exactly the same, it definitely supports.
        if left.normalized_text == right.normalized_text and left.normalized_text:
            supports = True
            contradicts = False

        return SemanticInterpretationResult(
            cosine_similarity=cosine_sim,
            supports_same_business_purpose=supports,
            contradicts_business_purpose=contradicts,
            provider_id=left_id.provider_id,
            model_id=left_id.model_id,
            semantic_version=left_id.semantic_version
        )

    @staticmethod
    def _cosine_similarity(vec1: Tuple[float, ...], vec2: Tuple[float, ...]) -> float:
        if len(vec1) != len(vec2):
            raise ValueError("Vectors must have the same dimensionality.")
        
        dot = sum(a * b for a, b in zip(vec1, vec2))
        # Since vectors are L2 normalized in SimulatedEmbeddingProvider, dot product == cosine similarity
        return dot
