# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A union of B: ",A.union(B))

# Find A intersection B
print("A intersection B: ",A.intersection(B))

# Is A subset of B
print("Is A subset of B: ", B.issubset(A))

# Are A and B disjoint sets
print(A.isdisjoint(B))
print(B.isdisjoint(A))

# Join A with B and B with A
print("A Union B",A.union(B))
print("B Union A",B.union(A))

# What is the symmetric difference between A and B
print("Symmetric difference between A and B: ",A.symmetric_difference(B))


# Delete the sets completely
del A
del B

print("After using 'del A and del B' Set A and B are deleted")