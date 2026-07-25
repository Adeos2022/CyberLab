import sys
import argparse
import subprocess


def whois_lookup(domain):
    """Run a whois lookup on a domain and return the raw output."""
    try:
        result = subprocess.run(
            ["whois", domain],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout
    except FileNotFoundError:
        print("The 'whois' command is not installed. Run: pkg install whois")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("Whois lookup timed out.")
        sys.exit(1)


def summarize(output):
    """Extract commonly useful fields from raw whois output, if present."""
    interesting_fields = [
        "Domain Name", "Registrar", "Creation Date", "Registry Expiry Date",
        "Updated Date", "Name Server", "Domain Status"
    ]
    lines = output.splitlines()
    summary = []
    for line in lines:
        for field in interesting_fields:
            if line.strip().lower().startswith(field.lower()):
                summary.append(line.strip())
                break
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perform a whois lookup on a domain."
    )
    parser.add_argument("domain", help="Domain to look up (e.g. example.com)")
    parser.add_argument("-f", "--full", action="store_true", help="Show full raw whois output instead of a summary")

    args = parser.parse_args()
    raw_output = whois_lookup(args.domain)

    if args.full:
        print(raw_output)
    else:
        summary = summarize(raw_output)
        if summary:
            print(f"\nWhois summary for {args.domain}:")
            print("-" * 50)
            for line in summary:
                print(f"  {line}")
        else:
            print("No summary fields found. Try running with -f for full output.")
