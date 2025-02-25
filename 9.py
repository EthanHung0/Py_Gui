from guizero import *
# game = App(title="Simple Clicker Game",width=400,height=300)
# count = 0
# def pushed():
#     global count
#     count += 1
#     score.value = f"Score: {count}"
# score = Text(game,text="Score: 0")
# Button = PushButton(game,command=pushed,image="img/10-2-birthday-cake-png-clipart-thumb.png")
# game.display()

app = App(title="Button*3",width=500,height=500,bg="#FFDE21")
dad = Box(app , align="center" , layout="grid")

def pressed(color):
    app.bg = color
    # print(f"{color} button pressed.")

b1 = PushButton(dad,text="red",grid=[0,0],command=pressed,args=["red"])
# b1.bg = "red"

b2 = PushButton(dad,text="blue",grid=[1,0],command=pressed,args=["blue"])
# b2.bg = "blue"

b3 = PushButton(dad,text="black",grid=[2,0],command=pressed,args=["black"])
# b3.bg = "black"

app.display()
