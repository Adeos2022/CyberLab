import sys
import hashlib
import argparse


def hash_file(filepath, algorithm="sha256"):
    """Compute the hash of a file's contents, reading in chunks to save memory."""
    try:
        hasher = hashlib.new(algorithm)
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)
    except PermissionError:
        print(f"Permission denied reading: {filepath}")
        sys.exit(1)
    except ValueError:
        print(f"Unsupported algorithm: {algorithm}")
        sys.exit(1)


def hash_text(text, algorithm="sha256"):
    """Compute the hash of a plain text string."""
    try:
        hasher = hashlib.new(algorithm)
        hasher.update(text.encode())
        return hasher.hexdigest()
    except ValueError:
        print(f"Unsupported algorithm: {algorithm}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute a hash (MD5, SHA1, SHA256, etc.) of a file or text string."
    )
    parser.add_argument("mode", choices=["file", "text"], help="Whether to hash a file or plain text")
    parser.add_argument("value", help="Path to the file, or the text string to hash")
    parser.add_argument(
        "-a", "--algorithm",
        default="sha256",
        help="Hash algorithm to use (default: sha256). Options include md5, sha1, sha256, sha512."
    )

    args = parser.parse_args()

    if args.mode == "file":
        result = hash_file(args.value, args.algorithm)
    else:
        result = hash_text(args.value, args.algorithm)

    print(f"{args.algorithm.upper()} hash: {result}")
