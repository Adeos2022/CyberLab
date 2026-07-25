import sys
import os
import argparse
from datetime import datetime

try:
    import exifread
except ImportError:
    exifread = None


def get_basic_info(filepath):
    """Return basic filesystem metadata for any file."""
    stat = os.stat(filepath)
    return {
        "File size (bytes)": stat.st_size,
        "Created": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
        "Modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
    }


def get_exif_data(filepath):
    """Extract EXIF metadata from an image file, if present."""
    if exifread is None:
        return None

    with open(filepath, "rb") as f:
        tags = exifread.process_file(f, details=False)

    if not tags:
        return None

    interesting = [
        "Image Make", "Image Model", "Image DateTime", "GPS GPSLatitude",
        "GPS GPSLongitude", "EXIF DateTimeOriginal", "Image Software"
    ]
    found = {}
    for tag in interesting:
        if tag in tags:
            found[tag] = str(tags[tag])
    return found


def extract(filepath):
    """Extract and print all available metadata for a file."""
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    print(f"\nMetadata for: {filepath}")
    print("-" * 50)

    basic = get_basic_info(filepath)
    print("Basic file info:")
    for k, v in basic.items():
        print(f"  {k}: {v}")

    exif = get_exif_data(filepath)
    if exif:
        print("\nEXIF data found:")
        for k, v in exif.items():
            print(f"  {k}: {v}")
    elif exifread is None:
        print("\n(exifread not installed — image EXIF data unavailable. Run: pip install exifread)")
    else:
        print("\nNo EXIF data found (not an image, or metadata was stripped).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract basic and EXIF metadata from a file."
    )
    parser.add_argument("filepath", help="Path to the file to inspect")

    args = parser.parse_args()
    extract(args.filepath)
