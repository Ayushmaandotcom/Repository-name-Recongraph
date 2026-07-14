# Tax Scalar Information Loss

The current tax scalar reduces all of the following to 0.0:
- Missing vs Missing (wait, actually None for Missing)
- Different state GSTIN / Same PAN (0.0)
- Different PAN (0.0)
- Structurally invalid vs invalid (1.0 if identical)
- Interstate registrations of the same legal entity (0.0)

The information loss is CRITICAL.
