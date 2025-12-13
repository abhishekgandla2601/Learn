#Arithmetic Operators

'''
Addition(+)
Subtraction(-)
Multiplication(*)
Division(/)
Floor Division(//)
Modulus(%)
Exponentiation(**)
'''
print(56+689)#Addition
print(689-56)#Subtraction
print(56*689)#Multiplication
print(689/56)#Division
print(689//56)#Floor Division
print(689%56)#Modulus
print(56**3)#Exponentiation

#Exercise 1

# Create a calculator

# capable of performing
# addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print('Addition:',a+b)
print('Subtraction:',a-b)
print('Multiplication:',a*b)
print('Division:',a/b)
print('Floor Division:',a//b)
print('Modulus:',a%b)
print('Exponentiation:',a**b)
#End of Exercise 1

#solution:
a = 25

b = 3

print("The value of", a, "+", b, "is", a + b)
print("The value of", a, "-", b, "is", a - b)
print("The value of", a, "*", b, "is", a * b)
print("The value of", a, "/", b, "is", a / b)
print("The value of", a, "//", b, "is", a // b)
print("The value of", a, "%", b, "is", a % b)
print("The value of", a, "**", b, "is", a ** b)
#End of solution