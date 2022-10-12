"""Testing main module."""
import os
import sys

from dotenv import load_dotenv  # type: ignore

from src.main import MainValidator  # type: ignore

sys.path.extend('./src')  # type: ignore

load_dotenv()

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("URL")
obj_main = MainValidator(API_URL, API_KEY)


def test_bank_details_response():
    """Test bank_detail functionality."""
    result = obj_main.send_request_bank_details()
    assert result.status_code == 200


def test_bank_names_response():
    """Writing test case of bank names functions."""
    result_bank_names_obj = obj_main.send_request_bank_name()
    assert result_bank_names_obj.status_code == 200


def test_validations_of_iban_numbers():
    """Testing validation function."""
    response_instance_obj = obj_main.send_request_bank_iban_number()
    assert response_instance_obj.status_code == 200


def test_bank_swift_code_validations():
    """Testing validation function status code true."""
    response_validation_iban = obj_main.send_request_bank_swift_code()
    assert response_validation_iban.status_code == 200
