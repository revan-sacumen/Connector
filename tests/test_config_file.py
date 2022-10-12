"""Config parameter and path testing."""
import sys

import pytest  # type: ignore

from src.config_file import config_output_expected  # type: ignore
from src.config_file import get_config_data

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
    data_dict = get_config_data()
    endpoints = data_dict.get(input_key)
    path = str(endpoints.get('path'))
    param = endpoints['param']
    config_iban_checks = config_output_expected()
    assert endpoints == config_iban_checks[expected_key]
    assert path == config_iban_checks[expected_key]['path']
    assert param == config_iban_checks[expected_key]['param']
