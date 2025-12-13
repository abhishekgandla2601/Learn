# Tuples in Python
# Tuples are immutable lists

# we cant change tuple

tup = (1, 5, 6)# tup = (1,) this will be tuple with single element
# tup = (1)# this will be integer
print(type(tup), tup)

# everything is same as list but we cant change it

print(tup[0])# indexing
print(tup[1:3])# slicing
print(tup.index(5))# index of element
print(tup.count(1))# count of element
# tup[0] = 9 this will give error
print(tup)

if 342 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

# tuples are immutable
#lists are mutable