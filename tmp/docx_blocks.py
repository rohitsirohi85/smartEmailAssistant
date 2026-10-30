from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
D=Document('output/docx/SmartMail_Assistant_Project_Report.docx')
for i,e in enumerate(D.element.body.iterchildren()):
 if isinstance(e,CT_P): t=Paragraph(e,D).text
 elif isinstance(e,CT_Tbl): t=' | '.join(c.text for row in Table(e,D).rows for c in row.cells)
 else: t=''
 if i<180 and t.strip(): print(i,repr(t[:220]))
