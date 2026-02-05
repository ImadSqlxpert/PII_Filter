import re
from pii_filter.pii_filter import PIIFilter
pf=PIIFilter()
samples=[
    "Ich wohne Königsberger Feld 4, 69120 Heidelberg (Mitte).",
    "Adresse: Hauptstraße 5, 10115 Berlin",
    "Karl-Marx-Allee 1, 20099 Hamburg",
    "mon numéro est 06 12 34 56 78.",
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
    print('BASE:')
    for r in base:
        print(' ', r.entity_type, repr(t[r.start:r.end]), r.start, r.end, r.score)
    after_custom = pf._inject_custom_matches(t, base)
    print('STRICT_ADDRESS RX matches:')
    for m in pf.STRICT_ADDRESS_RX.finditer(t):
        print(' ', repr(m.group()), m.start(), m.end())
    print('AFTER_CUSTOM:')
    for r in after_custom:
        print(' ', r.entity_type, repr(t[r.start:r.end]), r.start, r.end, r.score)
    # replicate anonymize_text post-processing to see final pipeline state
    items = after_custom[:]
    # Remove BANK/ACCOUNT overlapping email spans
    email_spans = [(r.start, r.end) for r in items if r.entity_type in ("EMAIL","EMAIL_ADDRESS")]
    if email_spans:
        preserved=[]
        for r in items:
            if r.entity_type in ("BANK_ACCOUNT","ACCOUNT_NUMBER") and any(not (r.end<=s or r.start>=e) for (s,e) in email_spans):
                continue
            preserved.append(r)
        items = preserved
    # Drop non-person single tokens
    pruned=[]
    for r in items:
        if r.entity_type=='PERSON':
            span=t[r.start:r.end].strip()
            if re.fullmatch(r"[A-Za-zÄÖÜäöüßÀ-ÿ]+", span) and span.lower() in pf.NON_PERSON_SINGLE_TOKENS:
                continue
        pruned.append(r)
    items=pruned
    items = pf._filter_locations_with_inline_or_near_labels(t, items, window=28)
    items = pf._filter_non_postal_locations(t, items, enable=pf.STRICT_LOCATION_POSTAL_ONLY)
    # Address guards (use defaults)
    items = pf._guard_natural_suffix_requires_number(t, items, pf.NATURAL_SUFFIXES)
    items = pf._guard_single_token_addresses(t, items)
    items = pf._guard_address_vs_person(items)
    items = pf._guard_requires_context(t, items, pf.ADDRESS_CONTEXT_KEYWORDS, 40)
    items = pf._demote_phone_over_date(t, items)
    items = pf._promote_meeting_over_phone(t, items, window=24)
    items = pf._trim_address_spans(t, items)
    items = pf._filter_idnumber_false_positives(t, items)
    items = pf._promote_phone_to_account_if_labeled(t, items)
    items = pf._merge_address_location(t, items)
    print('FINAL (full pipeline):')
    for r in items:
        print(' ', r.entity_type, repr(t[r.start:r.end]), r.start, r.end, r.score)
    print('ANON:', pf.anonymize_text(t))
    print('---')
