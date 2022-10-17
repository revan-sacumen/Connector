"""This module send request API and get the response and stored into files."""
import json
import os.path
import sys

from sac_requests.context.request import Response

from src.confige import logger
from src.send_request import ApiRequest

sys.path.extend('./src')


# started here bank connectors
class Validators:
    """Initializing requirements url and params in constructor method."""

    def __init__(self, api_key: str) -> None:
        """Initiate instance variable in the constructor."""
        self.api_key = api_key
        self.send_request = ApiRequest(self.api_key)
        logger.info("Initialized required details.")

    def bank_details(self, path: str, query: str, param: str) -> Response:
        """Send a request to api and Get a response.

        Args:
            path (str): passing paths and params.
            query (str): search query
            param (str): requesting params.

        Returns:
            response: it returns json response
        """
        logger.info("Got it required parameters to getting bank details.and sending request.")
        response = self.send_request.send_request_config(path=path, query=query, param=param)
        logger.info("Bank Details response has been received")
        if response.status_code == 200:
            logger.info('Valid Bank details response has been received processing to storing into file.')
            file_path = 'data_files/banks_details.json'
            mode = 'a' if os.path.exists(file_path) else 'w'
            with open(file=file_path, mode=mode, encoding='utf-8') as data_file:
                data_file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                logger.info('Bank Details response data stored in file.')
        else:
            err_msg: int = response.status_code
            logger.error("Bank details response has been caught error code is:%d", err_msg)
        return response

    def banks_names(self, path: str, query: str, param: str) -> Response:
        """Get all bank names requesting BankAPi.

        Args:
            param ([str]): getting bank data through passing query params.
            path ([str]): this path variable is required if not passed error will through.
            query([str]): search query get expected response.
        Return:
            response(str): return getting response from api.
        """
        logger.info("Got it required attributes to getting bank names response.sending request.")
        response = self.send_request.send_request_config(path=path, query=query, param=param)
        logger.info("Bank Names response has been received")
        if response.status_code == 200:
            logger.info('Bank Names response has been received. and processing to storing into file.')
            filename = 'data_files/bank_names.json'
            mode = 'a' if os.path.exists(filename) else 'w'
            with open(file=filename, mode=mode, encoding="utf-8") as file:
                file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
            logger.info('Bank Names response data stored in file safely.')
        else:
            err_msg: int = response.status_code
            logger.error("Bank Names response has been caught error code is :%d", err_msg)
        return response

    def bank_iban_validation(self, path: str, query: str, param: str) -> Response:
        """Validate iban number and Getting valid response and saving in files.

        Args:
            path ([str]): this path variable is required for validating iban number.
            query ([str]): search query for required response
            param ([str]): destination url for getting bank api.
        """
        logger.info("Got it required attributes to getting bank names response.sending request.")
        response = self.send_request.send_request_config(path=path, query=query, param=param)
        logger.info("Bank iban validate response has been received")
        if response.status_code == 200:
            logger.info('Bank iban response has been received. and processing to storing into file.')
            file_dir_path = 'data_files/iban_validation.json'
            mode = 'a' if os.path.exists(file_dir_path) else 'w'
            data = json.loads(response.text)
            if data.get('valid') is True:
                with open(file=file_dir_path, mode=mode, encoding="utf-8") as file:
                    file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                logger.info('Bank iban response data stored in file safely.')
            else:
                logger.error('The given data was invalid.The iban number field is required')
        else:
            err_msg: int = response.status_code
            logger.error("Bank iban response has been caught error code is:%d", err_msg)
        return response

    def validation_bank_swift_code(self, path: str, query: str, param: str) -> Response:
        """Validate swift code and if its valid then storing into files.

        Args:
            query(str): pass swift code search query.
            param([str]): access_token for getting bank data.
            path([str]): this path variable is required for validating swift code.
        """
        logger.info("Got it required attributes to getting bank swift code response.sending request.")
        response = self.send_request.send_request_config(path=path, query=query, param=param)
        logger.info("Bank swift code validate response has been received")
        if response.status_code == 200:
            logger.info('Bank swift code response has been received. and processing to storing into file.')
            files = 'data_files/swift_code_valid.json'
            mode = 'a' if os.path.exists(files) else 'w'
            data = json.loads(response.text)
            if data.get('valid') is True:
                with open(file=files, mode=mode, encoding="utf-8") as file:
                    file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                logger.info('Bank swift code response data stored in file safely.')
            else:
                logger.error('The given data was invalid.The swift code field is required')
        else:
            err_msg: int = response.status_code
            logger.error("Bank iban response has been caught error code is:%d", err_msg)
        return response
