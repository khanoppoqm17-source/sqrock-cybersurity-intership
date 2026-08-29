import whois
import socket
import requests

def osint_scan(domain):
    print(f"\n=== OSINT Scan: {domain} ===\n")
    
    # WHOIS lookup
    try:
        w = whois.whois(domain)
        print(f"Registrar   : {w.registrar}")
        print(f"Created On  : {w.creation_date}")
        print(f"Expires On  : {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"[!] WHOIS failed: {e}")

    # DNS / IP resolution
    try:
        ip = socket.gethostbyname(domain)
        print(f"\nIP Address  : {ip}")
    except Exception as e:
        print(f"[!] DNS resolution failed: {e}")
        return

    # IP Geolocation
    try:
        geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        print(f"Location    : {geo.get('city')}, {geo.get('country')}")
        print(f"ISP         : {geo.get('isp')}")
    except Exception as e:
        print(f"[!] Geolocation failed: {e}")

if __name__ == "__main__":
    osint_scan("example.com")