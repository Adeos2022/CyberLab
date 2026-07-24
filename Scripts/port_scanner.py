import socket
import sys
import argparse
from datetime import datetime


def scan_port(target, port):
    """Attempt a TCP connection to check if a port is open. Returns True/False."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False


def run_scan(target, start_port, end_port):
    """Scan a range of ports on a target host and print/report open ones."""
    print(f"\nScanning target: {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 40)

    open_ports = []

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"Port {port}: OPEN")
            open_ports.append(port)

    print("-" * 40)
    print(f"Scan completed at: {datetime.now()}")
    print(f"Open ports found: {open_ports if open_ports else 'None'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple TCP port scanner for authorized security testing."
    )
    parser.add_argument("target", help="Target hostname or IP address")
    parser.add_argument("start_port", type=int, help="Start of port range")
    parser.add_argument("end_port", type=int, help="End of port range")

    args = parser.parse_args()

    if args.start_port < 1 or args.end_port > 65535:
        print("Ports must be between 1 and 65535.")
        sys.exit()

    if args.start_port > args.end_port:
        print("start_port must be less than or equal to end_port.")
        sys.exit()

    run_scan(args.target, args.start_port, args.end_port)
