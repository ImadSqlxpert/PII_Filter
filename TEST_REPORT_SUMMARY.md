# Test Execution Report

Generated: **2026-02-14 20:36:54**

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 1117 |
| Passed | 1093 |
| Failed | 24 |
| Skipped | 0 |
| Pass Rate | 97.9% |

## Per‑File Results

### test_api_keys.py
- Passed: 28
- Failed: 0
- Skipped: 0

### test_chat_person_address_de_en.py
- Passed: 36
- Failed: 11
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
- Passed: 8
- Failed: 4
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
- Passed: 58
- Failed: 8
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

### ❌ test_chat_person_address_de_en.py

#### ::test_chat_person_address_de_en::test_chat_address_true_positives[User: Shipping address: Main Street 42, 12345 Sampletown]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E977305890>
chat = 'User: Shipping address: Main Street 42, 12345 Sampletown'

    @pytest.mark.parametrize("chat", [
        "User: My address is 221B Baker Street, NW1 6XE London",
        "User: Shipping address: Main Street 42, 12345 Sampletown",
        "Kunde: Meine Adresse ist Hauptstraße 5, 10115 Berlin",
        "Kunde: Lieferadresse: Goethestraße 10\n80331 München",
        "User: Send to Am Stadtpark 3, 20095 Hamburg",
    ])
    def test_chat_address_true_positives(f, chat):
        out = f.anonymize_text(chat)
>       assert has_tag(out, ADDRESS), out
E       AssertionError: User: Shipping address: Main Street 42, <LOCATION>
E       assert False
E        +  where False = has_tag('User: Shipping address: Main Street 42, <LOCATION>', 'ADDRESS')

tests\unit\test_chat_person_address_de_en.py:91: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_address_true_positives[Kunde: Meine Adresse ist Hauptstra\xdfe 5, 10115 Berlin]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E931E00F50>
chat = 'Kunde: Meine Adresse ist Hauptstraße 5, 10115 Berlin'

    @pytest.mark.parametrize("chat", [
        "User: My address is 221B Baker Street, NW1 6XE London",
        "User: Shipping address: Main Street 42, 12345 Sampletown",
        "Kunde: Meine Adresse ist Hauptstraße 5, 10115 Berlin",
        "Kunde: Lieferadresse: Goethestraße 10\n80331 München",
        "User: Send to Am Stadtpark 3, 20095 Hamburg",
    ])
    def test_chat_address_true_positives(f, chat):
        out = f.anonymize_text(chat)
        assert has_tag(out, ADDRESS), out
        # Don’t mis-tag address as PERSON
>       assert not has_tag(out, PERSON), out
E       AssertionError: <PERSON>: Meine Adresse ist <ADDRESS>
E       assert not True
E        +  where True = has_tag('<PERSON>: Meine Adresse ist <ADDRESS>', 'PERSON')

tests\unit\test_chat_person_address_de_en.py:93: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_address_true_positives[Kunde: Lieferadresse: Goethestra\xdfe 10\n80331 M\xfcnchen]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E904DE8A10>
chat = 'Kunde: Lieferadresse: Goethestraße 10\n80331 München'

    @pytest.mark.parametrize("chat", [
        "User: My address is 221B Baker Street, NW1 6XE London",
        "User: Shipping address: Main Street 42, 12345 Sampletown",
        "Kunde: Meine Adresse ist Hauptstraße 5, 10115 Berlin",
        "Kunde: Lieferadresse: Goethestraße 10\n80331 München",
        "User: Send to Am Stadtpark 3, 20095 Hamburg",
    ])
    def test_chat_address_true_positives(f, chat):
        out = f.anonymize_text(chat)
        assert has_tag(out, ADDRESS), out
        # Don’t mis-tag address as PERSON
>       assert not has_tag(out, PERSON), out
E       AssertionError: <PERSON>: <PERSON>: <ADDRESS>
E       assert not True
E        +  where True = has_tag('<PERSON>: <PERSON>: <ADDRESS>', 'PERSON')

