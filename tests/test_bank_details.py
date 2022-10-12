"""Saving response form Validators module."""

import os
import sys

import pytest  # type: ignore
from dotenv import load_dotenv  # type: ignore

from src.validation import Validators  # type: ignore

sys.path.extend('./src')  # type: ignore

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("URL")
obj = Validators(API_URL, API_KEY)


# testing weather my function returning correct response
@pytest.mark.parametrize("path, param, expected",
                         {
                             ("all", 2, 200),
                             ('', '', 404)
                         })
def test_bank_details_response(path: str, param: str, expected: int):
    """Test bank details data getting status code."""
    result = obj.bank_details(path=path, param=param)
    assert result.status_code == expected


# Checking expected data was returning or not
@pytest.mark.parametrize("path, param, expected",
                         [
                             ("banks_by_country", "DE", 200),
                             ('banks_by_country', 'ABCD', 422),
                             ('', '', 404),
                         ])
def test_bank_names_response(path: str, param: str, expected: int):
    """Writing test case of bank names functions.

    Args:
        path (str): its give the path.
        param (str): params pass the function.
        expected (str): we are comparing weather actual param and expected param.
    """
    result_bank_names_obj = obj.banks_names(path=path, param=param)
    assert result_bank_names_obj.status_code == expected


@pytest.mark.parametrize("path, param, expected",
                         [
                             ("iban_validate", "GB33BUKB20201555555555", 200),
                             ('iban_validate', 'US64BACKUS6S3300958879', 422),
                             ('', 'US64SVBKUS6S3300958879', 404),

                         ])
def test_validations_of_iban_numbers(path: str, param: str, expected: int):
    """Testing validation function.

    Args:
        path (str): passing path for source.
        param (str): params to check given params return the correct obj.
        expected (Any): comparing actual response vs expected.
    """
    response_instance_obj = obj.bank_iban_validation(path=path, param=param)
    assert response_instance_obj.status_code == expected


@pytest.mark.parametrize("path, param, expected",
                         [
                             ("swift_check", "AAMAADAD", 200),
                             ('swift_check', 'MYNBGBQ65ZTS', 422),
                             ('', 'AAMAADAD', 404),

                         ])
def test_bank_swift_code_validations(path: str, param: str, expected: int):
    """Testing validation function.

    Args:
        path (str): passing path for source.
        param (str): params to check given params return the correct obj.
        expected (Any): comparing actual response vs expected.
    """
    response_validation_iban = obj.validation_bank_swift_code(path=path, param=param)

    assert response_validation_iban.status_code == expected
