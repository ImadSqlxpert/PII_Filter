import sys
sys.path.insert(0,'.')
from pii_filter.pii_filter import PIIFilter
f=PIIFilter()
print('ACCT_LABEL_RX pattern:', f.ACCT_LABEL_RX.pattern)
print('LABELED_BANK_RX pattern:', f.LABELED_BANK_RX.pattern)
PY