tests\unit\test_chat_person_address_de_en.py:93: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_single_tokens_not_person_or_address[Kunde: RECHNUNG]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E9121F7710>
chat = 'Kunde: RECHNUNG'

    @pytest.mark.parametrize("chat", [
        "User: Straße",
        "User: Weg",
        "User: Gasse",
        "User: Allee",
        "User: ADDRESS:",
        "Kunde: RECHNUNG",
        "Kunde: KUNDENNUMMER",
    ])
    def test_chat_single_tokens_not_person_or_address(f, chat):
        out = f.anonymize_text(chat)
>       assert not has_tag(out, PERSON), out
E       AssertionError: <PERSON>: <BANK_ACCOUNT>
E       assert not True
E        +  where True = has_tag('<PERSON>: <BANK_ACCOUNT>', 'PERSON')

tests\unit\test_chat_person_address_de_en.py:129: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_single_tokens_not_person_or_address[Kunde: KUNDENNUMMER]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E977181F50>
chat = 'Kunde: KUNDENNUMMER'

    @pytest.mark.parametrize("chat", [
        "User: Straße",
        "User: Weg",
        "User: Gasse",
        "User: Allee",
        "User: ADDRESS:",
        "Kunde: RECHNUNG",
        "Kunde: KUNDENNUMMER",
    ])
    def test_chat_single_tokens_not_person_or_address(f, chat):
        out = f.anonymize_text(chat)
>       assert not has_tag(out, PERSON), out
E       AssertionError: <PERSON>: KUNDENNUMMER
E       assert not True
E        +  where True = has_tag('<PERSON>: KUNDENNUMMER', 'PERSON')

tests\unit\test_chat_person_address_de_en.py:129: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_de_chat_ich_bin_location_not_person[Kunde: Ich bin in M\xfcnchen im Urlaub]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E905F13910>
chat = 'Kunde: Ich bin in München im Urlaub'

    @pytest.mark.parametrize("chat", [
        "Kunde: Ich bin in München im Urlaub",
        "User: Ich bin in Berlin, kein Name",
    ])
    def test_de_chat_ich_bin_location_not_person(f, chat):
        out = f.anonymize_text(chat)
>       assert not has_tag(out, PERSON), out
E       AssertionError: <PERSON>: Ich bin in München im Urlaub
E       assert not True
E        +  where True = has_tag('<PERSON>: Ich bin in München im Urlaub', 'PERSON')

tests\unit\test_chat_person_address_de_en.py:184: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_partial_address_across_lines[User: Stra\xdfe: Hauptstra\xdfe\nNr.: 10\nPLZ/Ort: 10115 Berlin]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E936CE4450>
chat = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

    @pytest.mark.parametrize("chat", [
        "User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin",
        "User: Street: Baker St.\nNumber: 221B\nCity: London",
    ])
    def test_chat_partial_address_across_lines(f, chat):
        out = f.anonymize_text(chat)
>       assert has_tag(out, ADDRESS), out
E       AssertionError: User: Straße: Hauptstraße
E         Nr.: 10
E         PLZ/Ort: <LOCATION>
E       assert False
E        +  where False = has_tag('User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: <LOCATION>', 'ADDRESS')

tests\unit\test_chat_person_address_de_en.py:197: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_partial_address_across_lines[User: Street: Baker St.\nNumber: 221B\nCity: London]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E927ABD1D0>
chat = 'User: Street: Baker St.\nNumber: 221B\nCity: London'

    @pytest.mark.parametrize("chat", [
        "User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin",
        "User: Street: Baker St.\nNumber: 221B\nCity: London",
    ])
    def test_chat_partial_address_across_lines(f, chat):
        out = f.anonymize_text(chat)
>       assert has_tag(out, ADDRESS), out
E       AssertionError: User: Street: <PERSON>
E         Number: 221B
E         City: London
E       assert False
E        +  where False = has_tag('User: Street: <PERSON>\nNumber: 221B\nCity: London', 'ADDRESS')

tests\unit\test_chat_person_address_de_en.py:197: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_chat_address_abbreviations_true_positive[User: Shipping to Main St. 10, 90210 Beverly Hills]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E975E550D0>
chat = 'User: Shipping to Main St. 10, 90210 Beverly Hills'

    @pytest.mark.parametrize("chat", [
        "User: Send to Hauptstr. 5, 10115 Berlin",
        "User: Shipping to Main St. 10, 90210 Beverly Hills",
        "User: Deliver to 10 Downing St, SW1A 2AA London",
    ])
    def test_chat_address_abbreviations_true_positive(f, chat):
        out = f.anonymize_text(chat)
