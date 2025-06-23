from guizero import *
app = App(title="Schedule",width=500,height=500,bg=(255,0,0))

dad = Box(app,layout="grid")
Text(dad,"Tasks: ",grid=[0,0])
task = TextBox(dad,grid=[1,0])
task.bg = "#D3D3D3"

def save():
    with open("tasks.txt",mode="w",encoding="utf-8") as a:
        for i in Tlist.items:
            a.write(f"{i.strip()}\n")
def add_schedule():
    if not task.value:
        app.warn("ERROR!","Empty input!")
    else:
        Tlist.append(task.value)
        task.value = ""
        save()
def remove_schedule():
    if not Tlist.value:
        app.warn("ERROR!","Schedule is empty!")
    else:
        Tlist.remove(Tlist.value)
        save()

add = PushButton(dad,grid=[2,0],command=add_schedule,text="ADD")
add.bg = "#D3D3D3"
remov = PushButton(dad,command=remove_schedule,grid=[2,1],text="REMOVE")
remov.bg = "#D3D3D3"
Tlist = ListBox(app,width=1000,height=1000)
Tlist.bg = "#D3D3D3"

app.display()