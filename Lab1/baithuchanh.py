# nguoi dung nhap vao chuoi hh:mm:ss
user_input = input("Nhap thoi gian (hh:mm:ss): ")
# cat chuoi thanh 3 bien hour, min, sec
user_input = user_input.split(":")
# truong hop ngoai le -----------------------------
isFault = True
while isFault:
    # 1. thieu thanh phan
    if len(user_input) < 3:
        user_input = input("Nhap lai thoi gian (hh:mm:ss): ")
        user_input = user_input.split(":")
    else:
        isFault = False

# quy dinh bien hour, min, sec
hour = int(user_input[0])
min = int(user_input[1])
sec = int(user_input[2])


# xay dung ham kiem tra
def checkTime(hour, min, sec):
    # 2. hour [0,23]
    if not (0 <= hour <= 23):
        return False
    # 3. min [0,59]
    elif not (0 <= min <= 59):
        return False
    # 4. sec [0,59]
    elif not (0 <= sec <= 59):
        return False
    return True

# in ra hop le neu ham tra ve true
if checkTime(hour=hour, min=min, sec=sec):
    print("Hop le!")
else:
    print("Khong hop le")
