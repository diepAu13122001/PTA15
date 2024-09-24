import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.countNum = 0
        self.renderUi()
        self.show()

    def renderUi(self):
        # thay doi ten cho window title
        self.setWindowTitle("Click Me: Diep")
        # cai dat size cho cua so
        self.setGeometry(200, 200, 800, 500)
        # add button
        self.setCentralWidget(self.createButton())

    def createButton(self):
        # tao button
        button = QPushButton("Press me")
        # thay doi trang thai (da bam)
        button.setCheckable(False)
        # bat su kien cho button
        button.clicked.connect(self.counter)
        return button

    def counter(self):
        self.countNum += 1
        print("clicked", self.countNum)


if __name__ == "__main__":
    # chi chay code khi mo file nay + run tai file goc
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
