from guizero import *

app = App(title="info text color",width=1000,height=500)
dadbox = Box(app,layout="grid")
img = Picture(dadbox,image="img/1.png",width=100,height=100,grid=[0,0])

txtbox = Box(dadbox,layout="grid",grid=[1,0])
name = Text(txtbox,text="Name: ",grid=[0,0])
nametextbox = TextBox(txtbox,grid=[1,0])
nickname = Text(txtbox,text="Nickname: ",grid=[0,1])
nicknametextbox = TextBox(txtbox,grid=[1,1])
number = Text(txtbox,text="Number: ",grid=[0,2])
numbertextbox = TextBox(txtbox,grid=[1,2])
address = Text(txtbox,text="Address: ",grid=[0,3])
addresstextbox = TextBox(txtbox,grid=[1,3])

def color_change():
    nametextbox.text_color = colorlist.value
    nicknametextbox.text_color = colorlist.value
    numbertextbox.text_color = colorlist.value
    addresstextbox.text_color = colorlist.value
colorlist = ListBox(dadbox, items=["red","blue","green","black"],command=color_change,grid=[2,0])



app.display()