>       assert has_tag(out, ADDRESS), out
E       AssertionError: User: Shipping to Main St. 10, <LOCATION>
E       assert False
E        +  where False = has_tag('User: Shipping to Main St. 10, <LOCATION>', 'ADDRESS')

tests\unit\test_chat_person_address_de_en.py:239: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_non_regression_other_entities_in_chat[Call me at +49 30 1234567-PHONE_NUMBER]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E9386251D0>
chat = 'Call me at +49 30 1234567', expected = 'PHONE_NUMBER'

    @pytest.mark.parametrize("chat, expected", [
        ("Call me at +49 30 1234567", "PHONE_NUMBER"),
        ("I was born on March 15, 1985", "DATE"),
        ("SSN: 123-45-6789", "ID_NUMBER"),
        ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token", "ACCESS_TOKEN"),
        ("sk-proj-1234567890abcdefghijklmnop", "API_KEY"),
        ("tok_abc123def456ghi789xyz", "PAYMENT_TOKEN"),
        ("MAC AA:BB:CC:DD:EE:FF", "MAC_ADDRESS"),
        ("IP: 192.168.1.1", "IP_ADDRESS"),
    ])
    def test_non_regression_other_entities_in_chat(f, chat, expected):
        out = f.anonymize_text(chat)
>       assert has_tag(out, expected), out
E       AssertionError: Call me at <PHONE>
E       assert False
E        +  where False = has_tag('Call me at <PHONE>', 'PHONE_NUMBER')

tests\unit\test_chat_person_address_de_en.py:258: AssertionError
```
</details>

#### ::test_chat_person_address_de_en::test_non_regression_other_entities_in_chat[tok_abc123def456ghi789xyz-PAYMENT_TOKEN]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x000001E905269110>
chat = 'tok_abc123def456ghi789xyz', expected = 'PAYMENT_TOKEN'

    @pytest.mark.parametrize("chat, expected", [
        ("Call me at +49 30 1234567", "PHONE_NUMBER"),
        ("I was born on March 15, 1985", "DATE"),
        ("SSN: 123-45-6789", "ID_NUMBER"),
        ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token", "ACCESS_TOKEN"),
        ("sk-proj-1234567890abcdefghijklmnop", "API_KEY"),
        ("tok_abc123def456ghi789xyz", "PAYMENT_TOKEN"),
        ("MAC AA:BB:CC:DD:EE:FF", "MAC_ADDRESS"),
        ("IP: 192.168.1.1", "IP_ADDRESS"),
    ])
    def test_non_regression_other_entities_in_chat(f, chat, expected):
        out = f.anonymize_text(chat)
>       assert has_tag(out, expected), out
E       AssertionError: tok_abc123def456ghi789xyz
E       assert False
E        +  where False = has_tag('tok_abc123def456ghi789xyz', 'PAYMENT_TOKEN')

tests\unit\test_chat_person_address_de_en.py:258: AssertionError
```
</details>

### ❌ test_guards.py

#### ::test_guards::test_guard_natural_suffix_requires_number_off_keeps

**Original:**
```
Am Wald
```

**Expected:**
```
<ADDRESS>
```

**Actual:**
```
Am Wald
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x0000021064079D10>

    def test_guard_natural_suffix_requires_number_off_keeps(f):
        text = "Am Wald"
        out = f.anonymize_text(
            text,
            guards_enabled=True,
            guard_natural_suffix_requires_number=False,   # OFF
            guard_single_token_addresses=False,
            guard_address_vs_person_priority=False,
            guard_requires_context_without_number=False,
        )
        # With other guards off, permissive regex may keep it
>       assert "<ADDRESS>" in out, "With guard OFF and other guards disabled, 'Am Wald' may be kept as ADDRESS."
E       AssertionError: With guard OFF and other guards disabled, 'Am Wald' may be kept as ADDRESS.
E       assert '<ADDRESS>' in 'Am Wald'

tests\unit\test_guards.py:38: AssertionError
```
</details>

