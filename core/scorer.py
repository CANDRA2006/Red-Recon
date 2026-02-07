def score_target(ports):
    score = len(ports)
    if 22 in ports:
        score += 2
    if score >= 5:
        return "HIGH"
    if score >= 3:
        return "MEDIUM"
    return "LOW"
