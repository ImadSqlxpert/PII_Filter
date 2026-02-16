import re

text = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

block_rx = re.compile(r"(?im)(?:^|\n)\s*([^\n]*?(?:straße|strasse|str\.?|street|st\.?)[^\n]*)\n\s*([^\n]*?(?:nr\.?|no\.?|number|nummer)[^\n]*)\n\s*([^\n]*?(?:plz\/ort|plz|postal|city|stadt|ort)[^\n]*)")

matches = list(block_rx.finditer(text))
print(f"Number of block matches: {len(matches)}")

for m in matches:
    print(f"  Full match [{m.start()}-{m.end()}]: {repr(m.group(0))}")
    print(f"    Group 1 (street) [{m.start(1)}-{m.end(1)}]: {repr(m.group(1))}")
    print(f"    Group 2 (number) [{m.start(2)}-{m.end(2)}]: {repr(m.group(2))}")
    print(f"    Group 3 (city)  [{m.start(3)}-{m.end(3)}]: {repr(m.group(3))}")
    print(f"  Address span would be: ({m.start(1)}, {m.end(3)})")
    print(f"  That spans: {repr(text[m.start(1):m.end(3)])}")

# Try without the "str\." part
print("\n\nTesting simpler patterns:")
test_patterns = [
    r"(?im)straße",
    r"(?im)nr\.",
    r"(?im)plz\/ort",
]

for p in test_patterns:
    matches = list(re.finditer(p, text))
    print(f"Pattern {p!r}: {len(matches)} matches")
    for m in matches:
        print(f"  [{m.start()}-{m.end()}]: {repr(m.group(0))}")
