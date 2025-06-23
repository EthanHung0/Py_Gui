from guizero import *
from PIL import Image

main = App(title="Py Quiz",width=500,height=500,bg="#F5F5DC")

High_box = Box(main,layout="grid")
quiz_pic = Image.open("img/qz.png")
if quiz_pic.mode == "RGBA":
    quiz_pic.convert("RGB")
quiz_pic.resize(size=(50,50),resample=Image.Resampling.LANCZOS)
Picture(High_box,image=quiz_pic,grid=[0,0],width=50,height=50)
Text(High_box,text="Trắc Nghiệm Python.",size=20,bold=True,grid=[1,0],font="Times New Roman")

Questions =[{"Q":"n = '5 là kiểu dữ liệu nào?","choices":["A. integer","B. string","C. tuple","D. operator"]},
            {"Q":"Lệnh nào dùng để lấy dữ liệu đầu vào từ người dùng?","choices":["A. cin","B. scanf()","C. input()","D. <>"]},
            {"Q":"Kí hiệu nào dùng để xác định các khối lệnh (khối lệnh của hàm, vòng lặp,...) trong Python?","choices":["A. Dấu ngoặc nhọn { }","B. Dấu ngoặc vuông [ ]","C. Thụt lề","D. Dầu ngoặc đơn ( )"]}
]

question = Text(main,size=10,font="Helvetica")



main.display()
