tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

result = tuple(sorted(tuple1, key=lambda x: x[1]))

print(result)
