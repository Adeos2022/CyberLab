# CyberLab

A personal cybersecurity learning lab built and organized while working through the ALX Cybersecurity program. Includes hands-on Python security tools, notes, and a structured environment for practicing offensive and defensive security concepts.

## Environment

Built and run entirely from Termux on Android, using:
- Python 3
- Debian (via proot-distro) for a fuller Linux toolset
- Nmap, DNS utilities, and standard networking tools

## Structure

CyberLab/
- Notes/ - Study notes by topic (Linux, Networking, Crypto, etc.)
- Projects/ - Larger standalone projects
- Scripts/ - Python security tools (see below)
- Reports/ - Write-ups and findings
- Tools/ - Downloaded/installed security tools
- Wordlists/ - Wordlists for testing (e.g. subdomains.txt)
- Labs/ - Lab exercise files
- Downloads/ - Misc downloads

## Scripts

All tools live in Scripts/ and use Python's argparse, so each supports --help.

- port_scanner.py - TCP connect-scan for a target host over a port range
- dns_lookup.py - Forward and reverse DNS lookups (auto-detects domain vs. IP)
- log_parser.py - Parses auth logs for failed SSH login attempts, summarized by user and IP
- hash_calculator.py - Computes file or text hashes (MD5, SHA1, SHA256, SHA512)
- banner_grabber.py - Connects to a port and grabs the service banner (e.g. SSH version)
- header_scanner.py - Checks a website's HTTP response headers for common security misconfigurations
- password_checker.py - Evaluates password strength against common weak patterns and criteria
- subdomain_enum.py - Enumerates subdomains of a target domain using a wordlist

### Usage examples

python3 port_scanner.py scanme.nmap.org 20 100
python3 dns_lookup.py example.com
python3 log_parser.py sample.log
python3 hash_calculator.py text "hello world" -a sha256
python3 banner_grabber.py scanme.nmap.org 22
python3 header_scanner.py example.com
python3 password_checker.py "Tr0ub4dor&3xample!"
python3 subdomain_enum.py google.com Wordlists/subdomains.txt

## Disclaimer

These tools are for educational use and authorized security testing only. Only scan or test systems you own or have explicit permission to assess.

## Author

Deogracius Ayile - ALX Cybersecurity Program
