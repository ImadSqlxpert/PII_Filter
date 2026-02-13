# Comprehensive Entity Type Demonstration

**Generated**: 2026-02-13 19:32:41

This document demonstrates all PII entity types found by the filter.
**Note**: Each entry shows the original text and the anonymized result produced by `PIIFilter.anonymize_text()`.

---

## ACCESS_CODE

### de

**Source:** Comms/Devices/Geo  
**Original:** `Coords: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft; Kennzeichen: B-AB 1234`  
**Anonymized:** `Coords: <GEO_COORDINATES>; Plus Code: <ACCESS_CODE>+2V; w3w: ///index.home.raft; Kennzeichen: <LICENSE_PLATE>`  

---

### en

**Source:** German - Geo/Locations  
**Original:** `Koordinaten: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft`  
**Anonymized:** `Koordinaten: <GEO_COORDINATES>; Plus Code: <ACCESS_CODE>+2V; w3w: ///index.home.raft`  

**Source:** Authentication Secrets  
**Original:** `Code Authentification: 456789`  
**Anonymized:** `Code Authentification: <ACCESS_CODE>`  

**Source:** API & Authentication Tokens  
**Original:** `Authentication code: 765432`  
**Anonymized:** `Authentication code: <ACCESS_CODE>`  

---

### fr

**Source:** Location & Geographic Codes  
**Original:** `Plus Code: 9C3W9QCJ+2V`  
**Anonymized:** `Plus Code: <ACCESS_CODE>+2V`  

---

### nl

**Source:** Location & Geographic Codes  
**Original:** `Zip Code: 94105`  
**Anonymized:** `Zip Code: <ACCESS_CODE>`  

---

### pt

**Source:** Authentication Secrets  
**Original:** `PIN-Code: 8901`  
**Anonymized:** `<PIN>: <ACCESS_CODE>`  

**Source:** Location & Geographic Codes  
**Original:** `Code Postal: 75001`  
**Anonymized:** `Code <PERSON>: <ACCESS_CODE>`  

---

## ACCESS_TOKEN

### en

**Source:** synthesized  
**Original:** `Example ACCESS_TOKEN placeholder: <ACCESS_TOKEN>`  
**Anonymized:** `Example ACCESS_TOKEN placeholder: <ACCESS_TOKEN>`  

---

## ACCOUNT_NUMBER

### da

**Source:** German - Payments/Bank  
**Original:** `Kontonummer: 1234-567890-12`  
**Anonymized:** `<SERVICEKONTO>: <ACCOUNT_NUMBER>`  

---

### en

**Source:** Payments  
**Original:** `Routing (ABA): 021000021. Kontonummer: 1234-567890-12.`  
**Anonymized:** `Routing (ABA): <ROUTING_NUMBER>. <SERVICEKONTO>: <ACCOUNT_NUMBER>.`  

**Source:** German E-Government IDs  
**Original:** `Service Account: SK-2025-009876`  
**Anonymized:** `Service Account: <ACCOUNT_NUMBER>`  

---

## ADDRESS

### ar

**Source:** Arabic  
**Original:** `أعيش في شارع الملك فيصل 20، الرياض 12345.`  
**Anonymized:** `أعيش في <ADDRESS>، الرياض 12345.`  

---

### de

**Source:** German - Basics  
**Original:** `Ich wohne in der Musterstraße 5, 10115 Berlin (Mitte).`  
**Anonymized:** `Ich wohne <ADDRESS> (<LOCATION>).`  

**Source:** German - Basics  
**Original:** `ich bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `Ich Bin Anna Müller und ich wohne in der Blablastrasse 9, Berlin 10999. I will ein Gewerbe anmelden`  
**Anonymized:** `Ich Bin <PERSON> und ich wohne <ADDRESS> 10999. I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `ich Bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich Bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `ich bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `ich Bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich Bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `Gibt es Beratungszentern in Tempelhof-Shöneberg für Gründung von Unternehmen?`  
**Anonymized:** `<PERSON> <ADDRESS>?`  

**Source:** German - Street Variants  
**Original:** `Adresse: Am Waldrand 12, 50667 Köln.`  
**Anonymized:** `Adresse: <ADDRESS>.`  

**Source:** German - Street Variants  
**Original:** `Ich wohne Im Tal 7; An der See 3 (OH).`  
**Anonymized:** `Ich wohne <ADDRESS>; <ADDRESS> (OH).`  

**Source:** German - Street Variants  
**Original:** `Ich wohne Im Tal 7; An der See 3 (OH).`  
**Anonymized:** `Ich wohne <ADDRESS>; <ADDRESS> (OH).`  

**Source:** German - Street Variants  
**Original:** `Unter den Linden 77, 10117 Berlin.`  
**Anonymized:** `<ADDRESS>.`  

**Source:** German - Street Variants  
**Original:** `Karl-Marx-Allee 1, 10243 Berlin.`  
**Anonymized:** `<ADDRESS>.`  

**Source:** German - Street Variants  
**Original:** `Königsberger Feld 4, 69120 Heidelberg.`  
**Anonymized:** `<ADDRESS>, 69120 Heidelberg.`  

**Source:** German - Apartment/Unit Suffixes  
**Original:** `Musterstraße 10, Whg. 5, 2. Etage, 01067 Dresden.`  
**Anonymized:** `<ADDRESS>.`  

**Source:** German - Apartment/Unit Suffixes  
**Original:** `Hauptstraße 12, Stiege 2, Top 14, 2. OG, 1010 Wien.`  
**Anonymized:** `<ADDRESS>, Stiege 2, Top 14, 2. OG, 1010 Wien.`  

---

### en

**Source:** English  
**Original:** `I live at 221B Baker Street, London.`  
**Anonymized:** `I live at <ADDRESS>.`  

**Source:** US Tax & IDs  
**Original:** `Address: 742 Evergreen Terrace, 90210 Beverly Hills.`  
**Anonymized:** `Address: <ADDRESS>.`  

**Source:** Authentication Secrets  
**Original:** `PUK: 1111111`  
**Anonymized:** `<ADDRESS>111`  

---

### es

**Source:** Spanish  
**Original:** `Vivo en la Calle Mayor 10, 28013 Madrid.`  
**Anonymized:** `Vivo en la <ADDRESS>.`  

**Source:** Extended Government & Education IDs  
**Original:** `Immatriculación: STU-77888`  
**Anonymized:** `Immatriculación: <ADDRESS>`  

---

### fr

**Source:** French  
**Original:** `J'habite au 12 rue de Rivoli, 75001 Paris.`  
**Anonymized:** `J'habite <ADDRESS>.`  

---

### it

**Source:** Extended Government & Education IDs  
**Original:** `Numero di matricola: STU-99000`  
**Anonymized:** `Numero di <PASSPORT>: <ADDRESS>`  

---

### pt

**Source:** Location & Geographic Codes  
**Original:** `Postal: 28013`  
**Anonymized:** `<ADDRESS>3`  

---

### sv

**Source:** German - Street Variants  
**Original:** `Gänsemarkt 2, 20354 Hamburg.`  
**Anonymized:** `<ADDRESS>.`  

**Source:** Extended Government & Education IDs  
**Original:** `Matrikelnummer: STU-55666`  
**Anonymized:** `<PERSON>: <ADDRESS>`  

---

### tl

**Source:** Authentication Secrets  
**Original:** `PUK: 1010101`  
**Anonymized:** `<ADDRESS>101`  

---

### tr

**Source:** Turkish  
**Original:** `Adresim Atatürk Caddesi No:15, Ankara.`  
**Anonymized:** `<PERSON><ADDRESS>.`  

---

## ADVERTISING_ID

### pt

**Source:** German - Devices/Network  
**Original:** `IDFA: 123e4567-e89b-12d3-a456-426614174000, Gerät-ID: 123e4567-e89b-12d3-a456-426614174001`  
**Anonymized:** `IDFA: <ADVERTISING_ID>, Gerät-ID: 123e4567-e89b-12d3-a456-<MAC_ADDRESS>`  

**Source:** Comms/Devices/Geo  
**Original:** `MAC 00:1A:2B:3C:4D:5E, IMEI 490154203237518, IDFA: 123e4567-e89b-12d3-a456-426614174000.`  
**Anonymized:** `MAC 00:1A:2B:3C:4D:5E, IMEI <IMEI>, IDFA: <ADVERTISING_ID>.`  

**Source:** API & Authentication Tokens  
**Original:** `IDFA: 550e8400-e29b-41d4-a716-446655440000`  
**Anonymized:** `IDFA: <ADVERTISING_ID>`  

---

## API_KEY

### da

**Source:** Payments  
**Original:** `API key: sk_live_abcDEF1234567890; Stripe pub: pk_test_1xYzABC1234567890`  
**Anonymized:** `API key: <API_KEY>; Stripe pub: <API_KEY>`  

**Source:** Payments  
**Original:** `API key: sk_live_abcDEF1234567890; Stripe pub: pk_test_1xYzABC1234567890`  
**Anonymized:** `API key: <API_KEY>; Stripe pub: <API_KEY>`  

**Source:** API & Authentication Tokens  
**Original:** `API Key: sk_live_abcDEF1234567890ghijkl`  
**Anonymized:** `API Key: <API_KEY>`  

**Source:** API & Authentication Tokens  
**Original:** `Stripe API: rk_live_abcd1234efgh5678ijkl9012mnop3456`  
**Anonymized:** `Stripe API: <API_KEY>`  

---

### en

**Source:** API & Authentication Tokens  
**Original:** `Google API Key: AIzaSyDxKmE5R4L9JqR7vJlR3V9p8q9r0s1t2u3v`  
**Anonymized:** `Google API Key: <API_KEY>`  

**Source:** API & Authentication Tokens  
**Original:** `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U`  
**Anonymized:** `Authorization: Bearer <API_KEY>`  

**Source:** API & Authentication Tokens  
**Original:** `access_token: ya29.a0AfH6SMBx1234567890abcdefghijklmnopqrstuvwxyz`  
**Anonymized:** `access_token: <API_KEY>`  

---

### et

**Source:** API & Authentication Tokens  
**Original:** `session_id: sess_1234567890abcdefghijklmnop`  
**Anonymized:** `session_id: <API_KEY>`  

---

### nl

**Source:** API & Authentication Tokens  
**Original:** `GitHub Token: ghp_1234567890abcdefghijklmnopqrstuvwxyz`  
**Anonymized:** `GitHub <PERSON>: <API_KEY>`  

**Source:** API & Authentication Tokens  
**Original:** `rt_live_abcdef1234567890ghijklmnop9876543210`  
**Anonymized:** `<API_KEY>`  

