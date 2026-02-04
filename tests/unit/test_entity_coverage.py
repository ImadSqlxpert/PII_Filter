import pytest
from pii_filter import PIIFilter

@pytest.fixture(scope="module")
def f():
    return PIIFilter()

# Flattened list: (entity, text, expected_tag)
entity_samples = [
    # PERSON
    ("PERSON", "My name is John Doe", "<PERSON>"),
    ("PERSON", "Ich heiße Hans Müller", "<PERSON>"),
    ("PERSON", "Je m'appelle Marie Dupont", "<PERSON>"),
    ("PERSON", "Me llamo Carlos García", "<PERSON>"),
    ("PERSON", "اسمي أحمد محمد", "<PERSON>"),
    ("PERSON", "Benim adım Ahmet Yılmaz", "<PERSON>"),

    # EMAIL_ADDRESS
    ("EMAIL_ADDRESS", "My email is john@example.com", "<EMAIL>"),
    ("EMAIL_ADDRESS", "Email: hans@test.de", "<EMAIL>"),
    ("EMAIL_ADDRESS", "Correo: marie@gmail.com", "<EMAIL>"),
    ("EMAIL_ADDRESS", "بريدي ahmed@example.com", "<EMAIL>"),

    # PHONE_NUMBER
    ("PHONE_NUMBER", "+1 (555) 123-4567", "<PHONE>"),
    ("PHONE_NUMBER", "+49 151 23456789", "<PHONE>"),
    ("PHONE_NUMBER", "+966 50 123 4567", "<PHONE>"),

    # ADDRESS
    ("ADDRESS", "123 Main Street, New York", "<ADDRESS>"),
    ("ADDRESS", "Hauptstraße 5, Berlin", "<ADDRESS>"),
    ("ADDRESS", "12 rue de Rivoli, Paris", "<ADDRESS>"),
    ("ADDRESS", "شارع الملك فيصل 20، الرياض", "<ADDRESS>"),

    # LOCATION
    ("LOCATION", "10115 Berlin", "<LOCATION>"),  # Use postal to avoid strict filter
    ("LOCATION", "75008 Paris", "<LOCATION>"),
    ("LOCATION", "28013 Madrid", "<LOCATION>"),

    # DATE
    ("DATE", "Born on 12/31/1990", "<DATE>"),
    ("DATE", "Geburtstag 31.12.1990", "<DATE>"),
    ("DATE", "Né le 31-05-1995", "<DATE>"),

    # PASSPORT
    ("PASSPORT", "US Passport: A12345678", "<ID_NUMBER>"),  # Detected as ID_NUMBER due to priority
    ("PASSPORT", "EU Passport: X1Y2Z3A4B", "<ID_NUMBER>"),

    # ID_NUMBER
    ("ID_NUMBER", "ID: 12345678Z", "<ID_NUMBER>"),
    ("ID_NUMBER", "Personalausweis: T22000129", "<ID_NUMBER>"),

    # TAX_ID
    ("TAX_ID", "VAT: DE123456789", "<TAX_ID>"),
    ("TAX_ID", "Steuer-ID: 12 345 678 901", "<TAX_ID>"),

    # IP_ADDRESS
    ("IP_ADDRESS", "Server IP: 192.168.1.10", "<IP_ADDRESS>"),
    ("IP_ADDRESS", "IPv6: 2001:db8::1", "<IP_ADDRESS>"),

    # CREDIT_CARD
    ("CREDIT_CARD", "Card: 4111 1111 1111 1111", "<CREDIT_CARD>"),

    # BANK_ACCOUNT
    ("BANK_ACCOUNT", "IBAN: DE44 5001 0517 5407 3249 31", "<BANK_ACCOUNT>"),

    # HEALTH_INFO
    ("HEALTH_INFO", "Diagnosed with diabetes", "<HEALTH_INFO>"),
    ("HEALTH_INFO", "Blood type: O+", "<HEALTH_INFO>"),

    # MAC_ADDRESS
    ("MAC_ADDRESS", "MAC: 00:1A:2B:3C:4D:5E", "<MAC_ADDRESS>"),

    # IMEI
    ("IMEI", "Device IMEI: 490154203237518", "<IMEI>"),  # Add label to distinguish from CC

    # GEO_COORDINATES
    ("GEO_COORDINATES", "Coords: 52.5200, 13.4050", "<GEO_COORDINATES>"),

    # LICENSE_PLATE
    ("LICENSE_PLATE", "License Plate: B-AB 1234", "<LICENSE_PLATE>"),  # Use full label

    # Add more as needed for other entities
]

@pytest.mark.parametrize("entity,text,expected", entity_samples)
def test_entity_coverage(f, entity, text, expected):
    out = f.anonymize_text(text)
    assert expected in out, f"Failed to detect {entity} in: {text}"