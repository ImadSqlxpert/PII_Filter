import os,sys
sys.path.insert(0, os.getcwd())
from pii_filter import PIIFilter
pf = PIIFilter()
text = "Je m'appelle Rue Victor"
print('Text:', text)
base = pf.analyzer.analyze(text=text, language='en', entities=pf.ALLOWED_ENTITIES, score_threshold=0.5)
print('\nBase analyzer results:')
for r in base:
    print(' ', r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

# PERSON cleanup
filtered=[]
for r in base:
    if r.entity_type == 'PERSON':
        span = text[r.start:r.end]
        trimmed, offset = pf._trim_intro(span)
        print('\nTrimmed:', repr(trimmed), 'offset', offset)
        if offset>0:
            ns = r.start+offset
            if (r.end-ns) >= 2:
                r = type(r)('PERSON', ns, r.end, r.score)
                span = trimmed
        print('Plausible?', pf._plausible_person(span, text, r.start))
    filtered.append(r)

print('\nAfter person cleanup (filtered):')
for r in filtered:
    print(' ', r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

# inject name intro persons
injected = pf._inject_name_intro_persons(text, filtered)
print('\nAfter inject_name_intro_persons:')
for r in injected:
    print(' ', r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)
