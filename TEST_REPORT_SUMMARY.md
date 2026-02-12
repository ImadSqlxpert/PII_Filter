# Test Execution Report

Generated: **2026-02-12 14:05:30**

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1004 |
| Passed | 972 |
| Failed | 32 |
| Skipped | 0 |
| Pass Rate | 96.8% |

## Per‑File Results

### test_api_keys.py
- Passed: 21
- Failed: 7
- Skipped: 0

### test_debug_address.py
- Passed: 1
- Failed: 0
- Skipped: 0

### test_entity_coverage.py
- Passed: 573
- Failed: 24
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

### ❌ test_api_keys.py

#### ::TestAPIKeyDetection::test_google_api_key

**Original:**
```
google_api_key=AIzaSyDummyKeyForTestingPurposesOnly123456
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
google_api_key=AIzaSyDummyKeyForTestingPurposesOnly123456
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A24190>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217B6868110>

    def test_google_api_key(self, filter_instance):
        """Test Google API Key detection."""
        text = "google_api_key=AIzaSyDummyKeyForTestingPurposesOnly123456"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'google_api_key=AIzaSyDummyKeyForTestingPurposesOnly123456'

tests\unit\test_api_keys.py:94: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_mailchimp_api_key

**Original:**
```
mailchimp_api_key=MAILCHIMP_KEY_REDACTED
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
mailchimp_api_key=MAILCHIMP_KEY_REDACTED
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A250D0>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217CD263890>

    def test_mailchimp_api_key(self, filter_instance):
        """Test Mailchimp API Key detection."""
        text = "mailchimp_api_key=MAILCHIMP_KEY_REDACTED"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'mailchimp_api_key=MAILCHIMP_KEY_REDACTED'

tests\unit\test_api_keys.py:108: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_azure_api_key

**Original:**
```
azure_api_key=<ID_NUMBER>-<PHONE>-<MAC_ADDRESS>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
azure_api_key=<ID_NUMBER>-<PHONE>-<MAC_ADDRESS>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A25FD0>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217C6D38310>

    def test_azure_api_key(self, filter_instance):
        """Test Azure API Key detection."""
        text = "azure_api_key=12345678-1234-1234-1234-123456789012"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'azure_api_key=<ID_NUMBER>-<PHONE>-<MAC_ADDRESS>'

tests\unit\test_api_keys.py:122: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_openai_api_key

**Original:**
```
openai_api_key=sk-proj-1234567890abcdefghijklmnop
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
openai_api_key=sk-proj-1234567890abcdefghijklmnop
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A26750>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217B738F250>

    def test_openai_api_key(self, filter_instance):
        """Test OpenAI API Key detection."""
        text = "openai_api_key=sk-proj-1234567890abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'openai_api_key=sk-proj-1234567890abcdefghijklmnop'

tests\unit\test_api_keys.py:129: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_firebase_api_key

**Original:**
```
firebase_api_key=AIzaSyDummyFirebaseKeyForTestingOnly1234567
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
firebase_api_key=AIzaSyDummyFirebaseKeyForTestingOnly1234567
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A26ED0>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217E41E3C90>

    def test_firebase_api_key(self, filter_instance):
        """Test Firebase API Key detection."""
        text = "firebase_api_key=AIzaSyDummyFirebaseKeyForTestingOnly1234567"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'firebase_api_key=AIzaSyDummyFirebaseKeyForTestingOnly1234567'

tests\unit\test_api_keys.py:136: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_digitalocean_token

**Original:**
```
digitalocean_api_key=dop_v1_1234567890abcdefghijklmnopqrst
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
digitalocean_api_key=dop_v1_1234567890abcdefghijklmnopqrst
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A30590>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217C5677610>

    def test_digitalocean_token(self, filter_instance):
        """Test DigitalOcean API Token detection."""
        text = "digitalocean_api_key=dop_v1_1234567890abcdefghijklmnopqrst"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'digitalocean_api_key=dop_v1_1234567890abcdefghijklmnopqrst'

tests\unit\test_api_keys.py:157: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_api_key_in_url

