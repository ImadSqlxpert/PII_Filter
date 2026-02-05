import sys
sys.path.insert(0, '.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
cases=[
 'The weather is nice today in the city.',
 '+966 50 123 4567',
 'US Passport: A12345678',
 'Personalausweis: T22000129',
 'Amex 371449635398431',
 'My IBAN is DE12345678901234567890',
 'Meine Faxnummer ist +49 30 1234567',
 'Zwischen',
 'Join with meeting id 123 456 7890',
 'NL BSN: 123456782',
 '01001-000 São Paulo'
]
for c in cases:
    print('---')
    print('IN :', c)
    out=f.anonymize_text(c)
    print('OUT:', out)
PY