from PIL import Image, ImageDraw
from pathlib import Path
d=Path(r'E:\email-writer-sb\tmp')
files=[d/f'long-report-page-{i:02d}.png' for i in range(21,71)]
print('missing', [str(x) for x in files if not x.exists()])
for batch in range(5):
    thumbs=[]
    for p in files[batch*10:(batch+1)*10]:
        im=Image.open(p).convert('RGB')
        im.thumbnail((330,440))
        canvas=Image.new('RGB',(350,475),'white')
        canvas.paste(im,((350-im.width)//2,25))
        ImageDraw.Draw(canvas).text((8,5),p.stem,fill='black')
        thumbs.append(canvas)
    sheet=Image.new('RGB',(1750,950),(210,210,210))
    for j,im in enumerate(thumbs): sheet.paste(im,((j%5)*350,(j//5)*475))
    out=d/f'appendix-contact-{batch+1}.jpg'
    sheet.save(out,quality=85)
    print(out)
