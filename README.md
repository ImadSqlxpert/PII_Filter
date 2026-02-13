# PII Filter

A comprehensive Python-based Personally Identifiable Information (PII) detection and anonymization system. Detects and redacts sensitive entities across **60+ PII types** in **9+ languages** using regex patterns, Presidio, and custom language detection.

---

## What the Filter Does

The `PIIFilter` class detects personally identifiable and sensitive information in text and optionally anonymizes it by replacing detected entities with placeholder tokens (e.g., `<PHONE_NUMBER>`, `<EMAIL_ADDRESS>`).

**Core Capabilities:**
- Detects **60+ entity types** across personal, financial, government, health, and communication categories
- Supports **9+ languages**: English, German, French, Spanish, Turkish, Arabic, and more
- Uses **regex patterns + Presidio recognizers** for high-accuracy detection
- Implements **smart merging logic** to avoid overlapping entities
- Provides **multilingual language detection** (automatic or manual)
- Returns **detailed metadata** (entity type, span positions, confidence score)

---

## Supported Entities by Category

### Personal & Identity (11 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **PERSON** | en, de, fr, es, tr, ar | Full names, first/last names, titles |
| **EMAIL_ADDRESS** | All | Email addresses (RFC-compliant) |
| **PHONE_NUMBER** | All | Phone numbers (multiple formats per locale) |
| **FAX_NUMBER** | All | Fax numbers |
| **PASSPORT** | All | Passport numbers |
| **ID_NUMBER** | All | Generic ID/national ID numbers |
| **DRIVER_LICENSE** | All | Driver license numbers |
| **VOTER_ID** | en, de, fr, es, tr, ar | Voter registration IDs |
| **RESIDENCE_PERMIT** | en, de, fr, es, tr, ar | Residence/immigration permits |
| **BENEFIT_ID** | en, de, fr, es, tr, ar | Social benefit/welfare IDs |
| **MILITARY_ID** | en, de, fr, es, tr, ar | Military service IDs |

### Location & Geographic (6 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **ADDRESS** | en, de, fr, es, tr, ar | Street addresses, house numbers, postal codes |
| **LOCATION** | All | City/country/region names |
| **GEO_COORDINATES** | All | GPS coordinates (lat/long, Plus codes, what3words) |
| **PLUS_CODE** | All | Google Plus Codes |
| **W3W** | All | what3words location codes |
| **LICENSE_PLATE** | en, de, fr, es, tr, ar | Vehicle registration plates |

### Financial & Banking (6 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **CREDIT_CARD** | All | Credit card numbers (Luhn-validated) |
| **BANK_ACCOUNT** | All | Bank account numbers + IBAN/BIC codes |
| **ROUTING_NUMBER** | en, de | Bank routing numbers (ABA, BLZ) |
| **ACCOUNT_NUMBER** | All | Generic account numbers |
| **PAYMENT_TOKEN** | All | Payment gateway tokens |
| **CRYPTO_ADDRESS** | All | Bitcoin, Ethereum, crypto wallet addresses |

### Government & Tax IDs (9 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **TAX_ID** | en, de, fr, es, tr | Tax ID, VAT number, NIF, Steuer-ID |
| **EORI** | en, de, fr, es | European customs registration numbers |
| **COMMERCIAL_REGISTER** | en, de, fr | Company registration numbers (HRB, SIREN, etc.) |
| **CASE_REFERENCE** | en, de, fr, es | Court/legal case reference numbers |
| **BUND_ID** | de | German federal admin ID |
| **ELSTER_ID** | de | German tax office ID |
| **SERVICEKONTO** | de | German service account number |

### Healthcare & Medical (4 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **HEALTH_ID** | All | Health insurance IDs, NHS numbers |
| **MRN** | All | Medical Record Numbers |
| **INSURANCE_ID** | All | Insurance policy numbers |
| **HEALTH_INFO** | All | Medical conditions, symptoms, diagnoses |

