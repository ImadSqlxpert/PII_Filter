import traceback
import os
import sys
# Ensure project root is on sys.path for local imports
sys.path.insert(0, os.getcwd())
try:
    import importlib
    m = importlib.import_module('pii_filter.pii_filter')
    print('Imported module:', m)
    print('Has PIIFilter:', hasattr(m, 'PIIFilter'))
    print('Has anonymize_text:', hasattr(m, 'anonymize_text'))
except Exception:
    traceback.print_exc()
