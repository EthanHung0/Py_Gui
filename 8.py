from PIL import Image,ImageFilter
from guizero import *

aaaaaaaaap = App(title="eight",width=500,height=500)

img = Image.open("img/dog2.png")
if img.mode == "RGBA":
    img.convert("RGB")

box = Box(aaaaaaaaap, align="center",layout="grid")

transposed = img.transpose(Image.FLIP_LEFT_RIGHT)
box1 = Box(box,grid=[0,0],border=2)
img1 = Picture(box1,image=transposed)

box2 = Box(box,grid=[1,0],border=2)
rotated = img.rotate(angle=180,expand=True)
img2 = Picture(box2,image=rotated)

box3 = Box(box,grid=[0,1],border=2,width=187,height=270)
cropped = img.crop((0,0,187,240))
img3 = Picture(box3,image=cropped)

box4 = Box(box,grid=[1,1],border=2)
filtered = img.filter(ImageFilter.BLUR)
img4 = Picture(box4,image=filtered)

print(img.size)
aaaaaaaaap.display()