### Education & Employment (4 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **STUDENT_NUMBER** | en, de, fr, es, tr | Student/matriculation IDs |
| **EMPLOYEE_ID** | en, de, fr, es, tr | Employee/staff numbers |
| **PRO_LICENSE** | en, de, fr, es | Professional licenses (bar, medical) |

### Communication & Social (3 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **SOCIAL_HANDLE** | All | Social media usernames/handles |
| **MESSAGING_ID** | All | Chat/messaging IDs, Telegram/WhatsApp |
| **MEETING_ID** | All | Zoom/Teams/Meet room IDs |

### Device & Technical (4 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **MAC_ADDRESS** | All | MAC/hardware addresses |
| **IMEI** | All | device International Mobile Equipment Identifiers |
| **DEVICE_ID** | All | Device identifiers (UDIDs, etc.) |
| **IP_ADDRESS** | All | IPv4 and IPv6 addresses |
| **ADVERTISING_ID** | All | Google Ads/Apple IDFA identifiers |

### Secrets & Tokens (8 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **API_KEY** | All | API keys, tokens, secrets |
| **SESSION_ID** | All | Session tokens, cookies |
| **ACCESS_TOKEN** | All | OAuth, JWT, bearer tokens |
| **REFRESH_TOKEN** | All | Refresh tokens for auth flows |
| **ACCESS_CODE** | All | OTP/2FA codes, access codes |
| **OTP_CODE** | All | One-time passwords |
| **PASSWORD** | All | Passwords (pattern-based detection) |
| **PIN** | All | PIN codes |
| **TAN** | All | Transaction Authentication Numbers |
| **PUK** | All | Phone SIM PUK codes |
| **RECOVERY_CODE** | All | Account recovery/backup codes |

### Administrative & System (3 entities)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **FILE_NUMBER** | All | File/dossier reference numbers |
| **TRANSACTION_NUMBER** | All | Transaction IDs, order numbers |
| **CUSTOMER_NUMBER** | All | Customer/account reference IDs |
| **TICKET_ID** | All | Support ticket, issue, or case IDs |

### Date & Time (1 entity)
| Entity | Languages | Description |
|--------|-----------|-------------|
| **DATE** | en, de, fr, es, ar | Dates in multiple formats (DD.MM.YYYY, MM/DD/YYYY, etc.) |

---

## Language Support

The filter detects text language automatically or can be set manually. Supported languages:

| Language | Code | Entity Coverage | Notes |
|----------|------|-----------------|-------|
| English | `en` | Full (60+ entities) | Default; extensive pattern library |
| German | `de` | Full + specialized | German street types, postal codes, GovIDs |
| French | `fr` | Full | French address formats, tax IDs |
| Spanish | `es` | Full | Spanish address/phone formats |
| Turkish | `tr` | Full | Turkish character support, phone formats |
| Arabic | `ar` | Full | Right-to-left text, Arabic numerals |
| Italian | `it` | Partial | Basic patterns |
| Portuguese | `pt` | Partial | Basic patterns |
| Czech | `cs` | Partial | Basic patterns |

---

## Usage Examples

### Basic Detection & Anonymization

```python
from pii_filter import PIIFilter

# Initialize filter
pii = PIIFilter()

# Detect PII in German text
text = "Hallo, ich bin Max Mustermann. Meine Email ist max@example.de"
results = pii.detect(text, language='de')
for entity in results:
    print(f"{entity['entity_type']}: {text[entity['start']:entity['end']]}")

# Anonymize the text
anonymized = pii.anonymize(text, language='de')
print(anonymized)
# Output: "Hallo, ich bin <PERSON>. Meine Email ist <EMAIL_ADDRESS>"
```

### Run with CLI

```bash
# Scan a text string
python -c "from pii_filter import PIIFilter; pii = PIIFilter(); print(pii.anonymize('Name: John Smith, Email: john@example.com'))"

# Run main test runner
python main_runner.py
```

