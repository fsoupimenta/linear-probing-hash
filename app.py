from src.domain.hash import Hash

values = {452: 'A', 623: 'B', 766: 'C', 564: 'D', 825: 'E', 387: 'F', 237: 'G', 360: 'H', 134: 'I', 285: 'J'}
hash_object = Hash(23)

for key, element in values.items():
    hash_object.insert_key(key, element)

hash_object.print_hash_table()
print(hash_object.get_element(134))
