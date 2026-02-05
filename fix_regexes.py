#!/usr/bin/env python
"""Fix key regexes that are causing excessive false positives."""

# Read the file
with open('PII_filter/pii_filter.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Make EU_PASSPORT_REGEX much stricter
# Old: r'\b(?=[A-Z0-9]{6,9}\b)(?=.*[A-Z])[A-Z0-9]{6,9}\b'
# New: Only match actual EU passport patterns (1-2 letters followed by 6-8 digits)
content = content.replace(
    r'self.EU_PASSPORT_REGEX = r"\b(?=[A-Z0-9]{6,9}\b)(?=.*[A-Z])[A-Z0-9]{6,9}\b"',
    r'self.EU_PASSPORT_REGEX = r"\b[A-Z]{1,2}\d{6,8}\b"'
)

# Write back
with open('PII_filter/pii_filter.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Fixed EU_PASSPORT_REGEX to be much stricter')
