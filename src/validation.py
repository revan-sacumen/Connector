"""This module send request API and get the response and stored into files."""
import json
import logging
import os.path
import sys

import requests

module_logger = logging.getLogger(__name__)

sys.path.extend('./src')


# started here bank connectors
class Validators:
    """Initializing requirements url and params in constructor method."""

    def __init__(self, url: str, api_key: str) -> None:
        """Initiate instance variable in the constructor."""
        self.url = url
        self.api_key = api_key
        self.logger = logging.getLogger("validation_collectors.validators")
        self.logger.info('requirements are initializing')

    def bank_details(self, path: str, param: str) -> requests.Response:
        """Send a request to api and Get a response.

        Args:
            path (str): passing paths and params.
            param (str): requesting params.

        Returns:
            response: it returns json response
        """
        self.logger.info('getting bank details from Bank API')
        response = None
        if param:
            urls = f'{self.url}/{path}?page={param}'
            headers = {
                'apikey': self.api_key,
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = requests.get(urls, headers=headers)
        else:
            urls = f'{self.url}/{path}'
            headers = {
                'apikey': self.api_key,
                'Content-Type': 'application/json; charset=utf-8'
            }
            response = requests.get(urls, headers=headers)
            file_path = './data_files/banks_details.json'
            mode = 'a' if os.path.exists(file_path) else 'w'
            with open(file=file_path, mode=mode, encoding='utf-8') as data_file:
                data_file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                self.logger.info('All Bank Data stored in file')
        return response

    def banks_names(self, path: str, param: str) -> requests.Response:
        """Get all bank names requesting BankAPi.

        Args:
            param ([str]): getting bank data through passing query params.
            path ([str]): this path variable is required if not passed error will through.
        Return:
            response(str): return getting response from api.
        """
        response = None
        if param is not None:
            urls = f'{self.url}/{path}?country_code={param}'
            headers = {
                'apikey': self.api_key,
                'Content-Type': "application/json; charset=utf-8"
            }
            response = requests.get(urls, headers=headers)
            if response.status_code != 429:
                with open(file='data_files/bank_names.json', mode='w', encoding="utf-8") as file:
                    file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
            else:
                self.logger.error("Daily request limit has been ended.")
        else:
            self.logger.info("parameter is empty bank_names")
        return response

    def bank_iban_validation(self, path: str, param: str) -> requests.Response:
        """Validate iban number and Getting valid response and saving in files.

        Args:
            url ([str]): destination url for getting bank api.
            api_key ([str]): access_token for getting bank data.
            paths ([str]): this path variable is required for validating iban number.
            @param param:
            @param path:
        """
        response = None
        if param is not None:
            urls = f'{self.url}/{path}?iban_number={param}'

            headers = {
                'apikey': self.api_key,
                'Content-Type': "application/json; charset=utf-8"
            }
            response = requests.get(urls, headers=headers)
            if response.status_code != 429:
                data = json.loads(response.text)
                if data.get('valid') is True:
                    with open(file='data_files/iban_validation.json', mode='w+', encoding="utf-8") as file:
                        file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                else:
                    self.logger.info('This Iban number is invalid')
            else:
                self.logger.error('The given data was invalid.The iban number field is required')
        return response

    def validation_bank_swift_code(self, path: str, param: str) -> requests.Response:
        """Validate swift code and if its valid then storing into files.

        Args:
            url([str]): destination url for getting bank api.
            api_key([str]): access_token for getting bank data.
            paths([str]): this path variable is required for validating swift code.
            @param param:
            @param path:
        """
        response = None
        if param is not None:
            urls = f'{self.url}/{path}?swift_code={param}'
            headers = {
                'apikey': self.api_key,
                'Content-Type': "application/json; charset=utf-8"
            }
            response = requests.get(urls, headers=headers)
            data = json.loads(response.text)
            files = 'data_files/swift_code_valid.json'
            if data.get('valid') is True:
                with open(file=files, mode='a', encoding="utf-8") as file:
                    file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
            else:
                self.logger.info('This swift code is invalid')
        else:
            self.logger.error('The given data was invalid.The swift code field is required')
        return response
