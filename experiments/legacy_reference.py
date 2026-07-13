from typing import Optional
from recongraph.normalization.text import normalize_reference

def extract_numeric_reference_tokens(
    reference: str,
    min_length: int = 3,
) -> tuple[str, ...]:
    if min_length < 1:
        raise ValueError("min_length must be positive")
        
    if not reference:
        return ()
        
    tokens = []
    current_token = []
    
    for char in reference:
        if char.isdigit():
            current_token.append(char)
        else:
            if current_token:
                if len(current_token) >= min_length:
                    tokens.append("".join(current_token))
                current_token = []
                
    if current_token and len(current_token) >= min_length:
        tokens.append("".join(current_token))
        
    return tuple(tokens)

def reference_score(
    reference_a: str | None,
    reference_b: str | None,
    shared_numeric_score: float = 0.8,
) -> float | None:
    if not reference_a or not reference_b:
        return None

    if not reference_a.strip() or not reference_b.strip():
        return None

    normalized_a = normalize_reference(reference_a)
    normalized_b = normalize_reference(reference_b)

    if normalized_a == normalized_b:
        return 1.0

    numeric_tokens_a = extract_numeric_reference_tokens(
        reference_a, min_length=3
    )
    numeric_tokens_b = extract_numeric_reference_tokens(
        reference_b, min_length=3
    )

    shared_tokens = set(numeric_tokens_a).intersection(numeric_tokens_b)
    
    for token in shared_tokens:
        if len(token) == 4 and 1900 <= int(token) <= 2100:
            continue
        return shared_numeric_score

    return 0.0
