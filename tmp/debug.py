from pathlib import Path
s=Path(r'E:\email-writer-sb\tmp\appendices.py').read_text()
print(repr(s[s.index('("J",'):s.index('for prefix, heading')]))
