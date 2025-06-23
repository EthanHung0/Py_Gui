from guizero import *
from PIL import Image

app = App(title="Write on Pic.",width=1000,height=1000) #App creation.
#=================================================================================

#Upper Box for applying Texts, Text colors and Fonts into the picture.
upper = Box(
    app,
    layout="grid",
    border=1
)
upper.bg = "#E6F2FF"

txt = Text( #Inputting Text into picture with TextBox.
    upper,
    text="Add text: ",
    grid=[0,0]
)
txt_tbox = TextBox(upper, width=25, grid=[1,0])
txt_tbox.bg = "white"

clr_txt = Text(upper, text="Select Color: ", grid=[0,1])
clr = Combo( #Text's Coilor selection with Combo.
    upper,
    options=["Black","White","Red","Blue","Green","Yellow","Purple","Pink"],
    selected="Black",
    grid=[1,1]
)
clr.bg = "white"

font_txt = Text(upper,text="Select Font: ",grid=[0,2])
font = ButtonGroup( #Text's Font setting using ButtonGroup to choose between Times New Roman and Arial.
    upper,
    options=["Times New Roman","Arial"],
    horizontal=True,
    selected="Arial",
    grid=[1,2]
)

#----------------------------------------------------------------------
def Applytxt():
    draw_space.clear()
    draw_space.text( #Apply function for The final PushButton. (apply all the settings above into the picture.)
        0,0,
        text=txt_tbox.value,
        color=clr.value,
        font=font.value)
applytxt = PushButton( #The final PushButton.
    upper,
    text="Apply Text",
    command=Applytxt,
    grid=[0,3]
)
applytxt.bg = "white"

#===========================================================================================================================================
lower = Box(app,layout="grid") #Lower Box for picture selection and emoji drawing.

def Pic_Selection():
    img = Image.open(pic_list.value)
    if img.mode == "RGBA":
        img.convert("RGB")
    img.resize(size=(500,500),resample=Image.Resampling.LANCZOS)
    Picture( #Picture selection.
        lower,
        image=img,
        width=500,
        height=500,
        grid=[1,0]
    )
pic_list = ListBox( #Available pictures list.
    lower,
    items=["img/cat1.png","img/cat2.png","img/cat3.png"],
    grid=[0,0],
    command=Pic_Selection
)
pic_list.bg = "#E6F2FF"

draw_space = Drawing( #Drawing space to apply
    lower,
    width=500,
    height=500,
    grid=[1,0]
)
draw_space.bg = "black"

#----------------------------------------------------------------------

lower_right = Box(lower,layout="grid",grid=[2,0]) #Box for lower right usage.

x_ratio = (draw_space.width+50)/100
y_ratio = (draw_space.height+50)/100
def Apply_Emoji():
    draw_space.clear()
    draw_space.image((X.value*x_ratio),(Y.value*y_ratio),image=f"img/{emoji_diction[em.value]}",width=50,height=50)

X_txt = Text(lower_right, text="X", grid=[0,0,3,1])
X = Slider(lower_right, start=0, end=100, horizontal=True, grid=[0,1,3,1], command=Apply_Emoji,width=300)

Y_txt = Text(lower_right, text="Y", grid=[3,2,1,3])
Y = Slider(lower_right, start=0, end=100, horizontal=False, grid=[2,2,1,3], command=Apply_Emoji,height=250)

em_box = Box
em_txt = Text(lower_right,text="Add emoji: ",grid=[0,2])
emoji_diction = {"❤️":"heart.png","⭐":"star.png","🎉":"confetti.png"}
em = Combo(
    lower_right,
    options=["❤️","⭐","🎉"],
    grid=[0,3]
)

applyemo = PushButton(lower_right, command=Apply_Emoji, text="Apply Emoji", grid=[0,4,2,1])

###############
app.display()