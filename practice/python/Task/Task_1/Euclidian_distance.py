# find an Euclidean distance between (2,3) and (10,8)

p1 = float(input("Enter x1 coordinate: "))
p2 = float(input("Enter x2 coordinate: "))

q1 = float(input("Enter y1 coordinate: "))
q2 = float(input("Enter y2 coordinate: "))

result = (((p1 - q1)**2 + (p2 - q2)**2))

result = result ** 0.5

print("Euclidean distance of (p1, p2) and (q1, q2): ", result)


# also can be written as: 
'''
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))

x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Euclidean distance is:", distance)

'''