---

## Scripts Overview

### 1. `main_runner.py` – Test Corpus & Entity Demonstration

**Purpose:** Run the PII filter end-to-end on a multilingual test corpus and generate a comprehensive demonstration report.

**What It Does:**
- Initializes `PIIFilter` with the full pattern library
- Processes **100+ test texts** across **9+ languages** and **multiple PII categories**:
  - English, German (a lot of variants), French, Spanish, Turkish, Arabic, Italian, Portuguese
  - Financial, Crypto, Healthcare, E-Government, Auth Secrets, Communication, Device IDs, Addresses, etc.
- For each text:
  1. **Detects** all PII entities
  2. **Anonymizes** the text (replaces entities with `<ENTITY_TYPE>` tokens)
  3. Displays side-by-side: original input → anonymized output
- Generates **entity coverage report** (total detections per entity type across all texts)
- Outputs a detailed markdown report: `entity_demonstration_report.md`

**Output Files:**
- `entity_demonstration_report.md` 
  - Grouped by entity type and language
  - Shows original/anonymized text examples
  - Coverage statistics for each entity

**Run:**
```bash
python main_runner.py
```


---

### 2. `run_tests.py` – Main Test Runner

**Purpose:** Execute the entire unit test suite and report results.

**What It Does:**
- Runs all test files in `tests/unit/` with pytest
- Executes test cases covering:
  - Entity coverage validation 
  - False positive filtering
  - Language-specific behavior
  - Overlap resolution logic
  - Person detection guards
  - API key/token patterns
  - Address parsing edge cases
  - ID and tax number patterns
  - Validators and guards
- Provides verbose output showing pass/fail per test
- Returns clear exit codes (0 = all pass, 1 = some failed)

**Test Files Included:**
- `test_entity_coverage.py` – Entity detection validation
- `test_api_keys.py` – Secret/token patterns
- `test_false_positives.py` – Guard logic validation
- `test_guards.py` – People/address guard rules
- `test_ids_tax.py` – ID and tax number patterns
- `test_overlap_resolution.py` – Entity merging logic
- `test_person_logic.py` – Name detection heuristics
- `test_reference_identifiers.py` – Reference ID patterns
- `test_tokens.py` – Authentication token patterns
- `test_validators.py` – Standalone validator functions

**Run:**
```bash
python run_tests.py
```

**Example Output:**
```
================================================================================
Running ALL Unit Tests from tests/unit/...
================================================================================

tests/unit/test_regex_patterns.py .......................................... [100%]
tests/unit/test_entity_coverage.py ...................................... [ 95%]
...

=================== tests passed ====================
```

**Interpreting Results:**
- `.` = test passed
- `F` = test failed
- `s` = test skipped
- `E` = error during test execution

---

### 3. `test_runner_simple.py` – Per-File Report Generator

**Purpose:** Run tests file-by-file and generate a detailed markdown summary report.

**What It Does:**
- Runs each `tests/unit/test_*.py` **individually**
- Collects per-file statistics:
  - Passed count
  - Failed count
  - Skipped count
- Aggregates to generate overall stats
- **Extracts failed test names** and module info
- Writes detailed report: `TEST_REPORT_SUMMARY.md`

**Output File:** `TEST_REPORT_SUMMARY.md`
- Provides pass/fail counts per test file
- Aggregates overall statistics
- Identifies failed test names for debugging

**Run:**
```bash
python test_runner_simple.py
```

**When to Use:**
- After making changes to quickly identify problem areas
- Generating reports for debugging

---

## Project Structure

