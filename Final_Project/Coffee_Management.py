from pathlib import Path
from guizero import *
from PIL import Image,ImageGrab
import datetime
import random
import os

BASE_DIR = Path(__file__).parent

Main = App(title="Hui Cafe P.O.S system",width=1000,height=600,bg="#F8F4E1")

def Switch1(): #Open up Order Menu
    Menu.hide()
    OrderMenu.show()
    load_ids()

def Switch2(): #Open up Pay Menu
    Menu.hide()
    HistoryMenu.show()
    load_ids()
    History_ListBox.clear()
    for i in Receipt_IDs:
        History_ListBox.append(i)
    # print(Receipt_IDs)

def Back(): #Return to Main Menu
    OrderMenu.hide()
    HistoryMenu.hide()
    Menu.show()

#=============================================================================================================
Items = { #Items
    1:["Espresso",4.2,BASE_DIR / "items/espresso.png",0],
    2:["Cappucchino",3.3,BASE_DIR / "items/cappucchino.png",0],
    3:["Latte",4.0,BASE_DIR / "items/latte.png",0],
    4:["Americano",4.0,BASE_DIR / "items/americano.png",0],
    5:["Iced Coffee Milk",3.8,BASE_DIR / "items/icedcoffeemilk.png",0],
    6:["Cold Brew",4.0,BASE_DIR / "items/coldbrew.png",0],
    7:["Salted Caramel",4.2,BASE_DIR / "items/saltedcaramel.png",0],
    8:["Peppermint Tea",4.0,BASE_DIR / "items/pepperminttea.png",0],
    9:["Orange Juice",3.0,BASE_DIR / "items/orangejuice.png",0],
    10:["Blue Ocean Soda",4.0,BASE_DIR /"items/blueoceansoda.png",0] #Honorable mention
    }
#=============================================================================================================
Menu = Box(Main,width="fill",height="fill") #Main Menu

lg = Image.open(str(BASE_DIR / 'TransaprentLogo.png')) # Logo hex: #264F10
if lg.mode == "RGBA":
    lg.convert("RGB")
resized_logo1 = lg.resize((300,300),resample=Image.Resampling.LANCZOS)
Menu_Logo = Picture(Menu,image=resized_logo1)

options = Box(Menu,layout="grid") #Grid box below logo with 2 PushButtons to toggle Menus
Order = PushButton(options,text="Order",width=15,height=3,command=Switch1,grid=[0,0]) #Order Menu Button
Order.text_bold = True
Order.bg = "#E3DCC4"
Order.text_color = "#264F10"
History = PushButton(options,text="Transaction\nHistory",width=15,height=3,command=Switch2,grid=[1,0]) #Pay Menu Button
History.text_bold = True
History.bg = "#E3DCC4"
History.text_color = "#264F10"

#=============================================================================================================
OrderMenu = Box(Main,width="fill",height="fill",layout="grid",visible=False) #Order Menu

lg_box = Box(OrderMenu,layout="grid",align="left",grid=[0,0])
lg_wordmark = Image.open(str(BASE_DIR / "TransaprentWordmarkLogo.png"))
resized_wordmark = lg_wordmark.resize((165,65),resample=Image.Resampling.LANCZOS)
Order_wordmark = Picture(lg_box,image=resized_wordmark,grid=[0,0]) #Wordmark

Order_back = PushButton(lg_box,text="Back To Menu",command=Back,grid=[1,0]) #Back to Main Menu button
Order_back.text_bold = True
Order_back.bg = "#E3DCC4"
Order_back.text_color = "#264F10"

#-----------------------------------------------------------------------------------
OrderMainBox = Box(OrderMenu,layout="grid",height=500,width=700,grid=[0,1]) #box where items are shown
OrderMainBox.set_border(thickness=2,color="#E3DCC4")

def ITEMTXT(a,b):
    Text(a,text=Items[b][0],size=10,grid=[0,0])
    Text(a,text=f"{Items[b][1]}$",size=8,grid=[0,1])

def Cost():
    Total = 0
    for i in range(1,11):
        item_price = Items[i][1]
        item_quantity = Items[i][3]
        Total += item_price*item_quantity
    return round(Total,2)

def show_Cost(cost):
    PlaceOrder.text = f"Place Order {cost}$"

def ITEMORDER(a):
    item_name = Items[a][0]
    item_price = Items[a][1]
    if item_name in Selected_Item:
        old = Items[a][3]
        Items[a][3] += 1
        # print(Items[a][3])
        SelectListbox.remove(f"{item_name} - {item_price}$ - {old}")
        SelectListbox.append(f"{item_name} - {item_price}$ - {Items[a][3]}")
    else:
        Items[a][3] += 1
        SelectListbox.append(f"{item_name} - {item_price}$ - {Items[a][3]}")
        Selected_Item.append(Items[a][0])
    # print(Selected_Item)
    global TotalCost
    TotalCost = Cost()
    show_Cost(Cost())

