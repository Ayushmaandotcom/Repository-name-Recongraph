from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class DocumentRegion(Enum):
    HEADER = auto()
    FOOTER = auto()
    TOTALS_BLOCK = auto()
    SIGNATURE = auto()
    TABLE_ROW = auto()
    VENDOR_DETAILS = auto()

@dataclass(frozen=True)
class BoundingBox:
    x0: float
    y0: float
    x1: float
    y1: float
    page_num: int
    
    def overlaps(self, other: "BoundingBox") -> bool:
        if self.page_num != other.page_num:
            return False
        return not (self.x1 < other.x0 or self.x0 > other.x1 or self.y1 < other.y0 or self.y0 > other.y1)
        
    def contains(self, other: "BoundingBox") -> bool:
        if self.page_num != other.page_num:
            return False
        return (self.x0 <= other.x0 and self.x1 >= other.x1 and 
                self.y0 <= other.y0 and self.y1 >= other.y1)

@dataclass(frozen=True)
class DocumentBlock:
    region_type: DocumentRegion
    box: BoundingBox
    text: Optional[str] = None
    confidence: float = 1.0

@dataclass(frozen=True)
class DocumentLayoutArtifact:
    """Represents the structural map of a document."""
    blocks: tuple[DocumentBlock, ...]
    
    def get_blocks_by_region(self, region: DocumentRegion) -> List[DocumentBlock]:
        return [b for b in self.blocks if b.region_type == region]
