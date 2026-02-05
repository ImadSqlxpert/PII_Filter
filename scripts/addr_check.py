import os,sys,re
sys.path.insert(0, os.getcwd())
from pii_filter import PIIFilter
pf=PIIFilter()
text='Hauptstraße 5 10115 Berlin'
print('Text:',text)
for m in pf.STRICT_ADDRESS_RX.finditer(text):
    print('Address match:', repr(m.group()), m.start(), m.end())
for patt in pf.POSTAL_EU_PATTERNS:
    for m in re.finditer(patt, text, flags=re.I|re.UNICODE):
        print('Postal match:', repr(m.group()), m.start(), m.end())
for m in pf.PHONE_RX.finditer(text):
    print('Phone match:', repr(m.group()), m.start(), m.end())
print('PHONE regex:', pf.PHONE_REGEX)
