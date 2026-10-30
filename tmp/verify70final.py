from pypdf import PdfReader
p=r'E:\email-writer-sb\output\pdf\SmartMail_Assistant_Project_Report.pdf';r=PdfReader(p)
print('page_count',len(r.pages))
print('page13_footer',repr((r.pages[20].extract_text() or '').splitlines()[0]))
print('page13_has_roadmap','5.3 Prioritized implementation roadmap' in (r.pages[20].extract_text() or ''))
text='\n'.join(pg.extract_text() or '' for pg in r.pages)
print('screenshot_placeholders',text.count('SCREENSHOT TO BE INSERTED HERE'))
print('embedded_app_screens',[(i+1,len(pg.images)) for i,pg in enumerate(r.pages) if len(pg.images)>0])
print('last_page',repr((r.pages[-1].extract_text() or '').splitlines()[0]))
