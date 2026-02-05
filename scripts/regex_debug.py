import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
text='My IBAN is DE12345678901234567890'
for m in f.ACCT_LABEL_RX.finditer(text):
    print('MATCH:', repr(m.group(0)))
    print('groups:', m.groups())
    print('start, end:', m.start(), m.end())
    try:
        print('group1 start,end:', m.start(1), m.end(1), '->', repr(text[m.start(1):m.end(1)]))
    except Exception as e:
        print('no group1', e)
for m in f.IBAN_RX.finditer(text):
    print('IBAN MATCH:', repr(m.group(0)), m.start(), m.end())
PY