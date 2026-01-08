# list
l1 = eval(input("Enter the list data: "))

print(l1)

print(type(l1))
# insertion is preserved(Input== Output)
for a1 in l1:
    print(a1)

# duplication is allowed
l2 = [10, 20, 30, 10, 20, 30]
print(l2)

# hetrogenious objects are allowed, means different data types
# in a single list
l3 = [10, 20.5, "Hello", True, 30+5j]
print(l3)
for q in l3: 
    print(q)
    
# mutable
l1 = ['a', 'b', 'c']
print(l1)
l1[0] = "A"
print(l1)