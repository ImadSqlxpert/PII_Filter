import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
text='The weather is nice today in the city.'
base = f.analyzer.analyze(text, language='en')
print('BASE:', [(r.entity_type, text[r.start:r.end], r.score) for r in base])
added=f._inject_custom_matches(text, base)
print('ADDED:', [(r.entity_type, text[r.start:r.end], r.score) for r in added])
print('ANON:', f.anonymize_text(text))
PY