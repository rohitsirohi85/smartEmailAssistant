from PIL import Image,ImageDraw
from pathlib import Path
import re
d=Path(r'E:\email-writer-sb\tmp')
files=[p for p in d.glob('qa75-*.png') if re.fullmatch(r'qa75-\d{2}\.png',p.name)]
files.sort(key=lambda p:int(p.stem.split('-')[1]));print('renders',len(files))
for batch in range(8):
 items=files[batch*10:(batch+1)*10];sheet=Image.new('RGB',(1200,720),(210,210,210))
 for j,p in enumerate(items):
  im=Image.open(p).convert('RGB');im.thumbnail((225,310));x=(j%5)*240+(240-im.width)//2;y=(j//5)*360+25
  sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text(((j%5)*240+6,(j//5)*360+5),p.stem,fill='black')
 out=d/f'qa75-contact-{batch+1}.jpg';sheet.save(out,quality=88);print(out)
