from pathlib import Path
p=Path(r'E:\email-writer-sb\tmp\appendices.py');s=p.read_text()
needle='\n])\nfor prefix, heading, records in extra_sections:'
print('needle?',needle in s)
s=s.replace(needle,'\n])]\nfor prefix, heading, records in extra_sections:')
p.write_text(s)
