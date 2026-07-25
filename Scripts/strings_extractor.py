import sys
import argparse
import re


def extract_strings(filepath, min_length=4):
    """Extract sequences of printable ASCII characters from a binary file."""
    try:
        with open(filepath, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    pattern = rb"[\x20-\x7E]{%d,}" % min_length
    matches = re.findall(pattern, data)
    return [m.decode("ascii", errors="ignore") for m in matches]


def highlight_interesting(strings):
    """Flag strings that look like URLs, file paths, or IP addresses."""
    interesting = []
    for s in strings:
        if re.search(r"https?://", s) or re.search(r"\b\d+\.\d+\.\d+\.\d+\b", s) or "/" in s or "\\" in s:
            interesting.append(s)
    return interesting


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract printable strings from a binary file (like the classic 'strings' utility)."
    )
    parser.add_argument("filepath", help="Path to the file to inspect")
    parser.add_argument("-n", "--min-length", type=int, default=4, help="Minimum string length to extract (default: 4)")
    parser.add_argument("--interesting-only", action="store_true", help="Only show strings that look like URLs, paths, or IPs")

    args = parser.parse_args()
    strings = extract_strings(args.filepath, args.min_length)

    if args.interesting_only:
        strings = highlight_interesting(strings)

    print(f"\nExtracted {len(strings)} string(s) from {args.filepath}:")
    print("-" * 50)
    for s in strings:
        print(s)
