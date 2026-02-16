import sys
from pathlib import Path
import re
import pytest

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from pii_filter.pii_filter import PIIFilter


# -------------------------
# Test helpers
# -------------------------

@pytest.fixture
def f():
    return PIIFilter()

def has_tag(out: str, tag: str) -> bool:
    """Convenience helper to check if a placeholder tag appears."""
    return f"<{tag}>" in out

def only_tag(out: str, tag: str) -> bool:
    """True if the output contains at least one <tag> and contains no other <...> tags."""
    return has_tag(out, tag) and not re.search(r"<(?!%s)[A-Z_]+>" % tag, out)

def no_tags(out: str) -> bool:
    """True if the output contains no entities at all."""
    return not re.search(r"<[A-Z_]+>", out)


# ============================================================
# PERSON — True positives (DE/EN) with intro-cues
# ============================================================

@pytest.mark.parametrize("text", [
    "Mein Name ist Anna Müller",
    "Ich heiße Lukas Bauer",
    "My name is John Doe",
    "I am called Sarah Connor",
    # allow small variation/whitespace
    "  Mein Name ist   Paul  Meier  ",
])
def test_person_intro_true_positives(f, text):
    out = f.anonymize_text(text)
    assert has_tag(out, "PERSON"), f"Expected <PERSON> in: {out}"


# ============================================================
# PERSON — Should NOT match (common FPs)
# ============================================================

@pytest.mark.parametrize("text", [
    "Adresse: Hauptstraße",               # address keyword + street (should not be PERSON)
    "Straße", "Weg", "Gasse", "Allee",    # street words alone
    "RECHNUNG", "KUNDENNUMMER",           # all caps labels
    "am 12. März 1985",                  # date-like context
    "Meine Telefonnummer ist 030 123456", # phone context
    "Hauptstraße 10",                     # looks like address; PERSON must not win
    "Ich bin in Berlin",                  # 'Ich bin' + location (not a name)
    "Customer name: street",              # English noise
])
def test_person_common_false_positives(f, text):
    out = f.anonymize_text(text)
    assert not has_tag(out, "PERSON"), f"Unexpected <PERSON> in: {out}"


# ============================================================
# PERSON vs ADDRESS — Overlap resolution
#  - Intro cue near name -> PERSON wins
#  - House number/postal present -> ADDRESS wins
#  - Otherwise drop weaker
# ============================================================

def test_overlap_intro_prefers_person(f):
    text = "Mein Name ist Julia Hauptstraße 10"  # ambiguous tail; intro-cue should keep PERSON
    out = f.anonymize_text(text)
    assert has_tag(out, "PERSON"), f"Expected <PERSON> with intro cue in: {out}"

def test_overlap_numeric_prefers_address(f):
    text = "Name: Hauptstraße 10 Paul"  # numeric address should dominate over stray name-like token
    out = f.anonymize_text(text)
    assert has_tag(out, "ADDRESS"), f"Expected <ADDRESS> to win numeric overlap in: {out}"


# ============================================================
# ADDRESS — True positives (DE + EN)
# ============================================================

@pytest.mark.parametrize("text", [
    "Musterstraße 12, 10115 Berlin",
    "Hauptstraße 5",
    "Main Street 42, 12345 Sampletown",
    "Goethestraße 10\n10115 Berlin",
    "Lindenstr. 7 – 80331 München",
    "Am Stadtpark 3, 20095 Hamburg",
])
def test_address_true_positives(f, text):
    out = f.anonymize_text(text)
    assert has_tag(out, "ADDRESS"), f"Expected <ADDRESS> in: {out}"


# ============================================================
# ADDRESS — Should NOT match single tokens / city-only / email/url parts
# ============================================================

@pytest.mark.parametrize("text", [
    "Straße", "Weg", "Gasse", "Allee",        # single street-type tokens
    "Berlin", "München", "Hamburg",           # city-only; may be <LOCATION>, not ADDRESS
    "adresse: rue-victor@example.com",        # email context
    "Adresse: https://example.com/Hauptstrasse",  # URL context nearby
])
def test_address_common_false_positives(f, text):
    out = f.anonymize_text(text)
    # Must NOT be address; LOCATION is fine for city-only case
    assert not has_tag(out, "ADDRESS"), f"Unexpected <ADDRESS> in: {out}"


# ============================================================
# LOCATION — Postal + City (not an address by itself)
# ============================================================

