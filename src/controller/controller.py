from src.domain.hash import Hash
from src.view.main_window import MainWindow
from src.view.table_window import TableWindow


class Controller:
    def __init__(self):
        self.main_window = MainWindow()
        self.table_window = TableWindow()
        self.hash_object = Hash()
        self.connect_events()

    def connect_events(self):
        self.main_window.create_button.clicked.connect(self.show_table_window)
        self.table_window.insert_button.clicked.connect(self.insert_element)
        self.table_window.search_button.clicked.connect(self.search_element)

    def insert_element(self):
        address = self.hash_object.insert_key(int(self.table_window.key_input.text()),
                                              self.table_window.element_input.text())
        self.table_window.create_table(self.hash_object.hash_table)
        self.table_window.return_label.setText(f"{self.table_window.element_input.text()} inserted in the {address} "
                                               f"position")

    def search_element(self):
        element, address = self.hash_object.get_element(int(self.table_window.key_input.text()))
        if address is not None:
            self.table_window.return_label.setText(f"{element} was found in the {address} "
                                                   f"position")
        else:
            self.table_window.return_label.setText(f"{element}")

    def show_main_window(self):
        self.main_window.show()

    def show_table_window(self):
        self.table_window.show()
        self.table_window.create_table(self.hash_object.hash_table)
