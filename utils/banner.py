def grab_banner(sock):
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        return sock.recv(1024).decode(errors="ignore").strip()
    except:
        return None
