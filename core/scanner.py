import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((host, port))
        banner = None
        try:
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            pass
        s.close()
        return port, banner
    except:
        return None

def scan_ports(host, ports, timeout, threads):
    results = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(scan_port, host, p, timeout)
            for p in ports
        ]

        for f in futures:
            res = f.result()
            if res:
                results.append(res)

    return results
