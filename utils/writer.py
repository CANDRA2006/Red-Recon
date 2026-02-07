import json
import os
from datetime import datetime

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def save_json(data, filename):
    ensure_dir(filename)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def save_txt(data, filename):
    ensure_dir(filename)
    with open(filename, "w") as f:
        for item in data:
            f.write(f"Target: {item['target']}\n")
            f.write(f"IP: {item['ip']}\n")
            f.write(f"Open Ports:\n")
            for p in item["ports"]:
                f.write(f"  - {p['port']} ({p['service']})\n")
            f.write(f"Risk: {item['risk']}\n")
            f.write("-" * 40 + "\n")

def save_html(data, filename):
    ensure_dir(filename)

    html = f"""
    <html>
    <head>
        <title>Red-Recon Report</title>
        <style>
            body {{ font-family: Arial; background: #111; color: #eee; }}
            h1 {{ color: #ff5555; }}
            h2 {{ color: #50fa7b; }}
            .risk-HIGH {{ color: red; }}
            .risk-MEDIUM {{ color: orange; }}
            .risk-LOW {{ color: green; }}
        </style>
    </head>
    <body>
        <h1>Red-Recon Report</h1>
        <p>Generated at: {datetime.now()}</p>
    """

    for item in data:
        html += f"""
        <h2>{item['target']}</h2>
        <ul>
            <li>IP: {item['ip']}</li>
            <li>Ports:
                <ul>
        """

        for p in item["ports"]:
            html += f"<li>{p['port']} — {p['service']}</li>"

        html += f"""
                </ul>
            </li>
            <li class="risk-{item['risk']}">Risk: {item['risk']}</li>
        </ul>
        """

    html += "</body></html>"

    with open(filename, "w") as f:
        f.write(html)
