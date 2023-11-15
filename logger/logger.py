# logger.py

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(user)s - %(message)s', datefmt='%H:%M:%S %m-%d-%Y')
log_filename = datetime.now().strftime('logs/fastapi.log')
server_log_handler = TimedRotatingFileHandler(log_filename, when='midnight', interval=1, backupCount=90, encoding='utf-8')
server_log_handler.setFormatter(log_formatter)
server_log_handler.setLevel(logging.INFO)
logger_init = logging.getLogger(__name__)
logger_init.setLevel(logging.INFO)
logger_init.addHandler(server_log_handler)