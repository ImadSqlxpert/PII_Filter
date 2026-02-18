
#!/usr/bin/env python3
"""
PIIFilter – Full Sanity Runner (class-based)
--------------------------------------------
• Initializes PIIFilter and runs end-to-end pipeline on a multilingual corpus.
• Prints final resolved entities, anonymized output, and a coverage summary.
• CLI flags to pass text/file and guard toggles.

Usage:
  python main_runner.py
  python main_runner.py --text "Musterstraße 5, 10115 Berlin"
  python main_runner.py --file samples.txt --guards-off
  python main_runner.py --json

Requires:
  - presidio-analyzer
  - presidio-anonymizer
  - langdetect
"""

from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
import sys
from pathlib import Path
import textwrap

# -----------------------------
# Ensure project root on sys.path
# -----------------------------
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# -----------------------------
# Safe third-party imports
# -----------------------------
try:
    from langdetect import detect as _ld_detect
    def _detect_lang(text: str) -> str:
        try:
            return _ld_detect(text)
        except Exception:
            return "en"
except Exception:
    def _detect_lang(text: str) -> str:
        return "en"

# Try PIIFilter (class) or anonymize_text (function)
pf_class = None
anonymize_fn = None
try:
    from pii_filter.pii_filter import PIIFilter as _PF
    pf_class = _PF
except Exception:
    pass

if anonymize_fn is None:
    try:
        from pii_filter.pii_filter import anonymize_text as _ANON
        anonymize_fn = _ANON
    except Exception:
        pass

if pf_class is None and anonymize_fn is None:
    raise ImportError(
        "Failed to import PIIFilter or anonymize_text.\n"
        "Ensure package exists at: PII_filter/core.py and that you run from the project root."
    )

# Presidio result type (for type hints/pretty-printing)
try:
    from presidio_analyzer import RecognizerResult
except Exception:
    # Minimal fallback struct if Presidio isn't importable (for pretty-print only)
    @dataclass
    class RecognizerResult:
        entity_type: str
        start: int
        end: int
        score: float = 0.0


