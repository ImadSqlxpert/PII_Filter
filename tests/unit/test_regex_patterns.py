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