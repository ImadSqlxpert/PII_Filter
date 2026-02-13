# Test Execution Report

Generated: **2026-02-13 18:08:58**

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1004 |
| Passed | 1003 |
| Failed | 1 |
| Skipped | 0 |
| Pass Rate | 99.9% |

## Per‑File Results

### test_api_keys.py
- Passed: 28
- Failed: 0
- Skipped: 0

### test_debug_address.py
- Passed: 1
- Failed: 0
- Skipped: 0

### test_entity_coverage.py
- Passed: 597
- Failed: 0
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
- Passed: 30
- Failed: 0
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

## Failure Details

### ❌ test_tokens.py

#### ::TestOTPCode::test_one_time_password_format

**Original:**
```
one_time_<PASSWORD>
```

**Expected:**
```
<OTP_CODE>
```

**Actual:**
```
one_time_<PASSWORD>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_tokens.TestOTPCode object at 0x000001F361D49510>
filter_instance = <PII_filter.pii_filter.PIIFilter object at 0x000001F3015F9110>

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
>       assert "<OTP_CODE>" in result
E       AssertionError: assert '<OTP_CODE>' in 'one_time_<PASSWORD>'

tests\unit\test_tokens.py:123: AssertionError
```
</details>