# -------------------------------------------------------------
# Large multilingual PII test corpus (expanded German coverage)
# -------------------------------------------------------------
TEST_TEXTS = {
    "English": """
My name is John Smith. I was born on 12/31/1990.
I live at 221B Baker Street, London.
You can reach me at john.smith@example.com or call +44 7700 900123.
U.S. Passport: K12345678
My office IPs are 192.168.1.10 and 2001:0db8:85a3::8a2e:0370:7334.
""",

    "German - Basics": """
Mein Name ist Max Mustermann, geboren am 31.12.1990.
ich Heisse Max Mustermann und ich bin am 31.12.1990 geboren.
ich heisse Max Mustermann und ich bin am 31.12.1990 geboren.
ich heisse max mustermann und ich bin am 31.12.1990 geboren.
Ich wohne in der Musterstraße 5, 10115 Berlin (Mitte).
Meine E-Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.
Personalausweisnummer: T22000129
Steuer-ID: 12 345 678 901
USt-IdNr.: DE 123456789
ich will Gewerbe anmelden.
ich bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
Ich Bin Anna Müller und ich wohne in der Blablastrasse 9, Berlin 10999. Ich will ein Gewerbe anmelden
ich Bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
ich bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
ich Bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
Guten Tag, mein name ist Frank Verz, ich möchte ein Gewerbe anmelden.
Gibt es Beratungszentern in Tempelhof-Shöneberg für Gründung von Unternehmen?
"Ich bin beschäftigt."
"Ich bin nicht beschäftigt."
"Ich bin heute beschäftigt."
"Ich bin beschäftigt heute."
"Ich bin sehr beschäftigt."
"Ich bin beschäftigt sehr"
"Ich bin beschäftigt einfach."
"Ich bin einfach beschäftigt."
"Ich bin Beschäftigt."
"Ich bin mark beschäftigt."
"Ich bin beschäftigt schmidt."
"Ich bin Mark Beschäftigt."
"Ich bin Beschäftigt Schmidt."
""",

    "German - Street Variants": """
Adresse: Am Waldrand 12, 50667 Köln.
Ich wohne Im Tal 7; An der See 3 (OH).
Unter den Linden 77, 10117 Berlin.
Karl-Marx-Allee 1, 10243 Berlin.
Lange Reihe 15, 20099 Hamburg.
Gänsemarkt 2, 20354 Hamburg.
Königsberger Feld 4, 69120 Heidelberg.
""",

    "German - Apartment/Unit Suffixes": """
Musterstraße 10, Whg. 5, 2. Etage, 01067 Dresden.
Hauptstraße 12, Stiege 2, Top 14, 2. OG, 1010 Wien.
""",

    "German - Postal & Location": """
DE-10115 Berlin (Mitte)
50667 Köln
20095 Hamburg (Altstadt)
""",

    "German - Payments/Bank": """
Visa 4111 1111 1111 1111
IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX
Kontonummer: 1234-567890-12
""",

    "German - Communications": """
Fax: +49 30 1234567
Meeting ID: 987 654 321
Twitter @hans_muell3r
Discord hans#1234
Google Meet: abc-defg-hij
""",

    "German - Devices/Network": """
IP: 192.168.1.10 und IPv6: 2001:db8::1
MAC 00:1A:2B:3C:4D:5E; IMEI 490154203237518
IDFA: 123e4567-e89b-12d3-a456-426614174000, Gerät-ID: 123e4567-e89b-12d3-a456-426614174001
""",

    "German - Geo/Locations": """
Koordinaten: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft
Kennzeichen: B-AB 1234
""",

    "German - Edge Cases": """
Ich wohne in Müritzsee.
Meine Adresse: Schwabental
Ich heiße Anna Gasse.
Ruf mich unter 12-03-2023 an.
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

    "Turkish": """
Benim adım Ahmet Yılmaz. Doğum tarihim 01-01-1992.
Adresim Atatürk Caddesi No:15, Ankara.
E‑posta adresim ahmet.yilmaz@example.com ve telefon numaram 0555 123 45 67.
""",

    "Arabic": """
اسمي أحمد محمد. ولدت في 31/12/1990.
أعيش في شارع الملك فيصل 20، الرياض 12345.
بريدي الإلكتروني ahmed.mohamed@example.com ورقم هاتفي +966 50 123 4567.
جواز السفر: A12345678
عنوان IP الخاص بي: 192.168.1.10
""",

    "US Tax & IDs": """
Name: Jane Miller. I was born on 31 December 1988.
Address: 742 Evergreen Terrace, 90210 Beverly Hills.
Email: jane.miller@example.org, Phone: +1 (213) 555-0182
SSN: 536-80-4398
ITIN: 912-91-3457
EIN: 51-2144346
U.S. Passport: Z98765432
My server IP is 10.0.0.12 and IPv6 is 2a02:26f0:fe::5.
""",

    "Payments": """
Visa 4111 1111 1111 1111, Amex 3782 822463 10005.
IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX.
Routing (ABA): 021000021. Kontonummer: 1234-567890-12.
API key: sk_live_abcDEF1234567890; Stripe pub: pk_test_1xYzABC1234567890
""",

    "Crypto": """
BTC: 1BoatSLRHtKNngkdXEeobR76b53LETtpyT,
bech32: bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kygt080,
ETH: 0x52908400098527886e0f7030069857d2e4169ee7
""",

    "Health": """
NHS number 943 476 5919, MRN: ABC-123456, Insurance policy: POL-987654321.
Diagnosed with diabetes. Blood type: O+.
""",

    "Comms/Devices/Geo": """
Twitter @john_doe123, email john.doe@acme.io, Discord user#1234,
Meeting ID: 987 654 321, Meet code: abc-defg-hij.
MAC 00:1A:2B:3C:4D:5E, IMEI 490154203237518, IDFA: 123e4567-e89b-12d3-a456-426614174000.
Coords: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft; Kennzeichen: B-AB 1234
""",

    "Commercial Register (European)": """
# German
Amtsgericht München, Handelsregister B 123456
Registergericht Dresden, Abteilung B, HRB 234567
Das Unternehmen ist eingetragen im Handelsregister beim Amtsgericht München, Abteilung B, HRA 345678.

# French
Tribunal de Commerce Paris, Registre B 567890
RCS Paris B 678901
L'entreprise est immatriculée au RCS Paris, section B sous le numéro 789012.

# Spanish
Registro Mercantil Madrid, Sección B 890123
Reg. Merc. Barcelona, Secc. A 901234
La sociedad está inscrita en el Registro Mercantil de Madrid, sección B, número 012345.

# Italian
Registro delle Imprese Roma, Sezione B 123456
REA Roma 234567
L'impresa è iscritta nel Registro delle Imprese di Roma, sezione B, numero 345678.

# Dutch
Handelsregister Amsterdam, Afdeling B 456789
KVK Amsterdam 567890
Het bedrijf staat ingeschreven in het Handelsregister van Amsterdam, afdeling B, nummer 678901.
""",

    "Case Reference (Multilingual)": """
# English
Case ID: CASE-2023-001234
Reference Number: REF-2024-567890
Ticket ID: TKT-2024-999
Customer Number: CUST-2023-55555

# German
Aktenzeichen: AZ-2023-123456
Vorgangsnummer: VN-2024-789012
Kundennummer: KN-2023-456789

# French
Numéro de dossier: ND-2024-001
Dossier #DOSS-2023-999

# Spanish
Número de expediente: EXP-2023-999
Expediente #EXP-2024-111

# Italian
Numero pratica: PR-2024-555
Pratica #PRT-2023-222

# Turkish
Dosya numarası: DN-2023-777
Dosya #DOS-2024-333

# Arabic
رقم القضية: RQ-2024-333
رقم القضية #RQ-2023-444
""",

    "German E-Government IDs": """
# BundID (German Federal Digital Identity)
BundID: BUND-12345678-ABCD
Bundidentität BUND-87654321-WXYZ
Bundesausweis-ID: BUND-11111111-1111
Digital Identity: BUND-99999999-ZYXW

# ELSTER (Elektronische Steuererklärung - German tax system)
ELSTER-ID: ELST-12345
ELSTER Login: elster_user_12345
ELSTER-Benutzername: user.name@example
elster_konto_abcd1234

# Servicekonto (German government service account)
Servicekonto-ID: SK-2024-001234
Service-Konto: servicekonto_56789
Service Account: SK-2025-009876
Servicekonto: 123456789
Konto-ID: account_gov_12345
Government-Account: gov_12345678
""",
    "Authentication Secrets": """
# English passwords
Password: MySecureP@ss2024!
pwd: Complex$Pass#123
User password: AlphaNum3r1c@Secure
Password is SuperStr0ng!Key#2025

# English PINs
PIN: 1234
PIN: 5678
PIN: 9012
Personal ID Number: 3456

# English TANs
TAN: 654321
transaction-authentication-number: 789012
TAN code: 345678

# English PUKs
PUK: 12345678
pin-unlock-key: 87654321
PUK-code: 55555555

# English Recovery codes
recovery-code: ABC-DEF-123-456
backup-code: XYZ-ABC-789-012
recovery: ABCD-EFGH-IJKL-MNOP
recovery-code: 1234-5678-9012-3456

# German passwords
Passwort: SicherP@ssw0rt2024!
Kennwort: KomplexesK3nnw0rt#GmbH
pwd: Deutsch$Pass123Sicher
Passwort ist GesamterW@rt!Schutz

# German PINs
PIN: 4567
PIN-Code: 8901
PIN: 2345
personal id number: 6789

# German TANs
TAN: 765432
TAN: 098765
TAN-Code: 456789
TAN: 012345

# German PUKs
PUK: 23456789
PUK: 98765432
PUK-Code: 66666666
PUK: 22222222

# German Recovery codes
recovery-code: DEF-GHI-234-567
backup-code: BCD-EFG-890-123
recovery: BCDE-FGHI-JKLM-NOPQ
recovery-code: 2345-6789-0123-4567

# French passwords
Mot de passe: MotDePasse@Secure2024
Mot de passe: ComplicedPass#456French
pwd: French$Pass789Secure
Mot de passe est ComplexeFrEnc@Protected

# French PINs
PIN: 1111
code-secret: 2222
Code PIN: 3333
personal identification number: 4444

# French TANs
TAN: 654987
TAN: 321654
Numero TAN: 789123
Code Authentification: 456789

# French PUKs
PUK: 34567890
PUK: 09876543
Code PUK: 77777777
PUK: 33333333

# French Recovery codes
recovery-code: GHI-JKL-345-678
backup-code: HIJ-KLM-901-234
recovery: CDEF-GHIJ-KLMN-OPQR
recovery-code: 3456-7890-1234-5678

# Spanish passwords
pwd: SpanishPass@Segura2024!
pwd: SpanishComplex#789Pass
pwd: Spanish$Pass456Secure
pwd: SpanishComplete@Protected

# Spanish PINs
PIN: 5555
code-secret: 6666
Codigo PIN: 7777
personal identification number: 8888

# Spanish TANs
TAN: 543216
TAN: 210543
Numero TAN: 678912
Codigo Autenticacion: 345678

# Spanish PUKs
PUK: 45678901
PUK: 10987654
Codigo PUK: 88888888
Codigo Desbloqueo: 44444444

# Spanish Recovery codes
recovery-code: JKL-MNO-456-789
backup-code: KLM-NOP-012-345
recovery: DEFG-HIJK-LMNO-PQRS
recovery-code: 4567-8901-2345-6789

# Italian passwords
pwd: ItalianSecure@2024!
pwd: ItalianComplex#789Pass
pwd: Italiano$Pass123Secure
pwd: ItalianComplete@Protected

# Italian PINs
PIN: 9999
code-secret: 1010
Codice PIN: 1111
personal identification number: 1212

# Italian TANs
TAN: 432109
TAN: 109432
Numero TAN: 567891
Codice Autenticazione: 234567

# Italian PUKs
PUK: 56789012
PUK: 21098765
Codice PUK: 99999999
Chiave Sblocco: 55555555

# Italian Recovery codes
recovery-code: MNO-PQR-567-890
backup-code: NOP-QRS-123-456
recovery: EFGH-IJKL-MNOP-QRST
recovery-code: 5678-9012-3456-7890

# Turkish passwords
pwd: TurkishSecure2024@Pass
pwd: TurkishComplex#890Pass
pwd: Turkish$Pass789Secure
pwd: TurkishComplete@Protected

# Turkish PINs
PIN: 1313
PIN: 1414
PIN: 1515
personal id: 1616

# Turkish TANs
TAN: 321098
TAN: 098321
TAN: 456789
TAN: 123456

# Turkish PUKs
PUK: 67890123
PUK: 32109876
PUK: 1010101
PUK: 66666666

# Turkish Recovery codes
recovery-code: PQR-STU-678-901
backup-code: QRS-TUV-234-567
recovery: FGHI-JKLM-NOPQ-RSTU
recovery-code: 6789-0123-4567-8901

# Arabic passwords
pwd: SecurePass2024@Arabic
pwd: ComplexPass#789Arabic
pwd: Arabic$Pass789Secure
pwd: ArabicSecurePass@Protected

# Arabic PINs
PIN: 1717
PIN: 1818
PIN: 1919
PIN: 2020

# Arabic TANs
TAN: 210987
TAN: 987210
TAN: 345678
TAN: 012345

# Arabic PUKs
PUK: 78901234
مفتاح-فتح-الحظر: 43210987
# Arabic PUKs
PUK: 78901234
PUK: 43210987
PUK: 1111111
PUK: 77777777

# Arabic Recovery codes
recovery-code: STU-VWX-789-012
backup-code: TUV-WXY-345-678
recovery: GHIJ-KLMN-OPQR-STUV
recovery-code: 7890-1234-5678-9012
""",

    "API & Authentication Tokens": """
# API Keys
API Key: sk_live_abcDEF1234567890ghijkl
api_key: sk_test_9876543210fedcbaZYXW
AWS_ACCESS_KEY_ID: AKIAIOSFODNN7EXAMPLE
GitHub Token: ghp_1234567890abcdefghijklmnopqrstuvwxyz
Stripe API: rk_live_abcd1234efgh5678ijkl9012mnop3456
Google API Key: AIzaSyDxKmE5R4L9JqR7vJlR3V9p8q9r0s1t2u3v

# Access Tokens (OAuth, JWT, Bearer)
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U
access_token: ya29.a0AfH6SMBx1234567890abcdefghijklmnopqrstuvwxyz
OAuth Token: ac2220a67b28eb907d90d07f051875275cab6b20
Auth Token: 4517d1f2-4f81-4e1d-a6a8-c5c9d1b3f5d7

# Refresh Tokens
refresh_token: 1//0gxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
refresh_token: AQAB5Hxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
rt_live_abcdef1234567890ghijklmnop9876543210

# Session IDs
PHPSESSID: 9a1f6d3a8e4b7c2f5d9b1a3e6c8f2b5d
session_id: sess_1234567890abcdefghijklmnop
jsessionid: D1C1234567890ABCDEF1234567890AB

# OTP & 2FA Codes
OTP Code: 123456
2FA Code: 987654
Time-based OTP: 546374
One-time password: 234567
Authentication code: 765432
verification_code: 654321

# Device/Client IDs
Device ID: 12345a6b-78cd-90ef-ghij-klmnopqrst12
client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
IDFA: 550e8400-e29b-41d4-a716-446655440000
Android ID: 7a1b8c9d0e1f2a3b4c5d6e7f
Device Identifier: AABBCCDDEE11223344556677
""",

    "Government & Official IDs": """
# Driver Licenses
Driver License: D12345678
DL: CA1234567
Driving License: 1234567/ABC/2015/00123
License Number: SMITH121080A1A2
EU Driver License: 1234567/19/AB/CD

# Voter ID
Voter ID: VID123456789
Voter Registration: VOT-2024-987654
Electoral Card: 123-456-789-012
Voter Number: VN-2024-554433

# Residence Permit / Visa
Residence Permit: RP-2024-123456
Visa Number: V123456789
Permit Number: P-2024-999888
Aufenthaltserlaubnis: AE-2024-555666
Travel Document: TD-2024-111222

# Military ID
Military ID: MIL-2024-777888
Service Number: SN-2024-333444
Armed Forces ID: AF-2024-666777
Military Service Number: MSN-1990-234567
Defence ID: DEF-2024-888999

# Professional & Education IDs
Employee ID: EMP-2024-123456
Staff Number: STF-2024-555666
Mitarbeiternummer: MIT-2024-778899
Student Number: STU-2024-456789
Student ID: 20240987654
Enrollment Number: ENR-2024-112233
University ID: UNI-2024-334455

# Professional Licenses
Professional License: LIC-2024-567890
License Number: PROF-000123456
Contractor License: CTR-2024-777888
Medical License: MED-2024-999000
Architect License: ARC-2024-111222
Professional Registration: PRF-2024-333444

# Benefit & Social IDs
Benefit ID: BEN-2024-123456
Social Security: SOC-2024-654321
Unemployment Benefit: UNE-2024-987654
Welfare ID: WEL-2024-456789
Child Benefit: CHB-2024-321456
Pension ID: PEN-2024-654987
""",

    "Location & Geographic Codes": """
# Geographic Coordinates
Coordinates: 40.7128, -74.0060
Lat/Long: 51.5074, -0.1278
GPS: 35.6892, 139.6917
Location: 48.8566, 2.3522

# Plus Codes (Google)
Plus Code: 9C3W9QCJ+2V
plus_code: 8QQH+RR Lagos
location_code: 7PHWJ4WJ+M2

# What3Words Addresses
w3w: ///index.home.raft
what3words: ///filled.count.soap
w3w address: ///puffin.limits.jugs
what3words location: ///sorted.magic.spanned

# Postal Codes as Location
Postcode: SW1A 2AA
Zip Code: 94105
PLZ: 10115
Code Postal: 75001
Postal: 28013
""",

    "Financial & Routing": """
# Routing Numbers
Routing Number: 021000021
ABA: 123456789
Bank Routing: 061000146
Transit Number: 001005124

# File & Reference Numbers
File Number: FILE-2024-123456
Case Number: CASE-2024-987654
Reference Number: REF-2024-555666
Document Number: DOC-2024-777888
Ticket Number: TKT-2024-111222
Dossier Number: DOSS-2024-333444
Invoice Number: INV-2024-999000
Order Number: ORD-2024-456789
Transaction ID: TXN-2024-654321
""",

    "Extended Government & Education IDs": """
# Voter ID (V + 7 digits)
My voter ID is V1234567
Voter ID: V9876543
Wählerausweis: V1122334
Meine Wählerausweinnummer: V4455667
Voter card: V7788990

# Residence Permit (RP + 6 digits)
Residence permit: RP123456
My residence permit is RP654321
Aufenthaltserlaubnis: RP999888
Aufenthaltstitel: RP333444
Titre de séjour: RP777888
Permiso de residencia: RP666777

# Benefit ID (B + 8 digits)
My benefit ID is B12345678
Sozialhilfe: B65432100
Carte d'allocataire: C98765432
Allocations familiales: A55566677

# Military ID (M + 8 digits)
Military ID: M45678901
Service number: M99900011
Militärausweis: M33344455
Meine Militärnummer: M66677788
Carte militaire: M88899900

# Student Number (STU- + 5 digits)
Student number: STU-12345
My student ID is STU-54321
Matrikelnummer: STU-55666
Immatriculación: STU-77888
Numero di matricola: STU-99000

# Employee ID (EMP- + 5 digits)
Employee ID: EMP-78901
Staff ID: EMP-45678
Personalnummer: EMP-12345
Numéro d'employé: EMP-33444
Número de empleado: EMP-66677

# Device ID (DEV- + 9 digits)
Device ID: DEV-123456789
My device ID is DEV-987654321
UDID: DEV-555666777
Device identifier: DEV-444555666

# EORI (English, German, French, Spanish, Italian)
EORI: DE123456789
EORI DE 123456789
My EORI is DE123456789000
EORI: FR123456789
EORI: IT987654321
EORI ES 111222333
Numéro d'établissement: NE ES 444555666
""",

    "Healthcare & Administrative IDs": """
# Tax ID / VAT Numbers (European VAT formats)
Steuer-ID: DE 123456789
VAT: GB 987654321
Tax Number: FR 1234567890
Partita IVA: IT 12345678901
NIF: ES A12345678
Tax ID: CH CHE 123456789 TVA

# Health ID / NHS Numbers (3-digit groups)
Health ID: 943 476 5919
NHS Number: 456 789 1234
Patient ID: 123 456 7890
Health record: 789 012 3456

# Medical Record Number (MRN) (3 letters - 6 digits)
MRN: ABC-123456
Medical Record: DEF-456789
MRN Number: GHI-789012
Patient Record: JKL-234567
Dossier Médical: MNO-567890

# Insurance ID (label-based or POL-XXXXXXXXX format)
INSURE123456789
Insurance ID Policy123456
Policy: INSURE987654321
Insurance member: MYINSUR1234567


# Health Information (medical conditions/terms)
Diagnosed: Diabetes Type 2
Patient has allergies: Penicillin and Latex
Blood type: O positive
Medications: Insulin, Metformin
Prescription: Hypertension treatment
Condition: Diagnosed with cancer

# Social Media Handles (Twitter, Discord, etc.)
Follow @john_smith on Twitter
My handle is @mary_j_watson
Contact me at @alex_dev_2024
Discord user: @techie_coder_789

# Messaging IDs (Discord user#0000, Telegram, Signal, etc.)
Discord: john_doe#1234
My Skype: user_123_skype
Telegram: @signal_user_456
Signal contact: wave_user_789
Telegram ID: telegram_dev_2024
Skype: alice.work.domain
Line: line_user_9999

# License Plates (Multilingual European formats)
Kennzeichen: B-AB 1234
License Plate: AB 12 CDE
Immatriculation: AZ-123-AB
Targa: CA 123 AB
Registration: BA 1234 CD
Plaque: YZ 234 XY

# File Numbers (Dossier, Case, Expediente, Aktenzeichen)
File Number: FILE2024001234
Dossier: DOSS2024999888
Case Number: CASE2024777666
Reference: REF2024555444
Aktenzeichen: AZ2024333222
Dossier Number: DOSS2024111000
Fascicolo: FASC2024456789

# Ticket / Issue Numbers (Issue, Task, Ticket, Problem)
Issue Number: ISSUE2024001
Ticket ID: TKT2024999
Task Number: TASK2024888
Problem ID: PROB2024777
Ticketnummer: TKT2024666
Issue ID: ISSUE2024555
Tâche: TASK2024444
""",

    "some examples:": """
Mein Name ist Max Mustermann, geboren am 31.12.1990.
ich Heisse Max Mustermann und ich bin am 31.12.1990 geboren.
ich heisse Max Mustermann und ich bin am 31.12.1990 geboren.
ich heisse max mustermann und ich bin am 31.12.1990 geboren.
Personalausweisnummer: T22000129
Steuer-ID: 12 345 678 901
Ich wohne in der Musterstraße 5, 10115 Berlin (Mitte).
USt-IdNr.: DE 123456789
""",

    "some examples 2:": """
ich will Gewerbe anmelden.
ich bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
Ich Bin Anna Müller und ich wohne in der Blablastrasse 9, Berlin 10999. Ich will ein Gewerbe anmelden
ich Bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
ich bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
ich Bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? Ich will ein Gewerbe anmelden
Guten Tag, mein name ist Frank Verz, ich möchte ein Gewerbe anmelden.
Meine E-Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.
Personalausweisnummer: T22000129
""",

    "some examples 3:": """
Gibt es Beratungszentern in Tempelhof-Shöneberg für Gründung von Unternehmen?
Gibt es in Tempelhof-Shöneberg Beratungsstellen für Gastronomiebetriebe?
Hallo mein Name ist lukas fuchs. Meine Personalausweisnummer ist L01X00T47. Ich möchte einen neuen Personalausweis beanragen
Hallo mein Name ist lukas fuchs. Meine Personalausweisnummer ist L01X00T47. Ich möchte einen neuen Personalausweis beantragen
Ich bin Elektriker und habe meine Ausbildung in Polen gemacht. Wie geht das mit Anerkennung?
""",
    "some examples 4:": """
Ich bin beschäftigt.
Ich bin nicht beschäftigt.
Ich bin heute beschäftigt.
Ich bin beschäftigt heute.
Ich bin sehr beschäftigt.
Ich bin beschäftigt sehr
Ich bin beschäftigt einfach.
Ich bin einfach beschäftigt.
Ich bin Beschäftigt."
Ich bin mark und bin beschäftigt.
Ich bin Mark und bin beschäftigt.
Ich bin schnell.
Ich bin nicht schnell.
Ich bin heute schnell.
Ich bin schnell heute.
Ich bin sehr schnell.
Ich bin schnell sehr
Ich bin schnell einfach.
Ich bin einfach schnell.
Ich bin Schnell."
Ich bin mark und bin schnell.
Ich bin Mark und bin schnell.
Ich bin mark.
Ich bin Mark.
Ich bin mark schmidt.
Ich bin Mark schmidt.
Ich bin mark Schmidt.
Ich bin Mark Schmidt.
Ich bin beschäftigt schon.
Ich bin schon beschäftigt.
Ich bin schnell schon.
Ich bin schon schnell.

""",
"some examples 5:": """
Ich will mich selbstständig machen – muss ich dafür überhaupt ein Gewerbe anmelden?
Ich möchte einen kleinen Imbiss eröffnen – welche Genehmigungen brauche ich dafür in Berlin?
Ich ziehe mit meinem Business um – wo melde ich die neue Adresse für mein Gewerbe an?
Ich will für Firmen alten Schrott und Abfälle abholen und wegbringen – brauche ich dafür eine Erlaubnis oder Anmeldung?
Ich habe meinen Abschluss im Ausland gemacht – wie kann ich meinen Beruf in Berlin anerkennen lassen, damit ich arbeiten darf?
Gibt es Beratungszentern in Tempelhof-Shöneberg für Gründung von Unternehmen?
Gibt es in Tempelhof-Shöneberg Beratungsstellen für Gastronomiebetriebe?
Meine E-Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.
Steuer-ID: 12 345 678 901
Ich wohne in der Musterstraße 5, 10115 Berlin (Mitte).
Ich möchte einen kleinen Imbiss eröffnen.
Die Adresse wäre Karl-Marx-Straße 201, 12055 Berlin.
Welche Genehmigungen brauche ich dafür in Berlin?
ich betreibe ein Gewerbe unter der Nummer GEW-2025-7788.
Ich ziehe mit meinem Business um – wo melde ich die neue Adresse für mein Gewerbe an?
ich habe meinen Abschluss als Elektriker in Polen gemacht und bin am 21.08.1995 geboren.
Wie kann ich meinen Beruf in Berlin anerkennen lassen, damit ich arbeiten darf?
 
""",

}

# -------------------------------------------------------------
# Runner class
# -------------------------------------------------------------
class PIIRunner:
    """Full-featured runner using PIIFilter’s internal pipeline."""

    def __init__(self, pf: _PF | None = None):
        # Prefer class instance for full entity resolution; fallback to function for anonymization only.
        self.pf = pf if pf else (pf_class() if pf_class else None)
        self.coverage = Counter()

    @staticmethod
    def _pretty_entities(text: str, entities: list[RecognizerResult]) -> str:
        if not entities:
            return "  - None"
        out = []
        for r in entities:
            snippet = text[r.start:r.end].replace("\n", "\\n")
            out.append(f"  - {r.entity_type:<18} [{r.start}:{r.end}] '{snippet}' (score={getattr(r, 'score', 0):.2f})")
        return "\n".join(out)

    def _pipeline_entities(
        self,
        text: str,
        *,
        guards_enabled: bool = True,
        guard_natural_suffix_requires_number: bool = True,
        guard_single_token_addresses: bool = True,
        guard_address_vs_person_priority: bool = True,
        guard_requires_context_without_number: bool = True,
        guard_context_window: int = 40,
    ) -> list[RecognizerResult]:
        """
        Mirrors PIIFilter.anonymize_text up to 'final' resolved entities (before anonymizer replace).
        Requires PIIFilter class; if only a function is available, this method is unsupported.
        """
        if not self.pf:
            raise RuntimeError("Entity analysis requires PIIFilter class. Only anonymize_text function is available.")

        pf = self.pf
        lang = _detect_lang(text)
        if lang not in getattr(pf.analyzer, "supported_languages", {"en"}):
            lang = "en"

        # Base
        base = pf.analyzer.analyze(
            text=text,
            language=lang,
            entities=pf.ALLOWED_ENTITIES,
            score_threshold=0.50
        )

        # PERSON cleanup (trim intro + plausibility)
        filtered = []
        for r in base:
            if r.entity_type == "PERSON":
                span = text[r.start:r.end]
                trimmed, offset = pf._trim_intro(span)
                if offset > 0:
                    ns = r.start + offset
                    if (r.end - ns) >= 2:
                        r = RecognizerResult("PERSON", ns, r.end, r.score)
                        span = trimmed
                if not pf._plausible_person(span, text, r.start):
                    continue
            filtered.append(r)

        # Intro persons
        filtered = pf._inject_name_intro_persons(text, filtered)

        # Custom injections
        final = pf._inject_custom_matches(text, filtered)

        # Address guards
        if guards_enabled:
            if guard_natural_suffix_requires_number:
                final = pf._guard_natural_suffix_requires_number(text, final, pf.NATURAL_SUFFIXES)
            if guard_single_token_addresses:
                final = pf._guard_single_token_addresses(text, final)
            if guard_address_vs_person_priority:
                final = pf._guard_address_vs_person(final)
            if guard_requires_context_without_number:
                final = pf._guard_requires_context(text, final, pf.ADDRESS_CONTEXT_KEYWORDS, guard_context_window)

        # Phone/date demotion + meeting promotion
        final = pf._demote_phone_over_date(text, final)
        final = pf._promote_meeting_over_phone(text, final, window=24)

        # Address trimming + ID false-positive filtering
        final = pf._trim_address_spans(text, final)
        final = pf._filter_idnumber_false_positives(text, final)

        # Merge address/location
        final = pf._merge_address_location(text, final)

        return sorted(final, key=lambda r: (r.start, r.end))

    def anonymize(
        self,
        text: str,
        *,
        guards_enabled: bool = True,
        guard_natural_suffix_requires_number: bool = True,
        guard_single_token_addresses: bool = True,
        guard_address_vs_person_priority: bool = True,
        guard_requires_context_without_number: bool = True,
        guard_context_window: int = 40,
    ) -> str:
        """Public anonymization using PIIFilter (class or function)."""
        if self.pf:
            return self.pf.anonymize_text(
                text,
                guards_enabled=guards_enabled,
                guard_natural_suffix_requires_number=guard_natural_suffix_requires_number,
                guard_single_token_addresses=guard_single_token_addresses,
                guard_address_vs_person_priority=guard_address_vs_person_priority,
                guard_requires_context_without_number=guard_requires_context_without_number,
                guard_context_window=guard_context_window,
            )
        elif anonymize_fn:
            # Fallback: function-based anonymization (no guards toggles supported unless function supports them)
            try:
                return anonymize_fn(text)
            except TypeError:
                # If function signature differs, just pass text
                return anonymize_fn(text)
        else:
            raise RuntimeError("No PIIFilter class or anonymize_text function available.")

    def run_on_texts(
        self,
        corpus: dict[str, str],
        *,
        show_entities: bool = True,
        show_anonymized: bool = True,
        guards_enabled: bool = True,
        guard_natural_suffix_requires_number: bool = True,
        guard_single_token_addresses: bool = True,
        guard_address_vs_person_priority: bool = True,
        guard_requires_context_without_number: bool = True,
        guard_context_window: int = 40,
        json_mode: bool = False,
    ) -> None:
        """Run on a dict of label->text; print entity lists, anonymized text, and coverage."""
        print("=" * 100)
        print("PIIFilter – Full Sanity Runner")
        print("=" * 100)

        for i, (label, text) in enumerate(corpus.items(), start=1):
            print(f"\n[{i}/{len(corpus)}] {label}")
            print("-" * 100)
            print("Original:")
            print(textwrap.indent(text.strip(), "  "))

            if not self.pf and not anonymize_fn:
                print("\n(No PIIFilter available; cannot analyze or anonymize)")
                continue

            try:
                # Compute anonymized first
                anonymized = None
                if show_anonymized:
                    anonymized = self.anonymize(
                        text,
                        guards_enabled=guards_enabled,
                        guard_natural_suffix_requires_number=guard_natural_suffix_requires_number,
                        guard_single_token_addresses=guard_single_token_addresses,
                        guard_address_vs_person_priority=guard_address_vs_person_priority,
                        guard_requires_context_without_number=guard_requires_context_without_number,
                        guard_context_window=guard_context_window,
                    )
                    print("\nAnonymized:")
                    print(textwrap.indent(anonymized, "  "))

                if self.pf and show_entities:
                    ents = self._pipeline_entities(
                        text,
                        guards_enabled=guards_enabled,
                        guard_natural_suffix_requires_number=guard_natural_suffix_requires_number,
                        guard_single_token_addresses=guard_single_token_addresses,
                        guard_address_vs_person_priority=guard_address_vs_person_priority,
                        guard_requires_context_without_number=guard_requires_context_without_number,
                        guard_context_window=guard_context_window,
                    )
                    if json_mode:
                        # Minimal JSON lines per entity
                        import json
                        print("\nEntities (JSON):")
                        j = [
                            {
                                "entity_type": r.entity_type,
                                "start": r.start,
                                "end": r.end,
                                "text": text[r.start:r.end],
                                "score": getattr(r, "score", 0.0),
                            }
                            for r in ents
                        ]
                        print(textwrap.indent(json.dumps(j, ensure_ascii=False, indent=2), "  "))
                    else:
                        print("\nEntities:")
                        print(self._pretty_entities(text, ents))

                    # coverage
                    for e in ents:
                        self.coverage[e.entity_type] += 1

            except Exception as exc:
                print(f"\n⚠️ Error analyzing/anonymizing: {exc}")
                if anonymize_fn and show_anonymized:
                    print("\nFallback anonymized:")
                    print(textwrap.indent(anonymize_fn(text), "  "))

        print("\n" + "=" * 100)
        print("Coverage summary (entity types observed)")
        print("=" * 100)
        if self.coverage:
            for ent, count in self.coverage.most_common():
                print(f"{ent:<18} {count}")
        else:
            print("No entities detected.")
        print("=" * 100)

    # Convenience: run text twice (guards ON vs OFF) to compare
    def compare_guards(self, text: str) -> None:
        print("=" * 100)
        print("PIIFilter – Guard comparison (ON vs OFF)")
        print("=" * 100)
        print("\nOriginal:")
        print(textwrap.indent(text.strip(), "  "))

        if not self.pf:
            print("\n⚠️ Guard comparison requires PIIFilter class.")
            return

        ents_on = self._pipeline_entities(text, guards_enabled=True)
        ents_off = self._pipeline_entities(
            text,
            guards_enabled=False,
            guard_natural_suffix_requires_number=False,
            guard_single_token_addresses=False,
            guard_address_vs_person_priority=False,
            guard_requires_context_without_number=False,
        )
        print("\nEntities (guards ON):")
        print(self._pretty_entities(text, ents_on))
        print("\nEntities (guards OFF):")
        print(self._pretty_entities(text, ents_off))

        anon_on = self.anonymize(text, guards_enabled=True)
        anon_off = self.anonymize(
            text,
            guards_enabled=False,
            guard_natural_suffix_requires_number=False,
            guard_single_token_addresses=False,
            guard_address_vs_person_priority=False,
            guard_requires_context_without_number=False,
        )
        print("\nAnonymized (guards ON):")
        print(textwrap.indent(anon_on, "  "))
        print("\nAnonymized (guards OFF):")
        print(textwrap.indent(anon_off, "  "))


# -------------------------------------------------------------
# CLI
# -------------------------------------------------------------
def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="PIIFilter – Full Sanity Runner")
    g = p.add_argument_group("Input")
    g.add_argument("--text", type=str, help="Analyze/anonymize a single text snippet.")
    g.add_argument("--file", type=str, help="Analyze/anonymize a file's entire contents.")
    g.add_argument("--json", action="store_true", help="Emit entities as JSON.")
    g = p.add_argument_group("Guards")
    g.add_argument("--guards-off", action="store_true", help="Disable all guard filters.")
    g.add_argument("--no-natural-suffix", action="store_true", help="Disable natural suffix requires number guard.")
    g.add_argument("--no-single-token", action="store_true", help="Disable single-token addresses guard.")
    g.add_argument("--no-addr-vs-person", action="store_true", help="Disable address vs person priority guard.")
    g.add_argument("--no-ctx", action="store_true", help="Disable context-required-without-number guard.")
    g.add_argument("--ctx-window", type=int, default=40, help="Context window size for context guard.")
    g = p.add_argument_group("Output")
    g.add_argument("--no-entities", action="store_true", help="Do not print entities.")
    g.add_argument("--no-anonymized", action="store_true", help="Do not print anonymized text.")
    g.add_argument("--compare-guards", action="store_true", help="Run ON vs OFF comparison (single text only).")
    return p


def _guard_config_from_args(args: argparse.Namespace) -> dict:
    if args.guards_off:
        return dict(
            guards_enabled=False,
            guard_natural_suffix_requires_number=False,
            guard_single_token_addresses=False,
            guard_address_vs_person_priority=False,
            guard_requires_context_without_number=False,
            guard_context_window=args.ctx_window,
        )
    return dict(
        guards_enabled=True,
        guard_natural_suffix_requires_number=(not args.no_natural_suffix),
        guard_single_token_addresses=(not args.no_single_token),
        guard_address_vs_person_priority=(not args.no_addr_vs_person),
        guard_requires_context_without_number=(not args.no_ctx),
        guard_context_window=args.ctx_window,
    )


def _generate_side_by_side_report(filter_instance, output_file="entity_demonstration_report.md"):
    """
    Generate a comprehensive side-by-side original vs anonymized text report
    for all entity types in all supported languages.
    """
    from datetime import datetime
    import re

    # We'll build examples for every entity by scanning the existing TEST_TEXTS
    # blocks. For each non-empty, non-comment line we run the filter and group
    # original/anonymized pairs by the anonymizer placeholders (e.g. <EMAIL>). 
    # This captures supported formats, edge cases and many false-positive
    # scenarios already present in TEST_TEXTS. We also append a raw dump of
    # the TEST_TEXTS blocks and their full anonymized output so you can see
    # the runner results inline.

    placeholder_to_entity = {
        'PERSON': 'PERSON', 'EMAIL': 'EMAIL_ADDRESS', 'PHONE': 'PHONE_NUMBER',
        'FAX': 'FAX_NUMBER', 'ADDRESS': 'ADDRESS', 'LOCATION': 'LOCATION',
        'DATE': 'DATE', 'PASSPORT': 'PASSPORT', 'ID_NUMBER': 'ID_NUMBER',
        'TAX_ID': 'TAX_ID', 'IP_ADDRESS': 'IP_ADDRESS', 'EORI': 'EORI',
        'CREDIT_CARD': 'CREDIT_CARD', 'BANK_ACCOUNT': 'BANK_ACCOUNT',
        'ROUTING_NUMBER': 'ROUTING_NUMBER', 'ACCOUNT_NUMBER': 'ACCOUNT_NUMBER',
        'PAYMENT_TOKEN': 'PAYMENT_TOKEN', 'CRYPTO_ADDRESS': 'CRYPTO_ADDRESS',
        'DRIVER_LICENSE': 'DRIVER_LICENSE', 'VOTER_ID': 'VOTER_ID',
        'RESIDENCE_PERMIT': 'RESIDENCE_PERMIT', 'BENEFIT_ID': 'BENEFIT_ID',
        'MILITARY_ID': 'MILITARY_ID', 'HEALTH_ID': 'HEALTH_ID', 'MRN': 'MRN',
        'INSURANCE_ID': 'INSURANCE_ID', 'HEALTH_INFO': 'HEALTH_INFO',
        'STUDENT_NUMBER': 'STUDENT_NUMBER', 'EMPLOYEE_ID': 'EMPLOYEE_ID',
        'PRO_LICENSE': 'PRO_LICENSE', 'SOCIAL_HANDLE': 'SOCIAL_HANDLE',
        'MESSAGING_ID': 'MESSAGING_ID', 'MEETING_ID': 'MEETING_ID',
        'MAC_ADDRESS': 'MAC_ADDRESS', 'IMEI': 'IMEI', 'ADVERTISING_ID': 'ADVERTISING_ID',
        'DEVICE_ID': 'DEVICE_ID', 'GEO_COORDINATES': 'GEO_COORDINATES',
        'PLUS_CODE': 'PLUS_CODE', 'W3W': 'W3W', 'LICENSE_PLATE': 'LICENSE_PLATE',
        'API_KEY': 'API_KEY', 'SESSION_ID': 'SESSION_ID', 'ACCESS_TOKEN': 'ACCESS_TOKEN',
        'REFRESH_TOKEN': 'REFRESH_TOKEN', 'ACCESS_CODE': 'ACCESS_CODE', 'OTP_CODE': 'OTP_CODE',
        'FILE_NUMBER': 'FILE_NUMBER', 'TRANSACTION_NUMBER': 'TRANSACTION_NUMBER',
        'CUSTOMER_NUMBER': 'CUSTOMER_NUMBER', 'TICKET_ID': 'TICKET_ID',
        'CASE_REFERENCE': 'CASE_REFERENCE', 'PASSWORD': 'PASSWORD', 'PIN': 'PIN',
        'TAN': 'TAN', 'PUK': 'PUK', 'RECOVERY_CODE': 'RECOVERY_CODE'
    }

    examples = {e: {} for e in getattr(filter_instance, 'ALLOWED_ENTITIES', [])}

    placeholder_rx = re.compile(r"<([A-Z0-9_]+)>")

    # Walk TEST_TEXTS blocks and collect per-line examples
    for block_label, block in TEST_TEXTS.items():
        for raw_line in str(block).splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue

            anonymized = filter_instance.anonymize_text(line)
            tags = placeholder_rx.findall(anonymized)
            # infer language using earlier detection helper if available
            try:
                lang = _detect_lang(line)
            except Exception:
                lang = 'en'

            if not tags:
                # keep a bucket for 'NO_ENTITY' examples (edge-cases / false negatives)
                ent = 'NO_ENTITY'
                examples.setdefault(ent, {})
                examples[ent].setdefault(lang, [])
                if len(examples[ent][lang]) < 50:
                    examples[ent][lang].append((line, anonymized, block_label))
                continue

            for t in tags:
                entity = placeholder_to_entity.get(t, t)
                if entity not in examples:
                    examples.setdefault(entity, {})
                examples[entity].setdefault(lang, [])
                if len(examples[entity][lang]) < 200:
                    examples[entity][lang].append((line, anonymized, block_label))

    # For any allowed entities with no examples, synthesize a small set
    for ent in getattr(filter_instance, 'ALLOWED_ENTITIES', []):
        if ent not in examples or not examples[ent]:
            examples.setdefault(ent, {})
            examples[ent].setdefault('en', [])
            synth = f"Example {ent} placeholder: <{ent}>"
            examples[ent]['en'].append((synth, filter_instance.anonymize_text(synth), 'synthesized'))

    # Build report
    lines = []
    lines.append("# Comprehensive Entity Type Demonstration\n\n")
    lines.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    lines.append("This document demonstrates all PII entity types found by the filter.\n")
    lines.append("**Note**: Each entry shows the original text and the anonymized result produced by `PIIFilter.anonymize_text()`.\n\n---\n\n")

    for entity_type in sorted(examples.keys()):
        lines.append(f"## {entity_type}\n\n")
        for lang in sorted(examples[entity_type].keys()):
            lines.append(f"### {lang}\n\n")
            for original, anonymized, source in examples[entity_type][lang]:
                lines.append(f"**Source:** {source}  \n")
                lines.append(f"**Original:** `{original}`  \n")
                lines.append(f"**Anonymized:** `{anonymized}`  \n\n")
            lines.append("---\n\n")

    lines.append("*End of Report*\n")

    output_path = Path(output_file)
    output_path.write_text("".join(lines), encoding="utf-8")
    print(f"\n✅ Report generated: {output_path.absolute()}")
    return output_path


def main():
    args = _build_arg_parser().parse_args()
    runner = PIIRunner()

    guard_kw = _guard_config_from_args(args)
    show_entities = not args.no_entities
    show_anonymized = not args.no_anonymized

    # Single text from CLI
    if args.text:
        if args.compare_guards:
            runner.compare_guards(args.text)
            return
        corpus = {"CLI Text": args.text}
        runner.run_on_texts(
            corpus,
            show_entities=show_entities,
            show_anonymized=show_anonymized,
            json_mode=args.json,
            **guard_kw
        )
        return

    # File input
    if args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"⚠️ File not found: {path}")
            sys.exit(1)
        text = path.read_text(encoding="utf-8", errors="ignore")
        label = f"File: {path.name}"
        if args.compare_guards:
            runner.compare_guards(text)
            return
        corpus = {label: text}
        runner.run_on_texts(
            corpus,
            show_entities=show_entities,
            show_anonymized=show_anonymized,
            json_mode=args.json,
            **guard_kw
        )
        return

    # Default: run built-in corpus + generate report
    runner.run_on_texts(
        TEST_TEXTS,
        show_entities=show_entities,
        show_anonymized=show_anonymized,
        json_mode=args.json,
        **guard_kw
    )
    
    # Generate comprehensive side-by-side report
    print("\n" + "="*80)
    print("📊 GENERATING COMPREHENSIVE ENTITY DEMONSTRATION REPORT...")
    print("="*80)
    if pf_class:
        filter_instance = pf_class()
        _generate_side_by_side_report(filter_instance)


if __name__ == "__main__":
    main()
