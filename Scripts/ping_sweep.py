import sys
import socket
import argparse
import ipaddress

COMMON_PORTS = [22, 80, 443, 445, 3389]


def check_host(ip, ports, timeout=0.5):
    """Check if a host responds on any of the given ports. Returns True if alive."""
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((str(ip), port))
            sock.close()
            if result == 0:
                return True
        except socket.error:
            continue
    return False


def sweep(network, ports, timeout=0.5):
    """Sweep every host in a network range, checking for open common ports as a liveness signal."""
    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError as e:
        print(f"Invalid network: {e}")
        sys.exit(1)

    total = net.num_addresses - 2 if net.num_addresses > 2 else net.num_addresses
    print(f"\nSweeping {net} ({total} hosts) using TCP checks on ports {ports}...")
    print("-" * 50)

    alive = []
    for ip in net.hosts():
        if check_host(ip, ports, timeout):
            print(f"ALIVE: {ip}")
            alive.append(str(ip))

    print("-" * 50)
    print(f"Sweep complete. {len(alive)} host(s) responded out of {total} checked.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sweep a network range for live hosts using TCP connect checks "
                    "(works without root, unlike ICMP ping)."
    )
    parser.add_argument("network", help="Network in CIDR notation (e.g. 192.168.1.0/24)")
    parser.add_argument(
        "-p", "--ports",
        default=",".join(str(p) for p in COMMON_PORTS),
        help=f"Comma-separated ports to check (default: {','.join(str(p) for p in COMMON_PORTS)})"
    )
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Per-port timeout in seconds (default: 0.5)")

    args = parser.parse_args()
    ports = [int(p.strip()) for p in args.ports.split(",")]

    sweep(args.network, ports, args.timeout)
