# CyberLab

A personal cybersecurity learning lab built and organized while working through the ALX Cybersecurity program. Includes hands-on Python security tools, notes, and a structured environment for practicing offensive and defensive security concepts.

## Environment

Built and run entirely from Termux on Android, using:
- Python 3
- Debian (via proot-distro) for a fuller Linux toolset
- Nmap, DNS utilities, whois, and standard networking tools

## Structure

CyberLab/
- Notes/ - Study notes by topic (Linux, Networking, Crypto, etc.)
- Projects/ - Larger standalone projects
- Scripts/ - Python security tools (see below)
- Reports/ - Write-ups, findings, and generated scan reports
- Tools/ - Downloaded/installed security tools
- Wordlists/ - Wordlists for testing (subdomains, common paths)
- Labs/ - Lab exercise files
- Downloads/ - Misc downloads

## Scripts

All tools live in Scripts/ and use Python's argparse, so each supports --help.

### Reconnaissance
- port_scanner.py - TCP connect-scan for a target host over a port range
- dns_lookup.py - Forward and reverse DNS lookups (auto-detects domain vs. IP)
- banner_grabber.py - Connects to a port and grabs the service banner (e.g. SSH version)
- subdomain_enum.py - Enumerates subdomains of a target domain using a wordlist
- whois_lookup.py - Domain registration lookup (registrar, dates, nameservers)
- ping_sweep.py - TCP-based host discovery across a network range (no root required)
- dir_bruteforce.py - Brute-forces common directory/file paths on a website

### Web Security
- header_scanner.py - Checks HTTP response headers for common security misconfigurations
- cookie_inspector.py - Analyzes cookies for Secure, HttpOnly, and SameSite flags
- sqli_tester.py - Tests a URL parameter for basic SQL injection error signatures

### Forensics & Analysis
- log_parser.py - Parses auth logs for failed SSH login attempts, summarized by user and IP
- hash_calculator.py - Computes file or text hashes (MD5, SHA1, SHA256, SHA512)
- integrity_monitor.py - Baselines and detects changes to files in a directory (tamper detection)
- metadata_extractor.py - Extracts basic file info and EXIF metadata from images
- strings_extractor.py - Extracts printable strings from binary files

### Cryptography
- caesar_cipher.py - Encrypt, decrypt, or brute-force crack Caesar cipher text
- encoder_decoder.py - Base64 and Hex encoding/decoding
- file_encryptor.py - AES-256 file encryption/decryption with password-based key derivation

### Passwords
- password_checker.py - Evaluates password strength against common weak patterns

### Utility
- geolocate.py - IP geolocation lookup (country, city, ISP, coordinates)
- report_generator.py - Wraps tool output into a clean, timestamped report file

### Usage examples

python3 port_scanner.py scanme.nmap.org 20 100
python3 dns_lookup.py example.com
python3 header_scanner.py example.com
python3 cookie_inspector.py github.com
python3 log_parser.py sample.log
python3 hash_calculator.py text "hello world" -a sha256
python3 caesar_cipher.py encrypt "Attack at dawn" -s 5
python3 password_checker.py "Tr0ub4dor&3xample!"
python3 whois_lookup.py example.com
python3 subdomain_enum.py google.com Wordlists/subdomains.txt

## Disclaimer

These tools are for educational use and authorized security testing only. Only scan or test systems you own or have explicit permission to assess.

## Author

Deogracius Ayile - ALX Cybersecurity Program
