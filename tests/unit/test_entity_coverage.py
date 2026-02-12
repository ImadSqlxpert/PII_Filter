import pytest
from pii_filter.pii_filter import PIIFilter

@pytest.fixture
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
    ("ADDRESS", "1600 Pennsylvania Avenue NW, Washington, DC 20500", "<ADDRESS>"),
    ("ADDRESS", "Via Roma 10, 00100 Roma, Italy", "<ADDRESS>"),
    ("ADDRESS", "123 Main St, Apt 4B, New York, NY 10001", "<ADDRESS>"),
    ("ADDRESS", "Carrer de la Pau 1, 08002 Barcelona, Spain", "<ADDRESS>"),
    ("ADDRESS", "ул. Тверская 15, Москва 125009, Россия", "<ADDRESS>"),
    ("ADDRESS", "Musterstraße 10, Whg. 5, 01067 Dresden", "<ADDRESS>"),
    ("ADDRESS", "Atatürk Caddesi No:15, Ankara, Turkey", "<ADDRESS>"),
    ("ADDRESS", "Am Waldrand 12, 50667 Köln", "<ADDRESS>"),
    ("ADDRESS", "Unter den Linden 77, 10117 Berlin", "<ADDRESS>"),
    ("ADDRESS", "Gänsemarkt 2, 20354 Hamburg", "<ADDRESS>"),

    # LOCATION
    ("LOCATION", "10115 Berlin", "<LOCATION>"),  # Use postal to avoid strict filter
    ("LOCATION", "75008 Paris", "<LOCATION>"),
    ("LOCATION", "28013 Madrid", "<LOCATION>"),

    # DATE
    ("DATE", "Born on 12/31/1990", "<DATE>"),
    ("DATE", "Geburtstag 31.12.1990", "<DATE>"),
    ("DATE", "Né le 31-05-1995", "<DATE>"),

    # PASSPORT
    ("PASSPORT", "US Passport: A12345678", "<PASSPORT>"),  # Detected as PASSPORT
    ("PASSPORT", "EU Passport: X1Y2Z3A4B", "<ID_NUMBER>"),

    # ID_NUMBER
    ("ID_NUMBER", "ID: 12345678Z", "<ID_NUMBER>"),
    ("ID_NUMBER", "Personalausweis: T22000129", "<PASSPORT>"),

    # TAX_ID
    ("TAX_ID", "VAT: DE123456789", "<TAX_ID>"),
    ("TAX_ID", "Steuer-ID: 12 345 678 901", "<TAX_ID>"),

    # IP_ADDRESS
    ("IP_ADDRESS", "Server IP: 192.168.1.10", "<IP_ADDRESS>"),
    ("IP_ADDRESS", "IPv6: 2001:db8::1", "<IP_ADDRESS>"),

    # CREDIT_CARD
    ("CREDIT_CARD", "Card: 4111 1111 1111 1111", "<CREDIT_CARD>"),
    ("CREDIT_CARD", "Amex 371449635398431", "<CREDIT_CARD>"),  # Amex should be CREDIT_CARD, not IMEI

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

    # Chatbot query-style positive tests (government official page scenarios)
    ("PERSON", "Hello, my name is Jane Smith", "<PERSON>"),
    ("ADDRESS", "I need to update my address to 456 Elm Street, Springfield", "<ADDRESS>"),
    ("DATE", "I was born on March 15, 1985", "<DATE>"),
    ("EMAIL_ADDRESS", "You can contact me at jane.smith@gmail.com", "<EMAIL>"),
    ("PHONE_NUMBER", "Call me at +1 555-123-4567", "<PHONE>"),
    ("ID_NUMBER", "My social security number is 123-45-6789", "<ID_NUMBER>"),
    ("PASSPORT", "My passport number is X1234567", "<PASSPORT>"),
    ("BANK_ACCOUNT", "My IBAN is DE12345678901234567890", "<BANK_ACCOUNT>"),
    ("CREDIT_CARD", "My credit card is 4111 1111 1111 1111", "<CREDIT_CARD>"),
    ("HEALTH_INFO", "I have diabetes and need medical assistance", "<HEALTH_INFO>"),
    ("SOCIAL_HANDLE", "Follow me on Twitter @jane_smith", "<SOCIAL_HANDLE>"),
    ("LICENSE_PLATE", "My license plate is ABC-123", "<LICENSE_PLATE>"),
    ("IP_ADDRESS", "My IP address is 192.168.1.1", "<IP_ADDRESS>"),
    ("GEO_COORDINATES", "My location is 40.7128, -74.0060", "<GEO_COORDINATES>"),
    ("MEETING_ID", "Join my meeting at 123 456 789", "<MEETING_ID>"),
    ("PAYMENT_TOKEN", "My API key is sk_live_abc123def456", "<PAYMENT_TOKEN>"),
    ("CRYPTO_ADDRESS", "Send to BTC address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "<CRYPTO_ADDRESS>"),
    ("TAX_ID", "My tax ID is 12-3456789", "<TAX_ID>"),
    ("ACCOUNT_NUMBER", "My account number is 1234567890", "<ACCOUNT_NUMBER>"),
    ("ROUTING_NUMBER", "My routing number is 021000021", "<ROUTING_NUMBER>"),
    ("MAC_ADDRESS", "My MAC address is 00:1A:2B:3C:4D:5E", "<MAC_ADDRESS>"),
    ("IMEI", "My device IMEI is 490154203237518", "<IMEI>"),
    ("ADVERTISING_ID", "My IDFA is 123e4567-e89b-12d3-a456-426614174000", "<ADVERTISING_ID>"),
    ("PLUS_CODE", "Meet me at 9G8F+5W New York", "<PLUS_CODE>"),
    ("MESSAGING_ID", "My Discord is jane#1234", "<MESSAGING_ID>"),
    ("FAX_NUMBER", "My fax number is +1 555-123-4568", "<FAX>"),
    ("MRN", "My medical record number is ABC-123456", "<MRN>"),
    ("INSURANCE_ID", "My insurance policy is POL-987654321", "<INSURANCE_ID>"),
    ("STUDENT_NUMBER", "My student ID is STU-12345", "<STUDENT_NUMBER>"),
    ("EMPLOYEE_ID", "My employee number is EMP-67890", "<EMPLOYEE_ID>"),
    ("PRO_LICENSE", "My professional license is LIC-54321", "<PRO_LICENSE>"),
    ("HEALTH_ID", "My NHS number is 943 476 5919", "<HEALTH_ID>"),
    ("DRIVER_LICENSE", "My driver's license is D1234567", "<DRIVER_LICENSE>"),
    ("VOTER_ID", "My voter ID is V9876543", "<VOTER_ID>"),
    ("RESIDENCE_PERMIT", "My residence permit is RP456789", "<RESIDENCE_PERMIT>"),
    ("BENEFIT_ID", "My benefit card is B11223344", "<BENEFIT_ID>"),
    ("MILITARY_ID", "My military ID is M55667788", "<MILITARY_ID>"),
    ("DEVICE_ID", "My device ID is DEV-999888777", "<DEVICE_ID>"),

    # German chatbot query-style positive tests (government official page scenarios)
    ("PERSON", "Hallo, mein Name ist Max Müller", "<PERSON>"),
    ("ADDRESS", "Ich muss meine Adresse auf Hauptstraße 10, Berlin ändern", "<ADDRESS>"),
    ("DATE", "Ich bin am 15. März 1985 geboren", "<DATE>"),
    ("EMAIL_ADDRESS", "Sie können mich unter max.mueller@example.de erreichen", "<EMAIL>"),
    ("PHONE_NUMBER", "Rufen Sie mich unter +49 123 456789 an", "<PHONE>"),
    ("ID_NUMBER", "Meine Sozialversicherungsnummer ist 123-45-6789", "<ID_NUMBER>"),
    ("PASSPORT", "Meine Passnummer ist X1234567", "<PASSPORT>"),
    ("BANK_ACCOUNT", "Meine IBAN ist DE12345678901234567890", "<BANK_ACCOUNT>"),
    ("CREDIT_CARD", "Meine Kreditkarte ist 4111 1111 1111 1111", "<CREDIT_CARD>"),
    ("HEALTH_INFO", "Ich habe Diabetes und brauche medizinische Hilfe", "<HEALTH_INFO>"),
    ("SOCIAL_HANDLE", "Folgen Sie mir auf Twitter @max_mueller", "<SOCIAL_HANDLE>"),
    ("LICENSE_PLATE", "Mein Kennzeichen ist B-AB 1234", "<LICENSE_PLATE>"),
    ("IP_ADDRESS", "Meine IP-Adresse ist 192.168.1.1", "<IP_ADDRESS>"),
    ("GEO_COORDINATES", "Mein Standort ist 52.5200, 13.4050", "<GEO_COORDINATES>"),
    ("MEETING_ID", "Treten Sie meinem Meeting bei unter 123 456 789", "<MEETING_ID>"),
    ("PAYMENT_TOKEN", "Mein API-Schlüssel ist sk_live_abc123def456", "<PAYMENT_TOKEN>"),
    ("CRYPTO_ADDRESS", "Senden Sie an BTC-Adresse 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "<CRYPTO_ADDRESS>"),
    ("TAX_ID", "Meine Steuer-ID ist 12-3456789", "<TAX_ID>"),
    ("ACCOUNT_NUMBER", "Meine Kontonummer ist 1234567890", "<ACCOUNT_NUMBER>"),
    ("ROUTING_NUMBER", "Meine Bankleitzahl ist 021000021", "<ROUTING_NUMBER>"),
    ("MAC_ADDRESS", "Meine MAC-Adresse ist 00:1A:2B:3C:4D:5E", "<MAC_ADDRESS>"),
    ("IMEI", "Die IMEI meines Geräts ist 490154203237518", "<IMEI>"),
    ("ADVERTISING_ID", "Meine IDFA ist 123e4567-e89b-12d3-a456-426614174000", "<ADVERTISING_ID>"),
    ("PLUS_CODE", "Treffen wir uns bei 9G8F+5W Berlin", "<PLUS_CODE>"),
    ("MESSAGING_ID", "Mein Discord ist max#1234", "<MESSAGING_ID>"),
    ("FAX_NUMBER", "Meine Faxnummer ist +49 30 1234567", "<FAX>"),
    ("MRN", "Meine Krankenaktennummer ist ABC-123456", "<MRN>"),
    ("INSURANCE_ID", "Meine Versicherungspolice ist POL-987654321", "<INSURANCE_ID>"),
    ("STUDENT_NUMBER", "Meine Studentenausweisnummer ist STU-12345", "<STUDENT_NUMBER>"),
    ("EMPLOYEE_ID", "Meine Mitarbeiternummer ist EMP-67890", "<EMPLOYEE_ID>"),
    ("PRO_LICENSE", "Meine Berufslizenz ist LIC-54321", "<PRO_LICENSE>"),
    ("HEALTH_ID", "Meine NHS-Nummer ist 943 476 5919", "<HEALTH_ID>"),
    ("DRIVER_LICENSE", "Mein Führerschein ist D1234567", "<DRIVER_LICENSE>"),
    ("VOTER_ID", "Meine Wählerausweisnummer ist V9876543", "<VOTER_ID>"),
    ("RESIDENCE_PERMIT", "Meine Aufenthaltsgenehmigung ist RP456789", "<RESIDENCE_PERMIT>"),
    ("BENEFIT_ID", "Meine Sozialhilfekarte ist B11223344", "<BENEFIT_ID>"),
    ("MILITARY_ID", "Meine Militärausweis ist M55667788", "<MILITARY_ID>"),
    ("DEVICE_ID", "Meine Geräte-ID ist DEV-999888777", "<DEVICE_ID>"),

    # Add more as needed for other entities
]

@pytest.mark.parametrize("entity,text,expected", entity_samples)
def test_entity_coverage(f, entity, text, expected):
    out = f.anonymize_text(text)
    assert expected in out, f"Failed to detect {entity} in: {text}"

# Test cases for PERSON false positives (should NOT detect PERSON)
person_false_positive_samples = [
    "Ich wohne in Müritzsee.",  # Lake name
    "Meine Adresse: Schwabental",  # Valley name
    "Ich heiße Anna Gasse.",  # Name + street suffix
    "Koordinaten: 52.5200, 13.4050",  # Coordinates label
    "Personalausweisnummer: T22000129",  # ID label
    "Ruf mich unter 12-03-2023 an.",  # "Call me"
    "ولدت في 31/12/1990.",  # "I was born" in Arabic
    "Diagnosed with diabetes.",  # Health context
    "Blood type: O+",  # Health info
    "Fax: +49 30 1234567",  # Fax label
    "Meeting ID: 987 654 321",  # Meeting label
    "MAC 00:1A:2B:3C:4D:5E",  # Device label
    "IMEI 490154203237518",  # Device label
    "IDFA: 123e4567-e89b-12d3-a456-426614174000",  # Device label
    "Kennzeichen: B-AB 1234",  # License plate label
    "Plus Code: 9C3W9QCJ+2V",  # Geo label
    "w3w: ///index.home.raft",  # Geo label
    "Twitter @john_doe123",  # Social handle
    "Discord user#1234",  # Messaging ID
    "Visa 4111 1111 1111 1111",  # Payment label
    "IBAN: DE44 5001 0517 5407 3249 31",  # Bank label
    "BTC: 1BoatSLRHtKNngkdXEeobR76b53LETtpyT",  # Crypto label
    "ETH: 0x52908400098527886e0f7030069857d2e4169ee7",  # Crypto label
    "NHS number 943 476 5919",  # Health ID label
    "MRN: ABC-123456",  # MRN label
    "Insurance policy: POL-987654321",  # Insurance label
    "API key: sk_live_abcDEF1234567890",  # Payment token
    "Stripe pub: pk_test_1xYzABC1234567890",  # Payment token
    "Kontonummer: 1234-567890-12",  # Account number
    "Steuer-ID: 12 345 678 901",  # Tax ID
    "USt-IdNr.: DE 123456789",  # Tax ID
    "SSN: 536-80-4398",  # ID
    "ITIN: 912-91-3457",  # ID
    "EIN: 51-2144346",  # ID
    "VAT: ES X1234567T",  # Tax ID
    "Routing (ABA): 021000021",  # Routing number
    "BIC: COBADEFFXXX",  # Bank account
    # Additional capitalized words that might be false positives
    "Apple",  # Company name
    "Google",  # Company name
    "Microsoft",  # Company name
    "Facebook",  # Company name
    "Amazon",  # Company name
    "Berlin",  # City name (LOCATION, but test PERSON)
    "London",  # City name
    "Paris",  # City name
    "München",  # City name in German
    "Hamburg",  # City name
    "Computer",  # Common noun
    "Science",  # Common noun
    "Machine",  # Common noun
    "Learning",  # Common noun
    "Das Haus",  # German capitalized noun
    "Der Baum",  # German capitalized noun
    "Die Stadt",  # German capitalized noun
    # Additional normal words and phrases that could potentially affect bot logic if misclassified
    "Doctor",  # Common title, not a name
    "President",  # Title, not a name
    "Professor",  # Title, not a name
    "Manager",  # Job title, not a name
    "Engineer",  # Job title, not a name
    "January",  # Month name, not part of date
    "February",  # Month name
    "March",  # Month name
    "April",  # Month name
    "Street",  # Common address component
    "Avenue",  # Common address component
    "Road",  # Common address component
    "Boulevard",  # Common address component
    "Park",  # Common location word
    "Lake",  # Common location word
    "River",  # Common location word
    "Mountain",  # Common location word
    "Company",  # Business term
    "Corporation",  # Business term
    "University",  # Institution
    "School",  # Institution
    "Hospital",  # Institution
    "Bank",  # Institution
    "Library",  # Institution
    "Airport",  # Location
    "Station",  # Location
    "Center",  # Common word
    "Building",  # Common word
    "Office",  # Common word
    "Department",  # Common word
    "Service",  # Common word
    "System",  # Common word
    "Program",  # Common word
    "Project",  # Common word
    "Report",  # Common word
    "Document",  # Common word
    "File",  # Common word
    "Data",  # Common word
    "Information",  # Common word
    "Request",  # Common word
    "Application",  # Common word
    "Form",  # Common word
    "Process",  # Common word
    "Status",  # Common word
    "Update",  # Common word
    "Change",  # Common word
    "Help",  # Common word
    "Support",  # Common word
    "Contact",  # Common word
    "Question",  # Common word
    "Answer",  # Common word
    "Issue",  # Common word
    "Problem",  # Common word
    "Solution",  # Common word
    "Thank you",  # Common phrase
    "Please",  # Common word
    "Hello",  # Common greeting
    "Goodbye",  # Common farewell
    "Yes",  # Common affirmation
    "No",  # Common negation
    "Okay",  # Common agreement
    "Maybe",  # Common uncertainty
    "Sorry",  # Common apology
    "Excuse me",  # Common phrase
    "I need",  # Common phrase
    "I want",  # Common phrase
    "Can you",  # Common phrase
    "How do I",  # Common phrase
    "What is",  # Common phrase
    "Where is",  # Common phrase
    "When is",  # Common phrase
    "Why is",  # Common phrase
    "Who is",  # Common phrase
    "Which",  # Common word
    "That",  # Common word
    "This",  # Common word
    "Here",  # Common word
    "There",  # Common word
    "Now",  # Common word
    "Then",  # Common word
    "Today",  # Common word
    "Tomorrow",  # Common word
    "Yesterday",  # Common word
    "Monday",  # Day of week
    "Tuesday",  # Day of week
    "Wednesday",  # Day of week
    "Thursday",  # Day of week
    "Friday",  # Day of week
    "Saturday",  # Day of week
    "Sunday",  # Day of week
    "Morning",  # Time of day
    "Afternoon",  # Time of day
    "Evening",  # Time of day
    "Night",  # Time of day
    "Early",  # Common adverb
    "Late",  # Common adverb
    "Fast",  # Common adjective
    "Slow",  # Common adjective
    "Good",  # Common adjective
    "Bad",  # Common adjective
    "Big",  # Common adjective
    "Small",  # Common adjective
    "New",  # Common adjective
    "Old",  # Common adjective
    "Hot",  # Common adjective
    "Cold",  # Common adjective
    "High",  # Common adjective
    "Low",  # Common adjective
    "Right",  # Common adjective/direction
    "Left",  # Common adjective/direction
    "Up",  # Common direction
    "Down",  # Common direction
    "In",  # Common preposition
    "Out",  # Common preposition
    "On",  # Common preposition
    "Off",  # Common preposition
    "At",  # Common preposition
    "By",  # Common preposition
    "For",  # Common preposition
    "With",  # Common preposition
    "From",  # Common preposition
    "To",  # Common preposition
    "Of",  # Common preposition
    "As",  # Common preposition
    "And",  # Common conjunction
    "Or",  # Common conjunction
    "But",  # Common conjunction
    "If",  # Common conjunction
    "Then",  # Common conjunction
    "Because",  # Common conjunction
    "So",  # Common conjunction
    "Although",  # Common conjunction
    "While",  # Common conjunction
    "Since",  # Common conjunction
    "Until",  # Common conjunction
    "Before",  # Common conjunction
    "After",  # Common conjunction
    "During",  # Common conjunction
    "Through",  # Common preposition
    "Over",  # Common preposition
    "Under",  # Common preposition
    "Above",  # Common preposition
    "Below",  # Common preposition
    "Between",  # Common preposition
    "Among",  # Common preposition
    "Within",  # Common preposition
    "Without",  # Common preposition
    "Against",  # Common preposition
    "Towards",  # Common preposition
    "Into",  # Common preposition
    "Onto",  # Common preposition
    "Upon",  # Common preposition
    "About",  # Common preposition
    "Across",  # Common preposition
    "Along",  # Common preposition
    "Around",  # Common preposition
    "Behind",  # Common preposition
    "Beside",  # Common preposition
    "Besides",  # Common preposition
    "Near",  # Common preposition
    "Next",  # Common preposition
    "Past",  # Common preposition
    "Round",  # Common preposition
    "Since",  # Common preposition
    "Through",  # Common preposition
    "Throughout",  # Common preposition
    "Till",  # Common preposition
    "Toward",  # Common preposition
    "Underneath",  # Common preposition
    "Until",  # Common preposition
    "Unto",  # Common preposition
    "Upon",  # Common preposition
    "With",  # Common preposition
    "Within",  # Common preposition
    "Without",  # Common preposition
    # German normal words and phrases that could affect bot logic
    "Doktor",  # Title
    "Präsident",  # Title
    "Professor",  # Title
    "Manager",  # Job title
    "Ingenieur",  # Job title
    "Januar",  # Month
    "Februar",  # Month
    "März",  # Month
    "April",  # Month
    "Mai",  # Month
    "Juni",  # Month
    "Juli",  # Month
    "August",  # Month
    "September",  # Month
    "Oktober",  # Month
    "November",  # Month
    "Dezember",  # Month
    "Montag",  # Day
    "Dienstag",  # Day
    "Mittwoch",  # Day
    "Donnerstag",  # Day
    "Freitag",  # Day
    "Samstag",  # Day
    "Sonntag",  # Day
    "Straße",  # Address component
    "Avenue",  # Address component (keep English for mixed)
    "Weg",  # Road
    "Boulevard",  # Boulevard
    "Park",  # Park
    "See",  # Lake
    "Fluss",  # River
    "Berg",  # Mountain
    "Firma",  # Company
    "Korporation",  # Corporation
    "Universität",  # University
    "Schule",  # School
    "Krankenhaus",  # Hospital
    "Bank",  # Bank
    "Bibliothek",  # Library
    "Flughafen",  # Airport
    "Bahnhof",  # Station
    "Zentrum",  # Center
    "Gebäude",  # Building
    "Büro",  # Office
    "Abteilung",  # Department
    "Dienst",  # Service
    "System",  # System
    "Programm",  # Program
    "Projekt",  # Project
    "Bericht",  # Report
    "Dokument",  # Document
    "Datei",  # File
    "Daten",  # Data
    "Information",  # Information
    "Anfrage",  # Request
    "Anwendung",  # Application
    "Formular",  # Form
    "Prozess",  # Process
    "Status",  # Status
    "Aktualisierung",  # Update
    "Änderung",  # Change
    "Hilfe",  # Help
    "Unterstützung",  # Support
    "Kontakt",  # Contact
    "Frage",  # Question
    "Antwort",  # Answer
    "Problem",  # Problem
    "Lösung",  # Solution
    "Danke",  # Thank you
    "Bitte",  # Please
    "Hallo",  # Hello
    "Auf Wiedersehen",  # Goodbye
    "Ja",  # Yes
    "Nein",  # No
    "Okay",  # Okay
    "Vielleicht",  # Maybe
    "Entschuldigung",  # Sorry
    "Entschuldigen Sie",  # Excuse me
    "Ich brauche",  # I need
    "Ich möchte",  # I want
    "Können Sie",  # Can you
    "Wie mache ich",  # How do I
    "Was ist",  # What is
    "Wo ist",  # Where is
    "Wann ist",  # When is
    "Warum ist",  # Why is
    "Wer ist",  # Who is
    "Welcher",  # Which
    "Das",  # That
    "Dies",  # This
    "Hier",  # Here
    "Dort",  # There
    "Jetzt",  # Now
    "Dann",  # Then
    "Heute",  # Today
    "Morgen",  # Tomorrow
    "Gestern",  # Yesterday
    "Morgen",  # Morning
    "Nachmittag",  # Afternoon
    "Abend",  # Evening
    "Nacht",  # Night
    "Früh",  # Early
    "Spät",  # Late
    "Schnell",  # Fast
    "Langsam",  # Slow
    "Gut",  # Good
    "Schlecht",  # Bad
    "Groß",  # Big
    "Klein",  # Small
    "Neu",  # New
    "Alt",  # Old
    "Heiß",  # Hot
    "Kalt",  # Cold
    "Hoch",  # High
    "Niedrig",  # Low
    "Rechts",  # Right
    "Links",  # Left
    "Hoch",  # Up
    "Runter",  # Down
    "In",  # In
    "Aus",  # Out
    "Auf",  # On
    "Aus",  # Off
    "Bei",  # At
    "Von",  # By
    "Für",  # For
    "Mit",  # With
    "Aus",  # From
    "Zu",  # To
    "Von",  # Of
    "Als",  # As
    "Und",  # And
    "Oder",  # Or
    "Aber",  # But
    "Wenn",  # If
    "Dann",  # Then
    "Weil",  # Because
    "Also",  # So
    "Obwohl",  # Although
    "Während",  # While
    "Seit",  # Since
    "Bis",  # Until
    "Vor",  # Before
    "Nach",  # After
    "Während",  # During
    "Durch",  # Through
    "Über",  # Over
    "Unter",  # Under
    "Über",  # Above
    "Unter",  # Below
    "Zwischen",  # Between
    "Unter",  # Among
    "Innerhalb",  # Within
    "Ohne",  # Without
    "Gegen",  # Against
    "Zu",  # Towards
    "In",  # Into
    "Auf",  # Onto
    "Auf",  # Upon
    "Über",  # About
    "Über",  # Across
    "Entlang",  # Along
    "Um",  # Around
    "Hinter",  # Behind
    "Neben",  # Beside
    "Außer",  # Besides
    "Nah",  # Near
    "Nächste",  # Next
    "Vorbei",  # Past
    "Rund",  # Round
    "Seit",  # Since
    "Durch",  # Through
    "Überall",  # Throughout
    "Bis",  # Till
    "Zu",  # Toward
    "Unter",  # Underneath
    "Bis",  # Until
    "Zu",  # Unto
    "Auf",  # Upon
    "Mit",  # With
    "Innerhalb",  # Within
    "Ohne",  # Without
    # German chat-like sentences that should not be detected as PII
    "Hallo, wie geht es dir?",
    "Ich brauche Hilfe.",
    "Was kann ich für Sie tun?",
    "Danke für die Information.",
    "Das ist toll.",
    "Entschuldigung, ich verstehe nicht.",
    "Können Sie mir helfen?",
    "Ja, das klingt gut.",
    "Nein, das passt nicht.",
    "Vielen Dank.",
    "Auf Wiedersehen.",
    "Wie kann ich Ihnen helfen?",
    "Ich habe eine Frage.",
    "Das ist sehr nett.",
    "Guten Tag.",
    "Guten Abend.",
    "Gute Nacht.",
    "Wie bitte?",
    "Entschuldigen Sie die Störung.",
    "Ich bin beschäftigt.",
    "Das macht nichts.",
    "Kein Problem.",
    "Alles klar.",
    "Verstanden.",
    "Ich melde mich später.",
    "Bis bald.",
    "Tschüss.",
    "Auf Wiederhören.",
]

@pytest.mark.parametrize("text", person_false_positive_samples)
def test_person_false_positives(f, text):
    out = f.anonymize_text(text)
    assert "<PERSON>" not in out, f"False positive PERSON detection in: {text}"

# Test cases for ADDRESS false positives (should NOT detect ADDRESS)
address_false_positive_samples = [
    "Main Street",  # Just street name
    "New York",  # Just city
    "Berlin",  # Just city
    "Paris",  # Just city
    "The Empire State Building",  # Building name without address
    "Via Roma",  # Just street
    "Hauptstraße",  # Just street
    "Rue de Rivoli",  # Just street
    "I live on Main Street.",  # Incomplete address
    "My office is in New York.",  # Just city mention
    "The meeting is at Hauptstraße.",  # Just street
    "Visit us in Paris.",  # Just city
    "Street address: Main Street",  # Incomplete
    "City: New York",  # Just city
    "Location: Berlin",  # Just city
    "Address: Paris",  # Just city
    "Building: Empire State",  # Just building
    "Road: Via Roma",  # Just street
    "Avenue: Hauptstraße",  # Just street
    "Boulevard: Rue de Rivoli",  # Just street
    "Müritzsee",  # Lake name
    "Schwabental",  # Valley name
    "Anna Gasse",  # Name
    "Koordinaten: 52.5200, 13.4050",  # Coordinates
    "Plus Code: 9C3W9QCJ+2V",  # Geo code
    "w3w: ///index.home.raft",  # What3Words
    "Kennzeichen: B-AB 1234",  # License plate
]

@pytest.mark.parametrize("text", address_false_positive_samples)
def test_address_false_positives(f, text):
    out = f.anonymize_text(text)
    assert "<ADDRESS>" not in out, f"False positive ADDRESS detection in: {text}"

# Test cases for LOCATION false positives (should NOT detect LOCATION)
location_false_positive_samples = [
    "Top 14",  # Apartment number
    "Stiege 2",  # Staircase number
    "Whg. 5",  # Apartment abbreviation
    "2. Etage",  # Floor number
    "2. OG",  # Floor number (Austrian)
]

@pytest.mark.parametrize("text", location_false_positive_samples)
def test_location_false_positives(f, text):
    out = f.anonymize_text(text)
    assert "<LOCATION>" not in out, f"False positive LOCATION detection in: {text}"