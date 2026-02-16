import pytest
from pii_filter.pii_filter import PIIFilter
from tests.conftest import has_tag, count_tag, normalize_placeholders as norm


@pytest.fixture(scope="module")
def f():
    return PIIFilter()


# -----------------------------
# 1) Multilingual intros → PERSON
# -----------------------------
@pytest.mark.parametrize("text", [
    "My name is John Doe",
    "Mein Name ist Hans Müller",
    "Je m’appelle Pierre Dupont",
    "Me llamo Juan Pérez",
    "Mi chiamo Mario Rossi",
    "Meu nome é Ana Silva",
    "Ik heet Jan Jansen",
    "Jag heter Sara Lind",
    "Jeg hedder Lars Jensen",
    "Minun nimeni on Matti Meikäläinen",
    "Nazywam się Jan Kowalski",
    "Jmenuji se Karel Novák",
    "Volám sa Peter Horváth",
    "A nevem László Kovács",
    "Mă numesc Andrei Popescu",
    "Με λένε Γιώργο Παπαδόπουλο",
    "Benim adım Ahmet Yılmaz",
    "اسمي أحمد محمد",
    "Меня зовут Иван Петров",
])
def test_intro_multilingual_produces_person(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert has_tag(out, "PERSON"), f"Intro should produce PERSON: {text}"


# -----------------------------
# 2) Intro trimming: only the name should be anonymized
# -----------------------------
@pytest.mark.parametrize("text,prefix", [
    ("My name is John Doe", "My name is "),
    ("Je m’appelle Marie Curie", "Je m’appelle "),
    ("Benim adım Cem Yılmaz", "Benim adım "),
    ("اسمي محمد أحمد", "اسمي "),
])
def test_intro_trimming_keeps_prefix_and_replaces_name_only(f, text, prefix):
    out = f.anonymize_text(text, guards_enabled=True)
    out_n = norm(out)
    assert prefix in out_n, "Intro prefix should remain"
    assert "<PERSON>" in out_n, "Name should be replaced with PERSON"
    # Ensure full sentence is not all replaced
    assert out_n.count("<PERSON>") == 1, "Only the name span should be PERSON"


# -----------------------------
# 3) PERSON blockers: street words → NOT PERSON
# -----------------------------
@pytest.mark.parametrize("text", [
    "via Roma",
    "rue de Rivoli",
    "calle Mayor",
    "straße der Nationen",
])
def test_person_not_triggered_by_street_words(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert not has_tag(out, "PERSON"), f"Street tokens should not become PERSON: {text}"


# -----------------------------
# 4) Pronoun/stopword blockers → NOT PERSON
# -----------------------------
@pytest.mark.parametrize("text", [
    "I and you and we",
    "yo y tú y nosotros",
    "je et tu et nous",
    "ich und du und wir",
])
def test_person_not_triggered_by_pronouns(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert not has_tag(out, "PERSON"), "Pronouns/stopwords should not become PERSON"


# -----------------------------
# 5) PERSON vs ADDRESS guard: prefer PERSON, drop overlapping ADDRESS
#    We disable the 'requires_context_without_number' so the address-like part
#    could be kept if not for the 'address_vs_person' guard.
# -----------------------------
@pytest.mark.parametrize("text", [
    "Je m'appelle Rue Victor",      # 'Rue Victor' could look like a street name
    "Mi chiamo Via Roma",           # 'Via Roma' looks like a street
])
def test_address_dropped_when_overlapping_with_person(f, text):
    out = f.anonymize_text(
        text,
        guards_enabled=True,
        guard_requires_context_without_number=False,   # allow address-like span without number
        guard_natural_suffix_requires_number=False,
        guard_single_token_addresses=False,
        guard_address_vs_person_priority=True,         # the one we verify
    )
    assert has_tag(out, "PERSON"), "Intro must produce PERSON"
    assert not has_tag(out, "ADDRESS"), "ADDRESS overlapping PERSON should be dropped by guard"


# -----------------------------
# 6) Still PERSON with additional PII nearby
# -----------------------------
def test_person_with_email_nearby_is_still_person(f):
    text = "My name is John Doe, email john.doe@example.com"
    out = f.anonymize_text(text, guards_enabled=True)
    assert has_tag(out, "PERSON"), "Intro must produce PERSON"
    assert has_tag(out, "EMAIL_ADDRESS"), "Nearby email should also be anonymized"


# -----------------------------
# 7) Lowercase single-token after intro still captured (intro injection is permissive)
# -----------------------------
@pytest.mark.parametrize("text", [
    "my name is john",
    "je m’appelle jean",
])
def test_intro_lowercase_single_token_allowed(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert has_tag(out, "PERSON"), "Intro injection should capture lowercase names as PERSON"


# -----------------------------
# 8) Non-intro, non-name content should not create PERSON
# -----------------------------
@pytest.mark.parametrize("text", [
    "Policy name field is required",
    "The address label is missing",
    "Numero di telefono",
])
def test_no_false_person_without_intro_and_no_name_like_span(f, text):
    out = f.anonymize_text(text, guards_enabled=True)
    assert not has_tag(out, "PERSON")