from pii_filter.pii_filter import PIIFilter
pf=PIIFilter()
samples=['Max unter 12.04 an.','Anna Gasse','Ich heiße Anna Gasse.','Herr Meyer unter 01.01 an.']
for t in samples:
    print('TEXT:',t)
    try:
        from langdetect import detect
        lang = detect(t)
    except Exception:
        lang = 'en'
    if lang not in getattr(pf.analyzer,'supported_languages',{'en'}):
        lang='en'
    base = pf.analyzer.analyze(text=t, language=lang, entities=pf.ALLOWED_ENTITIES)
    print('BASE:', base)
    # Check our dropping condition manually
    for r in base:
        if r.entity_type == 'PERSON':
            right = t[r.end:r.end+24].lower()
            has_date_entity = any(d.entity_type in ('DATE','DATE_TIME') and 0 <= d.start - r.end <= 24 for d in base)
            mid = None
            if has_date_entity:
                for d in base:
                    if d.entity_type in ('DATE','DATE_TIME') and 0 <= d.start - r.end <= 24:
                        mid = t[r.end:d.start].lower(); break
            print(' PERSON span:', repr(t[r.start:r.end]), 'right:', repr(right), 'mid:', repr(mid), 'raw-match:', bool(__import__('re').search(r"\bunter\b\s*\d{1,2}[./-]\d{1,2}\b", right)))
    print('ANON:', pf.anonymize_text(t))
    print('---')
