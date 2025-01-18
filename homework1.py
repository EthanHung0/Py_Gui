# Tiêu đề là "Chào mừng đến với guizero!".
# Màu nền là xanh dương nhạt (#add8e6).
# Nội dung: "Hãy học lập trình GUI với guizero!"
# Màu chữ: xanh lá cây.
# Cỡ chữ: 18.
# Sử dụng một file hình ảnh có sẵn, ví dụ: logo.png

from guizero import *
app = App(title="Chào mừng đến với guizero!",bg=(173, 216, 230),layout="auto")
text_ = Text(app, text="Hãy học lập trình GUI với guizero!", color=(1,100,32), size=18)
img = Picture(app, image="img/python.png")

app.display()