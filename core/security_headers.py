import aiohttp
import asyncio

SECURITY_HEADERS = {
    "Content-Security-Policy": "critical",
    "Strict-Transport-Security": "critical",
    "X-Frame-Options": "important",
    "X-Content-Type-Options": "important",
    "Referrer-Policy": "optional",
    "Permissions-Policy": "optional"
}

async def scan_headers(domain):
    url = f"https://{domain}"
    result = {
        "target": domain,
        "headers": {}
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                headers = response.headers

                for header, level in SECURITY_HEADERS.items():
                    if header in headers:
                        result["headers"][header] = {
                            "status": "present",
                            "value": headers.get(header),
                            "level": level
                        }
                    else:
                        result["headers"][header] = {
                            "status": "missing",
                            "value": None,
                            "level": level
                        }

    except Exception as e:
        result["error"] = str(e)

    return result
