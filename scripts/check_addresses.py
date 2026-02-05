from pii_filter.pii_filter import PIIFilter
pf=PIIFilter()
samples=[
    "Ich wohne Königsberger Feld 4, 69120 Heidelberg (Mitte).",
    "Adresse: Hauptstraße 5, 10115 Berlin",
    "Karl-Marx-Allee 1, 20099 Hamburg",
    "Karl-Marx-Allee 1, 20099 Hamburg",
    "20354 Hamburg",
    "mon numéro est 06 12 34 56 78.",
    "Ich heiße Anna Gasse.",
]
for t in samples:
    print('TEXT:',t)
    try:
        from langdetect import detect
        lang = detect(t)
    except Exception:
        lang = 'en'
    if lang not in getattr(pf.analyzer, 'supported_languages', {'en'}):
        lang = 'en'
    base = pf.analyzer.analyze(text=t, language=lang, entities=pf.ALLOWED_ENTITIES, score_threshold=0.50)
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
