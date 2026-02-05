from pii_filter.pii_filter import PIIFilter

f = PIIFilter()
text = 'My credit card is 4111 1111 1111 1111'
print('TEXT:', text)
lang = 'en'
base = f.analyzer.analyze(text=text, language=lang, entities=f.ALLOWED_ENTITIES, score_threshold=0.5)
print('\nBASE RECOGNIZERS:')
for r in base:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

filtered = []
for r in base:
    if r.entity_type == 'PERSON':
        span = text[r.start:r.end]
        if not f._plausible_person(span, text, r.start):
            continue
    filtered.append(r)
print('\nAFTER PERSON CLEANUP:')
for r in filtered:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

injected = f._inject_custom_matches(text, filtered)
print('\nAFTER CUSTOM INJECTIONS:')
for r in injected:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

merged = f._resolve_overlaps(text, injected)
print('\nMERGED:')
for r in merged:
    print(r.entity_type, repr(text[r.start:r.end]), r.start, r.end, r.score)

# final anonymized
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
ops = { 'CREDIT_CARD': OperatorConfig('replace', {'new_value':'<CREDIT_CARD>'}), 'PHONE_NUMBER': OperatorConfig('replace', {'new_value':'<PHONE>'}) }

from presidio_anonymizer import AnonymizerEngine
an = AnonymizerEngine()
print('\nANONYMIZED:', an.anonymize(text=text, analyzer_results=merged, operators=ops).text)
