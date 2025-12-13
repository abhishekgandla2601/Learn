# Exercise 1 Rectangle Area Calc
from django.template.defaultfilters import length

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area is: {area}cm")