#Write a script that prompts the user
# to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter the base of the triangle: \t"))
height = float(input("Enter the height of the triangle: \t"))

area = 0.5 * base * height

print(f"The area of the triangle is: \t \t {area:.2f}")