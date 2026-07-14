# Source Version Placement Decision

## SV001
Can the same logical artifact mutate?
**Yes.** (e.g. ERP rows, manually edited worksheets).

## SV002
If yes, must two versions have different lineage?
**Yes.** An assertion about V1 is not an assertion about V2.

## SV003
Does SourceArtifactId identify logical persistence or exact source state?
**Logical persistence.** `SourceArtifactId("purchase_invoice:874219")` points to the row, not its temporal state.

## SV004
If it identifies exact state, how do we refer to the logical artifact across versions?
N/A (Identifies logical persistence).

## SV005
If it identifies logical persistence, where is version state represented?
In an explicit `SourceVersionRef` that acts as a state qualifier over the artifact.

## SV006
Can a source lacking native row versions still create lineage?
**Yes.** The version qualifier becomes `None`.

## SV007
Is ingestion batch ID a source version?
**No.** Ingestion is an operational event in our pipeline, not a state identity of the upstream source. 

## SV008
Is content hash always a valid source version?
**No.** For independently duplicated documents, identical content hashes can belong to different `SourceArtifactIds` (Upload 1 vs Upload 2). Using content hash as version conflates observation content identity with source temporal occurrence.

## SV009
Can an artifact version be unknown?
**Yes.** Many APIs or document uploads do not expose a strict upstream revision tag.

## SV010
Does unknown version destroy lineage validity?
**No.** It merely signifies our provenance knowledge is limited to the logical artifact coordinate.

## SV011
Does unknown version affect cache eligibility?
**Yes.** An unknown mutable source cannot be safely cached for temporal replay if the derivation relies on exact upstream state (EXTERNAL_SNAPSHOT_DEPENDENT).

## SV012
Should version state be an optional field?
**Yes.** `SourceVersionRef | None`.

## SV013
Would optional version create identity ambiguity?
**No.** `None` means explicitly "we do not know the version", whereas `"v1"` means explicitly "version 1". They are distinct epistemic states.

## SV014
Can the cache distinguish: known stable snapshot vs unknown mutable source if version is omitted?
**Yes.** If omitted (`None`), the cache must assume the source is an unknown mutable source (NONDETERMINISTIC) and refuse global caching, unless the derivation itself is pure and only relies on the extracted Observation content state (which is safe).

## SV015
Final decision.
The 3-part ontology (`SourceSystem`, `SourceArtifact`, `SourceLocator`) is the core coordinate. 
**`SourceVersionRef` is a state qualifier over the artifact.** 
The architecture must be:
```python
SourceSystemId
SourceArtifactId
SourceVersionRef | None
SourceLocator
```
