from PIL import Image
from pathlib import Path
for pg in (41,43):
 p=Path(fr'E:\email-writer-sb\tmp\long-report-page-{pg:02d}.png')
 im=Image.open(p)
 im.crop((90,55,700,135)).resize((1220,160)).save(p.with_name(f'page{pg}-heading.png'))
