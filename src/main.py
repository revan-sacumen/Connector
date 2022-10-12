"""Here this module will each method operation will happen here."""
import logging
import os
import sys

import requests
from dotenv import load_dotenv  # type: ignore

from src.config_file import get_config_data  # type: ignore
from src.validation import Validators  # type: ignore

sys.path.extend('./src')  # type: ignore


load_dotenv()
URL = str(os.getenv("URL"))
API_KEY = str(os.getenv("API_KEY"))

# creating loggers name for saving logs parents files
logger = logging.getLogger('validation_collectors')
logger.setLevel(logging.DEBUG)

# creating formatters
formatters = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(process)d')

# all activity of collectors saving into logs
file_handler = logging.FileHandler('./loggs/validation_collectors.log')
file_handler.setLevel(logging.DEBUG)

# errors in console level set below
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# setting formatters to Handlers
file_handler.setFormatter(formatters)
console_handler.setFormatter(formatters)

# adding handler to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class MainValidator:
    """Providing parameters and path and getting saved response."""

    def __init__(self, url, api_key):
        """Initialize of main Validators module."""
        self.vali_obj = Validators(url=url, api_key=api_key)

    def send_request_bank_details(self) -> requests.Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("getting all bank details and performing to stor in file")
        bank_detail = get_config_data()
        path = bank_detail["all_banks"]["path"]
        param = bank_detail["all_banks"]["param"]['page']
        bank_method_response = self.vali_obj.bank_details(path=path, param=param)
        logger.info("response stored in file")
        return bank_method_response

    def send_request_bank_name(self) -> requests.Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("requesting all banks name")
        # Bank name function calling.
        bank_name = get_config_data()
        path = bank_name["Banks_by_name"]["path"]
        param = bank_name["Banks_by_name"]["param"]["country_code"]
        bank_name_method_response = self.vali_obj.banks_names(path=path, param=param)
        logger.info('stored response into file')
        return bank_name_method_response

    def send_request_bank_iban_number(self) -> requests.Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("requesting and checking iban number validation")
        # Iban function calling.
        iban_number = get_config_data()
        path = iban_number["iban_checks"]["path"]
        param = iban_number["iban_checks"]["param"]["iban_number"]
        iban_method_response = self.vali_obj.bank_iban_validation(path=path, param=param)
        logger.info("stored valid iban bank details into file")
        return iban_method_response

    def send_request_bank_swift_code(self) -> requests.Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("Checking swift code is valid or not ")
        # Swift code validate function.
        swift_code = get_config_data()
        path = swift_code["swift_codes_checks"]["path"]
        param = swift_code["swift_codes_checks"]["param"]["swift_code"]
        swift_method_response = self.vali_obj.validation_bank_swift_code(path=path, param=param)
        logger.info("stored valid swift code bank details into file")
        return swift_method_response


load_dotenv()
URL = str(os.getenv("URL"))
API_KEY = str(os.getenv("API_KEY"))
MainValidator(url=URL, api_key=API_KEY)
