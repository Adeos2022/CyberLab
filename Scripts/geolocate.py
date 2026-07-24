import sys
import argparse
import requests


def geolocate_ip(ip):
    """Look up rough geolocation info for an IP address using a free public API."""
    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    if data.get("status") == "fail":
        print(f"Lookup failed: {data.get('message', 'unknown error')}")
        sys.exit(1)

    print(f"\nGeolocation for {ip}:")
    print("-" * 40)
    print(f"  Country:      {data.get('country')}")
    print(f"  Region:       {data.get('regionName')}")
    print(f"  City:         {data.get('city')}")
    print(f"  ISP:          {data.get('isp')}")
    print(f"  Organization: {data.get('org')}")
    print(f"  Latitude:     {data.get('lat')}")
    print(f"  Longitude:    {data.get('lon')}")
    print(f"  Timezone:     {data.get('timezone')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Look up rough geolocation info for an IP address."
    )
    parser.add_argument("ip", help="IP address to look up")

    args = parser.parse_args()
    geolocate_ip(args.ip)
