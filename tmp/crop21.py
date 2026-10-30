from PIL import Image
p=r'E:\email-writer-sb\tmp\page13fix-21.png'; im=Image.open(p)
im.crop((0,0,1241,600)).save(r'E:\email-writer-sb\tmp\p21top.png')
im.crop((0,1000,1241,1754)).save(r'E:\email-writer-sb\tmp\p21bottom.png')