**Source:** API & Authentication Tokens  
**Original:** `Device ID: 12345a6b-78cd-90ef-ghij-klmnopqrst12`  
**Anonymized:** `Device ID: <API_KEY>`  

---

### no

**Source:** API & Authentication Tokens  
**Original:** `api_key: sk_test_9876543210fedcbaZYXW`  
**Anonymized:** `api_key: <API_KEY>`  

---

### tl

**Source:** API & Authentication Tokens  
**Original:** `AWS_ACCESS_KEY_ID: AKIAIOSFODNN7EXAMPLE`  
**Anonymized:** `AWS_ACCESS_KEY_ID: <API_KEY>`  

---

## BANK_ACCOUNT

### so

**Source:** German - Payments/Bank  
**Original:** `IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX`  
**Anonymized:** `IBAN: <BANK_ACCOUNT>, BIC: <BANK_ACCOUNT>`  

**Source:** German - Payments/Bank  
**Original:** `IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX`  
**Anonymized:** `IBAN: <BANK_ACCOUNT>, BIC: <BANK_ACCOUNT>`  

**Source:** Payments  
**Original:** `IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX.`  
**Anonymized:** `IBAN: <BANK_ACCOUNT>, BIC: <BANK_ACCOUNT>.`  

**Source:** Payments  
**Original:** `IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX.`  
**Anonymized:** `IBAN: <BANK_ACCOUNT>, BIC: <BANK_ACCOUNT>.`  

---

## BENEFIT_ID

### de

**Source:** Extended Government & Education IDs  
**Original:** `My benefit ID is B12345678`  
**Anonymized:** `My benefit ID is <BENEFIT_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Sozialhilfe: B65432100`  
**Anonymized:** `Sozialhilfe: <BENEFIT_ID>`  

**Source:** Failed  
**Original:** `Meine Sozialhilfekarte ist B11223344`  
**Anonymized:** `Meine Sozialhilfekarte ist <BENEFIT_ID>`  

---

## BUND_ID

### de

**Source:** German E-Government IDs  
**Original:** `BundID: BUND-12345678-ABCD`  
**Anonymized:** `<BUND_ID>`  

**Source:** German E-Government IDs  
**Original:** `Bundidentität BUND-87654321-WXYZ`  
**Anonymized:** `<BUND_ID>`  

**Source:** German E-Government IDs  
**Original:** `Bundesausweis-ID: BUND-11111111-1111`  
**Anonymized:** `Bundesausweis-ID: <BUND_ID>`  

---

### en

**Source:** German E-Government IDs  
**Original:** `Digital Identity: BUND-99999999-ZYXW`  
**Anonymized:** `Digital Identity: <BUND_ID>`  

---

## CASE_REFERENCE

### ar

**Source:** Case Reference (Multilingual)  
**Original:** `رقم القضية: RQ-2024-333`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Case Reference (Multilingual)  
**Original:** `رقم القضية #RQ-2023-444`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### da

**Source:** Case Reference (Multilingual)  
**Original:** `Vorgangsnummer: VN-2024-789012`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### de

**Source:** Case Reference (Multilingual)  
**Original:** `Aktenzeichen: AZ-2023-123456`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Case Reference (Multilingual)  
**Original:** `Dossier #DOSS-2023-999`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Government & Official IDs  
**Original:** `Voter Number: VN-2024-554433`  
**Anonymized:** `Voter Number: <CASE_REFERENCE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Dossier: DOSS2024999888`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Aktenzeichen: AZ2024333222`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### en

**Source:** Case Reference (Multilingual)  
**Original:** `Case ID: CASE-2023-001234`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Case Reference (Multilingual)  
**Original:** `Reference Number: REF-2024-567890`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Financial & Routing  
**Original:** `Case Number: CASE-2024-987654`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Financial & Routing  
**Original:** `Reference Number: REF-2024-555666`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Immatriculation: AZ-123-AB`  
**Anonymized:** `Immatriculation: <CASE_REFERENCE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Case Number: CASE2024777666`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### es

**Source:** Case Reference (Multilingual)  
**Original:** `Número de expediente: EXP-2023-999`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Case Reference (Multilingual)  
**Original:** `Expediente #EXP-2024-111`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### it

**Source:** Case Reference (Multilingual)  
**Original:** `Numero pratica: PR-2024-555`  
**Anonymized:** `<CASE_REFERENCE>`  

**Source:** Case Reference (Multilingual)  
**Original:** `Pratica #PRT-2023-222`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### pt

**Source:** Case Reference (Multilingual)  
**Original:** `Numéro de dossier: ND-2024-001`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### sv

**Source:** Financial & Routing  
**Original:** `Ticket Number: TKT-2024-111222`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### tl

**Source:** Case Reference (Multilingual)  
**Original:** `Dosya #DOS-2024-333`  
**Anonymized:** `<CASE_REFERENCE>`  

---

### tr

**Source:** Case Reference (Multilingual)  
**Original:** `Dosya numarası: DN-2023-777`  
**Anonymized:** `<CASE_REFERENCE>`  

---

## COMMERCIAL_REGISTER

### ca

**Source:** Commercial Register (European)  
**Original:** `Tribunal de Commerce Paris, Registre B 567890`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

**Source:** Commercial Register (European)  
**Original:** `Reg. Merc. Barcelona, Secc. A 901234`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

---

### da

**Source:** Commercial Register (European)  
**Original:** `Handelsregister Amsterdam, Afdeling B 456789`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

---

### de

**Source:** Commercial Register (European)  
**Original:** `Amtsgericht München, Handelsregister B 123456`  
**Anonymized:** `<COMMERCIAL_REGISTER>123456`  

**Source:** Commercial Register (European)  
**Original:** `Registergericht Dresden, Abteilung B, HRB 234567`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

**Source:** Commercial Register (European)  
**Original:** `Das Unternehmen ist eingetragen im Handelsregister beim Amtsgericht München, Abteilung B, HRA 345678.`  
**Anonymized:** `Das Unternehmen ist eingetragen im Handelsregister beim <COMMERCIAL_REGISTER>.`  

---

### en

**Source:** Commercial Register (European)  
**Original:** `RCS Paris B 678901`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

---

### es

**Source:** Commercial Register (European)  
**Original:** `Registro Mercantil Madrid, Sección B 890123`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

**Source:** Commercial Register (European)  
**Original:** `La sociedad está inscrita en el Registro Mercantil de Madrid, sección B, número 012345.`  
**Anonymized:** `La sociedad está inscrita en el <COMMERCIAL_REGISTER>, número 012345.`  

---

### it

**Source:** Commercial Register (European)  
**Original:** `Registro delle Imprese Roma, Sezione B 123456`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

**Source:** Commercial Register (European)  
**Original:** `L'impresa è iscritta nel Registro delle Imprese di Roma, sezione B, numero 345678.`  
**Anonymized:** `L'impresa è iscritta nel <COMMERCIAL_REGISTER>, numero 345678.`  

---

### nl

**Source:** Commercial Register (European)  
**Original:** `KVK Amsterdam 567890`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

**Source:** Commercial Register (European)  
**Original:** `Het bedrijf staat ingeschreven in het Handelsregister van Amsterdam, afdeling B, nummer 678901.`  
**Anonymized:** `Het bedrijf staat ingeschreven in het <COMMERCIAL_REGISTER>, nummer 678901.`  

---

### ro

**Source:** Commercial Register (European)  
**Original:** `REA Roma 234567`  
**Anonymized:** `<COMMERCIAL_REGISTER>`  

---

## CREDIT_CARD

### tl

**Source:** German - Payments/Bank  
**Original:** `Visa 4111 1111 1111 1111`  
**Anonymized:** `Visa <CREDIT_CARD>`  

**Source:** Payments  
**Original:** `Visa 4111 1111 1111 1111, Amex 3782 822463 10005.`  
**Anonymized:** `Visa <CREDIT_CARD>, Amex <CREDIT_CARD>.`  

**Source:** Payments  
**Original:** `Visa 4111 1111 1111 1111, Amex 3782 822463 10005.`  
**Anonymized:** `Visa <CREDIT_CARD>, Amex <CREDIT_CARD>.`  

---

## CRYPTO_ADDRESS

### en

**Source:** Crypto  
**Original:** `bech32: bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kygt080,`  
**Anonymized:** `bech32: <CRYPTO_ADDRESS>,`  

---

### id

**Source:** Crypto  
**Original:** `BTC: 1BoatSLRHtKNngkdXEeobR76b53LETtpyT,`  
**Anonymized:** `BTC: <CRYPTO_ADDRESS>,`  

---

### nl

**Source:** Crypto  
**Original:** `ETH: 0x52908400098527886e0f7030069857d2e4169ee7`  
**Anonymized:** `ETH: <CRYPTO_ADDRESS>`  

---

## CUSTOMER_NUMBER

### de

**Source:** Case Reference (Multilingual)  
**Original:** `Kundennummer: KN-2023-456789`  
**Anonymized:** `<CUSTOMER_NUMBER>-456789`  

---

### en

**Source:** Case Reference (Multilingual)  
**Original:** `Customer Number: CUST-2023-55555`  
**Anonymized:** `<CUSTOMER_NUMBER>-55555`  

---

## DATE

### ar

**Source:** Arabic  
**Original:** `اسمي أحمد محمد. ولدت في 31/12/1990.`  
**Anonymized:** `اسمي <PERSON>. ولدت في <DATE>.`  

---

### de

**Source:** German - Basics  
**Original:** `Mein Name ist Max Mustermann, geboren am 31.12.1990.`  
**Anonymized:** `Mein Name ist <PERSON>, geboren am <DATE>.`  

**Source:** German - Basics  
**Original:** `ich Heisse Max Mustermann und ich bin am 31.12.1990 geboren.`  
**Anonymized:** `ich Heisse <PERSON> und ich bin am <DATE> geboren.`  

**Source:** German - Basics  
**Original:** `ich heisse Max Mustermann und ich bin am 31.12.1990 geboren.`  
**Anonymized:** `ich heisse <PERSON> und ich bin am <DATE> geboren.`  

**Source:** German - Basics  
**Original:** `ich heisse max mustermann und ich bin am 31.12.1990 geboren.`  
**Anonymized:** `ich heisse <PERSON> und ich bin am <DATE> geboren.`  

**Source:** German - Edge Cases  
**Original:** `Ruf mich unter 12-03-2023 an.`  
**Anonymized:** `Ruf mich unter <DATE> an.`  

---

### en

