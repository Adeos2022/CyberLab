import socket
import sys
import argparse


def grab_banner(target, port, timeout=2):
    """Connect to a port and attempt to read the service banner it sends."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target, port))
        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
        except socket.timeout:
            banner = ""
        sock.close()
        return banner if banner else "(no banner received)"
    except (socket.timeout, ConnectionRefusedError):
        return None
    except socket.gaierror:
        print(f"Could not resolve host: {target}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Connect to a port and grab the service banner, if any."
    )
    parser.add_argument("target", help="Target hostname or IP address")
    parser.add_argument("port", type=int, help="Port to connect to")
    parser.add_argument("-t", "--timeout", type=float, default=2, help="Connection timeout in seconds (default: 2)")

    args = parser.parse_args()

    result = grab_banner(args.target, args.port, args.timeout)
    if result is None:
        print(f"{args.target}:{args.port} - connection refused or timed out")
    else:
        print(f"{args.target}:{args.port} -> {result}")
