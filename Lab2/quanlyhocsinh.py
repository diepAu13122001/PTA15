class QuanLyDiemHS:
    def __init__(self, hoten, lop, truong, diemtoan, diemvan, diemanh):
        self.hoten = hoten
        self.lop = lop
        self.truong = truong
        self.diemtoan = diemtoan
        self.diemvan = diemvan
        self.diemanh = diemanh

    def tinhDiemTrungBinh(self):
        return sum([self.diemanh, self.diemtoan, self.diemvan]) / 3


# tao cac object cho lop
st1 = QuanLyDiemHS("Nguyen Van A", "9A", "ABC", 10, 6, 9.5)
st2 = QuanLyDiemHS("Nguyen Van B", "9B", "ABC", 5, 9, 9.5)
st3 = QuanLyDiemHS("Nguyen Van C", "9C", "ABC", 0, 4, 6.5)
st4 = QuanLyDiemHS("Nguyen Van D", "9D", "ABC", 10, 6, 9.5)

# danh sach chua cac obj => loc qua danh sach => kiem max
st_list = [st1, st2, st3, st4]
max_dtb = st1.tinhDiemTrungBinh()
#  duyet danh sach => kiem max
for i in st_list:
    max_dtb = max(max_dtb, i.tinhDiemTrungBinh())

print("Danh sach hoc sinh co diem tb cao nhat:", max_dtb)
# duyet danh sach => in ra man hinh ket qua
for i in st_list:
    if(max_dtb == i.tinhDiemTrungBinh()):
        print(i.hoten)

