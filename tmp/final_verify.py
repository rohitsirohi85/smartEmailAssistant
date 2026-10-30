from pypdf import PdfReader
p=r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report.pdf'
r=PdfReader(p)
print('pages',len(r.pages))
print('bytes',__import__('os').path.getsize(p))
for i in (29,30,31,32,33):
 pg=r.pages[i]
 print('page',i+1,'footer', (pg.extract_text() or '').splitlines()[0], 'images',len(pg.images),'text', (pg.extract_text() or '').splitlines()[1:3])
print('last', (r.pages[-1].extract_text() or '')[-230:])