def CLEARSELECTION():
    SelectListbox.clear()
    Selected_Item.clear()
    for i in range(1,11):
        Items[i][3] = 0
    global TotalCost
    TotalCost = 0
    show_Cost(TotalCost)

def ITEM(itemx,itemy,IID):
        itemgrid = [itemx,itemy]
        item = Box(OrderMainBox,width=175,height=166,grid=itemgrid)
        item.set_border(1,color="#264F10")
        if IID in [5,7,9]:
            Picture(item,str(Items[IID][2]),width=120,height=120)
        else:
            Picture(item,str(Items[IID][2]),width=140,height=120)
        item_info = Box(item,layout="grid")
        Text(item_info,text=Items[IID][0],size=10,grid=[0,0])
        Text(item_info,text=f"{Items[IID][1]}$",size=8,grid=[0,1])
        item_order = PushButton(item_info,text="ADD",width=2,height=1,command=ITEMORDER,args=[IID],grid=[1,0,1,2])
        item_order.text_bold = 1
        item_order.bg = "#E3DCC4"

ItemID = 1
for y in range(0,3):
    for x in range(0,4):
        if ItemID <= len(Items):
            ITEM(x,y,ItemID)
            ItemID += 1

#-----------------------------------------------------------------------------------

def R_item(box,y,index,id):
    idindex = id[index]
    Text(box,text=f"{Items[idindex][0]}",size=10,align="left",grid=[0,y])
    Text(box,text=f"{Items[idindex][3]}",size=10,align="center",grid=[1,y])
    Text(box,text=f"{Items[idindex][1]}$",size=10,align="center",grid=[2,y])
    Text(box,text=f"{Items[idindex][1]*Items[idindex][3]:.1f}$",size=10,align="right",grid=[3,y])

def capture_window(id):
    x = Main.tk.winfo_rootx()
    y = Main.tk.winfo_rooty()
    width = x + Main.tk.winfo_width()
    height = y + Main.tk.winfo_height()
    img = ImageGrab.grab(bbox=(x, y, width, height))
    img.save(str(BASE_DIR / f"receipts/{id}.png"))
    print("Saved!")

Receipt_IDs = []

def load_ids():
    Receipt_IDs.clear()
    if not os.path.exists(str(BASE_DIR /"ReceiptIDsFile.txt")):
        return
    with open(str(BASE_DIR /"ReceiptIDsFile.txt"), "r") as fil:
        for line in fil:
            Receipt_IDs.append(line.strip())
def save_ids():
    lines = [f"{i}\n" for i in Receipt_IDs]
    with open(str(BASE_DIR /"ReceiptIDsFile.txt"),"w") as fil:
        fil.writelines(lines)

def generate_id():
    return "".join(random.choices("0123456789", k=8))
def id_check():
    load_ids()
    while True:
        new_id = generate_id()
        if new_id not in Receipt_IDs:
            Receipt_IDs.append(new_id)
            print(Receipt_IDs)
            return new_id


def RECEIPT():
    currentDT = datetime.datetime.now()
    checkOut = currentDT.strftime("%H:%M")
    date = currentDT.strftime("%d/%m/%Y")
    if not Cus_Name.value:
        if yesno("Empty Name","Leave Customer's Name blank? (replaced with 'Customer')"):
            Cus_Name.value = "Customer"
    else:
        receipt = Box(Main,width="fill",height="fill",visible=False)
        receipt.bg = "white"
        info = Box(receipt)
        Text(info,text="HUI CAFE",bold=True,size=14)
        Text(info,text="Road No.24 KDC An Khánh, An Khánh Ward\nNinh Kiểu District - Cần Thơ City",size=10)
        Text(info,text="Phone: 0974.300.007 - 0909.191.195\n",size=10)
        Text(info,text="PURCHASE RECEIPT",size=14,bold=True)
        Text(info,text=f"Table {Cus_Table.value}\n",size=10,bold=True)

        receipt_id = id_check()
        box1 = Box(receipt,layout="grid")
        Text(box1,text=f"ID: {receipt_id}",size=10,grid=[0,0],align="left")
        Text(box1,text=f"Date: {date}",size=10,align="right",grid=[1,0])
        Text(box1,text="Cashier: Nguyễn Minh Hùng",size=10,grid=[0,1,2,1],align="left")
        Text(box1,text=f"Customer: {Cus_Name.value}",size=10,align="left",grid=[0,2])
        Text(box1,text=f"CheckOut: {checkOut}",size=10,align="left",grid=[0,3])

        box2 = Box(receipt,layout="grid")
        Text(box2,text="Items",bold=1,size=10,grid=[0,0])
        Text(box2,text="Quantity",bold=1,size=10,grid=[1,0])
        Text(box2,text="Price",bold=1,size=10,grid=[2,0])
        Text(box2,text="Total",bold=1,size=10,grid=[3,0])
        OrderedItems = []

        for i in Items:
            if Items[i][3]:
                OrderedItems.append(i)
        indx = 0
        for y in range(1,len(OrderedItems)+1):
            if indx < len(OrderedItems):
                R_item(box2,y,indx,OrderedItems)
                indx += 1

        box3 = Box(receipt, layout="grid", align="top")
        Text(box3, text="Total", size=14, grid=[0,0], align="left", bold=True)
        Text(box3, text="             ", size=14, grid=[1,0])
        Text(box3, text="             ", size=14, grid=[2,0])
        Text(box3, text=f"{TotalCost}$", size=14, grid=[3,0], align="right", bold=True)

        Text(receipt,text="\nThank you. See you again!", align="top", size=10, italic=True)

        def r_exit():
            receipt.hide()
            OrderMenu.show()
            Receipt_IDs.pop()
        def r_save():
            buttons.hide()
            save_ids()
            Main.update()
            capture_window(receipt_id)
            Cus_Name.clear()
            Cus_Table.select_default()
            CLEARSELECTION()
            r_exit()
        buttons = Box(receipt,layout="grid")
        PushButton(buttons,text="EXIT",command=r_exit,grid=[0,0])
        PushButton(buttons,text="SAVE",command=r_save,grid=[1,0])

        OrderMenu.hide()
        receipt.show()


