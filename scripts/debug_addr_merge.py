from pii_filter.pii_filter import PIIFilter
pf=PIIFilter()
text='Hauptstraße 5 10115 Berlin'
print('ANON:', pf.anonymize_text(text, guards_enabled=True))
from langdetect import detect
try:
    lang = detect(text)
except Exception:
    lang = 'en'
if lang not in getattr(pf.analyzer, 'supported_languages', {'en'}):
    lang = 'en'
base = pf.analyzer.analyze(text=text, language=lang, score_threshold=0.50)
print('BASE:', base)
merged = pf._inject_custom_matches(text, base)
print('AFTER_CUSTOM:', merged)
final = pf._merge_address_location(text, merged)
print('FINAL MERGED:', final)
for r in final:
    print(r.entity_type, repr(text[r.start:r.end]), r.score)
