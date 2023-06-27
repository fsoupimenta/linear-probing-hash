from src.domain.hash import Hash

values = [452, 623, 766, 564, 825, 387, 237, 360, 134, 285]
hash_object = Hash(23)

for i in range(0, len(values)):
    hash_object.insert(values[i])

print(hash_object.hash_table)
