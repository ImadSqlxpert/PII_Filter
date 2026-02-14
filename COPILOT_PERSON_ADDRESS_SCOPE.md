# Copilot Task: Improve <PERSON> & <ADDRESS> (German + English) in `PIIFilter` without touching other entities

We have a large `PIIFilter` class that already passes our test suite, but <PERSON> and <ADDRESS> are still prone to false positives in real chat/user text.

You must:
- Increase **precision** and **stability** for **German (de)** and **English (en)** PERSON/ADDRESS.
- **Do not** change any behavior for other entities (PHONE_NUMBER, DATE, ID_NUMBER, PASSPORT, TAX_ID, BANK_ACCOUNT, CREDIT_CARD, API_KEY, PAYMENT_TOKEN, MAC_ADDRESS, IP_ADDRESS, DEVICE_ID, HEALTH_*, etc.).
- Keep the current public API and placeholders (e.g., `<PERSON>`, `<ADDRESS>`) unchanged.
- Keep execution time within ±10% of current.

We will use two focused test files that must pass alongside the existing suite:
- `tests/unit/test_person_address_de_en.py`
- `tests/unit/test_chat_person_address_de_en.py`

## Context about the class (anchors you can use directly)
These objects and helpers already exist—**reuse and extend** them rather than inventing new structures:

- PERSON logic:
  - `_plausible_person(span, text, start)`
  - `_inject_name_intro_persons(text, results)`
  - `INTRO_PATTERNS`, `INTRO_CUES`
  - `NON_PERSON_SINGLE_TOKENS`, `PERSON_BLACKLIST_WORDS`, `PRONOUN_PERSONS`
  - `STREET_BLOCKERS`  (already contains DE street tokens + multi‑lang)
  - Priority resolution via `_resolve_overlaps(text, items)` and `_effective_priority(text, r)`

- ADDRESS logic:
  - `STRICT_ADDRESS_RX`  (strict multi‑lang street patterns)
  - `FALLBACK_STREET_RX` (conservative fallback)
  - `POSTAL_EU_PATTERNS`  (emits LOCATION)
  - Label/adjacency filters: `_filter_label_leading_locations`, `_filter_label_adjacent_locations`
  - Guards: `_guard_single_token_addresses`, `_guard_natural_suffix_requires_number`, `_trim_address_spans`
  - Merge: `_merge_address_location(text, items)`
  - Email/URL guard: `_span_inside_email(text, s, e)`

**Important:** Do not modify other recognizers or their order; scope changes to PERSON/ADDRESS and their guards/overlap rules only.

## Desired behavior (summarized)
**PERSON**
- True positives: DE/EN with intro cues like “Mein Name ist … / Ich heiße … / My name is … / I am called …”.
- False positives to avoid:
  - Single street words (“Straße”, “Weg”, “Gasse”, “Allee”, “Street”, “Road/rd”, “St.”) not part of a name.
  - All‑caps labels (“RECHNUNG”, “KUNDENNUMMER”, “ADDRESS”).
  - Date contexts (e.g., “am 12. März”), city‑only mentions, phone/email labels.
  - Single-token PERSON without an intro cue (except obviously name-like, capitalized tokens and no street/role words).

**ADDRESS**
- True positives: street + number (DE/EN), optional postal+city adjacency or merge across comma/newline/dash.
- False positives to avoid:
  - Single street‑type tokens alone (no number).
  - City‑only spans; they may be `<LOCATION>` but not `<ADDRESS>`.
  - Address spans inside/adjacent to emails/URLs or after labels like “Email:” or “Telefon:”.
  - Natural suffix nouns (Berg, Wald, Feld, See, Bach) without number/postal context.

**Overlap rules (PERSON vs ADDRESS)**
- If an intro cue precedes a name span → prefer `<PERSON>`.
- Else if there is a house number or postal context → prefer `<ADDRESS>`.
- Else drop the weaker/ambiguous one (favor precision).

## Implementation tasks (minimal, safe changes)

