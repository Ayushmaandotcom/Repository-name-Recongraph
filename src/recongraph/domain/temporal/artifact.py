from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class TemporalArtifact:
    record_date: datetime.date
    filing_period: str | None = None
    
    @classmethod
    def create(cls, record_date: datetime.date, filing_period: str | None = None) -> "TemporalArtifact":
        return cls(record_date=record_date, filing_period=filing_period)
