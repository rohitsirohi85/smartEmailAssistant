from pypdf import PdfReader
p=r'E:\email-writer-sb\tmp\base20.pdf'; r=PdfReader(p)
def visitor(text,cm,tm,font,size):
 if text.strip(): print(repr(text.strip()),'y=',round(tm[5],1),'x=',round(tm[4],1))
r.pages[4].extract_text(visitor_text=visitor)
