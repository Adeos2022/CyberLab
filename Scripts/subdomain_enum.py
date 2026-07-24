import socket
import sys
import argparse


def enumerate_subdomains(domain, wordlist_path):
    """Check each word in a wordlist as a subdomain of the target domain and report which resolve."""
    try:
        with open(wordlist_path, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Wordlist not found: {wordlist_path}")
        sys.exit(1)

    print(f"\nEnumerating subdomains of {domain} using {len(words)} words...")
    print("-" * 50)

    found = []

    for word in words:
        subdomain = f"{word}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"FOUND: {subdomain} -> {ip}")
            found.append(subdomain)
        except socket.gaierror:
            continue

    print("-" * 50)
    print(f"Scan complete. {len(found)} subdomain(s) found out of {len(words)} checked.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enumerate subdomains of a target domain using a wordlist."
    )
    parser.add_argument("domain", help="Target domain (e.g. example.com)")
    parser.add_argument("wordlist", help="Path to a wordlist file of subdomain names")

    args = parser.parse_args()
    enumerate_subdomains(args.domain, args.wordlist)
