import logging
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.exceptions import APIException
from utils.response import APIResponse  # 假设APIResponse类已经封装在utils.response中
from django.db import DatabaseError
from django.http import Http404
from rest_framework import status
from utils.logger import Logger

# 获取日志记录器
logger = Logger()



# 自定义全局异常处理函数
def custom_exception_handler(exc, context):
    """
    exc: 异常实例
    context: 异常发生时的上下文（包含视图等信息）
    """
    # 调用 DRF 默认的异常处理方法
    response = drf_exception_handler(exc, context)

    # 捕获常见异常并处理
    if response is None:
        if isinstance(exc, Http404):
            logger.warning(f"404 Not Found: {context['view']}: {exc}")
            response_data = {'code': 404, 'message': 'Resource not found'}
            return APIResponse(**response_data, status=status.HTTP_404_NOT_FOUND)

        elif isinstance(exc, DatabaseError):
            logger.error(f"Database error: {exc}")
            response_data = {'code': 500, 'message': 'A database error occurred'}
            return APIResponse(**response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 捕获未知异常
        logger.error(f"Unhandled exception: {exc}")
        # 正确的返回方式
        response_data = {'code': 500, 'message': 'Internal server error'}
        return APIResponse(**response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 对于已知的 DRF 异常，可以进一步调整返回格式
    if response is not None:
        custom_data = {
            'code': response.status_code,
            'message': response.data.get('detail', 'An error occurred'),
        }
        response.data = custom_data

    return response
