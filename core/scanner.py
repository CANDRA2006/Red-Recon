import aiohttp

async def probe_http(session, host):
    urls = [f"https://{host}", f"http://{host}"]

    for url in urls:
        try:
            async with session.get(url, timeout=5) as resp:
                return {
                    "url": url,
                    "status": resp.status,
                    "headers": dict(resp.headers)
                }
        except:
            continue

    return None
