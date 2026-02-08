import re
import pytest
from pii_filter import PIIFilter


@pytest.fixture(scope="module")
def f():
    return PIIFilter()


# -----------------------------
# Strict address regex tests
# -----------------------------
@pytest.mark.parametrize("text", [
    "123 Main Street",
    "Hauptstraße 5",
    "Rue de la Paix 12",
    "Calle Mayor 10",
    "Fatih mahallesi No:25",
    "شارع الملك فيصل 20",
])
def test_address_regex_positive(f, text):
    assert f.STRICT_ADDRESS_RX.search(text), f"Should match: {text}"



@pytest.mark.parametrize("text", [
    "Random text without patterns",
    "Company policy document",
    "John likes pizza on weekends",
    "Lorem ipsum dolor sit amet",
])
def test_address_pipeline_negative_with_guards(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert "<ADDRESS>" not in out, f"Guarded pipeline should not produce ADDRESS for: {text}"

# -----------------------------
# Postal code regex tests
# -----------------------------
@pytest.mark.parametrize("text", [
    "10115 Berlin",
    "75008 Paris",
    "28013 Madrid",
    "00144 Roma",
    "W1A 1AA",              # UK
    "75008 PARIS",          # uppercase
])
def test_postal_regex_positive(f, text):
    assert any(re.search(p, text, flags=re.I) for p in f.POSTAL_EU_PATTERNS), f"Should match: {text}"



@pytest.mark.parametrize("text", [
    "A1B 2C3 Toronto",             # Canada
    "90210-1234 Beverly Hills",    # US ZIP+4
    "150-0001 Tokyo",              # Japan
    "01001-000 São Paulo",         # Brazil CEP
])
def test_postal_pipeline_negative_with_guards(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert "<LOCATION>" not in out, f"Non‑EU postal should not become LOCATION: {text}"
    
# -----------------------------
# Phone number regex tests
# -----------------------------
@pytest.mark.parametrize("text", [
    "+49 151 23456789",
    "+1 (555) 123-4567",
    "0555-1234567",
    "+971 55 123 4567"
])
def test_phone_regex_positive(f, text):
    assert f.PHONE_RX.search(text), f"Should match: {text}"


@pytest.mark.parametrize("text", [
    "12345",            # too short
    "abc-def-ghij",     # letters
    "room 123",         # not a phone
])
def test_phone_regex_negative(f, text):
    assert not f.PHONE_RX.search(text), f"Should NOT match: {text}"


# -----------------------------
# Date regex tests
# -----------------------------
@pytest.mark.parametrize("text", [
    "12/10/2023",
    "12-10-2023",
    "2023-10-12",
    "12 October 2023",
    "12 Okt 2023",
])
def test_date_regex_positive(f, text):
    found = (
        re.search(f.DATE_REGEX_1, text) or
        re.search(f.DATE_REGEX_2, text) or
        re.search(f.DATE_REGEX_3, text)
    )
    assert found, f"Should match: {text}"


@pytest.mark.parametrize("text", [
    "123456",            # ambiguous
    "yesterday",         # not a date
    "12/2023",           # incomplete
])
def test_date_regex_negative(f, text):
    found = (
        re.search(f.DATE_REGEX_1, text) or
        re.search(f.DATE_REGEX_2, text) or
        re.search(f.DATE_REGEX_3, text)
    )
    assert not found, f"Should NOT match: {text}"

# -----------------------------
# Health info tests
# -----------------------------
@pytest.mark.parametrize("text", [
    "Diagnosed with diabetes",
    "Blood type: O+",
])
def test_health_info_positive(f, text):
    out = f.anonymize_text(text)
    assert "<HEALTH_INFO>" in out, f"Should detect health info: {text}"


# -----------------------------
# Commercial Register (Handelsregister) tests — Multilingual European support
# Tests for: German, French, Spanish, Italian, Dutch
# Covers: Register Court + Division A/B + optional register numbers
# -----------------------------

@pytest.mark.parametrize("text", [
    # German variations
    "Amtsgericht München, Handelsregister B 123456",
    "Registergericht Dresden, Abteilung B, HRB 234567",
    "Das Unternehmen ist eingetragen im Handelsregister beim Amtsgericht München, Abteilung B, HRA 345678.",
    
    # French variations
    "Tribunal de Commerce Paris, Registre B 567890",
    "RCS Paris B 678901",
    
    # Spanish variations
    "Registro Mercantil Madrid, Sección B 890123",
    "Reg. Merc. Barcelona, Secc. A 901234",
    "La sociedad está inscrita en el Registro Mercantil de Madrid, sección B, número 012345.",
    
    # Italian variations
    "Registro delle Imprese Roma, Sezione B 123456",
    "REA Roma 234567",
    "L'impresa è iscritta nel Registro delle Imprese di Roma, sezione B, numero 345678.",
    
    # Dutch variations
    "Handelsregister Amsterdam, Afdeling B 456789",
    "KVK Amsterdam 567890",
    "Het bedrijf staat ingeschreven in het Handelsregister van Amsterdam, afdeling B, nummer 678901.",
])
def test_commercial_register_regex_positive(f, text):
    """Test COMMERCIAL_REGISTER regex matches valid commercial register entries across all languages."""
    assert f.COMMERCIAL_REGISTER_RX.search(text), f"Should match commercial register: {text}"


@pytest.mark.parametrize("text", [
    "Random business text",
    "Company ABC 123",
    "Division B of the company",
    "12345678",  # just numbers, no register context
    "Paris Section B",  # missing RCS keyword
])
def test_commercial_register_regex_negative(f, text):
    """Test COMMERCIAL_REGISTER regex doesn't match invalid patterns."""
    assert not f.COMMERCIAL_REGISTER_RX.search(text), f"Should NOT match: {text}"


@pytest.mark.parametrize("text,expected_in_output", [
    ("Amtsgericht München, Handelsregister B 123456", "<COMMERCIAL_REGISTER>"),
    ("Registergericht Dresden, Abteilung B, HRB 234567", "<COMMERCIAL_REGISTER>"),
    ("RCS Paris B 678901", "<COMMERCIAL_REGISTER>"),
    ("Registro Mercantil Madrid, Sección B 890123", "<COMMERCIAL_REGISTER>"),
    ("Registro delle Imprese Roma, Sezione B 123456", "<COMMERCIAL_REGISTER>"),
    ("Handelsregister Amsterdam, Afdeling B 456789", "<COMMERCIAL_REGISTER>"),
])
def test_commercial_register_anonymization(f, text, expected_in_output):
    """Test COMMERCIAL_REGISTER entities are properly anonymized."""
    out = f.anonymize_text(text)
    assert expected_in_output in out, f"Should anonymize and contain {expected_in_output}: {text}"


def test_commercial_register_german_court_variants():
    """Test German commercial register court name variations."""
    f = PIIFilter()
    
    german_entries = [
        "Amtsgericht Hamburg, Handelsregister A 123456",
        "Registergericht Köln, Abteilung B, HRA 999999",
    ]
    
    for text in german_entries:
        out = f.anonymize_text(text)
        # Should detect and anonymize
        assert "<COMMERCIAL_REGISTER>" in out, f"Should anonymize German register: {text}"


def test_commercial_register_language_coverage():
    """Test all 5 languages are covered."""
    f = PIIFilter()
    
    test_cases = {
        "German": "Amtsgericht München, Handelsregister B 123456",
        "French": "Tribunal de Commerce Paris, Registre B 567890",
        "Spanish": "Registro Mercantil Madrid, Sección B 890123",
        "Italian": "Registro delle Imprese Roma, Sezione B 123456",
        "Dutch": "Handelsregister Amsterdam, Afdeling B 456789",
    }
    
    for language, text in test_cases.items():
        out = f.anonymize_text(text)
        assert "<COMMERCIAL_REGISTER>" in out, f"Should detect {language} commercial register: {text}"


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
    assert "<EMAIL>" in out, "Should also detect email"
    assert "<TAX_ID>" in out, "VAT ID should be detected and anonymized"


# ----------------------------
# Case Reference tests — Multilingual Support
# Tests for: English, German, French, Spanish, Italian, Turkish, Arabic
# Covers: Case ID, Reference Number, Ticket ID, Customer Number, Aktenzeichen, etc.
# ----------------------------

@pytest.mark.parametrize("text", [
    # English variations
    "Case ID: CASE-2023-001234",
    "Reference Number: REF-2024-567890",
    "Ticket ID: TKT-2024-999",
    "Customer Number: CUST-2023-55555",
    
    # German variations
    "Aktenzeichen: AZ-2023-123456",
    "Vorgangsnummer: VN-2024-789012",
    "Kundennummer: KN-2023-456789",
    
    # French
    "Numéro de dossier: ND-2024-001",
    "Dossier #DOSS-2023-999",
    
    # Spanish
    "Número de expediente: EXP-2023-999",
    "Expediente #EXP-2024-111",
    
    # Italian
    "Numero pratica: PR-2024-555",
    "Pratica #PRT-2023-222",
    
    # Turkish
    "Dosya numarası: DN-2023-777",
    "Dosya #DOS-2024-333",
    
    # Arabic
    "رقم القضية: RQ-2024-333",
    "رقم القضية #RQ-2023-444",
])
def test_case_reference_regex_positive(f, text):
    """Test CASE_REFERENCE regex matches valid case/reference identifiers across all languages."""
    assert f.CASE_REFERENCE_RX.search(text), f"Should match case reference: {text}"


@pytest.mark.parametrize("text", [
    "Random case text",
    "123456789",  # just numbers, no case context
    "case of the missing letter",
    "reference book",
    "ticket sales event",
])
def test_case_reference_regex_negative(f, text):
    """Test CASE_REFERENCE regex doesn't match invalid patterns."""
    assert not f.CASE_REFERENCE_RX.search(text), f"Should NOT match: {text}"


@pytest.mark.parametrize("text,expected_in_output", [
    ("Case ID: CASE-2023-001234", "<CASE_REFERENCE>"),
    ("Reference Number: REF-2024-567890", "<CASE_REFERENCE>"),
    ("Aktenzeichen: AZ-2023-123456", "<CASE_REFERENCE>"),
    ("Numéro de dossier: ND-2024-001", "<CASE_REFERENCE>"),
    ("Número de expediente: EXP-2023-999", "<CASE_REFERENCE>"),
    ("Numero pratica: PR-2024-555", "<CASE_REFERENCE>"),
    ("Dosya numarası: DN-2023-777", "<CASE_REFERENCE>"),
    ("رقم القضية: RQ-2024-333", "<CASE_REFERENCE>"),
])
def test_case_reference_anonymization(f, text, expected_in_output):
    """Test CASE_REFERENCE entities are properly anonymized."""
    out = f.anonymize_text(text)
    assert expected_in_output in out, f"Should anonymize and contain {expected_in_output}: {text}"


def test_case_reference_language_coverage():
    """Test all 8 languages are covered."""
    f = PIIFilter()
    
    test_cases = {
        "English": "Case ID: CASE-2023-001234",
        "German": "Aktenzeichen: AZ-2023-123456",
        "French": "Numéro de dossier: ND-2024-001",
        "Spanish": "Número de expediente: EXP-2023-999",
        "Italian": "Numero pratica: PR-2024-555",
        "Turkish": "Dosya numarası: DN-2023-777",
        "Arabic": "رقم القضية: RQ-2024-333",
    }
    
    for language, text in test_cases.items():
        out = f.anonymize_text(text)
        assert "<CASE_REFERENCE>" in out, f"Should detect {language} case reference: {text}"


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
    assert "<EMAIL>" in out, "Should detect email"


def test_case_reference_no_conflict_with_phone():
    """Test CASE_REFERENCE doesn't conflict with PHONE_NUMBER detection."""
    f = PIIFilter()
    
    # Case reference with numbers that could look like phone
    document = "Case ID: 123-456-7890 is not a phone number"
    out = f.anonymize_text(document)
    assert "<CASE_REFERENCE>" in out, "Should detect case reference format"


def test_case_reference_no_conflict_with_date():
    """Test CASE_REFERENCE doesn't conflict with DATE detection."""
    f = PIIFilter()
    
    # Case reference with numbers that could look like date
    document = "Reference Number: 2024-12-15 was opened"
    out = f.anonymize_text(document)
    assert "<CASE_REFERENCE>" in out, "Should detect case reference format"


# ----------------------------
# German E-Government ID tests
# Covers: BundID, ELSTER_ID, SERVICEKONTO
# ----------------------------

@pytest.mark.parametrize("text", [
    # BundID variations
    "BundID: BUND-12345678-ABCD",
    "Bundidentität BUND-87654321-WXYZ",
    "Bundesausweis-ID: BUND-11111111-1111",
    "Digital Identity: BUND-99999999-ZYXW",
    
    # ELSTER variations
    "ELSTER-ID: ELST-12345",
    "ELSTER Login: elster_user_12345",
    "ELSTER-Benutzername: user.name@example",
    "elster_konto_abcd1234",
    
    # Servicekonto variations
    "Servicekonto-ID: SK-2024-001234",
    "Service-Konto: servicekonto_56789",
    "Service Account: SK-2025-009876",
    "Servicekonto: 123456789",
    "Konto-ID: account_gov_12345",
])
def test_german_gov_id_regex_positive(f, text):
    """Test German e-government ID regex matches valid identifiers."""
    match_found = bool(f.BUND_ID_RX.search(text) or f.ELSTER_ID_RX.search(text) or f.SERVICEKONTO_RX.search(text))
    assert match_found, f"Should match German gov ID: {text}"


@pytest.mark.parametrize("text", [
    "Random government text",
    "Bundle of sticks",
    "Service at the counter",
    "ELSTER is a good name",  # word without labels
    "123456789",  # just numbers
    "SK SKate",  # letters without pattern
])
def test_german_gov_id_regex_negative(f, text):
    """Test German e-government ID regex doesn't match invalid patterns."""
    match_found = bool(f.BUND_ID_RX.search(text) or f.ELSTER_ID_RX.search(text) or f.SERVICEKONTO_RX.search(text))
    assert not match_found, f"Should NOT match: {text}"


@pytest.mark.parametrize("text,expected_entity", [
    ("BundID: BUND-12345678-ABCD", "<BUND_ID>"),
    ("ELSTER-ID: ELST-12345", "<ELSTER_ID>"),
    ("Servicekonto-ID: SK-2024-001234", "<SERVICEKONTO>"),
    ("ELSTER Login: elster_user_12345", "<ELSTER_ID>"),
    ("Service-Konto: servicekonto_56789", "<SERVICEKONTO>"),
])
def test_german_gov_id_anonymization(f, text, expected_entity):
    """Test German e-government IDs are properly anonymized."""
    out = f.anonymize_text(text)
    assert expected_entity in out, f"Should anonymize and contain {expected_entity}: {text}"


def test_bundid_variations():
    """Test BundID detection across format variations."""
    f = PIIFilter()
    
    bundid_examples = [
        "BundID: BUND-12345678-ABCD",
        "Bundidentität: BUND-87654321-WXYZ",
        "Digital Identity BUND-11111111-1111",
    ]
    
    for text in bundid_examples:
        out = f.anonymize_text(text)
        assert "<BUND_ID>" in out, f"Should detect BundID: {text}"


def test_elster_variations():
    """Test ELSTER_ID detection across format variations."""
    f = PIIFilter()
    
    elster_examples = [
        "ELSTER-ID: ELST-12345",
        "ELSTER Login: elster_user_12345",
        "ELSTER-Benutzername: user.name",
        "elster_konto_abcd1234",
    ]
    
    for text in elster_examples:
        out = f.anonymize_text(text)
        assert "<ELSTER_ID>" in out, f"Should detect ELSTER_ID: {text}"


def test_servicekonto_variations():
    """Test SERVICEKONTO detection across format variations."""
    f = PIIFilter()
    
    servicekonto_examples = [
        "Servicekonto-ID: SK-2024-001234",
        "Service-Konto: servicekonto_56789",
        "Servicekonto: 123456789",
    ]
    
    for text in servicekonto_examples:
        out = f.anonymize_text(text)
        assert "<SERVICEKONTO>" in out, f"Should detect SERVICEKONTO: {text}"


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
    assert "<EMAIL>" in out, "Should detect email"


def test_german_gov_ids_no_false_positives():
    """Test German e-government ID detection avoids false positives."""
    f = PIIFilter()
    
    # These should not match
    false_positive_texts = [
        "The service is going well",
        "Bundle package arrived",
        "ELSTER is mounted on the wall",
        "Service desk hours: 9-5",
    ]
    
    for text in false_positive_texts:
        out = f.anonymize_text(text)
        # Should not have any of the German gov IDs marked
        assert "<BUND_ID>" not in out, f"False positive for BUND_ID: {text}"
        assert "<ELSTER_ID>" not in out, f"False positive for ELSTER_ID: {text}"
        assert "<SERVICEKONTO>" not in out, f"False positive for SERVICEKONTO: {text}"


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
    assert "<PHONE>" in out, "Should detect phone"
    assert "<EMAIL>" in out, "Should detect email"
