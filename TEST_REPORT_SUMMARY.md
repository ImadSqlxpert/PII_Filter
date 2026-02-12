# Test Execution Report

Generated: **2026-02-12 22:57:28**

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1004 |
| Passed | 969 |
| Failed | 35 |
| Skipped | 0 |
| Pass Rate | 96.5% |

## Per‑File Results

### test_api_keys.py
- Passed: 18
- Failed: 10
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

#### ::TestAPIKeyDetection::test_aws_access_key_id

**Original:**
```
My AWS access key is AKIA2JFAKJ1234ABCD.
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
My AWS access key is AKIA2JFAKJ1234ABCD.
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E872968D0>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024EFF921550>

    def test_aws_access_key_id(self, filter_instance):
        """Test AWS Access Key ID detection."""
        text = "My AWS access key is AKIA2JFAKJ1234ABCD."
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'My AWS access key is AKIA2JFAKJ1234ABCD.'

tests\unit\test_api_keys.py:24: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_stripe_live_secret_key

**Original:**
```
Stripe secret key: <PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
Stripe secret key: <PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E87253D90>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024E8708F3D0>

    def test_stripe_live_secret_key(self, filter_instance):
        """Test Stripe Live Secret Key detection."""
        text = "Stripe secret key: sk_live_1234567890abcdefghijk"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'Stripe secret key: <PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:56: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_stripe_test_secret_key

**Original:**
```
Test key <PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
Test key <PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E87258590>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024EB7706250>

    def test_stripe_test_secret_key(self, filter_instance):
        """Test Stripe Test Secret Key detection."""
        text = "Test key sk_test_123456789abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'Test key <PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:62: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_stripe_live_public_key

**Original:**
```
Public key: <PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
Public key: <PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E8714EB10>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024F519E5C50>

    def test_stripe_live_public_key(self, filter_instance):
        """Test Stripe Live Public Key detection."""
        text = "Public key: pk_live_1234567890abcdefghijk"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'Public key: <PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:68: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_stripe_test_public_key

**Original:**
```
<PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
<PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E87848110>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024ED3467110>

    def test_stripe_test_public_key(self, filter_instance):
        """Test Stripe Test Public Key detection."""
        text = "pk_test_123456789abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in '<PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:74: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_openai_api_key

**Original:**
```
openai_api_key=<PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
openai_api_key=<PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E878EE590>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024F52165550>

    def test_openai_api_key(self, filter_instance):
        """Test OpenAI API Key detection."""
        text = "openai_api_key=sk-proj-1234567890abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'openai_api_key=<PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:129: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_cloudflare_api_token

**Original:**
```
cloudflare_token=1234567890abcdef1234567890abcdef1234567890
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
cloudflare_token=1234567890abcdef1234567890abcdef1234567890
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E878EE9D0>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024E8E450290>

    def test_cloudflare_api_token(self, filter_instance):
        """Test Cloudflare API Token detection."""
        text = "cloudflare_token=1234567890abcdef1234567890abcdef1234567890"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'cloudflare_token=1234567890abcdef1234567890abcdef1234567890'

tests\unit\test_api_keys.py:150: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_multiple_api_keys

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
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E878EFE90>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024E962E0150>

    def test_multiple_api_keys(self, filter_instance):
        """Test detection of multiple API keys in single text."""
        text = """
        AWS: AKIA2JFAKJ1234ABCD
        Stripe: sk_live_1234567890abcdefghijk
        GitHub: ghp_1234567890abcdefghijklmnopqrstuvwxyz
        """
        result = filter_instance.anonymize_text(text)
        # Count API_KEY occurrences
        count = result.count("<API_KEY>")
>       assert count >= 3
E       assert 1 >= 3

tests\unit\test_api_keys.py:191: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_api_key_in_url

**Original:**
```
https://api.example.com?<PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
https://api.example.com?<PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E878F4550>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024EB3EC00D0>

    def test_api_key_in_url(self, filter_instance):
        """Test API key detection in URLs."""
        text = "https://api.example.com?api_key=sk_test_1234567890abcdefghijklmnop"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'https://api.example.com?<PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:198: AssertionError
```
</details>

#### ::TestAPIKeyDetection::test_api_key_with_colon

**Original:**
```
stripe_secret_key: <PAYMENT_TOKEN>
```

**Expected:**
```
<API_KEY>
```

**Actual:**
```
stripe_secret_key: <PAYMENT_TOKEN>
```

<details><summary>Full Failure Block</summary>

```
self = <unit.test_api_keys.TestAPIKeyDetection object at 0x0000024E878F5250>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024E8E87EA90>

    def test_api_key_with_colon(self, filter_instance):
        """Test API key detection with : separator."""
        text = "stripe_secret_key: sk_live_1234567890abcdefghijk"
        result = filter_instance.anonymize_text(text)
>       assert "<API_KEY>" in result
E       AssertionError: assert '<API_KEY>' in 'stripe_secret_key: <PAYMENT_TOKEN>'

tests\unit\test_api_keys.py:211: AssertionError
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D609A876D0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D584DD4090>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5D5709E10>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5B852AE10>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5D8300D10>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5CB635210>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5E4C79F90>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D587B683D0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D60EF91C10>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D633AF5290>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5E8A750D0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D584FB4DD0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D583AD3310>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D58128DCD0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5BF1065D0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D58102BA90>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5CA0CC1D0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5BF030190>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D609B1DD10>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D581029550>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5E60F6FD0>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5E53C3210>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D5E53C3D10>
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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001D65A2C1350>
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
self = <unit.test_tokens.TestOTPCode object at 0x00000175C771B950>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x00000175CA7A4F10>

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
>       assert "<OTP_CODE>" in result
E       AssertionError: assert '<OTP_CODE>' in 'one_time_<PASSWORD>'

tests\unit\test_tokens.py:123: AssertionError
```
</details>