#### ::test_guards::test_guard_requires_context_without_number_kept_with_keyword

**Original:**
```
My address is Rue Victor Hugo
```

**Expected:**
```
<ADDRESS>
```

**Actual:**
```
My address is Rue Victor Hugo
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x0000021064079D10>

    def test_guard_requires_context_without_number_kept_with_keyword(f):
        text = "My address is Rue Victor Hugo"   # 'address' is in ADDRESS_CONTEXT_KEYWORDS
        out = f.anonymize_text(
            text,
            guards_enabled=True,
            guard_requires_context_without_number=True,   # ON
            guard_natural_suffix_requires_number=False,
            guard_single_token_addresses=False,
            guard_address_vs_person_priority=False,
        )
>       assert "<ADDRESS>" in out, "Context keyword + no number → allowed by the guard."
E       AssertionError: Context keyword + no number → allowed by the guard.
E       assert '<ADDRESS>' in 'My address is Rue Victor Hugo'

tests\unit\test_guards.py:67: AssertionError
```
</details>

#### ::test_guards::test_guard_requires_context_without_number_off_kept

**Original:**
```
Rue Victor Hugo
```

**Expected:**
```
<ADDRESS>
```

**Actual:**
```
Rue Victor Hugo
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x0000021064079D10>

    def test_guard_requires_context_without_number_off_kept(f):
        text = "Rue Victor Hugo"
        out = f.anonymize_text(
            text,
            guards_enabled=True,
            guard_requires_context_without_number=False,  # OFF
            guard_natural_suffix_requires_number=False,
            guard_single_token_addresses=False,
            guard_address_vs_person_priority=False,
        )
>       assert "<ADDRESS>" in out, "With guard OFF, name-only street can be kept."
E       AssertionError: With guard OFF, name-only street can be kept.
E       assert '<ADDRESS>' in 'Rue Victor Hugo'

tests\unit\test_guards.py:80: AssertionError
```
</details>

#### ::test_guards::test_guard_single_token_addresses_off_keeps

**Original:**
```
Rosenweg
```

**Expected:**
```
<ADDRESS>
```

**Actual:**
```
Rosenweg
```

<details><summary>Full Failure Block</summary>

```
f = <pii_filter.pii_filter.PIIFilter object at 0x0000021064079D10>

    def test_guard_single_token_addresses_off_keeps(f):
        text = "Rosenweg"
        out = f.anonymize_text(
            text,
            guards_enabled=True,
            guard_single_token_addresses=False,           # OFF
            guard_requires_context_without_number=False,
            guard_natural_suffix_requires_number=False,
            guard_address_vs_person_priority=False,
        )
>       assert "<ADDRESS>" in out, "With guard OFF, permissive suffix match can be kept as ADDRESS."
E       AssertionError: With guard OFF, permissive suffix match can be kept as ADDRESS.
E       assert '<ADDRESS>' in 'Rosenweg'

tests\unit\test_guards.py:109: AssertionError
```
</details>

### ❌ test_person_address_de_en.py

#### ::test_person_address_de_en::test_person_intro_true_positives[I am called Sarah Connor]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199A00BDED0>
text = 'I am called Sarah Connor'

    @pytest.mark.parametrize("text", [
        "Mein Name ist Anna Müller",
        "Ich heiße Lukas Bauer",
        "My name is John Doe",
        "I am called Sarah Connor",
        # allow small variation/whitespace
        "  Mein Name ist   Paul  Meier  ",
    ])
    def test_person_intro_true_positives(f, text):
        out = f.anonymize_text(text)
>       assert has_tag(out, "PERSON"), f"Expected <PERSON> in: {out}"
E       AssertionError: Expected <PERSON> in: I am called Sarah Connor
E       assert False
E        +  where False = has_tag('I am called Sarah Connor', 'PERSON')

