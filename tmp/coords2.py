from pypdf import PdfReader
r=PdfReader(r'E:\email-writer-sb\tmp\base20.pdf')
def v(t,cm,tm,f,size):
 if t.strip(): print(repr(t.strip()),'cm',cm,'tm',tm,'size',size)
r.pages[2].extract_text(visitor_text=v)
