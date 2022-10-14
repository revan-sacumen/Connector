"""Config parameter and path testing."""
import sys

import pytest  # type: ignore

from src.utlity import EXPECTED_OUTPUT, PATH_QUERY  # type: ignore

sys.path.extend('./src')  # type: ignore


@pytest.mark.parametrize("input_key, expected_key", [
    ("all_banks", "all"),
    ("Banks_by_name", "bank_names"),
    ("iban_checks", "iban_check"),
    ("swift_codes_checks", "swift_codes"),
])
def test_config_datas_bank_detail(input_key: str, expected_key: str):
    """Test config function.

    params:
        input_key(str): input param and path.
        expected_key(str): expected param and path.
    """
    data_dict = PATH_QUERY
    endpoints = data_dict.get(input_key)
    path = str(endpoints.get('path'))
    param = endpoints['param']
    expected_output = EXPECTED_OUTPUT
    assert endpoints == expected_output[expected_key]
    assert path == expected_output[expected_key]['path']
    assert param == expected_output[expected_key]['param']
