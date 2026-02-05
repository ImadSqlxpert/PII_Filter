import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
val='DE12345678901234567890'
print('iban_ok?', f._iban_ok(val))
text='My IBAN is DE12345678901234567890'
for m in f.ACCT_LABEL_RX.finditer(text):
    print('ACCT group:', repr(m.group(1)))
    print('start,end', m.start(1), m.end(1))
for m in f.IBAN_RX.finditer(text):
    print('IBAN_match:', repr(m.group(0)), m.start(), m.end())