import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pii_filter.pii_filter import PIIFilter
pf = PIIFilter()
texts = [
    "Mă numesc Andrei Popescu",
    "Je m'appelle Rue Victor",
]
for t in texts:
    print('TEXT:', t)
    out = pf.anonymize_text(t, guards_enabled=True, guard_requires_context_without_number=True)
    print('ANON:', out)
    # show recognizers
    res = pf._inject_name_intro_persons(t, [])
    print('INJECTED:', res)
    print('---')
