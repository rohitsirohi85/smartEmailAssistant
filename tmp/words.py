import pdfplumber
p=r'E:\email-writer-sb\tmp\base20.pdf'
with pdfplumber.open(p) as pdf:
 page=pdf.pages[2]
 for w in page.extract_words():
  if 100< w['top'] < 180: print(w['text'],round(w['top'],1),round(w['x0'],1))
