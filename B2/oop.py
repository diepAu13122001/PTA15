class VatNuoi:
    # khai bao thuoc tinh
    # constructor: khong duoc return => none
    def __init__(self, ten, giong, mausac, tuoi, cannang):
        self.ten = ten
        self.giong = giong
        self.mausac = mausac
        self.tuoi = tuoi
        self.cannang = cannang


vn1 = VatNuoi(ten="Nunu", giong="Golden", 
              mausac="vang nhat", 
              tuoi=10, cannang=15.5)
print(vn1.ten) # Nunu
# thay doi gia tri cua thuoc tinh
vn1.tuoi = 15
print(vn1.tuoi) # 15
print(vn1.__str__())