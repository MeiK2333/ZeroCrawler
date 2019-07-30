import unittest

from ZeroCrawler import fetch


class TestFetch(unittest.TestCase):
    def test_fetch(self):
        resp = fetch('http://httpbin.org/get')
        self.assertTrue(resp.startswith('HTTP/1.1 200 OK'))


if __name__ == '__main__':
    unittest.main()
