import re
import pdfplumber
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
pdf_path='output/pdf/SmartMail_Assistant_Project_Report.pdf'
doc_path='output/docx/SmartMail_Assistant_Project_Report.docx'
def norm(s): return re.sub(r'[^a-z0-9]+','',s.lower())
doc=Document(doc_path)
parts=[]; posmap=[]
for el in doc.element.body.iterchildren():
    if isinstance(el, CT_P):
        txt=Paragraph(el,doc).text
        if txt.strip(): parts.append(txt); posmap.append(('p',el,txt))
    elif isinstance(el, CT_Tbl):
        tb=Table(el,doc)
        for row in tb.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    if para.text.strip(): parts.append(para.text); posmap.append(('p',para._p,para.text))
joined='\n'.join(parts); njoined=norm(joined)
last=0; ok=0
with pdfplumber.open(pdf_path) as pdf:
    for i,page in enumerate(pdf.pages,1):
        lines=[x.strip() for x in (page.extract_text() or '').splitlines() if x.strip()]
        cand=lines[0] if lines else ''
        target=norm(cand)
        found=njoined.find(target,last) if len(target)>=8 else -1
        if found<0 and len(lines)>1:
            cand=' '.join(lines[:2]); target=norm(cand); found=njoined.find(target,last)
        if found>=0:
            ok+=1; last=found+max(1,len(target)); status='OK'
        else: status='MISS'
        print(f'{i:02} {status} {cand[:100]!r}')
print('matched',ok,'/',len(pdf.pages))
