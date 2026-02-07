import socket

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None
