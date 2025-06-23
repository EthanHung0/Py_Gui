"""Bài 1: Viết một ứng dụng GUI Đếm Bước Chân. Người dùng có thể tăng số bước chân bằng cách nhấn nút, đặt lại số bước chân và đặt mục tiêu.
Yêu cầu:
1. Viết một ứng dụng GUI (Giao diện người dùng đồ họa) sử dụng thư viện GUIZero để đếm số bước chân.
2. Ứng dụng có các chức năng sau:
- Nút "Thêm bước chân" để tăng số bước chân lên mỗi lần bấm.
- Nút "Đặt lại số bước chân" để đặt lại số bước chân về 0.
- Hiển thị số bước chân hiện tại.
- Cho phép người dùng nhập mục tiêu số bước chân vào ô nhập liệu. Khi đạt được mục tiêu, hiển thị thông báo "Chúc mừng!".

Thiết kế giao diện:
1. Giao diện có nền màu nhẹ nhàng và các thành phần được căn giữa.
2. Có một câu nói động viên ở trên cùng.
3. Hai nút chức năng: "Thêm bước chân" và "Đặt lại số bước chân" có màu sắc nổi bật.
4. Giao diện gọn gàng, dễ sử dụng và phù hợp với người dùng.

Yêu cầu cụ thể về thành phần:
1. Sử dụng các thành phần GUI như Text, PushButton, TextBox và Box để bố trí giao diện.
2. Nút "Thêm bước chân" có màu nền xanh lá và nút "Đặt lại số bước chân" có màu đỏ cam.
3. Khi đạt được mục tiêu số bước chân, một thông báo sẽ xuất hiện để chúc mừng người dùng.
4. Người dùng có thể nhập mục tiêu bước chân vào ô nhập liệu, nếu nhập sai (không phải số nguyên), chương trình sẽ hiển thị thông báo lỗi."""

from guizero import *

# MAKE APP
main = App(title="steps",width=500,height=500)
choice_box = Box(main,layout="grid")

#TAKE STEPS + RESET STEPS FUNCTIONS
steps = 0
def takestep():
    global goal
    global steps
    steps += 1
    stepshow.value = f"Steps: {steps}"
    if goal is not None:
        if steps == int(goal):
            main.info("Congrats!","You have reached your goal!")

def resetsteps():
    choice = main.yesno("Reset steps","Are you sure to set your steps to 0?")
    if choice == True:
        global steps
        steps = 0
        stepshow.value = f"Steps: 0"

#SHOW CURRENT STEPS + USE THE FUNCTIONS ABOVE
stepshow = Text(main,text="Steps: 0")
take_a_step = PushButton(choice_box,command=takestep,text="Take a step.",grid=[0,0])
take_a_step.bg = "green"
reset = PushButton(choice_box,command=resetsteps,text="Reset steps",grid=[1,0])
reset.bg = "#FF4500"

#GOAL CHANGING FUNCTION
def goalchange():
    global goal
    newgoal = main.question("Goal Changer","Set your new goal:")
    if newgoal.isdigit() and int(newgoal)>0 and newgoal is not None:
        goal = newgoal
        GOAL.value = f"Goal: {goal}"
    else:
        main.warn("Warning.","Invalid Input. (goal must be a positive integer)")

#GOAL WITH "NONE" AS DEFAULT + GOAL CHANGE BUTTON WITH FUNCTION ABOVE
goal = None
GOAL = Text(main,text="Goal: None")
goal_change = PushButton(main,command=goalchange,text="Change Goal",width=8,height=1)

main.display()