# ZeroCrawler

从零开始写爬虫

## Usage

```python
>>> from ZeroCrawler import fetch
>>> resp = fetch('http://httpbin.org/get')
>>> resp
'HTTP/1.1 200 OK\r\nAccess-Control-Allow-Credentials: true\r\nAccess-Control-Allow-Origin: *\r\nContent-Type: application/json\r\nDate: Tue, 30 Jul 2019 12:19:26 GMT\r\nReferrer-Policy: no-referrer-when-downgrade\r\nServer: nginx\r\nX-Content-Type-Options: nosniff\r\nX-Frame-Options: DENY\r\nX-XSS-Protection: 1; mode=block\r\nContent-Length: 146\r\nConnection: Close\r\n\r\n{\n  "args": {}, \n  "headers": {\n    "Host": "httpbin.org"\n  }, \n  "origin": "36.110.78.251, 36.110.78.251", \n  "url": "https://httpbin.org/get"\n}\n'
```

## Test

```shell script
$ python -m unittest tests/test_*.py
```
