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
anchors = []
misses = []
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, 1):
        lines = [line.strip() for line in (page.extract_text() or '').splitlines() if line.strip()]
        if not lines:
            misses.append((page_num, 'empty source page'))
            continue
        found_i = None
        line = re.sub(r'\(cid:\s*127\)', ' ', lines[0], flags=re.I)
        # Match the actual start of a paragraph before allowing a contained phrase.
        for length in (120, 85, 60, 40, 25, 16, 8):
            target = norm(line[:length])
            if len(target) < 8: continue
            for i in range(cursor, len(blocks)):
                if block_norms[i].startswith(target):
                    found_i = i
                    break
            if found_i is not None: break
        if found_i is None:
            for length in (120, 85, 60, 40, 25, 16):
                target = norm(line[:length])
                if len(target) < 12: continue
                for i in range(cursor, len(blocks)):
                    if target in block_norms[i]:
                        found_i = i
                        break
                if found_i is not None: break
        if page_num == 12:
            # The source page begins with the request/response sequence figure;
            # it is the second drawing that follows the Chapter 2 heading.
            drawing_indices = [i for i, (el, _, _) in enumerate(blocks)
                               if i >= cursor and (el.xpath('.//w:drawing') or el.xpath('.//w:pict'))]
            if len(drawing_indices) >= 2:
                found_i = drawing_indices[1]
        if found_i is None:
            misses.append((page_num, lines[0][:100]))
            continue
        anchors.append((page_num, blocks[found_i][0], blocks[found_i][1]))
        cursor = found_i

if misses:
    raise RuntimeError(f'Could not map source page starts: {misses}')

used = set()
for page_num, element, text in anchors:
    if page_num == 1:
        continue
    key = element
    if key in used:
        raise RuntimeError(f'Pages mapped to the same paragraph near page {page_num}: {text[:80]}')
    used.add(key)
    p = Paragraph(element, doc)
    p.paragraph_format.page_break_before = True

doc.save(doc_path)
print(f'Inserted {len(used)} page-start breaks across {len(anchors)} source pages.')
print('Page 12 anchor:', next(text[:100] for page, _, text in anchors if page == 12) or '[drawing]')
