from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\final_report.pdf';r=PdfReader(p);print('pages',len(r.pages))
for i in (3,20,21,22,69):
 print('---',i+1,'---',repr((r.pages[i].extract_text() or '')[:800]))
text='\n'.join(pg.extract_text() or '' for pg in r.pages)
print('blank boxes',text.count('SCREENSHOT TO BE INSERTED HERE'))
print('old samples',any(x in text for x in ('MYSTIGEM','Ishika Sharma','Anshul Bharti')))
print('screenshot pages',[(i+1,len(pg.images)) for i,pg in enumerate(r.pages) if pg.images])
