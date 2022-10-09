"""Saving response form Validators module."""

import os

from dotenv import load_dotenv  # type: ignore

from src.validation import Validators  # type: ignore

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("URL")

obj = Validators(API_URL, API_KEY)


def response_data_passing(path, param) -> bool:
    """We are checking weather my function is working properly or not so.

    path(str):its take the path  as input.
    param(str): its params we are providing parameter
    """
    response = obj.bank_details(path=path, param=param)
    true: bool = True
    false: bool = False
    if response.status_code == 200:
        return true
    else:
        return false


def bank_names_data(path: str, param: str) -> str:
    """Take a params and sending response.

    Args:
        path (str): required path for api.
        param (str): required param.

    Returns:
        str: returning response for test.
    """
    return obj.banks_names(path=path, param=param)


def iban_validation_data(path: str, param: str):
    """Send a Request to API and returning response.

    Args:
        path (str): wher we want validate the iban number that path we are taking.
        param (str): iban number as param.

    Returns:
        str: returning response further testing.
    """
    response_validtion_iban = obj.bank_iban_validation(path=path, param=param)
    if response_validtion_iban.status_code == 200:
        return True
    elif response_validtion_iban.status_code == 422:
        return "Invalid Iban Number"
    else:
        return 404


def swift_validation_data(path: str, param: str):
    """Bank swift validation requesting objects.

    Args:
        path (str): Taking path.
        param (str): passing swift code returning swift validate data.

    Returns:
        _type_: valid and invalid resopnse what we are getting from Api.
    """
    response_validtion_iban = obj.validation_bank_swift_code(path=path, param=param)
    if response_validtion_iban.status_code == 200:
        return True
    elif response_validtion_iban.status_code == 422:
        return "Invalid swift Number"
    else:
        return 404
