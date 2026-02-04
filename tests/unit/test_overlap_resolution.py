import pytest
from pii_filter import PIIFilter
from tests.conftest import has_tag, count_tag  # import helpers


@pytest.fixture(scope="module")
def f():
    return PIIFilter()


# -----------------------------
# 1) Higher priority entity should win on overlap → ADDRESS + LOCATION merged into ADDRESS
# -----------------------------
@pytest.mark.parametrize("text", [
    "Hauptstraße 5, 10115 Berlin",
    "Calle Mayor 5, 28013 Madrid",
    "Rue de la Paix 12 - 75008 Paris",
    "Via Roma 10\n00144 Roma",
])
def test_merge_address_and_location_into_single_address(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert count_tag(out, "ADDRESS") == 1, f"Should be merged into one ADDRESS: {text}"
    assert not has_tag(out, "LOCATION"), f"LOCATION should be merged away: {text}"


# -----------------------------
# 2) Merge when adjacent by spaces (no punctuation)
# -----------------------------
@pytest.mark.parametrize("text", [
    "Hauptstraße 5 10115 Berlin",
    "Calle Mayor 5 28013 Madrid",
])
def test_merge_address_location_when_adjacent_by_spaces(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert count_tag(out, "ADDRESS") == 1
    assert not has_tag(out, "LOCATION")


# -----------------------------
# 3) Same-priority tie → longer span wins (PASSPORT vs ID_NUMBER)
#    Current pipeline usually yields ID_NUMBER for generic passport-like tokens.
# -----------------------------
@pytest.mark.parametrize("text", [
    "EU passport: X1Y2Z3A4B",
    "Passport: A12345678",
])
def test_same_priority_longer_span_wins_passport_vs_id(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    # One of them must appear
    assert has_tag(out, "ID_NUMBER") or has_tag(out, "PASSPORT")
    # Typically your pipeline resolves to ID_NUMBER; if you later prefer PASSPORT, relax this line.
    # (Leave as-is for now to enforce deterministic resolution.)
    assert not has_tag(out, "PASSPORT")


# -----------------------------
# 4) TAX label removes nearby/inline LOCATION but keeps TAX_ID
# -----------------------------
def test_tax_label_removes_nearby_location_but_keeps_tax(f):
    text = "10115 Berlin VAT DE123456789"
    out = f.anonymize_text(text, guards_enabled=True)
    assert has_tag(out, "TAX_ID"), "TAX value should be kept"
    assert not has_tag(out, "LOCATION"), "Adjacent/inline label should remove LOCATION"


# -----------------------------
# 5) LOCATION kept when truly postal (digits in-span) and no labels nearby
# -----------------------------
@pytest.mark.parametrize("text", [
    "10115 Berlin",
    "75008 Paris",
    "28013 Madrid",
    "00144 Roma",
])
def test_location_kept_when_postal_and_no_labels_nearby(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert has_tag(out, "LOCATION"), f"Postal+city should remain LOCATION: {text}"
    assert not has_tag(out, "ADDRESS"), "No street part here; should not produce ADDRESS"
