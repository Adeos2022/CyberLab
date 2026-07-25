import sys
import argparse
import requests


def brute_force(base_url, wordlist_path, timeout=3):
    """Check each word in a wordlist as a path against the target URL and report which respond."""
    if not base_url.startswith(("http://", "https://")):
        base_url = "https://" + base_url
    base_url = base_url.rstrip("/")

    try:
        with open(wordlist_path, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Wordlist not found: {wordlist_path}")
        sys.exit(1)

    print(f"\nBrute-forcing {base_url} with {len(words)} paths...")
    print("-" * 50)

    found = []
    for word in words:
        url = f"{base_url}/{word}"
        try:
            response = requests.get(url, timeout=timeout, allow_redirects=False)
            if response.status_code < 400:
                print(f"FOUND [{response.status_code}]: {url}")
                found.append((url, response.status_code))
            elif response.status_code in (301, 302, 403):
                print(f"INTERESTING [{response.status_code}]: {url}")
                found.append((url, response.status_code))
        except requests.exceptions.RequestException:
            continue

    print("-" * 50)
    print(f"Scan complete. {len(found)} interesting path(s) found out of {len(words)} checked.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Brute-force common directory/file paths on a website using a wordlist."
    )
    parser.add_argument("url", help="Target URL or domain (e.g. example.com)")
    parser.add_argument("wordlist", help="Path to a wordlist file of paths to check")
    parser.add_argument("-t", "--timeout", type=float, default=3, help="Request timeout in seconds (default: 3)")

    args = parser.parse_args()
    brute_force(args.url, args.wordlist, args.timeout)
