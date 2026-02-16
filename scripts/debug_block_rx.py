#!/usr/bin/env python
"""Debug the block_rx regex matching."""

import sys
sys.path.insert(0, r'C:\Users\imadi\Desktop\projects\PII_Filter')

import re

text = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

print("Testing block_rx pattern:")
print(f"Input: {repr(text)}\n")

block_rx = re.compile(
    r"(?im)"
    r"(?:straße|strasse|str\.?|street|st\.?|adresse|address|rue)[:\s]*([^\n:]+)"
    r"(?:\n\s*(?:nr\.?|no\.?|number|nummer|num)[:\s]*([^\n:]+))?"
    r"(?:\n\s*(?:plz\/ort|plz|postal|city|stadt|ort|ville|ciudad)[:\s]*([^\n:]+))?"
)

print(f"Pattern: {block_rx.pattern}\n")

matches = list(block_rx.finditer(text))
print(f"Number of matches: {len(matches)}\n")

for i, m in enumerate(matches):
    print(f"Match {i}:")
    print(f"  Full: {repr(m.group(0))} at [{m.start(0)}-{m.end(0)}]")
    group1 = m.group(1)
    group2 = m.group(2)
    group3 = m.group(3)
    print(f"  G1 (street): {repr(group1)} at [{m.start(1)}-{m.end(1)}]" if group1 else f"  G1: None")
    print(f"  G2 (number): {repr(group2)} at [{m.start(2)}-{m.end(2)}]" if group2 else f"  G2: None")
    print(f"  G3 (city):   {repr(group3)} at [{m.start(3)}-{m.end(3)}]" if group3 else f"  G3: None")
    
    # Calculate address span
    if group2 and group3:
        s = m.start(1)
        if group3:
            e = m.end(3)
        elif group2:
            e = m.end(2)
        else:
            e = m.end(1)
        print(f"  -> ADDRESS span: ({s}, {e}) = {repr(text[s:e])}")
    else:
        print(f"  -> SKIP (group2={group2}, group3={group3})")
    print()

# Now test with the actual PIIFilter
print("\n" + "="*70)
print("Testing with actual PIIFilter:")
from PII_filter.pii_filter import PIIFilter

analyzer = PIIFilter()
out = analyzer.anonymize_text(text)
print(f"Output: {repr(out)}")
print()
print(out)
