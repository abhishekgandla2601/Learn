# two dimensional lists

# a list made up of lists

fruits = ["apple", "banana", "coconut"]
vegetables =["celery", "carrots", "potatoes"]
meats=["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]

#groceries = [["apple", "orange", "banana" "coconut"],
            # ["celery", "carrots", "potatoes"],
            # ["chicken", "fish", "turkey"
# print(groceries[0])
# print(groceries[0][0])
# print(groceries[0][1])
# print(groceries[0][2])
# print()
# print(groceries[1])
# print(groceries[1][0])
# print(groceries[1][1])
# print(groceries[1][2])
# print()
# print(groceries[2])
# print(groceries[2][0])
# print(groceries[2][1])
# print(groceries[2][2])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()