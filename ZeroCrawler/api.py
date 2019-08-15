from typing import Dict

from . import sessions


def request(method: str, url: str, **kwargs):
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)


def get(url: str, params: Dict = None, **kwargs):
    return request("get", url, params=params, **kwargs)


def options(url: str, **kwargs):
    return request("options", url, **kwargs)


def head(url: str, **kwargs):
    return request("head", url, **kwargs)


def post(url: str, data: str = None, **kwargs):
    return request("post", url, data=data, **kwargs)


def put(url: str, data: Dict = None, **kwargs):
    return request("put", url, data=data, **kwargs)


def patch(url: str, data: Dict = None, **kwargs):
    return request("patch", url, data=data, **kwargs)


def delete(url: str, **kwargs):
    return request("delete", url, **kwargs)
