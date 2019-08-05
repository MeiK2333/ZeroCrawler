import json
import unittest

from ZeroCrawler import fetch
from ZeroCrawler.utils import get_body_by_response


class TestFetch(unittest.TestCase):
    def test_fetch(self):
        resp = fetch("get", "http://httpbin.org/get")
        self.assertTrue(resp.startswith("HTTP/1.1 200 OK"))

    def test_fetch_params(self):
        params = {"key1": "value1", "key2": "value2"}
        resp = fetch("get", "http://httpbin.org/get", params=params)
        data = get_body_by_response(resp)
        data = json.loads(data)
        args = data.get("args")
        for key, value in params.items():
            self.assertTrue(key in args.keys())
            self.assertEqual(value, args[key])

    def test_fetch_headers(self):
        headers = {"User-Agent": "ZeroCrawler"}
        resp = fetch("get", "http://httpbin.org/get", headers=headers)
        data = get_body_by_response(resp)
        data = json.loads(data)
        resp_headers = data.get("headers")
        for key, value in headers.items():
            self.assertTrue(key in resp_headers.keys())
            self.assertEqual(value, resp_headers[key])

    def test_fetch_method(self):
        methods = ["get", "post", "put", "delete", "patch"]
        for method in methods:
            resp = fetch(method, f"http://httpbin.org/{method}")
            data = get_body_by_response(resp)
            data = json.loads(data)
            url = data.get("url")
            self.assertTrue(url.endswith(f"httpbin.org/{method}"))

    def test_fetch_data(self):
        data = "Hello World!"
        resp = fetch("post", "http://httpbin.org/post", data=data)
        resp_data = get_body_by_response(resp)
        resp_data = json.loads(resp_data)
        self.assertEqual(resp_data["data"], data)


if __name__ == "__main__":
    unittest.main()
