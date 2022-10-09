"""This module send request API and get the response and stored into files."""
import json
import logging

import requests

module_logger = logging.getLogger(__name__)


# started here bank connectors
class Validators:
    """Initializing requirements url and params in constructor method."""

    def __init__(self, url: str, api_key: str) -> None:
        """Initiate instance variable in the constructor."""
        self.url = url
        self.api_key = api_key
        self.logger = logging.getLogger("validation_collectors.validators")
        self.logger.info('requirements are initializing')

    def bank_details(self, path: str, param: str) -> None:
        """Send a request to api and Get a response.

        Args:
            url (str): this target or dat source and get data.
            api_key (str): this will be the access_token of the url or api.
            paths (str): passing paths and params.

        Returns:
            response: it returns json response
        """
        self.logger.info('getting bank details from Bank API')
        if param:
            urls = f'{self.url}/{path}?page={param}'
        else:
            urls = f'{self.url}/{path}'
        headers = {
            'apikey': self.api_key,
            'Content-Type': 'application/json; charset=utf-8'
        }
        response = requests.get(urls, headers=headers)
        try:
            with open(file='data_files/banks_details.json', mode="a", encoding='utf-8') as data_file:
                data_file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                self.logger.info('All Bank Data stored in file')
        except TypeError as msg:
            self.logger.error(msg)
        except KeyError as kmsg:
            self.logger.error(kmsg)
        return response  # type: ignore

    def banks_names(self, path: str, param: str) -> None:
        """Get all bank names requesting BankAPi.

        Args:
            url ([str]): destination url for getting bank api.
            api_key ([str]): access_token for getting bank data.
            paths ([str]): this path variable is required if not passed error will through.
        """
        if param is not None:
            urls = f'{self.url}/{path}?country_code={param}'
        else:
            self.logger.error("The given data was invalid.The country code field is required")
        headers = {
            'apikey': self.api_key,
            'Content-Type': "application/json; charset=utf-8"
        }
        response = requests.get(urls, headers=headers)
        try:
            with open(file='data_files/bank_names.json', mode='w', encoding="utf-8") as file:
                file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
        except TypeError as msg:
            self.logger.error(msg)
        except KeyError as kmsg:
            self.logger.error(kmsg)
        return response  # type: ignore

    def bank_iban_validation(self, path: str, param: str) -> None:
        """Validate iban number and Getting valid response and saving in files.

        Args:
            url ([str]): destination url for getting bank api.
            api_key ([str]): access_token for getting bank data.
            paths ([str]): this path variable is required for validating iban number.
            @param param:
            @param path:
        """
        if param is not None:
            urls = f'{self.url}/{path}?iban_number={param}'
        else:
            self.logger.error('The given data was invalid.The iban number field is required')
        headers = {
            'apikey': self.api_key,
            'Content-Type': "application/json; charset=utf-8"
        }
        response = requests.get(urls, headers=headers)
        data = json.loads(response.text)
        try:
            if data.get('valid') is True:
                try:
                    with open(file='data_files/iban_validation.json', mode='w+', encoding="utf-8") as file:
                        file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                except FileNotFoundError as msg:
                    self.logger.info(msg)
            else:
                self.logger.info('This Iban number is invalid')
        except TypeError as msg:
            self.logger.error(msg)
        except KeyError as kmsg:
            self.logger.error(kmsg)
        return response  # type: ignore

    def validation_bank_swift_code(self, path: str, param: str) -> None:
        """Validate swift code and if its valid then storing into files.

        Args:
            url([str]): destination url for getting bank api.
            api_key([str]): access_token for getting bank data.
            paths([str]): this path variable is required for validating swift code.
            @param param:
            @param path:
        """
        if param is not None:
            urls = f'{self.url}/{path}?swift_code={param}'
        else:
            self.logger.error('The given data was invalid.The swift code field is required')
        headers = {
            'apikey': self.api_key,
            'Content-Type': "application/json; charset=utf-8"
        }
        response = requests.get(urls, headers=headers)
        data = json.loads(response.text)
        files = 'data_files/swift_code_valid.json'
        try:
            if data.get('valid') is True:
                try:
                    with open(file=files, mode='a', encoding="utf-8") as file:
                        file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
                except TypeError as msg:
                    self.logger.info(msg)
            else:
                self.logger.info('This swift code is invalid')
        except TypeError as msg:
            self.logger.error(msg)
        except KeyError as kmsg:
            self.logger.error(kmsg)
        return response  # type: ignore
