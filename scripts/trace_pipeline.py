import sys
from pathlib import Path
sys.path.insert(0, str(Path('.').absolute()))
from PII_filter.pii_filter import PIIFilter

f = PIIFilter()
text = 'I am called Sarah Connor'
print('TEXT:', text)
lang = 'en'
base = f.analyzer.analyze(text=text, language=lang, entities=f.ALLOWED_ENTITIES, score_threshold=0.50)
print('\nBASE:')
for r in base:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end)

# Show strict/fallback address regex matches
print('\nSTRICT_ADDRESS_RX matches:')
for m in f.STRICT_ADDRESS_RX.finditer(text):
    print('STRICT match:', repr(m.group()), m.start(), m.end())
print('\nFALLBACK_STREET_RX matches:')
for m in f.FALLBACK_STREET_RX.finditer(text):
    print('FALLBACK match:', repr(m.group()), m.start(), m.end())

# PERSON cleanup
filtered = []
for r in base:
    if r.entity_type == 'PERSON':
        span = text[r.start:r.end]
        trimmed, offset = f._trim_intro(span)
        if offset > 0:
            ns = r.start + offset
            if (r.end - ns) >= 2:
                r = type(r)("PERSON", ns, r.end, r.score)
                span = trimmed
        addr_m = f.STRICT_ADDRESS_RX.search(span)
        if addr_m and re.search(r"\d", addr_m.group()):
            pass
        if not f._plausible_person(span, text, r.start):
            print('DROPPING PERSON at cleanup:', repr(span))
            continue
    filtered.append(r)
print('\nAFTER PERSON CLEANUP:')
for r in filtered:
    print(r.entity_type, repr(text[r.start:r.end]))

# Intro injection
injected = f._inject_name_intro_persons(text, filtered)
print('\nAFTER INTRO INJECTION:')
for r in injected:
    print(r.entity_type, repr(text[r.start:r.end]))

# Continue to end (quick)
final = f._inject_custom_matches(text, injected)
print('\nAFTER CUSTOM INJECTIONS:')
for r in final:
    print(r.entity_type, repr(text[r.start:r.end]))

# Run final pruning from anonymize_text
pruned = []
for r in final:
    if r.entity_type == 'PERSON':
        span = text[r.start:r.end].strip()
        if re.fullmatch(r"[A-Za-zÄÖÜäöüßÀ-ÿ]+", span) and span.lower() in f.NON_PERSON_SINGLE_TOKENS:
            print('Dropped single-token non-person later:', span)
            continue
        tokens = [t.lower() for t in span.split()]
        if len(tokens) >= 2:
            sentence_starters = {"ich","du","er","sie","es","wir","ihr","möchte","kann","werde","würde","habe","hab","bin","ist","sind","hat","hätte","für","von","zu","bei","mit","ohne","in"}
            if any(t in sentence_starters for t in tokens[:2]):
                print('Dropped sentence-like PERSON later:', span)
                continue
    pruned.append(r)
print('\nAFTER PRUNING:')
for r in pruned:
    print(r.entity_type, repr(text[r.start:r.end]))

print('\nANONYMIZED OUTPUT:')
print(f.anonymize_text(text))
