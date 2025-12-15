# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) 
# and 
# circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input("Enter the radius of the circle :\t"))
PI = 3.14

area = PI * radius **2

circumference = 2 * PI * radius

print(f"The area of circle is : \t {area:.2f} \nand \nIts circumference is : \t {circumference:.2f}")