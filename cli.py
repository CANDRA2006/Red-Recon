import sys
import asyncio
from datetime import datetime

from utils.banner import show_banner
from utils.writer import save_json, save_txt
from core.resolver import resolve_domain
from core.security_headers import scan_headers

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    show_banner()
    print(f"[INFO] Recon started for {domain}")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    results = []

    targets = [domain, f"www.{domain}"]

    for t in targets:
        data = resolve_domain(t)
        if data["ips"]:
            print(f"[+] {t} -> {', '.join(data['ips'])} | CDN: {data['cdn']}")
        results.append(data)

    print("[INFO] Scanning security headers...")

    header_results = asyncio.run(scan_headers(domain))

    save_json(
        {
            "recon": results,
            "security_headers": header_results
        },
        f"output/json/report_{ts}.json"
    )

    save_txt(results, f"output/txt/report_{ts}.txt")

    print("[INFO] Security header scan completed")
    print("[INFO] Recon finished")

if __name__ == "__main__":
    main()
