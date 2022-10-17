"""module response form Validators module."""
import os
import sys

import pytest  # type: ignore
from dotenv import load_dotenv  # type: ignore

from src.send_request import ApiRequest
from src.validation import Validators  # type: ignore

sys.path.extend('./src')  # type: ignore

load_dotenv()
API_KEY = str(os.getenv("API_KEY"))

obj = Validators(API_KEY)

api_instance = ApiRequest(api_key=API_KEY)


# testing weather my function returning correct response
@pytest.mark.parametrize("path, query, param, expected",
                         [
                             ("all", None, None, 200),
                             ("", "", "", 404),

                         ])
def test_bank_details(path: str, query: str, param: str, expected: str):
    """Test bank details data getting status code."""
    result = obj.bank_details(path=path, query=query, param=param)
    assert result.status_code == expected


# Checking expected data was returning or not
@pytest.mark.parametrize("path, query, param, expected",
                         [
                             ("banks_by_country", "country_code", "DE", 200),
                             ('banks_by_country', "country_code", 'ABCD', 400),
                             ('', "country_code", '', 404),
                         ])
def test_bank_names_response(path: str, query: str, param: str, expected: int):
    """Writing test case of bank names functions.

    Args:
        path (str): its give the path.
        param (str): params pass the function.
        expected (str): we are comparing weather actual param and expected param.
    """
    result_bank_names_obj = obj.banks_names(path=path, query=query, param=param)
    assert result_bank_names_obj.status_code == expected


@pytest.mark.parametrize("path, query, param, expected",
                         [
                             ("iban_validate", "iban_number", "GB33BUKB20201555555555", 200),
                             ('iban_validate', "iban_number", 'US64BACKUS6S3300958879', 400),
                             ('', "iban_number", 'US64SVBKUS6S3300958879', 404),

                         ])
def test_validations_of_iban_numbers(path: str, query: str, param: str, expected: int):
    """Testing validation function.

    Args:
        path (str): passing path for source.
        param (str): params to check given params return the correct obj.
        query (str): search query to get required data.
        expected (Any): comparing actual response vs expected.
    """
    response_instance_obj = obj.bank_iban_validation(path=path, query=query, param=param)
    assert response_instance_obj.status_code == expected


@pytest.mark.parametrize("path, query, param, expected",
                         [
                             ("swift_check", "swift_code", "AAMAADAD", 200),
                             ('swift_check', "swift_code", 'MYNBGBQ65ZTS', 400),
                             ('', "swift_code", 'AAMAADAD', 404),

                         ])
def test_bank_swift_code_validations(path: str, query: str, param: str, expected: int):
    """Testing validation function.

    Args:
        path (str): passing path for source.
        param (str): params to check given params return the correct obj.
        query (str): search query to get required response.
        expected (Any): comparing actual response vs expected.
    """
    response_validation_iban = obj.validation_bank_swift_code(path=path, query=query, param=param)
    assert response_validation_iban.status_code == expected


@pytest.mark.parametrize("path, query, param", [
    ["all", "", ""],
    ["banks_by_country", "country_code", "DE"],
    ["iban_validate", "iban_number", "GB33BUKB20201555555555"],
    ["swift_check", "swift_code", "AAMAADAD"]
])
def test_send_request(path: str, query: str, param: str):
    """Test function take required parameter and path.

    Args:
        path (str): provide path to required response getting.
        query (str): passing query parameter.
        param (str): passing params.
    """
    response_obj = api_instance.send_request_config(
        path=path, query=query, param=param)
    assert response_obj.status_code == 200
