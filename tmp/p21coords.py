from pypdf import PdfReader
r=PdfReader(r'E:\email-writer-sb\tmp\final_report.pdf')
def v(t,cm,tm,f,size):
 if t.strip():
  y=cm[5]+tm[5]*cm[3]
  if y<300:print(round(y,1),repr(t.strip()))
r.pages[20].extract_text(visitor_text=v)
