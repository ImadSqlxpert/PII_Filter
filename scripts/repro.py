import os, sys
sys.path.insert(0, os.getcwd())
from pii_filter import PIIFilter

cases = [
    "+966 50 123 4567",
    "My driver's license is D1234567",
    "SE personnummer: 850709-9805",
    "Hauptstraße 5 10115 Berlin",
    "01001-000 São Paulo",
    "Je m'appelle Rue Victor",
    "Personalausweis: T22000129",
    "My student ID is STU-12345",
    "My device ID is DEV-999888777",
    "Sie können mich unter max.mueller@example.de erreichen",
    "Treten Sie meinem Meeting bei unter 123 456 789",
    "Meine Kontonummer ist 1234567890",
    "Meine Bankleitzahl ist 021000021",
    "Meine Faxnummer ist +49 30 1234567",
    "Meine Geräte-ID ist DEV-999888777",
    "Mein Führerschein ist D1234567",
    "Meine Wählerausweisnummer ist V9876543",
    "Meine Aufenthaltsgenehmigung ist RP456789",
    "Meine Sozialhilfekarte ist B11223344",
    "Meine Militärausweis ist M55667788",
]

pf = PIIFilter()
for t in cases:
    print('\n---')
    print('TEXT:', t)
    print('ANON:', pf.anonymize_text(t))
    # Show details by re-running steps from anonymize_text to see final entity list
    lang = 'en'
    base = pf.analyzer.analyze(text=t, language=lang, entities=pf.ALLOWED_ENTITIES, score_threshold=0.50)
    print('\nBase analyzer results:')
    for r in base:
        print(' ', r.entity_type, repr(t[r.start:r.end]), r.start, r.end, r.score)
    # Inject custom matches
    final = pf._inject_custom_matches(t, list(base))
    print('\nAfter custom injections:')
    for r in sorted(final, key=lambda x: (x.start, x.end)):
        print(' ', r.entity_type, repr(t[r.start:r.end]), r.start, r.end, r.score)
    # Apply post-injection filters same as anonymize_text
    final = pf._filter_locations_with_inline_or_near_labels(t, final, window=28)
    final = pf._filter_non_postal_locations(t, final, enable=pf.STRICT_LOCATION_POSTAL_ONLY)
    final = pf._guard_natural_suffix_requires_number(t, final, pf.NATURAL_SUFFIXES)
    final = pf._guard_single_token_addresses(t, final)
    final = pf._guard_address_vs_person(final)
    final = pf._guard_requires_context(t, final, pf.ADDRESS_CONTEXT_KEYWORDS, 40)
    final = pf._demote_phone_over_date(t, final)
    final = pf._promote_meeting_over_phone(t, final, window=24)
    final = pf._trim_address_spans(t, final)
    final = pf._filter_idnumber_false_positives(t, final)
    final = pf._promote_phone_to_account_if_labeled(t, final)
    final = pf._merge_address_location(t, final)
    print('\nFinal spans before anonymizer:')
    for r in sorted(final, key=lambda x: (x.start, x.end)):
        print(' ', r.entity_type, repr(t[r.start:r.end]), r.start, r.end, r.score)
