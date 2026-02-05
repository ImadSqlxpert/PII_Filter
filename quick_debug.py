from pii_filter.pii_filter import PIIFilter

examples = [
    "My name is John Smith. I was born on 12/31/1990. I live at 221B Baker Street, London.",
    "Meine E-Mail ist max.mustermann@beispiel.de und ich wohne in der Musterstraße 5, 10115 Berlin.",
    "I live at 221B Baker Street, London.",
]

f = PIIFilter()
for text in examples:
    print('\n' + '='*80)
    print('TEXT:', text)
    lang = 'de' if any(ch in text for ch in ['ß','ö','ü','ä']) else 'en'
    base = f.analyzer.analyze(text=text, language=lang, entities=f.ALLOWED_ENTITIES, score_threshold=0.5)
    print('\nBASE:')
    for r in base:
        print(f"  - {r.entity_type:15} [{r.start}:{r.end}] '{text[r.start:r.end]}' (score={r.score})")

    filtered = []
    for r in base:
        if r.entity_type == 'PERSON':
            span = text[r.start:r.end]
            if not f._plausible_person(span, text, r.start):
                continue
        filtered.append(r)
    print('\nAFTER PERSON CLEANUP:')
    for r in filtered:
        print(f"  - {r.entity_type:15} [{r.start}:{r.end}] '{text[r.start:r.end]}' (score={r.score})")

    injected = f._inject_custom_matches(text, filtered)
    print('\nAFTER CUSTOM INJECTIONS:')
    for r in injected:
        print(f"  - {r.entity_type:15} [{r.start}:{r.end}] '{text[r.start:r.end]}' (score={r.score})")

    merged = f._resolve_overlaps(text, injected)
    print('\nMERGED:')
    for r in merged:
        print(f"  - {r.entity_type:15} [{r.start}:{r.end}] '{text[r.start:r.end]}' (score={r.score})")

print('\nDone')