# find an Euclidean distance between (2,3) and (10,8)

p1 = float(input("Enter x1 coordinate: "))
p2 = float(input("Enter y1 coordinate: "))

q1 = float(input("Enter x2 coordinate: "))
q2 = float(input("Enter y2 coordinate: "))

result = (((p1 - q1)**2 + (p2 - q2)**2))

result = result ** 0.5

print("Euclidean distance is:", result)
