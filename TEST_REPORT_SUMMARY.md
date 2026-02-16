# Test Execution Report

Generated: **2026-02-16 23:32:18**

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1117 |
| Passed | 1108 |
| Failed | 9 |
| Skipped | 0 |
| Pass Rate | 99.2% |

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
- Passed: 7
- Failed: 1
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
- Passed: 185
- Failed: 6
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
f = <PII_filter.pii_filter.PIIFilter object at 0x000001BE8C8DC9D0>
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

### ❌ test_false_positives.py

#### ::test_false_positives::test_false_positives[Meine E-Mail ist max.mustermann@beispiel.de und ich wohne in der Musterstra\xdfe 5, 10115 Berlin.-<EMAIL>]

**Original:**
```
Meine E-Mail ist <EMAIL_ADDRESS> und ich wohne <ADDRESS>.
```

**Expected:**
```
<EMAIL>
```

**Actual:**
```
Meine E-Mail ist <EMAIL_ADDRESS> und ich wohne <ADDRESS>.
```

<details><summary>Full Failure Block</summary>

```
f = <PII_filter.pii_filter.PIIFilter object at 0x000001917AD506D0>
text = 'Meine E-Mail ist max.mustermann@beispiel.de und ich wohne in der Musterstraße 5, 10115 Berlin.'
expected = '<EMAIL>'

    @pytest.mark.parametrize("text,expected", cases)
    def test_false_positives(f, text, expected):
        out = f.anonymize_text(text)
>       assert expected in out, f"Expected {expected} in anonymized output for: {text}; got: {out}"
E       AssertionError: Expected <EMAIL> in anonymized output for: Meine E-Mail ist max.mustermann@beispiel.de und ich wohne in der Musterstraße 5, 10115 Berlin.; got: Meine E-Mail ist <EMAIL_ADDRESS> und ich wohne <ADDRESS>.
E       assert '<EMAIL>' in 'Meine E-Mail ist <EMAIL_ADDRESS> und ich wohne <ADDRESS>.'

tests\unit\test_false_positives.py:23: AssertionError
```
</details>

### ❌ test_regex_patterns.py

#### ::test_regex_patterns::test_commercial_register_with_context

**Original:**
```
\n    Company Registration <LICENSE_PLATE>:\n    The company is registered at:\n    - <COMMERCIAL_REGISTER>123456\n    - German VAT ID: <TAX_ID>\n    - Contact: <EMAIL_ADDRESS>\n    
```

**Expected:**
```
<EMAIL>
```

**Actual:**
```
\n    Company Registration <LICENSE_PLATE>:\n    The company is registered at:\n    - <COMMERCIAL_REGISTER>123456\n    - German VAT ID: <TAX_ID>\n    - Contact: <EMAIL_ADDRESS>\n    
```

<details><summary>Full Failure Block</summary>

```
def test_commercial_register_with_context():
        """Test COMMERCIAL_REGISTER detection in realistic document context."""
        f = PIIFilter()
    
        document = """
        Company Registration Details:
        The company is registered at:
        - Amtsgericht München, Handelsregister B 123456
        - German VAT ID: DE123456789
        - Contact: max.mustermann@example.de
        """
    
        out = f.anonymize_text(document)
        assert "<COMMERCIAL_REGISTER>" in out, "Should detect commercial register in document"
>       assert "<EMAIL>" in out, "Should also detect email"
E       AssertionError: Should also detect email
E       assert '<EMAIL>' in '\n    Company Registration <LICENSE_PLATE>:\n    The company is registered at:\n    - <COMMERCIAL_REGISTER>123456\n    - German VAT ID: <TAX_ID>\n    - Contact: <EMAIL_ADDRESS>\n    '

tests\unit\test_regex_patterns.py:237: AssertionError
```
</details>

#### ::test_regex_patterns::test_case_reference_with_context

**Original:**
```
\n    Case Management System:\n    - <CASE_REFERENCE>\n    - <CASE_REFERENCE>\n    - Customer Name: <PERSON>\n    - Email: <EMAIL_ADDRESS>\n    - Registration: <LICENSE_PLATE>ter B 123456\n    
```

**Expected:**
```
<EMAIL>
```

**Actual:**
```
\n    Case Management System:\n    - <CASE_REFERENCE>\n    - <CASE_REFERENCE>\n    - Customer Name: <PERSON>\n    - Email: <EMAIL_ADDRESS>\n    - Registration: <LICENSE_PLATE>ter B 123456\n    
```

