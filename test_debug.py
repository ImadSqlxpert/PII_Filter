#!/usr/bin/env python
import sys
sys.path.insert(0, '/c/Users/Imad/Desktop/projects/PII_filter_tester')

from pii_filter import PIIFilter

filter = PIIFilter()

test_cases = [
    "Am Waldrand 12, 50667 Köln",
    "US Passport: A12345678",
    "Personalausweis: T22000129",
    "Steuer-ID: 12 345 678 901",
    "IBAN: DE44 5001 0517 5407 3249 31",
    "Diagnosed with diabetes",
    "Device IMEI: 490154203237518",
    "My tax ID is 12-3456789",
    "My routing number is 021000021",
    "My device IMEI is 490154203237518",
    "My IDFA is 123e4567-e89b-12d3-a456-426614174000",
    "My fax number is +1 555-123-4568",
    "Ich habe Diabetes und brauche medizinische Hilfe",
    "Meine Steuer-ID ist 12-3456789",
    "Meine Bankleitzahl ist 021000021",
    "Die IMEI meines Geräts ist 490154203237518",
    "Meine Faxnummer ist +49 30 1234567",
]

for text in test_cases:
    try:
        # Run AnalyzerEngine
        lang = 'de' if any(ord(c) > 127 for c in text) else 'en'
        base = filter.analyzer.analyze(text=text, language=lang, entities=filter.ALLOWED_ENTITIES, score_threshold=0.5)
    except Exception as e:
        print(f"Analyzer error for '{text}': {e}")
        continue
    print(f"\nInput:  {text}")
    print("Analyzer results:")
    for r in base:
        print(f"  {r.entity_type} | {r.start}:{r.end} | score={r.score} | span='{text[r.start:r.end]}'")
    # Apply PERSON cleanup and intro injection
    filtered = []
    for r in base:
        if r.entity_type == 'PERSON':
            span = text[r.start:r.end]
            if not filter._plausible_person(span, text, r.start):
                continue
        filtered.append(r)
    filtered = filter._inject_name_intro_persons(text, filtered)
    print("After person intro injection:")
    for r in filtered:
        print(f"  {r.entity_type} | {r.start}:{r.end} | score={r.score} | span='{text[r.start:r.end]}'")
    final = filter._inject_custom_matches(text, filtered)
    print("After custom injections:")
    for r in final:
        print(f"  {r.entity_type} | {r.start}:{r.end} | score={r.score} | span='{text[r.start:r.end]}'")

# Also test the regex patterns directly
print("\n--- Direct regex testing ---")
for text in test_cases[:5]:
    print(f"\nTesting: {text}")
    
    m_driver = filter.DRIVER_LICENSE_LABEL_RX.search(text)
    print(f"  DRIVER_LICENSE_LABEL_RX: {m_driver is not None}" + (f" -> {m_driver.group(1) if m_driver else ''}" if m_driver else ""))
    
    m_voter = filter.VOTER_ID_LABEL_RX.search(text)
    print(f"  VOTER_ID_LABEL_RX: {m_voter is not None}" + (f" -> {m_voter.group(1) if m_voter else ''}" if m_voter else ""))
    
    m_residence = filter.RESIDENCE_PERMIT_LABEL_RX.search(text)
    print(f"  RESIDENCE_PERMIT_LABEL_RX: {m_residence is not None}" + (f" -> {m_residence.group(1) if m_residence else ''}" if m_residence else ""))
    
    m_benefit = filter.BENEFIT_ID_LABEL_RX.search(text)
    print(f"  BENEFIT_ID_LABEL_RX: {m_benefit is not None}" + (f" -> {m_benefit.group(1) if m_benefit else ''}" if m_benefit else ""))
    
    m_military = filter.MILITARY_ID_LABEL_RX.search(text)
    print(f"  MILITARY_ID_LABEL_RX: {m_military is not None}" + (f" -> {m_military.group(1) if m_military else ''}" if m_military else ""))
