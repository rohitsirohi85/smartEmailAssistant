from pathlib import Path
p=Path(r'E:\email-writer-sb\tmp\appendices.py');s=p.read_text(encoding='utf-8')
s=s.replace('for title,intro,caption,image_path in screens:', 'for title,intro,caption,image_path in screens[:2]:')
s=s.replace('complete academic details on the bonafide certificate, add actual screenshots where the reserved boxes appear, and attach the approved similarity report. Confirm that the report\'s author and project title are correct and that any screenshots use fictional or sanitized data.', 'complete academic details on the bonafide certificate and attach the approved similarity report. Confirm that the report\'s author and project title are correct and that the two screenshots match the described workflow states.')
s=s.replace('"Replace screenshot placeholders with current app captures and captions."', '"Keep the supplied app and Gmail screenshots tied to the described workflow states."')
s=s.replace('The remaining three figure areas are reserved for later captures; no live Gemini result is claimed.', 'Neither image demonstrates a live Gemini generation or verified draft insertion.')
p.write_text(s,encoding='utf-8')