**Original:**
```
https://api.example.com?api_key=sk_test_1234567890abcdefghijklmnop
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
https://api.example.com?api_key=sk_test_1234567890abcdefghijklmnop
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x00000217B2A31290>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000217B58C5A90>

    def test_api_key_in_url(self, filter_instance):
        """Test API key detection in URLs."""
        text = "https://api.example.com?api_key=sk_test_1234567890abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'https://api.example.com?api_key=sk_test_1234567890abcdefghijklmnop'

tests\unit\test_api_keys.py:198: AssertionError
```
</details>

### ❌ test_entity_coverage.py

#### ::test_entity_coverage::test_entity_coverage[PASSPORT-EU Passport: X1Y2Z3A4B-<ID_NUMBER>]

**Original:**
```
EU Passport: <PASSPORT>
```

**Expected:**
```
<ID_NUMBER>
```

**Actual:**
```
EU Passport: <PASSPORT>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B22A354C10>
entity = 'PASSPORT', text = 'EU Passport: X1Y2Z3A4B', expected = '<ID_NUMBER>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect PASSPORT in: EU Passport: X1Y2Z3A4B
E       assert '<ID_NUMBER>' in 'EU Passport: <PASSPORT>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[DATE-I was born on March 15, 1985-<DATE>]

**Original:**
```
I was born on March 15, 1985
```

**Expected:**
```
<DATE>
```

**Actual:**
```
I was born on March 15, 1985
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20A14B750>
entity = 'DATE', text = 'I was born on March 15, 1985', expected = '<DATE>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect DATE in: I was born on March 15, 1985
E       assert '<DATE>' in 'I was born on March 15, 1985'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[ID_NUMBER-My social security number is 123-45-6789-<ID_NUMBER>]

**Original:**
```
My social security number is 123-45-6789
```

**Expected:**
```
<ID_NUMBER>
```

**Actual:**
```
My social security number is 123-45-6789
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B24484D090>
entity = 'ID_NUMBER', text = 'My social security number is 123-45-6789'
expected = '<ID_NUMBER>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect ID_NUMBER in: My social security number is 123-45-6789
E       assert '<ID_NUMBER>' in 'My social security number is 123-45-6789'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[PAYMENT_TOKEN-My API key is sk_live_abc123def456-<PAYMENT_TOKEN>]

**Original:**
```
My API key is sk_live_abc123def456
```

**Expected:**
```
<PAYMENT_TOKEN>
```

**Actual:**
```
My API key is sk_live_abc123def456
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20E29A550>
entity = 'PAYMENT_TOKEN', text = 'My API key is sk_live_abc123def456'
expected = '<PAYMENT_TOKEN>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect PAYMENT_TOKEN in: My API key is sk_live_abc123def456
E       assert '<PAYMENT_TOKEN>' in 'My API key is sk_live_abc123def456'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[MRN-My medical record number is ABC-123456-<MRN>]

**Original:**
```
My medical record number is ABC-123456
```

**Expected:**
```
<MRN>
```

**Actual:**
```
My medical record number is ABC-123456
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20C47F790>
entity = 'MRN', text = 'My medical record number is ABC-123456'
expected = '<MRN>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect MRN in: My medical record number is ABC-123456
E       assert '<MRN>' in 'My medical record number is ABC-123456'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[INSURANCE_ID-My insurance policy is POL-987654321-<INSURANCE_ID>]

**Original:**
```
My <PASSPORT> policy is POL-<ID_NUMBER>
```

**Expected:**
```
<INSURANCE_ID>
```

**Actual:**
```
My <PASSPORT> policy is POL-<ID_NUMBER>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20A206490>
entity = 'INSURANCE_ID', text = 'My insurance policy is POL-987654321'
expected = '<INSURANCE_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect INSURANCE_ID in: My insurance policy is POL-987654321
E       assert '<INSURANCE_ID>' in 'My <PASSPORT> policy is POL-<ID_NUMBER>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[STUDENT_NUMBER-My student ID is STU-12345-<STUDENT_NUMBER>]

**Original:**
```
My student ID is <ADDRESS>
```

