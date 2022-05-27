import logging
from logger.CSVLogHandler import CSVLogHandler


def addLoggingLevel(levelName, levelNum):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    Refer to: https://stackoverflow.com/a/35804945/1691778

    """
    methodName = levelName.lower()

    if hasattr(logging, levelName):
       raise AttributeError('{} already defined in logging module'.format(levelName))
    if hasattr(logging, methodName):
       raise AttributeError('{} already defined in logging module'.format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
       raise AttributeError('{} already defined in logger class'.format(methodName))

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)
    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)


addLoggingLevel("METADATA", 200)
addLoggingLevel("START_FUNC", 198)
addLoggingLevel("END_FUNC", 199)

handlers = []

handlers.append(logging.StreamHandler())

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %I:%M:%S %p',
    handlers=handlers
)

logger = logging.getLogger('CSV Logger')
logger.setLevel(10)

ph = CSVLogHandler(5)
logger.addHandler(ph)
