import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class App(QWidget):
    def __init__(self):
            super().__init__()
    
            self.title = "Midterm in OOP"
            self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200, 100, 600, 350)
    
        self.label = QLabel("Enter your fullname:", self)
        self.label.setGeometry(50, 120, 140, 25)
        self.label.setStyleSheet("color: red;")
               
        self.inputBox = QLineEdit(self)
        self.inputBox.setGeometry(300, 115, 220, 30)
             
        self.button = QPushButton("Click to display your Fullname", self)
        self.button.setGeometry(50, 165, 160, 30)
        self.button.setStyleSheet("color: red;")
               
        self.outputBox = QLineEdit(self)
        self.outputBox.setGeometry(300, 165, 220, 30)
               
        self.button.clicked.connect(self.display)
        self.show()

    def display(self):
        fullname = self.inputBox.text()
        self.outputBox.setText(fullname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