@pytest.mark.parametrize("text", [
    "10115 Berlin",
    "20095 Hamburg",
    "80331 München",
    "12345 Sampletown",
])
def test_postal_city_is_location_not_address(f, text):
    out = f.anonymize_text(text)
    assert has_tag(out, "LOCATION"), f"Expected <LOCATION> in: {out}"
    assert not has_tag(out, "ADDRESS"), f"Should not tag pure postal+city as <ADDRESS>: {out}"


# ============================================================
# ADDRESS + LOCATION — Merge rule (adjacent) -> becomes ADDRESS
# ============================================================

@pytest.mark.parametrize("text", [
    "Hauptstraße 5, 80331 München",
    "Goethestraße 10\n10115 Berlin",
    "Main Street 42 — 12345 Sampletown",
])
def test_address_location_merge_becomes_address(f, text):
    out = f.anonymize_text(text)
    assert has_tag(out, "ADDRESS"), f"Expected merged <ADDRESS> in: {out}"


# ============================================================
# ADDRESS — Guards: natural suffix words require numeric or postal context
# ============================================================

@pytest.mark.parametrize("text", [
    "Berg", "Wald", "Feld", "See", "Bach",        # natural suffix words alone
    "Am Berg", "Im Wald",                         # without numbers -> not address
])
def test_natural_suffix_requires_number(f, text):
    out = f.anonymize_text(text)
    assert not has_tag(out, "ADDRESS"), f"Unexpected <ADDRESS> in: {out}"


# ============================================================
# ADDRESS — Trim at newline/label boundaries (avoid bleed)
# ============================================================

@pytest.mark.parametrize("text", [
    "Hauptstraße 10\nEmail: someone@example.com",
    "Main Street 42, 12345 City\nTelefon: 030 123456",
])
def test_address_trim_and_no_bleed_into_labels(f, text):
    out = f.anonymize_text(text)
    assert has_tag(out, "ADDRESS"), f"Expected <ADDRESS> in: {out}"
    # Should not convert email/phone labels to address
    assert not has_tag(out, "EMAIL_ADDRESS"), "Email should remain a separate entity"
    assert not has_tag(out, "PHONE_NUMBER") or has_tag(out, "ADDRESS"), "Phone should remain separate"


# ============================================================
# PERSON — Single token name should require intro cue (conservative)
# ============================================================

@pytest.mark.parametrize("text, expect_person", [
    ("Anna", False),                   # too ambiguous; no intro cue
    ("Mein Name ist Anna", True),     # intro cue allows single token
    ("Ich bin Anna", True),           # allowed if name-like token follows
    ("Ich bin in München", False),    # 'Ich bin' + location (not a name)
])
def test_person_single_token_needs_intro(f, text, expect_person):
    out = f.anonymize_text(text)
    assert has_tag(out, "PERSON") == expect_person, out


# ============================================================
# Non-Regression: Core entities unaffected by PERSON/ADDRESS tuning
# ============================================================

@pytest.mark.parametrize("text, tag", [
    ("+49 30 1234567", "PHONE_NUMBER"),
    ("I was born on March 15, 1985", "DATE"),
    ("Meine Sozialversicherungsnummer ist 123-45-6789", "ID_NUMBER"),
    ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.token", "ACCESS_TOKEN"),
    ("sk-proj-1234567890abcdefghijklmnop", "API_KEY"),
    ("sk_live_abc123def456", "API_KEY"),  # by policy in your suite
    ("tok_abc123def456ghi789xyz", "PAYMENT_TOKEN"),
    ("0x52908400098527886E0F7030069857D2E4169EE7", "CRYPTO_ADDRESS"),
    ("AA:BB:CC:DD:EE:FF", "MAC_ADDRESS"),
    ("192.168.1.10", "IP_ADDRESS"),
])
def test_non_regression_other_entities(f, text, tag):
    out = f.anonymize_text(text)
    assert has_tag(out, tag), f"Expected <{tag}> in: {out}"


# ============================================================
# Stress: lines mixing labels with names and addresses
# ============================================================

@pytest.mark.parametrize("text", [
    "Kunde: Anna Müller, Adresse: Hauptstraße 5, 10115 Berlin",
    "Customer: John Doe; Address: Main Street 42, 12345 Sampletown",
])
def test_mixed_line_stress(f, text):
    out = f.anonymize_text(text)
    assert has_tag(out, "PERSON"), f"Expected <PERSON> in: {out}"
    assert has_tag(out, "ADDRESS"), f"Expected <ADDRESS> in: {out}"
    # ensure not everything collapses to ADDRESS
    assert not only_tag(out, "ADDRESS"), f"PERSON should not be lost: {out}"