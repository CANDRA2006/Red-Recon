import json
import os

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def save_json(data, filename):
    ensure_dir(filename)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_txt(results, filename):
    ensure_dir(filename)
    with open(filename, "w", encoding="utf-8") as f:
        for item in results:
            f.write(f"Target : {item['target']}\n")
            f.write(f"IPs    : {', '.join(item['ips']) if item['ips'] else 'None'}\n")
            f.write(f"CDN    : {item['cdn']}\n")
            f.write("-" * 40 + "\n")
