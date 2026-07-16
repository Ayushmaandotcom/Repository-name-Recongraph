from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class TemporalArtifact:
    record_date: datetime.date
    
    @classmethod
    def create(cls, record_date: datetime.date) -> "TemporalArtifact":
        return cls(record_date=record_date)
