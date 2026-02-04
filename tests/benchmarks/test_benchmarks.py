import pytest
from pii_filter import PIIFilter

@pytest.fixture(scope="module")
def f():
    return PIIFilter()

@pytest.fixture
def large_text():
    # Generate a large text with repeated PII
    base = "My name is John Doe, email john@example.com, phone +1234567890, address 123 Main St, 12345 City."
    return (base + " ") * 100  # Repeat to make large

def test_anonymize_performance(benchmark, f, large_text):
    benchmark(f.anonymize_text, large_text)

def test_entity_detection_performance(benchmark, f, large_text):
    benchmark(f.analyzer.analyze, text=large_text, language="en")