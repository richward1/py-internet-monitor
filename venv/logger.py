"""
Logger

Makes use of RotatingFileHandler to automatically rotate log files.
"""

import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = './logs/monitor.log'

file_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5 * 1024 * 1024, backupCount=2, encoding=None, delay=0)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)

app_log.addHandler(file_handler)

def log(message):
    app_log.info(message)       # Should implement different log levels (I.e. Warning)
