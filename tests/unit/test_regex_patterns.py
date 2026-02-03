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