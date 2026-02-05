from pii_filter.pii_filter import PIIFilter
pf=PIIFilter()
texts=['Personalausweis: T22000129','RO VAT: RO12345678']
for t in texts:
    print('TEXT:',t)
    try:
        from langdetect import detect
        lang = detect(t)
    except Exception:
        lang = 'en'
    if lang not in getattr(pf.analyzer, 'supported_languages', {'en'}):
        lang = 'en'
    base = pf.analyzer.analyze(text=t, language=lang, score_threshold=0.50)
    print('BASE:', base)
    filtered=[]
    for r in base:
        if r.entity_type=='PERSON':
            span=t[r.start:r.end]
            trimmed,offset=pf._trim_intro(span)
            if offset>0:
                ns=r.start+offset
                if (r.end-ns)>=2:
                    r=type(r)('PERSON',ns,r.end,r.score)
                    span=trimmed
            if not pf._plausible_person(span,t,r.start):
                continue
        filtered.append(r)
    print('FILTERED:',filtered)
    after_intro=pf._inject_name_intro_persons(t,filtered)
    print('AFTER_INTRO:',after_intro)
    after_custom=pf._inject_custom_matches(t,after_intro)
    print('AFTER_CUSTOM:',after_custom)
    final=pf._resolve_overlaps(t,after_custom)
    print('FINAL:',final)
    print('ANON:',pf.anonymize_text(t))
    print('---')
