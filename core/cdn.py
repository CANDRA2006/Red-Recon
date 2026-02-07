def detect_cdn(headers: dict) -> str:
    if not headers:
        return "Unknown"

    h = {k.lower(): v.lower() for k, v in headers.items()}

    if "cloudflare" in h.get("server", ""):
        return "Cloudflare"

    if "cf-ray" in h:
        return "Cloudflare"

    if "akamai" in h.get("server", ""):
        return "Akamai"

    if "x-akamai-transformed" in h:
        return "Akamai"

    if "fastly" in h.get("server", ""):
        return "Fastly"

    if "x-served-by" in h and "fastly" in h["x-served-by"]:
        return "Fastly"

    if "cloudfront" in h.get("via", ""):
        return "CloudFront"

    if "x-cache" in h and "cloudfront" in h["x-cache"]:
        return "CloudFront"

    return "No CDN / Unknown"
