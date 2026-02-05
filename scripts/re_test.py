import re
s='Max unter 12.04 an.'
right = s[3:3+24].lower()
print('RIGHT:',repr(right))
print('MATCH:', bool(re.search(r'\bunter\b\s*\d{1,2}[./-]\d{1,2}\b', right)))
