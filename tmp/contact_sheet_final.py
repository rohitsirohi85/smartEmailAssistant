from PIL import Image, ImageDraw
from pathlib import Path
paths=sorted(Path('tmp').glob('qa78final-*.png'), key=lambda p:int(p.stem.split('-')[-1]))
for base in range(0,len(paths),12):
    group=paths[base:base+12]; tw=260; cards=[]
    for i,path in enumerate(group,base+1):
        im=Image.open(path).convert('RGB'); h=round(im.height*tw/im.width); im=im.resize((tw,h))
        card=Image.new('RGB',(tw+16,h+40),'white'); card.paste(im,(8,30)); ImageDraw.Draw(card).text((8,8),f'PDF page {i}',fill='black'); cards.append(card)
    cols=3; rows=(len(cards)+cols-1)//cols; cw=max(x.width for x in cards); ch=max(x.height for x in cards)
    sheet=Image.new('RGB',(cols*cw,rows*ch),(225,225,225))
    for j,im in enumerate(cards): sheet.paste(im,((j%cols)*cw,(j//cols)*ch))
    out=Path(f'tmp/contact78-final-{base//12+1}.jpg'); sheet.save(out,quality=88); print(out)
