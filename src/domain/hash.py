class Hash:
    def __init__(self, size):
        self.size = size
        self.hash_table = {}

    def insert(self, value):
        address = value % self.size
        self.hash_table[address] = value
