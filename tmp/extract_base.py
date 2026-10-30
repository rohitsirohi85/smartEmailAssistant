from pypdf import PdfReader, PdfWriter
src=r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report.pdf'
out=r'E:\email-writer-sb\tmp\base20.pdf'
r=PdfReader(src); w=PdfWriter()
for p in r.pages[:20]: w.add_page(p)
with open(out,'wb') as f: w.write(f)
print('extracted',len(w.pages))
