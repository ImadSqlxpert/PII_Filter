from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
texts=[
'+966 50 123 4567',
'Am Waldrand 12, 50667 Köln',
'US Passport: A12345678',
'Personalausweis: T22000129',
'Steuer-ID: 12 345 678 901',
'IBAN: DE44 5001 0517 5407 3249 31',
'Device IMEI: 490154203237518'
]
for text in texts:
    print('\n---',text)
    base = f.analyzer.analyze(text=text, language='en', entities=f.ALLOWED_ENTITIES, score_threshold=0.5)
    print('BASE:')
    for r in base:
        print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)
    filtered = []
    for r in base:
        if r.entity_type == 'PERSON':
            span = text[r.start:r.end]
            if not f._plausible_person(span, text, r.start):
                continue
        filtered.append(r)
    injected = f._inject_custom_matches(text, filtered)
    print('INJECTED:')
    for r in injected:
        print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)
    merged = f._resolve_overlaps(text, injected)
    print('MERGED:')
    for r in merged:
        print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)
