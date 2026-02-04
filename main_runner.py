
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

    "German (expanded)": """
Mein Name ist Max Mustermann, geboren am 31.12.1990.
Ich wohne in der Musterstraße 5, 10115 Berlin (Mitte).
Meine E-Mail ist max.mustermann@beispiel.de und meine Nummer ist 0176 12345678.
Personalausweisnummer: T22000129
Steuer-ID: 12 345 678 901
USt-IdNr.: DE 123456789

# Deutsche Straßenvarianten (Suffixe, Präfixe, Komposita)
Adresse: Am Waldrand 12, 50667 Köln.
Ich wohne Im Tal 7; An der See 3 (OH).
Unter den Linden 77, 10117 Berlin.
Karl-Marx-Allee 1, 10243 Berlin.
Lange Reihe 15, 20099 Hamburg.
Gänsemarkt 2, 20354 Hamburg.
Königsberger Feld 4, 69120 Heidelberg.

# Wohnungstails (DE/AT-Stil gemischt)
Musterstraße 10, Whg. 5, 2. Etage, 01067 Dresden.
Hauptstraße 12, Stiege 2, Top 14, 2. OG, 1010 Wien.

# PLZ → LOCATION
DE-10115 Berlin (Mitte)
50667 Köln
20095 Hamburg (Altstadt)

# Zahlungen/Bank
Visa 4111 1111 1111 1111
IBAN: DE44 5001 0517 5407 3249 31, BIC: COBADEFFXXX
Kontonummer: 1234-567890-12

# Comms/Meeting
Fax: +49 30 1234567
Meeting ID: 987 654 321
Twitter @hans_muell3r
Discord hans#1234
Google Meet: abc-defg-hij

# Devices/Netz
IP: 192.168.1.10 und IPv6: 2001:db8::1
MAC 00:1A:2B:3C:4D:5E; IMEI 490154203237518
IDFA: 123e4567-e89b-12d3-a456-426614174000, Gerät-ID: 123e4567-e89b-12d3-a456-426614174001

# Geo/Extras
Koordinaten: 52.5200, 13.4050; Plus Code: 9C3W9QCJ+2V; w3w: ///index.home.raft
Kennzeichen: B-AB 1234

# Edge cases für Guards
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

    # Default: run built-in corpus
    runner.run_on_texts(
        TEST_TEXTS,
        show_entities=show_entities,
        show_anonymized=show_anonymized,
        json_mode=args.json,
        **guard_kw
    )


if __name__ == "__main__":
    main()
