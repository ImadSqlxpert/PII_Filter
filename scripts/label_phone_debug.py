import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
pattern=f.LABELED_ID_VALUE_RX
s='NL BSN: 123456782'
m=pattern.search(s)
print('match?', bool(m), 'groups:', m.groups() if m else None)
for m2 in f.PHONE_RX.finditer(s):
    print('PHONE match:', m2.group(), m2.start(), m2.end())
PY