from pii_filter import PIIFilter
pf = PIIFilter()
texts = ["Je m'appelle Rue Victor", "Mein Führerschein ist D1234567", "Meine Aufenthaltsgenehmigung ist RP456789"]
for text in texts:
    print('\nTEXT:', text)
    for rx in pf.INTRO_PATTERNS:
        m = rx.search(text)
        if m:
            print('INTRO PATTERN MATCH:', rx.pattern, '->', m.group(1))
    print('DRIVER_LICENSE_LABEL_RX match:', bool(pf.DRIVER_LICENSE_LABEL_RX.search(text)))
    print('RESIDENCE_PERMIT_LABEL_RX match:', bool(pf.RESIDENCE_PERMIT_LABEL_RX.search(text)))
