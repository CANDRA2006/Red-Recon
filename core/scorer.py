def score_target(ports):
    score = 0

    open_ports = [p for p, _ in ports]

    if 22 in open_ports:
        score += 2
    if 80 in open_ports or 443 in open_ports:
        score += 1
    if len(open_ports) >= 5:
        score += 2

    if score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    return "LOW"
