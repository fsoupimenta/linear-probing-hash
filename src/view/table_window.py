from PyQt6.QtWidgets import *


class TableWindow(QWidget):
    def __init__(self):
        super().__init__(parent=self)
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()