### 1) PERSON tightening (DE + EN)
- In `_plausible_person()`:
  - Keep existing guards (no digits, not UUID-like, not all‑caps).
  - Require at least one **capitalized** token for DE/EN when **no intro cue** is present.
  - Limit single-token PERSON: only accept if **intro cue** exists and token is name‑like (capitalized, not in negative lexicons, not a street type).
  - Reuse `STREET_BLOCKERS` to reject spans that end with street suffixes.
  - Expand negative lexicons by extending `NON_PERSON_SINGLE_TOKENS` / `PERSON_BLACKLIST_WORDS` with DE/EN function/role words (e.g., “adresse”, “address”, “straße/strasse/str.”, “weg”, “gasse”, “allee”, “platz”, “market/markt”, “nummer/no/nr”, “ticket/issue/case”, “device”, “konto/account”, days/months in DE/EN). Keep these expansions **localized** (avoid impacting other entities).

- Intro‑cue handling:
  - If `_has_intro_prefix(text, start)` is true, accept `<PERSON>` unless the last token is a street‑type word; ensure at least one capitalized token.

### 2) ADDRESS tightening (strict + fallback + guards)
- Keep `STRICT_ADDRESS_RX` unchanged structurally, but apply **post-match guards** before injection:
  - Require either a house **number** in the span or a **street-suffix + (right-context) number**, or a **postal+city adjacency** validated by `POSTAL_EU_PATTERNS`.
  - Do not inject `<ADDRESS>` for single-token street‑type matches without digits.
- Keep `FALLBACK_STREET_RX` but ensure it requires “<StreetName><StreetType> <Number>”.
- `_trim_address_spans()`: ensure trimming at newline/“Email:”/“Telefon:” labels to avoid bleed.
- Add a simple URL guard for ADDRESS similar to `_span_inside_email` (if not present): if a candidate lies inside a URL or immediately adjacent to a URL segment, drop it (use a lightweight URL regex).

### 3) Overlap resolution (PERSON vs ADDRESS only)
- In `_resolve_overlaps()`:
  - Add a branch handling the pair {PERSON, ADDRESS} only:
    - If intro cue near PERSON → keep PERSON, drop ADDRESS.
    - Else if ADDRESS span contains digits or passes postal adjacency → keep ADDRESS, drop PERSON.
    - Else drop the one with lower effective priority/score. Do **not** change overlap logic for other entity pairs.

### 4) Small helpers (keep them local)
- Add `_looks_like_name_de_en(tokens: list[str]) -> bool` used by `_plausible_person()`: return True if ≥1 capitalized token, no digits, not all‑caps, not in street/role lexicons.
- Optionally add `_has_postal_context(text: str, s: int, e: int) -> bool` to detect nearby postal+city adjacency using `POSTAL_EU_PATTERNS`. Use it ONLY for ADDRESS post-guards and PERSON/ADDRESS overlap decisions.

### 5) Tests as contract (don’t change other entities)
- Make sure these two new files pass with your edits:
  - `tests/unit/test_person_address_de_en.py`
  - `tests/unit/test_chat_person_address_de_en.py`
- Then run the full suite. No regressions are allowed in other entities.

## Accept/Reject boundaries
- ✅ Allowed: Edits to `_plausible_person`, ADDRESS post‑guards, trimming/URL guards, overlap logic for PERSON vs ADDRESS, lexicon expansions.
- ❌ Not allowed: Renaming entities/placeholders, altering other recognizers, changing injection order for non‑PERSON/ADDRESS blocks, removing validations (Luhn, IBAN), or introducing heavy external models.

## Scoring & priority
- Keep existing scores for other entities. Any score tweaks should be localized to PERSON/ADDRESS matches and only insofar as needed to enforce the overlap rules above (intro‑cue → PERSON; numeric/postal → ADDRESS).

## Output from you (Copilot)
1) Minimal patches to `PIIFilter` implementing the items above (focused diffs, well‑commented).
2) No changes to the signatures of public methods.
3) All tests pass:
   - `pytest tests/unit/test_person_address_de_en.py -q`
   - `pytest tests/unit/test_chat_person_address_de_en.py -q`
   - full suite `pytest -q`

> If a suggestion impacts entities outside PERSON/ADDRESS, **retract** and propose a smaller change constrained to the specified areas.