import logging


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(__file__)

        # 封装日志记录函数
    def debug(self, message):
        """
        记录 DEBUG 级别的日志
        """
        self.logger.debug(message)

    def info(self, message):
        """
        记录 INFO 级别的日志
        """
        self.logger.info(message)

    def warning(self, message):
        """
        记录 WARNING 级别的日志
        """
        self.logger.warning(message)

    def error(self, message):
        """
        记录 ERROR 级别的日志
        """
        self.logger.error(message)

    def exception(self, exception):
        """
        记录 EXCEPTION 级别的日志
        """
        self.logger.exception(exception)
