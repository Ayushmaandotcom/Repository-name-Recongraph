from dataclasses import dataclass
from typing import Optional

from recongraph.domain.document.layout import DocumentLayoutArtifact, DocumentRegion

@dataclass(frozen=True)
class DocumentLayoutInterpretation:
    has_signature: bool
    has_totals_block: bool
    has_header: bool

class DocumentLayoutInterpreter:
    @classmethod
    def interpret(cls, layout: Optional[DocumentLayoutArtifact]) -> DocumentLayoutInterpretation:
        if not layout:
            return DocumentLayoutInterpretation(False, False, False)
            
        has_signature = len(layout.get_blocks_by_region(DocumentRegion.SIGNATURE)) > 0
        has_totals_block = len(layout.get_blocks_by_region(DocumentRegion.TOTALS_BLOCK)) > 0
        has_header = len(layout.get_blocks_by_region(DocumentRegion.HEADER)) > 0
        
        return DocumentLayoutInterpretation(
            has_signature=has_signature,
            has_totals_block=has_totals_block,
            has_header=has_header
        )
