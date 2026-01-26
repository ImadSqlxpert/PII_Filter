from PII_filter.core import anonymize_text


TEST_TEXTS = {
"English": """
My name is John Smith. I was born on 12/31/1990.
I live at 221B Baker Street, London.
You can reach me at john.smith@example.com or call +44 7700 900123.
U.S. Passport: K12345678
My office IPs are 192.168.1.10 and 2001:0db8:85a3::8a2e:0370:7334.
""",

    "German": """
Mein Name ist Max Mustermann, geboren am 31.12.1990.
Ich wohne in der Musterstraße 5, 10115 Berlin.
Meine E‑Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.
Personalausweisnummer: T22000129
Steuer-ID: 12 345 678 901
USt-IdNr.: DE 123456789
""",

    "German": """
Mein Name ist Max Mustermann, geboren am 31.12.1990.
Ich wohne in der Musterallee 5, 10115 Berlin.
Meine E‑Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.
Personalausweisnummer: T22000129
Steuer-ID: 12 345 678 901
USt-IdNr.: DE 123456789
""",


    "French": """
Je m'appelle Marie Dupont, née le 31-05-1995.
J'habite au 12 rue de Rivoli, 75001 Paris.
Mon email est marie.dupont@gmail.com et mon numéro est 06 12 34 56 78.
Passeport (UE): AB1234567
Mon IPv6 à domicile: 2001:db8::1
""",

    "Spanish": """
Me llamo Carlos García. Nací el 31/12/1990.
Vivo en la Calle Mayor 10, 28013 Madrid.
Mi correo es carlos.garcia@email.com y mi teléfono es +34 612 345 678.
ID No.: X1234567
VAT: ES X1234567T
""",

    "Italian": """
Mi chiamo Luca Rossi. Nato il 1990-06-15.
Abito in Via Roma 22, 00100 Roma.
La mia email è luca.rossi@mail.it e il mio numero è 333 123 4567.
VAT: IT 12345678901
""",

    "Turkish": """
Benim adım Ahmet Yılmaz. Doğum tarihim 01-01-1992.
Adresim Atatürk Caddesi No:15, Ankara.
E‑posta adresim ahmet.yilmaz@example.com ve telefon numaram 0555 123 45 67.
""",

    "Arabic": """
اسمي محمد أحمد، تاريخ الميلاد 1991-07-20.
أسكن في شارع الملك فهد 15، الرياض.
بريدي الإلكتروني هو mohammed.ahmed@email.com ورقم هاتفي +966 55 123 4567.
""",

    "US Tax & IDs": """
Name: Jane Miller. I was born on 31 December 1988.
Address: 742 Evergreen Terrace, 90210 Beverly Hills.
Email: jane.miller@example.org, Phone: +1 (213) 555-0182
SSN: 536-80-4398
SSN (compact): 536804398
ITIN: 912-91-3457
ITIN (compact): 912913457
EIN: 51-2144346
U.S. Passport: Z98765432
My server IP is 10.0.0.12 and IPv6 is 2a02:26f0:fe::5.
""",

    "EU Tax & IDs": """
Je m’appelle Ana Novak. Born: 31 March 1992.
Adresse: Hauptstr. 7, 50667 Köln.
Email: ana.novak@example.eu, Tel: +49 221 987654
TIN: DE 12 345 678 901
VAT: FR 12345678901
VAT: NL 123456789B01
Personalausweis-Nr.: L9X7A2B3C
Passeport (UE): XY7654321
"""
}



def main():
    for language, text in TEST_TEXTS.items():
        print("=" * 60)
        print(f"LANGUAGE: {language}")
        print("- Original:")
        print(text.strip())

        anonymized = anonymize_text(text)

        print("\n- Anonymized:")
        print(anonymized)


if __name__ == "__main__":
    main()
