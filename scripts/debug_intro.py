from pii_filter.pii_filter import PIIFilter
pf = PIIFilter()
texts = [
    "Mă numesc Andrei Popescu",
    "Je m'appelle Rue Victor",
    "Mi chiamo Via Roma",
]
for text in texts:
    print('TEXT:', text)
    injected = pf._inject_name_intro_persons(text, [])
    print('Injected:', injected)
    if 'Andrei' in text:
        s = text.find('Andrei')
        print('prefix:', text[max(0,s-40):s].lower())
        print('has_intro_prefix:', pf._has_intro_prefix(text, s))
        print('plausible:', pf._plausible_person(text[s:], text, s))
    print('---')
