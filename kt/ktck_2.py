"""
Câu 2: Hãy tạo một ứng dụng quản lý tệp văn bản đơn giản sử dụng thư viện guizero trong Python. Ứng dụng này sẽ cho phép người dùng chọn và chỉnh sửa các tệp .txt từ một thư mục được chỉ định. Ứng dụng cần có các chức năng sau:

1. Hiển thị danh sách các tệp .txt trong thư mục: Người dùng có thể chọn một tệp để xem nội dung của nó trong một hộp văn bản (TextBox).
2. Chỉnh sửa nội dung tệp: Người dùng có thể chỉnh sửa nội dung của tệp văn bản đã chọn trong TextBox.
3. Lưu nội dung đã chỉnh sửa: Có một nút để lưu nội dung mới của tệp vào tệp .txt.
4. Thay đổi màu chữ: Có một bảng chọn (ComboBox) cho phép người dùng thay đổi màu chữ của TextBox.
5. Thay đổi kiểu chữ: Người dùng có thể chọn kiểu chữ (font) cho TextBox từ danh sách các font như Times, Courier, Arial.
6. Thay đổi cỡ chữ: Có một thanh trượt (Slider) để điều chỉnh kích thước chữ trong TextBox.

+ Hiển thị danh sách các tệp txt trong thư mục lên ListBox.
+ Hiển thị nội dung tệp đang chọn trong ListBox lên TextBox.
+ Chỉnh sửa nội dung tệp trong TextBox và Lưu thành công(có thông báo).
+ Thay đổi màu chữ và kiểu chữ.
+ Thay đổi cỡ chữ.
+ Sử dụng try-except.(bỏ)
"""

from guizero import *

app = App(title="practice",width=800,height=400,layout="grid",bg="#BDDDE4")

dad = Box(app,layout="grid",grid=[2,0])

def select_txt_clr():
    txt.text_color = txtclr_selection.value
txtclr_selection = Combo(dad,options=["#006A71","black"],command=select_txt_clr,selected="#006A71",grid=[0,1])
txtclr_selection.bg = "#F2EFE7"

def select_font():
    txt.font = font_selection.value
font_selection = ButtonGroup(dad,options=["Times New Roman","Arial"],horizontal=True,selected="Arial",command=select_font,grid=[0,2])
font_selection.bg = "#F2EFE7"

def txt_size():
    txt.text_size = size_slider.value
size_slider = Slider(dad,start=10,end=20,horizontal=True,command=txt_size,grid=[0,3])
size_slider.bg = "#F2EFE7"

txtb = Box(app,grid=[1,0],width=300,height=400)
txt = TextBox(
    txtb,
    text="",
    width=40,
    height=25,
    multiline=True,
    scrollbar=True)
txt.bg = "#F2EFE7"

def show():
    with open(file_list.value,"r",encoding="utf-8") as tfile:
        txt.value = tfile.read()

def update():
    with open(file_list.value,"w",encoding="utf-8") as tfile:
        tfile.write(txt.value)
    show()

file_list = ListBox(
    app,
    items=["practice1.txt","practice2.txt","practice3.txt"],
    selected="practice1.txt",
    command=show,
    width=150,
    height=400,
    grid=[0,0])
file_list.bg = "#9ACBD0"

but = PushButton(dad,text="SAVE",command=update,grid=[0,0])
but.bg = "#006A71"
but.text_color = "#F2EFE7"


app.display()