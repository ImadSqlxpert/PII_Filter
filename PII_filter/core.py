
from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern, RecognizerResult
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
from langdetect import detect
import re
import warnings
import logging

warnings.filterwarnings("ignore")
logging.getLogger().setLevel(logging.ERROR)

# ============================================================
# Helpers: Unicode-friendly "word" class (no \p{}, Python-safe)
# ============================================================
# Allow a dot '.' in name words (e.g., "17." in "Straße des 17. Juni")
NAME_WORD = (
    r"(?:[A-Za-zÀ-ÖØ-öø-ÿĀ-ſ\u00C0-\u024F\u0370-\u03FF"
    r"\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u0750-\u077F"
    r"\u08A0-\u08FF]"
    r"[A-Za-z0-9À-ÖØ-öø-ÿĀ-ſ\u00C0-\u024F\u0370-\u03FF"
    r"\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u0750-\u077F"
    r"\u08A0-\u08FF'’\.-]*)"
)

# ============================================================
# Street types
# ============================================================
# Expanded general STREET_TYPES (kept your international ones + full German set)
STREET_TYPES = (
    r"(?:"
    # English / international
    r"street|st\.?|road|rd\.?|avenue|ave\.?|boulevard|blvd\.?|lane|ln\.?|drive|dr\.?"
    r"|rue|chemin|via|viale|calle|carrer"
    # Core German
    r"|allee|weg|platz|ufer|ring|damm"
    r"|straße|strasse|str\.?"
    # Newly added German/DE variants
    r"|gasse|gässchen|gäßchen|gässle|gäßle|gaesschen|gaessle"
    r"|chaussee|chaus\."
    r"|brücke|bruecke"
    r"|steig|stiege|stieg|steg"
    r"|zeile|pfad"
    r"|twiete|tweute|twete"
    r"|hohl|hohle"
    r"|berg|tal|thal|wald|feld|see|bach"
    r"|kai|kanal|deich|wall|gürtel|guertel|markt|anger"
    # Turkish (kept)
    r"|caddesi|cad\.?|sokak|sk\.?"
    r")"
)

# Dedicated German street suffix list (ordered longest-first to avoid partials like 'see' inside 'chaussee')
STREET_TYPES_DE = (
    r"(?:"
    r"straße|strasse|str\.?"
    r"|chaussee|chaus\."
    r"|gässchen|gäßchen|gässle|gäßle|gaesschen|gaessle|gasse"
    r"|allee|platz|ufer|ring|damm|weg"
    r"|brücke|bruecke"
    r"|stiege|steig|stieg|steg"
    r"|zeile|pfad"
    r"|twiete|tweute|twete"
    r"|hohle|hohl"
    r"|berg|thal|tal|wald|feld|see|bach"
    r"|kai|kanal|deich|wall|gürtel|guertel|markt|anger"
    r")"
)

# ============================================================
# STRICT ADDRESS PATTERNS
# ============================================================
PATTERN_NUM_TYPE_NAME = rf"""
\b
\d{{1,5}}\w?
\s+
(?:{STREET_TYPES})
\s+
(?:{NAME_WORD}(?:\s+{NAME_WORD}){{0,4}})
\b
"""

PATTERN_TYPE_NAME_NUM = rf"""
\b
(?:{STREET_TYPES})
\s+
(?:{NAME_WORD}(?:\s+{NAME_WORD}){{0,4}})
\s+
\d{{1,5}}[a-zA-Z]?
\b
"""

PATTERN_NUM_NAME_TYPE = rf"""
\b
\d{{1,5}}[a-zA-Z]?
\s+
(?:{NAME_WORD}(?:\s+{NAME_WORD}){{0,4}})
\s+
(?:{STREET_TYPES})
\b
"""

# Classic DE "…straße/strasse/str." + (optional) number/range
PATTERN_DE_SUFFIX_NUM = rf"""
\b
[A-ZÄÖÜ][\wÄÖÜäöüß'’-]*?(?:straße|strasse|str\.)
\s*
\d{{1,5}}[a-zA-Z]?
(?:\s*[-–]\s*\d+[a-zA-Z]?)?
\b
"""

