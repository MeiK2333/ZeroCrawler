def get_body_by_response(response):
    """ 从返回的响应中获得数据正文 """
    return response.split('\r\n\r\n', 1)[1]
