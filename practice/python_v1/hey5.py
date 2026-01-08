# integer
age = 24
print(age)
print(type(age))
print(id(age))

# floating
a1 = 12.1
print(a1, type(a1), id(a1))

a2 = 3.14e2 # exponential notation for floating point 3.14 * 10^2
print(a2, type(a2), id(a2))

# boolean 

x1 = 100
x2 = 200

res1 = x1 == x2
res2 = x1 != x2
print(res1, res2)
print(x1 is x2)


q1 = input("Enter your name: ")
print("Hello,", q1)