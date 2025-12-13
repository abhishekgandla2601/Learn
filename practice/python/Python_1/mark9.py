# string slicing

# length of a string
# We can find the length of a string using len() function

string = "Abhishek,Gandla"
# 0 start

#string[start : end]
print(string[0:4])
print(len(string))
print(string[0:15])
print(string[:15])# if not given in start position default will be 0

#negative slicing

print(string[0 :-3])
print(string[-1 :-3])

fruit = 'Mango'

mangolen = len(fruit)

print(mangolen)

print(fruit[0 : 4]) # including 0 but not 4

print(fruit[ :5])

print(fruit[0 : -3])

print(fruit[:len(fruit)-3])

print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])

#Question:

# nm = 'Harry'

# print(nm[-4 : -2])

nm = 'Harry'
#len(nm) - 4 = H
#len(nm) -2 = ar -- Harry-2 = Harr --ar
print(nm[-4 : -2])