**Source:** English  
**Original:** `My name is John Smith. I was born on 12/31/1990.`  
**Anonymized:** `My name is <PERSON>. I was born on <DATE>.`  

**Source:** US Tax & IDs  
**Original:** `Name: Jane Miller. I was born on 31 December 1988.`  
**Anonymized:** `Name: <PERSON>. I was born on <DATE>.`  

---

### es

**Source:** Spanish  
**Original:** `Me llamo Carlos García. Nací el 31/12/1990.`  
**Anonymized:** `Me llamo <PERSON>. Nací el <DATE>.`  

---

### fr

**Source:** French  
**Original:** `Je m'appelle Marie Dupont, née le 31-05-1995.`  
**Anonymized:** `Je m'appelle <PERSON>, née le <DATE>.`  

---

### tr

**Source:** Turkish  
**Original:** `Benim adım Ahmet Yılmaz. Doğum tarihim 01-01-1992.`  
**Anonymized:** `Benim adım <PERSON>. Doğum tarihim <DATE>.`  

---

## DEVICE_ID

### de

**Source:** Failed  
**Original:** `Meine Geräte-ID ist DEV-999888777`  
**Anonymized:** `Meine Geräte-ID ist <DEVICE_ID>`  

---

### en

**Source:** Extended Government & Education IDs  
**Original:** `Device ID: DEV-123456789`  
**Anonymized:** `Device ID: <DEVICE_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `My device ID is DEV-987654321`  
**Anonymized:** `My device ID is <DEVICE_ID>`  

---

## DRIVER_LICENSE

### nl

**Source:** Government & Official IDs  
**Original:** `Driver License: D12345678`  
**Anonymized:** `Driver <PRO_LICENSE>: <DRIVER_LICENSE>`  

---

## ELSTER_ID

### de

**Source:** German E-Government IDs  
**Original:** `ELSTER-Benutzername: user.name@example`  
**Anonymized:** `<ELSTER_ID>@example`  

---

### en

**Source:** German E-Government IDs  
**Original:** `ELSTER-ID: ELST-12345`  
**Anonymized:** `<ELSTER_ID>`  

---

### no

**Source:** German E-Government IDs  
**Original:** `ELSTER Login: elster_user_12345`  
**Anonymized:** `<ELSTER_ID>`  

**Source:** German E-Government IDs  
**Original:** `elster_konto_abcd1234`  
**Anonymized:** `<ELSTER_ID>`  

---

## EMAIL_ADDRESS

### ar

**Source:** Arabic  
**Original:** `بريدي الإلكتروني ahmed.mohamed@example.com ورقم هاتفي +966 50 123 4567.`  
**Anonymized:** `بريدي الإلكتروني <EMAIL> ورقم هاتفي <PHONE>.`  

---

### de

**Source:** German - Basics  
**Original:** `Meine E-Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.`  
**Anonymized:** `Meine E-Mail ist <EMAIL> und meine Nummer ist 0176 12345678.`  

---

### en

**Source:** English  
**Original:** `You can reach me at john.smith@example.com or call +44 7700 900123.`  
**Anonymized:** `You can reach me at <EMAIL> or call <PHONE>.`  

**Source:** US Tax & IDs  
**Original:** `Email: jane.miller@example.org, Phone: +1 (213) 555-0182`  
**Anonymized:** `Email: <EMAIL>, Phone: <PHONE>`  

**Source:** Comms/Devices/Geo  
**Original:** `Twitter @john_doe123, email john.doe@acme.io, Discord user#1234,`  
**Anonymized:** `Twitter <SOCIAL_HANDLE>, email <EMAIL>, Discord <MESSAGING_ID>,`  

---

### es

**Source:** Spanish  
**Original:** `Mi correo es carlos.garcia@email.com y mi teléfono es +34 612 345 678.`  
**Anonymized:** `Mi correo es <EMAIL> y mi teléfono es <PHONE>.`  

---

### fr

**Source:** French  
**Original:** `Mon email est marie.dupont@gmail.com et mon numéro est 06 12 34 56 78.`  
**Anonymized:** `Mon email est <EMAIL> et mon numéro est <PHONE>.`  

---

### pt

**Source:** Turkish  
**Original:** `E‑posta adresim ahmet.yilmaz@example.com ve telefon numaram 0555 123 45 67.`  
**Anonymized:** `E‑posta adresim <EMAIL> ve telefon numaram <PHONE>.`  

---

## EMPLOYEE_ID

### de

**Source:** Government & Official IDs  
**Original:** `Mitarbeiternummer: MIT-2024-778899`  
**Anonymized:** `<PERSON>: <EMPLOYEE_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Staff ID: EMP-45678`  
**Anonymized:** `Staff ID: <EMPLOYEE_ID>`  

---

### en

**Source:** Government & Official IDs  
**Original:** `Employee ID: EMP-2024-123456`  
**Anonymized:** `Employee ID: <EMPLOYEE_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Employee ID: EMP-78901`  
**Anonymized:** `Employee ID: <EMPLOYEE_ID>`  

---

### fr

**Source:** Extended Government & Education IDs  
**Original:** `Numéro d'employé: EMP-33444`  
**Anonymized:** `Numéro d'employé: <EMPLOYEE_ID>`  

---

### pt

**Source:** Extended Government & Education IDs  
**Original:** `Número de empleado: EMP-66677`  
**Anonymized:** `Número de <EMPLOYEE_ID>: <EMPLOYEE_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Número de empleado: EMP-66677`  
**Anonymized:** `Número de <EMPLOYEE_ID>: <EMPLOYEE_ID>`  

---

### sv

**Source:** Extended Government & Education IDs  
**Original:** `Personalnummer: EMP-12345`  
**Anonymized:** `<PERSON>: <EMPLOYEE_ID>`  

---

## EORI

### de

**Source:** Extended Government & Education IDs  
**Original:** `EORI: DE123456789`  
**Anonymized:** `EORI: <EORI>`  

**Source:** Extended Government & Education IDs  
**Original:** `EORI DE 123456789`  
**Anonymized:** `EORI <EORI>`  

**Source:** Extended Government & Education IDs  
**Original:** `EORI: FR123456789`  
**Anonymized:** `EORI: <EORI>`  

**Source:** Extended Government & Education IDs  
**Original:** `EORI ES 111222333`  
**Anonymized:** `EORI <EORI>`  

---

### en

**Source:** Extended Government & Education IDs  
**Original:** `My EORI is DE123456789000`  
**Anonymized:** `My EORI <EORI>`  

**Source:** Extended Government & Education IDs  
**Original:** `EORI: IT987654321`  
**Anonymized:** `EORI: <EORI>`  

---

## FAX_NUMBER

### so

**Source:** German - Communications  
**Original:** `Fax: +49 30 1234567`  
**Anonymized:** `Fax: <FAX>`  

---

## FILE_NUMBER

### de

**Source:** Financial & Routing  
**Original:** `File Number: FILE-2024-123456`  
**Anonymized:** `<FILE_NUMBER>`  

**Source:** Financial & Routing  
**Original:** `Dossier Number: DOSS-2024-333444`  
**Anonymized:** `<FILE_NUMBER>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `File Number: FILE2024001234`  
**Anonymized:** `<FILE_NUMBER>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Dossier Number: DOSS2024111000`  
**Anonymized:** `<FILE_NUMBER>`  

---

## GEO_COORDINATES

### de

**Source:** Comms/Devices/Geo  
**Original:** `Coords: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft; Kennzeichen: B-AB 1234`  
**Anonymized:** `Coords: <GEO_COORDINATES>; Plus Code: <ACCESS_CODE>+2V; w3w: ///index.home.raft; Kennzeichen: <LICENSE_PLATE>`  

**Source:** Location & Geographic Codes  
**Original:** `GPS: 35.6892, 139.6917`  
**Anonymized:** `GPS: <GEO_COORDINATES>`  

---

### en

**Source:** German - Geo/Locations  
**Original:** `Koordinaten: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft`  
**Anonymized:** `Koordinaten: <GEO_COORDINATES>; Plus Code: <ACCESS_CODE>+2V; w3w: ///index.home.raft`  

**Source:** Location & Geographic Codes  
**Original:** `Coordinates: 40.7128, -74.0060`  
**Anonymized:** `Coordinates: <GEO_COORDINATES>`  

**Source:** Location & Geographic Codes  
**Original:** `Location: 48.8566, 2.3522`  
**Anonymized:** `Location: <GEO_COORDINATES>`  

---

### tl

**Source:** Location & Geographic Codes  
**Original:** `Lat/Long: 51.5074, -0.1278`  
**Anonymized:** `Lat/Long: <GEO_COORDINATES>`  

---

## HEALTH_ID

### de

**Source:** Healthcare & Administrative IDs  
**Original:** `NHS Number: 456 789 1234`  
**Anonymized:** `NHS Number: <HEALTH_ID>`  

---

### en

**Source:** Health  
**Original:** `NHS number 943 476 5919, MRN: ABC-123456, Insurance policy: POL-987654321.`  
**Anonymized:** `NHS number <HEALTH_ID>, MRN: <MRN>, <PASSPORT> policy: <INSURANCE_ID>.`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Health ID: 943 476 5919`  
**Anonymized:** `Health ID: <HEALTH_ID>`  

---

### fr

**Source:** Healthcare & Administrative IDs  
**Original:** `Patient ID: 123 456 7890`  
**Anonymized:** `Patient ID: <HEALTH_ID>`  

---

## HEALTH_INFO

### af

**Source:** Healthcare & Administrative IDs  
**Original:** `Diagnosed: Diabetes Type 2`  
**Anonymized:** `<HEALTH_INFO>: <HEALTH_INFO> Type 2`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Diagnosed: Diabetes Type 2`  
**Anonymized:** `<HEALTH_INFO>: <HEALTH_INFO> Type 2`  

---

### en

**Source:** Health  
**Original:** `Diagnosed with diabetes. Blood type: O+.`  
**Anonymized:** `<HEALTH_INFO> with <HEALTH_INFO>. <HEALTH_INFO>: O+.`  

**Source:** Health  
**Original:** `Diagnosed with diabetes. Blood type: O+.`  
**Anonymized:** `<HEALTH_INFO> with <HEALTH_INFO>. <HEALTH_INFO>: O+.`  

