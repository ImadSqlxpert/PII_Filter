import pytest
from pii_filter.pii_filter import PIIFilter


@pytest.fixture(scope="module")
def f():
    return PIIFilter()


# -----------------------------
# Luhn (Credit card validator)
# -----------------------------
def test_luhn_valid(f):
    # Valid Visa test number
    assert f._luhn_ok("4111111111111111") is True
    # Valid Mastercard
    assert f._luhn_ok("5555555555554444") is True


def test_luhn_invalid(f):
    assert f._luhn_ok("4111111111111121") is False
    assert f._luhn_ok("notdigits") is False
    assert f._luhn_ok("12345") is False


# -----------------------------
# IBAN mod97 validation
# -----------------------------
def test_iban_valid(f):
    assert f._iban_ok("DE89 3704 0044 0532 0130 00") is True
    assert f._iban_ok("GB82 WEST 1234 5698 7654 32") is True
    assert f._iban_ok("FR14 2004 1010 0505 0001 3M02 606") is True


def test_iban_invalid(f):
    assert f._iban_ok("DE89 3704 0044 0532 0130 01") is False  # wrong checksum
    assert f._iban_ok("XX123456") is False
    assert f._iban_ok("DE8937040044053201300X") is False  # bad character


# -----------------------------
# ABA Routing (US)
# -----------------------------
def test_aba_valid(f):
    assert f._aba_ok("011000015") is True   # real Bank of America routing number


def test_aba_invalid(f):
    assert f._aba_ok("011000016") is False
    assert f._aba_ok("123") is False
    assert f._aba_ok("abcdefgh9") is False


# -----------------------------
# IMEI (Luhn 15-digit)
# -----------------------------
def test_imei_valid(f):
    assert f._imei_luhn_ok("490154203237518") is True  # GSMA test IMEI


def test_imei_invalid(f):
    assert f._imei_luhn_ok("490154203237519") is False
    assert f._imei_luhn_ok("123456789") is False
    assert f._imei_luhn_ok("abc") is False


# -----------------------------
# NHS number checksum
# -----------------------------
def test_nhs_valid(f):
    # Example of synthetically valid NHS number:
    # 943 476 5919 is known valid
    assert f._nhs_ok("9434765919") is True


def test_nhs_invalid(f):
    assert f._nhs_ok("9434765918") is False
    assert f._nhs_ok("1234") is False
    assert f._nhs_ok("abcdefghij") is False


# -----------------------------
# Coordinates
# -----------------------------
def test_geo_bounds_valid(f):
    assert f._geo_in_bounds(51.5, -0.1) is True  # London
    assert f._geo_in_bounds(-33.9, 151.2) is True  # Sydney


def test_geo_bounds_invalid(f):
    assert f._geo_in_bounds(95.0, 10.0) is False
    assert f._geo_in_bounds(45.0, 200.0) is False
    assert f._geo_in_bounds(-91.0, 0.0) is False
