from guizero import App, PushButton

app_ = App(title="hello", width=400, height=250, layout="grid", bg=(0, 0, 0))

def press_check():
    print("Pressed.")

button = PushButton(app_, text="Calm.", command=press_check,grid=[1,1])
button.bg = (255, 255, 255)
button.text_color = (0, 0, 0)
button.text_bold = True
app_.tk.grid_rowconfigure(1,weight = 1)
app_.tk.grid_columnconfigure(1,weight = 1)

app_.display()
