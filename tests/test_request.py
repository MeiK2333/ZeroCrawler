import unittest
import json
from ZeroCrawler import get, post


class TestFetch(unittest.TestCase):
    def test_get(self):
        req = get("http://httpbin.org/get")
        self.assertEqual(req.status_code, 200)

    def test_params(self):
        req = get("http://httpbin.org/get", params={"key": "value"})
        data = json.loads(req.content)
        self.assertTrue("key" in data["args"].keys())
        self.assertTrue("value" in data["args"].values())

    def test_post(self):
        req = post("http://httpbin.org/post", data="Hello World!")
        self.assertEqual("Hello World!", json.loads(req.content)["data"])

    def test_status_code(self):
        req = get("http://httpbin.org/status/200")
        self.assertEqual(req.status_code, 200)

        req = get("http://httpbin.org/status/404")
        self.assertEqual(req.status_code, 404)

        req = get("http://httpbin.org/status/500")
        self.assertEqual(req.status_code, 500)


if __name__ == "__main__":
    unittest.main()
