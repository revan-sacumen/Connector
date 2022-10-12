"""providing url paths and required parameters to validation module."""


def get_config_data():
    """All input params passing."""
    data = {
        "all_banks": {
            'path': 'all',
            'param': {
                'page': None,
                'per_page': 5
            }
        },
        "Banks_by_name": {
            'path': 'banks_by_country',
            'param': {
                'country_code': 'DE',
                'page': None,
            }
        },
        "iban_checks": {
            'path': 'iban_validate',
            'param': {
                'iban_number': 'GB33BUKB20201555555555',
            }
        },
        "swift_codes_checks": {
            'path': 'swift_check',
            'param': {
                'swift_code': 'AAMAADAD',
            }
        },
    }
    return data


def config_output_expected():
    """Expect output path and param."""
    output_config = {
        "all": {'path': 'all', 'param': {'page': None, 'per_page': 5}},
        "bank_names": {'path': 'banks_by_country', 'param': {'country_code': 'DE', 'page': None}},
        "iban_check": {'path': 'iban_validate',
                       'param': {'iban_number': 'GB33BUKB20201555555555'}},
        "swift_codes": {'path': 'swift_check', 'param': {'swift_code': 'AAMAADAD'}},
    }
    return output_config
