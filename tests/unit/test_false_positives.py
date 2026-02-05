import pytest
from pii_filter import PIIFilter

@pytest.fixture
def f():
    return PIIFilter()

cases = [
    # (input, expected substring in anonymized output)
    ("I live at 221B Baker Street, London.", "<ADDRESS>"),
    ("Meine E-Mail ist max.mustermann@beispiel.de und ich wohne in der Musterstraße 5, 10115 Berlin.", "<EMAIL>"),
    ("Ich will Gewerbe anmelden.", "Gewerbe"),
    ("IMEI 490154203237518", "<IMEI>"),
    ("My device IMEI is 490154203237518", "<IMEI>"),
    ("Diagnosed with diabetes.", "<HEALTH_INFO>"),
    ("Visa 4111 1111 1111 1111", "<CREDIT_CARD>"),
    ("My name is John Smith", "<PERSON>"),
]

@pytest.mark.parametrize("text,expected", cases)
def test_false_positives(f, text, expected):
    out = f.anonymize_text(text)
    assert expected in out, f"Expected {expected} in anonymized output for: {text}; got: {out}"
