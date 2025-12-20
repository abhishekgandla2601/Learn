#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math

# Given points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope calculation
slope = (y2 - y1) / (x2 - x1)

# Euclidean distance calculation
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", slope)
print("Euclidean Distance:", distance)
