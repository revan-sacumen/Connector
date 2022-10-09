"""Here this module will each methods opertion will happen here."""
import logging
import os

from dotenv import load_dotenv  # type: ignore

import config_file as conf_file
from validation import Validators

load_dotenv()
URL = str(os.getenv("URL"))
API_KEY = str(os.getenv("API_KEY"))

# creating loggers name for saving loggs parents files
logger = logging.getLogger('validation_collectors')
logger.setLevel(logging.DEBUG)

# creating formmatters
formatters = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(process)d')

# all activity of collectors saving into logs
file_handler = logging.FileHandler('loggs/validation_collectors.log')
file_handler.setLevel(logging.DEBUG)

# erros in console level seted below
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# seting formatters to Handlers
file_handler.setFormatter(formatters)
console_handler.setFormatter(formatters)

# adding handler to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info('creating validators instance')
objs = Validators(url=URL, api_key=API_KEY)
logger.info('initlized and created instance')

logger.info("getting all bank details and performing to stor in file")
endpoints = conf_file.endpoints_all_banks
PATH = str(endpoints.get('path'))
PARAM = endpoints['params']['page']
objs.bank_details(path=PATH, param=PARAM)

logger.info("response stored in file")

logger.info("requesting all banks name")
endpoints = conf_file.endpoints_Banks_by_name
PATH = str(endpoints.get('path'))
PARAM = endpoints['params']['country_code']
objs.banks_names(path=PATH, param=PARAM)

logger.info('stored response into file')

logger.info("requsting and checking iban number validation")
endpoints = conf_file.endpoints_iban_checks
PATH = str(endpoints.get('path'))
PARAM = endpoints['params']['iban_number'][0]
objs.bank_iban_validation(path=PATH, param=PARAM)
logger.info("stored valid iban bank details into file")

logger.info("Checking swift code is valid or not ")
endpoints = conf_file.endpoints_swift_codes_checks
PATH = str(endpoints.get('path'))
PARAM = endpoints['params']['swift_code'][0]
objs.validation_bank_swift_code(path=PATH, param=PARAM)
logger.info("stored valid swift code bank details into file")

logger.info('appliction runing  successfully')
