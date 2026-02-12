import json
import pytest
from pathlib import Path
from pii_filter.pii_filter import PIIFilter

@pytest.fixture(scope="module")
def f():
    return PIIFilter()

def load_noise():
    noise_file = Path(__file__).parent.parent / "corpora" / "noise" / "noise.json"
    with open(noise_file, "r", encoding="utf-8") as file:
        return json.load(file)

@pytest.mark.parametrize("sample", load_noise())
def test_no_false_positives(f, sample):
    text = sample["text"]
    out = f.anonymize_text(text)
    # Should not contain any <TAG> placeholders
    assert not any(tag in out for tag in ["<PERSON>", "<EMAIL>", "<PHONE>", "<ADDRESS>", "<LOCATION>", "<DATE>", "<PASSPORT>", "<ID_NUMBER>", "<TAX_ID>", "<IP_ADDRESS>", "<CREDIT_CARD>", "<BANK_ACCOUNT>", "<ROUTING_NUMBER>", "<ACCOUNT_NUMBER>", "<PAYMENT_TOKEN>", "<CRYPTO_ADDRESS>", "<DRIVER_LICENSE>", "<VOTER_ID>", "<RESIDENCE_PERMIT>", "<BENEFIT_ID>", "<MILITARY_ID>", "<HEALTH_ID>", "<MRN>", "<INSURANCE_ID>", "<HEALTH_INFO>", "<STUDENT_NUMBER>", "<EMPLOYEE_ID>", "<PRO_LICENSE>", "<SOCIAL_HANDLE>", "<MESSAGING_ID>", "<MEETING_ID>", "<MAC_ADDRESS>", "<IMEI>", "<ADVERTISING_ID>", "<DEVICE_ID>", "<GEO_COORDINATES>", "<PLUS_CODE>", "<W3W>", "<LICENSE_PLATE>"]), f"False positive in: {text}"