```
PII_Filter/
├── run_tests.py                 # Main test runner (execute all tests)
├── main_runner.py               # Multilingual test corpus & demo report
├── test_runner_simple.py        # Per-file test reporter

├── requirements.txt             # Python dependencies
├── pytest.ini                   # Pytest configuration
│
├── PII_filter/                  # Package directory
│   ├── __init__.py
│   └── pii_filter.py            # Core PIIFilter class (2800+ lines)
│
├── tests/                       # Unit tests
│   ├── conftest.py
│   ├── unit/                    # Test files
│   │   ├── test_entity_coverage.py       (126 tests)
│   │   ├── test_api_keys.py
│   │   ├── test_false_positives.py
│   │   ├── test_guards.py
│   │   ├── test_ids_tax.py
│   │   ├── test_overlap_resolution.py
│   │   ├── test_person_logic.py
│   │   ├── test_reference_identifiers.py
│   │   ├── test_tokens.py
│   │   └── test_validators.py
│   ├── benchmarks/              # Performance benchmarks
│   ├── corpora/                 # Test data (JSON)
│   │   ├── ar/, de/, en/, es/, it/, nl/, tr/
│   │   └── mixed/, noise/
│   └── integration/             # Integration tests
│
├── scripts/                     # Analysis & debugging utilities
│   ├── addr_check.py
│   ├── analyze_base.py
│   ├── check_addresses.py
│   ├── id_match.py
│   └── ... (20+ analysis tools)
│
└── Documentation
    ├── README.md                (this file)
    ├── entity_demonstration_report.md   (auto-generated)
    └── TEST_REPORT_SUMMARY.md           (auto-generated)
```

---

## Dependencies

```
presidio-analyzer>=2.1.0
presidio-anonymizer>=2.1.0
langdetect>=1.0.9
regex>=2023.0.0
spacy>=3.5.0 (optional, for advanced NER)
pytest>=9.0.0 (for testing)
Faker>=18.0.0 (for test data generation)
hypothesis>=6.0.0 (for property-based testing)
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Quick Start

### 1. Basic Detection
```python
from pii_filter import PIIFilter

pii = PIIFilter()
text = "Call me at +1-555-123-4567 or john@example.com"
results = pii.detect(text)
print(results)
# [{'entity_type': 'PHONE_NUMBER', ...}, {'entity_type': 'EMAIL_ADDRESS', ...}]
```

### 2. Anonymize Text
```python
anonymized = pii.anonymize(text)
print(anonymized)
# "Call me at <PHONE_NUMBER> or <EMAIL_ADDRESS>"
```

### 3. Language-Specific Detection
```python
german_text = "Meine Nummer: 030-123456, Adresse: Berliner Str. 15"
pii.set_language('de')
results = pii.detect(german_text)
```

### 4. Run Full Test Suite
```bash
python run_tests.py
```

### 5. Generate Demo Report
```bash
python main_runner.py
```

### 6. Get Per-File Test Report
```bash
python test_runner_simple.py
cat TEST_REPORT_SUMMARY.md
```

---

## Configuration & Customization

### Set Detection Language
```python
pii.set_language('de')  # German
pii.set_language('fr')  # French
pii.set_language('en')  # English (default)
```

### Add Custom False Positive Samples
```python
pii = PIIFilter(
    person_false_positive_samples=[
        "Hello", "World", "Example", "Mr. Test"
    ]
)
```

## Testing & Quality Assurance

**Run all tests:**
```bash
python run_tests.py
```

**Run specific test file:**
```bash
python -m pytest tests/unit/test_entity_coverage.py -v
```

**Run with coverage:**
```bash
python -m pytest tests/unit/ --cov=pii_filter
```

**Generate test report:**
```bash
python test_runner_simple.py
```

---

## License & Contributing

This project uses open-source libraries (Presidio, spaCy, langdetect). Contributions welcome—please run full test suite before submitting PRs.

---
---
## Support

For issues, improvements, or questions:
1. Run `python test_runner_simple.py` to identify failing tests
2. Review test output in `TEST_REPORT_SUMMARY.md`
3. Check `pii_filter.py` for entity pattern definitions
4. Review entity coverage with `python main_runner.py`
---
---