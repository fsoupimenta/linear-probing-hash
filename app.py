import sys
from PyQt6.QtWidgets import QApplication
from src.controller.controller import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()

    controller.show_main_window()

    app.exec()
