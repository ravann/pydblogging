from logger.LogManager import logger
from test import test_log_from_test
import time

def test_log_funcl1():
    logger.info("From func 1")

logger.info("Test message")

test_log_funcl1()

test_log_from_test()

start_t = time.time()
logger.start_func("logging")

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

logger.end_func("logging")
end_t = time.time()
logger.metadata("Time Taken : " + str( (end_t - start_t) ))
logger.metadata("Table processed", extra = {'table_name' : 'MYTABLE', 'RECORDS' : '100'})
