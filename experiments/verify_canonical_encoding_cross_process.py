import sys
import argparse
from recongraph.domain.identity import canonical_encode
from recongraph.domain.payloads import CanonicalPayloadEnvelope, TypedPayloadEnvelope

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str)
    args = parser.parse_args()

    if args.test == "nfc_nfd":
        # NFD vs NFC
        import unicodedata
        payload = {"value": unicodedata.normalize("NFD", "é")}
        print(canonical_encode(payload).hex())
    elif args.test == "nfc_nfc":
        import unicodedata
        payload = {"value": unicodedata.normalize("NFC", "é")}
        print(canonical_encode(payload).hex())
    elif args.test == "mapping_order_1":
        payload = {"a": 1, "b": 2}
        print(canonical_encode(payload).hex())
    elif args.test == "mapping_order_2":
        payload = {"b": 2, "a": 1}
        print(canonical_encode(payload).hex())

if __name__ == "__main__":
    main()
