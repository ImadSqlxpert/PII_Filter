#!/usr/bin/env python
"""Debug the chat address merging issue."""

import sys
sys.path.insert(0, r'C:\Users\imadi\Desktop\projects\PII_Filter')

from PII_filter.pii_filter import PIIFilter
import spacy

f = PIIFilter()

chat = 'User: Straße: Hauptstraße\nNr.: 10\nPLZ/Ort: 10115 Berlin'

print("=" * 70)
print("Input text:")
print(repr(chat))
print()
print(chat)
print("=" * 70)

# Test with base spacy model
try:
    doc = f.nlp(chat)
    print("\nSpacy entities detected:")
    for ent in doc.ents:
        print(f"  {ent.label_:12s} [{ent.start_char:3d}-{ent.end_char:3d}]: {repr(ent.text)}")
except Exception as e:
    print(f"Error loading spacy model: {e}")

print("\n" + "=" * 70)
print("PIIFilter entities (before anonymize):")

# Get entities directly
try:
    # Use get_analyzed_entities if available
    if hasattr(f, 'get_analyzed_entities'):
        entities = f.get_analyzed_entities(chat)
    else:
        # Fallback: analyze and get from internal state
        from presidio_analyzer import AnalyzerEngine
        from presidio_analyzer.nlp_engine import NlpEngine
        
        # Create analyzer separately
        analyzer = AnalyzerEngine(nlp_engine=NlpEngine())
        entities = analyzer.analyze(text=chat, language='en')
    
    for ent in entities:
        print(f"  {ent.entity_type:15s} [{ent.start:3d}-{ent.end:3d}] conf={ent.score:.2f}: {repr(chat[ent.start:ent.end])}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 70)
print("Final anonymized output:")
out = f.anonymize_text(chat)
print(repr(out))
print()
print(out)
print("=" * 70)
