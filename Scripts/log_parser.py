import sys
import re
import argparse
from collections import Counter


def parse_failed_logins(filepath):
    """Scan a log file for failed SSH login attempts and count by user and IP."""
    pattern = r"Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+)"
    failed_users = Counter()
    failed_ips = Counter()

    try:
        with open(filepath, "r") as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    user, ip = match.groups()
                    failed_users[user] += 1
                    failed_ips[ip] += 1
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)
    except PermissionError:
        print(f"Permission denied reading: {filepath}")
        sys.exit(1)

    return failed_users, failed_ips


def print_report(failed_users, failed_ips):
    """Print a summary report of failed login attempts by user and by IP."""
    if not failed_users and not failed_ips:
        print("No failed login attempts found in this log.")
        return

    print("\n=== Failed Login Summary ===")
    print("\nTop offending usernames:")
    for user, count in failed_users.most_common():
        print(f"  {user}: {count} attempts")

    print("\nTop offending IPs:")
    for ip, count in failed_ips.most_common():
        print(f"  {ip}: {count} attempts")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse an auth log file and summarize failed SSH login attempts."
    )
    parser.add_argument("logfile", help="Path to the log file to parse")

    args = parser.parse_args()

    users, ips = parse_failed_logins(args.logfile)
    print_report(users, ips)
