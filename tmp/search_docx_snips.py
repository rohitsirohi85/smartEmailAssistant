from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
D=Document('output/docx/SmartMail_Assistant_Project_Report.docx')
i=0
for el in D.element.body.iterchildren():
    if isinstance(el,CT_P):
        t=Paragraph(el,D).text
        if any(s in t.lower() for s in ['construct a model prompt','return the reply text','persistent account or history','user client','submit email and tone']):print('P',i,repr(t))
    elif isinstance(el,CT_Tbl):
        T=Table(el,D)
        tx=' | '.join(c.text for r in T.rows for c in r.cells)
        if any(s in tx.lower() for s in ['construct a model prompt','return the reply text','persistent account or history','user client','submit email and tone']):print('T',i,repr(tx[:600]))
    i+=1
