#Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) 
# and 
# perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the lenght of the rectabgle :\t"))
width = float(input("Enter the width of the rectabgle   :\t"))

area = length * width

perimeter = 2* (length + width)

print(f"The area of rectangle is : \t {area:.2f} \nand \nIts perimeter is : \t {perimeter:.2f}")