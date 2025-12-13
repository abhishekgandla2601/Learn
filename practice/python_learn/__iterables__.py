# Iterables = An object/collection that can return its elements one at a time,
#               allowing it to be iterated over in a loop
#
# list
# numbers = [1,2,3,4,5]
# for number in reversed(numbers):
#     print(number, end=" - ")

# tuple
# numbers = (1,2,3,4,5)
# for number in numbers:
#     print(number, end=" - ")
#
# print()
#
# # set
# fruits = {"apple", "banana", "cherry"}
#
# for fruit in fruits:
#     print(fruit)

# string
#
# name = "Abhishek"
#
# for character in name:
#     print(character, end=" ")


# dictionary
my_dictionary = {"A":1, "B":2, "C":3}

for key, value in my_dictionary.items():
    print(f"{key}={value}")