import pdfplumber
with pdfplumber.open('tmp/final_report.pdf') as pdf:
    print('pages', len(pdf.pages))
    for i, page in enumerate(pdf.pages, 1):
        body = [c for c in page.chars if c.get('text', '').strip() and c['top'] < 790]
        end = max((c['bottom'] for c in body), default=0)
        txt = (page.extract_text() or '').splitlines()
        print(f'{i:02} chars={len(body):4d} body_end={end:5.1f} bottom_blank={842-end:5.1f} title={(txt[0] if txt else "NONE")[:80]}')
