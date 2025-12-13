num_pad = ((1, 2, 3),
           (1, 5 ,6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()