import sys
from pathlib import Path
import re
import pytest

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from pii_filter.pii_filter import PIIFilter


# -------------------------
# Helpers
# -------------------------

@pytest.fixture
def f():
    return PIIFilter()

def has_tag(out: str, tag: str) -> bool:
    return f"<{tag}>" in out

def count_tag(out: str, tag: str) -> int:
    return out.count(f"<{tag}>")

def contains_any_tag(out: str, tags: set[str]) -> bool:
    return any(f"<{t}>" in out for t in tags)

def no_other_tags_than(out: str, allowed: set[str]) -> bool:
    # True if all <...> tags present are within the allowed set
    others = set(m.group(1) for m in re.finditer(r"<([A-Z_]+)>", out))
    return others.issubset(allowed)

# Keep these handy
PERSON = "PERSON"
ADDRESS = "ADDRESS"
LOCATION = "LOCATION"

# For non-regression quick checks
NON_PERSON_ADDRESS_ENTITIES = {
    "PHONE_NUMBER", "DATE", "ID_NUMBER", "PASSPORT", "TAX_ID",
    "BANK_ACCOUNT", "CREDIT_CARD", "IP_ADDRESS", "MAC_ADDRESS",
    "API_KEY", "PAYMENT_TOKEN", "CRYPTO_ADDRESS", "DEVICE_ID"
}


# ============================================================
# EN — Chat: Intro cues should yield PERSON
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: Hi, my name is John Doe\nBot: Nice to meet you, John!",
    "User: hey there, I'm Sarah Connor\nAgent: Hi Sarah, how can I help?",
    "User: I am called Mike\nSupport: Hello Mike 👋",
])
def test_en_chat_person_intro(f, chat):
    out = f.anonymize_text(chat)
    assert has_tag(out, PERSON), out
    # Don’t accidentally tag an address here
    assert not has_tag(out, ADDRESS), out


# ============================================================
# DE — Chat: Intro cues should yield PERSON
# ============================================================

@pytest.mark.parametrize("chat", [
    "Kunde: Mein Name ist Anna Müller\nBot: Hallo Anna!",
    "User: Ich heiße Lukas Bauer\nBerater: Wie kann ich helfen?",
    "Kunde: Ich bin Paul Meier\nBot: Hallo Paul! 😊",
])
def test_de_chat_person_intro(f, chat):
    out = f.anonymize_text(chat)
    assert has_tag(out, PERSON), out
    assert not has_tag(out, ADDRESS), out


# ============================================================
# EN/DE — Chat: Sharing an address explicitly (true positives)
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: My address is 221B Baker Street, NW1 6XE London",
    "User: Shipping address: Main Street 42, 12345 Sampletown",
    "Kunde: Meine Adresse ist Hauptstraße 5, 10115 Berlin",
    "Kunde: Lieferadresse: Goethestraße 10\n80331 München",
    "User: Send to Am Stadtpark 3, 20095 Hamburg",
])
def test_chat_address_true_positives(f, chat):
    out = f.anonymize_text(chat)
    assert has_tag(out, ADDRESS), out
    # Don’t mis-tag address as PERSON
    assert not has_tag(out, PERSON), out


# ============================================================
# EN/DE — Chat: City mentions or postal+city should NOT become ADDRESS
#   (LOCATION is allowed; ADDRESS should not appear)
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: I am in Berlin today",
    "User: Let’s meet in Munich",
    "Kunde: Ich bin in Hamburg unterwegs",
    "Kunde: 10115 Berlin (nur PLZ+Stadt)",
])
def test_chat_city_or_postal_city_not_address(f, chat):
    out = f.anonymize_text(chat)
    assert not has_tag(out, ADDRESS), out
    # It’s fine if LOCATION is detected (optional)
    # We won’t assert LOCATION strictly to avoid over-constraining different configs.


# ============================================================
# EN/DE — Chat: Single street words or labels shouldn’t be PERSON/ADDRESS
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: Straße",
    "User: Weg",
    "User: Gasse",
    "User: Allee",
    "User: ADDRESS:",
    "Kunde: RECHNUNG",
    "Kunde: KUNDENNUMMER",
])
def test_chat_single_tokens_not_person_or_address(f, chat):
    out = f.anonymize_text(chat)
    assert not has_tag(out, PERSON), out
    assert not has_tag(out, ADDRESS), out


