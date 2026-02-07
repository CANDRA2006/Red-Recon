def guess_service(port):
    if port == 22:
        return "OpenSSH"
    if port in [80, 443]:
        return "Apache"
    if port == 3306:
        return "MySQL"
    return "Unknown"
