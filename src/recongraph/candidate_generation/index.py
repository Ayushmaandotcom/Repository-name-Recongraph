from typing import Any, Iterable
from collections import defaultdict
from recongraph.candidate_generation.blockers import Blocker

class InvertedIndex:
    """
    Maintains a mapping of blocking keys to the records that possess them.
    """
    def __init__(self, blockers: Iterable[Blocker]):
        self.blockers = tuple(blockers)
        self.index: dict[str, set[Any]] = defaultdict(set)
        
    def add(self, record: Any) -> frozenset[str]:
        keys = set()
        for blocker in self.blockers:
            keys.update(blocker.extract_keys(record))
            
        for key in keys:
            self.index[key].add(record)
            
        return frozenset(keys)
        
    def add_many(self, records: Iterable[Any]) -> None:
        for record in records:
            self.add(record)
            
    def query(self, key: str) -> frozenset[Any]:
        return frozenset(self.index.get(key, set()))
