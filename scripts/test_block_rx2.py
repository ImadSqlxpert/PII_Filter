import re

text = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

# New improved block_rx
block_rx = re.compile(r"(?im)(?:^|\n)\s*(?:straße|strasse|str\.?|street|st\.?|adresse|address|rue)\s*:?\s*([^\n]+)\n\s*(?:nr\.?|no\.?|number|nummer|num)\s*:?\s*([^\n]+)\n\s*(?:plz\/ort|plz|postal|city|stadt|ort|ville|ciudad)\s*:?\s*([^\n]+)")
matches = list(block_rx.finditer(text))

print(f'Number of block matches: {len(matches)}')

for m in matches:
    print(f'  Full match [{m.start()}-{m.end()}]: {repr(m.group(0))}')
    print(f'    Group 1 (street) [{m.start(1)}-{m.end(1)}]: {repr(m.group(1))}')
    print(f'    Group 2 (number) [{m.start(2)}-{m.end(2)}]: {repr(m.group(2))}')
    print(f'    Group 3 (city)  [{m.start(3)}-{m.end(3)}]: {repr(m.group(3))}')
    s, e = m.start(1), m.end(3)
    print(f'  Address span would be: ({s}, {e})')
    print(f'  That spans: {repr(text[s:e])}')

print("\n\nTest case 2 (English):")
text2 = "User: Street: Baker St.\nNumber: 221B\nCity: London"
matches2 = list(block_rx.finditer(text2))
print(f'Number of block matches: {len(matches2)}')
for m in matches2:
    s, e = m.start(1), m.end(3)
    print(f'  Address span: ({s}, {e})')
    print(f'  Spans: {repr(text2[s:e])}')
