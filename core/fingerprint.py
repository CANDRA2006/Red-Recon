def guess_service(port, banner):
    if port == 22:
        return "SSH"
    if port in [80, 443]:
        return "HTTP"
    if banner:
        return banner.split("\n")[0]
    return "UNKNOWN"
