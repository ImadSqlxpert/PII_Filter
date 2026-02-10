# Test Execution Report

**Generated**: 2026-02-10 21:33:27

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1004 |
| Passed | 992 |
| Failed | 12 |
| Skipped | 0 |
| Pass Rate | 98.8% |

## Per-File Results

### test_api_keys.py
- Passed: 21
- Failed: 7
- Skipped: 0

### test_debug_address.py
- Passed: 1
- Failed: 0
- Skipped: 0

### test_entity_coverage.py
- Passed: 594
- Failed: 3
- Skipped: 0

### test_false_positives.py
- Passed: 8
- Failed: 0
- Skipped: 0

### test_guards.py
- Passed: 12
- Failed: 0
- Skipped: 0

### test_ids_tax.py
- Passed: 29
- Failed: 1
- Skipped: 0

### test_overlap_resolution.py
- Passed: 13
- Failed: 0
- Skipped: 0

### test_person_logic.py
- Passed: 39
- Failed: 0
- Skipped: 0

### test_reference_identifiers.py
- Passed: 43
- Failed: 0
- Skipped: 0

### test_regex_patterns.py
- Passed: 191
- Failed: 0
- Skipped: 0

### test_tokens.py
- Passed: 29
- Failed: 1
- Skipped: 0

### test_validators.py
- Passed: 12
- Failed: 0
- Skipped: 0

## Failed Tests (12)

- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_google_api_key
- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_mailchimp_api_key
- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_azure_api_key
- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_openai_api_key
- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_firebase_api_key
- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_digitalocean_token
- **test_api_keys.py**: FAILED tests/unit/test_api_keys.py::TestAPIKeyDetection::test_api_key_in_url
- **test_entity_coverage.py**: FAILED tests/unit/test_entity_coverage.py::test_entity_coverage[VOTER_ID-Meine W\xe4hlerausweisnummer ist V9876543-<VOTER_ID>]
- **test_entity_coverage.py**: FAILED tests/unit/test_entity_coverage.py::test_entity_coverage[BENEFIT_ID-Meine Sozialhilfekarte ist B11223344-<BENEFIT_ID>]
- **test_entity_coverage.py**: FAILED tests/unit/test_entity_coverage.py::test_entity_coverage[MILITARY_ID-Meine Milit\xe4rausweis ist M55667788-<MILITARY_ID>]
- **test_ids_tax.py**: FAILED tests/unit/test_ids_tax.py::test_vat_tax_positive[RO VAT: RO12345678]
- **test_tokens.py**: FAILED tests/unit/test_tokens.py::TestOTPCode::test_one_time_password_format