# German prefix-based street names (with/without house number)
# e.g., "Am Kupfergraben 4", "Im Wiesental", "An der Spree 12"
PATTERN_DE_PREFIX_STREET = rf"""
\b
(?:Am|Im|In(?:\s+der|\s+den|\s+dem)?|An(?:\s+der|\s+den|\s+dem)?|
   Auf(?:\s+der|\s+dem)?|Unter(?:\s+der|\s+den|\s+dem)?|Über(?:\s+der|\s+den|\s+dem)?|
   Vor(?:\s+der|\s+den|\s+dem)?|Hinter(?:\s+der|\s+den|\s+dem)?|Neben(?:\s+der|\s+den|\s+dem)?|
   Bei(?:\s+der|\s+den|\s+dem)?|Zu(?:m|r))
\s+
(?:{NAME_WORD}(?:\s+{NAME_WORD}){{0,4}})
(?:\s+\d{{1,5}}[a-zA-Z]?)?
\b
"""

# Any Uppercase-started German compound ending with a known street suffix,
# with optional house number/range. Catches "Kurfürstendamm", "Alexanderplatz", "Seebach 3".
PATTERN_DE_ANY_SUFFIX = rf"""
\b
[A-ZÄÖÜ][\wÄÖÜäöüß'’-]+?(?:{STREET_TYPES_DE})
\s*
\d{{0,5}}[a-zA-Z]?
(?:\s*[-–]\s*\d+[a-zA-Z]?)?
\b
"""

PATTERN_TR_NO = rf"""
\b
{NAME_WORD}
\s+
(?:caddesi|cad\.?|sokak|sk\.?)
\s*
(?:No|Nr)\.?\s*[:\-]?\s*\d{{1,5}}[a-zA-Z]?
\b
"""

PATTERN_ARABIC = r"""
\b
(?:شارع|طريق|جادة|حي)
\s+
\S+(?:\s+\S+){0,4}
\b
"""

STRICT_ADDRESS_REGEX = (
    f"(?:{PATTERN_NUM_TYPE_NAME})|"
    f"(?:{PATTERN_TYPE_NAME_NUM})|"
    f"(?:{PATTERN_NUM_NAME_TYPE})|"
    f"(?:{PATTERN_DE_SUFFIX_NUM})|"
    f"(?:{PATTERN_DE_PREFIX_STREET})|"
    f"(?:{PATTERN_DE_ANY_SUFFIX})|"
    f"(?:{PATTERN_TR_NO})|"
    f"(?:{PATTERN_ARABIC})"
)

address_recognizer = PatternRecognizer(
    supported_entity="ADDRESS",
    supported_language="all",
    patterns=[Pattern("strict_address", STRICT_ADDRESS_REGEX, 0.80)],
)

# ============================================================
# POSTAL CODE + CITY  (multi-word city supported)
# ============================================================
POSTAL_CITY_LOCATION_REGEX = r"""
\b
\d{4,6}
\s+
[A-Z][A-Za-zÀ-ÖØ-öø-ÿĀ-ſ\u00C0-\u024F\u0370-\u03FF\u0400-\u04FF'’-]+
(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿĀ-ſ\u00C0-\u024F\u0370-\u03FF\u0400-\u04FF'’-]+){0,2}
\b
"""

# ============================================================
# PHONE NUMBERS
# ============================================================
PHONE_REGEX = r"""
(?ix)
(?<!\w)
(?:\+?\d{1,3}[ \-]?)?
(?:\(?\d{1,4}\)?[ \-]?)?
(?:\d[ \-]?){6,12}\d
(?!\w)
"""

phone_recognizer = PatternRecognizer(
    supported_entity="PHONE_NUMBER",
    supported_language="all",
    patterns=[Pattern("intl_phone", PHONE_REGEX, 0.72)],
)

# ============================================================
# DATES
# ============================================================
DATE_REGEX_1 = r"\b\d{1,2}[.\-/]\d{1,2}[.\-/]\d{2,4}\b"
DATE_REGEX_2 = r"\b\d{4}[.\-/]\d{1,2}[.\-/]\d{1,2}\b"
DATE_REGEX_3 = r"\b\d{1,2}\s+[A-Za-zÄÖÜäöüßÁÉÍÓÚáéíóúñç]+\s+\d{4}\b"

