class BankAccount:
    # phuong thuc khoi tao
    def __init__(self, bank_name, account_name, account_number, amount):
        self.bank_name = bank_name
        self.account_name = account_name
        self.account_number = account_number
        self.amount = amount

    # phuong thuc rut tien
    def rut_tien(self, so_tien_can_rut):
        if self.amount > so_tien_can_rut:
            # neu lon hon => duoc rut tien
            # self.amount = self.amount - so_tien_can_rut
            self.amount -= so_tien_can_rut
            print("Rut thanh cong, so tien hien tai la:", self.amount)
        else:
            print("So du cua tai khoan khong du!")

    # phuong thuc nap tien
    def nap_tien(self, so_tien_can_nap):
        # self.amount = self.amount + so_tien_can_nap
        self.amount += so_tien_can_nap
        print("Nap thanh cong, so tien hien tai la:", self.amount)


account_1 = BankAccount(  bank_name="BIDV", 
    account_number=1234567890, 
    account_name="AU NGOC DIEP", 
    amount=100000
)
account_1.rut_tien(12345)
account_1.nap_tien(456789)