<details><summary>Full Failure Block</summary>

```
def test_case_reference_with_context():
        """Test CASE_REFERENCE detection in realistic document context."""
        f = PIIFilter()
    
        document = """
        Case Management System:
        - Case ID: CASE-2023-001234
        - Reference Number: REF-2024-567890
        - Customer Name: John Schmidt
        - Email: john.schmidt@example.com
        - Registration: Handelsregister B 123456
        """
    
        out = f.anonymize_text(document)
        assert "<CASE_REFERENCE>" in out, "Should detect case reference in document"
        assert "<PERSON>" in out, "Should also detect person name"
>       assert "<EMAIL>" in out, "Should detect email"
E       AssertionError: Should detect email
E       assert '<EMAIL>' in '\n    Case Management System:\n    - <CASE_REFERENCE>\n    - <CASE_REFERENCE>\n    - Customer Name: <PERSON>\n    - Email: <EMAIL_ADDRESS>\n    - Registration: <LICENSE_PLATE>ter B 123456\n    '

tests\unit\test_regex_patterns.py:347: AssertionError
```
</details>

#### ::test_regex_patterns::test_german_gov_ids_with_context

**Original:**
```
\n    Behördliche Registrierung:\n    <BUND_ID>\n    <ELSTER_ID>\n    <SERVICEKONTO>\n    Name: <PERSON>\n    Email: <EMAIL_ADDRESS>\n    
```

**Expected:**
```
<EMAIL>
```

**Actual:**
```
\n    Behördliche Registrierung:\n    <BUND_ID>\n    <ELSTER_ID>\n    <SERVICEKONTO>\n    Name: <PERSON>\n    Email: <EMAIL_ADDRESS>\n    
```

<details><summary>Full Failure Block</summary>

```
def test_german_gov_ids_with_context():
        """Test German e-government IDs in realistic document context."""
        f = PIIFilter()
    
        document = """
        Behördliche Registrierung:
        BundID: BUND-12345678-ABCD
        ELSTER-ID: ELST-12345
        Servicekonto: servicekonto_56789
        Name: Max Mustermann
        Email: max@example.com
        """
    
        out = f.anonymize_text(document)
        assert "<BUND_ID>" in out, "Should detect BundID in document"
        assert "<ELSTER_ID>" in out, "Should detect ELSTER_ID in document"
        assert "<SERVICEKONTO>" in out, "Should detect SERVICEKONTO in document"
        assert "<PERSON>" in out, "Should also detect person name"
>       assert "<EMAIL>" in out, "Should detect email"
E       AssertionError: Should detect email
E       assert '<EMAIL>' in '\n    Behördliche Registrierung:\n    <BUND_ID>\n    <ELSTER_ID>\n    <SERVICEKONTO>\n    Name: <PERSON>\n    Email: <EMAIL_ADDRESS>\n    '

tests\unit\test_regex_patterns.py:492: AssertionError
```
</details>

#### ::test_regex_patterns::test_german_gov_ids_priority

**Original:**
```
\n    <BUND_ID>\n    Phone: <PHONE_NUMBER>\n    Email: <EMAIL_ADDRESS>\n    <SERVICEKONTO>\n    
```

**Expected:**
```
<PHONE>
```

**Actual:**
```
\n    <BUND_ID>\n    Phone: <PHONE_NUMBER>\n    Email: <EMAIL_ADDRESS>\n    <SERVICEKONTO>\n    
```

<details><summary>Full Failure Block</summary>

```
def test_german_gov_ids_priority():
        """Test that German e-government IDs don't conflict with other entities."""
        f = PIIFilter()
    
        # Document with mixed entity types
        document = """
        BundID: BUND-12345678-ABCD
        Phone: +49 30 12345678
        Email: user@example.de
        Service-Konto: servicekonto_xyz789
        """
    
        out = f.anonymize_text(document)
        assert "<BUND_ID>" in out, "Should detect BundID"
        assert "<SERVICEKONTO>" in out, "Should detect SERVICEKONTO"
>       assert "<PHONE>" in out, "Should detect phone"
E       AssertionError: Should detect phone
E       assert '<PHONE>' in '\n    <BUND_ID>\n    Phone: <PHONE_NUMBER>\n    Email: <EMAIL_ADDRESS>\n    <SERVICEKONTO>\n    '

tests\unit\test_regex_patterns.py:530: AssertionError
```
</details>

