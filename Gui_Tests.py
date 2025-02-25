time = int(input("Nhập số phút gọi trong tháng: "))
while time < 0:
    time = int(input("Nhập số phút gọi trong tháng (Không thể dưới 0): "))

def calculate(t):
    total = 0
    for i in range(t+1):
        if 0 < i <= 100:
            total += 1000
        elif 100 < i <= 300:
            total += 800
        elif i > 300:
            total += 600
    return total

result = calculate(time)
print(f"Số tiền cần thanh toán: {result:,} VND")
