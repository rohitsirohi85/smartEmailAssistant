from pypdf import PdfReader
p=r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report_70_Pages.pdf'
r=PdfReader(p)
print('pages',len(r.pages))
for i in range(38,43): print(i+1,repr(r.pages[i].extract_text()[:600]))
