"""collector validation."""
import logging
import os
import sys

from dotenv import load_dotenv
from sac_requests.context.request import Response

from src.utlity import PATH_QUERY
from src.validation import Validators

sys.path.extend('./src')  # type: ignore

load_dotenv()
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


class BankValidation:
    """Providing parameters and path and getting saved response."""

    def __init__(self, api_key):
        """Initialize of main Validators module."""
        self.path_query = PATH_QUERY
        self.vali_obj = Validators(api_key=api_key)

    def send_request_bank_details(self) -> Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("Providing required parameter to get all bank details.")
        bank_detail = PATH_QUERY
        query = bank_detail["search_bank"]
        path = bank_detail["all_banks"]["path"]
        param = bank_detail["all_banks"]["param"]['page']
        bank_method_response = self.vali_obj.bank_details(path=path, query=query, param=param)
        logger.info("Getting bank details response.")
        return bank_method_response

    def send_request_bank_name(self) -> Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("Passing the parameter to getting response.")
        # Bank name function.
        bank_name = PATH_QUERY
        path = bank_name["Banks_by_name"]["path"]
        query = bank_name["search_country_code"]
        param = bank_name["Banks_by_name"]["param"]["country_code"]
        bank_name_method_response = self.vali_obj.banks_names(path=path, query=query, param=param)
        logger.info("Parameter sent and response got")
        return bank_name_method_response

    def send_request_bank_iban_number(self):
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("Passing required parameter to validate iban number to getting response")
        # Iban function calling.
        iban_number = PATH_QUERY
        path = iban_number["iban_checks"]["path"]
        query = iban_number["search_iban_number"]
        param = iban_number["iban_checks"]["param"]["iban_number"]
        iban_method_response = self.vali_obj.bank_iban_validation(path=path, query=query, param=param)
        logger.info("Bank  Iban Response got.")
        return iban_method_response

    def send_request_bank_swift_code(self) -> Response:
        """Provide path and parameters function.

        return:
            response: returning response.
        """
        logger.info("sending params for getting to the bank validate swift code.")
        # Swift code validating response.
        swift_code = PATH_QUERY
        path = swift_code["swift_codes_checks"]["path"]
        query = swift_code["search_swift_code"]
        param = swift_code["swift_codes_checks"]["param"]["swift_code"]
        swift_method_response = self.vali_obj.validation_bank_swift_code(path=path, query=query, param=param)
        logger.info("Response has been got it")
        return swift_method_response


load_dotenv()
AUT_KEY = str(os.getenv("API_KEY"))
b_obj = BankValidation(api_key=AUT_KEY)
b_obj.send_request_bank_details()
b_obj.send_request_bank_name()
b_obj.send_request_bank_iban_number()
b_obj.send_request_bank_swift_code()