tests\unit\test_person_address_de_en.py:47: AssertionError
```
</details>

#### ::test_person_address_de_en::test_address_true_positives[Main Street 42, 12345 Sampletown]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199D4A5AC50>
text = 'Main Street 42, 12345 Sampletown'

    @pytest.mark.parametrize("text", [
        "Musterstraße 12, 10115 Berlin",
        "Hauptstraße 5",
        "Main Street 42, 12345 Sampletown",
        "Goethestraße 10\n10115 Berlin",
        "Lindenstr. 7 – 80331 München",
        "Am Stadtpark 3, 20095 Hamburg",
    ])
    def test_address_true_positives(f, text):
        out = f.anonymize_text(text)
>       assert has_tag(out, "ADDRESS"), f"Expected <ADDRESS> in: {out}"
E       AssertionError: Expected <ADDRESS> in: Main Street 42, <LOCATION>
E       assert False
E        +  where False = has_tag('Main Street 42, <LOCATION>', 'ADDRESS')

tests\unit\test_person_address_de_en.py:101: AssertionError
```
</details>

#### ::test_person_address_de_en::test_address_location_merge_becomes_address[Main Street 42 \u2014 12345 Sampletown]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199D32616D0>
text = 'Main Street 42 — 12345 Sampletown'

    @pytest.mark.parametrize("text", [
        "Hauptstraße 5, 80331 München",
        "Goethestraße 10\n10115 Berlin",
        "Main Street 42 — 12345 Sampletown",
    ])
    def test_address_location_merge_becomes_address(f, text):
        out = f.anonymize_text(text)
>       assert has_tag(out, "ADDRESS"), f"Expected merged <ADDRESS> in: {out}"
E       AssertionError: Expected merged <ADDRESS> in: Main Street 42 — <LOCATION>
E       assert False
E        +  where False = has_tag('Main Street 42 — <LOCATION>', 'ADDRESS')

tests\unit\test_person_address_de_en.py:147: AssertionError
```
</details>

#### ::test_person_address_de_en::test_address_trim_and_no_bleed_into_labels[Main Street 42, 12345 City\nTelefon: 030 123456]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199BF2DE890>
text = 'Main Street 42, 12345 City\nTelefon: 030 123456'

    @pytest.mark.parametrize("text", [
        "Hauptstraße 10\nEmail: someone@example.com",
        "Main Street 42, 12345 City\nTelefon: 030 123456",
    ])
    def test_address_trim_and_no_bleed_into_labels(f, text):
        out = f.anonymize_text(text)
>       assert has_tag(out, "ADDRESS"), f"Expected <ADDRESS> in: {out}"
E       AssertionError: Expected <ADDRESS> in: Main Street 42, <LOCATION>: 030 123456
E       assert False
E        +  where False = has_tag('Main Street 42, <LOCATION>: 030 123456', 'ADDRESS')

tests\unit\test_person_address_de_en.py:173: AssertionError
```
</details>

#### ::test_person_address_de_en::test_person_single_token_needs_intro[Anna-False]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199BF2A6B90>
text = 'Anna', expect_person = False

    @pytest.mark.parametrize("text, expect_person", [
        ("Anna", False),                   # too ambiguous; no intro cue
        ("Mein Name ist Anna", True),     # intro cue allows single token
        ("Ich bin Anna", True),           # allowed if name-like token follows
        ("Ich bin in München", False),    # 'Ich bin' + location (not a name)
    ])
    def test_person_single_token_needs_intro(f, text, expect_person):
        out = f.anonymize_text(text)
>       assert has_tag(out, "PERSON") == expect_person, out
E       AssertionError: <PERSON>
E       assert True == False
E        +  where True = has_tag('<PERSON>', 'PERSON')

