# ZeroCrawler

从零开始写爬虫

## 安装

从 pypi 安装：

```shell script
$ pip install ZeroCrawler
```

源码安装：

```shell script
$ git clone git@github.com:MeiK2333/ZeroCrawler.git
$ cd ZeroCrawler/
$ pip install .
```

直接从 GitHub 安装：

```shell script
$ git install git+https://github.com/MeiK2333/ZeroCrawler.git
```

## 使用

```python
>>> from ZeroCrawler import fetch
>>> resp = fetch('get', 'http://httpbin.org/get')
>>> resp
'HTTP/1.1 200 OK\r\nAccess-Control-Allow-Credentials: true\r\nAccess-Control-Allow-Origin: *\r\nContent-Type: application/json\r\nDate: Tue, 30 Jul 2019 12:19:26 GMT\r\nReferrer-Policy: no-referrer-when-downgrade\r\nServer: nginx\r\nX-Content-Type-Options: nosniff\r\nX-Frame-Options: DENY\r\nX-XSS-Protection: 1; mode=block\r\nContent-Length: 146\r\nConnection: Close\r\n\r\n{\n  "args": {}, \n  "headers": {\n    "Host": "httpbin.org"\n  }, \n  "origin": "36.110.78.251, 36.110.78.251", \n  "url": "https://httpbin.org/get"\n}\n'
```

## 测试

```shell script
$ python -m unittest tests/test_*.py
```
