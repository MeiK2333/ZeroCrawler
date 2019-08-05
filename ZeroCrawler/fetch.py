import socket


def fetch(
        method: str, url: str, params: dict = None, data: str = None, headers: dict = None
) -> str:
    if url.startswith("http://") is False:
        raise ValueError("url must start with `http://`")

    _tmp = url[7:].split("/", 1)
    if len(_tmp) > 1:
        host = _tmp[0]
        path = "/" + _tmp[1]
    else:
        host = _tmp[0]
        path = "/"

    method = method.upper()
    params = {} if params is None else params
    headers = {} if headers is None else headers

    params_str = "?" if params else ""
    param_count = 0
    for key, value in params.items():
        if param_count != 0:
            params_str += '&'
        params_str += f"{key}={value}"
        param_count += 1

    request_list = [f"{method} {path}{params_str} HTTP/1.0", f"Host: {host}"]
    for key, value in headers.items():
        request_list.append(f"{key}: {value}")

    if data is not None:
        request_list.append(f'Content-Length: {len(data)}')
        request_list.append('')  # 空行，以分割header域与data域
        request_list.append(data)
    request_list.append("\r\n")

    request = "\r\n".join(request_list)

    sock = socket.socket()
    sock.connect((host, 80))
    sock.send(request.encode("ascii"))

    response = b""
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    sock.close()

    return response.decode()
