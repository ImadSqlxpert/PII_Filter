import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pii_filter.pii_filter import PIIFilter
pf = PIIFilter()
texts = [
    "Mă numesc Andrei Popescu",
    "Je m'appelle Rue Victor",
]
for t in texts:
    print('TEXT:', t)
    # Reproduce pipeline
    lang = 'en'
    base = pf.analyzer.analyze(text=t, language=lang, entities=pf.ALLOWED_ENTITIES, score_threshold=0.50)
    print('BASE:', base)
    filtered = []
    for r in base:
        if r.entity_type == 'PERSON':
            span = t[r.start:r.end]
            trimmed, offset = pf._trim_intro(span)
            if offset > 0:
                ns = r.start + offset
                if (r.end - ns) >= 2:
                    r = type(r)("PERSON", ns, r.end, r.score)
                    span = trimmed
            if not pf._plausible_person(span, t, r.start):
                continue
        filtered.append(r)
    print('FILTERED:', filtered)
    after_intro = pf._inject_name_intro_persons(t, filtered)
    print('AFTER_INTRO_INJECT:', after_intro)
    after_custom = pf._inject_custom_matches(t, after_intro)
    print('AFTER_CUSTOM:', after_custom)
    pruned = []
    for r in after_custom:
        if r.entity_type == 'PERSON':
            span = t[r.start:r.end].strip()
            if __import__('re').fullmatch(r"[A-Za-zÄÖÜäöüßÀ-ÿ]+", span) and span.lower() in pf.NON_PERSON_SINGLE_TOKENS:
                continue
        pruned.append(r)
    print('PRUNED:', pruned)
    print('---')
