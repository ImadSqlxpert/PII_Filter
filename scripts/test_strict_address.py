from pii_filter.pii_filter import PIIFilter
pf=PIIFilter()
texts=['Königsberger Feld 4','Königsberger Feld 4, 69120 Heidelberg','Königsberger Feld 4 69120 Heidelberg','Heidelberg']
for t in texts:
    print('TEXT:',t)
    for m in pf.STRICT_ADDRESS_RX.finditer(t):
        print(' MATCH ->',repr(m.group()), m.start(), m.end())
    print('---')
