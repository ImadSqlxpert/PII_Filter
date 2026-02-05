from pii_filter.pii_filter import PIIFilter
import re
pf=PIIFilter()
text='NO fødselsnummer: 01010101006'
for patt,name in pf.ID_PATTERNS:
    m=re.search(patt,text,flags=re.I|re.UNICODE)
    print(name, '->', bool(m), 'match:', (m.group(1) if m and m.lastindex else (m.group(0) if m else '')))
