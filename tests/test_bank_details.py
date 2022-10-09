"""Saving response form Validators module."""

import os
import sys
from typing import Any

import pytest  # type: ignore
from dotenv import load_dotenv  # type: ignore

from tests.response_data import bank_names_data  # type: ignore
from tests.response_data import (iban_validation_data, response_data_passing,
                                 swift_validation_data)

sys.path.extend('./tests')


load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("URL")


# testing weather my function returning correct response
@pytest.mark.parametrize("path, param, expected",
                         {
                             ("all", 2, True),
                             ('', '', False)
                         })
def test_bank_details_response(path, param, expected):
    """Test bank details data geting status code."""
    result = response_data_passing(path, param)
    assert result == expected


# Checking expected data was returning or not
@pytest.mark.parametrize("path, param, expected",
                         [
                             ("banks_by_country", "DE", 200),
                             ('banks_by_country', 'ABCD', 422),
                             ('banks_by_country', '', 422),
                         ])
def test_bank_names_response(path: str, param: str, expected: str):
    """Writing test case of bank names functions.

    Args:
        path (str): its give the path.
        param (str): params pass the function.
        expected (str): we are comparing weather actual param and expected param.
    """
    result_bank_names_obj = bank_names_data(path, param)
    assert result_bank_names_obj.status_code == expected

@pytest.mark.parametrize("path, param, expected",
                         [
                             ("iban_validate", "GB33BUKB20201555555555", True),
                             ('iban_validate', 'US64SVBKUS6S3300958879', "Invalid swift Number"),
                             ('', 'US64SVBKUS6S3300958879', 404),

                         ])
def test_validations_of_iban_numbers(path: str, param: str, expected: Any):
    """Testing validation function.

    Args:
        path (str): passing path for source.
        param (str): params to check given params return the correct obj.
        expected (Any): comparing actual response vs expected.
    """
    response_instance_obj = iban_validation_data(path, param)
    assert response_instance_obj == expected


@pytest.mark.parametrize("path, param, expected",
                         [
                             ("swift_check", "AAMAADAD", True),
                             ('swift_check', 'MYNBGBQ65ZTS', "Invalid swift Number"),
                             ('', 'AAMAADAD', 404),

                         ])
def test_bank_swift_code_validations(path: str, param: str, expected: Any):
    """Testing validation function.

    Args:
        path (str): passing path for source.
        param (str): params to check given params return the correct obj.
        expected (Any): comparing actul response vs expected.
    """
    response_instance_obj = swift_validation_data(path, param)
    assert response_instance_obj == expected
