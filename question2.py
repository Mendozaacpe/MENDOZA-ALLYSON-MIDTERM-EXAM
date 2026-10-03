import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "Special Midterm Exam in OOP"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 600, 400)

        self.button = QPushButton("Click to Change Color", self)
        self.button.setGeometry(200, 170, 200, 50)
        self.button.clicked.connect(self.colors)
        self.show()

    def colors(self):
        self.button.setStyleSheet("background-color: yellow")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec()) 
