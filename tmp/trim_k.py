from pathlib import Path
p=Path(r'E:\email-writer-sb\tmp\appendices.py');s=p.read_text(encoding='utf-8')
a=s.index('add_k_page("K.4 WEB CLIENT')
b=s.index('class NumberedDoc',a)
s=s[:a]+s[b:]
s=s.replace('assert len(add_reader.pages)==53, len(add_reader.pages)','assert len(add_reader.pages)==48, len(add_reader.pages)')
s=s.replace('(\"APPENDICES\",\"15-67\",0,True)', '(\"APPENDICES\",\"15-62\",0,True)')
s=s.replace('(\"K. Implementation reference and release evidence\",\"62-67\",1,False)', '(\"K. Implementation reference and release evidence\",\"62\",1,False)')
needle='("5.2.5 Complete deployment and accessibility work","13",2,False),\n("REFERENCES","14",0,True),'
rep='("5.2.5 Complete deployment and accessibility work","13",2,False),\n("5.3 Prioritized implementation roadmap","13",1,False),\n("REFERENCES","14",0,True),'
if needle not in s: raise SystemExit('TOC anchor missing')
s=s.replace(needle,rep)
s=s.replace('# Merge the 53-page appendix after rebuilding the front matter to match the supplied 75-page format.','# Merge the compact appendix after rebuilding front matter to follow the supplied format.')
# Correct expected count in summary is derived dynamically, no hard-coded 75 text remains.
p.write_text(s,encoding='utf-8')
print('trimmed K to its API reference and updated TOC ranges')