date_recognizer = PatternRecognizer(
    supported_entity="DATE",
    supported_language="all",
    patterns=[
        Pattern("dob_1", DATE_REGEX_1, 0.70),
        Pattern("dob_2", DATE_REGEX_2, 0.70),
        Pattern("dob_3", DATE_REGEX_3, 0.65),
    ],
)

# ============================================================
# PASSPORTS
# ============================================================
US_PASSPORT_REGEX = r"\b[A-Z][0-9]{8}\b"
EU_PASSPORT_REGEX = r"\b(?=[A-Z0-9]{6,9}\b)(?=.*[A-Z])[A-Z0-9]{6,9}\b"

passport_recognizer = PatternRecognizer(
    supported_entity="PASSPORT",
    supported_language="all",
    patterns=[
        Pattern("us_passport", US_PASSPORT_REGEX, 0.80),
        Pattern("eu_passport_generic", EU_PASSPORT_REGEX, 0.70),
    ],
)

# ============================================================
# NATIONAL IDs (Germany + labeled)
# ============================================================
DE_ID_REGEX = r"\b(?=[A-Z0-9]{9}\b)(?=.*[A-Z])[A-Z0-9]{9}\b"

id_recognizer = PatternRecognizer(
    supported_entity="ID_NUMBER",
    supported_language="all",
    patterns=[Pattern("de_personalausweis", DE_ID_REGEX, 0.78)],
)

LABELED_ID_VALUE_RX = re.compile(
    r"(?i)\b(?:personalausweis(?:nummer|nr\.?)|identity\s*card|id\s*(?:no\.?|number)|dni|nif|nie)"
    r"\s*[:#]?\s*([A-Z0-9][A-Z0-9\-]{4,20})"
)

# ============================================================
# TAX IDs: U.S. SSN / ITIN / EIN + EU labeled TIN/VAT
# ============================================================
US_SSN_DASHED = r"\b\d{3}-\d{2}-\d{4}\b"
US_SSN_COMPACT = r"\b\d{9}\b"
US_ITIN_DASHED = r"\b9\d{2}-\d{2}-\d{4}\b"
US_ITIN_COMPACT = r"\b9\d{8}\b"
US_EIN = r"\b\d{2}-\d{7}\b"

# Allow spaces in the numeric value after labels (e.g., "12 345 678 901")
LABELED_TAX_VALUE_RX = re.compile(
    r"(?i)\b(?:steuer[-\s]*id|steueridentifikationsnummer|tin|tax\s*id|tax\s*number|vat"
    r"|u(?:msatz)?st-?id(?:nr\.?)?)"
    r"\s*[:#]?\s*([A-Z]{2}\s*[A-Z0-9][A-Z0-9\.\-\s]{1,24}|[A-Z0-9\-\s]{8,24})"
)

tax_recognizer = PatternRecognizer(
    supported_entity="TAX_ID",
    supported_language="all",
    patterns=[
        Pattern("us_ssn_dashed", US_SSN_DASHED, 0.80),
        Pattern("us_itin_dashed", US_ITIN_DASHED, 0.82),
        Pattern("us_ein", US_EIN, 0.80),
        Pattern("us_ssn_compact", US_SSN_COMPACT, 0.40),
        Pattern("us_itin_compact", US_ITIN_COMPACT, 0.45),
    ],
)

# ============================================================
# IP ADDRESSES — IPv4 + improved IPv6 (no trailing chars)
# ============================================================
IPV4_REGEX = r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\b"

IPV6_CORE = (
    r"(?:"  # Full + compressed combinations
    r"(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}|"
    r"(?:[A-F0-9]{1,4}:){1,7}:|"
    r":(?::[A-F0-9]{1,4}){1,7}|"
    r"(?:[A-F0-9]{1,4}:){1,6}:[A-F0-9]{1,4}|"
    r"(?:[A-F0-9]{1,4}:){1,5}(?::[A-F0-9]{1,4}){1,2}|"
    r"(?:[A-F0-9]{1,4}:){1,4}(?::[A-F0-9]{1,4}){1,3}|"
    r"(?:[A-F0-9]{1,4}:){1,3}(?::[A-F0-9]{1,4}){1,4}|"
    r"(?:[A-F0-9]{1,4}:){1,2}(?::[A-F0-9]{1,4}){1,5}|"
    r"[A-F0-9]{1,4}:(?::[A-F0-9]{1,4}){1,6}|"
    r"::(?:[A-F0-9]{1,4}:){0,6}[A-F0-9]{1,4}"
    r")"
)
IPV6_REGEX = r"(?i)(?<![A-F0-9:])" + IPV6_CORE + r"(?![A-F0-9:])"

