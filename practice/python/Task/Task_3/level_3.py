#Write a script that prompts
# the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = float(input("Enter side a of the triangle: \t\t"))
side_b = float(input("Enter side b of the triangle: \t\t"))
side_c = float(input("Enter side c of the triangle: \t\t"))

perimeter = side_a + side_b + side_c

print(f"The perimeter of the triangle is: \t{perimeter:.2f}")