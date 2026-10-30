from pypdf import PdfReader
p=r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report.pdf';r=PdfReader(p)
print('pages',len(r.pages))
for i in (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19):
 print(f'---PDF PAGE {i+1} ---')
 print((r.pages[i].extract_text() or '')[:1600])