**Source:** Health  
**Original:** `Diagnosed with diabetes. Blood type: O+.`  
**Anonymized:** `<HEALTH_INFO> with <HEALTH_INFO>. <HEALTH_INFO>: O+.`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Patient has allergies: Penicillin and Latex`  
**Anonymized:** `Patient has <HEALTH_INFO>: Penicillin and Latex`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Blood type: O positive`  
**Anonymized:** `<HEALTH_INFO>: O positive`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Prescription: Hypertension treatment`  
**Anonymized:** `<HEALTH_INFO>: Hypertension <PASSPORT>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Condition: Diagnosed with cancer`  
**Anonymized:** `<PASSPORT>: <HEALTH_INFO> with <HEALTH_INFO>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Condition: Diagnosed with cancer`  
**Anonymized:** `<PASSPORT>: <HEALTH_INFO> with <HEALTH_INFO>`  

---

## ID_NUMBER

### ca

**Source:** US Tax & IDs  
**Original:** `EIN: 51-2144346`  
**Anonymized:** `EIN: <ID_NUMBER>`  

---

### de

**Source:** German - Basics  
**Original:** `USt-IdNr.: DE 123456789`  
**Anonymized:** `USt-IdNr.: DE <ID_NUMBER>`  

**Source:** Government & Official IDs  
**Original:** `Student ID: 20240987654`  
**Anonymized:** `Student ID: <ID_NUMBER>`  

**Source:** Extended Government & Education IDs  
**Original:** `UDID: DEV-555666777`  
**Anonymized:** `UDID: DEV-<ID_NUMBER>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Steuer-ID: DE 123456789`  
**Anonymized:** `Steuer-ID: DE <ID_NUMBER>`  

---

### fr

**Source:** Extended Government & Education IDs  
**Original:** `Numéro d'établissement: NE ES 444555666`  
**Anonymized:** `Numéro d'établissement: NE ES <ID_NUMBER>`  

---

### hu

**Source:** Financial & Routing  
**Original:** `ABA: 123456789`  
**Anonymized:** `ABA: <ID_NUMBER>`  

---

### id

**Source:** Financial & Routing  
**Original:** `Transit Number: 001005124`  
**Anonymized:** `Transit Number: <ID_NUMBER>`  

---

### it

**Source:** Healthcare & Administrative IDs  
**Original:** `Partita IVA: IT 12345678901`  
**Anonymized:** `Partita IVA: IT <ID_NUMBER>`  

---

### nl

**Source:** Extended Government & Education IDs  
**Original:** `Device identifier: DEV-444555666`  
**Anonymized:** `Device identifier: DEV-<ID_NUMBER>`  

---

### pt

**Source:** Spanish  
**Original:** `ID No.: X1234567`  
**Anonymized:** `ID No.: <ID_NUMBER>`  

---

### so

**Source:** US Tax & IDs  
**Original:** `SSN: 536-80-4398`  
**Anonymized:** `SSN: <ID_NUMBER>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Tax ID: CH CHE 123456789 TVA`  
**Anonymized:** `Tax ID: CH CHE <ID_NUMBER> TVA`  

---

### tl

**Source:** US Tax & IDs  
**Original:** `ITIN: 912-91-3457`  
**Anonymized:** `ITIN: <ID_NUMBER>`  

---

## IMEI

### en

**Source:** German - Devices/Network  
**Original:** `MAC 00:1A:2B:3C:4D:5E; IMEI 490154203237518`  
**Anonymized:** `MAC 00:1A:2B:3C:4D:5E; IMEI <IMEI>`  

---

### pt

**Source:** Comms/Devices/Geo  
**Original:** `MAC 00:1A:2B:3C:4D:5E, IMEI 490154203237518, IDFA: 123e4567-e89b-12d3-a456-426614174000.`  
**Anonymized:** `MAC 00:1A:2B:3C:4D:5E, IMEI <IMEI>, IDFA: <ADVERTISING_ID>.`  

---

## INSURANCE_ID

### en

**Source:** Health  
**Original:** `NHS number 943 476 5919, MRN: ABC-123456, Insurance policy: POL-987654321.`  
**Anonymized:** `NHS number <HEALTH_ID>, MRN: <MRN>, <PASSPORT> policy: <INSURANCE_ID>.`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Insurance ID Policy123456`  
**Anonymized:** `<PASSPORT> ID <INSURANCE_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Insurance member: MYINSUR1234567`  
**Anonymized:** `<PASSPORT> member: <INSURANCE_ID>`  

---

## IP_ADDRESS

### ar

**Source:** Arabic  
**Original:** `عنوان IP الخاص بي: 192.168.1.10`  
**Anonymized:** `عنوان IP الخاص بي: <IP_ADDRESS>`  

---

### de

**Source:** German - Devices/Network  
**Original:** `IP: 192.168.1.10 und IPv6: 2001:db8::1`  
**Anonymized:** `IP: <IP_ADDRESS> und IPv6: <IP_ADDRESS>`  

**Source:** German - Devices/Network  
**Original:** `IP: 192.168.1.10 und IPv6: 2001:db8::1`  
**Anonymized:** `IP: <IP_ADDRESS> und IPv6: <IP_ADDRESS>`  

---

### en

**Source:** English  
**Original:** `My office IPs are 192.168.1.10 and 2001:0db8:85a3::8a2e:0370:7334.`  
**Anonymized:** `My office IPs are <IP_ADDRESS> and <IP_ADDRESS>.`  

**Source:** English  
**Original:** `My office IPs are 192.168.1.10 and 2001:0db8:85a3::8a2e:0370:7334.`  
**Anonymized:** `My office IPs are <IP_ADDRESS> and <IP_ADDRESS>.`  

**Source:** US Tax & IDs  
**Original:** `My server IP is 10.0.0.12 and IPv6 is 2a02:26f0:fe::5.`  
**Anonymized:** `My server IP is <IP_ADDRESS> and IPv6 is <IP_ADDRESS>.`  

**Source:** US Tax & IDs  
**Original:** `My server IP is 10.0.0.12 and IPv6 is 2a02:26f0:fe::5.`  
**Anonymized:** `My server IP is <IP_ADDRESS> and IPv6 is <IP_ADDRESS>.`  

---

### fr

**Source:** French  
**Original:** `Mon IPv6 à domicile: 2001:db8::1`  
**Anonymized:** `Mon IPv6 à domicile: <IP_ADDRESS>`  

---

## LICENSE_PLATE

### de

**Source:** German - Geo/Locations  
**Original:** `Kennzeichen: B-AB 1234`  
**Anonymized:** `Kennzeichen: <LICENSE_PLATE>`  

**Source:** Comms/Devices/Geo  
**Original:** `Coords: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft; Kennzeichen: B-AB 1234`  
**Anonymized:** `Coords: <GEO_COORDINATES>; Plus Code: <ACCESS_CODE>+2V; w3w: ///index.home.raft; Kennzeichen: <LICENSE_PLATE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Kennzeichen: B-AB 1234`  
**Anonymized:** `Kennzeichen: <LICENSE_PLATE>`  

---

### en

**Source:** Healthcare & Administrative IDs  
**Original:** `License Plate: AB 12 CDE`  
**Anonymized:** `<PRO_LICENSE> Plate: <LICENSE_PLATE>`  

---

## LOCATION

### ca

**Source:** Healthcare & Administrative IDs  
**Original:** `Plaque: YZ 234 XY`  
**Anonymized:** `Plaque: YZ<LOCATION>`  

---

### de

**Source:** German - Basics  
**Original:** `Ich wohne in der Musterstraße 5, 10115 Berlin (Mitte).`  
**Anonymized:** `Ich wohne <ADDRESS> (<LOCATION>).`  

**Source:** German - Street Variants  
**Original:** `Lange Reihe 15, 20099 Hamburg.`  
**Anonymized:** `Lange Reihe 15, <LOCATION>.`  

**Source:** German - Postal & Location  
**Original:** `DE-10115 Berlin (Mitte)`  
**Anonymized:** `<LOCATION> (Mitte)`  

**Source:** German - Postal & Location  
**Original:** `20095 Hamburg (Altstadt)`  
**Anonymized:** `<LOCATION> (Altstadt)`  

---

### en

**Source:** Healthcare & Administrative IDs  
**Original:** `Registration: BA 1234 CD`  
**Anonymized:** `Registration: BA<LOCATION>`  

---

### fr

**Source:** Commercial Register (European)  
**Original:** `L'entreprise est immatriculée au RCS Paris, section B sous le numéro 789012.`  
**Anonymized:** `L'entreprise est immatriculée au RCS <LOCATION>, section B sous le numéro 789012.`  

---

### hu

**Source:** German - Postal & Location  
**Original:** `50667 Köln`  
**Anonymized:** `<LOCATION>`  

---

### id

**Source:** Healthcare & Administrative IDs  
**Original:** `Targa: CA 123 AB`  
**Anonymized:** `Targa: CA<LOCATION>`  

---

## MAC_ADDRESS

### pt

**Source:** German - Devices/Network  
**Original:** `IDFA: 123e4567-e89b-12d3-a456-426614174000, Gerät-ID: 123e4567-e89b-12d3-a456-426614174001`  
**Anonymized:** `IDFA: <ADVERTISING_ID>, Gerät-ID: 123e4567-e89b-12d3-a456-<MAC_ADDRESS>`  

---

## MEETING_ID

### en

**Source:** German - Communications  
**Original:** `Meeting ID: 987 654 321`  
**Anonymized:** `Meeting ID: <MEETING_ID>`  

---

### nl

**Source:** German - Communications  
**Original:** `Google Meet: abc-defg-hij`  
**Anonymized:** `Google Meet: <MEETING_ID>`  

**Source:** Comms/Devices/Geo  
**Original:** `Meeting ID: 987 654 321, Meet code: abc-defg-hij.`  
**Anonymized:** `Meeting ID: <MEETING_ID>, Meet code: <MEETING_ID>.`  

**Source:** Comms/Devices/Geo  
**Original:** `Meeting ID: 987 654 321, Meet code: abc-defg-hij.`  
**Anonymized:** `Meeting ID: <MEETING_ID>, Meet code: <MEETING_ID>.`  

---

## MESSAGING_ID

### da

**Source:** Healthcare & Administrative IDs  
**Original:** `Telegram ID: telegram_dev_2024`  
**Anonymized:** `Telegram <MESSAGING_ID>: telegram_dev_2024`  

---

### de

**Source:** Healthcare & Administrative IDs  
**Original:** `Line: line_user_9999`  
**Anonymized:** `Line: <MESSAGING_ID>`  

---

### en

**Source:** Comms/Devices/Geo  
**Original:** `Twitter @john_doe123, email john.doe@acme.io, Discord user#1234,`  
**Anonymized:** `Twitter <SOCIAL_HANDLE>, email <EMAIL>, Discord <MESSAGING_ID>,`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Signal contact: wave_user_789`  
**Anonymized:** `Signal <MESSAGING_ID>: wave_user_789`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Skype: alice.work.domain`  
**Anonymized:** `Skype: <MESSAGING_ID>`  

