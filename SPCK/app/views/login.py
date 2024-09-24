from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import os


# tao class de chua giao dien Login
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        # ket noi giao dien voi code
        self.ui = uic.loadUi("SPCK/app/ui/login.ui", self)

        # bat su kien cho button
        self.ui.login_btn.clicked.connect(self.login)

    def login(self):
        self.validateForm("abc@gmail.com", "123456")

    def validateForm(self, emailToCheck, passwordToCheck):
        # get data from input
        email_input = self.ui.email_input.text()
        password_input = self.ui.password_input.text()
        # create message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Form validation error!")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        # validate
        if not email_input or not password_input:
            # khong nhap du du lieu
            msg_box.setText("Please fill all fields in form")
            msg_box.exec()
            return False
        elif email_input != emailToCheck:
            # email khong chinh xac
            msg_box.setText("Email is not correct")
            msg_box.exec()
            return False
        elif len(password_input) < 6:
            # password phai co tren 6 chu so
            msg_box.setText("Password is least at 6 letters")
            msg_box.exec()
            return False
        elif password_input != passwordToCheck:
            # mat khau k chinh xac
            msg_box.setText("Password is not correct")
            msg_box.exec()
            return False
        else:
            return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
