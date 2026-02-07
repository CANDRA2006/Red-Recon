import requests

def enum_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subs = set()
    try:
        r = requests.get(url, timeout=10)
        for e in r.json():
            for s in e["name_value"].split():
                if "*" not in s:
                    subs.add(s.strip())
    except:
        pass
    return list(subs)
