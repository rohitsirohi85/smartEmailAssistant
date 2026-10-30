from PIL import Image,ImageDraw
from pathlib import Path
d=Path(r'E:\email-writer-sb\tmp')
files=sorted(d.glob('qa-page-*.png'))
for batch in range(7):
    items=files[batch*10:(batch+1)*10]; sheet=Image.new('RGB',(1500,840),(205,205,205))
    for j,p in enumerate(items):
        im=Image.open(p).convert('RGB'); im.thumbnail((285,380)); x=(j%5)*300+(300-im.width)//2; y=(j//5)*420+25
        sheet.paste(im,(x,y)); ImageDraw.Draw(sheet).text(((j%5)*300+8,(j//5)*420+5),p.stem,fill='black')
    out=d/f'final-contact-{batch+1}.jpg'; sheet.save(out,quality=90)
    print(out)
