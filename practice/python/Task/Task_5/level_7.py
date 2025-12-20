# Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

s = sum(ages)
print(s)

print(len(ages))

print(s//(len(ages)))

# Find the range of the ages (max minus min)

print("Differece of max minus min: " ,max(ages) - min(ages))

# Compare the value of (min - average) and (max - average), use abs() method
print("(min - average): ",abs(min(ages) - s//(len(ages))))
print("(max - average): ",abs(max(ages) - s//(len(ages))))