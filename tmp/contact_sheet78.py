from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
paths=sorted(Path('tmp').glob('qa78-*.png'), key=lambda p:int(p.stem.split('-')[-1]))
for base in range(0,len(paths),12):
    group=paths[base:base+12]
    thumb_w=260
    thumbs=[]
    for i,path in enumerate(group,base+1):
        im=Image.open(path).convert('RGB')
        h=round(im.height*thumb_w/im.width)
        im=im.resize((thumb_w,h))
        card=Image.new('RGB',(thumb_w+16,h+40),'white')
        card.paste(im,(8,30))
        ImageDraw.Draw(card).text((8,8),f'PDF page {i}',fill='black')
        thumbs.append(card)
    cols=3; rows=(len(thumbs)+cols-1)//cols
    cw=max(x.width for x in thumbs); ch=max(x.height for x in thumbs)
    sheet=Image.new('RGB',(cols*cw,rows*ch),(225,225,225))
    for j,im in enumerate(thumbs): sheet.paste(im,((j%cols)*cw,(j//cols)*ch))
    out=Path(f'tmp/contact78-{base//12+1}.jpg')
    sheet.save(out,quality=88)
    print(out)
