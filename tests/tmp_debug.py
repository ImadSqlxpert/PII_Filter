from PII_filter.pii_filter import PIIFilter
f=PIIFilter()
print(f.anonymize_text('Customer Name: John Schmidt'))
print('---')
# full document
doc='''
Case Management System:
- Case ID: CASE-2023-001234
- Reference Number: REF-2024-567890
- Customer Name: John Schmidt
- Email: john.schmidt@example.com
- Registration: Handelsregister B 123456
'''
print(f.anonymize_text(doc))