# ============================================================
# EN/DE — Chat: Avoid ADDRESS inside email/URL fragments
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: adresse: max.mustermann@example.com",
    "User: Address: https://maps.example.com/Hauptstrasse",
    "Kunde: Meine Adresse ist in meinem Profil: https://portal.example.de/user/paul",
])
def test_chat_no_address_in_email_or_url(f, chat):
    out = f.anonymize_text(chat)
    assert not has_tag(out, ADDRESS), out


# ============================================================
# EN/DE — Chat: Mixed lines with timestamps and speakers
# ============================================================

def test_chat_mixed_timestamps_speakers(f):
    chat = (
        "[10:31] Anna: Ich heiße Anna Müller\n"
        "[10:32] Bot: Bitte nenne deine Adresse.\n"
        "[10:33] Anna: Hauptstraße 10, 10115 Berlin\n"
    )
    out = f.anonymize_text(chat)
    assert has_tag(out, PERSON), out
    assert has_tag(out, ADDRESS), out
    # Don’t flood with unrelated entities
    assert no_other_tags_than(out, {PERSON, ADDRESS, LOCATION}), out


# ============================================================
# EN — Chat edge: Ask for address but don’t mis-detect on the request line
# ============================================================

def test_en_chat_request_no_address(f):
    chat = "Agent: Please provide your postal address\nUser: Sure, I will type it next"
    out = f.anonymize_text(chat)
    assert not has_tag(out, ADDRESS), out


# ============================================================
# DE — Chat edge: “Ich bin in …” with location should not be PERSON
# ============================================================

@pytest.mark.parametrize("chat", [
    "Kunde: Ich bin in München im Urlaub",
    "User: Ich bin in Berlin, kein Name",
])
def test_de_chat_ich_bin_location_not_person(f, chat):
    out = f.anonymize_text(chat)
    assert not has_tag(out, PERSON), out


# ============================================================
# EN/DE — Chat: Partial address spread across lines (should still detect)
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin",
    "User: Street: Baker St.\nNumber: 221B\nCity: London",
])
def test_chat_partial_address_across_lines(f, chat):
    out = f.anonymize_text(chat)
    assert has_tag(out, ADDRESS), out


# ============================================================
# EN — Chat: Username mentions, tickets, codes should not become PERSON/ADDRESS
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: my handle is @john_doe and ticket is ABC-12345",
    "Support: refer to case #987654; user is @sarah-c",
    "User: send it to @max (not an address)",
])
def test_en_chat_handles_tickets_not_person_address(f, chat):
    out = f.anonymize_text(chat)
    assert not has_tag(out, PERSON), out
    assert not has_tag(out, ADDRESS), out


# ============================================================
# EN/DE — Chat: “Send to Baker Street?” without number is NOT an ADDRESS
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: Can you send it to Baker Street?",
    "Kunde: Kannst du es zur Goethestraße schicken?",
])
def test_chat_street_without_number_not_address(f, chat):
    out = f.anonymize_text(chat)
    assert not has_tag(out, ADDRESS), out


# ============================================================
# EN/DE — Chat: Valid address abbreviations should still be caught
# ============================================================

@pytest.mark.parametrize("chat", [
    "User: Send to Hauptstr. 5, 10115 Berlin",
    "User: Shipping to Main St. 10, 90210 Beverly Hills",
    "User: Deliver to 10 Downing St, SW1A 2AA London",
])
def test_chat_address_abbreviations_true_positive(f, chat):
    out = f.anonymize_text(chat)
    assert has_tag(out, ADDRESS), out


# ============================================================
# Sanity: Non-regression quick sweep (no changes to other entities)
# ============================================================

@pytest.mark.parametrize("chat, expected", [
    ("Call me at +49 30 1234567", "PHONE_NUMBER"),
    ("I was born on March 15, 1985", "DATE"),
    ("SSN: 123-45-6789", "ID_NUMBER"),
    ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token", "ACCESS_TOKEN"),
    ("sk-proj-1234567890abcdefghijklmnop", "API_KEY"),
    ("tok_abc123def456ghi789xyz", "PAYMENT_TOKEN"),
    ("MAC AA:BB:CC:DD:EE:FF", "MAC_ADDRESS"),
    ("IP: 192.168.1.1", "IP_ADDRESS"),
])
def test_non_regression_other_entities_in_chat(f, chat, expected):
    out = f.anonymize_text(chat)
    assert has_tag(out, expected), out
    # Ensure PERSON/ADDRESS aren’t spuriously added here
    assert not contains_any_tag(out, {PERSON, ADDRESS}), out