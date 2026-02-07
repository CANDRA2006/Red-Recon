import requests

def enum_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = set()

    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return []

        for entry in r.json():
            name = entry.get("name_value")
            if name:
                for sub in name.split("\n"):
                    if "*" not in sub:
                        subdomains.add(sub.strip())
    except Exception:
        pass

    return list(subdomains)
