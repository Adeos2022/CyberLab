import socket
import sys
import argparse


def is_ip(value):
    """Return True if the given string looks like a valid IPv4 address."""
    parts = value.split(".")
    if len(parts) != 4:
        return False
    return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)


def lookup_domain(domain):
    """Resolve a domain name to its IP address."""
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to: {ip}")
    except socket.gaierror:
        print(f"Could not resolve: {domain}")


def reverse_lookup(ip):
    """Resolve an IP address to its hostname (reverse DNS)."""
    try:
        host = socket.gethostbyaddr(ip)
        print(f"{ip} resolves to: {host[0]}")
    except socket.herror:
        print(f"Could not find hostname for: {ip}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Look up a domain's IP address, or an IP's hostname (reverse DNS)."
    )
    parser.add_argument("query", help="A domain name (e.g. example.com) or an IP address (e.g. 8.8.8.8)")

    args = parser.parse_args()

    if is_ip(args.query):
        reverse_lookup(args.query)
    else:
        lookup_domain(args.query)
