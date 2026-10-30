from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\final_report.pdf';r=PdfReader(p)
def v(t,cm,tm,f,size):
 if t.strip():
  y=cm[5]+tm[5]*cm[3]
  if y<230: print(round(y,1),repr(t.strip()),'size',size)
r.pages[12].extract_text(visitor_text=v)