**Expected:**
```
<STUDENT_NUMBER>
```

**Actual:**
```
My student ID is <ADDRESS>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B22A8A9910>
entity = 'STUDENT_NUMBER', text = 'My student ID is STU-12345'
expected = '<STUDENT_NUMBER>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect STUDENT_NUMBER in: My student ID is STU-12345
E       assert '<STUDENT_NUMBER>' in 'My student ID is <ADDRESS>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[EMPLOYEE_ID-My employee number is EMP-67890-<EMPLOYEE_ID>]

**Original:**
```
My employee number is EMP-67890
```

**Expected:**
```
<EMPLOYEE_ID>
```

**Actual:**
```
My employee number is EMP-67890
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20BC8C9D0>
entity = 'EMPLOYEE_ID', text = 'My employee number is EMP-67890'
expected = '<EMPLOYEE_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect EMPLOYEE_ID in: My employee number is EMP-67890
E       assert '<EMPLOYEE_ID>' in 'My employee number is EMP-67890'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[PRO_LICENSE-My professional license is LIC-54321-<PRO_LICENSE>]

**Original:**
```
My professional license is LIC-54321
```

**Expected:**
```
<PRO_LICENSE>
```

**Actual:**
```
My professional license is LIC-54321
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20A0AB550>
entity = 'PRO_LICENSE', text = 'My professional license is LIC-54321'
expected = '<PRO_LICENSE>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect PRO_LICENSE in: My professional license is LIC-54321
E       assert '<PRO_LICENSE>' in 'My professional license is LIC-54321'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[HEALTH_ID-My NHS number is 943 476 5919-<HEALTH_ID>]

**Original:**
```
My NHS number is <PHONE>
```

**Expected:**
```
<HEALTH_ID>
```

**Actual:**
```
My NHS number is <PHONE>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B237DFBE50>
entity = 'HEALTH_ID', text = 'My NHS number is 943 476 5919'
expected = '<HEALTH_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect HEALTH_ID in: My NHS number is 943 476 5919
E       assert '<HEALTH_ID>' in 'My NHS number is <PHONE>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[DEVICE_ID-My device ID is DEV-999888777-<DEVICE_ID>]

**Original:**
```
My device ID is DEV-<ID_NUMBER>
```

**Expected:**
```
<DEVICE_ID>
```

**Actual:**
```
My device ID is DEV-<ID_NUMBER>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B2454717D0>
entity = 'DEVICE_ID', text = 'My device ID is DEV-999888777'
expected = '<DEVICE_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect DEVICE_ID in: My device ID is DEV-999888777
E       assert '<DEVICE_ID>' in 'My device ID is DEV-<ID_NUMBER>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[DATE-Ich bin am 15. M\xe4rz 1985 geboren-<DATE>]

**Original:**
```
Ich bin am 15. März<LOCATION>
```

**Expected:**
```
<DATE>
```

**Actual:**
```
Ich bin am 15. März<LOCATION>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20A09CBD0>
entity = 'DATE', text = 'Ich bin am 15. März 1985 geboren', expected = '<DATE>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect DATE in: Ich bin am 15. März 1985 geboren
E       assert '<DATE>' in 'Ich bin am 15. März<LOCATION>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[ID_NUMBER-Meine Sozialversicherungsnummer ist 123-45-6789-<ID_NUMBER>]

**Original:**
```
Meine Sozialversicherungsnummer ist <PHONE>
```

**Expected:**
```
<ID_NUMBER>
```

