"""
Câu 1: Viết một ứng dụng GUI Xổ số đơn giản. Người dùng nhấn nút “Quay số” để chọn các số ngẫu nhiên. Một tờ vé số có 6 số và các số từ 0-9.
1. Thiết kế bao gồm một Drawing với nền là một ảnh
2. Một Text có nội dung là "Con số may mắn"
3. Một dãy 6 con số được tạo ngẫu nhiên được hiển thị lên Drawing
4. Một PushButton, sau khi nhấn button này sẽ tạo ra một số ngẫu nhiên.
Thiết kế bao gồm Drawing với nền ảnh
Text có nội dung "Con số may mắn
Tạo ra một dãy 6 số ngẫu nhiên từ 0-9
PushButton để tạo ra số ngẫu nhiên
"""

import random
from guizero import *

app = App(title="Lucky Number!",width=500,height=500)
draw_space = Drawing(app,width=500,height=450)
draw_space.image(0,0,"img/lottery.png",width=500,height=450)

def rand_num():
    return random.randint(0,9)
txt = draw_space.text(140,100,text="Lucky Number!",size=25,color="blue")

def pressed():
    draw_space.clear()
    draw_space.image(0,0,"img/lottery.png",width=500,height=450)
    txt = draw_space.text(140,100,text="Lucky Number!",size=25,color="blue")
    txt = draw_space.text(120,180,text=f"{rand_num()} {rand_num()} {rand_num()} {rand_num()} {rand_num()} {rand_num()}",size=40)

button = PushButton(app,pressed)

app.display()