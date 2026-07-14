# K4/K5 Performance Model
## Part O — Analytical Capacity

### Projections (100k purchases/GST)
- **Observations**: ~1.5M unique identities
- **Derivations**: ~8M invocations
- **Assertions**: ~10M unique identities

### Memory Risks
Using naive `@dataclass(frozen=True)` for 10M nodes will exhaust RAM due to Python object overhead (~150 bytes per object).
**Future Optimizations**: Integer Node IDs mapping to Arena Storage (NumPy/Arrow), or Content-Addressed Object Store. We will design K4/K5 to serialize cleanly to integers later.
