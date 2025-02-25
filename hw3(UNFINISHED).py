from guizero import *

app = App(title="Bill",width=400,height=500)
info = Box(app)
Text(info,text="CÀ PHÊ HUỲNH THÁI",bold=True,size=14)
Text(info,text="Đường số 24 DKC An Khánh, P. An Khánh\nQ. Ninh Kiểu - TP. Cần Thơ",size=10)
Text(info,text="ĐT: 0974.300.007 - 0909.191.195\n",size=10)
Text(info,text="HÓA ĐƠN BÁN HÀNG",size=14,bold=True)
Text(info,text="Bàn 05",size=10,bold=True)

box1 = Box(app,layout="grid")
Text(box1,text="Số: 02190003",size=10,grid=[0,0],align="left")
Text(box1,text="Ngày: 08/02/20925",size=10,grid=[1,0],align="right")
Text(box1,text="Thu Ngân: Nguyễn Minh Hùng",size=10,grid=[0,1,2,1],align="left")
Text(box1,text="Giờ vào: 1:41",size=10,grid=[0,2],align="left")
Text(box1,text="In lúc: 3:41",size=10,grid=[1,2],align="right")

box2 = Box(app,layout="grid")
Text(box2,text="Mặt hàng",size=10,bold=True,grid=[0,0])
Text(box2,text="Số lượng",size=10,bold=True,grid=[1,0])
Text(box2,text="Gíá",size=10,bold=True,grid=[2,0])
Text(box2,text="Thành tiền",size=10,bold=True,grid=[3,0])

Text(box2,text="Tổng",size=14,bold=True)

app.display()

#UNFINISHED