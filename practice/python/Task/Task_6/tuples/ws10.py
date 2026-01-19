tuple1 = (45, 45, 45, 45)
print(all(x == 45 for x in tuple1)) # Check if all elements are 45
# how this works: all() returns True if all elements in the iterable are true.
# Here, we use a generator expression to check if each element x in tuple1 is equal to 45.
print(any(x == 45 for x in tuple1)) # Check if any element is 45
# how this works: any() returns True if any element in the iterable is true.