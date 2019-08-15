from typing import Dict


class Request(object):
    def __init__(
        self,
        method: str = None,
        url: str = None,
        headers: Dict = None,
        data: str = None,
        params: Dict = None,
    ):
        data = "" if data is None else data
        headers = {} if headers is None else headers
        params = {} if params is None else params

        self.method = method
        self.url = url
        self.headers = headers
        self.data = data
        self.params = params

    def __repr__(self):
        return f"<Request [{self.method}]>"


class Response(object):
    def __init__(self, request, raw_content):
        self._raw_content = raw_content
        self._headers = {}
        self._content = None
        self._status_code = None
        self._request = request

        self.parse()

    @property
    def headers(self) -> Dict:
        return self._headers

    @property
    def raw_content(self) -> str:
        return self._raw_content

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def request(self) -> Request:
        return self._request

    @property
    def content(self) -> str:
        return self._content

    def __repr__(self):
        return f"<Response [{self.status_code}]>"

    def parse(self):
        f, t = self.raw_content.split("\r\n", 1)
        # 获取状态码
        self._status_code = int(f.split()[1])
        t, b = t.split("\r\n\r\n", 1)
        # 获取 headers
        for i in t.split("\r\n"):
            k, v = i.split(":", 1)
            self._headers[k.strip()] = v.strip()

        # 获取正文
        self._content = b
