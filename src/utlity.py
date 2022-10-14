"""providing url paths and required parameters to validation module."""
# Required Path and Parameters.
PATH_QUERY = {"search_bank": None,
              "all_banks": {
                  'path': 'all',
                  'param': {
                      'page': None,
                      'per_page': 5
                  }
              },
              "search_country_code": "country_code",
              "Banks_by_name": {
                  'path': 'banks_by_country',
                  'param': {
                      'country_code': 'DE',
                      'page': None,
                  }
              },
              "search_iban_number": "iban_number",
              "iban_checks": {
                  'path': 'iban_validate',
                  'param': {
                      'iban_number': 'GB33BUKB20201555555555',
                  }
              },
              "search_swift_code": "swift_code",
              "swift_codes_checks": {
                  'path': 'swift_check',
                  'param': {
                      'swift_code': 'AAMAADAD',
                  }
              },
              }


EXPECTED_OUTPUT = {
    "search_bank": "",
    "all": {
        'path': 'all',
        'param': {
            'page': None,
            'per_page': 5
        }
    },
    "search_country_code": "country_code",
    "bank_names": {
        'path': 'banks_by_country',
        'param': {
            'country_code': 'DE',
            'page': None
        }
    },
    "search_iban_number": "iban_number",
    "iban_check": {
        'path': 'iban_validate',
        'param': {
            'iban_number': 'GB33BUKB20201555555555'
        }
    },
    "search_swift_code": "swift_code",
    "swift_codes": {
        'path': 'swift_check',
        'param': {
            'swift_code': 'AAMAADAD'
        }
    },
}
