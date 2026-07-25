import sys
import argparse
import requests


def inspect_cookies(url):
    """Fetch a URL and analyze any cookies set in the response for security flags."""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to {url}: {e}")
        sys.exit(1)

    print(f"\nCookie inspection for: {url}")
    print("-" * 50)

    if not response.cookies:
        print("No cookies were set by this site.")
        return

    for cookie in response.cookies:
        print(f"\nCookie: {cookie.name}")
        print(f"  Value: {cookie.value[:40]}{'...' if len(cookie.value) > 40 else ''}")
        print(f"  Domain: {cookie.domain}")
        print(f"  Secure: {'Yes' if cookie.secure else 'NO — cookie can be sent over unencrypted HTTP'}")

        httponly = cookie.has_nonstandard_attr("HttpOnly") or "httponly" in [k.lower() for k in cookie._rest.keys()]
        print(f"  HttpOnly: {'Yes' if httponly else 'NO — cookie is accessible via JavaScript (XSS risk)'}")

        samesite = cookie._rest.get("SameSite") or cookie._rest.get("samesite")
        print(f"  SameSite: {samesite if samesite else 'NOT SET — vulnerable to CSRF in some browsers'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inspect cookies set by a website and check for common security flag issues."
    )
    parser.add_argument("url", help="Target URL or domain (e.g. example.com)")

    args = parser.parse_args()
    inspect_cookies(args.url)