ReceiptMainBox = Box(OrderMenu,width=300,height=500,grid=[1,1]) #Receipt section box where the order is taken
ReceiptMainBox.set_border(thickness=2,color="#E3DCC4")
Text(ReceiptMainBox,text="Purchase Receipt",size=15,color="#264F10")

CusInfoBox = Box(ReceiptMainBox,layout="grid",width=300,height=60) #Box for customer's Info
Text(CusInfoBox,text="Customer name",size=10,grid=[0,0])
Cus_Name = TextBox(CusInfoBox,width=30,grid=[0,1]) #Customer's Name TextBox
Cus_Name.text_size = 10
Cus_Name.bg = "white"
Text(CusInfoBox,text="Table",size=10,grid=[1,0])
Cus_Table = Combo(CusInfoBox,width=7,options=["A1","A2","A3","A4"],selected="A1",grid=[1,1]) #Customer's Table Combo
Cus_Table.bg = "#E3DCC4"
Cus_Table.text_color = "#264F10"
Cus_Table.text_bold = True

OrderInfoBox = Box(ReceiptMainBox,layout="grid",width=300,height=350)
Text(OrderInfoBox,text="Order list",color="#264F10",size=12,align="left",grid=[0,2])
Clear = PushButton(OrderInfoBox,text="Clear Selection",command=CLEARSELECTION,height=1,width=10,grid=[1,2])
Clear.bg = "#E3DCC4"
SelectListbox = ListBox(OrderInfoBox,scrollbar=True,width=300,height=350,grid=[0,3,2,1])
SelectListbox.text_size = 12

TotalCost = Cost()
Selected_Item = []

Pay_Order = Box(ReceiptMainBox,layout="grid")
PlaceOrder = PushButton(Pay_Order,text="Place Order  0$",width=25,command=RECEIPT,grid=[0,0])
PlaceOrder.bg = "#549A2E"
PlaceOrder.text_bold = 1
#=============================================================================================================
HistoryMenu = Box(Main,width="fill",height="fill",layout="grid",visible=False) #Transaction history

lg_box2 = Box(HistoryMenu,layout="grid",align="left",grid=[0,0])
Picture(lg_box2,image=resized_wordmark,grid=[0,0]) #Wordmark

History_back = PushButton(lg_box2,text="Back To Menu",command=Back,grid=[1,0]) #Back to Main Menu button
History_back.text_bold = True
History_back.bg = "#E3DCC4"
History_back.text_color = "#264F10"

#-----------------------------------------------------------------------------------

HistoryMainBox = Box(HistoryMenu,layout="grid",width=1000,height=500,grid=[0,1])
History_txt = Text(HistoryMainBox,text="Transaction History",size=20,align="left",grid=[0,0])
History_txt.font = "Helvetica"

def OpenReceipt():
    if History_ListBox.value:
        path = str(BASE_DIR / f"receipts/{History_ListBox.value}.png")
        img = Image.open(path)
        img.show()

def clearHistory():
    if yesno("ClearHistory","Clear Transaction History?"):
        if yesno("Confirmation","Are you sure? (This action cannot be undone.)"):
            History_ListBox.clear()
            Receipt_IDs.clear()
            with open(str(BASE_DIR / "ReceiptIDsFile.txt"),mode="w") as fil:
                fil.write("")
            for f in os.listdir(str(BASE_DIR / "receipts")):
                file_path = os.path.join(str(BASE_DIR / "receipts"),f)
                os.remove(file_path)

History_ListBox = ListBox(HistoryMainBox,command=OpenReceipt,width=1000,height=400,scrollbar=True,grid=[0,1,2,1])
History_ListBox.bg = "white"
History_Clear = PushButton(HistoryMainBox,text="Clear History",command=clearHistory,grid=[0,0])
History_Clear.bg = "#E3DCC4"
History_Clear.text_bold = True
History_Clear.text_color = "#C83535"

#=============================================================================================================
Main.display()