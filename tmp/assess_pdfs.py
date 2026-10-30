from pypdf import PdfReader
from pathlib import Path
for path in [r'C:\Users\ACER\Downloads\PROJECT REPORT FORMAT.pdf',r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report.pdf']:
 r=PdfReader(path); print('\nFILE',Path(path).name,'PAGES',len(r.pages))
 for i,p in enumerate(r.pages):
  t=p.extract_text() or ''
  if i<20 or len(t.strip())<120:
   print(i+1,len(t.strip()),repr(t.strip()[:180].replace('\n',' | ')))
