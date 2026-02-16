import sys
from pathlib import Path
sys.path.insert(0, str(Path('.').absolute()))
from PII_filter.pii_filter import PIIFilter
import re

f = PIIFilter()
text = 'Main Street 42, 12345 Sampletown'
print('TEXT:', text)
base = f.analyzer.analyze(text=text, language='en', entities=f.ALLOWED_ENTITIES, score_threshold=0.50)
print('\nBASE:')
for r in base:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end)
    
print('\nSTRICT match test:')
for m in f.STRICT_ADDRESS_RX.finditer(text):
    print('STRICT', repr(m.group()), m.start(), m.end())
print('\nFALLBACK match test:')
m = f.FALLBACK_STREET_RX.search(text)
print('FALLBACK m:', bool(m), repr(m.group()) if m else None)

# show injected matches
final = f._inject_custom_matches(text, base)
print('\nAFTER CUSTOM INJECTIONS:')
for r in final:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

merged = f._merge_address_location(text, final)
print('\nAFTER MERGE:')
for r in merged:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

print('\nANONYMIZED:')
print(f.anonymize_text(text))
