import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
text='NL BSN: 123456782'
base = f.analyzer.analyze(text, language='en')
print('BASE:', [(r.entity_type, text[r.start:r.end], r.score) for r in base])
added = []
for r in base:
    added.append(r)
added2 = f._inject_custom_matches(text, base)
print('ADDED/MERGED:', [(r.entity_type, text[r.start:r.end], r.score) for r in added2])
print('ANON:', f.anonymize_text(text))
PY