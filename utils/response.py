from rest_framework.response import Response

class APIResponse(Response):
    """
    封装统一的 API 响应格式
    """
    def __init__(self, data=None, code=0, message='success', status=None, headers=None, **kwargs):
        """
        :param data: 主要数据内容
        :param code: 自定义的状态码
        :param message: 提示信息
        :param status: HTTP 状态码
        :param headers: HTTP Headers
        :param kwargs: 其他扩展字段
        """
        # 构造返回数据的标准格式
        response_data = {}

        # 根据参数值是否存在，动态添加到返回数据中
        if code is not None:
            response_data['code'] = code
        if message:
            response_data['message'] = message
        if data is not None:
            response_data['data'] = data

        # 如果有其他字段，且值不为 None，添加到返回中
        for key, value in kwargs.items():
            if value is not None:
                response_data[key] = value

        # 调用父类的初始化方法
        super().__init__(response_data, status=status, headers=headers)
