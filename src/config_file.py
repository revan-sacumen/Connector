"""providing url paths and required parameters to validation module."""
from typing import Any, Dict

endpoints_all_banks: Dict[str, Any] = {
    'path': 'all',
    'param': {
        'page': None,
        'per_page': 5
    }
}
endpoints_Banks_by_name: Dict[str, Any] = {
    'path': 'banks_by_country',
    'param': {
        'country_code': 'DE',
        'page': None,
    }
}
endpoints_iban_checks: Dict[str, Any] = {
    'path': 'iban_validate',
    'param': {
        'iban_number': ['GB33BUKB20201555555555', 'US64SVBKUS6S3300958879']
    }
}

endpoints_swift_codes_checks: Dict[str, Any] = {
    'path': 'swift_check',
    'param': {
        'swift_code': ['AAMAADAD', 'MYNBGBQ65ZT']
    }
}
