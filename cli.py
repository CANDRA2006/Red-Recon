import sys
import asyncio
from datetime import datetime

from core.recon import recon_target
from utils.writer import save_json, save_txt
from utils.banner import show_banner

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    show_banner()

    print(f"[INFO] Recon started for {domain}")

    results = asyncio.run(recon_target(domain))

    lines = []
    for r in results:
        cdn = r["http"]["cdn"]
        line = f"[+] {r['host']} -> {', '.join(r['ips'])} | CDN: {cdn}"
        print(line)
        lines.append(line)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_json(results, f"output/json/report_{ts}.json")
    save_txt(lines, f"output/txt/report_{ts}.txt")

    print("[DONE] Recon finished")

if __name__ == "__main__":
    main()
