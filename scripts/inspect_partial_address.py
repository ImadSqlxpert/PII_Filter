import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pii_filter.pii_filter import PIIFilter

texts = [
    "User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin",
    "User: Street: Baker St.\nNumber: 221B\nCity: London",
]

f = PIIFilter()
for t in texts:
    print('--- TEXT ---')
    print(t)
    add = f._inject_custom_matches(t, [])
    print('--- INJECTIONS ---')
    for r in add:
        print(r.entity_type, r.start, r.end, repr(t[r.start:r.end]))
    print('\nANONYMIZED:')
    print(f.anonymize_text(t))
