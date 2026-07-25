import sys
import os
import json
import hashlib
import argparse

BASELINE_FILE = "../Reports/integrity_baseline.json"


def hash_file(filepath):
    """Compute the SHA256 hash of a file, reading in chunks."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def build_baseline(directory):
    """Hash every file in a directory (recursively) and save the results as a baseline."""
    baseline = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                baseline[path] = hash_file(path)
            except (PermissionError, FileNotFoundError):
                continue

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=2)

    print(f"Baseline created for {len(baseline)} file(s) in '{directory}'.")
    print(f"Saved to: {BASELINE_FILE}")


def check_integrity(directory):
    """Compare current file hashes against the saved baseline and report any changes."""
    try:
        with open(BASELINE_FILE, "r") as f:
            baseline = json.load(f)
    except FileNotFoundError:
        print("No baseline found. Run with --build first.")
        sys.exit(1)

    current = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                current[path] = hash_file(path)
            except (PermissionError, FileNotFoundError):
                continue

    modified = [p for p in baseline if p in current and baseline[p] != current[p]]
    deleted = [p for p in baseline if p not in current]
    added = [p for p in current if p not in baseline]

    print(f"\nIntegrity check for '{directory}':")
    print("-" * 50)

    if not modified and not deleted and not added:
        print("No changes detected. All files match the baseline.")
    else:
        if modified:
            print(f"MODIFIED ({len(modified)}):")
            for p in modified:
                print(f"  {p}")
        if deleted:
            print(f"DELETED ({len(deleted)}):")
            for p in deleted:
                print(f"  {p}")
        if added:
            print(f"NEW ({len(added)}):")
            for p in added:
                print(f"  {p}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Monitor a directory for file changes using SHA256 hashing."
    )
    parser.add_argument("directory", help="Directory to monitor")
    parser.add_argument("--build", action="store_true", help="Build a new baseline instead of checking against one")

    args = parser.parse_args()

    if args.build:
        build_baseline(args.directory)
    else:
        check_integrity(args.directory)
