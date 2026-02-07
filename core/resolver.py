import socket

CLOUDFLARE_IPS = (
    "104.16.", "104.17.", "104.18.", "104.19.",
    "172.64.", "172.67."
)

def detect_cdn(ip_list):
    for ip in ip_list:
        for cf in CLOUDFLARE_IPS:
            if ip.startswith(cf):
                return "Cloudflare"
    return "Unknown"

def resolve_domain(domain):
    try:
        _, _, ips = socket.gethostbyname_ex(domain)
        return {
            "target": domain,
            "ips": ips,
            "cdn": detect_cdn(ips)
        }
    except socket.gaierror:
        return {
            "target": domain,
            "ips": [],
            "cdn": "Unresolved"
        }