---

### nl

**Source:** German - Communications  
**Original:** `Discord hans#1234`  
**Anonymized:** `Discord <MESSAGING_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Discord: john_doe#1234`  
**Anonymized:** `Discord: <MESSAGING_ID>`  

---

### no

**Source:** Healthcare & Administrative IDs  
**Original:** `My Skype: user_123_skype`  
**Anonymized:** `My Skype: <MESSAGING_ID>`  

---

## MILITARY_ID

### de

**Source:** Extended Government & Education IDs  
**Original:** `Militärausweis: M33344455`  
**Anonymized:** `<PERSON>: <MILITARY_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Meine Militärnummer: M66677788`  
**Anonymized:** `Meine Militärnummer: <MILITARY_ID>`  

**Source:** Failed  
**Original:** `Meine Militärausweis ist M55667788`  
**Anonymized:** `Meine Militärausweis ist <MILITARY_ID>`  

---

### en

**Source:** Extended Government & Education IDs  
**Original:** `Military ID: M45678901`  
**Anonymized:** `Military ID: <MILITARY_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Service number: M99900011`  
**Anonymized:** `Service number: <MILITARY_ID>`  

---

### fr

**Source:** Extended Government & Education IDs  
**Original:** `Carte militaire: M88899900`  
**Anonymized:** `Carte <PASSPORT>: <MILITARY_ID>`  

---

## MRN

### de

**Source:** Healthcare & Administrative IDs  
**Original:** `MRN Number: GHI-789012`  
**Anonymized:** `MRN <MRN>: GHI-789012`  

---

### en

**Source:** Health  
**Original:** `NHS number 943 476 5919, MRN: ABC-123456, Insurance policy: POL-987654321.`  
**Anonymized:** `NHS number <HEALTH_ID>, MRN: <MRN>, <PASSPORT> policy: <INSURANCE_ID>.`  

---

### tl

**Source:** Healthcare & Administrative IDs  
**Original:** `MRN: ABC-123456`  
**Anonymized:** `MRN: <MRN>`  

---

## NO_ENTITY

### ca

**Source:** API & Authentication Tokens  
**Original:** `Android ID: 7a1b8c9d0e1f2a3b4c5d6e7f`  
**Anonymized:** `Android ID: 7a1b8c9d0e1f2a3b4c5d6e7f`  

---

### de

**Source:** German - Basics  
**Original:** `ich will Gewerbe anmelden.`  
**Anonymized:** `ich will Gewerbe anmelden.`  

**Source:** German - Edge Cases  
**Original:** `Ich wohne in Müritzsee.`  
**Anonymized:** `Ich wohne in Müritzsee.`  

**Source:** German - Edge Cases  
**Original:** `Meine Adresse: Schwabental`  
**Anonymized:** `Meine Adresse: Schwabental`  

**Source:** German - Edge Cases  
**Original:** `Ich heiße Anna Gasse.`  
**Anonymized:** `Ich heiße Anna Gasse.`  

**Source:** Government & Official IDs  
**Original:** `Voter ID: VID123456789`  
**Anonymized:** `Voter ID: VID123456789`  

**Source:** Government & Official IDs  
**Original:** `Benefit ID: BEN-2024-123456`  
**Anonymized:** `Benefit ID: BEN-2024-123456`  

**Source:** Government & Official IDs  
**Original:** `Welfare ID: WEL-2024-456789`  
**Anonymized:** `Welfare ID: WEL-2024-456789`  

---

### en

**Source:** API & Authentication Tokens  
**Original:** `Device Identifier: AABBCCDDEE11223344556677`  
**Anonymized:** `Device Identifier: AABBCCDDEE11223344556677`  

**Source:** Government & Official IDs  
**Original:** `Military ID: MIL-2024-777888`  
**Anonymized:** `Military ID: MIL-2024-777888`  

**Source:** Government & Official IDs  
**Original:** `Armed Forces ID: AF-2024-666777`  
**Anonymized:** `Armed Forces ID: AF-2024-666777`  

**Source:** Government & Official IDs  
**Original:** `Defence ID: DEF-2024-888999`  
**Anonymized:** `Defence ID: DEF-2024-888999`  

**Source:** Government & Official IDs  
**Original:** `University ID: UNI-2024-334455`  
**Anonymized:** `University ID: UNI-2024-334455`  

**Source:** Government & Official IDs  
**Original:** `Social Security: SOC-2024-654321`  
**Anonymized:** `Social Security: SOC-2024-654321`  

**Source:** Government & Official IDs  
**Original:** `Pension ID: PEN-2024-654987`  
**Anonymized:** `Pension ID: PEN-2024-654987`  

**Source:** Location & Geographic Codes  
**Original:** `w3w: ///index.home.raft`  
**Anonymized:** `w3w: ///index.home.raft`  

**Source:** Location & Geographic Codes  
**Original:** `what3words: ///filled.count.soap`  
**Anonymized:** `what3words: ///filled.count.soap`  

**Source:** Location & Geographic Codes  
**Original:** `w3w address: ///puffin.limits.jugs`  
**Anonymized:** `w3w address: ///puffin.limits.jugs`  

**Source:** Location & Geographic Codes  
**Original:** `what3words location: ///sorted.magic.spanned`  
**Anonymized:** `what3words location: ///sorted.magic.spanned`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Medical Record: DEF-456789`  
**Anonymized:** `Medical Record: DEF-456789`  

---

### es

**Source:** Authentication Secrets  
**Original:** `Codigo Autenticacion: 345678`  
**Anonymized:** `Codigo Autenticacion: 345678`  

---

### et

**Source:** API & Authentication Tokens  
**Original:** `jsessionid: D1C1234567890ABCDEF1234567890AB`  
**Anonymized:** `jsessionid: D1C1234567890ABCDEF1234567890AB`  

---

### fr

**Source:** Healthcare & Administrative IDs  
**Original:** `Patient Record: JKL-234567`  
**Anonymized:** `Patient Record: JKL-234567`  

---

### id

**Source:** Government & Official IDs  
**Original:** `Visa Number: V123456789`  
**Anonymized:** `Visa Number: V123456789`  

---

### it

**Source:** Authentication Secrets  
**Original:** `Codice Autenticazione: 234567`  
**Anonymized:** `Codice Autenticazione: 234567`  

---

### pl

**Source:** Healthcare & Administrative IDs  
**Original:** `Policy: INSURE987654321`  
**Anonymized:** `Policy: INSURE987654321`  

---

### pt

**Source:** Location & Geographic Codes  
**Original:** `Postcode: SW1A 2AA`  
**Anonymized:** `Postcode: SW1A 2AA`  

---

### so

**Source:** API & Authentication Tokens  
**Original:** `refresh_token: 1//0gxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`  
**Anonymized:** `refresh_token: 1//0gxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`  

**Source:** API & Authentication Tokens  
**Original:** `refresh_token: AQAB5Hxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`  
**Anonymized:** `refresh_token: AQAB5Hxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`  

**Source:** API & Authentication Tokens  
**Original:** `client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`  
**Anonymized:** `client_id: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`  

---

### tl

**Source:** Location & Geographic Codes  
**Original:** `PLZ: 10115`  
**Anonymized:** `PLZ: 10115`  

---

### uk

**Source:** Healthcare & Administrative IDs  
**Original:** `INSURE123456789`  
**Anonymized:** `INSURE123456789`  

---

### vi

**Source:** Healthcare & Administrative IDs  
**Original:** `Tâche: TASK2024444`  
**Anonymized:** `Tâche: TASK2024444`  

---

## OTP_CODE

### en

**Source:** API & Authentication Tokens  
**Original:** `Time-based OTP: 546374`  
**Anonymized:** `Time-based OTP: <OTP_CODE>`  

---

### it

**Source:** API & Authentication Tokens  
**Original:** `verification_code: 654321`  
**Anonymized:** `verification_code: <OTP_CODE>`  

---

### pt

**Source:** API & Authentication Tokens  
**Original:** `OTP Code: 123456`  
**Anonymized:** `OTP Code: <OTP_CODE>`  

**Source:** API & Authentication Tokens  
**Original:** `2FA Code: 987654`  
**Anonymized:** `2FA Code: <OTP_CODE>`  

---

## PASSPORT

### ar

**Source:** Arabic  
**Original:** `جواز السفر: A12345678`  
**Anonymized:** `جواز السفر: <PASSPORT>`  

---

### ca

**Source:** Government & Official IDs  
**Original:** `Electoral Card: 123-456-789-012`  
**Anonymized:** `<PASSPORT> Card: <PHONE>`  

---

### cy

**Source:** API & Authentication Tokens  
**Original:** `PHPSESSID: 9a1f6d3a8e4b7c2f5d9b1a3e6c8f2b5d`  
**Anonymized:** `<PASSPORT>: 9a1f6d3a8e4b7c2f5d9b1a3e6c8f2b5d`  

---

### de

**Source:** German - Basics  
**Original:** `Personalausweisnummer: T22000129`  
**Anonymized:** `Personalausweisnummer: <PASSPORT>`  

**Source:** Extended Government & Education IDs  
**Original:** `Meine Wählerausweinnummer: V4455667`  
**Anonymized:** `Meine Wählerausweinnummer: <PASSPORT>`  

**Source:** Extended Government & Education IDs  
**Original:** `Aufenthaltserlaubnis: RP999888`  
**Anonymized:** `Aufenthaltserlaubnis: <PASSPORT>`  

---

### en

**Source:** English  
**Original:** `U.S. Passport: K12345678`  
**Anonymized:** `U.S. Passport: <PASSPORT>`  

**Source:** French  
**Original:** `Passeport (UE): AB1234567`  
**Anonymized:** `<PASSPORT> (UE): <PASSPORT>`  

**Source:** French  
**Original:** `Passeport (UE): AB1234567`  
**Anonymized:** `<PASSPORT> (UE): <PASSPORT>`  

**Source:** US Tax & IDs  
**Original:** `U.S. Passport: Z98765432`  
**Anonymized:** `U.S. Passport: <PASSPORT>`  

**Source:** Health  
**Original:** `NHS number 943 476 5919, MRN: ABC-123456, Insurance policy: POL-987654321.`  
**Anonymized:** `NHS number <HEALTH_ID>, MRN: <MRN>, <PASSPORT> policy: <INSURANCE_ID>.`  

**Source:** Government & Official IDs  
**Original:** `DL: CA1234567`  
**Anonymized:** `DL: <PASSPORT>`  

