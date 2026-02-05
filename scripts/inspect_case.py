import sys
sys.path.insert(0, '.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
cases=['My IBAN is DE12345678901234567890','Amex 371449635398431','US Passport: A12345678','Join with meeting id 123 456 7890','The weather is nice today in the city.','Zwischen']
for c in cases:
    print('---')
    print('IN :', c)
    base=[]
    added=f._inject_custom_matches(c, base)
    print('Added:')
    for r in added:
        print(r.entity_type, repr(c[r.start:r.end]), r.score)
    merged=added
    print('Merged ->', f.anonymize_text(c))
