from PyQt6.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()

        label = QLabel("Size of Hash Table")
        self.layout.addWidget(label)

        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)

        self.button = QPushButton("Create")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    tela = MainWindow()
    tela.show()
    app.exec()
