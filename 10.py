"""These functions pop up a box on the screen that displays a message or asks a question. The functions available are:

- warn(title, text) - popup box with a warning icon
- info(title, text) - popup box with an information icon
- error(title, text) - popup box with an error icon
- yesno(title, text) - popup box with yes and no options. Pressing Yes returns True and pressing No returns False.
- question(title, text, initial_value=None) - popup box with a question box which can accept a text response. Pressing Ok returns value entered into the box
is returned and pressing Cancel returns None.
- select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False, filename="") - popup file dialog box which asks the user to
select a file. By default, an Open button is displayed, setting save to True will change the button to Save as. The path of the selected file is returned by
the function. A filename parameter can be supplied which will auto populate the file name field.
- select_folder(title="Select folder", folder=".") - popup box which asks the user to select a folder. The path of the selected folder is
- returned by the function.
- select_color(color=None) - popup box which prompts the user to select a color. Set color to an #rrggbb to select a default color when the popup opens.
- Pressing Ok returns the select color as a #rrggbb value, pressing Cancel returns None.
- All pop up boxes use the native display, so they will look different depending on your operating system."""

from guizero import *
from random import *
# app = App(title="greetings",width=500,height=500)

# def reply():
#     name = app.question("Name","Whats your name?")
#     if name != None:
#         greet.value = f"Hello {name}"

# hi = PushButton(app,command=reply,text="Hello")
# greet = Text(app)
# app.display()


RandNum = App(title="RandomNumber",width=500,height=500)

prev = None
def randn():
    global prev
    randnum = randint(1,10)
    while prev == randnum:
        randnum = randint(1,10)
    prev = randnum
    num.value = f"Number: {randnum}"

Text(RandNum,text="Hi.")
randbutton = PushButton(RandNum,command=randn,text="Random Number")
num = Text(RandNum)
RandNum.display()