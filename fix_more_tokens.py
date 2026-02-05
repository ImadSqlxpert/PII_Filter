#!/usr/bin/env python
"""Add more German tokens to non-person blacklist."""

# Read the file
with open('PII_filter/pii_filter.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the NON_PERSON_SINGLE_TOKENS set
old_tokens = '''            # Added German tokens to avoid single-token PERSON false positives
            "berg","groß","gross","klein","kalt","weil","neben","außer","ausser",
        }'''

new_tokens = '''            # Added German tokens to avoid single-token PERSON false positives
            "berg","groß","gross","klein","kalt","weil","neben","außer","ausser",
            # German days of week, time periods, directions, and common words
            "montag","dienstag","mittwoch","donnerstag","freitag","samstag","sonntag",
            "januar","februar","märz","april","mai","juni","juli","august","september","oktober","november","dezember",
            "morgen","mittag","abend","nacht","tag","woche","monat","jahr",
            "links","rechts","oben","unten","oben","vorne","hinten","innen","außen",
            "langsam","schnell","groß","klein","alt","jung","neu","gut","schlecht","schön",
            "hier","dort","da","wo","wann","wie","warum","was","welcher","welche","welches",
            "runter","hoch","rauf","runter","entlang","hinter","dienst","doktor",
        }'''

content = content.replace(old_tokens, new_tokens)

# Write back
with open('PII_filter/pii_filter.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Added more German tokens to NON_PERSON_SINGLE_TOKENS')