tests\unit\test_person_address_de_en.py:191: AssertionError
```
</details>

#### ::test_person_address_de_en::test_non_regression_other_entities[+49 30 1234567-PHONE_NUMBER]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199A3E2DC90>
text = '+49 30 1234567', tag = 'PHONE_NUMBER'

    @pytest.mark.parametrize("text, tag", [
        ("+49 30 1234567", "PHONE_NUMBER"),
        ("I was born on March 15, 1985", "DATE"),
        ("Meine Sozialversicherungsnummer ist 123-45-6789", "ID_NUMBER"),
        ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token", "ACCESS_TOKEN"),
        ("sk-proj-1234567890abcdefghijklmnop", "API_KEY"),
        ("sk_live_abc123def456", "API_KEY"),  # by policy in your suite
        ("tok_abc123def456ghi789xyz", "PAYMENT_TOKEN"),
        ("0x52908400098527886E0F7030069857D2E4169EE7", "CRYPTO_ADDRESS"),
        ("AA:BB:CC:DD:EE:FF", "MAC_ADDRESS"),
        ("192.168.1.10", "IP_ADDRESS"),
    ])
    def test_non_regression_other_entities(f, text, tag):
        out = f.anonymize_text(text)
>       assert has_tag(out, tag), f"Expected <{tag}> in: {out}"
E       AssertionError: Expected <PHONE_NUMBER> in: <PHONE>
E       assert False
E        +  where False = has_tag('<PHONE>', 'PHONE_NUMBER')

tests\unit\test_person_address_de_en.py:212: AssertionError
```
</details>

#### ::test_person_address_de_en::test_non_regression_other_entities[tok_abc123def456ghi789xyz-PAYMENT_TOKEN]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199B973B510>
text = 'tok_abc123def456ghi789xyz', tag = 'PAYMENT_TOKEN'

    @pytest.mark.parametrize("text, tag", [
        ("+49 30 1234567", "PHONE_NUMBER"),
        ("I was born on March 15, 1985", "DATE"),
        ("Meine Sozialversicherungsnummer ist 123-45-6789", "ID_NUMBER"),
        ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token", "ACCESS_TOKEN"),
        ("sk-proj-1234567890abcdefghijklmnop", "API_KEY"),
        ("sk_live_abc123def456", "API_KEY"),  # by policy in your suite
        ("tok_abc123def456ghi789xyz", "PAYMENT_TOKEN"),
        ("0x52908400098527886E0F7030069857D2E4169EE7", "CRYPTO_ADDRESS"),
        ("AA:BB:CC:DD:EE:FF", "MAC_ADDRESS"),
        ("192.168.1.10", "IP_ADDRESS"),
    ])
    def test_non_regression_other_entities(f, text, tag):
        out = f.anonymize_text(text)
>       assert has_tag(out, tag), f"Expected <{tag}> in: {out}"
E       AssertionError: Expected <PAYMENT_TOKEN> in: tok_abc123def456ghi789xyz
E       assert False
E        +  where False = has_tag('tok_abc123def456ghi789xyz', 'PAYMENT_TOKEN')

tests\unit\test_person_address_de_en.py:212: AssertionError
```
</details>

#### ::test_person_address_de_en::test_mixed_line_stress[Customer: John Doe; Address: Main Street 42, 12345 Sampletown]

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
f = <pii_filter.pii_filter.PIIFilter object at 0x00000199A2EE1F10>
text = 'Customer: John Doe; Address: Main Street 42, 12345 Sampletown'

    @pytest.mark.parametrize("text", [
        "Kunde: Anna Müller, Adresse: Hauptstraße 5, 10115 Berlin",
        "Customer: John Doe; Address: Main Street 42, 12345 Sampletown",
    ])
    def test_mixed_line_stress(f, text):
        out = f.anonymize_text(text)
>       assert has_tag(out, "PERSON"), f"Expected <PERSON> in: {out}"
E       AssertionError: Expected <PERSON> in: <CUSTOMER_NUMBER> Doe; Address: Main Street 42, <LOCATION>
E       assert False
E        +  where False = has_tag('<CUSTOMER_NUMBER> Doe; Address: Main Street 42, <LOCATION>', 'PERSON')

tests\unit\test_person_address_de_en.py:225: AssertionError
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
self = <unit.test_tokens.TestOTPCode object at 0x0000024C1A655910>
filter_instance = <pii_filter.pii_filter.PIIFilter object at 0x0000024C1A8C0610>

    def test_one_time_password_format(self, filter_instance):
        """Test one-time password format."""
        text = "one_time_password=987654"
        result = filter_instance.anonymize_text(text)
>       assert "<OTP_CODE>" in result
E       AssertionError: assert '<OTP_CODE>' in 'one_time_<PASSWORD>'

tests\unit\test_tokens.py:123: AssertionError
```
</details>

