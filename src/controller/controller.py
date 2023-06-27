from src.domain.hash import Hash
from src.view.main_window import MainWindow
from src.view.table_window import TableWindow


class Controller:
    def __init__(self):
        self.main_window = MainWindow()
        self.table_window = TableWindow()
        self.hash_object = None
        self.connect_events()

    def connect_events(self):
        self.main_window.create_button.clicked.connect(self.create_hash_table)

    def create_hash_table(self):
        self.hash_object = Hash(int(self.main_window.table_size.text()))
        self.table_window.show()
        self.table_window.create_table(self.hash_object.hash_table)

    def show_main_window(self):
        self.main_window.show()
