# Typed Payload Contract

This document evaluates how to safely bridge typed Python dataclasses into serializable JSON boundaries without recreating a typed dumping ground.

## Payload Designs

### TP-A — Dataclass Payloads with Protocol
Uses standard `dataclasses` conforming to a structural `Protocol` defining a `schema_version`.
* **Deserialization Flaw:** `json.loads()` produces a `dict`. To get a dataclass back, the reader must know *which* dataclass to instantiate.

### TP-B — Generic Type Parameter Only
`EvidenceContribution[VendorPayload]`
* **Flaw:** Python generics erase at runtime. You cannot instantiate `T_Payload` from a JSON trace without a registry.

### TP-C — Tagged Serializable Union
Each payload is serialized as: `{"payload_type": "vendor_identity", "schema_version": 1, "payload": {...}}`
* **Advantage:** Safe trace serialization. Readers can conditionally ignore payloads they don't understand based on the tag.

### TP-D — Registry-Based Codec
Plugins register serializers: `PayloadRegistry.register(VendorPayload)`.
* **Advantage:** Highly extensible. But creates global state and security risks if malicious trace files are loaded (similar to `pickle`).

## Historical Trace Handling (V1 vs V3)
**Scenario:** 
Historical trace: `payload_type = vendor_identity`, `schema_version = 1`. 
Current code expects `VendorIdentityPayloadV3`.
**Behavior:**
The trace reader should NOT crash. It should deserialize the payload into a generic `dict` (or a `LegacyPayload` stub) marked as `schema_version=1`. The visualization layer can render the dict. The reasoning engine should *not* attempt to re-evaluate it unless a specific `V1_to_V3_Upgrader` is registered.

## Recommendation
**TP-C (Tagged Serializable Union).** It ensures that if a plugin introduces a new payload type, the core engine can serialize and deserialize the envelope without needing to import the plugin's code. If the reader lacks the Python class, it simply preserves the JSON dict along with the type tag.
