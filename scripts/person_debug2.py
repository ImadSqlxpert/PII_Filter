import os,sys,re
sys.path.insert(0, os.getcwd())
from pii_filter import PIIFilter
pf=PIIFilter()
text="Je m'appelle Rue Victor"
span='Rue Victor'
start=13
print('Span:', repr(span))
print('contains email:', bool(re.search(r"\b(mail|e-mail|email|correo|e-?posta|adresse|address|telefon|phone|tel)\b", span, re.I)))
print('contains banned word:', bool(re.search(r"\b(appelle|numero|nummer|número|policy|license|licence|kontonummer|passeport|passport)\b", span, re.I)))
print('je m pattern:', bool(re.match(r"^\s*(?:je\s+m['’]|j['’]|je m['’])", span.lower())))
print('tokens:', [t for t in re.split(r"\s+", span) if t])
print('latin tokens:', [t for t in re.split(r"\s+", span) if t and re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿĀ-ſ]", t)])
print('capitalized check:', any(t[0].isupper() for t in [t for t in re.split(r"\s+", span) if t and re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿĀ-ſ]", t)]))
left_ctx = text[max(0, start - 24):start].lower()
print('left_ctx:', left_ctx)
print('any street_blockers in left ctx:', any(sb in left_ctx for sb in pf.STREET_BLOCKERS))
prefix = text[max(0, start - 40):start].lower()
print('prefix:', prefix)
intro_cues = [
    "my name is", "je m", "mein name", "ich hei", "me llamo", "mi chiamo",
]
print('intro cues present:', any(cue in prefix for cue in intro_cues))
print('final plausible_person:', pf._plausible_person(span, text, start))
