from pii_filter import PIIFilter
f=PIIFilter()
text='Am Waldrand 12, 50667 Köln'
print('INPUT:', text)
print('OUTPUT:', f.anonymize_text(text))
print('---')
text2='Hauptstraße 5, Berlin'
print('INPUT:', text2)
print('OUTPUT:', f.anonymize_text(text2))
