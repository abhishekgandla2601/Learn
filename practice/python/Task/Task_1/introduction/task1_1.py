# Checking the version of python
import sys
print(sys.version)

# arithmetic operations
a = 3
b = 4

print("Addition value : ", a + b)
print("Subtraction value : ", a - b)
print("Multiplication value : ", a * b)
print("Division value : ", a / b)
print("Floor Division value : ", a // b)
print("Modulus value : ", a % b)
print("Exponentiation value : ", a ** b)

# writing strings in python

myname = "Abhishek"
familyname = "Gandla"
country = "India"

print("My name is: \t", myname, 
      "\n My family name is: \t", familyname, 
      "\n I love my country: \t", country)

# checking data types
print("The data type of '10' is: \t", type(10))
print("The data type of '9.8' is: \t", type(9.8))
print("The data type of '3.14' is: \t", type(3.14))
print("The data type of '3 + 4j' is: \t", type(3 + 4j))
print(type(['Abhishek', 'Python', 'India']))
print("The data type of myname is: \t", type(myname))
print("The data type of familyname is: \t", type(familyname))
print("The data type of country is: \t", type(country))