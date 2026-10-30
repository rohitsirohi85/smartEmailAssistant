from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\final_report.pdf';r=PdfReader(p);print('pages',len(r.pages))
for i in [2,4,20,24,25,28,29,30,33,34,39,42,43,48,49,54,55,60,61,69]:
 print('---',i+1,'---',(r.pages[i].extract_text() or '')[:260].replace('\n',' | '))
