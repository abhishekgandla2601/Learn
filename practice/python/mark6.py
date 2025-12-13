#Typecasting::

#The conversion of one datatype into another 
# datatype is known as type casting in python.

# a = "1" #string
# b = "2"#string
a = 1 
b=2
print(a+b)

#python supports a wide variety of functions or methods like:
# str(),ord(),hex(),oct(),set(),tuple(),list(),dict(),etc. 

# Two types of typecasting:

#1.Explict Conversion(Explict type casting in python) - wanted conversion
#2.Implicit Conversion(Implict type casting in python) - automatic conversion

a = "1"

b = "2"

print(int(a)+int(b))

string = "15"
number = 7

string_number = int(string)

sum = number + string_number

print("The sum of both the numbers is:", sum)


#implicit type casting

c = 1.9

d = 8

print(c+d)#float - int  float - float - float

print(type(c+d))

