from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
D=Document('output/docx/SmartMail_Assistant_Project_Report.docx')
for i,e in enumerate(D.element.body.iterchildren()):
 if 90<=i<=150:
  if isinstance(e,CT_P):
   p=Paragraph(e,D); text=p.text[:120]; print(i,'P',repr(text),'drawing',bool(e.xpath('.//w:drawing')),'pict',bool(e.xpath('.//w:pict')),'textbox',bool(e.xpath('.//w:txbxContent')),'break',len(e.xpath('.//w:br')))
  elif isinstance(e,CT_Tbl):
   t=' | '.join(c.text for row in Table(e,D).rows for c in row.cells); print(i,'T',repr(t[:220]))
  else: print(i,type(e))
