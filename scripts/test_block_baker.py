#!/usr/bin/env python
"""Test block_rx on the English case."""

import re

text = 'User: Street: Baker St.\nNumber: 221B\nCity: London'

block_rx = re.compile(
    r"(?im)"
    r"(?:straße|strasse|str\.?|street|st\.?|adresse|address|rue)[:\s]*([^\n:]+)"
    r"(?:\n\s*(?:nr\.?|no\.?|number|nummer|num)[:\s]*([^\n:]+))?"
    r"(?:\n\s*(?:plz\/ort|plz|postal|city|stadt|ort|ville|ciudad)[:\s]*([^\n:]+))?"
)

matches = list(block_rx.finditer(text))
print(f"Block_rx matches: {len(matches)}")

for m in matches:
    print(f"  Full match: {repr(m.group(0))}")
    print(f"  Groups: street={m.group(1)!r}, number={m.group(2)!r}, city={m.group(3)!r}")
    
    if m.group(2) and m.group(3):
        print(f"  -> Would create ADDRESS span")
    else:
        print(f"  -> SKIP (missing number or city)")
