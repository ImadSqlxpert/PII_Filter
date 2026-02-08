from pii_filter import PIIFilter
f = PIIFilter()
examples = [
    "My API key is sk_live_abc123def456",
    "Mein API-Schlüssel ist sk_live_abc123def456",
    "Senden Sie an BTC-Adresse 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
]
for t in examples:
    print('ORIG:', t)
    print('ANON:', f.anonymize_text(t))
    print('---')
    # Debug: show PAYMENT_TOKEN_RX matches and left context heuristics
    for m in f.PAYMENT_TOKEN_RX.finditer(t):
        s = m.start(1) if m.lastindex else m.start()
        left = t[max(0, s-128):s].lower()
        print('MATCH:', m.group())
        print('LEFT_CTX:', repr(left))
        print('HAS api in left?', 'api' in left)
        print('syns present?', [syn for syn in ("key", "schl", "schlu", "schluessel", "schlüssel") if syn in left])
        print('---')
    if 'sk_live' in t:
        print('sk_live index:', t.find('sk_live'))
        print('repr:', repr(t))
        print('surrounding:', repr(t[max(0, t.find('sk_live')-20):t.find('sk_live')+40]))
