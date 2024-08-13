# Bien + nhap xuat du lieu --------------------------------------------
# input: ham return (tra ve) kieu du lieu string
# username = input("Nhap username: ")
# # type casting - chuyen doi kieu du lieu
# age = int(input("NHap tuoi: "))
# # xuat ra console (man hinh) username + age
# print(username + " is " + str(age) + " years old.")

# if - else -----------------------------------
# a = 10
# b = 5
# if (a > b):
#     print("True")
# elif (a + 1 < b):
#     print("else if")
# else:
#     print("False")

# Bieu thuc logic (and, or, not) ------------------
# m = not False
# n = 12
# o = 7

# x = (n > o) and m # True
# y = not (o == n) or m and m # True
# z = y and x or y # True

# Vong lap -------------------------------------------
# viet chuong trinh nhap vao 2 so nguyen duong (a, b),
# xuat ra man hinh tong cua so % 2 trong khoang tu a, b (while)

# Nhap tu ban phim 2 so a, b
a = int(input("Nhap a"))
b = int(input("Nhap b"))
sum = 0
# xet dieu kien (a < b)
while a >= b:
    print("a phai be hon b")
    a = int(input("Nhap a"))
    b = int(input("Nhap b"))
# tao vong lap
i = a
while i < b:
    if i % 2 == 0:
        sum += i
    i += 1

print("Tong tu a den b", sum)

# Danh sach + xau ---------------------------
# Nhap danh sach (cac so cach nhau boi dau ,)
# tinh tong so chia het cho 3

# nhap danh sach duoi dang string
nums = input("Nhap danh sach so: ")  # 1,2,3,4
# cat chuoi thanh danh sach
nums = nums.split(",")  # ["1", "2", "3", "4"]
# chuyen doi du lieu cho cac phan tu trong danh sach nums
# string => int
for i in range(len(nums)):
    nums[i] = int(nums[i])
# => [1, 2, 3, 4]

# tong cac phan tu chia het cho 3
s = 0
for i in range(len(nums)):
    if nums[i] % 3 == 0:  # kiem tra: neu phan tu chia het 3 => cong vao tong s
        s += nums[i]
print("Tong cac phan tu chia het cho 3:", s)

# sum([i for i in nums if i %3 == 0])


# 13/08 ------------------
# Bai1: tong so chan trong danh sach so nguyen
def tong_so_chan(nums):
    sum = 0
    for item in nums:
        if item % 2 == 0:
            sum += item
    return sum


# Bai2: xoa phan tu trung nhau trong danh sach
def xoa_phan_tu_trung(lis):
    for i in range(len(lis) - 1):
        for j in range(i + 1, len(lis)):
            if lis[i] == lis[j]:
                lis.remove(lis[j])
    return lis


# Bai3: kiem tra chuoi doi xung
def kiem_tra_chuoi_doi_xung(string):
    return string[::-1] == string


def kiem_tra_chuoi_doi_xung(string):
    mid = int((len(string) - 1) / 2)
    for i in range(mid + 1):
        for j in range(mid + 1, len(string), -1):
            if string[i] != string[j]:
                return False
    return True
