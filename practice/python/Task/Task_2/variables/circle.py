'''
The radius of a circle is 30 meters.
    (i) Calculate the area of a circle and assign the value to a variable name of area_of_circle
    (ii) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    (iii)Take radius as user input and calculate the area.

'''

radius = 30 # radius of the circle in meters
PI = 3.14
# (i) Calculate the area of a circle
area_of_circle = PI * radius**2
print("Area of the circle is :", area_of_circle, "square meters")

# (ii) Calculate the circumference of a circle
circum_of_circle = 2 * PI * radius
print("Circumference of the circle is :", circum_of_circle, "meters")

# (iii)Take radius as user input and calculate the area.
user_radius = float(input("Enter the radius of the circle in meters: "))
PI = 3.14
user_area_of_circle = PI * user_radius**2
print("Area of the circle with radius", user_radius, "meters is :", user_area_of_circle, "square meters")