**Actual:**
```
Meine Sozialversicherungsnummer ist <PHONE>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B22F9C91D0>
entity = 'ID_NUMBER', text = 'Meine Sozialversicherungsnummer ist 123-45-6789'
expected = '<ID_NUMBER>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect ID_NUMBER in: Meine Sozialversicherungsnummer ist 123-45-6789
E       assert '<ID_NUMBER>' in 'Meine Sozialversicherungsnummer ist <PHONE>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[PAYMENT_TOKEN-Mein API-Schl\xfcssel ist sk_live_abc123def456-<PAYMENT_TOKEN>]

**Original:**
```
Mein API-Schlüssel ist sk_live_abc123def456
```

**Expected:**
```
<PAYMENT_TOKEN>
```

**Actual:**
```
Mein API-Schlüssel ist sk_live_abc123def456
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B22FB8F7D0>
entity = 'PAYMENT_TOKEN', text = 'Mein API-Schlüssel ist sk_live_abc123def456'
expected = '<PAYMENT_TOKEN>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect PAYMENT_TOKEN in: Mein API-Schlüssel ist sk_live_abc123def456
E       assert '<PAYMENT_TOKEN>' in 'Mein API-Schlüssel ist sk_live_abc123def456'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[MRN-Meine Krankenaktennummer ist ABC-123456-<MRN>]

**Original:**
```
Meine Krankenaktennummer ist ABC-123456
```

**Expected:**
```
<MRN>
```

**Actual:**
```
Meine Krankenaktennummer ist ABC-123456
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B21AC2FD10>
entity = 'MRN', text = 'Meine Krankenaktennummer ist ABC-123456'
expected = '<MRN>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect MRN in: Meine Krankenaktennummer ist ABC-123456
E       assert '<MRN>' in 'Meine Krankenaktennummer ist ABC-123456'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[INSURANCE_ID-Meine Versicherungspolice ist POL-987654321-<INSURANCE_ID>]

**Original:**
```
Meine Versicherungspolice ist POL-<ID_NUMBER>
```

**Expected:**
```
<INSURANCE_ID>
```

**Actual:**
```
Meine Versicherungspolice ist POL-<ID_NUMBER>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B218BA7290>
entity = 'INSURANCE_ID', text = 'Meine Versicherungspolice ist POL-987654321'
expected = '<INSURANCE_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect INSURANCE_ID in: Meine Versicherungspolice ist POL-987654321
E       assert '<INSURANCE_ID>' in 'Meine Versicherungspolice ist POL-<ID_NUMBER>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[STUDENT_NUMBER-Meine Studentenausweisnummer ist STU-12345-<STUDENT_NUMBER>]

**Original:**
```
Meine Studentenausweisnummer ist <ADDRESS>
```

**Expected:**
```
<STUDENT_NUMBER>
```

**Actual:**
```
Meine Studentenausweisnummer ist <ADDRESS>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B246B57DD0>
entity = 'STUDENT_NUMBER', text = 'Meine Studentenausweisnummer ist STU-12345'
expected = '<STUDENT_NUMBER>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect STUDENT_NUMBER in: Meine Studentenausweisnummer ist STU-12345
E       assert '<STUDENT_NUMBER>' in 'Meine Studentenausweisnummer ist <ADDRESS>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[EMPLOYEE_ID-Meine Mitarbeiternummer ist EMP-67890-<EMPLOYEE_ID>]

**Original:**
```
Meine Mitarbeiternummer ist EMP-67890
```

**Expected:**
```
<EMPLOYEE_ID>
```

**Actual:**
```
Meine Mitarbeiternummer ist EMP-67890
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B226D41ED0>
entity = 'EMPLOYEE_ID', text = 'Meine Mitarbeiternummer ist EMP-67890'
expected = '<EMPLOYEE_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect EMPLOYEE_ID in: Meine Mitarbeiternummer ist EMP-67890
E       assert '<EMPLOYEE_ID>' in 'Meine Mitarbeiternummer ist EMP-67890'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[PRO_LICENSE-Meine Berufslizenz ist LIC-54321-<PRO_LICENSE>]

**Original:**
```
Meine Berufslizenz ist LIC-54321
```

**Expected:**
```
<PRO_LICENSE>
```

