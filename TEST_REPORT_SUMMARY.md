# Test Execution Report

Generated: **2026-02-17 11:41:32**

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1117 |
| Passed | 1115 |
| Failed | 2 |
| Skipped | 0 |
| Pass Rate | 99.8% |

## Per‑File Results

### test_api_keys.py
- Passed: 28
- Failed: 0
- Skipped: 0

### test_chat_person_address_de_en.py
- Passed: 47
- Failed: 0
- Skipped: 0

### test_debug_address.py
- Passed: 1
- Failed: 0
- Skipped: 0

### test_entity_coverage.py
- Passed: 596
- Failed: 1
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

### test_person_address_de_en.py
- Passed: 66
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

### ❌ test_entity_coverage.py

#### ::test_entity_coverage::test_person_false_positives[Ich bin besch\xe4ftigt.]

**Original:**
```
(not found)
```

**Expected:**
```
(not found)
```

**Actual:**
```
(not found)
```

<details><summary>Full Failure Block</summary>

```
f = <PII_filter.pii_filter.PIIFilter object at 0x0000024C8E7EA090>
text = 'Ich bin beschäftigt.'

    @pytest.mark.parametrize("text", person_false_positive_samples)
    def test_person_false_positives(f, text):
        out = f.anonymize_text(text)
>       assert "<PERSON>" not in out, f"False positive PERSON detection in: {text}"
E       AssertionError: False positive PERSON detection in: Ich bin beschäftigt.
E       assert '<PERSON>' not in 'Ich bin <PERSON>.'
E         
E         '<PERSON>' is contained here:
E           Ich bin <PERSON>.

tests\unit\test_entity_coverage.py:632: AssertionError
```
</details>

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
self = <unit.test_tokens.TestOTPCode object at 0x0000020ECDBBF850>
filter_instance = <PII_filter.pii_filter.PIIFilter object at 0x0000020F2134B850>

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
>       assert "<OTP_CODE>" in result
E       AssertionError: assert '<OTP_CODE>' in 'one_time_<PASSWORD>'

tests\unit\test_tokens.py:123: AssertionError
```
</details>

