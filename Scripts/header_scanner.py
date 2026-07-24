import sys
import argparse
import requests


SECURITY_HEADERS = {
    "Strict-Transport-Security": "Missing HSTS — site may allow insecure HTTP connections",
    "X-Content-Type-Options": "Missing X-Content-Type-Options — browser may MIME-sniff content",
    "X-Frame-Options": "Missing X-Frame-Options — site may be vulnerable to clickjacking",
    "Content-Security-Policy": "Missing Content-Security-Policy — no defense-in-depth against XSS",
    "Referrer-Policy": "Missing Referrer-Policy — referrer data may leak to third parties",
}


def scan_headers(url):
    """Fetch a URL and check its response headers for common security best practices."""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to {url}: {e}")
        sys.exit(1)

    print(f"\nScanned: {url}")
    print(f"Status code: {response.status_code}")
    print("-" * 50)

    headers = response.headers
    findings = []

    for header, warning in SECURITY_HEADERS.items():
        if header not in headers:
            findings.append(warning)

    if "Server" in headers:
        findings.append(f"Server header exposes: {headers['Server']} (consider hiding version info)")

    if findings:
        print("Findings:")
        for f in findings:
            print(f"  - {f}")
    else:
        print("No common issues found. All checked security headers are present.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check a website's HTTP response headers for common security misconfigurations."
    )
    parser.add_argument("url", help="Target URL or domain (e.g. example.com)")

    args = parser.parse_args()
    scan_headers(args.url)
