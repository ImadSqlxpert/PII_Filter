import sys
from pathlib import Path
sys.path.insert(0, str(Path('.').absolute()))
from PII_filter.pii_filter import PIIFilter

f = PIIFilter()
text = 'I am called Sarah Connor'
add = f._inject_name_intro_persons(text, [])
print('Injected results:')
for r in add:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

base = f.analyzer.analyze(text=text, language='en', entities=f.ALLOWED_ENTITIES, score_threshold=0.5)
print('\nBase results:')
for r in base:
    print(r.entity_type, repr(text[r.start:r.end]))

# Also run anonymize_text
print('\nAnonymized:')
print(f.anonymize_text(text))
