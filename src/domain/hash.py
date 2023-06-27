from array import array


class Hash:
    def __init__(self, size):
        self.size = size
        self.hash_table = array('i', [0] * size)

    def insert(self, value):
        address = value % self.size
        while self.hash_table[address] != 0:
            if address != self.size - 1:
                address = address + 1
            else:
                address = 0
        self.hash_table[address] = value

    def get_element(self, element):
        index = element % self.size
        while self.hash_table[index] != 0:
            if self.hash_table[index] == element:
                return index + 1
            index += 1

        return False

    def print_hash_table(self):
        for i in range(len(self.hash_table)):
            print(i, self.hash_table[i])
