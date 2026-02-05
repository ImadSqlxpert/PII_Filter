import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
s='Meine Faxnummer ist +49 30 1234567'
print('fax label find:', [m.group() for m in f.FAX_LABEL_RX.finditer(s)])
for m in f.FAX_LABEL_RX.finditer(s):
    start = m.end()
    seg = s[start:start+64]
    m2 = __import__('re').search(r"(?:\+?\d{1,3}[ \-]?)?(?:\(?\d{1,4}\)?[ \-]?)?(?:\d[ \-]?){5,12}\d", seg)
    print('seg:', seg, 'match:', m2.group() if m2 else None)
print('ANON:', f.anonymize_text(s))
PY