**Source:** Government & Official IDs  
**Original:** `Architect License: ARC-2024-111222`  
**Anonymized:** `<PASSPORT> <PRO_LICENSE>: ARC-<PHONE>`  

**Source:** Extended Government & Education IDs  
**Original:** `My residence permit is RP654321`  
**Anonymized:** `My <PASSPORT> permit is <RESIDENCE_PERMIT>`  

**Source:** Extended Government & Education IDs  
**Original:** `Allocations familiales: A55566677`  
**Anonymized:** `Allocations familiales: <PASSPORT>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Insurance ID Policy123456`  
**Anonymized:** `<PASSPORT> ID <INSURANCE_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Insurance member: MYINSUR1234567`  
**Anonymized:** `<PASSPORT> member: <INSURANCE_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Medications: Insulin, Metformin`  
**Anonymized:** `Medications: Insulin, <PASSPORT>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Prescription: Hypertension treatment`  
**Anonymized:** `<HEALTH_INFO>: Hypertension <PASSPORT>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Condition: Diagnosed with cancer`  
**Anonymized:** `<PASSPORT>: <HEALTH_INFO> with <HEALTH_INFO>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Reference: REF2024555444`  
**Anonymized:** `<PASSPORT>: REF2024555444`  

---

### es

**Source:** Extended Government & Education IDs  
**Original:** `Permiso de residencia: RP666777`  
**Anonymized:** `Permiso de residencia: <PASSPORT>`  

---

### fr

**Source:** Extended Government & Education IDs  
**Original:** `Titre de séjour: RP777888`  
**Anonymized:** `Titre de séjour: <PASSPORT>`  

**Source:** Extended Government & Education IDs  
**Original:** `Carte d'allocataire: C98765432`  
**Anonymized:** `Carte d'allocataire: <PASSPORT>`  

**Source:** Extended Government & Education IDs  
**Original:** `Carte militaire: M88899900`  
**Anonymized:** `Carte <PASSPORT>: <MILITARY_ID>`  

---

### it

**Source:** Extended Government & Education IDs  
**Original:** `Numero di matricola: STU-99000`  
**Anonymized:** `Numero di <PASSPORT>: <ADDRESS>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Fascicolo: FASC2024456789`  
**Anonymized:** `<PASSPORT>: FASC2024456789`  

---

### pt

**Source:** Government & Official IDs  
**Original:** `Residence Permit: RP-2024-123456`  
**Anonymized:** `<PASSPORT> Permit: RP-2024-123456`  

---

### ro

**Source:** Extended Government & Education IDs  
**Original:** `Residence permit: RP123456`  
**Anonymized:** `<PASSPORT> permit: <RESIDENCE_PERMIT>`  

---

## PASSWORD

### af

**Source:** Authentication Secrets  
**Original:** `Password: MySecureP@ss2024!`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `User password: AlphaNum3r1c@Secure`  
**Anonymized:** `User <PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `Password is SuperStr0ng!Key#2025`  
**Anonymized:** `<PASSWORD>`  

---

### ca

**Source:** Authentication Secrets  
**Original:** `pwd: ComplexPass#789Arabic`  
**Anonymized:** `<PASSWORD>`  

---

### cy

**Source:** Authentication Secrets  
**Original:** `pwd: SpanishPass@Segura2024!`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: SpanishComplete@Protected`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: ItalianSecure@2024!`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: ItalianComplete@Protected`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: TurkishSecure2024@Pass`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: TurkishComplete@Protected`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: SecurePass2024@Arabic`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: ArabicSecurePass@Protected`  
**Anonymized:** `<PASSWORD>`  

---

### de

**Source:** Authentication Secrets  
**Original:** `pwd: Deutsch$Pass123Sicher`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `Passwort ist GesamterW@rt!Schutz`  
**Anonymized:** `<PASSWORD>`  

---

### en

**Source:** Authentication Secrets  
**Original:** `pwd: Complex$Pass#123`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `Passwort: SicherP@ssw0rt2024!`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: French$Pass789Secure`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: SpanishComplex#789Pass`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: Spanish$Pass456Secure`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: ItalianComplex#789Pass`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: Italiano$Pass123Secure`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: TurkishComplex#890Pass`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: Turkish$Pass789Secure`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `pwd: Arabic$Pass789Secure`  
**Anonymized:** `<PASSWORD>`  

**Source:** API & Authentication Tokens  
**Original:** `One-time password: 234567`  
**Anonymized:** `One-time <PASSWORD>`  

**Source:** Failed  
**Original:** `one_time_password=987654`  
**Anonymized:** `one_time_<PASSWORD>`  

---

### fr

**Source:** Authentication Secrets  
**Original:** `Mot de passe: MotDePasse@Secure2024`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `Mot de passe: ComplicedPass#456French`  
**Anonymized:** `<PASSWORD>`  

**Source:** Authentication Secrets  
**Original:** `Mot de passe est ComplexeFrEnc@Protected`  
**Anonymized:** `<PASSWORD>`  

---

### nl

**Source:** Authentication Secrets  
**Original:** `Kennwort: KomplexesK3nnw0rt#GmbH`  
**Anonymized:** `<PASSWORD>`  

---

## PAYMENT_TOKEN

### cy

**Source:** API & Authentication Tokens  
**Original:** `OAuth Token: ac2220a67b28eb907d90d07f051875275cab6b20`  
**Anonymized:** `OAuth Token: <PAYMENT_TOKEN>`  

---

### en

**Source:** API & Authentication Tokens  
**Original:** `Auth Token: 4517d1f2-4f81-4e1d-a6a8-c5c9d1b3f5d7`  
**Anonymized:** `<PERSON>: <PAYMENT_TOKEN>`  

---

## PERSON

### ar

**Source:** Arabic  
**Original:** `اسمي أحمد محمد. ولدت في 31/12/1990.`  
**Anonymized:** `اسمي <PERSON>. ولدت في <DATE>.`  

---

### de

**Source:** German - Basics  
**Original:** `Mein Name ist Max Mustermann, geboren am 31.12.1990.`  
**Anonymized:** `Mein Name ist <PERSON>, geboren am <DATE>.`  

**Source:** German - Basics  
**Original:** `ich Heisse Max Mustermann und ich bin am 31.12.1990 geboren.`  
**Anonymized:** `ich Heisse <PERSON> und ich bin am <DATE> geboren.`  

**Source:** German - Basics  
**Original:** `ich heisse Max Mustermann und ich bin am 31.12.1990 geboren.`  
**Anonymized:** `ich heisse <PERSON> und ich bin am <DATE> geboren.`  

**Source:** German - Basics  
**Original:** `ich heisse max mustermann und ich bin am 31.12.1990 geboren.`  
**Anonymized:** `ich heisse <PERSON> und ich bin am <DATE> geboren.`  

**Source:** German - Basics  
**Original:** `ich bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `Ich Bin Anna Müller und ich wohne in der Blablastrasse 9, Berlin 10999. I will ein Gewerbe anmelden`  
**Anonymized:** `Ich Bin <PERSON> und ich wohne <ADDRESS> 10999. I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `ich Bin Sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich Bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `ich bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `ich Bin sebastian Holz und ich wohne in blablastrasse. 9, wer bist du? I will ein Gewerbe anmelden`  
**Anonymized:** `ich Bin <PERSON> und ich wohne <ADDRESS>, wer bist du? I will ein Gewerbe anmelden`  

**Source:** German - Basics  
**Original:** `Guten Tag, mein name ist Frank Verz, ich möchte ein Gewerbe anmelden.`  
**Anonymized:** `Guten Tag, mein name ist <PERSON>, <PERSON> anmelden.`  

**Source:** German - Basics  
**Original:** `Guten Tag, mein name ist Frank Verz, ich möchte ein Gewerbe anmelden.`  
**Anonymized:** `Guten Tag, mein name ist <PERSON>, <PERSON> anmelden.`  

**Source:** German - Basics  
**Original:** `Gibt es Beratungszentern in Tempelhof-Shöneberg für Gründung von Unternehmen?`  
**Anonymized:** `<PERSON> <ADDRESS>?`  

**Source:** Government & Official IDs  
**Original:** `Mitarbeiternummer: MIT-2024-778899`  
**Anonymized:** `<PERSON>: <EMPLOYEE_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Aufenthaltstitel: RP333444`  
**Anonymized:** `<PERSON>: <RESIDENCE_PERMIT>`  

**Source:** Extended Government & Education IDs  
**Original:** `Militärausweis: M33344455`  
**Anonymized:** `<PERSON>: <MILITARY_ID>`  

---

### en

**Source:** English  
**Original:** `My name is John Smith. I was born on 12/31/1990.`  
**Anonymized:** `My name is <PERSON>. I was born on <DATE>.`  

**Source:** US Tax & IDs  
**Original:** `Name: Jane Miller. I was born on 31 December 1988.`  
**Anonymized:** `Name: <PERSON>. I was born on <DATE>.`  

**Source:** API & Authentication Tokens  
**Original:** `Auth Token: 4517d1f2-4f81-4e1d-a6a8-c5c9d1b3f5d7`  
**Anonymized:** `<PERSON>: <PAYMENT_TOKEN>`  

---

### es

**Source:** Spanish  
**Original:** `Me llamo Carlos García. Nací el 31/12/1990.`  
**Anonymized:** `Me llamo <PERSON>. Nací el <DATE>.`  

**Source:** Authentication Secrets  
**Original:** `Codigo Desbloqueo: 44444444`  
**Anonymized:** `<PERSON>: <PHONE>`  

---

### fr

**Source:** French  
**Original:** `Je m'appelle Marie Dupont, née le 31-05-1995.`  
**Anonymized:** `Je m'appelle <PERSON>, née le <DATE>.`  

---

### nl

**Source:** API & Authentication Tokens  
**Original:** `GitHub Token: ghp_1234567890abcdefghijklmnopqrstuvwxyz`  
**Anonymized:** `GitHub <PERSON>: <API_KEY>`  

---

### pt

**Source:** Location & Geographic Codes  
**Original:** `Code Postal: 75001`  
**Anonymized:** `Code <PERSON>: <ACCESS_CODE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Dossier Médical: MNO-567890`  
**Anonymized:** `<PERSON>: MNO-567890`  

---

### sv

**Source:** Extended Government & Education IDs  
**Original:** `Matrikelnummer: STU-55666`  
**Anonymized:** `<PERSON>: <ADDRESS>`  

**Source:** Extended Government & Education IDs  
**Original:** `Personalnummer: EMP-12345`  
**Anonymized:** `<PERSON>: <EMPLOYEE_ID>`  

