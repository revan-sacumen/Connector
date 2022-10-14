"""Write the test case for the API. Send a request model and get a response."""
import os

import pytest
from dotenv import load_dotenv

from src.send_request import ApiRequest

load_dotenv()
API_KEY = str(os.getenv("API_KEY"))
api_instance = ApiRequest(api_key=API_KEY)


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
    response_obj = api_instance.send_request_config(path=path, query=query, param=param)
    assert response_obj.status_code == 200
