import pytest
from pii_filter import PIIFilter


@pytest.fixture(scope="module")
def f():
    # Use a fresh instance you modified earlier (with STRICT_LOCATION_POSTAL_ONLY = True by default)
    return PIIFilter()


# -----------------------------
# 1) Natural suffix requires number (e.g., Am Wald → must have digits)
# -----------------------------
def test_guard_natural_suffix_requires_number_on_drops(f):
    text = "Am Wald"
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_natural_suffix_requires_number=True,    # ON
        guard_single_token_addresses=False,
        guard_address_vs_person_priority=False,
        guard_requires_context_without_number=False,
    )
    assert "<ADDRESS>" not in out, "Should drop 'Am Wald' without house number when the natural-suffix guard is ON."


def test_guard_natural_suffix_requires_number_off_keeps(f):
    text = "Am Wald"
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_natural_suffix_requires_number=False,   # OFF
        guard_single_token_addresses=False,
        guard_address_vs_person_priority=False,
        guard_requires_context_without_number=False,
    )
    # With other guards off, permissive regex may keep it
    assert "<ADDRESS>" in out, "With guard OFF and other guards disabled, 'Am Wald' may be kept as ADDRESS."


# -----------------------------
# 2) Requires context when no number (no digit → need an address keyword nearby)
# -----------------------------
def test_guard_requires_context_without_number_drops_without_keyword(f):
    text = "Rue Victor Hugo"
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_requires_context_without_number=True,   # ON
        guard_natural_suffix_requires_number=False,
        guard_single_token_addresses=False,
        guard_address_vs_person_priority=False,
    )
    assert "<ADDRESS>" not in out, "No house number and no context → should drop."


def test_guard_requires_context_without_number_kept_with_keyword(f):
    text = "My address is Rue Victor Hugo"   # 'address' is in ADDRESS_CONTEXT_KEYWORDS
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_requires_context_without_number=True,   # ON
        guard_natural_suffix_requires_number=False,
        guard_single_token_addresses=False,
        guard_address_vs_person_priority=False,
    )
    assert "<ADDRESS>" in out, "Context keyword + no number → allowed by the guard."


def test_guard_requires_context_without_number_off_kept(f):
    text = "Rue Victor Hugo"
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_requires_context_without_number=False,  # OFF
        guard_natural_suffix_requires_number=False,
        guard_single_token_addresses=False,
        guard_address_vs_person_priority=False,
    )
    assert "<ADDRESS>" in out, "With guard OFF, name-only street can be kept."


# -----------------------------
# 3) Single-token address guard (drop one-token like 'Rosenweg' w/o number)
# -----------------------------
def test_guard_single_token_addresses_on_drops(f):
    text = "Rosenweg"
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_single_token_addresses=True,            # ON
        guard_requires_context_without_number=False,
        guard_natural_suffix_requires_number=False,
        guard_address_vs_person_priority=False,
    )
    assert "<ADDRESS>" not in out, "Single-token address w/o number should be dropped when guard is ON."


def test_guard_single_token_addresses_off_keeps(f):
    text = "Rosenweg"
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_single_token_addresses=False,           # OFF
        guard_requires_context_without_number=False,
        guard_natural_suffix_requires_number=False,
        guard_address_vs_person_priority=False,
    )
    assert "<ADDRESS>" in out, "With guard OFF, permissive suffix match can be kept as ADDRESS."


# -----------------------------
# 4) Label-leading/adjacent LOCATION filters
#    Ensure postal+city LOCATION is dropped if immediately followed by TAX label.
# -----------------------------
def test_location_dropped_when_followed_by_tax_label(f):
    # Postal+City (EU-like) followed by VAT label/value → LOCATION should be removed
    text = "10115 Berlin VAT DE123456789"
    out = f.anonymize_text(text, guards_enabled=True)
    # Expect TAX to remain but LOCATION removed by label-leading/adjacent filters
    assert "<TAX_ID>" in out
    assert "<LOCATION>" not in out, "Location next to tax label should be filtered out."


def test_location_dropped_when_preceded_by_id_label(f):
    # Label near the city, within window → drop LOCATION
    text = "passport 75008 Paris"
    out = f.anonymize_text(text, guards_enabled=True)
    #assert "<PASSPORT>" in out or "<ID_NUMBER>" in out  # passport value might be recognized as ID/PASSPORT depending on shape
    assert "<LOCATION>" not in out, "Location near 'passport' should be filtered out by adjacency filter."


# -----------------------------
# 5) Phone/date overlap demotion
# -----------------------------
def test_demote_phone_overlapping_with_date(f):
    # A date-like token should be DATE, not PHONE
    text = "The event is on 08-05-2021."
    out = f.anonymize_text(text, guards_enabled=True)
    assert "<DATE>" in out
    assert "<PHONE>" not in out, "Phone should be demoted when overlapping a DATE."


# -----------------------------
# 6) Meeting ID promotion over phone
# -----------------------------
def test_promote_meeting_over_phone(f):
    text = "Join with meeting id 123 456 7890"
    out = f.anonymize_text(text, guards_enabled=True)
    assert "<MEETING_ID>" in out
    assert "<PHONE>" not in out, "Should promote to MEETING_ID when 'meeting id' context exists."


# -----------------------------
# 7) Address span trimming (do not bleed across newline/labels)
# -----------------------------
def test_trim_address_span_at_newline_or_label(f):
    text = "Calle Mayor 5\nemail: juan@example.com"
    out = f.anonymize_text(text, guards_enabled=True)
    # Address should be trimmed before email label (and email anonymized)
    assert "<ADDRESS>" in out
    assert "<EMAIL>" in out