ip_recognizer = PatternRecognizer(
    supported_entity="IP_ADDRESS",
    supported_language="all",
    patterns=[
        Pattern("ipv4", IPV4_REGEX, 0.85),
        Pattern("ipv6", IPV6_REGEX, 0.85),
    ],
)

# ============================================================
# SETUP ANALYZER
# ============================================================
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

for rec in [
    address_recognizer,
    phone_recognizer,
    date_recognizer,
    passport_recognizer,
    id_recognizer,
    tax_recognizer,
    ip_recognizer,
]:
    analyzer.registry.add_recognizer(rec)

ALLOWED_ENTITIES = [
    "PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "ADDRESS", "LOCATION",
    "DATE", "PASSPORT", "ID_NUMBER", "TAX_ID", "IP_ADDRESS"
]

# DATE outranks PHONE to avoid <PHONE> on dates
PRIORITY = {
    "ADDRESS": 7,
    "PASSPORT": 6,
    "ID_NUMBER": 6,
    "TAX_ID": 6,
    "IP_ADDRESS": 5,
    "DATE": 5,          # ↑ increased
    "PHONE_NUMBER": 4,
    "EMAIL_ADDRESS": 3,
    "PERSON": 2,
    "LOCATION": 1,
}

# ============================================================
# PERSON CLEANUP
# ============================================================
INTRO_REGEXES = [
    re.compile(r"^(?:my name is)\s+", re.I),
    re.compile(r"^(?:je m(?:'|’| )appelle)\s+", re.I),
    re.compile(r"^(?:mein name ist)\s+", re.I),
    re.compile(r"^(?:me llamo)\s+", re.I),
    re.compile(r"^(?:mi chiamo)\s+", re.I),
    re.compile(r"^(?:benim adım)\s+", re.I),
    re.compile(r"^(?:اسمي)\s+"),
    re.compile(r"^(?:انا اسمي|أنا اسمي)\s+"),
]

NON_PERSON_SINGLE_TOKENS = {
    "meine","mein","meiner","ist","und","y","mi","il","la","el",
    "sono","soy","ich","bin","am","i","je","j'","j’",
    "abito","vivo","habito","wohne","adresse","indirizzo",
    "dirección","direccion",
    "numero","nummer","numéro","telefono","telefon","tel",
}

PRONOUN_PERSONS = {"ich","je","yo","io","benim","انا","أنا"}

# Extra verb filter for multi-token PERSON
MULTI_BAD_TOKENS = {
    "wohne","vivo","habito","abito","soy","sono","am","bin","je","ich"
}

EMAIL_WORDS_RE = re.compile(r"\b(mail|e-mail|email|correo|e-?posta)\b", re.I)
PHONE_WORDS_RE = re.compile(r"\b(numero|nummer|numéro|telefono|telefon|phone|tel)\b", re.I)

def _trim_intro(span: str):
    for rx in INTRO_REGEXES:
        m = rx.match(span)
        if m:
            off = m.end()
            return span[off:], off
    return span, 0

def _is_single_token_letters(s: str):
    return bool(re.match(r"^[^\W\d_]+$", s.strip(), re.UNICODE))

def _plausible_person(span: str, text: str, start: int):
    s = span.strip()
    if not s:
        return False
    if EMAIL_WORDS_RE.search(s) or PHONE_WORDS_RE.search(s):
        return False
    if " " in s:
        toks = [t for t in s.split() if t]
        # if verb/pronoun tokens in multi-token span -> drop
        if any(t.lower() in MULTI_BAD_TOKENS for t in toks):
            return False
        latin = [t for t in toks if re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿĀ-ſ]", t)]
        if latin and not any(t[0].isupper() for t in latin):
            return False
        return True
    if s.lower() in NON_PERSON_SINGLE_TOKENS:
        return False
    if s.lower() in PRONOUN_PERSONS:
        return False
    prefix = text[max(0,start-40):start].lower()
    return any(p in prefix for p in ["my name is","je m","mein name","me llamo","mi chiamo","benim adım","اسمي","انا اسمي","أنا اسمي","i am"])

