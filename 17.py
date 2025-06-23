from guizero import *
import os

# with open("practice.txt","w",encoding="utf-8") as file:
#     file.write("nhangay")

# with open("practice","r",encoding="utf-8") as file:
#     print(file.read())

app = App(title="practice",width=500,height=500,layout="grid")
# with open("practice","r",encoding="utf-8") as file:
#     Text(app,text=file.read())

txt = TextBox(
    app,
    text="",
    width=50,
    height=5,
    multiline=True,
    scrollbar=True,
    grid=[0,0])

def show():
    with open(file_list.value,"r",encoding="utf-8") as tfile:
        txt.value = tfile.read()

def update():
    with open(file_list.value,"w",encoding="utf-8") as tfile:
        tfile.write(txt.value)
    show()

file_list = ListBox(
    app,
    items=["practice1.txt","practice2.txt","practice3.txt"],
    selected="practice1.txt",
    command=show,
    grid=[2,0])

but = PushButton(app,command=update,grid=[1,0])

app.display()