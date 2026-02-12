import re
import pytest
from pii_filter.pii_filter import PIIFilter

@pytest.fixture(scope="module")
def f():
    return PIIFilter()


# -----------------------------
# PASSPORT (generic)
# -----------------------------
@pytest.mark.parametrize("text", [
    "US passport: A12345678",
    "EU passport: X1Y2Z3A4B",
])
def test_passport_positive(f, text):
    out = f.anonymize_text(text)
    assert "<PASSPORT>" in out or "<ID_NUMBER>" in out


@pytest.mark.parametrize("text", [
    "PASS port",  # not a number pattern
    "passport holder",  # noun phrase only
])
def test_passport_negative_pipeline(f, text):
    out = f.anonymize_text(text)
    assert "<PASSPORT>" not in out


# -----------------------------
# National IDs (format-level)
# -----------------------------
@pytest.mark.parametrize("text", [
    "UK NINO: AB 12 34 56 C",   # UK NINO 
    "ES DNI: 12345678Z",        # Spain DNI
    "ES NIE: X1234567L",        # Spain NIE
    "IT CF: RSSMRA85M01H501Z",  # Italian Codice Fiscale (example)
    "NL BSN: 123456782",        # NL BSN (example 9 digits; not checksum validated here)
    "PL PESEL: 02070803628",    # Example PESEL
    "SE personnummer: 850709-9805",  # Swedish
    "NO fødselsnummer: 01010101006", # Norwegian FNR
    "FI HETU: 131052-308T",          # Finnish HETU
])
def test_id_number_positive(f, text):
    out = f.anonymize_text(text)
    assert "<ID_NUMBER>" in out


@pytest.mark.parametrize("text", [
    "employee id: ABCDE",      # too short/alpha only
    "dni",                      # label only
    "personal number: policy",  # word noise
])
def test_id_number_negative_pipeline(f, text):
    out = f.anonymize_text(text)
    assert "<ID_NUMBER>" not in out


# -----------------------------
# VAT / TAX IDs (strict patterns)
# -----------------------------
@pytest.mark.parametrize("text", [
    "DE VAT: DE123456789",
    "FR VAT: FR12345678901",
    "IT VAT: IT12345678901",
    "ES VAT: ESX1234567L",
    "NL VAT: NL123456789B01",
    "PL NIP (tax): PL1234567890",
    "RO VAT: RO12345678",
    "SE VAT: SE123456789001",
    "GB VAT: GB123456789",
    "CH VAT: CHE123456789MWST",
])
def test_vat_tax_positive(f, text):
    out = f.anonymize_text(text)
    assert "<TAX_ID>" in out


@pytest.mark.parametrize("text", [
    "VAT",                # label without value
    "TIN abcdef",         # alpha only
    "SIREN 1234",         # too short
    "random 123456",      # ambiguous digits
])
def test_vat_tax_negative_pipeline(f, text):
    out = f.anonymize_text(text)
    assert "<TAX_ID>" not in out