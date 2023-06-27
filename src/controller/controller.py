from src.domain.hash import Hash
from src.view.main_window import MainWindow


class Controller:
    def __init__(self):
        self.main_window = MainWindow()
        self.hash_object = None
        self.connect_events()

    def connect_events(self):
        self.main_window.create_button.clicked.connect(self.create_hash_table)

    def create_hash_table(self):
        self.hash_object = Hash(int(self.main_window.table_size.text()))

    def show_main_window(self):
        self.main_window.show()