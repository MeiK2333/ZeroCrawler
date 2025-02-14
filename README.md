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
>>> from ZeroCrawler import get
>>> resp = get('http://httpbin.org/get')
>>> resp
<Response [200]>
>>> resp.content
'{\n  "args": {}, \n  "headers": {\n    "Host": "httpbin.org"\n  }, \n  "origin": "36.110.78.251, 36.110.78.251", \n  "url": "https://httpbin.org/get"\n}\n'
>>> resp = get('http://httpbin.org/status/404')
>>> resp
<Response [404]>
```

## 测试

```shell script
$ python -m unittest tests/test_*.py
```
