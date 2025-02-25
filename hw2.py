from guizero import *

#HPPYBRTHDAY
# app = App(title="Happy Birthday!")
# Text(app,text="Chúc mừng sinh nhật!")
# pic_box = Box(app,width=200,height=200)
# Picture(pic_box,image="img/10-2-birthday-cake-png-clipart-thumb.png")
# Text(app,text="Chúc bạn có một ngày sinh nhật thật tuyệt vời!")
# Text(app,text="From: huỳnh ngọc béo")

# app.display()
#---------------------------------------------------------------------------

app = App(title="Gallery")
Main_box = Box(app,layout="grid")

box1 = Box(Main_box,grid=[0,0],border=1)
Picture(box1,image="img/cat1.png",width=200,height=150)

box2 = Box(Main_box,grid=[1,0])
Picture(box2,image="img/cat2.png",width=200,height=150)

box3 = Box(Main_box,grid=[0,1,2,1])
Picture(box3,image="img/voi1.png",width=400,height=150)

app.display()

