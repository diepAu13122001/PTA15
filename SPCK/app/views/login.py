from PyQt6.QtWidgets import QApplication, QMainWindow
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
        print("Hello")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
