import socket


def fetch(url: str) -> str:
    if url.startswith("http://") is False:
        raise ValueError("url must start with `http://`")

    _tmp = url[7:].split("/", 1)
    if len(_tmp) > 1:
        host = _tmp[0]
        path = "/" + _tmp[1]
    else:
        host = _tmp[0]
        path = "/"

    sock = socket.socket()
    sock.connect((host, 80))

    request = "\r\n".join((f"GET {path} HTTP/1.0", f"Host: {host}", "\r\n"))
    sock.send(request.encode("ascii"))

    response = b""
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    sock.close()

    return response.decode()
