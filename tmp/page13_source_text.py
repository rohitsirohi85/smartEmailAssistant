from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\base20.pdf';r=PdfReader(p)
print(r.pages[10].extract_text())