#### ::test_regex_patterns::test_auth_secrets_with_context

**Original:**
```
\n    User Account Setup:\n    Username: <EMAIL_ADDRESS>\n    <PASSWORD>\n    <PIN>\n    \n    Two-Factor Authentication:\n    <TAN>\n    <PUK>\n    <RECOVERY_CODE>\n    
```

**Expected:**
```
<EMAIL>
```

**Actual:**
```
\n    User Account Setup:\n    Username: <EMAIL_ADDRESS>\n    <PASSWORD>\n    <PIN>\n    \n    Two-Factor Authentication:\n    <TAN>\n    <PUK>\n    <RECOVERY_CODE>\n    
```

<details><summary>Full Failure Block</summary>

```
def test_auth_secrets_with_context():
        """Test authentication secrets in realistic document context."""
        f = PIIFilter()
    
        document = """
        User Account Setup:
        Username: john.doe@example.com
        Password: SecureP@ssw0rd2024!
        PIN: 1234
    
        Two-Factor Authentication:
        TAN: 654321
        PUK: 12345678
        Recovery code: ABC-DEF-123-456
        """
    
        out = f.anonymize_text(document)
        assert "<PASSWORD>" in out, "Should detect password"
        assert "<PIN>" in out, "Should detect PIN"
        assert "<TAN>" in out, "Should detect TAN"
        assert "<PUK>" in out, "Should detect PUK"
        assert "<RECOVERY_CODE>" in out, "Should detect recovery code"
>       assert "<EMAIL>" in out, "Should also detect email"
E       AssertionError: Should also detect email
E       assert '<EMAIL>' in '\n    User Account Setup:\n    Username: <EMAIL_ADDRESS>\n    <PASSWORD>\n    <PIN>\n    \n    Two-Factor Authentication:\n    <TAN>\n    <PUK>\n    <RECOVERY_CODE>\n    '

tests\unit\test_regex_patterns.py:716: AssertionError
```
</details>

#### ::test_regex_patterns::test_auth_secrets_priority

**Original:**
```
\n    Login Credentials:\n    Email: <EMAIL_ADDRESS>\n    <PASSWORD>\n    <PIN>\n    Phone: <PHONE_NUMBER>\n    \n    <RECOVERY_CODE>:\n    <RECOVERY_CODE>\n    <PUK>\n    
```

**Expected:**
```
<EMAIL>
```

**Actual:**
```
\n    Login Credentials:\n    Email: <EMAIL_ADDRESS>\n    <PASSWORD>\n    <PIN>\n    Phone: <PHONE_NUMBER>\n    \n    <RECOVERY_CODE>:\n    <RECOVERY_CODE>\n    <PUK>\n    
```

<details><summary>Full Failure Block</summary>

```
def test_auth_secrets_priority():
        """Test that authentication secrets don't conflict with other entities."""
        f = PIIFilter()
    
        document = """
        Login Credentials:
        Email: user@example.com
        Password: SecureP@ss@2024!
        PIN: 1234
        Phone: +49 30 12345678
    
        Recovery Information:
        Recovery code: ABC-DEF-123-456
        PUK: 87654321
        """
    
        out = f.anonymize_text(document)
        assert "<PASSWORD>" in out, "Should detect password"
        assert "<PIN>" in out, "Should detect PIN"
        assert "<PUK>" in out, "Should detect PUK"
        assert "<RECOVERY_CODE>" in out, "Should detect recovery code"
>       assert "<EMAIL>" in out, "Should detect email"
E       AssertionError: Should detect email
E       assert '<EMAIL>' in '\n    Login Credentials:\n    Email: <EMAIL_ADDRESS>\n    <PASSWORD>\n    <PIN>\n    Phone: <PHONE_NUMBER>\n    \n    <RECOVERY_CODE>:\n    <RECOVERY_CODE>\n    <PUK>\n    '

tests\unit\test_regex_patterns.py:784: AssertionError
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
self = <unit.test_tokens.TestOTPCode object at 0x0000020692CAF910>
filter_instance = <PII_filter.pii_filter.PIIFilter object at 0x0000020697733250>

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
>       assert "<OTP_CODE>" in result
E       AssertionError: assert '<OTP_CODE>' in 'one_time_<PASSWORD>'

tests\unit\test_tokens.py:123: AssertionError
```
</details>