**Actual:**
```
Meine Berufslizenz ist LIC-54321
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B2447478D0>
entity = 'PRO_LICENSE', text = 'Meine Berufslizenz ist LIC-54321'
expected = '<PRO_LICENSE>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect PRO_LICENSE in: Meine Berufslizenz ist LIC-54321
E       assert '<PRO_LICENSE>' in 'Meine Berufslizenz ist LIC-54321'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[HEALTH_ID-Meine NHS-Nummer ist 943 476 5919-<HEALTH_ID>]

**Original:**
```
Meine NHS-Nummer ist 943 476 5919
```

**Expected:**
```
<HEALTH_ID>
```

**Actual:**
```
Meine NHS-Nummer ist 943 476 5919
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B2285C82D0>
entity = 'HEALTH_ID', text = 'Meine NHS-Nummer ist 943 476 5919'
expected = '<HEALTH_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect HEALTH_ID in: Meine NHS-Nummer ist 943 476 5919
E       assert '<HEALTH_ID>' in 'Meine NHS-Nummer ist 943 476 5919'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[VOTER_ID-Meine W\xe4hlerausweisnummer ist V9876543-<VOTER_ID>]

**Original:**
```
Meine Wählerausweisnummer ist <PASSPORT>
```

**Expected:**
```
<VOTER_ID>
```

**Actual:**
```
Meine Wählerausweisnummer ist <PASSPORT>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B213FA8250>
entity = 'VOTER_ID', text = 'Meine Wählerausweisnummer ist V9876543'
expected = '<VOTER_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect VOTER_ID in: Meine Wählerausweisnummer ist V9876543
E       assert '<VOTER_ID>' in 'Meine Wählerausweisnummer ist <PASSPORT>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[BENEFIT_ID-Meine Sozialhilfekarte ist B11223344-<BENEFIT_ID>]

**Original:**
```
Meine Sozialhilfekarte ist <PASSPORT>
```

**Expected:**
```
<BENEFIT_ID>
```

**Actual:**
```
Meine Sozialhilfekarte ist <PASSPORT>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B20F4F0ED0>
entity = 'BENEFIT_ID', text = 'Meine Sozialhilfekarte ist B11223344'
expected = '<BENEFIT_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect BENEFIT_ID in: Meine Sozialhilfekarte ist B11223344
E       assert '<BENEFIT_ID>' in 'Meine Sozialhilfekarte ist <PASSPORT>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[MILITARY_ID-Meine Milit\xe4rausweis ist M55667788-<MILITARY_ID>]

**Original:**
```
Meine Militärausweis ist <PASSPORT>
```

**Expected:**
```
<MILITARY_ID>
```

**Actual:**
```
Meine Militärausweis ist <PASSPORT>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B225277AD0>
entity = 'MILITARY_ID', text = 'Meine Militärausweis ist M55667788'
expected = '<MILITARY_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect MILITARY_ID in: Meine Militärausweis ist M55667788
E       assert '<MILITARY_ID>' in 'Meine Militärausweis ist <PASSPORT>'

tests\unit\test_entity_coverage.py:180: AssertionError
```
</details>

#### ::test_entity_coverage::test_entity_coverage[DEVICE_ID-Meine Ger\xe4te-ID ist DEV-999888777-<DEVICE_ID>]

**Original:**
```
Meine Geräte-ID ist DEV-<ID_NUMBER>
```

**Expected:**
```
<DEVICE_ID>
```

**Actual:**
```
Meine Geräte-ID ist DEV-<ID_NUMBER>
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x000002B24A3B3F90>
entity = 'DEVICE_ID', text = 'Meine Geräte-ID ist DEV-999888777'
expected = '<DEVICE_ID>'

    @pytest.mark.parametrize("entity,text,expected", entity_samples)
    def test_entity_coverage(f, entity, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Failed to detect {entity} in: {text}"
E       AssertionError: Failed to detect DEVICE_ID in: Meine Geräte-ID ist DEV-999888777
E       assert '<DEVICE_ID>' in 'Meine Geräte-ID ist DEV-<ID_NUMBER>'

tests\unit\test_entity_coverage.py:180: AssertionError
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
self = <unit.test_tokens.TestOTPCode object at 0x0000024B8840B390>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024B8C066550>

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
>       assert "<OTP_CODE>" in result
E       AssertionError: assert '<OTP_CODE>' in 'one_time_<PASSWORD>'

tests\unit\test_tokens.py:123: AssertionError
```
</details>

