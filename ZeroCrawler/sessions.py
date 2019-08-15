from typing import Dict

from .fetch import fetch
from .models import Request, Response


class Session(object):
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def request(
        self,
        method: str,
        url: str,
        params: Dict = None,
        data: str = None,
        headers: Dict = None,
    ) -> Response:
        req = Request(
            method=method.upper(), url=url, params=params, headers=headers, data=data
        )
        return self.send(req)

    def send(self, request: Request) -> Response:
        r = fetch(
            method=request.method,
            url=request.url,
            params=request.params,
            headers=request.headers,
            data=request.data,
        )
        resp = Response(request, r)
        return resp


def session():
    return Session()
