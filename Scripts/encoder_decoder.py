import sys
import argparse
import base64


def encode(text, fmt):
    """Encode text into the specified format (base64 or hex)."""
    data = text.encode()
    if fmt == "base64":
        return base64.b64encode(data).decode()
    elif fmt == "hex":
        return data.hex()


def decode(text, fmt):
    """Decode text from the specified format (base64 or hex) back to plain text."""
    try:
        if fmt == "base64":
            return base64.b64decode(text).decode(errors="replace")
        elif fmt == "hex":
            return bytes.fromhex(text).decode(errors="replace")
    except Exception as e:
        print(f"Decode failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encode or decode text using Base64 or Hex."
    )
    parser.add_argument("mode", choices=["encode", "decode"], help="Operation to perform")
    parser.add_argument("format", choices=["base64", "hex"], help="Encoding format")
    parser.add_argument("text", help="Text to process")

    args = parser.parse_args()

    if args.mode == "encode":
        print(encode(args.text, args.format))
    else:
        print(decode(args.text, args.format))
