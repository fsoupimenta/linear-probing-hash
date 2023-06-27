from PyQt6.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Size of Hash Table"))

        self.table_size = QLineEdit()
        self.layout.addWidget(self.table_size)

        self.create_button = QPushButton("Create")
        self.layout.addWidget(self.create_button)

        self.setLayout(self.layout)
