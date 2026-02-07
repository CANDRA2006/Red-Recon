import argparse
from datetime import datetime
from config import settings
from utils.logger import setup_logger
from utils.writer import save_json, save_txt, save_html
from core.subdomain import enum_subdomains
from core.resolver import resolve_domain
from core.scanner import scan_ports
from core.fingerprint import guess_service
from core.scorer import score_target

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description="Red-Recon v1.0")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--json", action="store_true", help="Save JSON report")
    parser.add_argument("--txt", action="store_true", help="Save TXT report")
    parser.add_argument("--html", action="store_true", help="Save HTML report")
    args = parser.parse_args()

    logger.info(f"Recon started for {args.domain}")

    results = []
    subs = enum_subdomains(args.domain) or [args.domain]

    for sub in subs:
        ip = resolve_domain(sub)
        if not ip:
            continue

        logger.info(f"[+] {sub} -> {ip}")

        scanned = scan_ports(
            ip,
            settings.COMMON_PORTS,
            settings.DEFAULT_TIMEOUT,
            settings.THREADS
        )

        ports = []
        for port, banner in scanned:
            service = guess_service(port, banner)
            ports.append({"port": port, "service": service})

        risk = score_target(scanned)

        results.append({
            "target": sub,
            "ip": ip,
            "ports": ports,
            "risk": risk
        })

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    if args.json:
        save_json(results, f"output/json/report_{ts}.json")
    if args.txt:
        save_txt(results, f"output/txt/report_{ts}.txt")
    if args.html:
        save_html(results, f"output/html/report_{ts}.html")

    logger.info("Recon completed")

if __name__ == "__main__":
    main()