# Name-intro injection
INTRO_PATTERNS = [
    re.compile(r"\bmy name is\s+([A-Z][^\s,.;:]+(?:\s+[A-Z][^\s,.;:]+){0,3})", re.I),
    re.compile(r"\bje m(?:'|’| )appelle\s+([A-ZÀ-ÖØ-Ý][^\s,.;:]+(?:\s+[A-ZÀ-ÖØ-Ý][^\s,.;:]+){0,3})", re.I),
    re.compile(r"\bmein name ist\s+([A-ZÄÖÜ][^\s,.;:]+(?:\s+[A-ZÄÖÜ][^\s,.;:]+){0,3})", re.I),
    re.compile(r"\bme llamo\s+([A-ZÁÉÍÓÚÑ][^\s,.;:]+(?:\s+[A-ZÁÉÍÓÚÑ][^\s,.;:]+){0,3})", re.I),
    re.compile(r"\bmi chiamo\s+([A-ZÀ-ÖØ-Ý][^\s,.;:]+(?:\s+[A-ZÀ-ÖØ-Ý][^\s,.;:]+){0,3})", re.I),
    re.compile(r"\bbenim adım\s+([A-ZÇĞİÖŞÜ][^\s,.;:]+(?:\s+[A-ZÇĞİÖŞÜ][^\s,.;:]+){0,3})", re.I),
    re.compile(r"(?:^|\b)(?:اسمي|انا اسمي|أنا اسمي)\s+([^\s،,]+(?:\s+[^\s،,]+){0,3})"),
]

def _inject_name_intro_persons(text, results):
    add=[]
    for rx in INTRO_PATTERNS:
        for m in rx.finditer(text):
            s,e = m.start(1), m.end(1)
            add.append(RecognizerResult("PERSON",s,e,0.96))
    return _resolve_overlaps(text, results+add) if add else results

# ============================================================
# Overlap handling + filtering
# ============================================================
def _resolve_overlaps(text, items):
    items = sorted(items, key=lambda r:(r.start, -PRIORITY[r.entity_type], -(r.end-r.start)))
    kept=[]
    for r in items:
        drop=False
        for k in kept:
            if not (r.end <= k.start or r.start >= k.end):
                if PRIORITY[r.entity_type] > PRIORITY[k.entity_type] or \
                   (PRIORITY[r.entity_type]==PRIORITY[k.entity_type] and (r.end-r.start) > (k.end-k.start)):
                    kept.remove(k)
                    kept.append(r)
                drop=True
                break
        if not drop:
            kept.append(r)
    return sorted(kept, key=lambda x:x.start)

def _demote_phone_over_date(text, items):
    dates=[(r.start,r.end) for r in items if r.entity_type=="DATE"]
    if not dates:
        return items
    out=[]
    for r in items:
        if r.entity_type!="PHONE_NUMBER":
            out.append(r); continue
        if any(not(r.end <= ds or r.start >= de) for ds,de in dates):
            continue
        out.append(r)
    return out

def _filter_label_leading_locations(text, items):
    """Drop LOCATION directly preceding 'Passport'/'ID' labels (e.g., 'U.S. Passport')."""
    out=[]
    for r in items:
        if r.entity_type=="LOCATION":
            tail = text[r.end:r.end+12].lower()
            if any(tail.strip().startswith(k) for k in ["passport", "id", "identity", "personalausweis"]):
                # skip this location to avoid '<LOCATION> Passport'
                continue
        out.append(r)
    return out

# ============================================================
# Toggleable FALSE-POSITIVE GUARDS (no class; keyword flags)
# ============================================================
NATURAL_SUFFIXES = ("berg","tal","thal","wald","feld","see","bach")

ADDRESS_CONTEXT_KEYWORDS = (
    "wohne", "wohnhaft", "adresse", "liegt", "befindet", "ist in", "bei"
)

