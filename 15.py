from guizero import *
import os

app = App(title="File Management",layout="grid")
dad = Box(app,layout="grid",grid=[1,0])

folder_n = "15th"

def load_list():
    Tlist.clear()
    files = os.listdir(folder_n)
    for f in files:
        Tlist.append(f)

def ADD():
    if not txt.value:
        app.warn("ERROR!","Empty input!")
    else:
        file_n = txt.value
        if file_n:
            if not os.path.exists(folder_n):
                os.mkdir(folder_n)
            new_file = os.path.join(folder_n,file_n)
            newfile_exists = os.path.exists(new_file)
            if not newfile_exists:
                open(new_file, "w", encoding= "utf-8").close()
                Tlist.append(file_n)
            txt.value = ""

def REMV():
    file_path = os.path.join(folder_n,Tlist.value)
    exists = os.path.exists(file_path)
    if not exists:
        app.warn("ERROR!","Folder is empty!")
    else:
        os.remove(file_path)
        Tlist.remove(Tlist.value)

def RENAME():
    new_name = txt.value
    selected = Tlist.value
    if not (selected and new_name):
        warn("ERROR!","Select file to rename!")
    else:
        new_file_n = os.path.join(folder_n,new_name)
        old_file_n = os.path.join(folder_n,selected)
        os.rename(old_file_n,new_file_n)
        load_list()

txt = TextBox(dad,width=25,grid=[0,0,3,1])
add = PushButton(dad,grid=[0,1],text="ADD",command=ADD)
remv = PushButton(dad,grid=[1,1],text="REMV",command=REMV)
rename = PushButton(dad,grid=[2,1],text="RENAME",command=RENAME)

Tlist = ListBox(app,width=200,height=100, grid=[0,0])

load_list()
app.display()

