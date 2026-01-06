# adding items to a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

# inserting items to a list
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2,"apple")
print(fruits)
fruits.insert(3, "lime")
print(fruits)

# removing items using pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# removing items using del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
# del fruits 
# print(fruits)

# clearing list items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# copying a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# joining lists
# plus operator

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# joining using extend()
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers:", num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers:", negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print("Fruits and vegetables:", fruits)

# counting items in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# finding index of an item in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

# reversing a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 26, 25, 24, 19, 22]
ages.reverse()
print(ages)

# sorting lists items

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print("sort")
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

# sorted() : returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print("sorted")
print(sorted(fruits))

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)