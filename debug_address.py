from pii_filter.pii_filter import PIIFilter

f=PIIFilter()
text='I live at 221B Baker Street, London.'
print('TEXT:', text)
base = f.analyzer.analyze(text=text, language='en', entities=f.ALLOWED_ENTITIES, score_threshold=0.5)
print('\nBASE:')
for r in base:
    print(r.entity_type, r.start, r.end, repr(text[r.start:r.end]), r.score)

filtered = []
for r in base:
    if r.entity_type == 'PERSON' and not f._plausible_person(text[r.start:r.end], text, r.start):
        continue
    filtered.append(r)
print('\nAFTER PERSON CLEANUP:')
for r in filtered:
    print(r.entity_type, r.start, r.end, repr(text[r.start:r.end]), r.score)

injected = f._inject_custom_matches(text, filtered)
print('\nINJECTED:')
for r in injected:
    print(r.entity_type, r.start, r.end, repr(text[r.start:r.end]), r.score)

merged = f._resolve_overlaps(text, injected)
print('\nMERGED:')
for r in merged:
    print(r.entity_type, r.start, r.end, repr(text[r.start:r.end]), r.score)

print('\nANONYMIZED:', f.anonymize_text(text))
