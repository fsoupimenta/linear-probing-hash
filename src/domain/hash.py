from typing import List, Union

from src.domain.utils import get_dictionary_key


class Hash:
    def __init__(self, size=23):
        self.size = size
        self.table_size = 0
        self.hash_table: List[Union[None, dict]] = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert_key(self, key, element):
        address = self.hash_function(key)
        if self.table_size != self.size:
            while self.hash_table[address] is not None:
                address = self.hash_function(address + 1)

            self.hash_table[address] = {key: element}
            self.table_size = self.table_size + 1

            return address

        return 'Full List'

    def get_element(self, key):
        index = self.hash_function(key)
        while self.hash_table[index] is not None:
            if get_dictionary_key(self.hash_table[index]) == key:
                return self.hash_table[index][key], index
            index += 1

        return 'Missing Key', None

    def print_hash_table(self):
        for i in range(len(self.hash_table)):
            print(i, self.hash_table[i])
