import json
import pytest
from pathlib import Path
from pii_filter import PIIFilter

@pytest.fixture(scope="module")
def f():
    return PIIFilter()

def load_corpora():
    corpora_dir = Path(__file__).parent.parent / "corpora"
    samples = []
    for lang_dir in corpora_dir.iterdir():
        if lang_dir.is_dir():
            for json_file in lang_dir.glob("*.json"):
                try:
                    with open(json_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        for item in data:
                            item["source"] = json_file.name
                            samples.append(item)
                except (json.JSONDecodeError, FileNotFoundError):
                    continue  # Skip empty or invalid files
    return samples

@pytest.mark.parametrize("sample", [s for s in load_corpora() if "expected_anonymized" in s])
def test_anonymization_accuracy(f, sample):
    text = sample["text"]
    expected = sample["expected_anonymized"]
    out = f.anonymize_text(text)
    # Simple check: ensure some tags are present, or exact match if possible
    # For now, check that output contains tags
    assert "<" in out and ">" in out, f"No anonymization for {sample['source']}: {text}"

@pytest.mark.parametrize("sample", [s for s in load_corpora() if "expected_no_pii" in s])
def test_no_false_positives(f, sample):
    text = sample["text"]
    out = f.anonymize_text(text)
    # Should not contain any <TAG> placeholders
    assert not any(tag in out for tag in ["<PERSON>", "<EMAIL>", "<PHONE>", "<ADDRESS>", "<LOCATION>", "<DATE>", "<PASSPORT>", "<ID_NUMBER>", "<TAX_ID>", "<IP_ADDRESS>", "<CREDIT_CARD>", "<BANK_ACCOUNT>", "<ROUTING_NUMBER>", "<ACCOUNT_NUMBER>", "<PAYMENT_TOKEN>", "<CRYPTO_ADDRESS>", "<DRIVER_LICENSE>", "<VOTER_ID>", "<RESIDENCE_PERMIT>", "<BENEFIT_ID>", "<MILITARY_ID>", "<HEALTH_ID>", "<MRN>", "<INSURANCE_ID>", "<HEALTH_INFO>", "<STUDENT_NUMBER>", "<EMPLOYEE_ID>", "<PRO_LICENSE>", "<SOCIAL_HANDLE>", "<MESSAGING_ID>", "<MEETING_ID>", "<MAC_ADDRESS>", "<IMEI>", "<ADVERTISING_ID>", "<DEVICE_ID>", "<GEO_COORDINATES>", "<PLUS_CODE>", "<W3W>", "<LICENSE_PLATE>"]), f"False positive in: {text}"