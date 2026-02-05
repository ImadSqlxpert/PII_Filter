import re

patterns = {
    "DRIVER_LICENSE": r"(?i)(?:my\s+)?(?:driver(?:'?s)?\s*(?:license|licence|lic)|dl\s*number|führerschein)[\s\b]+[:\-\s]*([A-Z]\d{5,10})",
    "VOTER_ID": r"(?i)(?:my\s+)?(?:voter\s*(?:id|card|number)|cartilla|carné\s*de\s*votante|wählerausweins?(?:nummer)?)[\s\b]+[:\-\s]*([A-Z]\d{5,10})",
    "RESIDENCE_PERMIT": r"(?i)(?:my\s+)?(?:residence\s*(?:permit|card)|resident\s*permit|título\s*de\s*residencia|aufenthaltstitel)[\s\b]+[:\-\s]*([A-Z]{2}\d{5,10})",
    "BENEFIT_ID": r"(?i)(?:my\s+)?(?:benefit\s*(?:id|card|number)|sozialhilfe(?:karte)?|prestação|aid\s*(?:id|number))[\s\b]+[:\-\s]*([A-Z]\d{5,10})",
    "MILITARY_ID": r"(?i)(?:my\s+)?(?:military\s*(?:id|number)|service\s*(?:number|id)|armed\s*forces\s*id|servicenummer|numéro\s*de\s*service|militär(?:ausweis)?)[\s\b]+[:\-\s]*([A-Z]\d{5,10})",
}

test_cases = {
    "DRIVER_LICENSE": [
        "My driver's license is D1234567",
        "Driver's license: D1234567",
        "DL number: D1234567",
    ],
    "VOTER_ID": [
        "My voter ID is V9876543",
        "Meine Wählerausweisnummer ist V9876543",
        "Voter card: V9876543",
    ],
    "RESIDENCE_PERMIT": [
        "My residence permit is RP456789",
        "Residence card: RP456789",
    ],
    "BENEFIT_ID": [
        "My benefit card is B11223344",
        "Meine Sozialhilfekarte ist B11223344",
    ],
    "MILITARY_ID": [
        "My military ID is M55667788",
        "Meine Militärausweis ist M55667788",
    ],
}

for entity_type, pattern_str in patterns.items():
    print(f"\n{entity_type}:")
    pattern = re.compile(pattern_str)
    if entity_type in test_cases:
        for text in test_cases[entity_type]:
            m = pattern.search(text)
            if m:
                print(f'  ✓ "{text}" -> "{m.group(1)}"')
            else:
                print(f'  ✗ "{text}" -> NO MATCH')
