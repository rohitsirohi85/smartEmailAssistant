from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\final_report.pdf';r=PdfReader(p)
alltext='\n'.join((pg.extract_text() or '') for pg in r.pages)
print('pages',len(r.pages))
print('old project text',[(x,x in alltext) for x in ('MYSTIGEM','Ishika Sharma','Anshul Bharti')])
for term in ('SCREENSHOT TO BE INSERTED HERE','C.3 Screenshot placeholder','C.4 Screenshot placeholder','C.5 Screenshot placeholder'):
 print('placeholder',term,alltext.count(term))
print('short pages',[(i+1,len((pg.extract_text() or '').strip())) for i,pg in enumerate(r.pages) if len((pg.extract_text() or '').strip())<350])
for i in (31,32): print('physical',i+1,'footer',repr((r.pages[i].extract_text() or '').splitlines()[0]),'images',len(r.pages[i].images))
