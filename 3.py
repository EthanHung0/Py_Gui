from guizero import *
app = App(title="Hộp quà ma thuật",width=500,height=500,layout="auto",bg=(137,207,240))
text1 = Text(app,text="Chào mừng đến với Hộp Quà Ma Thuật!",color="purple")
picture = Picture(app,image="bunnyincarrot.gif",)
text2 = Text(app,text="Khám phá những điều kì diệu bên trong!",color="green",size=10)

app.display()