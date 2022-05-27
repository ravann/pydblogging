import logging
import pandas as pd
from utils.BaseDBLogger import BaseDBLogHandler

class CSVLogHandler(BaseDBLogHandler):

    def __init__(self, flush_log_count=None):
        super().__init__(flush_log_count)
        self.file_suffix = 1

    def flush(self):
        print("Flush called ... ")
        df = pd.DataFrame(self.log_messages)
        df.to_csv(f"logs_{self.file_suffix}.csv", index=False)
        self.counter = 0
        self.log_messages = []
        self.file_suffix = self.file_suffix + 1