---

### tr

**Source:** Turkish  
**Original:** `Benim adım Ahmet Yılmaz. Doğum tarihim 01-01-1992.`  
**Anonymized:** `Benim adım <PERSON>. Doğum tarihim <DATE>.`  

**Source:** Turkish  
**Original:** `Adresim Atatürk Caddesi No:15, Ankara.`  
**Anonymized:** `<PERSON><ADDRESS>.`  

---

## PHONE_NUMBER

### ar

**Source:** Arabic  
**Original:** `بريدي الإلكتروني ahmed.mohamed@example.com ورقم هاتفي +966 50 123 4567.`  
**Anonymized:** `بريدي الإلكتروني <EMAIL> ورقم هاتفي <PHONE>.`  

**Source:** Authentication Secrets  
**Original:** `مفتاح-فتح-الحظر: 43210987`  
**Anonymized:** `مفتاح-فتح-الحظر: <PHONE>`  

---

### ca

**Source:** Government & Official IDs  
**Original:** `Electoral Card: 123-456-789-012`  
**Anonymized:** `<PASSPORT> Card: <PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Travel Document: TD-2024-111222`  
**Anonymized:** `Travel Document: TD-<PHONE>`  

---

### de

**Source:** Government & Official IDs  
**Original:** `Voter Registration: VOT-2024-987654`  
**Anonymized:** `Voter Registration: VOT-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Permit Number: P-2024-999888`  
**Anonymized:** `Permit Number: P-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Aufenthaltserlaubnis: AE-2024-555666`  
**Anonymized:** `Aufenthaltserlaubnis: AE-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Staff Number: STF-2024-555666`  
**Anonymized:** `Staff Number: STF-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Enrollment Number: ENR-2024-112233`  
**Anonymized:** `Enrollment Number: ENR-<PHONE>`  

**Source:** Financial & Routing  
**Original:** `Document Number: DOC-2024-777888`  
**Anonymized:** `Document Number: DOC-<PHONE>`  

**Source:** Financial & Routing  
**Original:** `Order Number: ORD-2024-456789`  
**Anonymized:** `Order Number: ORD-<PHONE>`  

---

### en

**Source:** English  
**Original:** `You can reach me at john.smith@example.com or call +44 7700 900123.`  
**Anonymized:** `You can reach me at <EMAIL> or call <PHONE>.`  

**Source:** US Tax & IDs  
**Original:** `Email: jane.miller@example.org, Phone: +1 (213) 555-0182`  
**Anonymized:** `Email: <EMAIL>, Phone: <PHONE>`  

**Source:** Government & Official IDs  
**Original:** `EU Driver License: 1234567/19/AB/CD`  
**Anonymized:** `EU Driver <PRO_LICENSE>: <PHONE>/19/AB/CD`  

**Source:** Government & Official IDs  
**Original:** `Service Number: SN-2024-333444`  
**Anonymized:** `Service Number: SN-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Military Service Number: MSN-1990-234567`  
**Anonymized:** `Military Service Number: MSN-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Architect License: ARC-2024-111222`  
**Anonymized:** `<PASSPORT> <PRO_LICENSE>: ARC-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Professional Registration: PRF-2024-333444`  
**Anonymized:** `Professional Registration: PRF-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Child Benefit: CHB-2024-321456`  
**Anonymized:** `Child Benefit: CHB-<PHONE>`  

**Source:** Financial & Routing  
**Original:** `Invoice Number: INV-2024-999000`  
**Anonymized:** `Invoice Number: INV-<PHONE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Health record: 789 012 3456`  
**Anonymized:** `Health record: <PHONE>`  

---

### es

**Source:** Spanish  
**Original:** `Mi correo es carlos.garcia@email.com y mi teléfono es +34 612 345 678.`  
**Anonymized:** `Mi correo es <EMAIL> y mi teléfono es <PHONE>.`  

**Source:** Authentication Secrets  
**Original:** `Codigo Desbloqueo: 44444444`  
**Anonymized:** `<PERSON>: <PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Contractor License: CTR-2024-777888`  
**Anonymized:** `Contractor <PRO_LICENSE>: CTR-<PHONE>`  

---

### fr

**Source:** French  
**Original:** `Mon email est marie.dupont@gmail.com et mon numéro est 06 12 34 56 78.`  
**Anonymized:** `Mon email est <EMAIL> et mon numéro est <PHONE>.`  

**Source:** Government & Official IDs  
**Original:** `Unemployment Benefit: UNE-2024-987654`  
**Anonymized:** `Unemployment Benefit: UNE-<PHONE>`  

---

### nl

**Source:** Government & Official IDs  
**Original:** `Driving License: 1234567/ABC/2015/00123`  
**Anonymized:** `Driving <PRO_LICENSE>: <PHONE>/ABC/2015/00123`  

---

### pt

**Source:** Turkish  
**Original:** `E‑posta adresim ahmet.yilmaz@example.com ve telefon numaram 0555 123 45 67.`  
**Anonymized:** `E‑posta adresim <EMAIL> ve telefon numaram <PHONE>.`  

---

## PIN

### ca

**Source:** Authentication Secrets  
**Original:** `personal id: 1616`  
**Anonymized:** `<PIN>`  

---

### cy

**Source:** Authentication Secrets  
**Original:** `Codigo PIN: 7777`  
**Anonymized:** `Codigo <PIN>`  

---

### en

**Source:** Authentication Secrets  
**Original:** `personal id number: 6789`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `personal identification number: 8888`  
**Anonymized:** `<PIN>`  

---

### fr

**Source:** Authentication Secrets  
**Original:** `code-secret: 2222`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `code-secret: 6666`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `code-secret: 1010`  
**Anonymized:** `<PIN>`  

---

### id

**Source:** Authentication Secrets  
**Original:** `Personal ID Number: 3456`  
**Anonymized:** `<PIN>`  

---

### it

**Source:** Authentication Secrets  
**Original:** `personal identification number: 4444`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `personal identification number: 1212`  
**Anonymized:** `<PIN>`  

---

### pt

**Source:** Authentication Secrets  
**Original:** `PIN-Code: 8901`  
**Anonymized:** `<PIN>: <ACCESS_CODE>`  

**Source:** Authentication Secrets  
**Original:** `Code PIN: 3333`  
**Anonymized:** `Code <PIN>`  

---

### ro

**Source:** Authentication Secrets  
**Original:** `Codice PIN: 1111`  
**Anonymized:** `Codice <PIN>`  

---

### tl

**Source:** Authentication Secrets  
**Original:** `PIN: 1234`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 5678`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 9012`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 4567`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 2345`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1111`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 5555`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 9999`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1313`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1414`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1515`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1717`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1818`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 1919`  
**Anonymized:** `<PIN>`  

**Source:** Authentication Secrets  
**Original:** `PIN: 2020`  
**Anonymized:** `<PIN>`  

---

## PLUS_CODE

### en

**Source:** Location & Geographic Codes  
**Original:** `location_code: 7PHWJ4WJ+M2`  
**Anonymized:** `location_code: <PLUS_CODE>`  

---

### es

**Source:** Location & Geographic Codes  
**Original:** `plus_code: 8QQH+RR Lagos`  
**Anonymized:** `plus_code: <PLUS_CODE> Lagos`  

---

## PRO_LICENSE

### en

**Source:** Government & Official IDs  
**Original:** `License Number: SMITH121080A1A2`  
**Anonymized:** `License Number: <PRO_LICENSE>`  

**Source:** Government & Official IDs  
**Original:** `EU Driver License: 1234567/19/AB/CD`  
**Anonymized:** `EU Driver <PRO_LICENSE>: <PHONE>/19/AB/CD`  

**Source:** Government & Official IDs  
**Original:** `Professional License: LIC-2024-567890`  
**Anonymized:** `Professional License: <PRO_LICENSE>`  

**Source:** Government & Official IDs  
**Original:** `Architect License: ARC-2024-111222`  
**Anonymized:** `<PASSPORT> <PRO_LICENSE>: ARC-<PHONE>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `License Plate: AB 12 CDE`  
**Anonymized:** `<PRO_LICENSE> Plate: <LICENSE_PLATE>`  

---

### es

**Source:** Government & Official IDs  
**Original:** `Contractor License: CTR-2024-777888`  
**Anonymized:** `Contractor <PRO_LICENSE>: CTR-<PHONE>`  

**Source:** Government & Official IDs  
**Original:** `Medical License: MED-2024-999000`  
**Anonymized:** `Medical License: <PRO_LICENSE>`  

---

### nl

**Source:** Government & Official IDs  
**Original:** `Driver License: D12345678`  
**Anonymized:** `Driver <PRO_LICENSE>: <DRIVER_LICENSE>`  

**Source:** Government & Official IDs  
**Original:** `Driving License: 1234567/ABC/2015/00123`  
**Anonymized:** `Driving <PRO_LICENSE>: <PHONE>/ABC/2015/00123`  

**Source:** Government & Official IDs  
**Original:** `License Number: PROF-000123456`  
**Anonymized:** `License Number: <PRO_LICENSE>`  

---

## PUK

### cy

**Source:** Authentication Secrets  
**Original:** `Codigo PUK: 88888888`  
**Anonymized:** `Codigo <PUK>`  

---

### en

**Source:** Authentication Secrets  
**Original:** `PUK: 12345678`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `pin-unlock-key: 87654321`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 23456789`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 22222222`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 34567890`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 09876543`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 33333333`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 45678901`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 10987654`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 56789012`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 21098765`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 32109876`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 66666666`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 78901234`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 78901234`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 43210987`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 77777777`  
**Anonymized:** `<PUK>`  

---

### it

**Source:** Authentication Secrets  
**Original:** `Chiave Sblocco: 55555555`  
**Anonymized:** `<PUK>`  

---

### pt

**Source:** Authentication Secrets  
**Original:** `PUK-code: 55555555`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK-Code: 66666666`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `Code PUK: 77777777`  
**Anonymized:** `Code <PUK>`  

---

### ro

**Source:** Authentication Secrets  
**Original:** `Codice PUK: 99999999`  
**Anonymized:** `Codice <PUK>`  

---

### tl

**Source:** Authentication Secrets  
**Original:** `PUK: 98765432`  
**Anonymized:** `<PUK>`  

**Source:** Authentication Secrets  
**Original:** `PUK: 67890123`  
**Anonymized:** `<PUK>`  

---

## RECOVERY_CODE

### ca

**Source:** Authentication Secrets  
**Original:** `backup-code: XYZ-ABC-789-012`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `backup-code: BCD-EFG-890-123`  
**Anonymized:** `<RECOVERY_CODE>`  

