from typing import List, Union


class Hash:
    def __init__(self, size=23):
        self.size = size
        self.hash_table: List[Union[None, dict]] = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert_key(self, key, element):
        address = self.hash_function(key)
        while self.hash_table[address] is not None:
            if address != self.size - 1:
                address = address + 1
            else:
                address = 0
        self.hash_table[address] = {key: element}

    def get_element(self, key):
        index = self.hash_function(key)
        while self.hash_table[index] is not None:
            if self.get_dictionary_key(self.hash_table[index]) == key:
                return self.hash_table[index][key]
            index += 1

        return 'Missing Key'

    @staticmethod
    def get_dictionary_key(dictionary):
        for key, element in dictionary.items():
            return key

    def print_hash_table(self):
        for i in range(len(self.hash_table)):
            print(i, self.hash_table[i])
