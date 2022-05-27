import logging
import pandas as pd

class BaseDBLogHandler(logging.Handler):

    def __init__(self, flush_log_count=20):
        super().__init__()
        self.df = None
        self.log_messages = []
        self.counter = 0
        if flush_log_count is not None:
            self.flush_log_count = flush_log_count
        else:
            self.flush_log_count = 20

    def emit(self, record):
        print(record)
        msg = {
            "name": record.name,
            "level_no": record.levelno,
            "level_name": record.levelname,
            "file_name": record.filename,
            "line_no": record.lineno,
            "created_time": record.created,
            "message": record.msg,
        }
        self.log_messages.append(msg)
        self.counter = self.counter + 1
        if self.counter % self.flush_log_count == 0:
            self.flush()
