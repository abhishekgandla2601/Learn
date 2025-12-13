# operations in tuples

# Manipulating Tuples

#count

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.count(3)
print('Count of 3 in tuple1 is: ', res)

res = tuple1.index(3,4, 8)
print('Count of 3 in tuple1 is:', res)

# tuples are immutable