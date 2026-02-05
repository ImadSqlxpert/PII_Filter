import re

# Test different approaches
test_text = "My driver's license is D1234567"

# Approach 1: Use positive lookahead instead of word boundary
pattern1 = r"(?i)(?:my\s+)?(?:driver(?:'?s)?\s*(?:license|licence|lic))\s+(?:is\s+)?([A-Z]\d{5,10})"

# Approach 2: Use \s+ after the label, then optional "is"
pattern2 = r"(?i)(?:my\s+)?(?:driver(?:'?s)?\s*(?:license|licence|lic))(?:\s+is)?[\s:]*([A-Z]\d{5,10})"

# Approach 3: Better spacing
pattern3 = r"(?i)(?:my\s+)?(?:driver(?:'?s)?\s*(?:license|licence|lic))\b(?:\s+is)?[\s:]*([A-Z]\d{5,10})"

patterns_to_test = {
    "pattern1": pattern1,
    "pattern2": pattern2,
    "pattern3": pattern3,
}

for name, pattern in patterns_to_test.items():
    m = re.search(pattern, test_text)
    print(f"{name}: {m is not None}")
    if m:
        print(f"  Match: {m.group(0)}")
        print(f"  Group 1: {m.group(1)}")

# Now test all types with the best approach
print("\n--- Testing with best pattern ---")
best_patterns = {
    "DRIVER_LICENSE": r"(?i)(?:my\s+)?(?:driver(?:'?s)?\s*(?:license|licence|lic)|dl\s*number)\b(?:\s+is)?[\s:]*([A-Z]\d{5,10})",
    "VOTER_ID": r"(?i)(?:my\s+)?(?:voter\s*(?:id|card|number)|wählerausweins?(?:nummer)?)\b(?:\s+ist)?[\s:]*([A-Z]\d{5,10})",
    "RESIDENCE_PERMIT": r"(?i)(?:my\s+)?(?:residence\s*(?:permit|card)|resident\s*permit)\b(?:\s+is)?[\s:]*([A-Z]{2}\d{5,10})",
    "BENEFIT_ID": r"(?i)(?:my\s+)?(?:benefit\s*(?:id|card|number)|sozialhilf(?:e|ekarte))\b(?:\s+is|st)?[\s:]*([A-Z]\d{5,10})",
    "MILITARY_ID": r"(?i)(?:my\s+)?(?:military\s*(?:id|number)|militär(?:ausweis)?)\b(?:\s+is|st)?[\s:]*([A-Z]\d{5,10})",
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

for entity_type, pattern_str in best_patterns.items():
    print(f"\n{entity_type}:")
    pattern = re.compile(pattern_str)
    if entity_type in test_cases:
        for text in test_cases[entity_type]:
            m = pattern.search(text)
            if m:
                print(f'  ✓ "{text}" -> "{m.group(1)}"')
            else:
                print(f'  ✗ "{text}" -> NO MATCH')
