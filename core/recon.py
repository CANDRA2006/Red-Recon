import dns.resolver
import asyncio
import aiohttp

from core.scanner import probe_http
from core.cdn import detect_cdn

SUBDOMAINS = ["www", "mail", "test", "dev", "api", "beta", "m", "admin"]

resolver = dns.resolver.Resolver()

async def resolve_domain(domain):
    try:
        answers = resolver.resolve(domain, "A")
        return [ip.to_text() for ip in answers]
    except:
        return []

async def scan_host(session, host):
    ips = await resolve_domain(host)
    if not ips:
        return None

    http_info = await probe_http(session, host)

    cdn = "Unknown"
    if http_info and "headers" in http_info:
        cdn = detect_cdn(http_info["headers"])

    return {
        "host": host,
        "ips": ips,
        "http": {
            "url": http_info["url"] if http_info else None,
            "status": http_info["status"] if http_info else None,
            "cdn": cdn
        }
    }

async def recon_target(domain):
    results = []

    async with aiohttp.ClientSession() as session:
        tasks = []

        for sub in SUBDOMAINS:
            tasks.append(scan_host(session, f"{sub}.{domain}"))

        tasks.append(scan_host(session, domain))

        scanned = await asyncio.gather(*tasks)

        for r in scanned:
            if r:
                results.append(r)

    return results
