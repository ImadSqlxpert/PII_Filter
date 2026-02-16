#!/usr/bin/env python
"""Test improved block_rx."""

import re

# New pattern
block_rx = re.compile(
    r"(?im)"
    r"(?:straße|strasse|str|street|adresse|address|rue)(?:\.|:|\s)(?:\s*:?\s*)([^\n:]+)"
    r"(?:\n\s*(?:nr|no|number|nummer|num)(?:\.|:|\s)(?:\s*:?\s*)([^\n:]+))?"
    r"(?:\n\s*(?:plz|postal|city|stadt|ort|ville|ciudad)(?:\.|:|\s)(?:\s*:?\s*)([^\n:]+))?"
)

test_cases_with_answers = [
    ('User: Street: Baker St.\nNumber: 221B\nCity: London', True),
    ('User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin', True),
]

for text, should_match in test_cases_with_answers:
    matches = list(block_rx.finditer(text))
    has_valid_match = any(m.group(2) and m.group(3) for m in matches)
    
    status = "✓" if has_valid_match == should_match else "✗"
    print(f"{status} {text[:40]:40s} - Found valid match: {has_valid_match}")
    
    for m in matches:
        if m.group(2) and m.group(3):
            print(f"    Street: {m.group(1)!r}, Number: {m.group(2)!r}, City: {m.group(3)!r}")
