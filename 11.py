from guizero import *
from random import *

# def numgenerator():

# def Check(button,grid=list):

spydetectapp = App(title="BluSpyDetect",width=1000,height=1000,bg=(0,0,0))
Text(spydetectapp,text="DETECT THE BLU SPY!",color="#B8383B",size=20)
dad = Box(spydetectapp,layout="grid")

Scout = PushButton(dad,grid=[0,0],image="img/scout.png",width=200,height=200)
Soldier = PushButton(dad,grid=[1,0],image="img/soldier.png",width=200,height=200)
Pyro = PushButton(dad,grid=[2,0],image="img/pyro.png",width=200,height=200)
Demoman = PushButton(dad,grid=[0,1],image="img/demom.png",width=200,height=200)
Heavy = PushButton(dad,grid=[1,1],image="img/heavy.png",width=200,height=200)
Engineer = PushButton(dad,grid=[2,1],image="img/engineer.png",width=200,height=200)
Medic = PushButton(dad,grid=[0,2],image="img/medic.png",width=200,height=200)
Sniper = PushButton(dad,grid=[1,2],image="img/sniper.png",width=200,height=200)
Spy = PushButton(dad,grid=[2,2],image="img/spy.png",width=200,height=200)

BLU_SPY = Picture(spydetectapp,)


spydetectapp.display()

