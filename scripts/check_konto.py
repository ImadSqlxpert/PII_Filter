import sys
sys.path.insert(0, '.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
text='Kontonummer: 1234-567890-12.'
merged=f._inject_custom_matches(text, [])
print('MERGED:', [(r.entity_type, text[r.start:r.end], r.score) for r in merged])
print('ANON:', f.anonymize_text(text))
