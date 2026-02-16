import re

text = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

block_rx = re.compile(
    r"(?im)"
    r"(?:straße|strasse|str\.?|street|st\.?|adresse|address|rue)[:\s]*([^\n:]+)"
    r"(?:\n\s*(?:nr\.?|no\.?|number|nummer|num)[:\s]*([^\n:]+))?"
    r"(?:\n\s*(?:plz\/ort|plz|postal|city|stadt|ort|ville|ciudad)[:\s]*([^\n:]+))?"
)

m = block_rx.search(text)
if m:
    print(f"Match: {repr(m.group(0))}")
    print(f"  m.start(0)={m.start(0)}, m.end(0)={m.end(0)}")
    print(f"  m.start(1)={m.start(1)}, m.end(1)={m.end(1)} => {repr(m.group(1))}")
    if m.group(2):
        print(f"  m.start(2)={m.start(2)}, m.end(2)={m.end(2)} => {repr(m.group(2))}")
    else:
        print(f"  m.group(2) is None")
    if m.group(3):
        print(f"  m.start(3)={m.start(3)}, m.end(3)={m.end(3)} => {repr(m.group(3))}")
    else:
        print(f"  m.group(3) is None")
    
    # For proper ADDRESS span, we want to include all matched groups
    # Use the span of the outermost group(0) or calculate based on which groups are present
    start = m.start(1)
    if m.group(3):
        end = m.end(3)
    elif m.group(2):
        end = m.end(2)
    else:
        end = m.end(1)
    
    print(f"\nCalculated ADDRESS span: ({start}, {end})")
    print(f"  Value: {repr(text[start:end])}")

else:
    print("No match")