def _guard_natural_suffix_requires_number(text: str, items, suffixes: tuple):
    """Drop ADDRESS if span ends with a natural-feature suffix and has no digits."""
    if not items:
        return items
    out = []
    for r in items:
        if r.entity_type == "ADDRESS":
            span = text[r.start:r.end].strip()
            lower = span.lower()
            if any(lower.endswith(suf) for suf in suffixes):
                if not re.search(r"\d", span):
                    # no house number → drop
                    continue
        out.append(r)
    return out

def _guard_single_token_addresses(text: str, items):
    """Drop ADDRESS if it is a single token without any digits."""
    if not items:
        return items
    out = []
    for r in items:
        if r.entity_type=="ADDRESS":
            span=text[r.start:r.end].strip()
            if len(span.split()) == 1 and not re.search(r"\d", span):
                continue
        out.append(r)
    return out

def _guard_address_vs_person(items):
    """Prefer PERSON over ADDRESS on overlaps."""
    if not items:
        return items
    persons = [p for p in items if p.entity_type == "PERSON"]
    if not persons:
        return items
    out = []
    for r in items:
        if r.entity_type == "ADDRESS":
            overlap_with_person = any(not (r.end <= p.start or r.start >= p.end) for p in persons)
            if overlap_with_person:
                # drop ADDRESS in favor of PERSON
                continue
        out.append(r)
    return out

def _guard_requires_context(text: str, items, keywords: tuple, window: int):
    """
    If ADDRESS has no digits (no house number), require presence of address-ish context
    within `window` chars around the span.
    """
    if not items:
        return items
    lower = text.lower()
    out = []
    for r in items:
        if r.entity_type == "ADDRESS":
            span = text[r.start:r.end]
            if not re.search(r"\d", span):
                left = max(0, r.start - window)
                right = min(len(text), r.end + window)
                ctx = lower[left:right]
                if not any(k in ctx for k in keywords):
                    # no contextual evidence → drop
                    continue
        out.append(r)
    return out

# ============================================================
# CUSTOM MATCH INJECTION
# ============================================================
def _inject_custom_matches(text, results):
    add=[]

    # Address
    for m in re.finditer(STRICT_ADDRESS_REGEX, text, flags=re.I|re.UNICODE|re.VERBOSE):
        add.append(RecognizerResult("ADDRESS", m.start(), m.end(), 0.95))

    # Postal+city → LOCATION
    for m in re.finditer(POSTAL_CITY_LOCATION_REGEX, text, flags=re.I|re.UNICODE|re.VERBOSE):
        add.append(RecognizerResult("LOCATION", m.start(), m.end(), 0.90))

    # Phone
    for m in re.finditer(PHONE_REGEX, text, flags=re.I|re.UNICODE|re.VERBOSE):
        if len(re.sub(r"\D","",m.group()))>=7:
            add.append(RecognizerResult("PHONE_NUMBER", m.start(), m.end(), 0.90))

    # Dates (explicit injection so they cannot be missed)
    for patt in (DATE_REGEX_1, DATE_REGEX_2, DATE_REGEX_3):
        for m in re.finditer(patt, text, flags=re.I|re.UNICODE):
            add.append(RecognizerResult("DATE", m.start(), m.end(), 0.93))

    # ID labels
    for m in LABELED_ID_VALUE_RX.finditer(text):
        s,e = m.start(1), m.end(1)
        add.append(RecognizerResult("ID_NUMBER", s, e, 0.92))

    # TAX labels
    for m in LABELED_TAX_VALUE_RX.finditer(text):
        s,e = m.start(1), m.end(1)
        add.append(RecognizerResult("TAX_ID", s, e, 0.92))

    # Passports (strong injection)
    for m in re.finditer(US_PASSPORT_REGEX, text):
        add.append(RecognizerResult("PASSPORT", m.start(), m.end(), 0.95))
    for m in re.finditer(EU_PASSPORT_REGEX, text):
        add.append(RecognizerResult("PASSPORT", m.start(), m.end(), 0.90))

    # IP
    for patt in (IPV4_REGEX, IPV6_REGEX):
        for m in re.finditer(patt,text,flags=re.I|re.UNICODE):
            add.append(RecognizerResult("IP_ADDRESS", m.start(), m.end(), 0.95))

    merged = _resolve_overlaps(text, results+add)
    # remove label-leading LOCATIONS like 'U.S. Passport'
    merged = _filter_label_leading_locations(text, merged)
    return merged

