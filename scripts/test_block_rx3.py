import re

text = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

print("Input:", repr(text))
print()

# Let's try different approaches

# Version 1: Keep the original but fix the greedy issue
# The problem is [^\n]*? is still too greedy
rx1 = re.compile(r"(?im)(?:straße|strasse|str\.?|street|st\.?)[:\s]*([^\n:]+)(?:\n\s*(?:nr\.?|no\.?|number|nummer)[:\s]*([^\n:]+))?(?:\n\s*(?:plz\/ort|plz|postal|city|stadt|ort)[:\s]*([^\n:]+))?")

print("Version 1 (match street, optional number+city):")
m = rx1.search(text)
if m:
    print(f"  Matched: {repr(m.group(0))}")
    print(f"  Groups: street={m.group(1)!r}, number={m.group(2)!r}, city={m.group(3)!r}")
else:
    print("  No match")

print()

# Version 2: be very explicit about the structure
# street_label:value\n number_label:value\n city_label:value
rx2 = re.compile(
    r"(?im)"
    r"(?:straße|strasse|str\.?|street|st\.?|adresse|address|rue)\s*:?\s*([^\n]+)"
    r"\n"
    r"(?:nr\.?|no\.?|number|nummer|num)\s*:?\s*([^\n]+)"
    r"\n"
    r"(?:plz\/ort|plz|postal|city|stadt|ort|ville|ciudad)\s*:?\s*([^\n]+)"
)

print("Version 2 (strict label:value format):")
m = rx2.search(text)
if m:
    print(f"  Matched: {repr(m.group(0))}")
    print(f"  Groups: street={m.group(1)!r}, number={m.group(2)!r}, city={m.group(3)!r}")
else:
    print("  No match")

print()
print("Debug: Let's check what each line component has:")
lines = text.split('\n')
for i, line in enumerate(lines):
    print(f"  Line {i}: {repr(line)}")

print()
print("Test case 2:")
text2 = "User: Street: Baker St.\nNumber: 221B\nCity: London"
print(repr(text2))
for i, line in enumerate(text2.split('\n')):
    print(f"  Line {i}: {repr(line)}")

m = rx2.search(text2)
if m:
    print(f"  Syntax 2 matched: {repr(m.group(0))}")
else:
    print("  Syntax 2: No match")
