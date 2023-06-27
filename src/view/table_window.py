from PyQt6.QtWidgets import *


class TableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()

        self.tableWidget = QTableWidget()

        self.set_up_layout()

    def create_table(self, list_):
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(len(list_))
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setHorizontalHeaderLabels(["Index", "Key"])

        for i, element in enumerate(list_):
            self.tableWidget.setCellWidget(i, 0, QLabel(str(i)))
            self.tableWidget.setCellWidget(i, 1, QLabel(str(element)))

        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: black; background-color: gray")
        self.tableWidget.setStyleSheet("background-color: #DCDCDC; color: black;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # self.tableWidget.setMaximumHeight((self.tableWidget.rowHeight(0) * len(self.values_image_t)) - 5)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 150)

    def set_up_layout(self):
        self.setMinimumSize(1000, 500)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
