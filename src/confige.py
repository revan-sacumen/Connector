"""required configuration  content will  string here."""
import logging
import os.path

from sac_configurations.input.cfg import CFGConfig

# api for collecting data for validation
API_URL = "api.apilayer.com/bank_data"

cfg_config = CFGConfig()
filenames = ["/home/revanasidda/Desktop/Connector/config/loger.cfg"]
cfg_config.read(filenames)
config = cfg_config.to_dict()  # it converts configuration file to dictionary file.

# creating loggers name for saving logs parents files
log_config = config.get('logging')

logger = logging.getLogger(log_config.get('logger_name'))
logger.setLevel(log_config.get('log_level'))

# creating formatters
formatters = logging.Formatter(log_config.get('log_formatter'))

# all activity of collectors saving into logs
log_file_path = os.path.join(log_config.get('log_file_path'), log_config.get('log_filename'))
file_handler = logging.FileHandler(log_file_path)

# errors in console level set below
console_handler = logging.StreamHandler()
console_handler.setLevel(log_config.get('stream_log_level'))

# setting formatters to Handlers
file_handler.setFormatter(formatters)
console_handler.setFormatter(formatters)

# adding handler to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
