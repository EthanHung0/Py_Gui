# a) Dùng thư viện random tạo một danh sách gồm 10 số nguyên ngẫu nhiên trong khoảng từ 1 đến 1000. In danh sách vừa tạo ra màn hình.
from random import *
def random_10():
    rand10 = []
    for i in range(10):
        rand10.append(randint(1,1000))
    return rand10
a = random_10()
print(a)

# b) Kiểm tra số nguyên tố trong danh sách vừa tạo ở câu a. In kết quả kiểm tra ra màn hình
def check(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_check(rlist):
    prime = []
    for i in rlist:
        if check(i):
            prime.append(i)
    return prime
b = prime_check(a)
print(b)

# c) Sắp xếp danh sách số nguyên tố tìm được ở câu b theo thứ tự giảm dần. In kết quả ra màn hình
c = sorted(b,reverse=True)
print(c)

# d) Tính tổng các số nguyên tố trong danh sách ở câu b. In kết quả ra màn hình

def list_sum(tlist):
    results = 0
    for i in tlist:
        results += i
    return results
d = list_sum(c)
print(d)

# e) Lọc ra các số chẵn từ danh sách đã tạo ở câu a. In kết quả ra màn hình12   QQ

