from guizero import *

MainApp = App(title="ResManagement", width=1000,height=500, bg="#01bfff")

Procedure = Box(MainApp,layout="grid",width="fill",height="fill")

Menu = Box(Procedure,layout="grid",width=350,height="500",grid=[0,0])
Menu.tk.configure(background="#F5F5F5")
menu_txt_box = Box(Menu, width=350, height=50, grid=[0, 0],border=2)
menu_text = Text(menu_txt_box, text="MENU", size=25, color=(255,255,255),font="arial",bold=3)



MainApp.display()