from pypdf import PdfReader
p=r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report.pdf';r=PdfReader(p)
print('pages',len(r.pages))
text='\n'.join(pg.extract_text() or '' for pg in r.pages)
print('screenshot placeholders',text.count('SCREENSHOT TO BE INSERTED HERE'))
print('old template project remnants',any(x in text for x in ('MYSTIGEM','Ishika Sharma','Anshul Bharti')))
for i in (31,32): print('screen page',i+1,'logical',repr((r.pages[i].extract_text() or '').splitlines()[0]),'images',len(r.pages[i].images))
print('last logical page',repr((r.pages[-1].extract_text() or '').splitlines()[0]))
