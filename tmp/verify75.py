from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\final_report.pdf';r=PdfReader(p);print('pages',len(r.pages))
for i,pg in enumerate(r.pages):
 t=pg.extract_text() or ''
 if len(t.strip())<350: print('SHORT',i+1,len(t.strip()),repr(t.strip()[:200]))
print('blank screenshot marker count',sum('SCREENSHOT TO BE INSERTED HERE' in (pg.extract_text() or '') for pg in r.pages))
for i in (24,25): print('screen',i+1,'images',len(r.pages[i].images),'text',repr((r.pages[i].extract_text() or '')[:250]))
print('last page',repr((r.pages[-1].extract_text() or '')[-400:]))
