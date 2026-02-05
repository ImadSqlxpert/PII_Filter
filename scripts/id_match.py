import os, sys, re
sys.path.insert(0, os.getcwd())
from pii_filter import PIIFilter
pf = PIIFilter()
text = 'SE personnummer: 850709-9805'
print('Text:', text)
for patt, name in pf.ID_PATTERNS:
    m = re.search(patt, text, flags=re.I | re.UNICODE)
    if m:
        print('Matched', name, '->', m.group(), 'groups:', m.groups())
