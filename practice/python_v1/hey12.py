# set is mutable object
s1 = {'A','B','C','D','E','F','G','H','I'}

print(s1)

# set is a dynamic or growable

s2 =set()
print(s1)
s2.add(1001)
print(s2)
s2.add(1002)
print(s2)

s2.remove(1001)
print(s2)