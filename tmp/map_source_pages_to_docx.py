import re
import pdfplumber
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P

pdf_path = 'output/pdf/SmartMail_Assistant_Project_Report.pdf'
doc_path = 'output/docx/SmartMail_Assistant_Project_Report.docx'

def norm(text):
    text = re.sub(r'\(cid:\s*127\)', ' ', text, flags=re.I)
    return re.sub(r'[^a-z0-9]+', '', text.lower())

doc = Document(doc_path)
blocks = []
for el in doc.element.body.iterchildren():
    if isinstance(el, CT_P):
        p = Paragraph(el, doc)
        if p.text.strip() or el.xpath('.//w:drawing') or el.xpath('.//w:pict'):
            blocks.append((el, p.text, 'P'))
    elif isinstance(el, CT_Tbl):
        table = Table(el, doc)
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    if p.text.strip(): blocks.append((p._p, p.text, 'CELL'))

block_norms = [norm(text) for _, text, _ in blocks]
cursor = 0
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, 1):
        lines = [line.strip() for line in (page.extract_text() or '').splitlines() if line.strip()]
        if not lines:
            print(f'{page_num:02} MISS empty page')
            continue
        found_i = None
        matched = ''
        # Prefer paragraph starts. This avoids matching a short heading embedded
        # in an earlier paragraph (for example, "Chapter 2" in a summary).
        line = re.sub(r'\(cid:\s*127\)', ' ', lines[0], flags=re.I)
        for length in (120, 85, 60, 40, 25, 16, 8):
            target = norm(line[:length])
            if len(target) < 8: continue
            for i in range(cursor, len(blocks)):
                if block_norms[i].startswith(target):
                    found_i = i
                    matched = line[:length]
                    break
            if found_i is not None: break
        # Some headings share a line with text or have a university label before
        # them. Allow a longer exact substring only when no paragraph-start hit exists.
        if found_i is None:
            for length in (120, 85, 60, 40, 25, 16):
                target = norm(line[:length])
                if len(target) < 12: continue
                for i in range(cursor, len(blocks)):
                    if target in block_norms[i]:
                        found_i = i
                        matched = line[:length]
                        break
                if found_i is not None: break
        if page_num == 12:
            # This source page starts with the request/response sequence figure.
            found_i = next((i for i, (el, _, _) in enumerate(blocks) if el.xpath('.//w:drawing') and i >= cursor and i > 0), None)
            # The first figure after page 11 is the architecture overview; page 12
            # begins with the second figure, the request/response sequence.
            drawings = [i for i, (el, _, _) in enumerate(blocks) if el.xpath('.//w:drawing') and i >= cursor]
            if len(drawings) >= 2: found_i = drawings[1]
            matched = '[sequence diagram drawing]'
        if found_i is None:
            print(f'{page_num:02} MISS {lines[0][:100]!r}')
        else:
            el, txt, kind = blocks[found_i]
            print(f'{page_num:02} {found_i:04} {kind} {matched[:70]!r} => {txt[:75]!r}')
            cursor = found_i