# ============================================================
# Merge ADDRESS + LOCATION (full address masking)
# ============================================================
def _merge_address_location(text, items):
    items=sorted(items,key=lambda r:r.start)
    merged=[]
    i=0
    while i < len(items):
        cur=items[i]
        if i+1 < len(items):
            nxt=items[i+1]
            between=text[cur.end:nxt.start]
            if (cur.entity_type=="ADDRESS" and nxt.entity_type=="LOCATION") or \
               (cur.entity_type=="LOCATION" and nxt.entity_type=="ADDRESS"):
                if re.fullmatch(r"\s*,?\s*|\s{1,3}",between):
                    s=min(cur.start,nxt.start)
                    e=max(cur.end,nxt.end)
                    merged.append(RecognizerResult("ADDRESS",s,e,max(cur.score,nxt.score)))
                    i+=2
                    continue
        merged.append(cur); i+=1
    return _resolve_overlaps(text, merged)

# ============================================================
# MAIN
# ============================================================
def anonymize_text(
    text: str,
    *,
    guards_enabled: bool = True,
    guard_natural_suffix_requires_number: bool = True,
    guard_single_token_addresses: bool = True,
    guard_address_vs_person_priority: bool = True,
    guard_requires_context_without_number: bool = True,
    guard_context_window: int = 40
) -> str:
    if not text or not text.strip():
        return text

    try:
        lang=detect(text)
    except:
        lang="en"
    if lang not in analyzer.supported_languages:
        lang="en"

    base=analyzer.analyze(text=text, language=lang, entities=ALLOWED_ENTITIES, score_threshold=0.50)

    # Person cleanup
    filtered=[]
    for r in base:
        if r.entity_type=="PERSON":
            span=text[r.start:r.end]
            trimmed,offset=_trim_intro(span)
            if offset>0:
                ns=r.start+offset
                if (r.end-ns)>=2:
                    r=RecognizerResult("PERSON",ns,r.end,r.score)
                    span=trimmed
            if not _plausible_person(span,text,r.start):
                continue
        filtered.append(r)

    filtered=_inject_name_intro_persons(text,filtered)

    final=_inject_custom_matches(text,filtered)

    # ---------- Toggleable guards ----------
    if guards_enabled:
        if guard_natural_suffix_requires_number:
            final = _guard_natural_suffix_requires_number(text, final, NATURAL_SUFFIXES)
        if guard_single_token_addresses:
            final = _guard_single_token_addresses(text, final)
        if guard_address_vs_person_priority:
            final = _guard_address_vs_person(final)
        if guard_requires_context_without_number:
            final = _guard_requires_context(text, final, ADDRESS_CONTEXT_KEYWORDS, guard_context_window)
    # --------------------------------------

    final=_demote_phone_over_date(text,final)
    final=_merge_address_location(text,final)

    # MASKS: single-escaped HTML tokens (as requested)
    operators={

        "PERSON":        OperatorConfig("replace", {"new_value": "&lt;PERSON&gt;"}),
        "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": "&lt;EMAIL&gt;"}),
        "PHONE_NUMBER":  OperatorConfig("replace", {"new_value": "&lt;PHONE&gt;"}),
        "ADDRESS":       OperatorConfig("replace", {"new_value": "&lt;ADDRESS&gt;"}),
        "LOCATION":      OperatorConfig("replace", {"new_value": "&lt;LOCATION&gt;"}),

        "DATE":          OperatorConfig("replace", {"new_value": "&lt;DATE&gt;"}),
        "PASSPORT":      OperatorConfig("replace", {"new_value": "&lt;PASSPORT&gt;"}),
        "ID_NUMBER":     OperatorConfig("replace", {"new_value": "&lt;ID_NUMBER&gt;"}),
        "TAX_ID":        OperatorConfig("replace", {"new_value": "&lt;TAX_ID&gt;"}),
        "IP_ADDRESS":    OperatorConfig("replace", {"new_value": "&lt;IP_ADDRESS&gt;"})
    }

    out=anonymizer.anonymize(text=text, analyzer_results=final, operators=operators)
    return out.text
