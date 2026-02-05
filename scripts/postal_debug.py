import os,sys,re
sys.path.insert(0, os.getcwd())
from pii_filter import PIIFilter
pf=PIIFilter()
text='01001-000 São Paulo'
print('Text:',text)
for i,patt in enumerate(pf.POSTAL_EU_PATTERNS):
    for m in re.finditer(patt,text,flags=re.I|re.UNICODE):
        print('Pattern idx',i,'pattern',patt)
        print('Match:',repr(m.group()),'groups:',m.groups(),'start',m.start(),m.end())