---

### en

**Source:** Authentication Secrets  
**Original:** `recovery-code: ABC-DEF-123-456`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: ABCD-EFGH-IJKL-MNOP`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 1234-5678-9012-3456`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: DEF-GHI-234-567`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: BCDE-FGHI-JKLM-NOPQ`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 2345-6789-0123-4567`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: GHI-JKL-345-678`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `backup-code: HIJ-KLM-901-234`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: CDEF-GHIJ-KLMN-OPQR`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 3456-7890-1234-5678`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: JKL-MNO-456-789`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `backup-code: KLM-NOP-012-345`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: DEFG-HIJK-LMNO-PQRS`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 4567-8901-2345-6789`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: MNO-PQR-567-890`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `backup-code: NOP-QRS-123-456`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: EFGH-IJKL-MNOP-QRST`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 5678-9012-3456-7890`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: PQR-STU-678-901`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `backup-code: QRS-TUV-234-567`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: FGHI-JKLM-NOPQ-RSTU`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 6789-0123-4567-8901`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: STU-VWX-789-012`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `backup-code: TUV-WXY-345-678`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery: GHIJ-KLMN-OPQR-STUV`  
**Anonymized:** `<RECOVERY_CODE>`  

**Source:** Authentication Secrets  
**Original:** `recovery-code: 7890-1234-5678-9012`  
**Anonymized:** `<RECOVERY_CODE>`  

---

## REFRESH_TOKEN

### en

**Source:** synthesized  
**Original:** `Example REFRESH_TOKEN placeholder: <REFRESH_TOKEN>`  
**Anonymized:** `Example REFRESH_TOKEN placeholder: <REFRESH_TOKEN>`  

---

## RESIDENCE_PERMIT

### de

**Source:** Extended Government & Education IDs  
**Original:** `Aufenthaltstitel: RP333444`  
**Anonymized:** `<PERSON>: <RESIDENCE_PERMIT>`  

---

### en

**Source:** Extended Government & Education IDs  
**Original:** `My residence permit is RP654321`  
**Anonymized:** `My <PASSPORT> permit is <RESIDENCE_PERMIT>`  

---

### ro

**Source:** Extended Government & Education IDs  
**Original:** `Residence permit: RP123456`  
**Anonymized:** `<PASSPORT> permit: <RESIDENCE_PERMIT>`  

---

## ROUTING_NUMBER

### en

**Source:** Payments  
**Original:** `Routing (ABA): 021000021. Kontonummer: 1234-567890-12.`  
**Anonymized:** `Routing (ABA): <ROUTING_NUMBER>. <SERVICEKONTO>: <ACCOUNT_NUMBER>.`  

**Source:** Financial & Routing  
**Original:** `Routing Number: 021000021`  
**Anonymized:** `Routing Number: <ROUTING_NUMBER>`  

---

### id

**Source:** Financial & Routing  
**Original:** `Bank Routing: 061000146`  
**Anonymized:** `Bank Routing: <ROUTING_NUMBER>`  

---

## SERVICEKONTO

### da

**Source:** German - Payments/Bank  
**Original:** `Kontonummer: 1234-567890-12`  
**Anonymized:** `<SERVICEKONTO>: <ACCOUNT_NUMBER>`  

---

### en

**Source:** Payments  
**Original:** `Routing (ABA): 021000021. Kontonummer: 1234-567890-12.`  
**Anonymized:** `Routing (ABA): <ROUTING_NUMBER>. <SERVICEKONTO>: <ACCOUNT_NUMBER>.`  

**Source:** German E-Government IDs  
**Original:** `Konto-ID: account_gov_12345`  
**Anonymized:** `<SERVICEKONTO>_gov_12345`  

**Source:** German E-Government IDs  
**Original:** `Government-Account: gov_12345678`  
**Anonymized:** `<SERVICEKONTO>`  

---

### hr

**Source:** German E-Government IDs  
**Original:** `Servicekonto-ID: SK-2024-001234`  
**Anonymized:** `Servicekonto-ID: <SERVICEKONTO>`  

**Source:** German E-Government IDs  
**Original:** `Servicekonto: 123456789`  
**Anonymized:** `<SERVICEKONTO>`  

---

### it

**Source:** German E-Government IDs  
**Original:** `Service-Konto: servicekonto_56789`  
**Anonymized:** `<SERVICEKONTO>`  

---

## SESSION_ID

### en

**Source:** synthesized  
**Original:** `Example SESSION_ID placeholder: <SESSION_ID>`  
**Anonymized:** `Example SESSION_ID placeholder: <SESSION_ID>`  

---

## SOCIAL_HANDLE

### ca

**Source:** Healthcare & Administrative IDs  
**Original:** `Contact me at @alex_dev_2024`  
**Anonymized:** `Contact me at <SOCIAL_HANDLE>`  

---

### da

**Source:** Healthcare & Administrative IDs  
**Original:** `Telegram: @signal_user_456`  
**Anonymized:** `Telegram: <SOCIAL_HANDLE>`  

---

### de

**Source:** Healthcare & Administrative IDs  
**Original:** `Discord user: @techie_coder_789`  
**Anonymized:** `Discord user: <SOCIAL_HANDLE>`  

---

### en

**Source:** German - Communications  
**Original:** `Twitter @hans_muell3r`  
**Anonymized:** `Twitter <SOCIAL_HANDLE>`  

**Source:** Comms/Devices/Geo  
**Original:** `Twitter @john_doe123, email john.doe@acme.io, Discord user#1234,`  
**Anonymized:** `Twitter <SOCIAL_HANDLE>, email <EMAIL>, Discord <MESSAGING_ID>,`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Follow @john_smith on Twitter`  
**Anonymized:** `Follow <SOCIAL_HANDLE> on Twitter`  

**Source:** Healthcare & Administrative IDs  
**Original:** `My handle is @mary_j_watson`  
**Anonymized:** `My handle is <SOCIAL_HANDLE>`  

---

## STUDENT_NUMBER

### de

**Source:** Government & Official IDs  
**Original:** `Student Number: STU-2024-456789`  
**Anonymized:** `Student Number: <STUDENT_NUMBER>`  

**Source:** Extended Government & Education IDs  
**Original:** `Student number: STU-12345`  
**Anonymized:** `Student number: <STUDENT_NUMBER>`  

---

### en

**Source:** Extended Government & Education IDs  
**Original:** `My student ID is STU-54321`  
**Anonymized:** `My student ID is <STUDENT_NUMBER>`  

---

## TAN

### es

**Source:** Authentication Secrets  
**Original:** `Numero TAN: 789123`  
**Anonymized:** `Numero <TAN>`  

**Source:** Authentication Secrets  
**Original:** `Numero TAN: 678912`  
**Anonymized:** `Numero <TAN>`  

---

### pt

**Source:** Authentication Secrets  
**Original:** `TAN code: 345678`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN-Code: 456789`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `Numero TAN: 567891`  
**Anonymized:** `Numero <TAN>`  

---

### vi

**Source:** Authentication Secrets  
**Original:** `TAN: 654321`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 765432`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 098765`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 012345`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 654987`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 321654`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 543216`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 210543`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 432109`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 109432`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 321098`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 098321`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 456789`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 123456`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 210987`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 987210`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 345678`  
**Anonymized:** `<TAN>`  

**Source:** Authentication Secrets  
**Original:** `TAN: 012345`  
**Anonymized:** `<TAN>`  

---

## TAX_ID

### ca

**Source:** Spanish  
**Original:** `VAT: ES X1234567T`  
**Anonymized:** `VAT: <TAX_ID>`  

---

### de

**Source:** German - Basics  
**Original:** `Steuer-ID: 12 345 678 901`  
**Anonymized:** `Steuer-ID: <TAX_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `VAT: GB 987654321`  
**Anonymized:** `VAT: <TAX_ID>`  

---

### hu

**Source:** Healthcare & Administrative IDs  
**Original:** `NIF: ES A12345678`  
**Anonymized:** `NIF: <TAX_ID>`  

---

### so

**Source:** Healthcare & Administrative IDs  
**Original:** `Tax Number: FR 1234567890`  
**Anonymized:** `Tax Number: <TAX_ID>`  

---

## TICKET_ID

### cs

**Source:** Healthcare & Administrative IDs  
**Original:** `Problem ID: PROB2024777`  
**Anonymized:** `<TICKET_ID>`  

---

### en

**Source:** Case Reference (Multilingual)  
**Original:** `Ticket ID: TKT-2024-999`  
**Anonymized:** `<TICKET_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Issue Number: ISSUE2024001`  
**Anonymized:** `<TICKET_ID>`  

---

### fr

**Source:** Healthcare & Administrative IDs  
**Original:** `Issue ID: ISSUE2024555`  
**Anonymized:** `<TICKET_ID>`  

---

### id

**Source:** Healthcare & Administrative IDs  
**Original:** `Task Number: TASK2024888`  
**Anonymized:** `<TICKET_ID>`  

---

### sv

**Source:** Healthcare & Administrative IDs  
**Original:** `Ticket ID: TKT2024999`  
**Anonymized:** `<TICKET_ID>`  

**Source:** Healthcare & Administrative IDs  
**Original:** `Ticketnummer: TKT2024666`  
**Anonymized:** `<TICKET_ID>`  

---

## TRANSACTION_NUMBER

### en

**Source:** Authentication Secrets  
**Original:** `transaction-authentication-number: 789012`  
**Anonymized:** `<TRANSACTION_NUMBER>-number: 789012`  

**Source:** Financial & Routing  
**Original:** `Transaction ID: TXN-2024-654321`  
**Anonymized:** `<TRANSACTION_NUMBER>21`  

---

## VOTER_ID

### af

**Source:** Extended Government & Education IDs  
**Original:** `My voter ID is V1234567`  
**Anonymized:** `My voter ID is <VOTER_ID>`  

---

### ca

**Source:** Extended Government & Education IDs  
**Original:** `Voter card: V7788990`  
**Anonymized:** `Voter card: <VOTER_ID>`  

---

### de

**Source:** Extended Government & Education IDs  
**Original:** `Voter ID: V9876543`  
**Anonymized:** `Voter ID: <VOTER_ID>`  

**Source:** Extended Government & Education IDs  
**Original:** `Wählerausweis: V1122334`  
**Anonymized:** `Wählerausweis: <VOTER_ID>`  

---

## W3W

### en

**Source:** synthesized  
**Original:** `Example W3W placeholder: <W3W>`  
**Anonymized:** `Example W3W placeholder: <W3W>`  

---

*End of Report*
