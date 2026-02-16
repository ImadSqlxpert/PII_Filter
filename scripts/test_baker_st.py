#!/usr/bin/env python
"""Quick test for Baker St address."""

import sys
sys.path.insert(0, r'C:\Users\imadi\Desktop\projects\PII_Filter')

from PII_filter.pii_filter import PIIFilter

f = PIIFilter()
chat = "User: Street: Baker St.\nNumber: 221B\nCity: London"
out = f.anonymize_text(chat)

print("Input:", repr(chat))
print("\nOutput:", repr(out))
print("\nFormatted output:")
print(out)

# Check what tags are present
if "<ADDRESS>" in out:
    print("\n✓ ADDRESS tag found")
elif "<PERSON>" in out:
    print("\n✗ Found PERSON instead of ADDRESS")
else:
    print("\n✗ No ADDRESS tag found")
